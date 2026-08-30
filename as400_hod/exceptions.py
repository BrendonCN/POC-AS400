"""Exceptions for Host On-Demand automation."""


class HodAutomationError(Exception):
    """Base error for HOD automation failures."""


class HodWindowClosedError(HodAutomationError):
    """Raised when the HOD window is closed or the HWND is no longer valid."""


class ElementNotFoundError(HodAutomationError):
    """Raised when find_element cannot locate a match."""


class HodTimeoutError(HodAutomationError):
    """Raised when a wait condition is not met within the timeout."""
