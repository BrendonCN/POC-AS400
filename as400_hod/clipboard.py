"""Clipboard helpers for screen-copy fallback (stdlib ctypes)."""

from __future__ import annotations

import time
from typing import Optional

from as400_hod import input_actions
from as400_hod import win32_api as w32
from as400_hod.window import ensure_alive


def read_clipboard_unicode() -> Optional[str]:
    """Read CF_UNICODETEXT; return None if unavailable."""
    w32.open_clipboard(0)
    try:
        return w32.get_clipboard_unicode()
    finally:
        w32.close_clipboard()


def save_clipboard_unicode() -> Optional[str]:
    """Best-effort snapshot of current Unicode clipboard text."""
    try:
        return read_clipboard_unicode()
    except OSError:
        return None


def restore_clipboard_unicode(text: Optional[str]) -> None:
    """Restore previous Unicode clipboard contents when possible."""
    if text is None:
        return
    try:
        w32.open_clipboard(0)
        try:
            w32.empty_clipboard()
            w32.set_clipboard_unicode(text)
        finally:
            w32.close_clipboard()
    except OSError:
        pass


def copy_screen_via_hotkeys(hwnd: int, *, settle: float = 0.25) -> str:
    """
    Post Ctrl+A then Ctrl+C to the HOD window and read the clipboard.

    Does not steal focus, but temporarily uses the system clipboard.
    Previous Unicode clipboard text is restored when possible.
    """
    ensure_alive(hwnd)
    previous = save_clipboard_unicode()
    try:
        # Clear our view: empty clipboard so we can detect a fresh copy
        try:
            w32.open_clipboard(0)
            try:
                w32.empty_clipboard()
            finally:
                w32.close_clipboard()
        except OSError:
            pass

        input_actions.post_chord(hwnd, [w32.VK_CONTROL], ord("A"))
        time.sleep(settle)
        ensure_alive(hwnd)
        input_actions.post_chord(hwnd, [w32.VK_CONTROL], ord("C"))
        time.sleep(settle)
        ensure_alive(hwnd)

        text = None
        for _ in range(10):
            try:
                text = read_clipboard_unicode()
            except OSError:
                text = None
            if text:
                break
            time.sleep(0.05)
        return text or ""
    finally:
        restore_clipboard_unicode(previous)
