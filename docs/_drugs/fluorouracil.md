---
layout: default
title: Fluorouracil
parent: 모델 예측만 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluorouracil: 예측 신규 적응증 질의 포도상 배아형 횡문근육종 (botryoid-type embryonal rhabdomyosarcoma of the vag… (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크로만 제공되어 구체적인 질환명은 확인되지 않음 (허가사항 참조)"
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome"]
---

# Fluorouracil
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

# Fluorouracil: 항암 화학요법에서 횡문근육종으로

## 한 문장 요약

Fluorouracil은 대표적인 항대사제(항암제)로, 한국에서는 주사제와 액제 형태로 시판되고 있습니다. TxGNN 모델은 **횡문근육종 중 질(vagina)의 포도상 배아형(botryoid-type embryonal rhabdomyosarcoma of the vagina)**에 효과가 있을 수 있다고 예측합니다. 다만 이 아형을 직접 뒷받침하는 임상시험과 문헌은 없고, 예측 점수만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크로만 제공되어 구체적인 질환명은 확인되지 않음 (허가사항 참조) |
| 예측 신규 적응증 | 질의 포도상 배아형 횡문근육종 (botryoid-type embryonal rhabdomyosarcoma of the vagina) |
| TxGNN 예측 점수 | 99.75% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 7건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 일반적으로 알려진 정보에 따르면 Fluorouracil은 티미딜산 합성효소(thymidylate synthase)를 억제하고 RNA/DNA에 삽입되는 항대사제로, 빠르게 증식하는 세포의 DNA·RNA 합성을 방해합니다. 증식성 육종에도 이론적으로 적용 가능한 일반적 항증식 기전입니다.

그러나 표준 횡문근육종 치료 요법(VAC/VDC/IE)은 Fluorouracil을 중심으로 하지 않으며, 이 아형에 특이적인 근거도 없습니다. 따라서 예측은 모델 점수에 기반한 가설 단계입니다.

참고로 같은 계열의 다른 예측(횡문근육종 일반, 간 육종, 담관 횡문근육종 등)도 점수는 높지만(99.7% 내외) 직접적인 근거는 제한적이며, 겸상적혈구 질환 계열 예측은 기전상 추측에 가깝고 만성 질환에 쓰기에는 독성 부담이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 이 아형(질의 포도상 배아형 횡문근육종)과 관련된 문헌이 없습니다.

참고로 상위 예측인 일반 횡문근육종(rhabdomyosarcoma)에서 검색된 문헌은 다음과 같으며, 모두 간접적이거나 일화적인 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | 소아 육종에서 보조 화학요법의 가치를 다룬 일반 고찰 |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | 화학요법으로 완치 가능한 진행성 암 개관 (횡문근육종 포함) |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case Report | Case Rep Oncol Med | 성인 설(舌) 횡문근육종 증례. 독소루비신+이포스파미드, 이후 시스플라틴+5-FU에서 질병 진행, 3차 요법으로 반응 |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | 소아 비인두 미분화 암종 코호트 (횡문근육종 특이적이지 않음) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202402958 | 케이메디에프유주 500 mg | 주사제 (갈색 바이알) | 허가사항 참조 |
| 197600064 | 중외5-에프유주(플루오로우라실) | 주사액 (앰플/바이알) | 허가사항 참조 |
| 201401391 | 일동플루오로우라실주사(수출용) | 주사액 (앰플/바이알) | 허가사항 참조 |
| 201206389 | 한국바이오켐플루오로우라실주사500밀리그램(수출용) | 주사액 (바이알) | 허가사항 참조 |
| 199101467 | 유토랄주250밀리그람(플루오로우라실) | 주사제 (앰플) | 허가사항 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Fluoropyrimidine 계열 항대사제) |
| 골수억제 위험 | 중등도 (혈소판감소, 호중구감소, 백혈구감소, 무과립구증이 금기 관련 질환으로 확인됨) |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC(분류 포함), 간·신기능, 구내염·설사 등 위장관 증상 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **금기 관련 질환(지식 그래프 기반, 허가사항 문구 아님)**: 신장 질환, 간 질환, 담낭 질환, 혈소판감소증, 호중구감소증, 무과립구증, 백혈구감소증, 설사성 질환, 활동성 소화성 궤양, 인두염, 구내염, 디히드로피리미딘 탈수소효소(DPD) 결핍
- **약물 상호작용**: 총 100건 조회됨. 주요 항목은 다음과 같습니다.
  - 중등도: Metronidazole, Tinidazole
  - 경미: Cimetidine, Levofloxacin
  - 그 외 다수는 등급 미상 (Pantoprazole, Omeprazole, Metformin, Morphine 등)

정확한 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높지만(99.75%) 이 아형에 대한 임상시험과 문헌이 전혀 없는 모델 예측 단계(L5)입니다. 표준 치료 요법도 Fluorouracil 중심이 아니며, 세포독성 약물로서 안전성 부담이 큽니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (허가사항 PDF 확인 필요)
- 상세한 작용 기전(MOA) 데이터 확보
- 횡문근육종에서 Fluorouracil 특이적 효과를 보여주는 전임상 또는 임상 근거
- 표준 요법(VAC/VDC/IE) 대비 Fluorouracil의 위치를 평가하는 비교 분석
- 투여 경로 적합성 평가 (현재 미확정)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

