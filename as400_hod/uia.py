"""Minimal UI Automation screen-text reader via ctypes COM (no comtypes)."""

from __future__ import annotations

import ctypes
from ctypes import wintypes
from typing import List, Optional

from as400_hod import win32_api as w32

# Property IDs
UIA_NamePropertyId = 30005
UIA_ValueValuePropertyId = 30045

# COM
COINIT_APARTMENTTHREADED = 0x2
CLSCTX_INPROC_SERVER = 0x1


class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8),
    ]

    def __init__(self, guid_str: str):
        super().__init__()
        # Accept "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}"
        g = guid_str.strip("{}").split("-")
        self.Data1 = int(g[0], 16)
        self.Data2 = int(g[1], 16)
        self.Data3 = int(g[2], 16)
        # Data4 is 8 bytes from hex pairs of last two groups
        hexbytes = bytes.fromhex(g[3] + g[4])
        for i, b in enumerate(hexbytes):
            self.Data4[i] = b


CLSID_CUIAutomation = GUID("{FF48DBA4-60EF-4201-AA87-54103EEF594E}")
IID_IUIAutomation = GUID("{30CBE57D-D9D0-452A-AB13-7AC5AC4825EE}")
IID_IUIAutomationElement = GUID("{D22108EE-33EE-44B7-9E3F-5A773F826F09}")
IID_IUIAutomationCondition = GUID("{352FFBA8-0973-437C-A61F-F64CAFD81DF9}")
IID_IUIAutomationElementArray = GUID("{14314595-B4BC-4055-95F2-58F2E42C9855}")

ole32 = ctypes.WinDLL("ole32", use_last_error=True)
oleaut32 = ctypes.WinDLL("oleaut32", use_last_error=True)

ole32.CoCreateInstance.argtypes = [
    ctypes.POINTER(GUID),
    wintypes.LPVOID,
    wintypes.DWORD,
    ctypes.POINTER(GUID),
    ctypes.POINTER(ctypes.c_void_p),
]
ole32.CoCreateInstance.restype = ctypes.HRESULT

oleaut32.VariantInit.argtypes = [ctypes.c_void_p]
oleaut32.VariantClear.argtypes = [ctypes.c_void_p]
oleaut32.VariantClear.restype = ctypes.HRESULT


class VARIANT(ctypes.Structure):
    """Simplified VARIANT for reading BSTR name/value properties."""

    class _Value(ctypes.Union):
        _fields_ = [
            ("llVal", ctypes.c_longlong),
            ("lVal", wintypes.LONG),
            ("bstrVal", ctypes.c_void_p),
            ("punkVal", ctypes.c_void_p),
            ("pbVal", ctypes.c_void_p),
        ]

    _anonymous_ = ("_v",)
    _fields_ = [
        ("vt", wintypes.WORD),
        ("wReserved1", wintypes.WORD),
        ("wReserved2", wintypes.WORD),
        ("wReserved3", wintypes.WORD),
        ("_v", _Value),
    ]


VT_EMPTY = 0
VT_BSTR = 8
VT_I4 = 3


def _vtable(obj: ctypes.c_void_p, index: int, *argtypes, restype=ctypes.HRESULT):
    """Build a callable for COM vtable slot ``index`` on ``obj``."""
    # obj is pointer to pointer to vtable
    p = ctypes.cast(obj, ctypes.POINTER(ctypes.c_void_p))
    vtbl = ctypes.cast(p[0], ctypes.POINTER(ctypes.c_void_p))
    func_ptr = vtbl[index]
    proto = ctypes.WINFUNCTYPE(restype, ctypes.c_void_p, *argtypes)
    return proto(func_ptr)


def _release(obj: Optional[ctypes.c_void_p]) -> None:
    if not obj:
        return
    try:
        release = _vtable(obj, 2)  # IUnknown::Release
        release(obj)
    except Exception:
        pass


def _bstr_to_str(bstr: ctypes.c_void_p) -> str:
    if not bstr:
        return ""
    return ctypes.wstring_at(bstr)


def _get_current_property_bstr(element: ctypes.c_void_p, prop_id: int) -> str:
    # IUIAutomationElement::GetCurrentPropertyValue index 10
    get_prop = _vtable(element, 10, wintypes.INT, ctypes.c_void_p)
    var = VARIANT()
    oleaut32.VariantInit(ctypes.byref(var))
    hr = get_prop(element, prop_id, ctypes.byref(var))
    if hr < 0:
        oleaut32.VariantClear(ctypes.byref(var))
        return ""
    try:
        if var.vt == VT_BSTR:
            return _bstr_to_str(var.bstrVal)
        return ""
    finally:
        oleaut32.VariantClear(ctypes.byref(var))


def _walk_collect_names(element: ctypes.c_void_p, automation: ctypes.c_void_p, depth: int, out: List[str]) -> None:
    if depth > 40:
        return
    name = _get_current_property_bstr(element, UIA_NamePropertyId).strip()
    value = _get_current_property_bstr(element, UIA_ValueValuePropertyId).strip()
    if name:
        out.append(name)
    if value and value != name:
        out.append(value)

    # CreateTrueCondition — IUIAutomation vtable index 21 on Win10+
    # (0-2 IUnknown, 3 CompareElements ... 21 CreateTrueCondition)
    create_true = _vtable(automation, 21, ctypes.POINTER(ctypes.c_void_p))
    condition = ctypes.c_void_p()
    hr = create_true(automation, ctypes.byref(condition))
    if hr < 0 or not condition:
        return

    try:
        # FindAll — IUIAutomationElement index 6: (TreeScope, condition, **array)
        # TreeScope_Children = 2; TreeScope_Descendants = 4
        find_all = _vtable(
            element,
            6,
            wintypes.INT,
            ctypes.c_void_p,
            ctypes.POINTER(ctypes.c_void_p),
        )
        array = ctypes.c_void_p()
        hr = find_all(element, 2, condition, ctypes.byref(array))  # children
        if hr < 0 or not array:
            return
        try:
            # IUIAutomationElementArray::get_Length index 3
            get_length = _vtable(array, 3, ctypes.POINTER(wintypes.INT), restype=ctypes.HRESULT)
            length = wintypes.INT(0)
            if get_length(array, ctypes.byref(length)) < 0:
                return
            # GetElement index 4
            get_element = _vtable(
                array,
                4,
                wintypes.INT,
                ctypes.POINTER(ctypes.c_void_p),
            )
            for i in range(int(length.value)):
                child = ctypes.c_void_p()
                if get_element(array, i, ctypes.byref(child)) < 0 or not child:
                    continue
                try:
                    _walk_collect_names(child, automation, depth + 1, out)
                finally:
                    _release(child)
        finally:
            _release(array)
    finally:
        _release(condition)


def get_uia_text(hwnd: int) -> str:
    """
    Collect Name/Value strings under ``hwnd`` via UI Automation.

    Returns empty string if COM/UIA is unavailable or the tree has no text
    (common when Java Access Bridge is disabled).
    """
    hr = w32.co_initialize()
    # S_OK=0, S_FALSE=1, RPC_E_CHANGED_MODE=0x80010106 — continue if already inited
    need_uninit = hr in (0, 1)

    automation = ctypes.c_void_p()
    try:
        hr = ole32.CoCreateInstance(
            ctypes.byref(CLSID_CUIAutomation),
            None,
            CLSCTX_INPROC_SERVER,
            ctypes.byref(IID_IUIAutomation),
            ctypes.byref(automation),
        )
        if hr < 0 or not automation:
            return ""

        # ElementFromHandle — IUIAutomation index 6
        element_from_handle = _vtable(
            automation,
            6,
            wintypes.HWND,
            ctypes.POINTER(ctypes.c_void_p),
        )
        root = ctypes.c_void_p()
        hr = element_from_handle(automation, wintypes.HWND(hwnd), ctypes.byref(root))
        if hr < 0 or not root:
            return ""

        try:
            parts: List[str] = []
            _walk_collect_names(root, automation, 0, parts)
            # De-dupe while preserving order
            seen = set()
            unique = []
            for p in parts:
                if p not in seen:
                    seen.add(p)
                    unique.append(p)
            return "\n".join(unique)
        finally:
            _release(root)
    except Exception:
        return ""
    finally:
        _release(automation if automation else None)
        if need_uninit:
            try:
                w32.co_uninitialize()
            except Exception:
                pass
