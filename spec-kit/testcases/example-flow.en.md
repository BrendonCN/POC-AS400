# Test cases: Registration of Funds Transfer

| Field | Value |
|-------|-------|
| Source spec | `specs\example _flow.en.md` |
| Document ID | TC-EXAMPLE-FLOW |

Auto-derived from the outline specification; each `REQ-*` maps to one `TC-*`.

## Summary

| TC ID | REQ | Title | Priority |
|-------|-----|-------|----------|
| TC-01 | REQ-01 | Input & Output | P1 |
| TC-02 | REQ-02 | It executes First Reference. | P1 |
| TC-03 | REQ-03 | It sets and indicates function keys using the sub-routine Indication of Function | P1 |
| TC-04 | REQ-04 | The following function keys(Parameters) will be set: | P1 |
| TC-05 | REQ-05 | F-1   Execution    (Execution)    <File Update & Print out> | P0 |
| TC-06 | REQ-06 | F-3   Code Help    (Code)        <It indicates Code Help> | P1 |
| TC-07 | REQ-07 | F-5   Account Menu    (Termination)    <It goes to the previous screen> | P1 |
| TC-08 | REQ-08 | F-10   Re-Input    (Re-Input)    <It initialises the screen> | P0 |
| TC-09 | REQ-09 | F-12   Confirm        (Confirmation)    <It verifies input value> | P0 |
| TC-10 | REQ-10 | It executes the corresponding Process using input results(pressing   F-1  ). | P0 |
| TC-11 | REQ-11 | It executes the transaction until   F-1  (Execution),   F-5  (Termination) has p | P0 |
| TC-12 | REQ-12 | Key Operations | P1 |
| TC-13 | REQ-13 | F-1   (Execution) | P0 |
| TC-14 | REQ-14 | It executes Error Checking. | P0 |
| TC-15 | REQ-15 | If there is no error: | P1 |
| TC-16 | REQ-16 | If there is an error: | P1 |
| TC-17 | REQ-17 | If there is no error above, it executes the following processes: | P1 |
| TC-18 | REQ-18 | It executes File Update. | P0 |
| TC-19 | REQ-19 | Show Yes/No message through Confirmation Message(subroutine). | P1 |
| TC-20 | REQ-20 | F-3   (Code) | P1 |
| TC-21 | REQ-21 | F-5   (Termination) | P1 |
| TC-22 | REQ-22 | F-10   (Re-Input) | P0 |
| TC-23 | REQ-23 | F-12   (Confirmation) | P0 |
| TC-24 | REQ-24 | It executes Error Checking. | P0 |
| TC-25 | REQ-25 | If there is no error: | P1 |
| TC-26 | REQ-26 | If there is an error: | P1 |
| TC-27 | REQ-27 | Field Checking | P1 |
| TC-28 | REQ-28 | If it is EQ Initial Value(0), it becomes an error. | P1 |
| TC-29 | REQ-29 | If there is no such a code, it becomes an error. | P1 |
| TC-30 | REQ-30 | If there is no error above, it sets Contents of Code to Contents of Branch | P1 |
| TC-31 | REQ-31 | It prints using fields which has been set by File Update. | P0 |
| TC-32 | REQ-32 | See Reference in Report Layout(P036_P1) for printing fields. | P1 |
| TC-33 | REQ-33 | If an error occurred when Print Process: | P0 |
| TC-34 | REQ-34 | If it is a print error including spool control, it becomes an error. | P1 |
| TC-35 | REQ-35 | It deletes spooled print data. | P1 |
| TC-36 | REQ-36 | Set Branch Bank Number (work)             with Initial Value(0). | P1 |
| TC-37 | REQ-37 | Set to Branch Bank Branch Number (work)     with Initial Value(0). | P1 |
| TC-38 | REQ-38 | Set to Branch Bank Account Number (work)     with Initial Value(blank). | P1 |
| TC-39 | REQ-39 | If there is no corresponding record, it becomes an error. | P1 |
| TC-40 | REQ-40 | If there is no error above, it executes the following processes: | P1 |
| TC-41 | REQ-41 | If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an | P1 |
| TC-42 | REQ-42 | Set Branch Bank Number (work)     with CNTBN1<Bank Number 1>. | P1 |
| TC-43 | REQ-43 | Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>. | P1 |
| TC-44 | REQ-44 | Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>. | P1 |
| TC-45 | REQ-45 | If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an | P1 |
| TC-46 | REQ-46 | Set Branch Bank Number (work)     with CNTBN2<Bank Number 2>. | P1 |
| TC-47 | REQ-47 | Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>. | P1 |
| TC-48 | REQ-48 | Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>. | P1 |
| TC-49 | REQ-49 | It becomes an error. It sets “003” to Error Code. | P0 |
| TC-50 | REQ-50 | If it is Update Error, it executes the following processes: | P0 |
| TC-51 | REQ-51 | If Error Code is not set, it sets Error Code. | P0 |

## Function-key cases (extract)

### TC-FK-01 — F-1

| | |
|--|--|
| **Key** | F-1 |
| **Spec line** | L31 |
| **Label / context** | F-1   Execution    (Execution)    <File Update & Print out> |
| **Preconditions** | Screen S1 indicated; fields ready for input. |
| **Steps** | 1. Enter fields per Input Process. 2. Press F-1. 3. Observe message / screen / cursor. |
| **Expected** | Behaviour matches specification for “F-1   Execution    (Execution)    <File Update & Print out>”. |
| **Status** | |

### TC-FK-02 — F-3

| | |
|--|--|
| **Key** | F-3 |
| **Spec line** | L32 |
| **Label / context** | F-3   Code Help    (Code)        <It indicates Code Help> |
| **Preconditions** | Screen S1 indicated; fields ready for input. |
| **Steps** | 1. Enter fields per Input Process. 2. Press F-3. 3. Observe message / screen / cursor. |
| **Expected** | Behaviour matches specification for “F-3   Code Help    (Code)        <It indicates Code Help>”. |
| **Status** | |

### TC-FK-03 — F-5

| | |
|--|--|
| **Key** | F-5 |
| **Spec line** | L33 |
| **Label / context** | F-5   Account Menu    (Termination)    <It goes to the previous screen> |
| **Preconditions** | Screen S1 indicated; fields ready for input. |
| **Steps** | 1. Enter fields per Input Process. 2. Press F-5. 3. Observe message / screen / cursor. |
| **Expected** | Behaviour matches specification for “F-5   Account Menu    (Termination)    <It goes to the previ”. |
| **Status** | |

### TC-FK-04 — F-10

| | |
|--|--|
| **Key** | F-10 |
| **Spec line** | L34 |
| **Label / context** | F-10   Re-Input    (Re-Input)    <It initialises the screen> |
| **Preconditions** | Screen S1 indicated; fields ready for input. |
| **Steps** | 1. Enter fields per Input Process. 2. Press F-10. 3. Observe message / screen / cursor. |
| **Expected** | Behaviour matches specification for “F-10   Re-Input    (Re-Input)    <It initialises the screen>”. |
| **Status** | |

### TC-FK-05 — F-12

| | |
|--|--|
| **Key** | F-12 |
| **Spec line** | L35 |
| **Label / context** | F-12   Confirm        (Confirmation)    <It verifies input value> |
| **Preconditions** | Screen S1 indicated; fields ready for input. |
| **Steps** | 1. Enter fields per Input Process. 2. Press F-12. 3. Observe message / screen / cursor. |
| **Expected** | Behaviour matches specification for “F-12   Confirm        (Confirmation)    <It verifies input v”. |
| **Status** | |

## Requirement-mapped cases

### TC-01 — Input & Output

| | |
|--|--|
| **REQ** | REQ-01 |
| **Path** | 2 Input & Output > I Input & Output Files > ③ Input & Output |
| **Spec line** | L14 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Input & Output”. |
| **Expected** | Cbc File     (CF) Dbc File     (DF) |
| **Status** | |

### TC-02 — It executes First Reference.

| | |
|--|--|
| **REQ** | REQ-02 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > 1 It executes First Reference. |
| **Spec line** | L24 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It executes First Reference.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-03 — It sets and indicates function keys using the sub-routine Indication of Function

| | |
|--|--|
| **REQ** | REQ-03 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > 2 It sets and indicates function keys using the sub-routine Indication of Function |
| **Spec line** | L26 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It sets and indicates function keys using the sub-routine Indication of Function”. |
| **Expected** | Keys. |
| **Status** | |

### TC-04 — The following function keys(Parameters) will be set:

| | |
|--|--|
| **REQ** | REQ-04 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > I The following function keys(Parameters) will be set: |
| **Spec line** | L29 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “The following function keys(Parameters) will be set:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-05 — F-1   Execution    (Execution)    <File Update & Print out>

| | |
|--|--|
| **REQ** | REQ-05 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ① F-1   Execution    (Execution)    <File Update & Print out> |
| **Spec line** | L31 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-1   Execution    (Execution)    <File Update & Print out>”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-06 — F-3   Code Help    (Code)        <It indicates Code Help>

| | |
|--|--|
| **REQ** | REQ-06 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ② F-3   Code Help    (Code)        <It indicates Code Help> |
| **Spec line** | L32 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-3   Code Help    (Code)        <It indicates Code Help>”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-07 — F-5   Account Menu    (Termination)    <It goes to the previous screen>

| | |
|--|--|
| **REQ** | REQ-07 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ③ F-5   Account Menu    (Termination)    <It goes to the previous screen> |
| **Spec line** | L33 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-5   Account Menu    (Termination)    <It goes to the previous screen>”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-08 — F-10   Re-Input    (Re-Input)    <It initialises the screen>

| | |
|--|--|
| **REQ** | REQ-08 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ④ F-10   Re-Input    (Re-Input)    <It initialises the screen> |
| **Spec line** | L34 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-10   Re-Input    (Re-Input)    <It initialises the screen>”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-09 — F-12   Confirm        (Confirmation)    <It verifies input value>

| | |
|--|--|
| **REQ** | REQ-09 |
| **Path** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ⑤ F-12   Confirm        (Confirmation)    <It verifies input value> |
| **Spec line** | L35 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-12   Confirm        (Confirmation)    <It verifies input value>”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-10 — It executes the corresponding Process using input results(pressing   F-1  ).

| | |
|--|--|
| **REQ** | REQ-10 |
| **Path** | 3 Specification > II Main Process > ② It executes the corresponding Process using input results(pressing   F-1  ). |
| **Spec line** | L41 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It executes the corresponding Process using input results(pressing   F-1  ).”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-11 — It executes the transaction until   F-1  (Execution),   F-5  (Termination) has pressed

| | |
|--|--|
| **REQ** | REQ-11 |
| **Path** | 3 Specification > II Main Process > ③ It executes the transaction until   F-1  (Execution),   F-5  (Termination) has pressed |
| **Spec line** | L43 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It executes the transaction until   F-1  (Execution),   F-5  (Termination) has p”. |
| **Expected** | or the transaction is abnormal ending(File Error occurred). |
| **Status** | |

### TC-12 — Key Operations

| | |
|--|--|
| **REQ** | REQ-12 |
| **Path** | 3 Specification > III Input Process > ② Key Operations |
| **Spec line** | L59 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Key Operations”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-13 — F-1   (Execution)

| | |
|--|--|
| **REQ** | REQ-13 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > 1 F-1   (Execution) |
| **Spec line** | L61 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-1   (Execution)”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-14 — It executes Error Checking.

| | |
|--|--|
| **REQ** | REQ-14 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > I It executes Error Checking. |
| **Spec line** | L63 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It executes Error Checking.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-15 — If there is no error:

| | |
|--|--|
| **REQ** | REQ-15 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > ① If there is no error: |
| **Spec line** | L65 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is no error:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-16 — If there is an error:

| | |
|--|--|
| **REQ** | REQ-16 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > ② If there is an error: |
| **Spec line** | L69 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is an error:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-17 — If there is no error above, it executes the following processes:

| | |
|--|--|
| **REQ** | REQ-17 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > II If there is no error above, it executes the following processes: |
| **Spec line** | L79 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is no error above, it executes the following processes:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-18 — It executes File Update.

| | |
|--|--|
| **REQ** | REQ-18 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > ① It executes File Update. |
| **Spec line** | L81 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It executes File Update.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-19 — Show Yes/No message through Confirmation Message(subroutine).

| | |
|--|--|
| **REQ** | REQ-19 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > ② Show Yes/No message through Confirmation Message(subroutine). |
| **Spec line** | L83 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Show Yes/No message through Confirmation Message(subroutine).”. |
| **Expected** | ・Parameter Message Contents "Hi there" |
| **Status** | |

### TC-20 — F-3   (Code)

| | |
|--|--|
| **REQ** | REQ-20 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > 2 F-3   (Code) |
| **Spec line** | L104 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-3   (Code)”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-21 — F-5   (Termination)

| | |
|--|--|
| **REQ** | REQ-21 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > 3 F-5   (Termination) |
| **Spec line** | L110 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-5   (Termination)”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-22 — F-10   (Re-Input)

| | |
|--|--|
| **REQ** | REQ-22 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > 4 F-10   (Re-Input) |
| **Spec line** | L114 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-10   (Re-Input)”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-23 — F-12   (Confirmation)

| | |
|--|--|
| **REQ** | REQ-23 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > 5 F-12   (Confirmation) |
| **Spec line** | L118 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “F-12   (Confirmation)”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-24 — It executes Error Checking.

| | |
|--|--|
| **REQ** | REQ-24 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > I It executes Error Checking. |
| **Spec line** | L120 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It executes Error Checking.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-25 — If there is no error:

| | |
|--|--|
| **REQ** | REQ-25 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > ① If there is no error: |
| **Spec line** | L122 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is no error:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-26 — If there is an error:

| | |
|--|--|
| **REQ** | REQ-26 |
| **Path** | 3 Specification > III Input Process > ② Key Operations > ② If there is an error: |
| **Spec line** | L128 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is an error:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-27 — Field Checking

| | |
|--|--|
| **REQ** | REQ-27 |
| **Path** | 3 Specification > IV Error Checking > ① Field Checking |
| **Spec line** | L140 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Field Checking”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-28 — If it is EQ Initial Value(0), it becomes an error.

| | |
|--|--|
| **REQ** | REQ-28 |
| **Path** | 3 Specification > IV Error Checking > ① Field Checking > I If it is EQ Initial Value(0), it becomes an error. |
| **Spec line** | L144 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If it is EQ Initial Value(0), it becomes an error.”. |
| **Expected** | ・If it is an error, it sets “UM00001” to Message Code. . . . |
| **Status** | |

### TC-29 — If there is no such a code, it becomes an error.

| | |
|--|--|
| **REQ** | REQ-29 |
| **Path** | 3 Specification > IV Error Checking > ① Field Checking > I If there is no such a code, it becomes an error. |
| **Spec line** | L152 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is no such a code, it becomes an error.”. |
| **Expected** | ・If it is an error, it sets “UM00067” to Message Code. |
| **Status** | |

### TC-30 — If there is no error above, it sets Contents of Code to Contents of Branch

| | |
|--|--|
| **REQ** | REQ-30 |
| **Path** | 3 Specification > IV Error Checking > ① Field Checking > II If there is no error above, it sets Contents of Code to Contents of Branch |
| **Spec line** | L155 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is no error above, it sets Contents of Code to Contents of Branch”. |
| **Expected** | Code. |
| **Status** | |

### TC-31 — It prints using fields which has been set by File Update.

| | |
|--|--|
| **REQ** | REQ-31 |
| **Path** | 3 Specification > V Print Process > ① It prints using fields which has been set by File Update. |
| **Spec line** | L160 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It prints using fields which has been set by File Update.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-32 — See Reference in Report Layout(P036_P1) for printing fields.

| | |
|--|--|
| **REQ** | REQ-32 |
| **Path** | 3 Specification > V Print Process > ③ See Reference in Report Layout(P036_P1) for printing fields. |
| **Spec line** | L166 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “See Reference in Report Layout(P036_P1) for printing fields.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-33 — If an error occurred when Print Process:

| | |
|--|--|
| **REQ** | REQ-33 |
| **Path** | 3 Specification > V Print Process > ④ If an error occurred when Print Process: |
| **Spec line** | L168 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If an error occurred when Print Process:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-34 — If it is a print error including spool control, it becomes an error.

| | |
|--|--|
| **REQ** | REQ-34 |
| **Path** | 3 Specification > V Print Process > ④ If an error occurred when Print Process: > 1 If it is a print error including spool control, it becomes an error. |
| **Spec line** | L170 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If it is a print error including spool control, it becomes an error.”. |
| **Expected** | ・If it is an error, it sets “031” to Error Code. |
| **Status** | |

### TC-35 — It deletes spooled print data.

| | |
|--|--|
| **REQ** | REQ-35 |
| **Path** | 3 Specification > V Print Process > ④ If an error occurred when Print Process: > 2 It deletes spooled print data. |
| **Spec line** | L173 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It deletes spooled print data.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-36 — Set Branch Bank Number (work)             with Initial Value(0).

| | |
|--|--|
| **REQ** | REQ-36 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ① It executes the following initially. > 1 Set Branch Bank Number (work)             with Initial Value(0). |
| **Spec line** | L188 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set Branch Bank Number (work)             with Initial Value(0).”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-37 — Set to Branch Bank Branch Number (work)     with Initial Value(0).

| | |
|--|--|
| **REQ** | REQ-37 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ① It executes the following initially. > 2 Set to Branch Bank Branch Number (work)     with Initial Value(0). |
| **Spec line** | L189 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set to Branch Bank Branch Number (work)     with Initial Value(0).”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-38 — Set to Branch Bank Account Number (work)     with Initial Value(blank).

| | |
|--|--|
| **REQ** | REQ-38 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ① It executes the following initially. > 3 Set to Branch Bank Account Number (work)     with Initial Value(blank). |
| **Spec line** | L190 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set to Branch Bank Account Number (work)     with Initial Value(blank).”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-39 — If there is no corresponding record, it becomes an error.

| | |
|--|--|
| **REQ** | REQ-39 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ② PHCNTF  It refers to PHCNTF for the corresponding record using Branch Code. > 1 If there is no corresponding record, it becomes an error. |
| **Spec line** | L200 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is no corresponding record, it becomes an error.”. |
| **Expected** | ・If error occurs, set Message Code with "UME0003". |
| **Status** | |

### TC-40 — If there is no error above, it executes the following processes:

| | |
|--|--|
| **REQ** | REQ-40 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: |
| **Spec line** | L203 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If there is no error above, it executes the following processes:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-41 — If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an

| | |
|--|--|
| **REQ** | REQ-41 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > I If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an |
| **Spec line** | L207 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an”. |
| **Expected** | error. ・If error occurs, set Message Code with "UMM0008". |
| **Status** | |

### TC-42 — Set Branch Bank Number (work)     with CNTBN1<Bank Number 1>.

| | |
|--|--|
| **REQ** | REQ-42 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ① Set Branch Bank Number (work)     with CNTBN1<Bank Number 1>. |
| **Spec line** | L213 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set Branch Bank Number (work)     with CNTBN1<Bank Number 1>.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-43 — Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>.

| | |
|--|--|
| **REQ** | REQ-43 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ② Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>. |
| **Spec line** | L214 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-44 — Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>.

| | |
|--|--|
| **REQ** | REQ-44 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ③ Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>. |
| **Spec line** | L215 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-45 — If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an

| | |
|--|--|
| **REQ** | REQ-45 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > I If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an |
| **Spec line** | L219 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an”. |
| **Expected** | error. ・If error occurs, set Message Code with "UMM0008". |
| **Status** | |

### TC-46 — Set Branch Bank Number (work)     with CNTBN2<Bank Number 2>.

| | |
|--|--|
| **REQ** | REQ-46 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ① Set Branch Bank Number (work)     with CNTBN2<Bank Number 2>. |
| **Spec line** | L225 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set Branch Bank Number (work)     with CNTBN2<Bank Number 2>.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-47 — Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>.

| | |
|--|--|
| **REQ** | REQ-47 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ② Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>. |
| **Spec line** | L226 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-48 — Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>.

| | |
|--|--|
| **REQ** | REQ-48 |
| **Path** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ③ Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>. |
| **Spec line** | L227 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-49 — It becomes an error. It sets “003” to Error Code.

| | |
|--|--|
| **REQ** | REQ-49 |
| **Path** | 7 File Update > I PHCNTF  It executes the following if it matches the condition. > ① It refers to PHCNTF for the corresponding record using Branch Code. > I It becomes an error. It sets “003” to Error Code. |
| **Spec line** | L250 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “It becomes an error. It sets “003” to Error Code.”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-50 — If it is Update Error, it executes the following processes:

| | |
|--|--|
| **REQ** | REQ-50 |
| **Path** | 7 File Update > III For record update above, if the corresponding record cannot be updated(including > ① If it is Update Error, it executes the following processes: |
| **Spec line** | L279 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If it is Update Error, it executes the following processes:”. |
| **Expected** | Matches specification text. |
| **Status** | |

### TC-51 — If Error Code is not set, it sets Error Code.

| | |
|--|--|
| **REQ** | REQ-51 |
| **Path** | 7 File Update > III For record update above, if the corresponding record cannot be updated(including > ① If it is Update Error, it executes the following processes: > 1 If Error Code is not set, it sets Error Code. |
| **Spec line** | L281 |
| **Preconditions** | Related screen / files available. |
| **Steps** | 1. Reach this step via the path. 2. Perform: “If Error Code is not set, it sets Error Code.”. |
| **Expected** | Matches specification text. |
| **Status** | |

## Message / error code coverage

| Type | Code |
|------|------|
| Message | UM00001 |
| Message | UM00067 |
| Message | UME0003 |
| Message | UMM0008 |
| Error | 003 |
| Error | 031 |
