---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Brigatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Brigatinib：ALK 陽性非小細胞肺癌 → 牙齦纖維瘤病

## 一句話摘要

Brigatinib（ALUNBRIG™，DrugBank ID: DB12267）是新一代 ALK / EGFR 多靶點酪胺酸激酶抑制劑，原核准適應症為 **ALK 重排陽性之晚期或轉移性非小細胞肺癌（NSCLC）**（美國 FDA 2017 年核准）。  
TxGNN 模型以 **99.89%** 的高分預測其對**牙齦纖維瘤病（Fibromatosis, Gingival）**可能有效，  
然而目前**無任何臨床試驗或支持文獻**，屬純模型預測（L5），且機轉分析顯示此為高可能性偽陽性訊號。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 原核准適應症 | ALK 陽性晚期 / 轉移性非小細胞肺癌（美國 FDA 2017 年核准；韓國尚未上市） |
| 預測新適應症 | 牙齦纖維瘤病（Fibromatosis, Gingival） |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5（純模型預測，無實際研究支持） |
| 韓國上市狀況 | ✗ 未上市 |
| 許可證數量 | 0 件 |
| 建議決策 | **Hold** |

---

## 此預測是否合理？

Brigatinib 為新一代多靶點酪胺酸激酶抑制劑（TKI），主要靶點涵蓋 **ALK（Anaplastic Lymphoma Kinase）、EGFR、ROS1 及 IGF-1R**。目前詳細 MOA 資料尚缺，但根據多項 Phase 3 臨床試驗（ALTA-1L，PMID [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) / [34537440](https://pubmed.ncbi.nlm.nih.gov/34537440/)），其核心作用為選擇性抑制 ALK 激酶活性，並克服第一代 crizotinib 耐藥突變（如 G1202R、L1196M 等），用於 ALK 重排陽性晚期 NSCLC 之一線及後線治療。

牙齦纖維瘤病（Gingival Fibromatosis）屬良性纖維增生性疾病，病理機制涉及 **HRAS / KRAS / SOS1 / FGFR1** 基因突變，造成牙齦結締組織過度增殖與堆積。此驅動通路與 Brigatinib 主要靶點 ALK / EGFR 激酶抑制機制**無任何已知分子交集**，目前亦無任何臨床前或臨床資料顯示兩者之間存在治療關聯，缺乏直接的生物學再利用依據。

> ⚠️ **偽陽性警示**：TxGNN 高分預測可能源自知識圖譜中「纖維增生 → 腫瘤 → 激酶抑制劑」的間接圖譜鏈結所產生之偽陽性訊號，**不建議據此配置研究或開發資源**。

---

## 臨床試驗證據

現無針對牙齦纖維瘤病的相關臨床試驗登錄。

---

## 文獻證據

現無針對牙齦纖維瘤病的相關文獻。

---

## 韓國上市資訊

Brigatinib 目前在韓國尚未取得藥品許可，無任何上市許可記錄。全球核准方面，美國 FDA 已於 2017 年加速核准（後轉為完整核准）用於 ALK+ 轉移性 NSCLC，但韓國 MFDS 尚無許可記錄。

---

## 細胞毒性

Brigatinib 為抗腫瘤標靶治療藥物（ALK TKI），適用細胞毒性資訊如下：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶抗腫瘤藥物（第二代 ALK 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 低（非傳統細胞毒性化療；貧血、嗜中性球低下為少見副作用） |
| 催吐等級 | 低 |
| 監測項目 | 肺功能（間質性肺病 / 肺炎）、肝功能（ALT / AST / 膽紅素）、腎功能、心電圖（QTc 延長）、CBC（含分類計數） |
| 操作防護 | 依細胞毒性藥物操作規範處理；育齡及哺乳期人員應避免直接接觸 |

---

## 安全性考量

安全性資訊請參照藥品仿單。

> 目前韓國 MFDS 仿單警語、禁忌及藥物交互作用資料尚缺（屬阻礙性資料缺口），建議取得完整仿單後方可進行正式安全性初評（S1 階段）。

---

## 結論與下一步

**決策：Hold**

**理由：**  
牙齦纖維瘤病的驅動突變（HRAS / KRAS / SOS1 / FGFR1）與 Brigatinib 核心靶點（ALK / EGFR）無已知分子交集；目前無任何臨床試驗或直接文獻支持，L5 等級證據顯示此預測極可能為知識圖譜偽陽性，不建議投入資源。

**如需重新評估，應先具備以下條件：**
- 牙齦纖維瘤病組織樣本中 ALK 融合基因或 EGFR 激活突變之分子流行病學資料
- Brigatinib 詳細靶點選擇性及完整 MOA 資料（建議補充 DrugBank API 查詢）
- 韓國 MFDS 仿單完整安全性資料（警語、禁忌、藥物交互作用）

> 💡 **補充說明**：在本 Evidence Pack 的其他預測中，**NF2 相關神經鞘瘤病**（Rank 10，L3 等級）與**肺炎性肌纖維母細胞瘤亞群**（Rank 5 附帶機轉外推，L4 等級）已有早期臨床或臨床前證據支持 Brigatinib 的再利用潛力，評估優先順序上明顯高於本適應症，建議優先針對該兩項進行深入分析。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

