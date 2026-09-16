# How to use Spec Kit

Step-by-step guide for this sub-project. Overview and links: [README.md](README.md) · 繁中：[HOWTO.zh-Hant.md](HOWTO.zh-Hant.md)

## What this is for

Turn a **technical specification** into:

1. **Test cases** (`TC-*` mapped to `REQ-*`)
2. **Logic diagrams** (Mermaid, same IDs on nodes)

Documents ship in **English** (`*.en.md`) and **Traditional Chinese** (`*.zh-Hant.md`) only. No cloud translation, no pip packages.

---

## 1. One-time setup

From the repo root:

```powershell
cd spec-kit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No `pip install` is required. Confirm the locale helper works:

```powershell
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant --key label.spec
```

Expected: English and Traditional Chinese labels print without errors.

---

## 2. Read the worked example first

Open the **Sign On → Main Menu** sample in order:

| Step | English | Traditional Chinese |
|------|---------|---------------------|
| Spec | [specs/SAMPLE-flow.en.md](specs/SAMPLE-flow.en.md) | [specs/SAMPLE-flow.zh-Hant.md](specs/SAMPLE-flow.zh-Hant.md) |
| Test cases | [testcases/SAMPLE-flow.en.md](testcases/SAMPLE-flow.en.md) | [testcases/SAMPLE-flow.zh-Hant.md](testcases/SAMPLE-flow.zh-Hant.md) |
| Diagrams | [diagrams/SAMPLE-flow.en.md](diagrams/SAMPLE-flow.en.md) | [diagrams/SAMPLE-flow.zh-Hant.md](diagrams/SAMPLE-flow.zh-Hant.md) |

Notice:

- Spec sections use **`REQ-01` … `REQ-06`**
- Each test case uses a matching **`TC-01` … `TC-06`**
- Mermaid nodes repeat those IDs for traceability

---

## 3. Add a new flow (recommended workflow)

Replace `my-flow` with your short kebab-case name (e.g. `order-inquiry`).

### 3.1 Copy templates

```powershell
cd spec-kit
Copy-Item templates\technical-spec.md specs\my-flow.en.md
Copy-Item templates\technical-spec.md specs\my-flow.zh-Hant.md
Copy-Item templates\testcases.md      testcases\my-flow.en.md
Copy-Item templates\testcases.md      testcases\my-flow.zh-Hant.md
Copy-Item templates\logic-diagram.md  diagrams\my-flow.en.md
Copy-Item templates\logic-diagram.md  diagrams\my-flow.zh-Hant.md
```

### 3.2 Write the English technical spec first

Edit `specs/my-flow.en.md`:

1. Fill **Document ID**, purpose, actors, preconditions.
2. Add requirements as `REQ-01`, `REQ-02`, … (description + expected result).
3. List happy-path steps and error paths.
4. Fill the **Traceability** table (REQ → TC → diagram node).

### 3.3 Derive test cases from the spec

Edit `testcases/my-flow.en.md`:

1. One row / section per `REQ-*` → `TC-*` (same number).
2. For each case: preconditions, steps, expected result.
3. Cover happy path **and** the error paths from the spec (invalid input, timeout, abort, etc.).

### 3.4 Draw logic diagrams

Edit `diagrams/my-flow.en.md`:

1. High-level flowchart: attach / act / verify / stop (or your real steps).
2. Decision / error diagram for branches.
3. Optional sequence diagram.
4. Put `REQ-*` and `TC-*` in node labels.

Mermaid renders on GitHub, GitLab, and many Markdown previewers (including VS Code / Cursor with a Mermaid extension).

### 3.5 Translate to Traditional Chinese

Mirror the same structure and **identical IDs** in:

- `specs/my-flow.zh-Hant.md`
- `testcases/my-flow.zh-Hant.md`
- `diagrams/my-flow.zh-Hant.md`

Do **not** renumber requirements between locales. Only the prose changes.

### 3.6 Shared labels (optional)

If several docs reuse the same short labels (e.g. “Main Menu”), add keys to both:

- [locales/en.json](locales/en.json)
- [locales/zh-Hant.json](locales/zh-Hant.json)

Then print them:

```powershell
python scripts\i18n.py --locale zh-Hant --key flow.main_menu
```

---

## 4. ID and naming rules

| Kind | Pattern | Example |
|------|---------|---------|
| Spec file | `{name}.en.md` / `{name}.zh-Hant.md` | `order-inquiry.en.md` |
| Requirement | `REQ-NN` | `REQ-03` |
| Test case | `TC-NN` (same NN as REQ) | `TC-03` |
| Error path (optional) | `EP-NN` | `EP-02` |
| Locale code | `en` or `zh-Hant` only | — |

Checklist before you finish a flow:

- [ ] Every `REQ-*` has a `TC-*`
- [ ] Diagram nodes mention the same IDs
- [ ] EN and zh-Hant files both exist and share IDs
- [ ] Cross-links between spec / testcases / diagrams are updated

---

## 5. Using the locale CLI

List all keys for a locale:

```powershell
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant
```

Print one key:

```powershell
python scripts\i18n.py --locale en --key label.testcases
python scripts\i18n.py --locale zh-Hant --key label.testcases
```

If Chinese characters look wrong in an old Windows console, set UTF-8 for the session:

```powershell
$env:PYTHONIOENCODING='utf-8'
python scripts\i18n.py --locale zh-Hant
```

---

## 6. What not to do

- Do not add gettext, babel, i18next, or translation APIs.
- Do not invent a third locale unless you extend `scripts/i18n.py` and both JSON files on purpose.
- Do not treat this folder as part of `as400_hod` — it is a standalone documentation kit.

---

## 7. Quick reference

| Goal | Action |
|------|--------|
| New flow | Copy `templates/*` → `specs/` + `testcases/` + `diagrams/` (EN + TC) |
| Traceability | `REQ-NN` = `TC-NN` = diagram labels |
| Labels | Edit `locales/*.json`, query with `scripts/i18n.py` |
| Sample | Start from `SAMPLE-flow.*.md` |
