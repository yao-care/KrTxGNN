---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan：肺動脈高壓到肺動靜脈畸形

## 一句話總結

Ambrisentan 是選擇性 ET-A 受體拮抗劑，全球批准用於肺動脈高壓（PAH）治療（美國商品名 Letairis、歐盟商品名 Volibris），但台灣目前無任何許可上市紀錄。TxGNN 模型以 **99.41%** 的預測分數，將**肺動靜脈畸形（Pulmonary Arteriovenous Malformation, PAVM）**列為首要預測新適應症；然而目前**無任何臨床試驗登錄**，僅有 **1 篇個案相關文獻**提供間接支持，整體根據強度有限。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 原有適應症 | 肺動脈高壓（PAH）— 全球批准，台灣未上市 |
| 預測新適應症 | 肺動靜脈畸形（Pulmonary Arteriovenous Malformation） |
| TxGNN 預測分數 | 99.41% |
| 根據水準 | L4 |
| 台灣上市現況 | ✗ 未上市 |
| 許可證數量 | 0 件 |
| 建議決策 | Hold |

---

## 為何此預測具有合理性？

Ambrisentan 選擇性阻斷 ET-A（內皮素受體 A）受體，抑制 ET-1 引起的肺血管平滑肌收縮與增生，臨床上核准用於降低肺血管阻力、改善 PAH 患者的運動耐受性。ET-A 訊號過度活化是多種 PAH 亞型的核心病理機轉。

PAVM 好發於遺傳性出血性毛細血管擴張症（HHT）患者，部分 HHT 患者可同時合併 PAH，ET-1 途徑在 HHT 血管病理中有明確參與。就此而言，ET-A 拮抗在理論上可能對 HHT 相關血管異常產生間接影響，此為 TxGNN 預測的機轉基礎。

然而，PAVM 的核心病理為**動靜脈結構性異常分流（AV shunting）**，本質上並非 ET-A 介導的血管收縮或重塑過程，與 Ambrisentan 作用機轉的關聯屬間接性。現有唯一文獻為 1 篇 HHT 合併 PAH 個案報告，未直接評估 Ambrisentan 對 PAVM 本身的療效，臨床轉譯可行性高度不確定。

---

## 臨床試驗根據

目前無已登錄的 Ambrisentan 用於肺動靜脈畸形的相關臨床試驗。

---

## 文獻根據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | 個案報告 | World J Clin Cases | HHT 合併 PAH 患者的臨床表現、治療經過及家族基因分析；屬背景文獻，未直接評估 Ambrisentan 對 PAVM 的療效 |

---

## 台灣上市資訊

Ambrisentan 目前在台灣**無任何藥品許可證**，尚未上市。如需於台灣進行相關臨床研究，須另行申請試驗用藥（IND）核可。

---

## 安全性注意事項

安全性資訊請參照原廠說明書及各國藥品監管機關公告。

---

## 結論與下一步

**決策：Hold**

**理由：**
PAVM 與 ET-A 機轉的關聯屬間接性，目前僅有 1 篇 HHT 合併 PAH 個案報告作為背景文獻（根據水準 L4），無任何針對 PAVM 的 Ambrisentan 臨床試驗登錄，根據強度不足以支持進一步評估。

**若要繼續推進，需要：**
- HHT/PAVM 患者中 ET-1 訊號角色的前臨床機轉研究
- 至少 1 項 Pilot 研究或病例系列，評估 Ambrisentan 在 HHT 相關 PAVM 患者的安全性與可行性
- 台灣試驗用藥（IND）申請規劃
- 詳細 MOA 數據補充（現列為 High 嚴重度缺口）

---

## 附錄：全部預測概覽（共 10 項）

> 本 Evidence Pack 為多適應症（multi）分析，TxGNN 共輸出 10 項預測。**最具臨床推進潛力者為 Rank 4（HIV 相關 PAH）**，具有直接 Phase 3 RCT 根據（L1），建議決策 **Proceed with Guardrails**，應優先評估。

| 排名 | 預測疾病 | TxGNN 分數 | 根據水準 | 臨床試驗 | 文獻 | 建議決策 |
|:---:|---------|:---------:|:------:|:-------:|:---:|:------:|
| 1 | 肺動靜脈畸形（PAVM） | 99.41% | L4 | 0 | 1 | Hold |
| 2 | 先天性心臟病相關 PAH | 99.37% | L2 | 9 | 18 | Research Question |
| 3 | 血吸蟲病相關 PAH | 99.30% | L5 | 0 | 0 | Hold |
| **4** | **HIV 感染相關 PAH** | **99.30%** | **L1** | **1** | **4** | **Proceed with Guardrails** |
| 5 | 慢性溶血性貧血相關 PAH | 99.30% | L5 | 0 | 0 | Hold |
| 6 | 結締組織病相關 PAH | 99.30% | L2 | 3 | 19 | Research Question |
| 7 | 牙周相關畸形症候群 | 99.19% | L5 | 0 | 20 † | Hold |
| 8 | 單純性頭皮稀毛症 | 99.15% | L5 | 0 | 0 | Hold |
| 9 | 多毛症 | 99.14% | L5 | 0 | 0 | Hold |
| 10 | Dandy-Walker 畸形症候群 | 99.12% | L5 | 0 | 0 | Hold |

> † Rank 7 的 20 篇文獻均為牙周病一般治療研究，無一與 Ambrisentan 直接相關，判定為背景雜訊（知識圖譜遠端稀疏連結）。

---

### Rank 4 重點摘要：HIV 相關 PAH（最高優先）

HIV 病毒蛋白（gp120、Tat）直接刺激肺血管內皮細胞 ET-1 過度分泌，並透過慢性免疫活化進一步放大 ET-A 訊號，驅動肺血管收縮與重塑——Ambrisentan 的選擇性 ET-A 拮抗與此病理機轉高度契合。

有 Phase 3 多中心雙盲安慰劑對照交叉試驗（[NCT00709956](https://clinicaltrials.gov/study/NCT00709956)，64 名 HIV-PAH 患者，COMPLETED）直接支持，為現有根據最強者。

**建議：** 以 Proceed with Guardrails 策略推進，並重點評估與 HIV 抗病毒藥物（尤其 CYP3A4/P-gp 抑制劑，如利托那韋類增效劑）的藥物交互作用風險。

---

### Rank 2 & 6 概況：CHD-PAH 與 CTD-PAH（次優先）

**先天性心臟病相關 PAH（Rank 2）**
異常血流剪切力與慢性容量超載顯著上調 ET-1 系統，Ambrisentan 機轉直接對應。共有 9 項臨床試驗，包含 Phase 3b 直接試驗（[NCT01808313](https://clinicaltrials.gov/study/NCT01808313)，134 名中國 PAH 患者）及兒科 PAH 延伸研究，佐以 18 篇文獻（含前瞻性世代研究）。根據水準 L2，建議 Research Question。

**結締組織病相關 PAH（Rank 6）**
自體免疫介導的血管內皮損傷顯著上調 ET-1，ET-A 拮抗機轉直接對應 CTD-PAH 核心病理。共有 3 項臨床試驗（含 2 項 COMPLETED），19 篇文獻（含 2 篇 Tier 1 Meta-analysis），AMBITION 試驗 CTD-PAH 亞群分析（[PMID 32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/)、[PMID 28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/)）提供重要佐證。根據水準 L2，建議 Research Question；欠缺大型 CTD-PAH 專屬 Phase 3 RCT 為主要根據缺口。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

