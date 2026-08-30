"""
Stdlib-only Host On-Demand (HOD) automation with a Selenium-like API.

Uses ctypes Win32 PostMessage for background click/type (no focus steal by
default), UI Automation + clipboard for screen text, and raises
HodWindowClosedError when the .hod window disappears.
"""

from as400_hod.by import By
from as400_hod.driver import HodDriver
from as400_hod.element import HodElement
from as400_hod.exceptions import (
    ElementNotFoundError,
    HodAutomationError,
    HodTimeoutError,
    HodWindowClosedError,
)
from as400_hod.keys import Keys

__all__ = [
    "By",
    "HodDriver",
    "HodElement",
    "HodAutomationError",
    "HodWindowClosedError",
    "ElementNotFoundError",
    "HodTimeoutError",
    "Keys",
]

__version__ = "0.1.0"
