---
layout: default
title: Etizolam
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 1
---

# Etizolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Etizolam：焦慮症到失眠症

## 一句話摘要

Etizolam 是一種 Thienodiazepine 類藥物，在日本、印度已核准用於焦慮症與失眠治療，但在台灣目前尚無任何上市登錄。TxGNN 模型以 **99.94%** 的極高分預測其對**失眠症（Insomnia）**具有療效潛力，然而目前僅有 **4 篇文獻**提供間接支持，且無任何直接臨床試驗根據，整體根據強度有限。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 既有適應症 | 無台灣登錄（日本、印度核准用於焦慮症／失眠） |
| 預測新適應症 | 失眠症（Insomnia） |
| TxGNN 預測分數 | 99.94% |
| 根據等級 | L4 |
| 台灣上市狀況 | ✗ 未上市 |
| 許可證數量 | 0 件 |
| 建議決策 | Hold |

---

## 此預測為何合理？

Etizolam 屬於 Thienodiazepine 類藥物（苯二氮平衍生物），其作用機轉為 **GABA-A 受體正向異位調節劑（positive allosteric modulator）**，透過增強 GABAergic 抑制性神經傳導，產生鎮靜、催眠及抗焦慮效果。由於 GABAergic 機轉與失眠病理生理直接相關，同類傳統苯二氮平藥物（如 triazolam、nitrazepam、temazepam）已廣泛用於失眠臨床治療，從藥理類比角度支持 TxGNN 此項預測。

就直接藥效學證據而言，動物實驗（PMID: 18789918）已明確證實 Etizolam 可顯著縮短入睡潛伏期、增加非快速眼動（non-REM）睡眠時間，並在連續給藥 7 天後停藥時觀察到反彈性失眠現象，顯示其 GABAergic 催眠機轉確實存在且具生理意義。

值得特別注意的是，Etizolam 在日本及印度早已獲得核准，適應症即涵蓋焦慮症與失眠症，TxGNN 的預測與其既有藥理應用高度一致。台灣資料庫中顯示為「未上市」且無正式適應症記錄，係資料庫收錄範圍所致，而非藥物本身缺乏此方向的藥理基礎。

---

## 臨床試驗根據

目前無針對 Etizolam 用於失眠症已登錄的臨床試驗。

---

## 文獻根據

| PMID | 年度 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [18789918](https://pubmed.ncbi.nlm.nih.gov/18789918/) | 2008 | 動物研究 | Eur J Pharmacol | Etizolam 可縮短大鼠入睡潛伏期、增加非快速眼動睡眠時間，停藥後出現反彈性失眠，與 triazolam 效果相當 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | 焦慮藥藥動學綜覽，Etizolam 等 thienodiazepine 類藥物的 ADME 特性分析 |
| [23553148](https://pubmed.ncbi.nlm.nih.gov/23553148/) | 2013 | Case Report | J Anesthesia | 75 歲患者術後停用 Etizolam 後出現惡性症候群相似症狀（含失眠），靜注 diazepam 後改善，顯示 GABA 受體依賴性 |
| [29105206](https://pubmed.ncbi.nlm.nih.gov/29105206/) | 2018 | 觀察研究 | J Paediatr Child Health | 住院惡性腫瘤兒童心理及心身症狀研究，Etizolam 作為症狀處置藥物之一出現於臨床情境 |

---

## 台灣上市資訊

Etizolam 目前在台灣**無任何藥品許可證**，屬完全未上市藥物，無可供參考的本地核准適應症。

---

## 安全性考量

安全性資訊請參閱日本（PMDA）或印度核准仿單，並評估苯二氮平類管制藥品相關規範。

---

## 結論與下一步

**決策：Hold**

**理由：**
儘管 TxGNN 預測分數極高（99.94%），且 GABAergic 藥理機轉與失眠治療直接相關，目前卻完全缺乏人體臨床試驗支持，根據等級僅達 L4（動物研究），加上台灣無任何上市登錄，整體準備度不足以進入再創用評估下一階段。

**若要推進，需補充：**
- 蒐集 Etizolam 用於失眠症的人體臨床試驗資料（優先尋找日本、印度已有的 RCT）
- 確認台灣法規路徑：Etizolam 是否涉及管制藥品分級（苯二氮平類），以及從未上市到申請許可的完整程序
- 取得日本 PMDA 或印度藥監局正式仿單，解析警語、禁忌及藥物交互作用資訊（對應 DG001）
- 補充完整 MOA 資料，查詢 DrugBank API 以確認受體結合特異性與選擇性（對應 DG002）
- 評估 Etizolam 相較於已在台上市的 Z-drug（zolpidem）或苯二氮平藥物的差異化價值
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

