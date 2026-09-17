#!/usr/bin/env python3
"""Minimal local EN / zh-Hant translation helper (stdlib only).

For outline tech-spec → testcase / diagram generation, use:
  python scripts/spec_pipeline.py "specs/example _flow.en.md"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

LOCALES_DIR = Path(__file__).resolve().parent.parent / "locales"
SUPPORTED = ("en", "zh-Hant")

_catalog: dict[str, str] = {}
_locale: str = "en"


def _configure_stdout() -> None:
    """Prefer UTF-8 on Windows consoles so TC strings print cleanly."""
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfigure):
        try:
            reconfigure(encoding="utf-8")
        except Exception:
            pass


def load(locale: str) -> dict[str, str]:
    """Load a locale JSON file into the active catalog and return it."""
    global _catalog, _locale
    if locale not in SUPPORTED:
        raise ValueError(f"Unsupported locale: {locale!r}. Use one of {SUPPORTED}")
    path = LOCALES_DIR / f"{locale}.json"
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Locale file must be a JSON object: {path}")
    _catalog = {str(k): str(v) for k, v in data.items()}
    _locale = locale
    return _catalog


def t(key: str, default: str | None = None) -> str:
    """Translate *key* using the loaded catalog."""
    if key in _catalog:
        return _catalog[key]
    if default is not None:
        return default
    return key


def main(argv: list[str] | None = None) -> int:
    _configure_stdout()
    parser = argparse.ArgumentParser(description="Local EN/TC string table (no pip deps)")
    parser.add_argument(
        "--locale",
        default="en",
        choices=SUPPORTED,
        help="Locale to load (default: en)",
    )
    parser.add_argument(
        "--key",
        default=None,
        help="Print a single key; omit to list all keys",
    )
    args = parser.parse_args(argv)

    catalog = load(args.locale)
    print(f"{t('cli.loaded', 'Loaded locale')}: {args.locale}")
    print(f"{t('cli.usage')}")
    print()

    if args.key:
        print(f"{args.key} = {t(args.key)}")
        return 0

    print(f"{t('cli.keys')}:")
    for key in sorted(catalog):
        print(f"  {key} = {catalog[key]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
