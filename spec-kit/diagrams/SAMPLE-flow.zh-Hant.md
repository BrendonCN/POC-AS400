# 邏輯圖：登入 → 主選單

| 欄位 | 值 |
|------|-----|
| 規格 | [SAMPLE-flow.zh-Hant.md](../specs/SAMPLE-flow.zh-Hant.md) |
| 測試案例 | [SAMPLE-flow.zh-Hant.md](../testcases/SAMPLE-flow.zh-Hant.md) |

## 1. 高階流程（REQ-01 … REQ-03）

```mermaid
flowchart TD
  startNode[開始] --> attachNode["附加工作階段 REQ-01 TC-01"]
  attachNode --> signOnNode["登入畫面可見"]
  signOnNode --> credsNode["輸入憑證 REQ-02 TC-02"]
  credsNode --> verifyNode["驗證主選單 REQ-03 TC-03"]
  verifyNode --> stopNode[停止]
```

## 2. 決策與錯誤路徑（REQ-04 … REQ-06）

```mermaid
flowchart TD
  actNode[執行動作] --> aliveDec{"工作階段存活？ REQ-06 TC-06"}
  aliveDec -->|否| abortNode[中止 停止]
  aliveDec -->|是| credsDec{"憑證正確？ REQ-04 TC-04"}
  credsDec -->|否| staySignOn[停留登入或錯誤]
  staySignOn --> failNode[失敗]
  credsDec -->|是| waitMenu[等待主選單]
  waitMenu --> timeoutDec{"逾時？ REQ-05 TC-05"}
  timeoutDec -->|是| failTimeout[失敗 逾時]
  timeoutDec -->|否| passMenu[通過 主選單]
  passMenu --> stopOk[停止]
```

## 3. 成功路徑時序

```mermaid
sequenceDiagram
  participant Op as 操作者
  participant Sess as 終端機工作階段
  participant Host as 主機應用

  Op->>Sess: 附加 REQ-01
  Sess-->>Op: 工作階段就緒
  Op->>Host: 使用者代號 密碼 Enter REQ-02
  Host-->>Sess: 主選單畫面
  Op->>Sess: 讀取畫面文字
  Sess-->>Op: 含主選單 REQ-03
```
