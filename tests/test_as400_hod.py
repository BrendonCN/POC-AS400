"""Unit tests for pure logic (no live HOD window required)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from as400_hod.coords import CellGeometry
from as400_hod.exceptions import ElementNotFoundError, HodWindowClosedError
from as400_hod.screen import find_text_matches, first_match, read_area
from as400_hod.window import ensure_alive


class TestCoords(unittest.TestCase):
    def test_row_col_to_client_center(self):
        g = CellGeometry(cell_width=10, cell_height=20, origin_x=5, origin_y=7)
        x, y = g.row_col_to_client(1, 1)
        self.assertEqual((x, y), (5 + 5, 7 + 10))
        x2, y2 = g.row_col_to_client(2, 3)
        self.assertEqual((x2, y2), (5 + 20 + 5, 7 + 20 + 10))

    def test_rejects_zero_based(self):
        g = CellGeometry()
        with self.assertRaises(ValueError):
            g.row_col_to_client(0, 1)


class TestScreenFind(unittest.TestCase):
    SAMPLE = "Sign On\nUser  . . . . ______\nPassword  . . ______\n"

    def test_find_text(self):
        matches = find_text_matches(self.SAMPLE, "Sign On")
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].row, 1)
        self.assertEqual(matches[0].col, 1)

    def test_find_user(self):
        m = first_match(self.SAMPLE, "User")
        self.assertIsNotNone(m)
        self.assertEqual(m.row, 2)
        self.assertEqual(m.col, 1)

    def test_read_area(self):
        self.assertEqual(read_area(self.SAMPLE, 1, 1, 7), "Sign On")

    def test_missing(self):
        self.assertEqual(find_text_matches(self.SAMPLE, "Nope"), [])


class TestEnsureAlive(unittest.TestCase):
    def test_closed_raises(self):
        with mock.patch("as400_hod.window.w32.is_window", return_value=False):
            with self.assertRaises(HodWindowClosedError):
                ensure_alive(12345)

    def test_alive_ok(self):
        with mock.patch("as400_hod.window.w32.is_window", return_value=True):
            ensure_alive(12345)


class TestDriverFind(unittest.TestCase):
    def test_find_element_by_text(self):
        from as400_hod.by import By
        from as400_hod.driver import HodDriver

        with mock.patch("as400_hod.driver.ensure_alive"):
            drv = HodDriver.__new__(HodDriver)
            drv._hwnd = 1
            drv._closed = False
            drv._geometry = CellGeometry()
            drv.focus_policy = "background"
            drv.text_strategy = "uia"
            drv.key_pause = 0.0
            drv.get_screen_text = mock.Mock(
                return_value="Main Menu\nOption 1\n"
            )
            el = drv.find_element(By.TEXT, "Main Menu")
            self.assertEqual(el.row, 1)
            self.assertEqual(el.col, 1)
            with self.assertRaises(ElementNotFoundError):
                drv.find_element(By.TEXT, "Missing")


if __name__ == "__main__":
    unittest.main()
