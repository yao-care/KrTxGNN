---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin：從廣譜惡性腫瘤化療到 Ewing 肉瘤

---

## 한 문장 요약

Doxorubicin 為蒽環類（Anthracycline）廣譜細胞毒性抗腫瘤藥物，全球廣泛用於乳癌、淋巴瘤及軟組織肉瘤等多種惡性腫瘤的治療，然而目前在韓國尚未取得上市許可。TxGNN 模型預測其對 **Ewing 肉瘤（Ewing Sarcoma）** 具有顯著療效，預測點數達 **99.90%**。現有 **0 件 ClinicalTrials.gov 登錄臨床試驗**及 **20 篇文獻**（含 6 篇 Phase 3 RCT）支持此方向，整體證據等級達 **L1**。

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 廣譜惡性腫瘤化療藥物（韓國未許可上市） |
| 예측 신규 적응증 | Ewing 肉瘤（Ewing Sarcoma） |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 未上市 |
| 허가증 수 | 0 件 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는？

Doxorubicin 為 Topoisomerase II（DNA 拓撲異構酶 II）抑制劑，其作用機轉為嵌入 DNA 雙螺旋股間（Intercalation），阻斷 DNA 複製與轉錄，並誘導 DNA 雙股斷裂（Double-Strand Break, DSB），對快速增殖的腫瘤細胞產生高度細胞毒性。在蒽環類藥物中，Doxorubicin 因廣泛的腫瘤活性與成熟的臨床應用歷史，被列為多種惡性腫瘤一線化療的基礎藥物。

Ewing 肉瘤為兒童及青少年第二常見的原發性骨惡性腫瘤，由 EWSR1-FLI1（或其他 EWS/ETS 家族）融合基因驅動，腫瘤細胞增殖迅速，對 DNA 損傷型細胞毒性藥物高度敏感。Doxorubicin 作為 VIDE（vincristine、ifosfamide、doxorubicin、etoposide）及 VAC/VAI 標準方案的核心組成，已在歐美及日本的國際多中心試驗中確立其臨床地位，機轉與疾病生物學之連結清晰。

儘管韓國目前尚未許可 Doxorubicin，多項已完成的 Phase 3 國際 RCT（EE2012、EURO-EWING、AEWS0031、AEWS1221 等）均以含 Doxorubicin 的組合方案作為標準對照或實驗臂，證明其療效與安全性已達可用於臨床決策的最高證據等級（L1）。在謹慎評估心毒性累積風險後，此方向具備充分科學依據推進至實際應用評估。

---

## 임상시험 근거

現在 Doxorubicin + Ewing Sarcoma 之組合查詢（ClinicalTrials.gov）登錄結果為 **0 件**。

> **注意**：此結果可能反映查詢策略限制——Doxorubicin 於 Ewing 肉瘤試驗中多以方案名稱（如 VIDE、VAC/VAI）記錄，而非單獨作為主要介入藥物登錄。下方文獻中引用之多項 Phase 3 RCT 均直接評估含 Doxorubicin 之方案療效，實際臨床試驗數量充足。

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발현 |
|------|------|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT (Phase 3) | N Engl J Med | 新診斷 Ewing 肉瘤加入 ifosfamide + etoposide 至標準含 doxorubicin 方案，顯著改善無事件存活率 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012 試驗：比較歐洲（VIDE，含 doxorubicin）vs 美國（VDC/IE）標準方案，確立 VIDE 同等療效 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT (Phase 3) | Trials | EURO-EWING 2012 試驗設計：多國協作評估新型誘導 / 鞏固化療，以含 doxorubicin 方案為治療骨架 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | AEWS1221：IGF-1R 抗體 Ganitumab 加入 interval-compressed 含 doxorubicin 化療於轉移性 Ewing 肉瘤，n=170 |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | RCT (Phase 3) | J Clin Oncol | Ewing 2008R3（12 國）：高危 Ewing 肉瘤中 Treosulfan/Melphalan 高劑量化療 vs 含 doxorubicin 標準治療比較 |
| [31553693](https://pubmed.ncbi.nlm.nih.gov/31553693/) | 2019 | RCT (Phase 3) | J Clin Oncol | R2Pulm 試驗：肺轉移 Ewing 肉瘤中高劑量化療+自體幹細胞 vs 含 doxorubicin 標準化療+全肺放療 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | 臨床指引 / 共識 | Cancer | 美國 National Ewing Sarcoma Tumor Board 多機構共識：確立含 doxorubicin 的 VIDE/VAC 方案為 ES 標準治療 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Ewing 肉瘤全面回顧：化療引入後局部腫瘤存活率從 10% 提升至 75%，多藥化療不可或缺 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Ewing 肉瘤多學科治療現況與國際合作優化歷程，詳述含 doxorubicin 方案的演進 |
| [37093679](https://pubmed.ncbi.nlm.nih.gov/37093679/) | 2023 | 回顧性佇列 | Jpn J Clin Oncol | 原發性皮膚 / 皮下 Ewing 肉瘤臨床特徵分析，評估含 doxorubicin 多模式治療策略 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 細胞毒性藥物（蒽環類抗生素，Anthracycline Antibiotic）；屬 Topoisomerase II 抑制劑 |
| 골수억제 위험 | **高**（中性球減少症、血小板減少症為常見劑量限制性毒性，發生率高） |
| 구토 유발성 등급 | **中等至高度**（取決於給藥劑量與方案組合，建議預防性止吐） |
| 모니터링 항목 | CBC（含白血球分類計數）、心臟功能（LVEF，定期心臟超音波）、肝腎功能、累積劑量追蹤（建議最大累積劑量 ≤550 mg/m²，心臟病患者應更低） |
| 취급 방호 | 需嚴格依細胞毒性藥物操作規範（NIOSH / ISO 標準）處理；需配戴雙層手套、護目鏡及防護衣；溶液製備應於生物安全操作台內進行；避免藥液接觸皮膚及黏膜 |

> 警告：Doxorubicin 具累積性心毒性（心肌病變、充血性心衰竭），為臨床使用最重要的長期安全性考量。詳細警語及禁忌建議參閱原廠仿單（DG001，Blocking 等級資料缺口）。

---

## 안전성 고려사항

安全性資訊請參照許可事項。

> 目前韓國 MFDS 仿單警語及禁忌屬資料缺口（**DG001，Blocking 等級**），需下載原廠仿單 PDF 進行解析後方可完整評估。在補齊此資料前，無法完成 S1 安全性初評流程。藥物交互作用查詢結果亦為 not_found（0 筆），建議透過 DrugBank API 重新查詢。

---

## 결론 및 다음 단계

**결정：Proceed with Guardrails**

**사유：**
Doxorubicin 於 Ewing 肉瘤具備充分的 Phase 3 RCT 臨床證據（**L1 等級**），多項完成的國際大型試驗（EE2012、EURO-EWING、AEWS0031、AEWS1221 等）均以含 Doxorubicin 的 VIDE/VAC/VAI 方案作為治療基礎，作用機轉（Topoisomerase II 抑制 × EWSR1-FLI1 驅動之高增殖腫瘤）與疾病生物學高度吻合，臨床應用成熟。

**진행하려면 필요한 것：**
- **[優先]** 取得 MFDS 或原廠仿單（補充 DG001），完成 S1 安全性初評，確認心毒性相關禁忌與警語
- **[優先]** 透過 DrugBank API 補充完整 MOA 資料（DG002），強化機轉關聯性分析
- 確認韓國 Ewing 肉瘤的未滿足醫療需求（Unmet Medical Need）現況，評估特殊許可或同情性使用申請可行性
- 制定完整累積心毒性監測計畫（定期心臟超音波、最大累積劑量管理方案）
- 評估與現行韓國兒童腫瘤治療方案（如 VIDE、VAC）的整合可行性及給藥途徑相容性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

