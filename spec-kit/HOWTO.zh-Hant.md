# 如何使用規格套件（Spec Kit）

本子專案的逐步說明。總覽：[README.zh-Hant.md](README.zh-Hant.md) · English：[HOWTO.md](HOWTO.md)

## 用途

把**技術規格**整理成：

1. **測試案例**（`TC-*` 對應 `REQ-*`）
2. **邏輯圖**（Mermaid，節點使用相同編號）

文件僅提供**英文**（`*.en.md`）與**繁體中文**（`*.zh-Hant.md`）。無雲端翻譯、無 pip 套件。

---

## 1. 一次性設定

在儲存庫根目錄執行：

```powershell
cd spec-kit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

不需 `pip install`。確認語系輔助程式可用：

```powershell
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant --key label.spec
```

預期：可正常印出英文與繁中標籤。

---

## 2. 先閱讀範例

依序開啟 **登入 → 主選單** 範例：

| 步驟 | 英文 | 繁體中文 |
|------|------|----------|
| 規格 | [specs/SAMPLE-flow.en.md](specs/SAMPLE-flow.en.md) | [specs/SAMPLE-flow.zh-Hant.md](specs/SAMPLE-flow.zh-Hant.md) |
| 測試案例 | [testcases/SAMPLE-flow.en.md](testcases/SAMPLE-flow.en.md) | [testcases/SAMPLE-flow.zh-Hant.md](testcases/SAMPLE-flow.zh-Hant.md) |
| 邏輯圖 | [diagrams/SAMPLE-flow.en.md](diagrams/SAMPLE-flow.en.md) | [diagrams/SAMPLE-flow.zh-Hant.md](diagrams/SAMPLE-flow.zh-Hant.md) |

請注意：

- 規格使用 **`REQ-01` … `REQ-06`**
- 測試案例使用對應的 **`TC-01` … `TC-06`**
- Mermaid 節點重複這些編號以利追蹤

---

## 3. 新增流程（建議步驟）

將 `my-flow` 換成你的短名稱（kebab-case，例如 `order-inquiry`）。

### 3.1 複製範本

```powershell
cd spec-kit
Copy-Item templates\technical-spec.md specs\my-flow.en.md
Copy-Item templates\technical-spec.md specs\my-flow.zh-Hant.md
Copy-Item templates\testcases.md      testcases\my-flow.en.md
Copy-Item templates\testcases.md      testcases\my-flow.zh-Hant.md
Copy-Item templates\logic-diagram.md  diagrams\my-flow.en.md
Copy-Item templates\logic-diagram.md  diagrams\my-flow.zh-Hant.md
```

### 3.2 先寫英文技術規格

編輯 `specs/my-flow.en.md`：

1. 填寫**文件編號**、目的、角色、前置條件。
2. 以 `REQ-01`、`REQ-02`… 新增需求（說明 + 預期結果）。
3. 列出成功路徑與錯誤路徑。
4. 填寫**追蹤對照**表（REQ → TC → 圖節點）。

### 3.3 由規格衍生測試案例

編輯 `testcases/my-flow.en.md`：

1. 每個 `REQ-*` 對應一個 `TC-*`（編號相同）。
2. 每個案例含：前置條件、步驟、預期結果。
3. 涵蓋成功路徑**以及**規格中的錯誤路徑（無效輸入、逾時、中止等）。

### 3.4 繪製邏輯圖

編輯 `diagrams/my-flow.en.md`：

1. 高階流程圖：附加／動作／驗證／停止（或實際步驟）。
2. 決策／錯誤分支圖。
3. 可選的時序圖。
4. 節點標籤寫上 `REQ-*` 與 `TC-*`。

Mermaid 可在 GitHub、GitLab 及多數 Markdown 預覽（含 VS Code／Cursor 的 Mermaid 擴充）顯示。

### 3.5 翻譯為繁體中文

以相同結構與**相同編號**維護：

- `specs/my-flow.zh-Hant.md`
- `testcases/my-flow.zh-Hant.md`
- `diagrams/my-flow.zh-Hant.md`

語系之間**不要**重新編號；只改文字內容。

### 3.6 共用標籤（選用）

若多份文件共用短標籤（例如「主選單」），請同時加入：

- [locales/en.json](locales/en.json)
- [locales/zh-Hant.json](locales/zh-Hant.json)

然後查詢：

```powershell
python scripts\i18n.py --locale zh-Hant --key flow.main_menu
```

---

## 4. 編號與命名規則

| 種類 | 格式 | 範例 |
|------|------|------|
| 規格檔名 | `{name}.en.md` / `{name}.zh-Hant.md` | `order-inquiry.en.md` |
| 需求 | `REQ-NN` | `REQ-03` |
| 測試案例 | `TC-NN`（與 REQ 同號） | `TC-03` |
| 錯誤路徑（選用） | `EP-NN` | `EP-02` |
| 語系代碼 | 僅 `en` 或 `zh-Hant` | — |

完成前檢查清單：

- [ ] 每個 `REQ-*` 都有對應 `TC-*`
- [ ] 邏輯圖節點含相同編號
- [ ] 英／繁檔案都存在且編號一致
- [ ] 規格／測試案例／邏輯圖之間的連結已更新

---

## 5. 語系命令列用法

列出某語系全部鍵值：

```powershell
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant
```

只印一個鍵：

```powershell
python scripts\i18n.py --locale en --key label.testcases
python scripts\i18n.py --locale zh-Hant --key label.testcases
```

若舊版 Windows 主控台中文亂碼，可先設定：

```powershell
$env:PYTHONIOENCODING='utf-8'
python scripts\i18n.py --locale zh-Hant
```

---

## 6. 請勿這樣做

- 不要加入 gettext、babel、i18next 或翻譯 API。
- 不要自行新增第三種語系，除非一併擴充 `scripts/i18n.py` 與兩個 JSON。
- 不要把本資料夾當成 `as400_hod` 的一部分——這是獨立文件套件。

---

## 7. 快速對照

| 目標 | 作法 |
|------|------|
| 新流程 | 複製 `templates/*` → `specs/` + `testcases/` + `diagrams/`（英＋繁） |
| 追蹤 | `REQ-NN` = `TC-NN` = 圖節點標籤 |
| 標籤 | 編輯 `locales/*.json`，用 `scripts/i18n.py` 查詢 |
| 範例 | 從 `SAMPLE-flow.*.md` 開始 |

## 8. 大綱規格管線（example _flow）

階層式 AS/400 規格（標記 `・1`、`I/II`、`①`、`(1)`、`F-1`、訊息代碼）請用標準函式庫管線產生產物：

```powershell
cd spec-kit
.\.venv\Scripts\Activate.ps1
python scripts\spec_pipeline.py --dry-run "specs\example _flow.en.md"
python scripts\spec_pipeline.py "specs\example _flow.en.md"
python scripts\spec_pipeline.py "specs\example _flow.en.md" --locale zh-Hant
```

輸出：`out/*.json`、`testcases/<basename>.*.md`、`diagrams/<basename>.*.md`。

