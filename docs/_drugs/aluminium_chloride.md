---
layout: default
title: Aluminium Chloride
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 0
---

# Aluminium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Aluminium Chloride：資料不足，無法完成再創出評估

## 한 문장 요약

Aluminium Chloride 的基本藥物資訊（原始適應證、作用機轉）均缺失，目前在台灣尚未取得任何許可證。TxGNN 模型**未產生任何適應證預測**，亦無臨床試驗或文獻根據支持。本報告僅記錄現有資料缺口，並建議補齊後重新評估。

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 無許可資料 |
| 예측 신규 적응증 | 無（TxGNN 未產生預測） |
| TxGNN 예측 점수 | 無 |
| 근거 수준 | L5（僅模型查詢，無實際研究） |
| 한국 시판 현황 | 未上市 |
| 허가증 수 | 0 件 |
| 권장 결정 | Hold |

---

## 결론 및 다음 단계

**決定：Hold**

**原因：**
此 Evidence Pack 缺乏評估所需的核心資料——TxGNN 模型未輸出任何預測適應證，且藥物的作用機轉、原始適應證、台灣許可及安全性資訊均未取得，無法進行任何機轉關聯性或風險分析。

**進行評估所需補齊的資料：**

| 優先順序 | 缺口 ID | 項目 | 取得方式 |
|---------|--------|------|---------|
| 🔴 關鍵 | DG001 | TFDA 仿單（警語 / 禁忌） | 至 TFDA 官網下載 PDF 並解析 |
| 🟠 高 | DG002 | 作用機轉（MOA）及 DrugBank ID | 查詢 DrugBank API |
| — | — | TxGNN 預測結果 | 確認藥物名稱匹配後重跑預測管線 |
| — | — | 台灣許可証資料（若有） | 確認藥物是否以其他品名上市 |

> ⚠️ **注意**：Aluminium Chloride（氯化鋁）在部分劑型中以外用製劑（止汗、收斂）形式存在，DrugBank ID 需確認後方可正確對應知識圖譜節點，並重新觸發預測流程。

---

*本報告僅供研究參考，不構成醫療建議。所有再創出候選需經臨床驗證方可應用。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

