---
layout: default
title: Empagliflozin
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 3
---

# Empagliflozin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Empagliflozin：從2型糖尿病到典型僵人症候群

## 一句話摘要

Empagliflozin（恩格列淨）是一種 SGLT2 抑制劑，在全球多國已核准用於治療2型糖尿病及心臟衰竭，但目前在本地尚未取得上市許可。
TxGNN 模型以 **99.06% 的預測分數**，預測其對**典型僵人症候群（Classic Stiff Person Syndrome）**可能具有療效。
然而，此方向目前完全缺乏臨床試驗與文獻佐證，屬於純模型推測階段。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 既有適應症 | 2型糖尿病（全球核准；本地尚未上市） |
| 預測新適應症 | 典型僵人症候群（Classic Stiff Person Syndrome） |
| TxGNN 預測分數 | 99.06% |
| 根據等級 | L5 |
| 本地上市現況 | ✗ 尚未上市 |
| 許可證數量 | 0件 |
| 建議決策 | Hold |

---

## 此預測為何合理？

目前缺乏本地許可仿單中的詳細作用機轉資料。根據已知資訊，Empagliflozin 是一種鈉-葡萄糖協同轉運蛋白2（SGLT2）抑制劑，透過抑制腎臟近端小管對葡萄糖的再吸收，達到降血糖目的，並具有抗氧化壓力、抑制 NLRP3 炎性體及促進酮體生成（β-羥基丁酸鹽）等次要效應。

典型僵人症候群（Classic SPS）是一種自體免疫性神經系統疾病，病理核心為抗 GAD65 抗體介導的 GABA 抑制性神經元受損，造成進行性肌肉強直與痙攣。從機轉角度推測，Empagliflozin 透過降低全身性氧化壓力與抑制神經炎症，理論上可能緩解 SPS 的神經退行性進展；其促酮體生成效應亦對 GABAergic 傳遞具有潛在調節作用。

然而，上述機轉連結均為間接且高度推測性，目前缺乏 SPS 相關動物模型或體外研究的驗證資料。值得注意的是，本次預測的第2名（局灶性僵肢症候群, Focal Stiff Limb Syndrome）與第1名的 TxGNN 分數完全相同（99.06%），強烈提示這兩項預測為知識圖譜中節點共享評分，而非獨立預測訊號，需謹慎解讀。

---

## 臨床試驗根據

目前無相關臨床試驗登錄。

---

## 文獻根據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參閱許可仿單。

---

## 結論與後續步驟

**決策：Hold**

**理由：**
三項預測適應症（典型僵人症候群、局灶性僵肢症候群、Opsismodysplasia）均屬 L5 純模型預測，完全缺乏臨床試驗與文獻支持，機轉連結屬高度間接推測；且本藥在本地尚無上市許可，缺乏本地安全性及藥品資訊，不具備進入可行性評估的最低條件。

**如需推進，須具備：**
- Empagliflozin 對 GABAergic 系統或自體免疫性神經疾病影響的前臨床資料（動物模型或體外研究）
- 詳細的作用機轉資料（MOA）及本地藥品審查資料
- SGLT2 抑制劑用於神經炎症疾病的早期訊號文獻（即使非 SPS 特定）
- 評估血腦屏障穿透率是否足以在中樞神經系統達到有效藥物濃度
- 確認第1名與第2名預測是否確為知識圖譜節點共享評分，以排除偽訊號
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

