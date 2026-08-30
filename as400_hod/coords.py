"""Map terminal row/column to HOD window client pixel coordinates."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass
class CellGeometry:
    """Character cell size and origin inside the HOD client area."""

    cell_width: int = 9
    cell_height: int = 16
    origin_x: int = 0
    origin_y: int = 0

    def row_col_to_client(self, row: int, col: int) -> Tuple[int, int]:
        """
        Convert 1-based terminal (row, col) to client pixel center of the cell.

        Terminal screens are typically 24x80 with row 1 at the top and col 1
        at the left.
        """
        if row < 1 or col < 1:
            raise ValueError("row and col must be 1-based (>= 1)")
        x = self.origin_x + (col - 1) * self.cell_width + self.cell_width // 2
        y = self.origin_y + (row - 1) * self.cell_height + self.cell_height // 2
        return x, y

    def client_to_row_col(self, x: int, y: int) -> Tuple[int, int]:
        """Convert client pixels to 1-based (row, col)."""
        col = ((x - self.origin_x) // self.cell_width) + 1
        row = ((y - self.origin_y) // self.cell_height) + 1
        return max(1, row), max(1, col)
