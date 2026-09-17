#!/usr/bin/env python3
"""Generate test cases and Mermaid diagrams from a parsed outline spec."""

from __future__ import annotations

import re
from pathlib import Path

from outline_parser import SpecDocument


def _slug(name: str) -> str:
    s = Path(name).name
    s = re.sub(r"\.(en|zh-Hant)\.md$", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\.md$", "", s, flags=re.IGNORECASE)
    s = s.replace("_", "-")
    s = re.sub(r"[^\w\-]+", "-", s, flags=re.UNICODE)
    s = re.sub(r"-+", "-", s).strip("-").lower()
    return s or "flow"


def generate_testcases_md(doc: SpecDocument, locale: str = "en") -> str:
    is_tc = locale == "zh-Hant"
    title = doc.title
    lines: list[str] = []

    if is_tc:
        lines += [
            f"# 測試案例：{title}",
            "",
            "| 欄位 | 值 |",
            "|------|-----|",
            f"| 來源規格 | `{doc.source}` |",
            f"| 文件編號 | TC-{_slug(doc.source).upper()} |",
            "",
            "由大綱規格自動衍生；每個 `REQ-*` 對應一個 `TC-*`。",
            "",
            "## 摘要",
            "",
            "| TC 編號 | REQ | 標題 | 優先級 |",
            "|---------|-----|------|--------|",
        ]
    else:
        lines += [
            f"# Test cases: {title}",
            "",
            "| Field | Value |",
            "|-------|-------|",
            f"| Source spec | `{doc.source}` |",
            f"| Document ID | TC-{_slug(doc.source).upper()} |",
            "",
            "Auto-derived from the outline specification; each `REQ-*` maps to one `TC-*`.",
            "",
            "## Summary",
            "",
            "| TC ID | REQ | Title | Priority |",
            "|-------|-----|-------|----------|",
        ]

    for req in doc.requirements:
        tc = req["id"].replace("REQ-", "TC-")
        pri = "P0" if any(x in req["title"] for x in ("F-1", "Error", "Update", "Print")) else "P1"
        lines.append(f"| {tc} | {req['id']} | {req['title'][:80]} | {pri} |")

    lines.append("")

    # Function-key focused cases (always useful for this style of spec)
    if is_tc:
        lines += ["## 功能鍵案例（摘錄）", ""]
    else:
        lines += ["## Function-key cases (extract)", ""]

    for i, fk in enumerate(doc.function_keys, start=1):
        tc_id = f"TC-FK-{i:02d}"
        if is_tc:
            lines += [
                f"### {tc_id} — {fk['key']}",
                "",
                "| | |",
                "|--|--|",
                f"| **按鍵** | {fk['key']} |",
                f"| **規格列** | L{fk['line']} |",
                f"| **標籤／脈絡** | {fk['label']} |",
                f"| **前置條件** | 畫面 S1 已顯示；欄位可輸入。 |",
                f"| **步驟** | 1. 依規格輸入欄位。2. 按下 {fk['key']}。3. 觀察訊息／畫面／游標。 |",
                f"| **預期結果** | 行為符合規格中「{fk['label'][:60]}」所述。 |",
                f"| **狀態** | |",
                "",
            ]
        else:
            lines += [
                f"### {tc_id} — {fk['key']}",
                "",
                "| | |",
                "|--|--|",
                f"| **Key** | {fk['key']} |",
                f"| **Spec line** | L{fk['line']} |",
                f"| **Label / context** | {fk['label']} |",
                f"| **Preconditions** | Screen S1 indicated; fields ready for input. |",
                f"| **Steps** | 1. Enter fields per Input Process. 2. Press {fk['key']}. "
                f"3. Observe message / screen / cursor. |",
                f"| **Expected** | Behaviour matches specification for “{fk['label'][:60]}”. |",
                f"| **Status** | |",
                "",
            ]

    if is_tc:
        lines += ["## 需求對應案例", ""]
    else:
        lines += ["## Requirement-mapped cases", ""]

    for req in doc.requirements:
        tc = req["id"].replace("REQ-", "TC-")
        if is_tc:
            lines += [
                f"### {tc} — {req['title'][:100]}",
                "",
                "| | |",
                "|--|--|",
                f"| **REQ** | {req['id']} |",
                f"| **路徑** | {req['path']} |",
                f"| **規格列** | L{req['line']} |",
                f"| **前置條件** | 相關畫面／檔案可用。 |",
                f"| **步驟** | 1. 依路徑到達此步驟。2. 執行：「{req['title'][:80]}」。 |",
                f"| **預期結果** | {req['detail'] or '符合規格敘述。'} |",
                f"| **狀態** | |",
                "",
            ]
        else:
            lines += [
                f"### {tc} — {req['title'][:100]}",
                "",
                "| | |",
                "|--|--|",
                f"| **REQ** | {req['id']} |",
                f"| **Path** | {req['path']} |",
                f"| **Spec line** | L{req['line']} |",
                f"| **Preconditions** | Related screen / files available. |",
                f"| **Steps** | 1. Reach this step via the path. 2. Perform: “{req['title'][:80]}”. |",
                f"| **Expected** | {req['detail'] or 'Matches specification text.'} |",
                f"| **Status** | |",
                "",
            ]

    if doc.message_codes or doc.error_codes:
        if is_tc:
            lines += ["## 訊息／錯誤代碼覆蓋", "", "| 類型 | 代碼 |", "|------|------|"]
        else:
            lines += ["## Message / error code coverage", "", "| Type | Code |", "|------|------|"]
        for c in doc.message_codes:
            lines.append(f"| Message | {c} |")
        for c in doc.error_codes:
            lines.append(f"| Error | {c} |")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def _safe_mermaid_label(text: str, limit: int = 40) -> str:
    t = re.sub(r'["\[\]\{\}]', "", text)
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) > limit:
        t = t[: limit - 1] + "…"
    return t


def generate_diagrams_md(doc: SpecDocument, locale: str = "en") -> str:
    is_tc = locale == "zh-Hant"
    title = doc.title
    lines: list[str] = []

    if is_tc:
        lines += [
            f"# 邏輯圖：{title}",
            "",
            f"來源：`{doc.source}`",
            "",
            "## 1. 章節結構",
            "",
            "```mermaid",
            "flowchart TD",
        ]
    else:
        lines += [
            f"# Logic diagrams: {title}",
            "",
            f"Source: `{doc.source}`",
            "",
            "## 1. Chapter structure",
            "",
            "```mermaid",
            "flowchart TD",
        ]

    lines.append("  root([Spec])")
    for ch in doc.chapters:
        cid = f"ch{ch.marker}"
        lines.append(f'  root --> {cid}["{_safe_mermaid_label(ch.marker + " " + ch.title)}"]')
        for roman in ch.children:
            if roman.kind != "roman":
                continue
            rid = f"{cid}_{roman.marker}"
            lines.append(
                f'  {cid} --> {rid}["{_safe_mermaid_label(roman.marker + " " + roman.title)}"]'
            )

    lines += ["```", ""]

    # F-1 execution decision flow (core of example _flow)
    if is_tc:
        lines += ["## 2. F-1 執行決策（錯誤檢查 → 更新 → 列印）", "", "```mermaid", "flowchart TD"]
        lines += [
            '  startFk[按下 F-1] --> errChk{錯誤檢查}',
            '  errChk -->|有錯誤| rev[反白錯誤欄位]',
            '  rev --> msg[顯示訊息 第一個錯誤]',
            '  msg --> cur[游標到第一個錯誤欄]',
            '  errChk -->|無錯誤| clr[清除訊息]',
            '  clr --> upd[檔案更新]',
            '  upd --> conf{確認訊息 Yes/No}',
            '  conf -->|Yes 0| prn[列印處理]',
            '  conf -->|No| menu1[回會計選單]',
            '  prn --> menu2[回會計選單]',
            '  upd -->|更新錯誤| pop[錯誤說明快顯]',
            '  pop --> menu3[回會計選單]',
        ]
    else:
        lines += [
            "## 2. F-1 Execution decision (error check → update → print)",
            "",
            "```mermaid",
            "flowchart TD",
            '  startFk["Press F-1"] --> errChk{"Error checking"}',
            '  errChk -->|Has error| rev["Reverse error fields"]',
            '  rev --> msg["Show message first error"]',
            '  msg --> cur["Cursor to first error field"]',
            '  errChk -->|No error| clr["Clear message"]',
            '  clr --> upd["File Update"]',
            '  upd --> conf{"Confirmation Yes/No"}',
            '  conf -->|Yes code 0| prn["Print Process"]',
            '  conf -->|No| menu1["Accounting Menu"]',
            '  prn --> menu2["Accounting Menu"]',
            '  upd -->|Update error| pop["Error Help popup"]',
            '  pop --> menu3["Accounting Menu"]',
        ]
    lines += ["```", ""]

    # Main process loop
    if is_tc:
        lines += [
            "## 3. 主處理迴圈",
            "",
            "```mermaid",
            "flowchart TD",
            "  init[初期處理 畫面S1] --> input[輸入各欄位]",
            "  input --> key{功能鍵}",
        ]
    else:
        lines += [
            "## 3. Main process loop",
            "",
            "```mermaid",
            "flowchart TD",
            '  init["Initial Process screen S1"] --> input["Input each field"]',
            "  input --> key{Function key}",
        ]

    for fk in doc.function_keys:
        nid = "fk" + fk["key"].replace("-", "")
        label = _safe_mermaid_label(f'{fk["key"]} {fk["label"]}', 36)
        lines.append(f'  key -->|{fk["key"]}| {nid}["{label}"]')
        lines.append(f"  {nid} --> input")

    lines.append('  key -->|Abnormal / file error| endNode[End transaction]')
    lines += ["```", ""]

    # Sequence for happy path
    if is_tc:
        lines += [
            "## 4. 成功路徑時序（F-1）",
            "",
            "```mermaid",
            "sequenceDiagram",
            "  participant Op as 操作者",
            "  participant Scr as 畫面S1",
            "  participant Upd as 檔案更新",
            "  participant Prn as 列印處理",
            "  Op->>Scr: 輸入欄位",
            "  Op->>Scr: F-1 執行",
            "  Scr->>Scr: 錯誤檢查",
            "  Scr->>Upd: 無錯誤則更新",
            "  Upd->>Op: 確認訊息",
            "  Op->>Prn: Yes",
            "  Prn-->>Op: 列印後回選單",
            "```",
            "",
        ]
    else:
        lines += [
            "## 4. Happy-path sequence (F-1)",
            "",
            "```mermaid",
            "sequenceDiagram",
            "  participant Op as Operator",
            "  participant Scr as ScreenS1",
            "  participant Upd as FileUpdate",
            "  participant Prn as PrintProcess",
            "  Op->>Scr: Enter fields",
            "  Op->>Scr: F-1 Execution",
            "  Scr->>Scr: Error checking",
            "  Scr->>Upd: Update if no error",
            "  Upd->>Op: Confirmation message",
            "  Op->>Prn: Yes",
            "  Prn-->>Op: Print then menu",
            "```",
            "",
        ]

    # REQ index diagram (compact)
    if doc.requirements:
        if is_tc:
            lines += ["## 5. 需求索引（前 20 筆）", "", "```mermaid", "flowchart LR"]
        else:
            lines += ["## 5. Requirement index (first 20)", "", "```mermaid", "flowchart LR"]
        for req in doc.requirements[:20]:
            rid = req["id"].replace("-", "")
            lines.append(f'  {rid}["{req["id"]}: {_safe_mermaid_label(req["title"], 28)}"]')
        lines += ["```", ""]

    return "\n".join(lines).rstrip() + "\n"


def write_artifacts(
    doc: SpecDocument,
    out_dir: Path,
    basename: str | None = None,
    locale: str | None = None,
) -> dict[str, Path]:
    """Write testcases/ and diagrams/ markdown next to the kit root."""
    kit_root = out_dir
    loc = locale or "en"
    base = basename or _slug(doc.source)
    # Avoid double locale in basename
    base = re.sub(r"\.(en|zh-Hant)$", "", base)

    tc_path = kit_root / "testcases" / f"{base}.{loc}.md"
    dg_path = kit_root / "diagrams" / f"{base}.{loc}.md"
    tc_path.parent.mkdir(parents=True, exist_ok=True)
    dg_path.parent.mkdir(parents=True, exist_ok=True)
    tc_path.write_text(generate_testcases_md(doc, loc), encoding="utf-8")
    dg_path.write_text(generate_diagrams_md(doc, loc), encoding="utf-8")
    return {"testcases": tc_path, "diagrams": dg_path}
