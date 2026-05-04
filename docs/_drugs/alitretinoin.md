---
layout: default
title: Alitretinoin
parent: 僅模型預測 (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
---

# Alitretinoin
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

# Alitretinoin: 慢性手部濕疹 → 閉經

## 一句話摘要

Alitretinoin（9-順式視網酸）是一種 retinoid 類藥物，在歐盟與加拿大以 Toctino® 獲批用於嚴重慢性手部濕疹的系統性治療，目前台灣尚未上市、無任何許可證記錄。TxGNN 模型預測其對**閉經（Amenorrhea）**具潛在療效，預測信心度達 **99.99%**。然而，目前**無任何臨床試驗或文獻支持**此一方向，整體根據水準為 **L5（僅模型預測）**，並存在機轉層面的根本性疑慮。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 既有適應症 | 嚴重慢性手部濕疹（國際許可；台灣無許可證） |
| 預測新適應症 | 閉經（Amenorrhea） |
| TxGNN 預測分數 | 99.99% |
| 根據水準 | L5 |
| 台灣上市狀況 | ✗ 未上市 |
| 許可證數 | 0 件 |
| 建議決策 | Hold |

---

## 為何此預測具合理性？

目前缺乏 Alitretinoin 的完整作用機轉資料（MOA 資料缺口）。就已知藥理而言，Alitretinoin 為天然配體 9-順式視網酸，是目前唯一能同時活化全部視黃酸受體（RAR α/β/γ）及視黃醇 X 受體（RXR α/β/γ）的化合物，主要透過調控細胞分化、免疫反應與表皮代謝發揮療效。

從間接機轉推論，維生素 A 缺乏確實可透過影響下視丘-腦垂體-性腺軸（HPG axis）干擾排卵功能，此一路徑可能是 TxGNN 知識圖譜中將 retinoid 代謝與閉經間接連結的來源。然而，此推論存在根本性矛盾：**高劑量 retinoids 本身已確認具致畸胎性（相當於妊娠 X 級），且有干擾生育功能的已知副作用**，在生物合理性上用於閉經治療恰好方向相悖，臨床轉譯潛力極低。

---

## 臨床試驗根據

目前無 Alitretinoin 用於閉經之相關臨床試驗登記。

---

## 文獻根據

目前無 Alitretinoin 用於閉經之相關文獻。

---

## 台灣上市資訊

Alitretinoin 目前在台灣**未上市**，無任何藥品許可證記錄。

> 國際參考：歐盟 / 加拿大以 Toctino®（口服膠囊）上市，適應症為嚴重慢性手部濕疹；美國以 Panretin®（外用凝膠）上市，適應症為 AIDS 相關卡波西氏肉瘤（Kaposi's sarcoma）局部病灶。兩者均尚未在台申請許可。

---

## 安全性考量

安全性資訊請參閱許可仿單。

> ⚠️ 注意：Alitretinoin 屬 retinoid 類藥物，具有明確且嚴重的致畸胎性，孕婦禁用。閉經患者族群多為育齡女性，若考慮推進此再利用方向，必須優先建立完善的妊娠預防計畫（Pregnancy Prevention Programme），並取得完整仿單安全性資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
本預測僅有 TxGNN 模型分數支持（L5），無臨床試驗或文獻根據；更關鍵的是，Alitretinoin 已知的致畸胎性與對 HPG 軸的潛在干擾，在生物合理性上與「治療閉經」的治療目標存在根本矛盾，繼續推進前需先解決此機轉衝突。

**若要繼續推進，需要：**
- 取得完整 MOA 資料，明確釐清 Alitretinoin 對 HPG 軸及排卵功能的實際影響方向
- 取得台灣仿單（如未來申請上市）或國際仿單之完整警語、禁忌與安全性資料
- 針對育齡女性族群制定妊娠預防計畫與風險管理框架
- 進行前臨床概念驗證研究（in vitro/in vivo），以建立機轉合理性的初步根據
- 重新評估 TxGNN 知識圖譜中閉經相關路徑的來源節點，確認預測是否源自有效的生物路徑連結
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

