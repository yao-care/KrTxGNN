---
layout: default
title: Durvalumab
parent: 모델 예측만 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Durvalumab: 예측 신규 적응증 전립선 요도 요로상피암 (Prostatic urethra urothelial carcinoma) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 확인되지 않았고 허가증 문서 링크만 있습니다. 허가사항 확인이 필요합니다"
monitor_inn: "Durvalumab"
predicted_indications: ["prostatic urethra urothelial carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Durvalumab
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

# Durvalumab: 기존 적응증 정보 미확인에서 전립선 요도 요로상피암으로

## 한 문장 요약

Durvalumab(임핀지주)은 항 PD-L1 항체로, 한국에서 허가되어 시판 중입니다. 다만 이번 보고서용으로 모은 데이터에는 허가 적응증 본문이 담겨 있지 않습니다.
TxGNN 모델은 **전립선 요도 요로상피암(prostatic urethra urothelial carcinoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 **임상시험과 문헌은 0건**입니다.
요로상피암 계열의 다른 예측 질환에서는 소규모 초기 임상시험이 확인되었습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 확인되지 않았고 허가증 문서 링크만 있습니다. 허가사항 확인이 필요합니다. |
| 예측 신규 적응증 | 전립선 요도 요로상피암 (Prostatic urethra urothelial carcinoma) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 Durvalumab은 PD-L1을 차단하는 단일클론항체입니다. 종양이 면역세포의 공격을 피하는 PD-1/PD-L1 경로를 막아 항종양 면역 반응을 되살리는 방식으로 작용합니다.

전립선 요도 요로상피암은 방광 등 다른 요로상피암과 조직학적으로 같은 계열입니다. PD-L1 경로가 관여할 가능성이 있어 TxGNN 예측은 생물학적으로 그럴듯합니다. 다만 이 부위를 직접 다룬 임상시험이나 문헌이 없으므로, 현 단계에서는 가설 수준입니다.

### 참고: 다른 예측 질환의 근거 현황

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 비고 |
|------|---------|-----------|---------|------|
| 2 | 신우 육종양 이행세포암 | 99.98% | L3 | 초기 임상시험 1건 |
| 3 | 침윤성 방광 요로상피암 육종양 변이형 | 99.98% | L3 | 임상시험 2건 |
| 6 | 자궁내막경부암 (endocervical carcinoma) | 99.91% | L3 | 임상시험 1건, 문헌 2편 |

## 임상시험 근거

예측 1순위인 전립선 요도 요로상피암에 대해 현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

예측 1순위인 전립선 요도 요로상피암에 대해 현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201804918 | 임핀지주(더발루맙) | 주사제 (바이알) | 허가증 문서 링크만 확인되며 적응증 본문은 허가사항 참조 |

## 안전성 고려사항

- **약물 상호작용**: 조회 결과 총 81건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **주요(Major)**: Adalimumab
  - **중등도(Moderate)**: 코르티코스테로이드 계열(Hydrocortisone, Prednisone, Prednisolone, Dexamethasone, Methylprednisolone, Budesonide 등), Roflumilast, Alemtuzumab, Anakinra, Alefacept, 파상풍 톡소이드 및 탄저 백신 등
  - **경미(Minor)**: 아연 제제(Zinc acetate, gluconate, sulfate, chloride)
  - 면역 반응에 영향을 줄 수 있는 약물이 많으므로, 병용 시 면역억제제와 코르티코스테로이드 사용 여부를 확인해야 합니다.

경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1순위 예측인 전립선 요도 요로상피암은 모델 예측만 있고 임상시험과 문헌이 없어 근거 수준이 L5입니다. 기전상 타당성은 있으나 실제 근거가 없어 보류합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증 본문) 확보 및 검토
- 상세한 작용 기전 데이터(MOA) 보완
- 전립선 요도 요로상피암에서의 PD-L1 발현 및 반응 관련 문헌 조사와 임상시험 검색
- 근거가 더 있는 대안 후보 검토: 침윤성 방광 요로상피암 육종양 변이형(순위 3, 소규모 Phase 2가 7명 등록 후 조기 종료), 신우 육종양 이행세포암(순위 2, 초기 Phase 1 파일럿)은 연구 질문 단계(Research Question)로 추가 검증 가능
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

