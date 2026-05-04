---
layout: default
title: Cilastatin
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Cilastatin
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

# Cilastatin: 이미페넴 복합 투여 보조약에서 세균성 관절염으로

---

## 한 문장 요약

Cilastatin은 카바페넴계 항생제 이미페넴(Imipenem)과 함께 복합 투여되는 신장 탈수펩티다제-I(DHP-I) 억제제로, 이미페넴이 신세뇨관에서 분해되는 것을 차단하여 항균 효능을 유지시키는 보조 성분입니다.
TxGNN 모델은 Cilastatin이 **세균성 관절염(Bacterial Arthritis)** 치료에 효과가 있을 수 있다고 예측하며,
현재 **임상시험 0건, 17편의 문헌**이 이 방향을 지지하고 있습니다. 단, 현재 근거의 대부분은 Cilastatin 단독이 아닌 Imipenem/Cilastatin 복합제에 관한 것임에 유의해야 합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | Imipenem/Cilastatin 복합제 성분 (한국 미허가) |
| 예측 신규 적응증 | 세균성 관절염 (Bacterial Arthritis) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Cilastatin은 독립적인 항균 활성이 없는 보조 성분입니다. 신장의 탈수펩티다제-I(DHP-I) 효소를 경쟁적·가역적으로 억제하여, 이미페넴이 신세뇨관에서 불활성화되는 것을 방지합니다. 이미페넴/실라스타틴 복합제(1:1 비율)로 투여될 때, 실라스타틴은 이미페넴의 혈중 농도 유지와 신독성 예방이라는 두 가지 역할을 담당합니다. 이미페넴 자체는 세포벽 합성을 억제하는 β-락탐계 카바페넴으로, 그람 양성균·그람 음성균·혐기성균을 포함한 광범위한 항균 스펙트럼을 가집니다.

현재 상세한 작용 기전 데이터(MOA)가 없습니다. 알려진 정보에 따르면, Cilastatin은 Imipenem/Cilastatin 복합제(제품명 Tienam 등)의 필수 구성 성분이며, TxGNN이 세균성 관절염을 예측한 것은 이미페넴/실라스타틴 복합제가 세균성 관절염의 주요 원인균—*Staphylococcus aureus*, *Streptococcus* spp., 장내 그람 음성균, 혐기성 세균—에 대해 포괄적인 항균력을 보유하고 있기 때문으로 해석됩니다.

실제로 세균성 관절염은 단일균 감염부터 다균성 감염까지 다양한 원인균을 가지며, 특히 면역저하자·다제내성균 감염 환자에서는 광범위 항생제가 필요합니다. PMID 3544811 및 PMID 3464787은 이미페넴/실라스타틴이 소아 화농성 관절염 및 골관절 감염에서 치료율 87–96%를 달성했음을 보고하며, 이는 복합제로서의 임상 타당성을 지지합니다. 그러나 재창출 후보로서 Cilastatin 단독 기여도를 분리하는 추가 연구가 필요합니다.

---

## 임상시험 근거

현재 Cilastatin을 세균성 관절염 적응증에 대해 평가한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 저널 | 주요 발견 |
|------|------|------|---------|
| [3544811](https://pubmed.ncbi.nlm.nih.gov/3544811/) | 1987 | Am J Dis Child | 소아 급성 골수염(7예) 및 화농성 관절염(11예) 환자에서 이미페넴/실라스타틴 100 mg/kg/일 투여: 전반적 치료 성공 |
| [3464787](https://pubmed.ncbi.nlm.nih.gov/3464787/) | 1986 | Jpn J Antibiotics | 골관절 감염 30예에서 이미페넴/실라스타틴 치료: 전체 치료율 87%, 급성기 96% |
| [7843815](https://pubmed.ncbi.nlm.nih.gov/7843815/) | 1994 | Infection | *Bacteroides fragilis*에 의한 고관절 패혈성 관절염 1예: 이미페넴/실라스타틴 + 메트로니다졸 4개월 치료 및 수술적 변연절제로 회복 |
| [40177421](https://pubmed.ncbi.nlm.nih.gov/40177421/) | 2025 | Open Life Sci | 급성 림프모구 백혈병 소아에서 *Aeromonas veronii*에 의한 고관절 패혈성 관절염: 이미페넴 포함 복합 항생제 치료 보고 |
| [38815931](https://pubmed.ncbi.nlm.nih.gov/38815931/) | 2024 | Indian J Med Microbiol | *Rhodococcus hoagii*에 의한 패혈성 관절염 및 균혈증 고령 환자: 반코마이신 + 이미페넴 복합 치료로 호전 |
| [36550469](https://pubmed.ncbi.nlm.nih.gov/36550469/) | 2022 | BMC Infect Dis | *Ureaplasma parvum* 패혈성 관절염 동반 고암모니아혈증 증례: 희귀 병원균에 의한 패혈성 관절염 조기 진단 및 항생제 전환의 중요성 |
| [37718611](https://pubmed.ncbi.nlm.nih.gov/37718611/) | 2023 | Mod Rheumatol Case Rep | 파종성 *M. abscessus* 감염 및 다관절 골관절 침범 면역저하 환자: 염증성 관절염과의 감별 필요성 기술 |
| [27826114](https://pubmed.ncbi.nlm.nih.gov/27826114/) | 2017 | Int J Infect Dis | *Nocardia elegans* 파종성 감염 증례: 이미페넴-실라스타틴 + 미노사이클린 병합 치료 후 생존 |
| [3904406](https://pubmed.ncbi.nlm.nih.gov/3904406/) | 1985 | Am J Dis Child | 세균 감염 소아 40명(화농성 관절염 포함)에서 이미페넴/실라스타틴 전향적 임상 효능 및 독성 평가 |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Int J Antimicrob Agents | MRSA, 카바페넴 내성 그람 음성균 감염에서 항생제 오프라벨 사용 및 공식 권장사항 비교 검토 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Cilastatin은 독립적인 항균 활성이 없으며, 세균성 관절염에 대한 모든 문헌 근거는 Imipenem/Cilastatin 복합제에 관한 것입니다. Cilastatin 단독 재창출 후보로서의 임상적 의의가 현재 근거만으로는 불분명하며, 한국 내 미허가 성분이므로 규제 검토 없이 임상 적용이 불가합니다.

**진행하려면 필요한 것:**
- Cilastatin의 독립적 효과와 Imipenem 복합 효과를 구분하는 기전 연구
- 상세한 작용 기전 데이터(MOA) 확보 (DrugBank API 조회 권장, DG002 해소)
- 한국 식품의약품안전처(MFDS)에서 이미페넴/실라스타틴 복합제 허가 현황 확인
- 허가사항 경고 및 금기사항 확보 (DG001 해소: 한국 의약품 허가정보 PDF 검토)
- 세균성 관절염 특이적 임상시험 계획 수립 (복합제 기준, Phase 2 이상)
- 재창출 대상을 Cilastatin 단독보다 Imipenem/Cilastatin 복합제로 재정의하는 방향 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

