#!/usr/bin/env python3
"""Parse hierarchical AS/400-style outline specs (stdlib only).

Recognises markers used in specs/example _flow.en.md:
  ・N, Roman I/II/…, ①②…, (1)(2)…, (I)(II)…, (①)(②)…, <1><2>…
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

# Major chapter: ・1  Summary  (requires ・ so "1 page contains…" is not a chapter)
_RE_CHAPTER = re.compile(r"^・\s*([1-9]\d*)\s+(.+)$")
# Roman section: I  Title / II  Main / Ⅴ  Print (2+ spaces after marker)
_RE_ROMAN = re.compile(
    r"^(Ⅴ|IV|III|II|I|V|X|IX|VIII|VII|VI)\s{2,}(.+)$",
    re.IGNORECASE,
)
_RE_CIRCLED = re.compile(r"^([①-⑳])\s+(.+)$")
_RE_PAREN_NUM = re.compile(r"^\((\d+)\)\s+(.+)$")
_RE_PAREN_ROMAN = re.compile(
    r"^\((Ⅴ|IV|III|II|I|V)\)\s+(.+)$",
    re.IGNORECASE,
)
_RE_PAREN_CIRCLED = re.compile(r"^\(([①-⑳])\)\s+(.+)$")
_RE_ANGLE = re.compile(r"^<(\d+)>\s+(.+)$")
_RE_NOTE = re.compile(r"^\*\s+(.+)$")
_RE_FK = re.compile(r"\bF-(\d+)\b", re.IGNORECASE)
_RE_MSG = re.compile(r"[\"“]?((?:UM|UME|UMM)\w*\d+)[\"”]?", re.IGNORECASE)
_RE_ERR = re.compile(
    r"(?:sets?\s+[\"“]?(\d{2,3})[\"”]?\s+to\s+Error\s+Code|"
    r"Error\s+Code[^\n]{0,40}?[\"“]?(\d{2,3})[\"”]?)",
    re.IGNORECASE,
)

@dataclass
class OutlineNode:
    kind: str
    marker: str
    title: str
    level: int
    line_no: int
    body: list[str] = field(default_factory=list)
    children: list[OutlineNode] = field(default_factory=list)

    def text(self) -> str:
        parts = [self.title] + self.body
        return "\n".join(p for p in parts if p.strip())


@dataclass
class SpecDocument:
    source: str
    title: str
    chapters: list[OutlineNode] = field(default_factory=list)
    function_keys: list[dict[str, str]] = field(default_factory=list)
    message_codes: list[str] = field(default_factory=list)
    error_codes: list[str] = field(default_factory=list)
    files: list[str] = field(default_factory=list)
    requirements: list[dict[str, str]] = field(default_factory=list)


def _norm_line(raw: str) -> str:
    # Normalise full-width spaces and odd bullets from Word paste
    return raw.replace("\u3000", " ").replace("\t", "    ").rstrip()


def _match_heading(line: str) -> tuple[str, str, str, int] | None:
    """Return (kind, marker, title, level) or None."""
    s = line.lstrip()
    if not s:
        return None

    m = _RE_CHAPTER.match(s)
    if m:
        return ("chapter", m.group(1), m.group(2).strip(), 1)

    m = _RE_ROMAN.match(s)
    if m:
        marker = m.group(1).upper().replace("Ⅴ", "V")
        return ("roman", marker, m.group(2).strip(), 2)

    m = _RE_CIRCLED.match(s)
    if m:
        return ("circled", m.group(1), m.group(2).strip(), 3)

    m = _RE_PAREN_CIRCLED.match(s)
    if m:
        return ("paren_circled", m.group(1), m.group(2).strip(), 4)

    m = _RE_PAREN_ROMAN.match(s)
    if m:
        return ("paren_roman", m.group(1).upper().replace("Ⅴ", "V"), m.group(2).strip(), 4)

    m = _RE_PAREN_NUM.match(s)
    if m:
        return ("paren_num", m.group(1), m.group(2).strip(), 4)

    m = _RE_ANGLE.match(s)
    if m:
        return ("angle", m.group(1), m.group(2).strip(), 5)

    m = _RE_NOTE.match(s)
    if m:
        return ("note", "*", m.group(1).strip(), 6)

    return None


def parse_outline(text: str, source: str = "") -> SpecDocument:
    lines = [_norm_line(ln) for ln in text.splitlines()]
    root_children: list[OutlineNode] = []
    stack: list[OutlineNode] = []
    doc_title = ""

    for i, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        heading = _match_heading(line)
        if heading is None:
            if stack:
                stack[-1].body.append(line.strip())
            continue

        kind, marker, title, level = heading
        node = OutlineNode(kind=kind, marker=marker, title=title, level=level, line_no=i)

        if kind == "chapter" and marker == "1" and not doc_title:
            # Prefer Summary title; else first chapter title
            doc_title = title

        while stack and stack[-1].level >= level:
            stack.pop()

        if stack:
            stack[-1].children.append(node)
        else:
            root_children.append(node)
        stack.append(node)

    if not doc_title and root_children:
        doc_title = root_children[0].title

    doc = SpecDocument(source=source, title=doc_title or Path(source).stem, chapters=root_children)
    _enrich(doc)
    return doc


def _walk(nodes: list[OutlineNode]):
    for n in nodes:
        yield n
        yield from _walk(n.children)


def _enrich(doc: SpecDocument) -> None:
    fk_seen: set[str] = set()
    msg_seen: set[str] = set()
    err_seen: set[str] = set()
    file_seen: set[str] = set()
    reqs: list[dict[str, str]] = []
    req_n = 0

    # Prefer a business title from appendix / screen layout lines
    for node in _walk(doc.chapters):
        m = re.search(
            r"Screen Layout\s*<\s*([^>]+)\s*>",
            node.text(),
            re.IGNORECASE,
        )
        if m:
            doc.title = m.group(1).strip()
            break

    action_hint = re.compile(
        r"\b(F-\d+|error|update|print|input|execute|terminat|confirm|message|"
        r"rollback|insert|refer|sets?|indicates?)\b",
        re.IGNORECASE,
    )

    for node in _walk(doc.chapters):
        blob = node.text()

        for m in _RE_FK.finditer(blob):
            key = f"F-{m.group(1)}"
            if key not in fk_seen:
                fk_seen.add(key)
                doc.function_keys.append(
                    {"key": key, "label": node.title, "line": str(node.line_no)}
                )

        for m in _RE_MSG.finditer(blob):
            code = m.group(1).upper()
            if code not in msg_seen:
                msg_seen.add(code)
                doc.message_codes.append(code)

        for m in _RE_ERR.finditer(blob):
            code = (m.group(1) or m.group(2) or "").strip()
            if code and code not in err_seen:
                err_seen.add(code)
                doc.error_codes.append(code)

        for token in re.findall(r"\b(PH[A-Z0-9]{3,})\b", blob):
            if token not in file_seen:
                file_seen.add(token)
                doc.files.append(token)

        # Actionable headings only (avoid every tiny leaf)
        if node.kind not in {"circled", "paren_num", "paren_circled", "paren_roman"}:
            continue
        if len(node.title) < 12:
            continue
        if node.title.lower().startswith("disc"):
            continue
        if not action_hint.search(node.title) and not action_hint.search(
            " ".join(node.body[:2])
        ):
            # Keep field-checking and key-operation parents
            if not re.search(
                r"\b(Checking|Operations|Process|Update|Print|Reference)\b",
                node.title,
                re.IGNORECASE,
            ):
                continue

        req_n += 1
        path = _path_of(doc.chapters, node)
        reqs.append(
            {
                "id": f"REQ-{req_n:02d}",
                "title": node.title[:120],
                "marker": f"{node.kind}:{node.marker}",
                "path": path,
                "line": str(node.line_no),
                "detail": " ".join(node.body)[:240],
            }
        )

    doc.requirements = reqs
    doc.message_codes = sorted(doc.message_codes)
    doc.error_codes = sorted(doc.error_codes)

def _path_of(chapters: list[OutlineNode], target: OutlineNode) -> str:
    path: list[str] = []

    def dfs(nodes: list[OutlineNode], trail: list[str]) -> bool:
        for n in nodes:
            here = trail + [f"{n.marker} {n.title}"]
            if n is target:
                path.extend(here)
                return True
            if dfs(n.children, here):
                return True
        return False

    dfs(chapters, [])
    return " > ".join(path)


def parse_file(path: Path) -> SpecDocument:
    text = path.read_text(encoding="utf-8")
    return parse_outline(text, source=str(path))


def to_json(doc: SpecDocument) -> str:
    return json.dumps(asdict(doc), ensure_ascii=False, indent=2)
