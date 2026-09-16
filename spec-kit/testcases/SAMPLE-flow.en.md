# Test cases: Sign On → Main Menu

| Field | Value |
|-------|-------|
| Spec | [SAMPLE-flow.en.md](../specs/SAMPLE-flow.en.md) |
| Diagrams | [SAMPLE-flow.en.md](../diagrams/SAMPLE-flow.en.md) |
| Document ID | TC-SAMPLE-FLOW |

Trace each case to a `REQ-*` ID. Status column is for manual or automation runs.

## Summary

| TC ID | REQ | Title | Priority |
|-------|-----|-------|----------|
| TC-01 | REQ-01 | Attach to open session | P0 |
| TC-02 | REQ-02 | Enter valid credentials and submit | P0 |
| TC-03 | REQ-03 | Verify Main Menu after Sign On | P0 |
| TC-04 | REQ-04 | Reject empty or invalid credentials | P1 |
| TC-05 | REQ-05 | Fail when Main Menu wait times out | P1 |
| TC-06 | REQ-06 | Abort when session window is closed | P0 |

---

### TC-01 — Attach to open session

| | |
|--|--|
| **REQ** | REQ-01 |
| **Preconditions** | Terminal session window is open. |
| **Steps** | 1. Attach to the session by agreed handle (title / process / window). 2. Confirm a usable session reference exists. |
| **Expected** | Attach succeeds; subsequent actions can target the session. |
| **Status** | |

### TC-02 — Enter valid credentials and submit

| | |
|--|--|
| **REQ** | REQ-02 |
| **Preconditions** | TC-01 passed; Sign On screen visible; valid test user available. |
| **Steps** | 1. Enter user ID. 2. Move to password field. 3. Enter password. 4. Submit (Enter / AID). |
| **Expected** | Host accepts input; flow leaves Sign On toward application screens. |
| **Status** | |

### TC-03 — Verify Main Menu after Sign On

| | |
|--|--|
| **REQ** | REQ-03 |
| **Preconditions** | TC-02 completed with valid credentials. |
| **Steps** | 1. Wait until screen text contains Main Menu indicator (within timeout). 2. Record pass/fail. |
| **Expected** | Main Menu text found within timeout → Pass. |
| **Status** | |

### TC-04 — Reject empty or invalid credentials

| | |
|--|--|
| **REQ** | REQ-04 |
| **Preconditions** | TC-01 passed; Sign On visible. |
| **Steps** | 1. Submit with empty user/password **or** invalid credentials. 2. Attempt Main Menu verification. |
| **Expected** | Remain on Sign On or error; Main Menu not shown → case Pass when rejection is observed. |
| **Status** | |

### TC-05 — Fail when Main Menu wait times out

| | |
|--|--|
| **REQ** | REQ-05 |
| **Preconditions** | Session attached; host will not show Main Menu in time (stub / blocked). |
| **Steps** | 1. Trigger wait-for-Main-Menu with a short timeout. 2. Observe outcome. |
| **Expected** | Timeout / fail; no false Pass. Happy-path steps after wait are not continued. |
| **Status** | |

### TC-06 — Abort when session window is closed

| | |
|--|--|
| **REQ** | REQ-06 |
| **Preconditions** | Mid-flow session available. |
| **Steps** | 1. Close or kill the terminal window. 2. Attempt another action (click / type / wait). |
| **Expected** | Flow aborts; no further successful actions against the dead session. |
| **Status** | |
