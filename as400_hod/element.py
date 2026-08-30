"""Selenium-like element wrapper for a location on the HOD screen."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Tuple, Union

from as400_hod.window import ensure_alive

if TYPE_CHECKING:
    from as400_hod.driver import HodDriver


class HodElement:
    """A located region on the terminal screen (text match or row/col)."""

    def __init__(
        self,
        driver: "HodDriver",
        *,
        row: int,
        col: int,
        text: str = "",
        length: Optional[int] = None,
    ) -> None:
        self._driver = driver
        self.row = row
        self.col = col
        self._text = text
        self._length = length if length is not None else len(text) if text else 1

    @property
    def text(self) -> str:
        """Return cached match text, or re-read from screen at this location."""
        ensure_alive(self._driver.hwnd)
        if self._text:
            return self._text
        screen = self._driver.get_screen_text()
        from as400_hod.screen import read_area

        return read_area(screen, self.row, self.col, self._length)

    @property
    def location(self) -> Tuple[int, int]:
        """1-based (row, col) of the element start."""
        return self.row, self.col

    def click(self) -> None:
        ensure_alive(self._driver.hwnd)
        self._driver.click(row=self.row, col=self.col)

    def send_keys(self, *parts: Union[str, object]) -> None:
        ensure_alive(self._driver.hwnd)
        self.click()
        self._driver.send_keys(*parts)

    def __repr__(self) -> str:
        preview = (self._text[:40] + "…") if len(self._text) > 40 else self._text
        return f"HodElement(row={self.row}, col={self.col}, text={preview!r})"
