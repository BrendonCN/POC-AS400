"""
Attach to a running Host On-Demand (.hod) window, dump screen text, and
demonstrate Selenium-like click / send_keys / wait helpers.

Requires an already-open HOD session. No credentials are hardcoded.

Usage:
  python examples/attach_and_read.py
  python examples/attach_and_read.py --title ".hod"
  python examples/attach_and_read.py --hwnd 123456
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running from repo root without installing the package
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from as400_hod import By, HodDriver, HodWindowClosedError, Keys  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Stdlib HOD attach & read demo")
    parser.add_argument("--title", default=".hod", help="Window title substring")
    parser.add_argument("--hwnd", type=int, default=None, help="Explicit HWND")
    parser.add_argument("--cell-w", type=int, default=9, help="Character cell width px")
    parser.add_argument("--cell-h", type=int, default=16, help="Character cell height px")
    parser.add_argument(
        "--origin-x", type=int, default=0, help="Terminal grid origin X in client px"
    )
    parser.add_argument(
        "--origin-y", type=int, default=0, help="Terminal grid origin Y in client px"
    )
    parser.add_argument(
        "--strategy",
        choices=("auto", "uia", "clipboard"),
        default="auto",
        help="Screen text strategy",
    )
    args = parser.parse_args()

    try:
        driver = HodDriver.attach(
            title_contains=None if args.hwnd else args.title,
            hwnd=args.hwnd,
            cell_size=(args.cell_w, args.cell_h),
            origin=(args.origin_x, args.origin_y),
            text_strategy=args.strategy,
        )
    except Exception as exc:
        print(f"Attach failed: {exc}", file=sys.stderr)
        return 1

    print(f"Attached to HWND {driver.hwnd}")
    try:
        screen = driver.get_screen_text()
        print("--- screen ---")
        print(screen if screen.strip() else "(empty — enable Java Access Bridge or use clipboard)")
        print("--------------")

        # Optional: locate a common label if present
        try:
            el = driver.find_element(By.TEXT, "Sign On")
            print(f"Found: {el!r}")
        except Exception:
            print("No 'Sign On' label found (ok if already logged in).")

        # Harmless AID key demo — comment out if you do not want to send F24
        # driver.send_keys(Keys.F24)

        print("Demo complete. Close the HOD window and re-run a step to see HodWindowClosedError.")
    except HodWindowClosedError as exc:
        print(f"Stopped: {exc}", file=sys.stderr)
        return 2
    finally:
        driver.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
