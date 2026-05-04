---
layout: default
title: Abatacept
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# Abatacept: 류마티스 관절염에서 류마티스 혈관염으로

## 한 문장 요약

Abatacept는 CTLA4-Ig 융합 단백질로, 전 세계적으로 류마티스 관절염(RA) 치료제로 사용되고 있으나 대만에서는 현재 허가·시판되지 않고 있습니다. TxGNN 모델은 **류마티스 혈관염(Rheumatoid Vasculitis)**에 효과가 있을 수 있다고 예측 점수 **99.91%**로 제시하며, 현재 **1건의 임상시험**과 **20편의 문헌**이 이 방향을 검토하고 있으나 직접적인 임상 근거는 증례 보고 수준에 머물러 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 대만 미허가 (글로벌 허가 적응증: 류마티스 관절염) |
| 예측 신규 적응증 | 류마티스 혈관염 (Rheumatoid Vasculitis) |
| TxGNN 예측 점수 | 99.91% |
| 근거 수준 | L4 |
| 대만 시판 현황 | ✗ 未上市 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Abatacept는 CTLA4-Ig 융합 단백질로서 T 세포 공자극(co-stimulation)의 핵심 경로인 CD80/CD86–CD28 상호작용을 경쟁적으로 차단합니다. 이를 통해 항원 제시 세포(APC)에 의해 유발되는 병원성 CD4+ T 세포의 활성화를 억제하고, 하위 염증성 사이토카인(TNF-α, IL-6, IL-17) 분비 및 면역 복합체 형성을 감소시킵니다. 현재 상세한 작용 기전(MOA) 데이터가 확보되지 않았으나, 류마티스 관절염·다관절형 소아 특발성 관절염·건선성 관절염에서의 글로벌 임상 허가 이력을 통해 T 세포 매개 자가면역 질환에서의 효능이 검증되어 있습니다.

류마티스 혈관염(Rheumatoid Vasculitis, RV)은 중증 RA의 드문 전신 합병증으로, 혈관벽에 CD4+ T 세포 침윤 및 면역 복합체 침착이 핵심 병리 기전입니다. RA에서 확립된 T 세포 공자극 경로의 병리적 역할이 RV에서도 동일하게 작동하므로, Abatacept의 CD28 차단 기전이 RV의 혈관 염증 억제에 적용될 수 있다는 합리적인 생물학적 근거가 존재합니다.

실제 임상에서도 긍정적 증례가 보고되었습니다. Al Attar & Shaver (2018, PMID 29930884)는 rituximab 사용이 금기인 공통 변이형 면역결핍(CVID) 동반 RA 환자에서 Abatacept로 RV를 성공적으로 치료한 사례를 보고하였으며, Fujii et al. (2012, PMID 22124545) 역시 MTX·TNF 억제제·IL-6 억제제 모두 실패한 RV 환자에서 Abatacept 투여 후 신속한 임상 호전을 보고하였습니다. 그러나 Carvajal Alegria et al. (2016, PMID 27052429)는 Abatacept 치료 도중 RV가 오히려 새롭게 발생한 역설적 사례를 보고하여, 치료 효과와 RV 유발 가능성 사이의 관계에 대한 추가 탐색이 필요함을 시사합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 미개시 | 80 | 선택적 어깨 관절 치환술 시행 류마티스 환자에서 면역억제제(Abatacept 포함) 수술 전 중단 시점 비교 연구. 류마티스 혈관염 직접 치료와 무관하며, RV 유효성 근거를 제공하지 않음 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29930884](https://pubmed.ncbi.nlm.nih.gov/29930884/) | 2018 | 증례 시리즈/서술 리뷰 | Cureus | CVID 동반 RA 환자에서 rituximab 대체 요법으로 Abatacept 투여 후 류마티스 혈관염 임상적 호전 보고 |
| [22124545](https://pubmed.ncbi.nlm.nih.gov/22124545/) | 2012 | 증례 보고 | Modern Rheumatology | MTX·TNF 억제제·IL-6 억제제 모두 실패한 RV 환자에서 Abatacept 투여 후 신속한 임상 증상 호전 (38세 여성 증례) |
| [30119075](https://pubmed.ncbi.nlm.nih.gov/30119075/) | 2018 | 증례 시리즈 | Ophthalmic Plastic & Reconstructive Surgery | Abatacept 치료 중 RA 관련 양측 안와 혈관염 발생 (호산구 침윤); cyclophosphamide 초기 반응 후 진행 |
| [27052429](https://pubmed.ncbi.nlm.nih.gov/27052429/) | 2016 | 증례 보고 | Joint Bone Spine | Abatacept 치료 중 류마티스 혈관염 신규 발생; rituximab 전환 후 호전 — 역설적 반응 주의 |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | 증례 보고 | Internal Medicine (Tokyo) | Abatacept·adalimumab 병용 중 MPO-ANCA 관련 신염 발생; tocilizumab 추가 후 완화 |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | 서술 리뷰 | J Clinical Medicine | RA 관련 공막염·상공막염 치료 현황 검토; Abatacept 포함 생물학적 제제 치료 전략 논의 |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | 후향적 코호트 | Ann Rheumatic Diseases | bDMARD 유발 루푸스·혈관염 발생 예측에서 ANA 정기 검사의 임상적 유용성 평가 |
| [31174819](https://pubmed.ncbi.nlm.nih.gov/31174819/) | 2018 | 서술 리뷰 | Best Pract Res Clin Rheumatol | RA 환자의 뇌혈관염 포함 CNS 침범 및 Abatacept 등 생물학적 제제 사용 시 신경학적 위험 검토 |
| [24493331](https://pubmed.ncbi.nlm.nih.gov/24493331/) | 2015 | 증례 시리즈 | Clinical Rheumatology | 근염(Myositis) 환자에서 Abatacept의 off-label 치료 가능성 증례 기반 기전 검토 |
| [41117362](https://pubmed.ncbi.nlm.nih.gov/41117362/) | 2026 | 논평 | Eur J Clinical Investigation | RA·전신 경화증·대혈관 혈관염 등 염증성 자가면역 류마티스 질환의 조기 진단·치료 전략 최신 고찰 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
류마티스 혈관염에 대한 Abatacept의 직접 임상 근거가 소수 증례 보고(L4) 수준에 국한되며, Abatacept 치료 중 RV가 오히려 새롭게 발생한 역설적 사례가 존재해 인과관계 방향성에 불확실성이 있습니다. 대만 내 허가도 없어 규제적 접근이 선행되어야 합니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 대만 TFDA 허가 경고 및 금기 정보 취득 (仿單 PDF 분석)
- 류마티스 혈관염 환자 대상 파일럿 전향적 연구 설계 (proof-of-concept 임상시험)
- Abatacept 치료 중 RV 신규 발생 역설적 반응 기전 규명 연구
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

