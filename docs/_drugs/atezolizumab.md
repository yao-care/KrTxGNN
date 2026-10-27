---
layout: default
title: Atezolizumab
parent: 모델 예측만 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Atezolizumab: 예측 신규 적응증 전립선 요도 요로상피암 (Prostatic urethra urothelial carcinoma) (근거 수준 L5). 기존 적응증: 한국 허가 적응증 원문은 이번 데이터에 텍스트로 수록되지 않았습니다(허가 문서 링크만 제공). 허가사항을 참조하세요"
monitor_inn: "Atezolizumab"
predicted_indications: ["prostatic urethra urothelial carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Atezolizumab
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

## Atezolizumab: 요로상피암에서 전립선 요도 요로상피암으로
{: .text-alpha }

## 한 문장 요약

Atezolizumab(티쎈트릭주)은 PD-L1을 차단하는 면역항암제로, 한국에서 허가를 받아 시판되고 있습니다.
TxGNN 모델은 **전립선 요도 요로상피암(prostatic urethra urothelial carcinoma)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**(1b상)이 이 방향을 간접적으로 지지하지만 직접 관련된 문헌은 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 적응증 원문은 이번 데이터에 텍스트로 수록되지 않았습니다(허가 문서 링크만 제공). 허가사항을 참조하세요. |
| 예측 신규 적응증 | 전립선 요도 요로상피암 (Prostatic urethra urothelial carcinoma) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 (실제 연구 근거는 Phase 1b 1건뿐이며 L1~L2 기준에 미달) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

> 참고: 데이터에는 해당 후보에 L3로 분류된 값이 있으나, 본 보고서의 판정 규칙(관찰 연구·체계적 문헌고찰 없음, Phase 1b 시험만 존재)에 따라 L5에 가까운 낮은 수준으로 판단했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 atezolizumab은 PD-L1을 표적으로 하는 단일클론항체이며, 방광 등 요로상피암에서 효능이 입증되어 있어 기전상 같은 조직형인 전립선 요도 요로상피암에도 적용 가능할 수 있습니다.

전립선 요도 요로상피암은 방광 요로상피암과 조직학적으로 동일한 요로상피 기원입니다. 따라서 PD-1/PD-L1 축을 공유한다는 점에서 생물학적 타당성이 있습니다.

다만 이 연관성은 모델 예측과 간접 추론에 근거합니다. 연결된 시험도 전립선 요도 질환에 특화되지 않은 고형암 대상 1b상 연구입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 (1b) | 모집 종료, 진행 중 | 914 | 진행성·전이성 고형암(요로상피암 포함)에서 cabozantinib 단독 또는 atezolizumab 병용의 안전성·내약성·예비 효능 평가. 전립선 요도를 직접 평가하지는 않음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201700266 | 티쎈트릭주(아테졸리주맙) | 바이알 주사제 (무색~연한 노랑 액체) | 허가 문서 링크로만 제공됨(허가사항 참조) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 (PD-L1 차단 항체) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 데이터에는 총 75건의 상호작용이 있으며, 확인된 주요 항목은 다음과 같습니다.
  - **Major**: adalimumab, baricitinib, BCG 생균 백신(Tice 균주)
  - **Moderate**: 코르티코스테로이드류(hydrocortisone, prednisone, dexamethasone, methylprednisolone 등), roflumilast, azathioprine, alemtuzumab, anakinra, 파상풍 톡소이드 및 탄저 백신 등

경고 및 금기 항목은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
전립선 요도 요로상피암에 대한 직접 근거는 전립선 요도 질환에 특화되지 않은 Phase 1b 시험 1건뿐이며, 관련 문헌이 없습니다. 기전적 타당성은 있으나 TxGNN 예측과 간접 추론에 의존하고 있어 연구 질문(Research Question) 단계에 머물러 있습니다.

**진행하려면 필요한 것:**
- 허가증의 적응증 원문과 경고·금기 정보 확보(MFDS 허가사항 PDF 분석)
- 상세한 작용 기전(MOA) 데이터 확보(DrugBank)
- 전립선 요도 요로상피암에 대한 후향 연구, 증례 보고 또는 하위군 분석 근거
- 이 아형을 포함하는 Phase 2 이상의 시험 데이터

### 참고: 기타 예측 적응증

| 순위 | 예측 적응증 | 점수 | 근거 | 결정 |
|------|-----------|------|------|------|
| 2 | 신우 육종양 이행세포암 | 99.98% | 임상시험·문헌 없음 | Hold |
| 3 | 침윤성 방광 요로상피암 육종양 변이형 | 99.98% | 임상시험·문헌 없음 | Hold |
| 4 | 신우 유두상 요로상피암 | 99.98% | 임상시험·문헌 없음 | Hold |
| 6 | 자궁내막경부 암종 | 99.92% | Phase 2 1건(n=11), Phase 1 1건(n=40), 리뷰 1편 | 추가 연구 필요 |

이 중 자궁경부 암종은 완료된 소규모 시험이 있으나 표본이 작고 조직형 특이성이 낮아 추가 검증이 필요합니다. 나머지 후보는 시험과 문헌이 없어 모델 예측에만 의존합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

