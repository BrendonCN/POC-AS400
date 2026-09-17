#!/usr/bin/env python3
"""CLI: outline technical spec → JSON + test cases + Mermaid diagrams.

Example:
  python scripts/spec_pipeline.py "specs/example _flow.en.md"
  python scripts/spec_pipeline.py specs/SAMPLE-flow.en.md --locale zh-Hant
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow `python scripts/spec_pipeline.py` from spec-kit/
_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from generate_artifacts import write_artifacts  # noqa: E402
from outline_parser import parse_file, to_json  # noqa: E402


def _configure_stdout() -> None:
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfigure):
        try:
            reconfigure(encoding="utf-8")
        except Exception:
            pass


def main(argv: list[str] | None = None) -> int:
    _configure_stdout()
    kit_root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(
        description="Parse outline tech spec and generate test cases + logic diagrams"
    )
    parser.add_argument(
        "spec",
        type=Path,
        help="Path to outline markdown (e.g. specs/example _flow.en.md)",
    )
    parser.add_argument(
        "--locale",
        default=None,
        choices=("en", "zh-Hant"),
        help="Output locale (default: infer from *.en.md / *.zh-Hant.md)",
    )
    parser.add_argument(
        "--json",
        type=Path,
        default=None,
        help="Optional path to write parsed JSON (default: out/<basename>.json)",
    )
    parser.add_argument(
        "--basename",
        default=None,
        help="Output file basename without locale suffix (default: from spec name)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and print summary only; do not write files",
    )
    args = parser.parse_args(argv)

    spec_path = args.spec
    if not spec_path.is_file():
        # Resolve relative to kit root
        candidate = kit_root / spec_path
        if candidate.is_file():
            spec_path = candidate
        else:
            print(f"Spec not found: {args.spec}", file=sys.stderr)
            return 1

    doc = parse_file(spec_path)
    locale = args.locale
    if locale is None:
        name = spec_path.name
        locale = "zh-Hant" if name.endswith(".zh-Hant.md") else "en"

    print(f"Source: {spec_path}")
    print(f"Title:  {doc.title}")
    print(f"Chapters: {len(doc.chapters)}")
    print(f"Function keys: {', '.join(fk['key'] for fk in doc.function_keys) or '(none)'}")
    print(f"Message codes: {', '.join(doc.message_codes) or '(none)'}")
    print(f"Error codes:   {', '.join(doc.error_codes) or '(none)'}")
    print(f"Requirements:  {len(doc.requirements)}")
    print(f"Locale:        {locale}")

    if args.dry_run:
        return 0

    out_json = args.json
    if out_json is None:
        out_dir = kit_root / "out"
        out_dir.mkdir(parents=True, exist_ok=True)
        stem = args.basename or re_slug(spec_path)
        out_json = out_dir / f"{stem}.json"
    else:
        out_json = out_json if out_json.is_absolute() else kit_root / out_json
        out_json.parent.mkdir(parents=True, exist_ok=True)

    out_json.write_text(to_json(doc), encoding="utf-8")
    print(f"Wrote JSON: {out_json}")

    paths = write_artifacts(
        doc,
        kit_root,
        basename=args.basename or re_slug(spec_path),
        locale=locale,
    )
    print(f"Wrote testcases: {paths['testcases']}")
    print(f"Wrote diagrams:  {paths['diagrams']}")
    return 0


def re_slug(path: Path) -> str:
    import re

    s = path.name
    s = re.sub(r"\.(en|zh-Hant)\.md$", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\.md$", "", s, flags=re.IGNORECASE)
    s = s.replace("_", "-")
    s = re.sub(r"[^\w\-]+", "-", s, flags=re.UNICODE)
    return re.sub(r"-+", "-", s).strip("-").lower() or "flow"


if __name__ == "__main__":
    sys.exit(main())
