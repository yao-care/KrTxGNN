---
layout: default
title: Dactinomycin
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 9
---

# Dactinomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# DACTINOMYCIN：橫紋肌肉瘤（RMS）→ 復發緩解型多發性硬化症

## 一句話摘要

DACTINOMYCIN（放線菌素 D）為傳統 DNA 插入型細胞毒性抗腫瘤抗生素，長期作為 VAC 方案（Vincristine + Actinomycin D + Cyclophosphamide）核心藥物，廣泛用於橫紋肌肉瘤（RMS）及 Wilms tumor 等兒童惡性腫瘤治療，但目前在臺灣並無藥品許可。
TxGNN 模型預測其對**復發緩解型多發性硬化症（Relapsing-Remitting Multiple Sclerosis，RRMS）**可能有效，預測分數達 **99.58%**；
然而，目前**完全無臨床試驗或文獻**支持此方向，作用機轉與 RRMS 病理的橋接依據極為薄弱，判定為模型跨疾病類別假陽性之可能性高。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 既有適應症 | 橫紋肌肉瘤（RMS）、Wilms tumor 等兒童惡性腫瘤（臺灣未上市，依全球臨床使用記錄推定） |
| 預測新適應症 | 復發緩解型多發性硬化症（Relapsing-Remitting Multiple Sclerosis） |
| TxGNN 預測分數 | 99.58%（全候選排名第 7,522） |
| 根據水準 | L5（僅模型預測，無任何實際研究支持） |
| 臺灣上市現況 | ❌ 未上市 |
| 許可證數 | 0 件 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測可能成立？

目前 DACTINOMYCIN 詳細作用機轉資料缺失（Data Gap DG002）。根據現有文獻記載，DACTINOMYCIN 為 DNA 插入劑（intercalator），能嵌入 DNA 雙鏈並與之緊密結合，從而抑制 RNA 聚合酶活性、阻斷 mRNA 合成，對快速增殖的腫瘤細胞具直接毒殺效果。此機轉自 1960 年代起即支撐其在橫紋肌肉瘤 VAC 方案中超過 60 年的臨床使用歷史。

然而，**RRMS 的核心病理機轉與 DACTINOMYCIN 的藥理作用之間缺乏已知的直接橋接**。RRMS 的病理核心為 CD4⁺/CD8⁺ T 細胞介導的中樞神經系統自體免疫性脫髓鞘，現有有效療法（干擾素 β、natalizumab、ocrelizumab）均鎖定免疫調節或 B/T 細胞耗竭路徑，與 DNA 轉錄抑制機轉無直接關聯。腫瘤細胞（高增殖）與 T 細胞自體免疫（免疫活化）雖然都涉及細胞增殖，但治療邏輯根本不同。

此外，DACTINOMYCIN 的嚴重毒性側寫（骨髓抑制、黏膜炎、肝毒性、靜脈閉塞症）對需要長期慢性疾病管理的 RRMS 患者而言，風險/效益比極差。Evidence Pack 中的機轉分析亦明確指出，TxGNN 此高分（0.996）預測極可能屬於**跨疾病類別假陽性**現象，不具臨床推進價值。

---

## 臨床試驗根據

目前無 DACTINOMYCIN 用於復發緩解型多發性硬化症的相關臨床試驗登記。

---

## 文獻根據

目前無支持 DACTINOMYCIN 用於復發緩解型多發性硬化症的相關文獻。

---

## 臺灣上市資訊

DACTINOMYCIN 目前在臺灣**未上市**，無任何藥品許可證資料，無法提取本地許可適應症。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA 插入劑 / 抗腫瘤抗生素） |
| 骨髓抑制風險 | **高**（骨髓抑制為主要劑量限制性毒性，含中性球減少、血小板減少、全血球減少） |
| 嘔吐誘發性等級 | 中等度 |
| 監測項目 | CBC（含白血球分類）、肝功能（AST／ALT／總膽紅素）、腎功能、靜脈閉塞症徵象（體重急增、腹水、黃疸）|
| 取用防護 | 需依細胞毒性藥物取用規範執行特殊防護措施（手套、護目鏡、防護衣），避免皮膚及黏膜接觸 |

---

## 安全性考量

安全性資訊請參照許可事項。

> TFDA 仿單警語及禁忌資料尚缺（Data Gap DG001，嚴重性：Blocking），且 DDI 查詢無結果（total_count = 0），目前無法進行完整安全性初評。補充上述資料為進入下一評估階段的前提條件。

---

## 結論及後續步驟

**決策：Hold**

**理由：**
DACTINOMYCIN 用於 RRMS 無任何臨床試驗或文獻根據（根據水準 L5），DNA 插入機轉與 T 細胞自體免疫病理的橋接缺乏合理依據，且嚴重的骨髓抑制及肝毒性使其不適合用於慢性自體免疫疾病的長期治療情境。不建議在此方向投入研究資源。

**本 Evidence Pack 中值得優先評估的其他預測：**

Evidence Pack 共包含 9 項預測，以下 RMS 相關方向具有較強臨床根據，應優先規劃評估：

| 預測方向 | 排名 | 根據水準 | 建議決策 |
|---------|------|---------|---------|
| Parameningeal embryonal rhabdomyosarcoma | 5 | **L1** | **Proceed with Guardrails** |
| Prostate embryonal rhabdomyosarcoma | 6 | L3 | Research Question |
| Liver sarcoma | 7 | L3 | Research Question |
| Upper aerodigestive tract neoplasm | 8 | L2 | Research Question |
| Head and neck cancer | 9 | L2 | Research Question |

其中，**parameningeal embryonal RMS**（Rank 5）有多項 IRS Phase 3 RCT（含 PMID 19770373、10856103）直接確認 VAC 方案療效，機轉橋接最為合理，為本批次預測中最具推進價值的方向。

**進行任何方向的進一步評估前，需補充：**
- 完整 MOA 詳細資料（Data Gap DG002，影響機轉關聯性分析）
- TFDA 仿單完整警語及禁忌資訊（Data Gap DG001，Blocking 等級）
- 完整 DDI 評估（目前查詢無結果）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

