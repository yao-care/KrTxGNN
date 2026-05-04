---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cyclophosphamide：造血幹細胞移植預處理（台灣未上市）→ 骨髓性白血病 (Myeloid Leukemia)

## 一段摘要

Cyclophosphamide 是一種 DNA 烷化劑，全球廣泛應用於血液腫瘤化療及造血幹細胞移植（HSCT）預處理，但目前在台灣尚無上市許可。TxGNN 模型預測其對**骨髓性白血病（Myeloid Leukemia）**具有治療潛力，預測分數高達 **99.47%**；目前已有超過 **10 項臨床試驗**（含多項已完成 Phase 2/3 試驗）及 **20 篇文獻**（含系統性網絡統合分析）支持此預測方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 既有適應症 | 無（台灣未上市；全球用於淋巴瘤、乳癌、自體免疫疾病及 HSCT 預處理） |
| 預測新適應症 | 骨髓性白血病（Myeloid Leukemia） |
| TxGNN 預測分數 | 99.47% |
| 根據等級 | L1 |
| 台灣上市現況 | ✗ 未上市 |
| 許可證數 | 0 件 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Cyclophosphamide 是一種前驅藥（prodrug），經肝臟 CYP450 酶系統活化後，其活性代謝物磷醯胺氮芥（phosphoramide mustard）可與 DNA 雙鏈形成共價交叉鏈結，干擾 DNA 複製與轉錄，對快速增殖的惡性細胞具強效殺傷作用。目前台灣雖無上市許可，但 Cyclophosphamide 在全球急性骨髓性白血病（AML）治療中已扮演不可或缺的角色。

在 AML 治療架構中，Cyclophosphamide 主要發揮兩種核心功能：第一，作為**骨髓清除性預處理方案（Myeloablative Conditioning, MAC）**的核心成分——BuCy（Busulfan + Cyclophosphamide）是異體造血幹細胞移植前的標準預處理方案，藉由徹底清除患者自身造血系統，確保供者幹細胞有效植入；第二，作為**移植後環磷醯胺（Post-Transplant Cyclophosphamide, PTCy）**，利用其選擇性耗竭同種反應性 T 細胞的獨特免疫機制，成為目前最受矚目的 GVHD 預防策略，此機轉已在多項大規模隨機對照試驗中獲得充分驗證。

骨髓性白血病的病理生理特徵——DNA 修復通路高度活化、快速分裂的原始細胞群——與 Cyclophosphamide 的 DNA 烷化機轉高度契合。多項已完成的 Phase 2/3 試驗（最大達 431 人之隨機 Phase 3 試驗 NCT03959241）及 2023 年系統性網絡統合分析（PMID 36357773）均確認 Cyclophosphamide 在此適應症中的療效，使 TxGNN 預測具備充分且高等級的臨床支持。

---

## 臨床試驗根據

| 試驗編號 | 期別 | 狀態 | 受試者數 | 主要發現 |
|---------|------|------|----------|---------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | 完成 | 202 | 前瞻性隨機對照試驗，直接比較 G-CSF+Decitabine+BuCy 與標準 BuCy 預處理方案於 AML/MDS 繼發 AML 異體幹細胞移植的安全性與療效，為本報告最高等級直接證據 |
| [NCT03959241](https://clinicaltrials.gov/study/NCT03959241) | Phase 3 | 完成 | 431 | 多中心隨機 Phase 3 試驗（BMT CTN 1703），比較 Tac/MTX 與 PTCy/Tac/MMF 作為 RIC allo-PBSCT 之 GVHD 預防策略，Cyclophosphamide 為主要評估藥物 |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | 完成 | 213 | Cyclophosphamide/Fludarabine/TBI 骨髓清除性預處理用於非相關臍帶血移植治療血液惡性疾病，213 人完成提供大型安全性數據 |
| [NCT00134017](https://clinicaltrials.gov/study/NCT00134017) | Phase 2 | 完成 | 142 | 評估 HLA 相合相關與非相關捐贈者骨髓移植中 BuCy 預處理加移植後高劑量 Cyclophosphamide 作為 GVHD 預防的療效 |
| [NCT07249346](https://clinicaltrials.gov/study/NCT07249346) | Phase 2 | 招募中 | 124 | 多中心試驗直接評估低劑量移植後 Cyclophosphamide（25 mg/kg，第 +3 & +4 天）/Tacrolimus/Ruxolitinib 於 MAC allo-PBSCT 之 GVHD 預防效益 |
| [NCT00241358](https://clinicaltrials.gov/study/NCT00241358) | Phase 1/2 | 完成 | 92 | 評估含 Cyclophosphamide 預處理之 AMD3100 動員幹細胞移植方案於血液惡性腫瘤的安全性與療效 |
| [NCT00809276](https://clinicaltrials.gov/study/NCT00809276) | Phase 1/2 | 完成 | 92 | 研究 Fludarabine/IV Busulfan 預處理後移植後高劑量 Cyclophosphamide 免疫抑制，評估預防骨髓移植後 GVHD 的效益 |
| [NCT00723099](https://clinicaltrials.gov/study/NCT00723099) | Phase 2 | 完成 | 73 | 含 Cyclophosphamide 之減量強度預處理非相關臍帶血移植，支持 Cy 在 AML 異體移植脈絡下的應用 |
| [NCT06532084](https://clinicaltrials.gov/study/NCT06532084) | Phase 2 | 招募中 | 88 | 單中心隨機試驗，在含 PTCy 之 allo-HSCT 後比較 Sorafenib 維持治療對高危骨髓惡性腫瘤療效，提供現代 AML 移植實踐數據 |
| [NCT00691015](https://clinicaltrials.gov/study/NCT00691015) | Phase 2 | 完成 | 48 | 評估 Sirolimus/Tacrolimus/Thymoglobulin 於非相關捐贈者 HCT（含 Cyclophosphamide 預處理）之 GVHD 預防方案，提供比較性背景數據 |

---

## 文獻根據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | 系統性回顧與網絡統合分析 | Bone Marrow Transplantation | 貝葉斯網絡統合分析比較 AML allo-HSCT 完全緩解患者各 MAC 方案（含 BuCy）之療效，提供目前最高等級統合證據 |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | 前瞻性登記研究 | Haematologica | 分析 217 例 AML 接受 MAC+PTCy GVHD 預防移植之遺傳風險分類與預後，整體 2 年 OS 達 77%（95% CI：71–83） |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | 回溯性比較研究 | Future Oncology | 直接比較標準 BuCy 與 FluBu 骨髓清除性預處理方案於 AML allo-HSCT，評估療效相近性及毒性差異 |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | 回溯性研究 | Bone Marrow Transplantation | 分析 1,823 例中高危 AML（CR1）接受 PTCy allo-HSCT 之預處理強度（MAC vs RIC）與移植預後關係 |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | 回溯性研究 | European Journal of Haematology | 評估 RIC 與 MAC 對 65 歲以下 AML 患者接受 ATG+PTCy+Cyclosporine GVHD 預防方案的存活影響 |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Phase 2 研究報告 | Transplant Immunology | 探索 Cladribine+BuCy 強化預處理方案用於難治復發 AML allo-HSCT 的療效與安全性，提供 BuCy 基礎方案強化數據 |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | 回溯性研究 | Cytotherapy | 分析半相合 HCT（haplo-HCT with PTCy）治療 AML 之預後因子，確認 PTCy 在有效抑制 GVHD 同時維持移植物抗白血病效應 |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | 回溯性研究 | Int J Molecular Sciences | 首篇報告 PTCy 作為兒科 AML 相合捐贈者 HSCT 之 GVHD 預防策略的專項研究，補充兒科安全性與療效數據 |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | 回溯性研究 | Hematology/Oncology and SCT | 比較 BuCy 與 BuFlu 作為 AML/MDS allo-HCT 骨髓清除性預處理的比較效益，聚焦生活品質影響 |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | 回溯性研究 | Leukemia & Lymphoma | 報告高劑量 Cyclophosphamide（60 mg/kg）用於 AML 高白細胞症（≥50×10⁹/L）或白血球瘀滯症之細胞減量療效（27 例），初步確認緊急情境下的應用價值 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 既有細胞毒性藥物（烷化劑，Alkylating Agent；前驅藥，須經肝臟 CYP2B6/CYP3A4 活化） |
| 骨髓抑制風險 | **高**（於 MAC 劑量下骨髓清除為預期治療效果；PTCy 劑量下仍顯著，需密切監測全血球計數） |
| 催吐等級 | 中~高（靜脈，高劑量 >750 mg/m²）；低~中（口服或低劑量靜脈） |
| 監測項目 | 全血球計數（含白血球分類）、肝腎功能（ALT/AST/Cr）、電解質、尿液分析（含尿潛血，出血性膀胱炎監測）、血尿素氮 |
| 特殊處置 | 遵循細胞毒性藥物操作及廢棄規範；高劑量靜脈給藥時須搭配 MESNA 預防出血性膀胱炎；充分水化（≥3 L/day）；備妥 G-CSF 及輸血支持；密切監測感染跡象 |

---

## 安全性考量

安全性資訊請參照許可說明書。

---

## 結論與下一步

**決策：Proceed with Guardrails（附條件推進）**

**理由：**
支持 Cyclophosphamide 用於骨髓性白血病（AML）的臨床證據等級高，包含一項 431 人隨機 Phase 3 試驗（NCT03959241，已完成）、一項 202 人 Phase 2/3 試驗（NCT02744742，已完成），及 2023 年貝葉斯系統性網絡統合分析（PMID 36357773），整體根據等級達 **L1**；藥物的雙重應用機轉（BuCy 骨髓清除性預處理及 PTCy GVHD 預防）在機轉上明確，已在全球多個骨髓移植中心廣泛驗證，具備充分推進條件。

**如需推進，需要：**
- 取得 TFDA 仿單警語及禁忌症完整資料（目前為 **Blocking Data Gap DG001**，阻斷 S1 安全性初評）
- 補充完整的作用機轉（MOA）數據（目前為 **High 優先 Data Gap DG002**，影響機轉關聯性分析）
- 評估台灣 AML 臨床治療現況及現有替代方案（FluBu 等）之比較分析
- 建立特定高風險族群（老年患者、腎功能不全、既有心臟疾病）的安全性監測計畫
- 若擬申請台灣上市許可，須制定完整的 TFDA 法規策略，包括橋接試驗數據評估及藥品技術文件準備
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

