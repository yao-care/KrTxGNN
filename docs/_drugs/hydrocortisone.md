---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: 코르티코스테로이드 제제에서 원형탈모증(Alopecia Areata)으로

## 한 문장 요약

Hydrocortisone(DrugBank ID: DB00741)은 부신피질호르몬(코르티코스테로이드) 계열 약물로, 대만에서는 현재 시판되지 않아 허가 적응증 정보가 확인되지 않습니다.
TxGNN 모델은 **원형탈모증(Alopecia Areata)**에 효과가 있을 것으로 예측(예측 점수 **99.97%**)하며, 소아 원형탈모증을 대상으로 한 완료된 Phase 3 무작위 대조시험을 포함해 현재 **4건의 임상시험**과 **20편의 문헌**이 이 방향을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (허가 정보 미확인, 대만 미상영) |
| 예측 신규 적응증 | 원형탈모증 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L1 |
| 대만 시판 현황 | 미상영 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 상의 상세한 작용 기전(MOA) 데이터는 확인되지 않습니다(Data Gap). 다만 임상 근거 자료에 따르면, Hydrocortisone을 포함한 국소·병변내 코르티코스테로이드는 원형탈모증 치료에서 이미 확립된 1차 또는 보조 치료법입니다.

작용 기전은 모낭 주변의 T세포 매개 자가면역성 염증 반응을 억제하여 모낭의 면역 특권(immune privilege) 상태를 회복시키는 것으로 알려져 있습니다. 이는 단순한 예측적 연관성이 아니라, 다수의 문헌과 무작위 대조시험(RCT)을 통해 이미 검증된 기전-적응증 관계입니다.

실제로 소아 원형탈모증 환자를 대상으로 Hydrocortisone 1% 크림과 Clobetasol propionate 0.05% 크림을 비교한 완료된 Phase 3 RCT(NCT01453686, PMID 24226568)가 존재하여 TxGNN 예측의 타당성을 뒷받침하며, 1950~60년대의 병변내 hydrocortisone 주사 관련 고전적 임상보고들도 같은 방향을 지지합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | 완료 | 41 | 소아 원형탈모증 대상, Hydrocortisone 1% 크림 vs Clobetasol propionate 0.05% 크림 무작위 대조시험 (약물·적응증 완전 일치, 근거 등급 A) |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | 모집 예정 | 72 | 경증~중등도 안드로겐성 탈모 환자 대상 4개 군 용량-반응 비교 시험, 국소 스테로이드 제형 관련 가능성 있으나 아직 데이터 없음 |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | 완료 | 18 | 병변내 Triamcinolone acetonide(동일 계열 코르티코스테로이드) 주사가 원형탈모증 환자의 부신 기능에 미치는 영향 평가 |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | 완료 | 380 | 부신선종 환자에서 스테로이드 대사 이상이 골강도·골밀도·골재형성에 미치는 영향 (코르티코스테로이드 전신 노출의 안전성 참고자료) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | 소아 원형탈모증 대상 Clobetasol propionate 0.05% vs Hydrocortisone 1% 무작위 임상시험 |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | 코호트/임상연구 | Clinical and Experimental Dermatology | 소아 중증 원형탈모증(전두·전신탈모 포함)에서 밀폐요법 병용 국소 코르티코스테로이드의 효능·안전성 후향적 분석 |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | 체계적 문헌고찰/메타분석 | Journal of Cosmetic Dermatology | 분획 레이저 단독/병용요법의 원형탈모증 치료 효과에 대한 체계적 문헌고찰 |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | 미분류 | Der Hautarzt | 병변내 hydrocortisone 주사 후 원형탈모증·악성탈모에서의 발모 효과 관찰 |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | 미분류 | Vestnik Dermatologii i Venerologii | Hydrocortisone 피내주사를 이용한 원형탈모증 및 전신탈모 치료 |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | 미분류 | Actas Dermo-Sifiliograficas | Hydrocortisone 피내주사를 이용한 원형탈모증 치료 |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | 사례군(역사적) | Medical Times | Cortisone, hydrocortisone 및 유사체(prednisone, prednisolone)를 이용한 부분·전신 원형탈모증 치료 사례 |
| [5696522](https://pubmed.ncbi.nlm.nih.gov/5696522/) | 1968 | 미분류 | British Journal of Dermatology | 코르티코스테로이드 치료 전후 원형탈모증 환자의 두피 혈관 변화 관찰 |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | 리뷰 | JEADV | 원형탈모증 환자에서 시상하부-뇌하수체-부신(HPA) 축 과활성 여부에 대한 고찰 |
| [22381765](https://pubmed.ncbi.nlm.nih.gov/22381765/) | 2012 | 미분류 | Journal of Southern Medical University | 간신허증형 중증 원형탈모증 환자의 혈청 코르티솔 및 말초혈액단핵구 당질코르티코이드 수용체 mRNA 발현 조사 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
원형탈모증에 대해서는 소아 대상 완료된 Phase 3 RCT(NCT01453686, PMID 24226568)와 다수의 관찰연구·역사적 임상보고가 기전과 효능을 뒷받침하여 근거 수준 L1으로 평가됩니다. 다만 안전성 정보(주요 경고, 금기, 약물상호작용)가 전부 확인되지 않고(Data Gap, **Blocking**) 대만 내 시판·허가 정보도 없어, 효능 근거는 강하지만 안전성 초기 평가(S1) 단계조차 진행할 수 없는 상태이므로 조건부 진행(Guardrails)으로 권고합니다.

**진행하려면 필요한 것:**
- TFDA(대만 식품藥物관리서) 공식 첨부문서(仿單)에서 경고·금기 정보 확보 (Blocking, DG001)
- DrugBank 등에서 상세 작용기전(MOA) 데이터 보완 (High, DG002)
- 약물상호작용(DDI) 데이터베이스 재조회 (현재 not_found, 0건)
- 대만 내 시판·허가 현황 확인 (현재 미상영, 허가증 0건)
- 순위 2~10위 예측 적응증(alopecia mucinosa, telogen effluvium 등)은 대부분 근거 수준 L5로 현재 Hold 권고 상태이며 추가 임상·문헌 근거 확보 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

