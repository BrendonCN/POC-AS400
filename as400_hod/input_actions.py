"""Background click and key input via PostMessage (no focus steal)."""

from __future__ import annotations

import time
from typing import Iterable, Union

from as400_hod import win32_api as w32
from as400_hod.keys import Keys
from as400_hod.window import ensure_alive

# Map Keys.* tokens to virtual-key codes
_KEY_VK = {
    Keys.ENTER: w32.VK_RETURN,
    Keys.TAB: w32.VK_TAB,
    Keys.BACKSPACE: w32.VK_BACK,
    Keys.ESCAPE: w32.VK_ESCAPE,
    Keys.DELETE: w32.VK_DELETE,
    Keys.HOME: w32.VK_HOME,
    Keys.END: w32.VK_END,
    Keys.PAGE_UP: w32.VK_PRIOR,
    Keys.PAGE_DOWN: w32.VK_NEXT,
    Keys.ARROW_LEFT: w32.VK_LEFT,
    Keys.ARROW_UP: w32.VK_UP,
    Keys.ARROW_RIGHT: w32.VK_RIGHT,
    Keys.ARROW_DOWN: w32.VK_DOWN,
    Keys.CONTROL: w32.VK_CONTROL,
    Keys.SHIFT: w32.VK_SHIFT,
    Keys.ALT: w32.VK_MENU,
}

for _i in range(1, 25):
    _token = getattr(Keys, f"F{_i}")
    _KEY_VK[_token] = w32.VK_F1 + (_i - 1)


def _keydown_lparam(repeat: int = 1, scan: int = 0, extended: bool = False) -> int:
    # bits: repeat | scan<<16 | extended<<24 | context<<29 | previous<<30 | transition<<31
    return (repeat & 0xFFFF) | ((scan & 0xFF) << 16) | ((1 if extended else 0) << 24)


def _keyup_lparam(scan: int = 0, extended: bool = False) -> int:
    return (1 & 0xFFFF) | ((scan & 0xFF) << 16) | ((1 if extended else 0) << 24) | (1 << 30) | (1 << 31)


def post_click(hwnd: int, x: int, y: int, *, pause: float = 0.02) -> None:
    """Left-click at client coordinates using PostMessage only."""
    ensure_alive(hwnd)
    lp = w32.MAKELPARAM(x, y)
    w32.post_message(hwnd, w32.WM_MOUSEMOVE, 0, lp)
    w32.post_message(hwnd, w32.WM_LBUTTONDOWN, w32.MK_LBUTTON, lp)
    time.sleep(pause)
    ensure_alive(hwnd)
    w32.post_message(hwnd, w32.WM_LBUTTONUP, 0, lp)


def post_vk(hwnd: int, vk: int, *, pause: float = 0.01) -> None:
    """Post a virtual-key down/up pair."""
    ensure_alive(hwnd)
    w32.post_message(hwnd, w32.WM_KEYDOWN, vk, _keydown_lparam())
    time.sleep(pause)
    ensure_alive(hwnd)
    w32.post_message(hwnd, w32.WM_KEYUP, vk, _keyup_lparam())


def post_char(hwnd: int, ch: str, *, pause: float = 0.005) -> None:
    """Post a printable character via WM_CHAR."""
    if len(ch) != 1:
        raise ValueError("post_char expects a single character")
    ensure_alive(hwnd)
    code = ord(ch)
    w32.post_message(hwnd, w32.WM_CHAR, code, 1)
    time.sleep(pause)


def post_chord(hwnd: int, modifiers: Iterable[int], vk: int, *, pause: float = 0.01) -> None:
    """Hold modifiers, tap vk, release modifiers (e.g. Ctrl+C)."""
    ensure_alive(hwnd)
    mods = list(modifiers)
    for m in mods:
        w32.post_message(hwnd, w32.WM_KEYDOWN, m, _keydown_lparam())
    w32.post_message(hwnd, w32.WM_KEYDOWN, vk, _keydown_lparam())
    time.sleep(pause)
    ensure_alive(hwnd)
    w32.post_message(hwnd, w32.WM_KEYUP, vk, _keyup_lparam())
    for m in reversed(mods):
        w32.post_message(hwnd, w32.WM_KEYUP, m, _keyup_lparam())


def send_keys(hwnd: int, *parts: Union[str, object], pause: float = 0.01) -> None:
    """
    Type text and special Keys tokens into the HOD window via PostMessage.

    Accepts strings and Keys.* constants mixed, similar to Selenium send_keys.
    """
    for part in parts:
        ensure_alive(hwnd)
        if part is None or part == Keys.NULL:
            continue
        token = str(part)
        if token in _KEY_VK:
            post_vk(hwnd, _KEY_VK[token], pause=pause)
            continue
        for ch in token:
            ensure_alive(hwnd)
            if ch == "\n":
                post_vk(hwnd, w32.VK_RETURN, pause=pause)
            elif ch == "\t":
                post_vk(hwnd, w32.VK_TAB, pause=pause)
            elif ch == "\b":
                post_vk(hwnd, w32.VK_BACK, pause=pause)
            else:
                post_char(hwnd, ch, pause=pause)
