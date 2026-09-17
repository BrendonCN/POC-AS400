# Logic diagrams: Registration of Funds Transfer

Source: `specs\example _flow.en.md`

## 1. Chapter structure

```mermaid
flowchart TD
  root([Spec])
  root --> ch1["1 Summary"]
  ch1 --> ch1_I["I some text here"]
  root --> ch2["2 Input & Output"]
  ch2 --> ch2_I["I Input & Output Files"]
  root --> ch3["3 Specification"]
  ch3 --> ch3_I["I Initial Process"]
  ch3 --> ch3_II["II Main Process"]
  ch3 --> ch3_III["III Input Process"]
  ch3 --> ch3_IV["IV Error Checking"]
  ch3 --> ch3_V["V Print Process"]
  root --> ch4["4 Appendix"]
  ch4 --> ch4_I["I The Screen Layout<Registration of Fun…"]
  ch4 --> ch4_II["II The Report Layout<Registration of Fu…"]
  root --> ch5["5 Calculation & Setting"]
  ch5 --> ch5_I["I Setting of Branch Bank Account"]
  root --> ch6["6 First Reference"]
  ch6 --> ch6_I["I It sets the following initially."]
  ch6 --> ch6_II["II It indicates the screen."]
  root --> ch7["7 File Update"]
  ch7 --> ch7_I["I PHCNTF It executes the following if i…"]
  ch7 --> ch7_III["III For record update above, if the cor…"]
```

## 2. F-1 Execution decision (error check → update → print)

```mermaid
flowchart TD
  startFk["Press F-1"] --> errChk{"Error checking"}
  errChk -->|Has error| rev["Reverse error fields"]
  rev --> msg["Show message first error"]
  msg --> cur["Cursor to first error field"]
  errChk -->|No error| clr["Clear message"]
  clr --> upd["File Update"]
  upd --> conf{"Confirmation Yes/No"}
  conf -->|Yes code 0| prn["Print Process"]
  conf -->|No| menu1["Accounting Menu"]
  prn --> menu2["Accounting Menu"]
  upd -->|Update error| pop["Error Help popup"]
  pop --> menu3["Accounting Menu"]
```

## 3. Main process loop

```mermaid
flowchart TD
  init["Initial Process screen S1"] --> input["Input each field"]
  input --> key{Function key}
  key -->|F-1| fkF1["F-1 F-1 Execution (Execution) <File…"]
  fkF1 --> input
  key -->|F-3| fkF3["F-3 F-3 Code Help (Code) <It indica…"]
  fkF3 --> input
  key -->|F-5| fkF5["F-5 F-5 Account Menu (Termination) …"]
  fkF5 --> input
  key -->|F-10| fkF10["F-10 F-10 Re-Input (Re-Input) <It i…"]
  fkF10 --> input
  key -->|F-12| fkF12["F-12 F-12 Confirm (Confirmation) <I…"]
  fkF12 --> input
  key -->|Abnormal / file error| endNode[End transaction]
```

## 4. Happy-path sequence (F-1)

```mermaid
sequenceDiagram
  participant Op as Operator
  participant Scr as ScreenS1
  participant Upd as FileUpdate
  participant Prn as PrintProcess
  Op->>Scr: Enter fields
  Op->>Scr: F-1 Execution
  Scr->>Scr: Error checking
  Scr->>Upd: Update if no error
  Upd->>Op: Confirmation message
  Op->>Prn: Yes
  Prn-->>Op: Print then menu
```

## 5. Requirement index (first 20)

```mermaid
flowchart LR
  REQ01["REQ-01: Input & Output"]
  REQ02["REQ-02: It executes First Reference."]
  REQ03["REQ-03: It sets and indicates funct…"]
  REQ04["REQ-04: The following function keys…"]
  REQ05["REQ-05: F-1 Execution (Execution) <…"]
  REQ06["REQ-06: F-3 Code Help (Code) <It in…"]
  REQ07["REQ-07: F-5 Account Menu (Terminati…"]
  REQ08["REQ-08: F-10 Re-Input (Re-Input) <I…"]
  REQ09["REQ-09: F-12 Confirm (Confirmation)…"]
  REQ10["REQ-10: It executes the correspondi…"]
  REQ11["REQ-11: It executes the transaction…"]
  REQ12["REQ-12: Key Operations"]
  REQ13["REQ-13: F-1 (Execution)"]
  REQ14["REQ-14: It executes Error Checking."]
  REQ15["REQ-15: If there is no error:"]
  REQ16["REQ-16: If there is an error:"]
  REQ17["REQ-17: If there is no error above,…"]
  REQ18["REQ-18: It executes File Update."]
  REQ19["REQ-19: Show Yes/No message through…"]
  REQ20["REQ-20: F-3 (Code)"]
```
