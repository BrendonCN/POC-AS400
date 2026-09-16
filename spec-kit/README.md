# Spec Kit

Technical specification → test cases & logic diagrams, with **local** English and Traditional Chinese (`zh-Hant`) only.

No third-party libraries. This folder is a standalone sub-project; it does not depend on other packages in the parent repo.

繁體中文說明：[README.zh-Hant.md](README.zh-Hant.md)

**How to use:** [HOWTO.md](HOWTO.md) · [HOWTO.zh-Hant.md](HOWTO.zh-Hant.md)

## Layout

```
spec-kit/
  locales/          # en.json, zh-Hant.json
  scripts/i18n.py   # stdlib locale loader
  specs/            # technical specs (*.en.md / *.zh-Hant.md)
  testcases/        # cases traced to REQ-* IDs
  diagrams/         # Mermaid logic diagrams
  templates/        # blank starters
```

## Traceability

1. Write requirements as `REQ-01`, `REQ-02`, … in `specs/`.
2. Map each requirement to `TC-01`, `TC-02`, … in `testcases/`.
3. Label Mermaid nodes with the same IDs in `diagrams/`.
4. Keep EN and TC files in sync (same IDs, parallel wording).

Worked example: **Sign On → Main Menu**

| Locale | Spec | Test cases | Diagrams |
|--------|------|------------|----------|
| EN | [SAMPLE-flow.en.md](specs/SAMPLE-flow.en.md) | [SAMPLE-flow.en.md](testcases/SAMPLE-flow.en.md) | [SAMPLE-flow.en.md](diagrams/SAMPLE-flow.en.md) |
| TC | [SAMPLE-flow.zh-Hant.md](specs/SAMPLE-flow.zh-Hant.md) | [SAMPLE-flow.zh-Hant.md](testcases/SAMPLE-flow.zh-Hant.md) | [SAMPLE-flow.zh-Hant.md](diagrams/SAMPLE-flow.zh-Hant.md) |

## Local venv (isolation only)

```powershell
cd spec-kit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# no pip install — requirements.txt is intentionally empty of packages
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant
python scripts\i18n.py --locale zh-Hant --key flow.main_menu
```

## Local translation helper

[`scripts/i18n.py`](scripts/i18n.py) loads [`locales/en.json`](locales/en.json) or [`locales/zh-Hant.json`](locales/zh-Hant.json) with the Python standard library only.

```python
from scripts.i18n import load, t  # run from spec-kit with PYTHONPATH=. if importing

load("zh-Hant")
print(t("label.spec"))  # 技術規格
```

Or use the CLI (recommended):

```powershell
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant --key project.title
```

## Adding a new flow

1. Copy [`templates/technical-spec.md`](templates/technical-spec.md) → `specs/YOUR-flow.en.md` and `specs/YOUR-flow.zh-Hant.md`.
2. Copy [`templates/testcases.md`](templates/testcases.md) → `testcases/…`.
3. Copy [`templates/logic-diagram.md`](templates/logic-diagram.md) → `diagrams/…`.
4. Add any shared UI labels to both locale JSON files.
