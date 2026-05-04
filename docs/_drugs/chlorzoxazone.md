---
layout: default
title: Chlorzoxazone
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Chlorzoxazone
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

# Chlorzoxazone：從肌肉鬆弛到偏頭痛（Migraine Disorder）

---

## 一句話摘要

Chlorzoxazone 是一種中樞性骨骼肌鬆弛劑，傳統用於緩解肌肉骨骼疼痛與痙攣。TxGNN 模型預測其對**偏頭痛（Migraine Disorder）**可能具有療效，核心假說機轉涉及 BK channel 活化對 CaV2.1 離子通道過度活化的補償效應。目前有 **0 件臨床試驗**及 **3 篇相關文獻**，所有根據均屬前臨床機轉研究層級（L4）。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 基存適應症 | 肌肉骨骼疼痛與痙攣（中樞性骨骼肌鬆弛劑） |
| 預測新適應症 | 偏頭痛（Migraine Disorder） |
| TxGNN 預測分數 | 99.73% |
| 根據水平 | L4（動物實驗 / 機轉研究） |
| 韓國市售現況 | ✗ 未上市 |
| 許可證數 | 0 件 |
| 建議決定 | Hold |

---

## 這項預測為何合理？

Chlorzoxazone 已知為 **BK channel（大電導鈣依賴性鉀通道）促進劑**，同時是 CYP2E1 酵素的探針底物，其主要藥理效果為中樞性骨骼肌鬆弛。現有正式作用機轉（MOA）資料尚待補全，以下分析基於現有文獻推導。

機轉假說的核心根據來自 PMID 23115190：在帶有 **CACNA1A S218L 功能增益突變**的小鼠模型中，BK channel 活化劑可有效緩解因 CaV2.1（P/Q 型鈣離子通道）過度活化所引起的小腦共濟失調症狀。此發現對偏頭痛具有直接意義，原因是 **CaV2.1 功能增益突變同時是家族性偏癱偏頭痛第一型（FHM1）的核心致病機轉**——兩種疾病共享相同的離子通道異常基礎。

由此建構的機轉假說鏈如下：

> **Chlorzoxazone → BK channel 活化 → 補償 CaV2.1 過度活化 → 可能緩解 FHM1 相關偏頭痛**

**重要限制**：此為多步驟間接推論，目前無直接以 Chlorzoxazone 治療偏頭痛的臨床或動物實驗資料。機轉假說僅適用於 FHM1 單基因特定亞型，對一般多因性常見偏頭痛（涉及 TRPM8、LRP1、PRDM16 等多基因背景）的適用性缺乏生物學合理性，需先以 FHM1 動物模型進行直接驗證。

---

## 臨床試驗根據

目前無 Chlorzoxazone 用於偏頭痛的相關臨床試驗登錄。

---

## 文獻根據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | 敘事性綜述 | Journal of Neurology | 小腦及中樞前庭疾患的藥物治療總覽，涵蓋 4-aminopyridine 等鉀通道調節劑的臨床應用，背景脈絡與 BK channel 假說相關 |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | 敘事性綜述 | Deutsches Arzteblatt International | 周邊與中樞性眩暈的病理與治療全面回顧，前庭性偏頭痛占所有眩暈案例 11.4%，提供疾病分類背景 |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | 基礎科學（活體動物模型） | The Journal of Neuroscience | **核心根據**：BK channel 活化劑可緩解 CACNA1A S218L 突變小鼠的小腦共濟失調，為 Chlorzoxazone → BK channel → CaV2.1 補償 → FHM1 偏頭痛機轉假說提供直接前臨床支持 |

> ⚠️ 上述文獻均非直接研究 Chlorzoxazone 對偏頭痛的療效，屬機轉推論性間接根據。

---

## 韓國市售資訊

Chlorzoxazone 在韓國目前**無任何藥品許可證**，市售狀態為未上市。

---

## 安全性考量

安全性資訊請參閱各國藥品許可事項。

> ⚠️ **已知安全信號（肝毒性）**：Chlorzoxazone 在醫學文獻中有嚴重特異性肝損傷（idiosyncratic hepatotoxicity）的案例報告，於任何慢性適應症的臨床轉化規劃中，此為**優先評估的安全顧慮**，治療窗口需於推進前明確建立。此外 PMID 19606800 記錄了多藥合用情境下的高鐵血紅素症毒性事件，提示過量風險。

---

## 結論及後續步驟

**決定：Hold**

**理由：**
目前所有根據均屬前臨床 / 機轉研究層級（L4），機轉假說為多步驟間接推論，且僅適用於 FHM1 特定遺傳亞型，無任何人體直接應用根據。藥品在韓國未上市、作用機轉資料缺失、安全性資料（警語與禁忌）尚未完整取得，整體條件尚不足以進入臨床評估。

**若要推進，需要：**
- 以 FHM1 動物模型（CACNA1A 功能增益突變鼠）**直接驗證** Chlorzoxazone 對偏頭痛相關症狀的抑制效果
- 補全作用機轉（MOA）資料，確認 BK channel 促進的劑量-反應特性與腦部暴露量
- 系統性肝毒性安全評估，明確建立安全治療窗口
- 取得完整藥品仿單安全資訊（警語、禁忌，目前為資料缺口）
- **附加評估建議**：類風濕性關節炎（RA，Rank 9）方向有 L3 根據（7 篇文獻），含 1960-70 年代 Predniflex 複方直接臨床使用紀錄及 Cochrane 系統綜述，機轉上屬症狀緩解輔助止痛，可作為次要候選方向另行評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

