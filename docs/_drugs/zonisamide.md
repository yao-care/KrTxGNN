---
layout: default
title: Zonisamide
parent: 모델 예측만 (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Zonisamide: 예측 신규 적응증 투렛 증후군 (Tourette syndrome) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가 문서 링크만 제공됨). 시판 품목은 항경련제로 분류됨"
monitor_inn: "Zonisamide"
predicted_indications: ["Tourette syndrome", "trichotillomania", "methemoglobinemia, alpha type", "methemoglobinemia", "Prinzmetal angina", "methemoglobin reductase deficiency", "manic bipolar affective disorder", "fibromyalgia", "conjunctivitis"]
---

# Zonisamide
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

## Zonisamide: 뇌전증 치료제에서 투렛 증후군으로
{: .text-alpha }

## 한 문장 요약

Zonisamide는 항경련제(뇌전증 치료제)로 한국에서 허가·시판되고 있는 약물입니다. TxGNN 모델은 **투렛 증후군(Tourette syndrome)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 뒷받침하는 임상시험이나 문헌은 현재 **0건**입니다. 한편 예측 순위 7~9위의 양극성 장애, 소아 결신 뇌전증, 섬유근육통에는 일부 문헌 또는 임상시험이 있어 참고용으로 아래에 함께 정리했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가 문서 링크만 제공됨). 시판 품목은 항경련제로 분류됨 |
| 예측 신규 적응증 | 투렛 증후군 (Tourette syndrome) |
| TxGNN 예측 점수 | 99.85% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터가 이 보고서용으로 수집되지 않았습니다. 다만 일반적으로 알려진 바에 따르면 zonisamide는 나트륨 채널과 T형 칼슘 채널을 차단하고, 도파민·세로토닌 신경전달에 영향을 줄 수 있습니다. 이 때문에 틱 회로와 어느 정도 관련될 가능성은 이론상 있으나, 추측 수준입니다.

오히려 항경련제가 틱 장애나 강박장애를 **유발**할 수 있다는 검토 논문(PMID 36005856)이 확인되어, 이 예측은 이득보다 위험 신호일 수 있습니다. 투렛 증후군에 대한 직접적인 임상 근거는 없으므로 예측 점수가 높더라도 기전적 타당성은 약합니다.

### 참고: 다른 예측 적응증의 근거

| 순위 | 적응증 | 점수 | 근거 수준 | 요약 |
|------|--------|------|----------|------|
| 2 | 발모벽 (trichotillomania) | 99.78% | L5 | 임상 근거 없음. 기전 연결은 가설 수준 |
| 3·4·6 | 메트헤모글로빈혈증 관련 질환 (3건) | 99.64%~99.53% | L5 | 기전적 연결 없음. 그래프 구조상 인위적 결과일 가능성 |
| 5 | 프린츠메탈 협심증 | 99.55% | L5 | 칼슘 채널 조절이라는 느슨한 연관만 있음 |
| 7 | 조증형 양극성 장애 | 99.35% | L4 | 양극성 우울증 예비 연구와 조증 유발 사례 보고가 상충 |
| 8 | 결신 뇌전증 | 99.24% | L3 | 기전 연관성 강함. 소규모 관찰 보고 있음 |
| 9 | 섬유근육통 | 99.20% | L4 | 유일한 임상시험이 철회됨 |
| 10 | 결막염 | 99.16% | L5 | 임상 근거 없음. 전신 사용은 비현실적 |

## 임상시험 근거

1위 예측 적응증(투렛 증후군)에 대해서는 현재 관련 임상시험 등록이 없습니다.

참고로 9위 예측인 섬유근육통에는 다음 시험이 등록되어 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00259636](https://clinicaltrials.gov/study/NCT00259636) | Phase 4 | 철회됨 | 0 | 섬유근육통·편두통 환자에서 zonisamide vs 위약 무작위 배정 계획. 참여자 0명으로 근거 없음 |

## 문헌 근거

1위 예측 적응증(투렛 증후군)에 대해서는 현재 관련 문헌이 없습니다. 아래는 투렛 증후군 관련 안전성 신호와, 순위가 낮은 예측 적응증 중 zonisamide 특이적 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36005856](https://pubmed.ncbi.nlm.nih.gov/36005856/) | 2022 | Review | Expert Rev Neurother | 항경련제가 강박장애·틱 장애를 유발할 수 있음 (위험 신호) |
| [17163811](https://pubmed.ncbi.nlm.nih.gov/17163811/) | 2007 | 임상 연구 (설계 미확인) | Expert Opin Pharmacother | 양극성 우울증에 대한 공개 표지 예비 연구 평가 |
| [2109869](https://pubmed.ncbi.nlm.nih.gov/2109869/) | 1990 | Case report | Psychosomatics | Zonisamide로 유발된 조증 |
| [15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/) | 2005 | 임상 보고 (차트 리뷰) | Epilepsy Res | 결신 발작 소아 45명 중 23명(51.1%)에서 발작 소실 |
| [24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/) | 2014 | 증례 시리즈 | Epilepsy Res | 난치성 연소기 결신 뇌전증에서 zonisamide 효과 평가 |
| [15634623](https://pubmed.ncbi.nlm.nih.gov/15634623/) | 2004 | 후향 연구 | Epileptic Disord | 연소기 근간대 뇌전증 15명에서 효능·내약성 평가 |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | 네트워크 메타분석 | Cochrane Database Syst Rev | 뇌전증 단독요법 항경련제 비교 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199000165 | 엑세그란정(조니사미드) (동아에스티) | 백색의 원형 필름코팅정 | 허가 적응증 본문 미확인 (허가 문서 참조) |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이 보고서에 포함되지 않았으므로 허가사항을 참조하세요.

- **지식 그래프 기반 금기 신호 (허가 문서 아님)**: 불안장애, 정신병적 장애, 조현정동장애 등 정신 질환, 신장·간·담낭 질환, 신장결석, 대사성 산증, 무과립구증·호중구감소증 등이 보고되어 있습니다. 허가 문서가 아닌 지식 그래프 기반이므로 참고용입니다.
- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: 항콜린제 계열(Methscopolamine, Hyoscyamine, Atropine, Scopolamine, Glycopyrronium, Clidinium, Dicyclomine, Trospium, Mepenzolate, Propantheline), Metformin
  - **Moderate**: Aprepitant, Morphine, Dexamethasone, Cimetidine, Clarithromycin, Dronabinol, Nabilone, Metoclopramide, Miconazole

## 결론 및 다음 단계

**결정: Hold**

**사유:**
투렛 증후군 예측은 점수(99.85%)가 높지만 임상시험과 문헌이 전혀 없는 모델 예측(L5)에 그치며, 항경련제 유발 틱 장애 보고가 오히려 위험 신호로 작용합니다. 허가사항 기반 안전성 정보와 작용 기전 데이터도 확보되지 않은 상태입니다.

**진행하려면 필요한 것:**
- 허가 문서에서 적응증, 경고, 금기 정보 확보 (현재 확인 불가)
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 투렛 증후군 및 틱 장애에 대한 zonisamide 특이적 문헌·임상 근거 탐색, 틱 유발 위험 평가
- 참고: 결신 뇌전증(L3)은 기존 적응증 계열과 가까워 후속 검토 대상(Research Question)으로 고려할 수 있으나, 대조 임상 근거는 제시되지 않았습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

