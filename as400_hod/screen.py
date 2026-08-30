"""Screen buffer helpers for find-by-text and row/col slicing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass(frozen=True)
class TextMatch:
    text: str
    row: int  # 1-based
    col: int  # 1-based
    end_col: int  # exclusive, 1-based column after last char


def normalize_screen(text: str) -> List[str]:
    """Split screen text into lines; strip trailing CR."""
    if not text:
        return []
    return [line.rstrip("\r") for line in text.replace("\r\n", "\n").split("\n")]


def find_text_matches(screen: str, needle: str) -> List[TextMatch]:
    """Find all occurrences of ``needle`` in the screen buffer (line-oriented)."""
    if not needle:
        return []
    matches: List[TextMatch] = []
    lines = normalize_screen(screen)
    for i, line in enumerate(lines):
        start = 0
        while True:
            idx = line.find(needle, start)
            if idx < 0:
                break
            row = i + 1
            col = idx + 1
            matches.append(
                TextMatch(
                    text=needle,
                    row=row,
                    col=col,
                    end_col=col + len(needle),
                )
            )
            start = idx + 1
    return matches


def read_area(screen: str, row: int, col: int, length: int) -> str:
    """Read ``length`` characters starting at 1-based (row, col)."""
    lines = normalize_screen(screen)
    if row < 1 or row > len(lines):
        return ""
    line = lines[row - 1]
    start = col - 1
    if start < 0:
        return ""
    return line[start : start + length]


def first_match(screen: str, needle: str) -> Optional[TextMatch]:
    found = find_text_matches(screen, needle)
    return found[0] if found else None
