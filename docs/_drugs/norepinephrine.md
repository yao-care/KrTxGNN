---
layout: default
title: Norepinephrine
parent: 모델 예측만 (L5)
nav_order: 553
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Norepinephrine: 예측 신규 적응증 폐쇄성 폐질환 (Obstructive Lung Disease) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 링크로만 제공되어 확인 불가 (허가사항 참조)"
monitor_inn: "norepinephrine"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome"]
---

# Norepinephrine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

# Norepinephrine: 승압 치료제에서 폐쇄성 폐질환으로

## 한 문장 요약

Norepinephrine(노르에피네프린)은 한국에서 주사제로 허가·시판 중인 혈관수축 승압제입니다.
TxGNN 모델은 **폐쇄성 폐질환(Obstructive Lung Disease)**에 효과가 있을 수 있다고 예측하지만, 이는 네트워크 기반 예측일 뿐입니다. 이 방향을 직접 지지하는 임상시험은 없고(등록된 1건은 관련성이 낮음), 문헌 18편도 대부분 기전·생리 관련 리뷰입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크로만 제공되어 확인 불가 (허가사항 참조) |
| 예측 신규 적응증 | 폐쇄성 폐질환 (Obstructive Lung Disease) |
| TxGNN 예측 점수 | 99.84% |
| 근거 수준 | L4 (기전 연구 수준, 직접적인 임상 근거 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 norepinephrine은 알파 및 베타 아드레날린 수용체에 작용하는 카테콜아민입니다. 전신 투여 시에는 알파-1 매개 혈관수축과 심장 자극 효과를 내는 승압제로 사용됩니다.

기도 긴장도, 기도 신경 분포, 천식·COPD의 신경면역 조절에는 아드레날린 신호가 관여한다고 보고되어 있습니다. 다만 이 연결은 간접적입니다. norepinephrine은 기관지확장제가 아니며, 승압 용량에서는 베타-2 작용이 제한적입니다. 또한 COPD와 저산소혈증 환자에서는 교감신경 긴장 증가와 빈맥성 부정맥 위험이 우려됩니다. 높은 TxGNN 점수는 임상 근거가 아니라 네트워크 기반 예측을 반영합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | 모집 중 | 420 | 고혈압 및 건강인에서 혈관 기능, 운동 재활, 골격근 구심성 피드백 연구. 폐쇄성 폐질환에 대한 norepinephrine 치료 시험이 아니며 관련성 낮음 |

## 문헌 근거

관련성이 있는 문헌 위주로 정리했습니다. RCT는 없고 대부분 리뷰와 생리 연구입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29696025](https://pubmed.ncbi.nlm.nih.gov/29696025/) | 2018 | Review | Front Immunol | 알레르기성 천식과 바이러스 감염에서의 아드레날린 신호 |
| [41601146](https://pubmed.ncbi.nlm.nih.gov/41601146/) | 2026 | Review | Ann Med | 호흡기 병태생리에서의 신경면역 회로와 표적 치료 |
| [40870471](https://pubmed.ncbi.nlm.nih.gov/40870471/) | 2025 | Review | Medicina | COPD 동반 불안·우울의 관리 |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Review | Pneumologie | 천식·COPD에서 기도 신경 분포의 역할 |
| [24486056](https://pubmed.ncbi.nlm.nih.gov/24486056/) | 2014 | Review | Semin Immunol | 염증의 신경내분비 조절 |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Review | Crit Care Clin | 중환자 치료에서의 카테콜아민 |
| [3966494](https://pubmed.ncbi.nlm.nih.gov/3966494/) | 1985 | 생리 연구 | Am J Med | 만성 폐쇄성 폐질환에서 저산소혈증이 나트륨·수분 배설에 미치는 영향 |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | 연구 | Am J Med | COPD 급성 호흡부전 환자의 고혈압 기전(norepinephrine 포함) |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | 생리 연구 | Am J Physiol Heart Circ Physiol | COPD 환자의 운동 중 근육 알파-아드레날린 반응성 |

## 한국 시판 정보

허가 적응증 텍스트는 허가사항 문서 링크로만 제공되어 요약하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200708895 | 큐프린주 | 주사제 (갈색 앰플) | 허가사항 참조 |
| 200101307 | 노르핀주 | 주사제 (갈색 앰플) | 허가사항 참조 |
| 199806705 | 노르아드레나린0.1% | 주사제 (앰플) | 허가사항 참조 |
| 200202661 | 노르에피린주사 | 주사제 (갈색 앰플) | 허가사항 참조 |
| 201504497 | 노르에핀주 (수출용) | 주사제 (갈색 앰플) | 허가사항 참조 |

## 안전성 고려사항

- **금기 질환 (지식그래프 기반, 허가 문구 아님)**: 고혈압성 질환, 고혈압, 혈전성 질환
- **약물 상호작용**: 총 70건이 확인되었으며, 표시된 항목은 모두 중등도(Moderate)입니다.
  - 혈당강하제: acarbose, metformin, pioglitazone, repaglinide, chlorpropamide
  - DPP-4 억제제: sitagliptin, saxagliptin, linagliptin, alogliptin
  - SGLT2 억제제: canagliflozin, dapagliflozin, empagliflozin
  - GLP-1 계열: semaglutide, dulaglutide, albiglutide
  - 인슐린: aspart, degludec, detemir
  - 식욕억제제: phentermine, diethylpropion
- 허가사항의 경고·금기 정보는 이번 자료에서 확인되지 않았으므로 허가사항을 직접 참조해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐쇄성 폐질환에 대한 직접적인 임상 근거가 없고 문헌도 간접적인 기전 설명에 그칩니다. norepinephrine은 기관지확장제가 아니며, COPD와 저산소혈증 환자에서 빈맥성 부정맥과 교감신경 과활성 위험이 우려됩니다. 높은 TxGNN 점수만으로는 진행을 뒷받침하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기)의 확보 및 분석. 안전성 선별 단계로 넘어가기 위한 필수 선행 과제입니다.
- 상세한 작용 기전(MOA) 데이터 보완
- 폐쇄성 폐질환에서의 norepinephrine 치료 효과를 직접 평가한 전임상·임상 근거
- 투여 경로 적합성 검토 (현재 주사제만 있고, 폐질환 치료에 적합한 경로인지 불명확)

**참고:** 같은 약물의 다른 예측 적응증인 호흡기 기형(Respiratory malformation, 99.84%)과 Rienhoff 증후군(99.83%)도 근거 수준 L5로 모두 Hold입니다. 임상시험이 없고 문헌은 치료 효과와 무관하거나(호흡기 기형은 약물 노출 위험 연구 위주, Rienhoff 증후군은 문헌 없음), 기전적 연결도 확인되지 않아 그래프 기반 산출물로 판단됩니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

