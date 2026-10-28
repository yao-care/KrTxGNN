---
layout: default
title: Riluzole
parent: 모델 예측만 (L5)
nav_order: 655
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Riluzole: 예측 신규 적응증 양측 두정-후두 부시상 다소뇌회증 (bilateral parasagittal parieto-occipital polymicr… (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 PDF 링크로만 제공되어 확인 불가 (문헌상 ALS 치료제)"
monitor_inn: "RILUZOLE"
predicted_indications: ["bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "monomelic amyotrophy", "Mills syndrome", "autosomal dominant mitochondrial myopathy with exercise intolerance", "amyotrohpic lateral sclerosis type 22"]
---

# Riluzole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Riluzole: 근위축성 측삭경화증에서 양측 두정-후두 부시상 다소뇌회증으로
{: .text-alpha }

## 한 문장 요약

Riluzole은 한국에서 근위축성 측삭경화증(ALS) 치료제로 시판 중인 약물입니다(허가 적응증 원문은 데이터에 링크로만 제공되어 있어 ALS는 문헌 근거에 따른 설명입니다).
TxGNN 모델은 **양측 두정-후두 부시상 다소뇌회증(bilateral parasagittal parieto-occipital polymicrogyria)**에 효과가 있을 수 있다고 예측하지만(점수 0.9999), 이 예측을 지지하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 근거 수준은 L5(모델 예측만 존재)이며, 현재로서는 보류가 적절합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 PDF 링크로만 제공되어 확인 불가 (문헌상 ALS 치료제) |
| 예측 신규 적응증 | 양측 두정-후두 부시상 다소뇌회증 (bilateral parasagittal parieto-occipital polymicrogyria) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Riluzole은 글루타메이트 조절 약물로, 글루타메이트 방출 억제와 나트륨 채널 조절을 통해 흥분독성을 줄이는 것으로 이해됩니다. 이 기전은 ALS 치료의 근거가 됩니다.

반면 다소뇌회증은 신경세포 이동 장애로 생기는 대뇌 피질 기형입니다. Riluzole의 기전과 이 질환 사이의 연관성은 추측 수준이며, 이를 뒷받침하는 임상·문헌 자료도 없습니다. 예측 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 관련 질환 간에 모델이 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

참고로 예측 순위 2위 이하에는 ALS 아형(ALS 22형 등), 하위운동신경원 증후군, 단지성 근위축증, Mills 증후군처럼 기존 적응증과 개념적으로 더 가까운 질환이 있습니다. 반면 축성 척추골간단단 이형성증처럼 기전상 연관이 없어 보이는 질환도 있습니다. 이 보고서는 1순위 예측을 다룹니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201404976 | 유리텍정(리루졸) | 필름코팅정 | 허가 적응증 원문은 PDF 링크로만 제공됨 |
| 200805962 | 리루텍정(리루졸) | 필름코팅정 | 허가 적응증 원문은 PDF 링크로만 제공됨 |
| 202202295 | 테글루틱현탁액(리루졸) | 현탁액제 | 허가 적응증 원문은 PDF 링크로만 제공됨 |

## 안전성 고려사항

- **약물 상호작용**: 총 44건이 조회되었으며 일부는 다음과 같습니다.
  - 중등도: Obeticholic acid, Naltrexone, Deferasirox, Osilodrostat, Anagrelide, Asparaginase, Brentuximab vedotin, Clofarabine, Methotrexate, Epirubicin
  - 경미: Omeprazole, Caffeine, Theophylline, Aminophylline
- **지식그래프상 금기 관련 질환**(허가사항이 아닌 모델 지식그래프 기준): 호중구감소증, 무과립구증, 약물 남용/의존, 고빌리루빈혈증, 길버트 증후군, 간질성 폐질환, 약물 유발 간손상
- 문헌에서는 경구 Riluzole 복용 ALS 환자의 약 50%에서 ALT가 정상 상한을 초과한다고 보고되어, 간기능 모니터링이 필요합니다.

허가사항의 경고 및 금기 정보는 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측(다소뇌회증)을 지지하는 임상시험과 문헌이 없고, 기전상 연관성도 추측에 그칩니다. 근거 수준은 L5입니다.

**진행하려면 필요한 것:**
- Riluzole의 상세 작용 기전(MOA) 데이터 확보
- 허가사항(경고·금기) 확인: 허가증 PDF 분석 필요
- 다소뇌회증에 대한 전임상 또는 기전 연구 근거
- 기전적으로 더 타당한 후보(ALS 22형 등 운동신경원 질환 계열)를 우선 검토하는 방안
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

