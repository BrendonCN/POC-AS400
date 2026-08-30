"""Selenium-like driver for IBM Host On-Demand (.hod) windows."""

from __future__ import annotations

import time
from typing import List, Optional, Pattern, Tuple, Union

from as400_hod import clipboard as clip_mod
from as400_hod import input_actions
from as400_hod import screen as screen_mod
from as400_hod import uia as uia_mod
from as400_hod.by import By
from as400_hod.coords import CellGeometry
from as400_hod.element import HodElement
from as400_hod.exceptions import (
    ElementNotFoundError,
    HodAutomationError,
    HodTimeoutError,
    HodWindowClosedError,
)
from as400_hod.window import ensure_alive, find_hod_hwnd


class HodDriver:
    """
    Attach to a running Host On-Demand window and automate it like Selenium.

    By default uses PostMessage only (``focus_policy='background'``) so other
    apps keep keyboard/mouse focus. Raises ``HodWindowClosedError`` when the
    .hod window disappears.
    """

    def __init__(
        self,
        hwnd: int,
        *,
        cell_size: Tuple[int, int] = (9, 16),
        origin: Tuple[int, int] = (0, 0),
        focus_policy: str = "background",
        text_strategy: str = "auto",
        key_pause: float = 0.01,
    ) -> None:
        if focus_policy not in ("background", "steal"):
            raise ValueError("focus_policy must be 'background' or 'steal'")
        if focus_policy == "steal":
            raise HodAutomationError(
                "focus_policy='steal' is reserved; only background PostMessage "
                "is implemented to avoid affecting other controls."
            )
        if text_strategy not in ("auto", "uia", "clipboard"):
            raise ValueError("text_strategy must be 'auto', 'uia', or 'clipboard'")

        ensure_alive(hwnd)
        self._hwnd = int(hwnd)
        self._geometry = CellGeometry(
            cell_width=cell_size[0],
            cell_height=cell_size[1],
            origin_x=origin[0],
            origin_y=origin[1],
        )
        self.focus_policy = focus_policy
        self.text_strategy = text_strategy
        self.key_pause = key_pause
        self._closed = False

    # --- construction --------------------------------------------------------

    @classmethod
    def attach(
        cls,
        *,
        title_contains: Optional[str] = None,
        title_equals: Optional[str] = None,
        title_regex: Optional[Union[str, Pattern[str]]] = None,
        hwnd: Optional[int] = None,
        process_name_contains: Optional[str] = None,
        cell_size: Tuple[int, int] = (9, 16),
        origin: Tuple[int, int] = (0, 0),
        focus_policy: str = "background",
        text_strategy: str = "auto",
        key_pause: float = 0.01,
    ) -> "HodDriver":
        """Find a HOD window and return a driver bound to it."""
        found = find_hod_hwnd(
            title_contains=title_contains,
            title_equals=title_equals,
            title_regex=title_regex,
            hwnd=hwnd,
            process_name_contains=process_name_contains,
        )
        return cls(
            found,
            cell_size=cell_size,
            origin=origin,
            focus_policy=focus_policy,
            text_strategy=text_strategy,
            key_pause=key_pause,
        )

    # --- lifecycle -----------------------------------------------------------

    @property
    def hwnd(self) -> int:
        return self._hwnd

    def _ensure(self) -> None:
        if self._closed:
            raise HodWindowClosedError("HOD window is closed; automation stopped")
        ensure_alive(self._hwnd)

    def quit(self) -> None:
        """Detach the driver (does not close the HOD application)."""
        self._closed = True

    # --- input ---------------------------------------------------------------

    def click(
        self,
        row: Optional[int] = None,
        col: Optional[int] = None,
        *,
        x: Optional[int] = None,
        y: Optional[int] = None,
    ) -> None:
        """
        Click a terminal cell (1-based row/col) or raw client pixel (x, y).
        """
        self._ensure()
        if x is not None and y is not None:
            cx, cy = int(x), int(y)
        elif row is not None and col is not None:
            cx, cy = self._geometry.row_col_to_client(int(row), int(col))
        else:
            raise ValueError("Provide row and col, or x and y")
        input_actions.post_click(self._hwnd, cx, cy)

    def send_keys(self, *parts: Union[str, object]) -> None:
        """Type text and/or Keys.* tokens into the HOD window."""
        self._ensure()
        input_actions.send_keys(self._hwnd, *parts, pause=self.key_pause)

    # --- text ----------------------------------------------------------------

    def get_screen_text(self) -> str:
        """
        Return visible screen text via UI Automation and/or clipboard copy.

        Strategy ``auto`` tries UIA first, then clipboard if UIA is empty.
        """
        self._ensure()
        strategy = self.text_strategy

        if strategy in ("auto", "uia"):
            text = uia_mod.get_uia_text(self._hwnd)
            self._ensure()
            if text.strip():
                return text
            if strategy == "uia":
                return text

        # clipboard fallback (auto or clipboard)
        text = clip_mod.copy_screen_via_hotkeys(self._hwnd)
        self._ensure()
        return text

    def get_text_at(self, row: int, col: int, length: int) -> str:
        """Read a slice of the current screen at 1-based coordinates."""
        self._ensure()
        return screen_mod.read_area(self.get_screen_text(), row, col, length)

    # --- find ----------------------------------------------------------------

    def find_element(self, by: str, value: Union[str, Tuple[int, int]]) -> HodElement:
        """Find the first matching element; raise ElementNotFoundError if none."""
        self._ensure()
        found = self.find_elements(by, value)
        if not found:
            raise ElementNotFoundError(f"No element found by {by}={value!r}")
        return found[0]

    def find_elements(self, by: str, value: Union[str, Tuple[int, int]]) -> List[HodElement]:
        self._ensure()
        if by == By.ROW_COL:
            if not isinstance(value, tuple) or len(value) != 2:
                raise ValueError("By.ROW_COL expects (row, col)")
            row, col = int(value[0]), int(value[1])
            return [HodElement(self, row=row, col=col, text="")]

        if by == By.TEXT:
            needle = str(value)
            screen = self.get_screen_text()
            matches = screen_mod.find_text_matches(screen, needle)
            return [
                HodElement(self, row=m.row, col=m.col, text=m.text, length=len(m.text))
                for m in matches
            ]

        raise ValueError(f"Unsupported locator strategy: {by!r}")

    # --- waits ---------------------------------------------------------------

    def wait_until_text_contains(
        self,
        text: str,
        timeout: float = 20.0,
        poll: float = 0.5,
    ) -> str:
        """Poll screen text until ``text`` appears or timeout / window closed."""
        deadline = time.monotonic() + timeout
        last = ""
        while True:
            self._ensure()
            last = self.get_screen_text()
            if text in last:
                return last
            if time.monotonic() >= deadline:
                raise HodTimeoutError(
                    f"Timed out after {timeout}s waiting for text containing {text!r}"
                )
            time.sleep(poll)

    def wait_until_text_gone(
        self,
        text: str,
        timeout: float = 20.0,
        poll: float = 0.5,
    ) -> str:
        deadline = time.monotonic() + timeout
        last = ""
        while True:
            self._ensure()
            last = self.get_screen_text()
            if text not in last:
                return last
            if time.monotonic() >= deadline:
                raise HodTimeoutError(
                    f"Timed out after {timeout}s waiting for text {text!r} to disappear"
                )
            time.sleep(poll)

    def __repr__(self) -> str:
        return f"HodDriver(hwnd={self._hwnd})"
