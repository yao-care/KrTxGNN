---
layout: default
title: Risperidone
parent: 모델 예측만 (L5)
nav_order: 659
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Risperidone: 예측 신규 적응증 가족성 수평 시선마비 및 진행성 척추측만증 (gaze palsy, familial horizontal… (근거 수준 L5). 기존 적응증: 허가증에 적응증 본문 없이 PDF 링크만 있어 본문을 확인할 수 없음 (일반적으로 조현병 등 정신질환에 쓰이는 비정형 항정신…"
monitor_inn: "RISPERIDONE"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "asperger syndrome, susceptibility to", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania", "major affective disorder"]
---

# Risperidone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Risperidone: 항정신병약(조현병 등)에서 가족성 수평 시선마비 및 진행성 척추측만증으로
{: .text-alpha }

## 한 문장 요약

Risperidone은 도파민 D2/세로토닌 5-HT2A 수용체 길항제 계열의 비정형 항정신병약으로, 한국에서는 정신질환 치료제로 허가·시판되고 있습니다.
TxGNN 모델은 **가족성 수평 시선마비 및 진행성 척추측만증(gaze palsy, familial horizontal, with progressive scoliosis)**에 효과가 있을 수 있다고 예측하며, 예측 점수는 높지만 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
이 예측은 모델 점수에만 근거하고 있어 현재로서는 실제 근거가 없는 가설 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 본문 없이 PDF 링크만 있어 본문을 확인할 수 없음 (일반적으로 조현병 등 정신질환에 쓰이는 비정형 항정신병약) |
| 예측 신규 적응증 | 가족성 수평 시선마비 및 진행성 척추측만증 (gaze palsy, familial horizontal, with progressive scoliosis) |
| TxGNN 예측 점수 | 99.76% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Risperidone은 D2/5-HT2A 길항 작용을 가진 항정신병약으로 알려져 있습니다.

예측된 질환은 ROBO3 관련 희귀 유전질환으로, 축삭 유도와 뇌간 발달의 이상이 원인입니다. Risperidone의 수용체 길항 작용과 이 병리 사이에서는 개연성 있는 기전적 연결고리를 찾지 못했습니다. 높은 TxGNN 점수는 지식 그래프 기반 예측일 뿐, 약리학적·임상적 타당성을 입증하지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 다른 예측 적응증 참고

이 약물에는 다른 예측 적응증도 있으며, 근거 수준은 질환마다 크게 다릅니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|-----------|-----------|---------|---------|------|
| 2 | 아스퍼거 증후군 감수성 | 99.74% | L5 | Hold | 자폐 관련 과민성에 대한 허가 사례는 있으나 이 항목 자체의 근거는 없음 |
| 3 | 아멜로세레브로저한성 증후군 | 99.69% | L5 | Hold | 기전 근거 및 연구 없음 |
| 4 | Phelan-McDermid 증후군 | 99.59% | L4 | Research Question | 리뷰 1편, 제브라피시 연구 1편. 인체 시험 없음 |
| 5 | 발모벽 (trichotillomania) | 99.51% | L4 | Research Question | 증례 보고·증례 시리즈 중심. 대조 시험 없음 |
| 6 | 주요 정동장애 (major affective disorder) | 99.11% | L1 | Proceed with Guardrails | 항우울제 불응성 우울증에서 보조요법 Phase 3 완료 시험 2건(NCT00095134, n=630; NCT00044681, n=258)과 양극성장애 Phase 3 시험 1건(NCT00277654, n=111) |

이 중 근거가 가장 풍부한 것은 6순위(주요 정동장애)입니다. 이 보고서가 다루는 1순위 질환과는 별개의 평가 대상입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201701456 | 리스펜오디정1밀리그램 | 구강붕해정 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201701456/EE) 참조 |
| 200400317 | 리스프리정2밀리그램 | 필름코팅정 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200400317/EE) 참조 |
| 201707618 | 리스달정2밀리그램 | 필름코팅정 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707618/EE) 참조 |
| 202102658 | 리스페달정0.5밀리그램 (한국얀센) | 필름코팅정 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202102658/EE) 참조 |
| 202502344 | 유제디원엠주50밀리그램 (한독테바) | 서방형 주사제 | [허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502344/EE) 참조 |

전체 20건 중 5건만 표시했습니다. 허가 적응증 본문은 이번 데이터에 텍스트로 수록되어 있지 않고 허가사항 PDF 링크로만 제공됩니다.

## 안전성 고려사항

허가사항의 경고 및 금기 본문은 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

- **지식 그래프 기반 금기 질환 (허가 문구가 아님)**: 기립성 저혈압, 다계통 위축증, 간부전·간질환, 간질, 당뇨병·고혈당·당뇨병성 케톤산증, 호중구감소증·무과립구증, 고지혈증, 비만, 뇌졸중·뇌혈관 질환, 심근경색, 심장 전도 질환 등 30개 질환이 연결되어 있습니다. 실제 금기 여부는 허가사항으로 확인해야 합니다.
- **약물 상호작용**: 총 100건이 조회되었습니다. 이 중 **주요(Major) 상호작용**으로 확인된 약물은 Bupropion, Morphine입니다. 중등도(Moderate) 상호작용에는 Metformin, Epinephrine, Hydrocortisone, Atropine, Canagliflozin, Alogliptin 등이 있습니다. 경미(Minor) 상호작용에는 Ranitidine이 있습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험과 문헌이 전혀 없고, 질환의 병리(ROBO3 관련 축삭 유도 이상)와 risperidone의 약리 작용 사이에서 기전적 연결고리도 찾지 못했습니다. 모델 예측만으로는 진행 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 경고·금기·적응증 본문 확보 (현재 안전성 1차 검토의 차단 요소)
- 상세한 작용 기전(MOA) 데이터 확보
- 이 질환과 risperidone을 연결하는 전임상·기전 연구 또는 증례 근거
- 우선순위 재검토: 근거가 더 풍부한 다른 예측 적응증, 특히 주요 정동장애를 먼저 평가하는 방안
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

