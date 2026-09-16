# Logic diagrams: Sign On → Main Menu

| Field | Value |
|-------|-------|
| Spec | [SAMPLE-flow.en.md](../specs/SAMPLE-flow.en.md) |
| Test cases | [SAMPLE-flow.en.md](../testcases/SAMPLE-flow.en.md) |

## 1. High-level flow (REQ-01 … REQ-03)

```mermaid
flowchart TD
  startNode[Start] --> attachNode["Attach session REQ-01 TC-01"]
  attachNode --> signOnNode["Sign On visible"]
  signOnNode --> credsNode["Enter credentials REQ-02 TC-02"]
  credsNode --> verifyNode["Verify Main Menu REQ-03 TC-03"]
  verifyNode --> stopNode[Stop]
```

## 2. Decisions and error paths (REQ-04 … REQ-06)

```mermaid
flowchart TD
  actNode[Perform action] --> aliveDec{"Session alive? REQ-06 TC-06"}
  aliveDec -->|No| abortNode[Abort stop]
  aliveDec -->|Yes| credsDec{"Credentials OK? REQ-04 TC-04"}
  credsDec -->|No| staySignOn[Stay on Sign On or error]
  staySignOn --> failNode[Fail]
  credsDec -->|Yes| waitMenu[Wait for Main Menu]
  waitMenu --> timeoutDec{"Timeout? REQ-05 TC-05"}
  timeoutDec -->|Yes| failTimeout[Fail timeout]
  timeoutDec -->|No| passMenu[Pass Main Menu]
  passMenu --> stopOk[Stop]
```

## 3. Sequence (happy path)

```mermaid
sequenceDiagram
  participant Op as Operator
  participant Sess as TerminalSession
  participant Host as HostApp

  Op->>Sess: Attach REQ-01
  Sess-->>Op: Session ready
  Op->>Host: User ID password Enter REQ-02
  Host-->>Sess: Main Menu screen
  Op->>Sess: Read screen text
  Sess-->>Op: Contains Main Menu REQ-03
```
