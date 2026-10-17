---
layout: default
title: Chlorzoxazone
parent: 모델 예측만 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Chlorzoxazone: 예측 신규 적응증 편두통 (Migraine Disorder) (근거 수준 L5). 기존 적응증: 신경통, 요통(허리통), 어깨결림"
monitor_inn: "Chlorzoxazone"
predicted_indications: ["migraine disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "pulmonary hypertension", "atrophoderma vermiculata", "ulerythema ophryogenesis", "kyphoscoliotic heart disease", "rheumatoid arthritis", "headache disorder"]
---

# Chlorzoxazone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Chlorzoxazone: 신경통·요통에서 편두통으로

## 한 문장 요약

Chlorzoxazone은 중추성 근이완제로, 한국에서 신경통, 요통(허리통), 어깨결림 치료에 사용되고 있습니다.
TxGNN 모델은 **편두통(Migraine Disorder)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이며 관련 문헌 3편도 소뇌 운동실조와 어지럼증을 다룬 것으로 편두통 치료 효과를 직접 뒷받침하지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 신경통, 요통(허리통), 어깨결림 |
| 예측 신규 적응증 | 편두통 (Migraine Disorder) |
| TxGNN 예측 점수 | 99.73% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Chlorzoxazone은 근골격계 통증과 근육 경련에 쓰이는 중추성 근이완제이며, 칼슘 의존성 칼륨 채널(SK/IK)을 활성화한다고 보고되어 있습니다.

편두통과 이어지는 유일한 연결고리는 이 이온 채널 조절 가능성입니다. 편두통의 일부 유전형(예: CACNA1A 변이)은 채널 이상과 관련되며, 마우스 모델 연구(PMID 23115190)에서 칼슘 의존성 칼륨 채널 활성화제가 CaV2.1 채널 이상으로 인한 운동실조를 완화했습니다. 다만 이는 운동실조 모델이며 편두통 자체에 대한 근거는 아닙니다.

따라서 현재 편두통에 대한 직접적인 기전적 근거는 확립되어 있지 않습니다. 0.997이라는 높은 예측 점수는 계산 모델의 결과일 뿐 임상적 뒷받침이 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [27083881](https://pubmed.ncbi.nlm.nih.gov/27083881/) | 2016 | Review | Journal of Neurology | 소뇌 및 중추 전정 질환의 약물치료 개관. 편두통 치료 근거는 아님 |
| [24000301](https://pubmed.ncbi.nlm.nih.gov/24000301/) | 2013 | Review | Deutsches Arzteblatt International | 말초성·중추성 어지럼증의 치료와 자연 경과. 전정 편두통이 전체 어지럼증의 11.4% |
| [23115190](https://pubmed.ncbi.nlm.nih.gov/23115190/) | 2012 | 전임상(동물 연구) | Journal of Neuroscience | Cacna1a 변이 마우스에서 칼슘 의존성 칼륨 채널 활성화제가 소뇌 운동실조를 완화 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202400777 | 렉스펜에스정 | 흰색의 원형 필름코팅정 | 신경통, 허리통, 어깨결림 |
| 202400815 | 티엔클라젠정 | 흰색의 원형 필름코팅정 | 신경통, 요통(허리통), 어깨결림 |
| 202400957 | 다푸러펜정 | 흰색의 원형 필름코팅정 | 신경통, 허리통, 어깨결림 |
| 201402338 | 케어담정 | 흰색의 장방형 필름코팅정 | 신경통, 요통, 어깨결림 |
| 202400351 | 리렉스담정 | 흰색의 원형 필름코팅정 | 신경통, 허리통, 어깨결림 |

전체 20건이 모두 단일제이며 유효 상태입니다.

## 안전성 고려사항

- **금기(지식그래프 기반 참고 정보, 허가 문서 아님)**: 간부전, 간질환, 담낭질환, 약물 남용/의존, 약물유발 간손상, 아세트아미노펜 중독과 관련된 것으로 나타납니다.
- **약물 상호작용**: 총 72건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major**: Morphine, Morphine(리포좀)
  - **Moderate**: Dronabinol, Metoclopramide, Nabilone, Naltrexone, Opium, Sibutramine, Ethanol, Promethazine
- **기타 안전 신호**: 다중 약물 과다복용 사례(PMID 19606800)에서 메트헤모글로빈혈증이 보고되었습니다. 이는 효능 근거가 아닌 안전성 신호입니다.

허가사항 상의 경고 및 금기는 확인되지 않았으므로, 상세 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
편두통에 대한 임상시험이 없고 문헌도 소뇌·전정 질환 및 동물 모델에 국한되어 있어 근거 수준은 L5입니다. 높은 예측 점수만으로는 진행 근거가 부족하며, 간질환 관련 금기 정보도 고려해야 합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 안전성 검토
- 작용 기전(MOA) 데이터 보강, 특히 칼륨 채널 조절과 편두통 병태생리의 연결 검증
- 편두통 또는 긴장형 두통에 대한 전임상·관찰 연구 및 소규모 탐색 임상시험
- 참고: 순위 9의 류마티스 관절염(근이완제를 통증·경련 보조요법으로 사용하는 가능성, L4)은 질병 조절 효과는 없고 오래된 보고 위주이지만, 별도 후속 연구 질문으로 검토할 수 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

