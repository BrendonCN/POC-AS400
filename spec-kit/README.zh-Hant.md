# 規格套件（Spec Kit）

技術規格 → 測試案例與邏輯圖，僅支援**本地**英文與繁體中文（`zh-Hant`）。

不依賴任何第三方套件。本資料夾為獨立子專案，不依賴上層儲存庫其他套件。

English: [README.md](README.md)

**使用說明：** [HOWTO.zh-Hant.md](HOWTO.zh-Hant.md) · [HOWTO.md](HOWTO.md)

## 目錄結構

```
spec-kit/
  locales/          # en.json、zh-Hant.json
  scripts/i18n.py   # 標準函式庫語系載入
  specs/            # 技術規格（*.en.md / *.zh-Hant.md）
  testcases/        # 對應 REQ-* 的測試案例
  diagrams/         # Mermaid 邏輯圖
  templates/        # 空白範本
```

## 追蹤方式

1. 在 `specs/` 以 `REQ-01`、`REQ-02`… 撰寫需求。
2. 在 `testcases/` 以 `TC-01`、`TC-02`… 對應各需求。
3. 在 `diagrams/` 的 Mermaid 節點標上相同編號。
4. 英／繁檔案同步維護（編號相同、內容對譯）。

範例流程：**登入 → 主選單**

| 語系 | 規格 | 測試案例 | 邏輯圖 |
|------|------|----------|--------|
| 英文 | [SAMPLE-flow.en.md](specs/SAMPLE-flow.en.md) | [SAMPLE-flow.en.md](testcases/SAMPLE-flow.en.md) | [SAMPLE-flow.en.md](diagrams/SAMPLE-flow.en.md) |
| 繁中 | [SAMPLE-flow.zh-Hant.md](specs/SAMPLE-flow.zh-Hant.md) | [SAMPLE-flow.zh-Hant.md](testcases/SAMPLE-flow.zh-Hant.md) | [SAMPLE-flow.zh-Hant.md](diagrams/SAMPLE-flow.zh-Hant.md) |

## 本地虛擬環境（僅隔離用）

```powershell
cd spec-kit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
# 無需 pip install — requirements.txt 刻意不含套件
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant
python scripts\i18n.py --locale zh-Hant --key flow.main_menu
```

## 本地翻譯輔助

[`scripts/i18n.py`](scripts/i18n.py) 僅用 Python 標準函式庫載入 [`locales/en.json`](locales/en.json) 或 [`locales/zh-Hant.json`](locales/zh-Hant.json)。

建議使用命令列：

```powershell
python scripts\i18n.py --locale en
python scripts\i18n.py --locale zh-Hant --key project.title
```

## 新增流程

1. 複製 [`templates/technical-spec.md`](templates/technical-spec.md) → `specs/YOUR-flow.en.md` 與 `specs/YOUR-flow.zh-Hant.md`。
2. 複製 [`templates/testcases.md`](templates/testcases.md) → `testcases/…`。
3. 複製 [`templates/logic-diagram.md`](templates/logic-diagram.md) → `diagrams/…`。
4. 共用標籤請同時更新兩個 locale JSON。
