"""Locate and validate Host On-Demand top-level windows."""

from __future__ import annotations

import re
from typing import Optional, Pattern, Union

from as400_hod.exceptions import HodAutomationError, HodWindowClosedError
from as400_hod import win32_api as w32


def find_hod_hwnd(
    *,
    title_contains: Optional[str] = None,
    title_equals: Optional[str] = None,
    title_regex: Optional[Union[str, Pattern[str]]] = None,
    hwnd: Optional[int] = None,
    process_name_contains: Optional[str] = None,
    prefer_hod_extension: bool = True,
) -> int:
    """
    Find a top-level HOD window HWND.

    Matching priority when multiple windows match: titles containing ``.hod``
    are preferred when ``prefer_hod_extension`` is True.
    """
    if hwnd is not None:
        if not w32.is_window(hwnd):
            raise HodWindowClosedError("HOD window is closed; automation stopped")
        return int(hwnd)

    pattern: Optional[Pattern[str]] = None
    if title_regex is not None:
        pattern = re.compile(title_regex) if isinstance(title_regex, str) else title_regex

    matches = []
    for candidate, title, _cls in w32.list_top_level_windows(visible_only=True):
        if title_equals is not None and title != title_equals:
            continue
        if title_contains is not None and title_contains not in title:
            continue
        if pattern is not None and not pattern.search(title):
            continue
        if process_name_contains:
            image = w32.get_process_image_name(w32.get_window_pid(candidate)).lower()
            if process_name_contains.lower() not in image:
                continue
        # If no filters given, only consider titles that look like HOD sessions
        if (
            title_equals is None
            and title_contains is None
            and pattern is None
            and process_name_contains is None
        ):
            if ".hod" not in title.lower():
                continue
        matches.append((candidate, title))

    if not matches:
        raise HodAutomationError(
            "No matching HOD window found. Open a .hod session or pass title_contains/hwnd."
        )

    if prefer_hod_extension:
        hodish = [(h, t) for h, t in matches if ".hod" in t.lower()]
        if hodish:
            matches = hodish

    return matches[0][0]


def ensure_alive(hwnd: int) -> None:
    """Raise HodWindowClosedError if the HWND is missing or invalid."""
    if not hwnd or not w32.is_window(hwnd):
        raise HodWindowClosedError("HOD window is closed; automation stopped")
