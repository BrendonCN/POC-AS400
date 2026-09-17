# 測試案例：Registration of Funds Transfer

| 欄位 | 值 |
|------|-----|
| 來源規格 | `specs\example _flow.en.md` |
| 文件編號 | TC-EXAMPLE-FLOW |

由大綱規格自動衍生；每個 `REQ-*` 對應一個 `TC-*`。

## 摘要

| TC 編號 | REQ | 標題 | 優先級 |
|---------|-----|------|--------|
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

## 功能鍵案例（摘錄）

### TC-FK-01 — F-1

| | |
|--|--|
| **按鍵** | F-1 |
| **規格列** | L31 |
| **標籤／脈絡** | F-1   Execution    (Execution)    <File Update & Print out> |
| **前置條件** | 畫面 S1 已顯示；欄位可輸入。 |
| **步驟** | 1. 依規格輸入欄位。2. 按下 F-1。3. 觀察訊息／畫面／游標。 |
| **預期結果** | 行為符合規格中「F-1   Execution    (Execution)    <File Update & Print out>」所述。 |
| **狀態** | |

### TC-FK-02 — F-3

| | |
|--|--|
| **按鍵** | F-3 |
| **規格列** | L32 |
| **標籤／脈絡** | F-3   Code Help    (Code)        <It indicates Code Help> |
| **前置條件** | 畫面 S1 已顯示；欄位可輸入。 |
| **步驟** | 1. 依規格輸入欄位。2. 按下 F-3。3. 觀察訊息／畫面／游標。 |
| **預期結果** | 行為符合規格中「F-3   Code Help    (Code)        <It indicates Code Help>」所述。 |
| **狀態** | |

### TC-FK-03 — F-5

| | |
|--|--|
| **按鍵** | F-5 |
| **規格列** | L33 |
| **標籤／脈絡** | F-5   Account Menu    (Termination)    <It goes to the previous screen> |
| **前置條件** | 畫面 S1 已顯示；欄位可輸入。 |
| **步驟** | 1. 依規格輸入欄位。2. 按下 F-5。3. 觀察訊息／畫面／游標。 |
| **預期結果** | 行為符合規格中「F-5   Account Menu    (Termination)    <It goes to the previ」所述。 |
| **狀態** | |

### TC-FK-04 — F-10

| | |
|--|--|
| **按鍵** | F-10 |
| **規格列** | L34 |
| **標籤／脈絡** | F-10   Re-Input    (Re-Input)    <It initialises the screen> |
| **前置條件** | 畫面 S1 已顯示；欄位可輸入。 |
| **步驟** | 1. 依規格輸入欄位。2. 按下 F-10。3. 觀察訊息／畫面／游標。 |
| **預期結果** | 行為符合規格中「F-10   Re-Input    (Re-Input)    <It initialises the screen>」所述。 |
| **狀態** | |

### TC-FK-05 — F-12

| | |
|--|--|
| **按鍵** | F-12 |
| **規格列** | L35 |
| **標籤／脈絡** | F-12   Confirm        (Confirmation)    <It verifies input value> |
| **前置條件** | 畫面 S1 已顯示；欄位可輸入。 |
| **步驟** | 1. 依規格輸入欄位。2. 按下 F-12。3. 觀察訊息／畫面／游標。 |
| **預期結果** | 行為符合規格中「F-12   Confirm        (Confirmation)    <It verifies input v」所述。 |
| **狀態** | |

## 需求對應案例

### TC-01 — Input & Output

| | |
|--|--|
| **REQ** | REQ-01 |
| **路徑** | 2 Input & Output > I Input & Output Files > ③ Input & Output |
| **規格列** | L14 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Input & Output」。 |
| **預期結果** | Cbc File     (CF) Dbc File     (DF) |
| **狀態** | |

### TC-02 — It executes First Reference.

| | |
|--|--|
| **REQ** | REQ-02 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > 1 It executes First Reference. |
| **規格列** | L24 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It executes First Reference.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-03 — It sets and indicates function keys using the sub-routine Indication of Function

| | |
|--|--|
| **REQ** | REQ-03 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > 2 It sets and indicates function keys using the sub-routine Indication of Function |
| **規格列** | L26 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It sets and indicates function keys using the sub-routine Indication of Function」。 |
| **預期結果** | Keys. |
| **狀態** | |

### TC-04 — The following function keys(Parameters) will be set:

| | |
|--|--|
| **REQ** | REQ-04 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > I The following function keys(Parameters) will be set: |
| **規格列** | L29 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「The following function keys(Parameters) will be set:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-05 — F-1   Execution    (Execution)    <File Update & Print out>

| | |
|--|--|
| **REQ** | REQ-05 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ① F-1   Execution    (Execution)    <File Update & Print out> |
| **規格列** | L31 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-1   Execution    (Execution)    <File Update & Print out>」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-06 — F-3   Code Help    (Code)        <It indicates Code Help>

| | |
|--|--|
| **REQ** | REQ-06 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ② F-3   Code Help    (Code)        <It indicates Code Help> |
| **規格列** | L32 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-3   Code Help    (Code)        <It indicates Code Help>」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-07 — F-5   Account Menu    (Termination)    <It goes to the previous screen>

| | |
|--|--|
| **REQ** | REQ-07 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ③ F-5   Account Menu    (Termination)    <It goes to the previous screen> |
| **規格列** | L33 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-5   Account Menu    (Termination)    <It goes to the previous screen>」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-08 — F-10   Re-Input    (Re-Input)    <It initialises the screen>

| | |
|--|--|
| **REQ** | REQ-08 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ④ F-10   Re-Input    (Re-Input)    <It initialises the screen> |
| **規格列** | L34 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-10   Re-Input    (Re-Input)    <It initialises the screen>」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-09 — F-12   Confirm        (Confirmation)    <It verifies input value>

| | |
|--|--|
| **REQ** | REQ-09 |
| **路徑** | 3 Specification > I Initial Process > ① Indication of Screen(S1) > ⑤ F-12   Confirm        (Confirmation)    <It verifies input value> |
| **規格列** | L35 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-12   Confirm        (Confirmation)    <It verifies input value>」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-10 — It executes the corresponding Process using input results(pressing   F-1  ).

| | |
|--|--|
| **REQ** | REQ-10 |
| **路徑** | 3 Specification > II Main Process > ② It executes the corresponding Process using input results(pressing   F-1  ). |
| **規格列** | L41 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It executes the corresponding Process using input results(pressing   F-1  ).」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-11 — It executes the transaction until   F-1  (Execution),   F-5  (Termination) has pressed

| | |
|--|--|
| **REQ** | REQ-11 |
| **路徑** | 3 Specification > II Main Process > ③ It executes the transaction until   F-1  (Execution),   F-5  (Termination) has pressed |
| **規格列** | L43 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It executes the transaction until   F-1  (Execution),   F-5  (Termination) has p」。 |
| **預期結果** | or the transaction is abnormal ending(File Error occurred). |
| **狀態** | |

### TC-12 — Key Operations

| | |
|--|--|
| **REQ** | REQ-12 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations |
| **規格列** | L59 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Key Operations」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-13 — F-1   (Execution)

| | |
|--|--|
| **REQ** | REQ-13 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > 1 F-1   (Execution) |
| **規格列** | L61 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-1   (Execution)」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-14 — It executes Error Checking.

| | |
|--|--|
| **REQ** | REQ-14 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > I It executes Error Checking. |
| **規格列** | L63 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It executes Error Checking.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-15 — If there is no error:

| | |
|--|--|
| **REQ** | REQ-15 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > ① If there is no error: |
| **規格列** | L65 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is no error:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-16 — If there is an error:

| | |
|--|--|
| **REQ** | REQ-16 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > ② If there is an error: |
| **規格列** | L69 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is an error:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-17 — If there is no error above, it executes the following processes:

| | |
|--|--|
| **REQ** | REQ-17 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > II If there is no error above, it executes the following processes: |
| **規格列** | L79 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is no error above, it executes the following processes:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-18 — It executes File Update.

| | |
|--|--|
| **REQ** | REQ-18 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > ① It executes File Update. |
| **規格列** | L81 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It executes File Update.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-19 — Show Yes/No message through Confirmation Message(subroutine).

| | |
|--|--|
| **REQ** | REQ-19 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > ② Show Yes/No message through Confirmation Message(subroutine). |
| **規格列** | L83 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Show Yes/No message through Confirmation Message(subroutine).」。 |
| **預期結果** | ・Parameter Message Contents "Hi there" |
| **狀態** | |

### TC-20 — F-3   (Code)

| | |
|--|--|
| **REQ** | REQ-20 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > 2 F-3   (Code) |
| **規格列** | L104 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-3   (Code)」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-21 — F-5   (Termination)

| | |
|--|--|
| **REQ** | REQ-21 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > 3 F-5   (Termination) |
| **規格列** | L110 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-5   (Termination)」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-22 — F-10   (Re-Input)

| | |
|--|--|
| **REQ** | REQ-22 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > 4 F-10   (Re-Input) |
| **規格列** | L114 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-10   (Re-Input)」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-23 — F-12   (Confirmation)

| | |
|--|--|
| **REQ** | REQ-23 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > 5 F-12   (Confirmation) |
| **規格列** | L118 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「F-12   (Confirmation)」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-24 — It executes Error Checking.

| | |
|--|--|
| **REQ** | REQ-24 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > I It executes Error Checking. |
| **規格列** | L120 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It executes Error Checking.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-25 — If there is no error:

| | |
|--|--|
| **REQ** | REQ-25 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > ① If there is no error: |
| **規格列** | L122 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is no error:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-26 — If there is an error:

| | |
|--|--|
| **REQ** | REQ-26 |
| **路徑** | 3 Specification > III Input Process > ② Key Operations > ② If there is an error: |
| **規格列** | L128 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is an error:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-27 — Field Checking

| | |
|--|--|
| **REQ** | REQ-27 |
| **路徑** | 3 Specification > IV Error Checking > ① Field Checking |
| **規格列** | L140 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Field Checking」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-28 — If it is EQ Initial Value(0), it becomes an error.

| | |
|--|--|
| **REQ** | REQ-28 |
| **路徑** | 3 Specification > IV Error Checking > ① Field Checking > I If it is EQ Initial Value(0), it becomes an error. |
| **規格列** | L144 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If it is EQ Initial Value(0), it becomes an error.」。 |
| **預期結果** | ・If it is an error, it sets “UM00001” to Message Code. . . . |
| **狀態** | |

### TC-29 — If there is no such a code, it becomes an error.

| | |
|--|--|
| **REQ** | REQ-29 |
| **路徑** | 3 Specification > IV Error Checking > ① Field Checking > I If there is no such a code, it becomes an error. |
| **規格列** | L152 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is no such a code, it becomes an error.」。 |
| **預期結果** | ・If it is an error, it sets “UM00067” to Message Code. |
| **狀態** | |

### TC-30 — If there is no error above, it sets Contents of Code to Contents of Branch

| | |
|--|--|
| **REQ** | REQ-30 |
| **路徑** | 3 Specification > IV Error Checking > ① Field Checking > II If there is no error above, it sets Contents of Code to Contents of Branch |
| **規格列** | L155 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is no error above, it sets Contents of Code to Contents of Branch」。 |
| **預期結果** | Code. |
| **狀態** | |

### TC-31 — It prints using fields which has been set by File Update.

| | |
|--|--|
| **REQ** | REQ-31 |
| **路徑** | 3 Specification > V Print Process > ① It prints using fields which has been set by File Update. |
| **規格列** | L160 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It prints using fields which has been set by File Update.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-32 — See Reference in Report Layout(P036_P1) for printing fields.

| | |
|--|--|
| **REQ** | REQ-32 |
| **路徑** | 3 Specification > V Print Process > ③ See Reference in Report Layout(P036_P1) for printing fields. |
| **規格列** | L166 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「See Reference in Report Layout(P036_P1) for printing fields.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-33 — If an error occurred when Print Process:

| | |
|--|--|
| **REQ** | REQ-33 |
| **路徑** | 3 Specification > V Print Process > ④ If an error occurred when Print Process: |
| **規格列** | L168 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If an error occurred when Print Process:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-34 — If it is a print error including spool control, it becomes an error.

| | |
|--|--|
| **REQ** | REQ-34 |
| **路徑** | 3 Specification > V Print Process > ④ If an error occurred when Print Process: > 1 If it is a print error including spool control, it becomes an error. |
| **規格列** | L170 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If it is a print error including spool control, it becomes an error.」。 |
| **預期結果** | ・If it is an error, it sets “031” to Error Code. |
| **狀態** | |

### TC-35 — It deletes spooled print data.

| | |
|--|--|
| **REQ** | REQ-35 |
| **路徑** | 3 Specification > V Print Process > ④ If an error occurred when Print Process: > 2 It deletes spooled print data. |
| **規格列** | L173 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It deletes spooled print data.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-36 — Set Branch Bank Number (work)             with Initial Value(0).

| | |
|--|--|
| **REQ** | REQ-36 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ① It executes the following initially. > 1 Set Branch Bank Number (work)             with Initial Value(0). |
| **規格列** | L188 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set Branch Bank Number (work)             with Initial Value(0).」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-37 — Set to Branch Bank Branch Number (work)     with Initial Value(0).

| | |
|--|--|
| **REQ** | REQ-37 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ① It executes the following initially. > 2 Set to Branch Bank Branch Number (work)     with Initial Value(0). |
| **規格列** | L189 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set to Branch Bank Branch Number (work)     with Initial Value(0).」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-38 — Set to Branch Bank Account Number (work)     with Initial Value(blank).

| | |
|--|--|
| **REQ** | REQ-38 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ① It executes the following initially. > 3 Set to Branch Bank Account Number (work)     with Initial Value(blank). |
| **規格列** | L190 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set to Branch Bank Account Number (work)     with Initial Value(blank).」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-39 — If there is no corresponding record, it becomes an error.

| | |
|--|--|
| **REQ** | REQ-39 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ② PHCNTF  It refers to PHCNTF for the corresponding record using Branch Code. > 1 If there is no corresponding record, it becomes an error. |
| **規格列** | L200 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is no corresponding record, it becomes an error.」。 |
| **預期結果** | ・If error occurs, set Message Code with "UME0003". |
| **狀態** | |

### TC-40 — If there is no error above, it executes the following processes:

| | |
|--|--|
| **REQ** | REQ-40 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: |
| **規格列** | L203 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If there is no error above, it executes the following processes:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-41 — If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an

| | |
|--|--|
| **REQ** | REQ-41 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > I If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an |
| **規格列** | L207 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If CNBAN1<Bank Account Number 1> EQ Initial Value(Blank), it becomes an」。 |
| **預期結果** | error. ・If error occurs, set Message Code with "UMM0008". |
| **狀態** | |

### TC-42 — Set Branch Bank Number (work)     with CNTBN1<Bank Number 1>.

| | |
|--|--|
| **REQ** | REQ-42 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ① Set Branch Bank Number (work)     with CNTBN1<Bank Number 1>. |
| **規格列** | L213 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set Branch Bank Number (work)     with CNTBN1<Bank Number 1>.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-43 — Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>.

| | |
|--|--|
| **REQ** | REQ-43 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ② Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>. |
| **規格列** | L214 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set Branch Bank Branch Number (work) with CNBBN1<Bank Branch Number 1>.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-44 — Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>.

| | |
|--|--|
| **REQ** | REQ-44 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ③ Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>. |
| **規格列** | L215 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set Branch Bank Account Number (work) with CNBAN1<Bank Account Number 1>.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-45 — If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an

| | |
|--|--|
| **REQ** | REQ-45 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > I If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an |
| **規格列** | L219 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If CNBAN2<Bank Account Number 2> EQ Initial Value(Blank), it becomes an」。 |
| **預期結果** | error. ・If error occurs, set Message Code with "UMM0008". |
| **狀態** | |

### TC-46 — Set Branch Bank Number (work)     with CNTBN2<Bank Number 2>.

| | |
|--|--|
| **REQ** | REQ-46 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ① Set Branch Bank Number (work)     with CNTBN2<Bank Number 2>. |
| **規格列** | L225 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set Branch Bank Number (work)     with CNTBN2<Bank Number 2>.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-47 — Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>.

| | |
|--|--|
| **REQ** | REQ-47 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ② Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>. |
| **規格列** | L226 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set Branch Bank Branch Number (work) with CNBBN2<Bank Branch Number 2>.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-48 — Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>.

| | |
|--|--|
| **REQ** | REQ-48 |
| **路徑** | 5 Calculation & Setting > I Setting of Branch Bank Account > ③ If there is no error above, it executes the following processes: > ③ Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>. |
| **規格列** | L227 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「Set Branch Bank Account Number (work) with CNBAN2<Bank Account Number 2>.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-49 — It becomes an error. It sets “003” to Error Code.

| | |
|--|--|
| **REQ** | REQ-49 |
| **路徑** | 7 File Update > I PHCNTF  It executes the following if it matches the condition. > ① It refers to PHCNTF for the corresponding record using Branch Code. > I It becomes an error. It sets “003” to Error Code. |
| **規格列** | L250 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「It becomes an error. It sets “003” to Error Code.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-50 — If it is Update Error, it executes the following processes:

| | |
|--|--|
| **REQ** | REQ-50 |
| **路徑** | 7 File Update > III For record update above, if the corresponding record cannot be updated(including > ① If it is Update Error, it executes the following processes: |
| **規格列** | L279 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If it is Update Error, it executes the following processes:」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

### TC-51 — If Error Code is not set, it sets Error Code.

| | |
|--|--|
| **REQ** | REQ-51 |
| **路徑** | 7 File Update > III For record update above, if the corresponding record cannot be updated(including > ① If it is Update Error, it executes the following processes: > 1 If Error Code is not set, it sets Error Code. |
| **規格列** | L281 |
| **前置條件** | 相關畫面／檔案可用。 |
| **步驟** | 1. 依路徑到達此步驟。2. 執行：「If Error Code is not set, it sets Error Code.」。 |
| **預期結果** | 符合規格敘述。 |
| **狀態** | |

## 訊息／錯誤代碼覆蓋

| 類型 | 代碼 |
|------|------|
| Message | UM00001 |
| Message | UM00067 |
| Message | UME0003 |
| Message | UMM0008 |
| Error | 003 |
| Error | 031 |
