# Logic diagrams: [TITLE]

| Field | Value |
|-------|-------|
| Spec | [link to specs/*.md](../specs/) |
| Test cases | [link to testcases/*.md](../testcases/) |

> Put Mermaid in fenced `mermaid` blocks. Label nodes with `REQ-*` / `TC-*` for traceability. Ship `*.en.md` and `*.zh-Hant.md`.

## 1. High-level flow

```mermaid
flowchart TD
  startNode[Start] --> step1["Step 1 REQ-01 TC-01"]
  step1 --> step2["Step 2 REQ-02 TC-02"]
  step2 --> stopNode[Stop]
```

## 2. Decisions / error paths

```mermaid
flowchart TD
  actNode[Perform action] --> decision{"Condition?"}
  decision -->|Yes| okNode[Continue]
  decision -->|No| failNode[Fail]
```

## 3. Sequence (optional)

```mermaid
sequenceDiagram
  participant A as Actor
  participant S as System
  A->>S: Action
  S-->>A: Result
```
