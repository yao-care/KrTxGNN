---
layout: default
title: Glycyrrhizic Acid
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Glycyrrhizic Acid
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

# Glycyrrhizic acid：無核准適應症 → 類風濕性關節炎

## 한 문장 요약

Glycyrrhizic acid（甘草酸）是從甘草根提取的天然三萜配糖體，目前台灣無核准藥品許可證。TxGNN 模型共預測 10 項新適應症，其中**類風濕性關節炎（Rheumatoid Arthritis）**擁有最完整的人類研究根據，支持文獻多達 **20 篇**並有 **1 項臨床試驗**在探索，在所有候選中根據水準最高（L3，決策階段 S2）；此外**巨細胞病毒感染**與**肺動脈高壓**亦各有 5 篇及 7 篇文獻的動物／臨床觀察支持。

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 基存適應症 | 台灣無核准適應症 |
| 予測新適應症 | 類風濕性關節炎（Rheumatoid Arthritis）|
| TxGNN 予測分數 | 97.82%（10 項預測中根據最完整者）|
| 根據水準 | L3（觀察研究 ＋ 系統性臨床前文獻）|
| 台灣市販現況 | ✗ 未上市 |
| 許可証數 | 0 件 |
| 権奨決定 | Research Question |

---

## 이 예측이 타당한 이유는？

Glycyrrhizic acid 為甘草（*Glycyrrhiza glabra* / *G. uralensis*）的主要活性成分，屬五環三萜結構，分子量 822.93 Da。其在腸道菌群作用下代謝為 18β-甘草次酸（18β-glycyrrhetinic acid, GA），後者亦具獨立藥理活性，並為多篇動物研究的受試成分。

目前相關文獻報告的甘草酸主要作用機轉包含：① 抑制 **NF-κB 信號通路**，減少 TNF-α、IL-1β、IL-6 等促炎細胞激素的轉錄；② 拮抗 **HMGB1（High Mobility Group Box 1）**蛋白，阻斷 HMGB1–RAGE–NF-κB 信號軸；③ 抑制 **11β-HSD2（11β-羥基類固醇脫氫酶2）**，干擾皮質醇─皮質酮的轉換平衡；④ 文獻報告 JAK1/2–STAT3 通路的調節效果（尚屬探索性）。

類風濕性關節炎的病理核心在於促炎細胞激素的過度活化（TNF-α、IL-6 主導）、滑膜纖維母細胞（FLS）的異常增殖，以及 RANKL 驅動的破骨細胞過度分化所造成的骨侵蝕。甘草酸的多重抗炎機轉——NF-κB 抑制、HMGB1 拮抗、JAK-STAT 調節、破骨細胞分化抑制——與 RA 現有藥物的主要治療靶點高度吻合，為此再利用假說提供清晰的機轉連結。然而，目前大量文獻以甘草酸作為複方成分或藥物遞送載體，缺乏純甘草酸單一製劑的隨機對照臨床試驗，臨床轉化路徑仍需系統性驗證。

---

## 所有預測適應症概覽

| 排序 | 疾病 | TxGNN 分數 | 根據水準 | 推薦 | 備註 |
|------|------|-----------|---------|------|------|
| 1 | Multiple Endocrine Neoplasia | 99.28% | L5 | Hold | 遺傳性多腺體腫瘤，無直接機轉 |
| 2 | Amenorrhea | 98.87% | L5 | Hold | 甘草酸已知可能促使月經紊亂，負向效應 |
| 3 | Hypoalphalipoproteinemia | 98.48% | L5 | Hold | 缺乏脂質調節機轉文獻 |
| 4 | Infectious Bovine Rhinotracheitis | 98.39% | L5 | Hold | 獸醫疾病，超出人類醫療範疇 |
| 5 | Malignant Catarrh | 98.39% | L5 | Hold | 反芻動物傳染病，超出人類醫療範疇 |
| 6 | Cytomegalovirus Infection | 98.24% | L3 | Research Question | 有抗病毒機轉 ＋ 兒科臨床觀察 |
| 7 | Acne（Disease）| 98.18% | L4 | Research Question | 抗炎機轉 ＋ 1 篇臨床干預報告 |
| 8 | Kyphoscoliotic Heart Disease | 97.96% | L5 | Hold | 機械性病因，無機轉連結 |
| 9 | Pulmonary Hypertension | 97.91% | L3 | Research Question | HMGB1 機轉 ＋ 多篇動物研究 |
| **10** | **Rheumatoid Arthritis** | **97.82%** | **L3** | **Research Question ★** | **根據最完整，1 CT ＋ 20 篇文獻** |

---

## 臨床試験根據（類風濕性關節炎）

| 試験番号 | 階段 | 状態 | 参加者数 | 主要発現 |
|---------|------|------|----------|---------|
| [NCT05788705](https://clinicaltrials.gov/study/NCT05788705) | Phase NA | UNKNOWN | 75 | 評估天然 JAK-STAT 抑制劑（含 Boswellic acid 及甘草酸相關成分）作為 RA 補充療法的療效，比較傳統 DMARDs（Methotrexate、生物製劑）治療 |

> ⚠️ Phase NA 表示此為非正式分期的探索性試驗；UNKNOWN 狀態代表資料更新缺失，無法確認是否完成，根據強度受限於 B 級相關性。

---

## 文獻根據（類風濕性關節炎）

| PMID | 年度 | 類型 | 期刊 | 主要発現 |
|------|-----|------|------|---------|
| [26498361](https://pubmed.ncbi.nlm.nih.gov/26498361/) | 2016 | Narrative Review | Oncotarget | 甘草酸（GL）及甘草次酸（GA）透過 COX-2/TxA2 通路對 RA 的潛在治療應用系統性綜述 |
| [40220871](https://pubmed.ncbi.nlm.nih.gov/40220871/) | 2025 | Preclinical | J Controlled Release | Sinomenine–甘草酸自組裝奈米水凝膠增強抗炎效果，改善 RA 動物模型症狀 |
| [38037139](https://pubmed.ncbi.nlm.nih.gov/38037139/) | 2023 | Preclinical | Chinese Medicine | 甘草酸聯合芒果苷廣泛抑制 RA 滑膜新生血管，減輕骨侵蝕（動物模型）|
| [35749826](https://pubmed.ncbi.nlm.nih.gov/35749826/) | 2022 | Preclinical | Phytomedicine | 甘草酸＋芒果苷逆轉 RA 能量代謝異常，改善疾病嚴重度（動物模型）|
| [31476301](https://pubmed.ncbi.nlm.nih.gov/31476301/) | 2019 | Preclinical | Arch Biochem Biophys | 甘草素聯合 PRP 透過自噬及氧化壓力機制改善膠原誘導 RA（大鼠模型）|
| [33593531](https://pubmed.ncbi.nlm.nih.gov/33593531/) | 2021 | Preclinical | Carbohydrate Polymers | 甘草酸／Budesonide 核殼奈米粒子對 RA 的協同抗炎及骨保護效果 |
| [12761187](https://pubmed.ncbi.nlm.nih.gov/12761187/) | 2003 | In vitro | J Biochemistry | 甘草酸與補體 C3 的結合特性及對 CK-2 的強效抑制（體外機轉驗證）|
| [38082504](https://pubmed.ncbi.nlm.nih.gov/38082504/) | 2024 | Mechanistic | Liver International | HMGB1 介導 Ferritinophagy 在 MTX 肝毒性的作用（甘草酸 HMGB1 靶點側面驗證）|

> 其餘 12 篇為含甘草成分的中藥複方（Shaoyao-Gancao-Fuzi 等）組學研究，甘草酸非單獨受試成分，直接適用性受限，未列入本表。

---

## 其他值得關注的預測適應症

### 巨細胞病毒感染（Cytomegalovirus Infection）— L3，Research Question

甘草酸具直接抗病毒機轉（干擾病毒粒子組裝與釋放），並透過 NF-κB 抑制減輕 CMV 引發的肝臟炎症反應。1990 年代有日本兒科小型臨床觀察，SNMC（含甘草酸的靜注製劑）在嬰兒 CMV 肝炎中顯示改善效果。

| PMID | 年度 | 類型 | 主要発現 |
|------|-----|------|---------|
| [8073426](https://pubmed.ncbi.nlm.nih.gov/8073426/) | 1994 | 臨床觀察（兒科）| SNMC 靜注對 CMV 相關嬰兒肝功能異常有明確改善（Tohoku J Exp Med）|
| [8193264](https://pubmed.ncbi.nlm.nih.gov/8193264/) | 1993 | 臨床觀察（兒科）| 口服甘草酸改善 CMV 相關嬰兒肝功能異常，含長期追蹤 |
| [8283138](https://pubmed.ncbi.nlm.nih.gov/8283138/) | 1994 | In vitro | 甘草酸抑制 U-937 及 MRC-5 細胞中 HCMV 病毒抗原表達（直接抗病毒確認）|
| [20416218](https://pubmed.ncbi.nlm.nih.gov/20416218/) | 2010 | 臨床（複方）| 複方甘草酸製劑對 CMV 肝炎兒童的 D-dimer 及 vWF 凝血指標研究 |

---

### 肺動脈高壓（Pulmonary Hypertension）— L3，Research Question

最強機轉路徑：甘草酸透過抑制 HMGB1，阻斷 HMGB1–RAGE–NF-κB 信號軸，減輕肺血管炎症與血管重塑。代謝物 18β-甘草次酸亦有高原性肺高壓大鼠模型資料。

| PMID | 年度 | 類型 | 主要発現 |
|------|-----|------|---------|
| [25420924](https://pubmed.ncbi.nlm.nih.gov/25420924/) | 2014 | 動物研究 | 甘草酸抑制 HMGB1，顯著減輕 MCT 誘發 PAH 及肺血管重塑（大鼠模型）|
| [30517029](https://pubmed.ncbi.nlm.nih.gov/30517029/) | 2019 | 機轉研究 | HMGB1 在 PAH 發展中的必要性機制驗證（甘草酸主要靶點確認）|
| [34419454](https://pubmed.ncbi.nlm.nih.gov/34419454/) | 2021 | 動物研究 | 18β-甘草次酸對高原性肺高壓大鼠的代謝組學保護效果 |
| [7613529](https://pubmed.ncbi.nlm.nih.gov/7613529/) | 1995 | 動物研究 | 甘草酸飲水給藥對大鼠右心房壓及肺血管的影響（最早期直接動物資料）|

---

### 痤瘡（Acne）— L4，Research Question

甘草酸透過抑制 NF-κB 及 IL-1β/TNF-α，可減輕 *C. acnes* 誘發的皮脂腺炎症。有 1 篇中文臨床干預報告（mesotherapy 途徑）。

| PMID | 年度 | 類型 | 主要発現 |
|------|-----|------|---------|
| [37036158](https://pubmed.ncbi.nlm.nih.gov/37036158/) | 2023 | 臨床干預 | 複方甘草酸 mesotherapy 注射治療中重度痤瘡（n=75，J Cosmetic Dermatology）|
| [40020947](https://pubmed.ncbi.nlm.nih.gov/40020947/) | 2025 | 製劑開發 | 甘草酸自組裝微胞增強 Cryptotanshinone 痤瘡治療穿透性與抗炎效果 |

---

## 台灣市販情報

台灣目前無 Glycyrrhizic acid（甘草酸）的核准藥品許可證，總許可証數 0 件。

> 補充：日本市場有 SNMC（Stronger Neo-Minophagen C，含 0.2% 甘草酸 ＋ 甘胺酸 ＋ 半胱胺酸）的靜注製劑，核准用於慢性活動性肝炎，可作為參考製劑規格。

---

## 安全性考量

安全性資訊請參閱許可事項。

> ⚠️ 重要安全訊號：文獻記載甘草酸透過抑制 11β-HSD2，大量或長期攝取可能引起**假性醛固酮增多症（Pseudoaldosteronism）**，症狀包括低血鉀、高血壓、水腫及血漿醛固酮偏低（PMID [39284704](https://pubmed.ncbi.nlm.nih.gov/39284704/)）。個體差異顯著，需監測電解質。

---

## 結論及下一步

**決定：Research Question（以類風濕性關節炎為優先研究目標）**

**理由：**
甘草酸對 RA 具有多重且互補的抗炎機轉（NF-κB 抑制、JAK-STAT 調節、HMGB1 拮抗、破骨細胞分化抑制），文獻量最大（20 篇），並有 1 項探索性臨床試驗，在所有 10 項預測適應症中根據最為完整。巨細胞病毒感染及肺動脈高壓亦各有機轉合理性與動物／臨床觀察資料，可作為平行研究問題。

**進行所需條件：**
- 補全 TFDA 安全性資料（DG001）及完整作用機轉資料（DG002）
- 純甘草酸（非複方）針對 RA 的系統性動物藥效研究（CIA 模型）
- 假性醛固酮增多症風險的安全劑量範圍確認，建立用藥監測計畫
- 設計 Phase 1 臨床試驗，確認人體安全劑量及 PK/PD 參數
- 對獸醫疾病（Rank 4、5）及負向效應適應症（Rank 2 Amenorrhea）正式排除，聚焦資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

