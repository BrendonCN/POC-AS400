# Technical specification: Sign On → Main Menu

| Field | Value |
|-------|-------|
| Document ID | SPEC-SAMPLE-FLOW |
| Version | 1.0 |
| Locales | `en`, `zh-Hant` |
| Related | [Test cases](../testcases/SAMPLE-flow.en.md), [Logic diagrams](../diagrams/SAMPLE-flow.en.md) |

## 1. Purpose

Define a generic green-screen style flow: attach to a live terminal session, complete Sign On, and verify the Main Menu. This is a worked example for the spec-kit traceability pattern (`REQ-*` → `TC-*` → diagram nodes).

## 2. Actors

| Actor | Role |
|-------|------|
| Operator | Person or automation that drives the session |
| Terminal session | Already-open emulator / host window |
| System under test | Host application presenting Sign On and Main Menu |

## 3. Preconditions

- Terminal session window is open and reachable.
- Operator knows a valid user ID and password (or test doubles).
- Screen layout is calibrated (row/column origin known) if cell-based actions are used.

## 4. Requirements

### REQ-01 — Attach session

The operator shall attach to an existing terminal session without requiring a new host connection from this document’s scope.

**Expected:** Session handle / window is available for subsequent actions.

### REQ-02 — Enter credentials

On the Sign On screen, the operator shall enter user ID and password into the designated fields and submit (Enter / equivalent AID key).

**Expected:** Credentials are accepted by the host; control advances past Sign On.

### REQ-03 — Verify Main Menu

After successful Sign On, the screen text shall contain a Main Menu indicator (e.g. label `Main Menu` or equivalent).

**Expected:** Verification succeeds within the agreed timeout.

### REQ-04 — Missing or invalid input

If user ID or password is empty or invalid, the system shall remain on Sign On (or show an error) and shall not present Main Menu.

**Expected:** Main Menu verification fails; Sign On (or error) remains visible.

### REQ-05 — Verification timeout

If Main Menu text does not appear within the timeout, the flow shall fail with a clear timeout outcome and stop further happy-path steps.

**Expected:** Timeout / fail status; no false Main Menu pass.

### REQ-06 — Session lost / abort

If the terminal session window closes or becomes unreachable mid-flow, the operator shall abort remaining steps.

**Expected:** Abort; no further click/type/wait against a dead session.

## 5. Happy-path steps

1. Attach to session (`REQ-01`).
2. Confirm Sign On screen is visible.
3. Enter user ID, tab/move to password, enter password, submit (`REQ-02`).
4. Wait until screen contains Main Menu (`REQ-03`).
5. Stop (`flow.stop`).

## 6. Error paths

| Path | Trigger | Outcome |
|------|---------|---------|
| EP-01 | Empty / invalid credentials | Stay on Sign On / error; fail `REQ-03` (`REQ-04`) |
| EP-02 | Slow or stuck host | Timeout on Main Menu wait (`REQ-05`) |
| EP-03 | Window closed | Abort remaining steps (`REQ-06`) |

## 7. Non-goals

- Establishing a new TN5250/TN3270 TCP connection.
- Full business menus beyond Main Menu.
- Automated translation services or third-party i18n frameworks.

## 8. Traceability

| REQ | Test case | Diagram |
|-----|-----------|---------|
| REQ-01 | TC-01 | Node `Attach` |
| REQ-02 | TC-02 | Node `Enter credentials` |
| REQ-03 | TC-03 | Node `Verify Main Menu` |
| REQ-04 | TC-04 | Decision `Credentials OK?` |
| REQ-05 | TC-05 | Decision `Timeout?` |
| REQ-06 | TC-06 | Decision `Session alive?` |
