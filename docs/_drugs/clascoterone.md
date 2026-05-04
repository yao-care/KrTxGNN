---
layout: default
title: Clascoterone
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Clascoterone
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

# Clascoterone: 痤瘡至念珠菌病

---

## 一句話摘要

Clascoterone（DB12499）是一種外用雄激素受體（AR）拮抗劑，於美國以「Winlevi」為品牌名稱核准用於 12 歲以上患者的面部痤瘡（青春痘）治療，目前在韓國尚未取得任何上市許可。TxGNN 模型預測其對**念珠菌病（Candidiasis）**可能有效，預測分數達 94.82%；然而，目前**無任何臨床試驗或相關文獻**支持此方向，機轉連結高度間接，屬模型拓撲假陽性的高風險預測。

---

## 快速概覽

| 項目 | 內容 |
|------|------|
| 既有適應症 | 痤瘡（青春痘）— 韓國無許可記錄；參考美國 FDA 核准適應症 |
| 預測新適應症 | 念珠菌病（Candidiasis） |
| TxGNN 預測分數 | 94.82% |
| 根據水準 | L5 |
| 韓國上市現況 | ✗ 未上市 |
| 許可證數 | 0 件 |
| 建議決策 | Hold |

---

## 此預測合理嗎？

目前詳細作用機轉資料尚未完整收錄（MOA Data Gap）。根據現有藥理學背景，Clascoterone 的化學結構源自 cortexolone（11-去氧皮質醇），是一種外用類固醇衍生物，主要作用為競爭性拮抗毛囊皮脂腺單位（pilosebaceous unit）中的雄激素受體，抑制皮脂過量分泌，進而改善痤瘡症狀。其作用部位侷限於局部皮膚，全身性藥物暴露極低。

知識圖譜推測 AR 拮抗可能透過調節宿主抗真菌免疫（Th17 軸）間接影響念珠菌感染易感性。雄激素對先天免疫確有一定調節作用，但此機轉連結極為間接。更根本的問題在於：Clascoterone 為**局部外用製劑**，念珠菌病的治療需求（全身性或黏膜抗真菌）與此製劑的藥動學特性存在根本性不相容。

綜合評估，此預測最可能為圖譜拓撲假陽性（graph topology artifact）所致，即模型透過共享的免疫調節節點產生高分，並非真實的治療連結。在本次 10 項預測中，機轉合理性最高的適應症為**腎上腺功能亢進（Rank 9）**，因 Clascoterone 本身具有 cortexolone 類固醇骨架，與腎上腺雄激素過量相關疾病（如先天性腎上腺增生症）存在直接結構-機轉連結，但同樣缺乏臨床與文獻支持。

---

## 臨床試驗根據

目前無任何與 Clascoterone 及念珠菌病相關的臨床試驗登錄記錄。

---

## 文獻根據

目前無任何與 Clascoterone 及念珠菌病直接相關的文獻。

> **備註（Rank 4 說明）**：查詢「偏頭痛易感性（migraine with or without aura, susceptibility to）」時擷取到 20 篇文獻，但經逐篇評估，內容均為癲癇遺傳學（SCN1A 多態性、神經炎症等），係透過癲癇-偏頭痛共病橋接而被納入，與 Clascoterone 無直接關聯，相關性評估為低度（Tier 3），不列入正式文獻根據。

---

## 韓國上市資訊

Clascoterone 目前在韓國未取得任何藥品上市許可，無許可證記錄可供列示。

---

## 安全性考量

安全性資訊請參考許可說明書。

---

## 結論及後續步驟

**決策：Hold**

**理由：**
念珠菌病預測屬 L5 最低根據水準，無任何臨床試驗或直接文獻支持；Clascoterone 的局部 AR 拮抗機轉與念珠菌感染的機轉連結高度間接，且外用製劑的藥動學特性與全身性或黏膜真菌感染的治療需求根本不相容，不建議在缺乏更多根據的情況下推進此方向。

**若要繼續評估，需要：**
- 補充完整作用機轉（MOA）資料（建議透過 DrugBank API 查詢 DB12499）
- 補充韓國/TFDA 許可說明書安全性警語及禁忌事項（目前為 Blocking 資料缺口）
- 重新評估機轉合理性最高的替代適應症，優先考慮 **Rank 9 腎上腺功能亢進（Adrenal Gland Hyperfunction）**（cortexolone 結構-機轉直接連結），並針對該適應症補充文獻與臨床試驗查詢
- 若考慮皮膚科延伸適應症，**Rank 6 萎縮性蟲蝕性皮膚病（Atrophoderma Vermiculata）**為毛囊角化症變體，具相對較高的局部皮膚科機轉合理性，可列為次優先評估項目
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

