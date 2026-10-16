---
layout: default
title: Chlorthalidone
parent: 모델 예측만 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Chlorthalidone: 예측 신규 적응증 원발성 유전성 녹내장 (Primary hereditary glaucoma) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 PDF 링크로만 제공되어 본문이 없음. 일반적으로 고혈압·부종 치료제)"
monitor_inn: "CHLORTHALIDONE"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Chlorthalidone: 고혈압에서 녹내장으로

## 한 문장 요약

Chlorthalidone은 티아지드계 이뇨제로, 한국에서 단일제 및 로사르탄 복합제로 시판 중입니다. 허가 적응증 원문은 이번 데이터에 파싱되어 있지 않아, 고혈압 계열 약물이라는 일반적 지식에 근거해 해석했습니다.
TxGNN 모델은 **원발성 유전성 녹내장(Primary hereditary glaucoma)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 PDF 링크로만 제공되어 본문이 없음. 일반적으로 고혈압·부종 치료제) |
| 예측 신규 적응증 | 원발성 유전성 녹내장 (Primary hereditary glaucoma) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Chlorthalidone은 티아지드 유사 이뇨제로 알려져 있으며, 신장에서 나트륨과 수분 재흡수를 줄여 혈압과 체액량을 낮춥니다.

녹내장과의 연관성은 안압 조절에 관여하는 방수 역학이나 이온·체액 수송을 통한 간접 영향 정도로만 추정할 수 있습니다. 이는 가설 수준이며, 티아지드 유사 이뇨제는 확립된 녹내장 치료제가 아닙니다. 점수가 높더라도 이는 모델 예측일 뿐, 실제 근거로 이어지지 않았습니다.

참고로 같은 예측 목록에서 상대적으로 가장 근거가 있는 항목은 **만성 폐성심(chronic pulmonary heart disease)**입니다(점수 99.82%, 근거 수준 L4). 울혈성 심부전에서 이뇨 효과를 보고한 1967년 문헌이 있으나, 간접적이고 오래된 자료입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202500118 | 클로베네정25밀리그램 (클로르탈리돈) | 분홍색 장방형 정제 | 허가사항 원문 참조 |
| 202202296 | 클로잘탄정100/12.5밀리그램 (로사르탄, 클로르탈리돈) | 노란색 타원형 필름코팅정 | 허가사항 원문 참조 |
| 200302309 | 하이그로톤정25밀리그램 (클로르탈리돈) | 연분홍색 원형 정제 | 허가사항 원문 참조 |
| 202301412 | 클로잘탄정50/6.25밀리그램 (로사르탄, 클로르탈리돈) | 분홍색 타원형 필름코팅정 | 허가사항 원문 참조 |
| 202202297 | 클로잘탄정50/12.5밀리그램 (로사르탄, 클로르탈리돈) | 흰색 타원형 필름코팅정 | 허가사항 원문 참조 |

## 안전성 고려사항

- **약물 상호작용**: 이번 데이터에서 총 100건의 상호작용이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **주의 필요(Major)**: Cisapride, Dolasetron
  - **중등도(Moderate)**: Acarbose, Metformin, Alogliptin, Albiglutide 등 혈당강하제, Hydrocortisone, Dexamethasone, Triamcinolone 등 코르티코스테roid, Omeprazole, Rabeprazole, Amphotericin B, Bupropion, Morphine, Cholecalciferol
  - **경미(Minor)**: Doxycycline, Atropine, Hyoscyamine
- **지식그래프상 금기 관련 질환** (허가사항 문구가 아닌 모델 지식그래프 기준): 간부전, 신장 질환, 무뇨증, 통풍, 고요산혈증, 제2형 당뇨병, 고칼슘혈증, 칼륨 결핍, 천식, 전신홍반루푸스, 췌장염, 소화성 궤양, 건선, 심근경색 등.

허가사항의 경고 및 금기 문구는 이번 데이터에 포함되지 않았으므로, 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
녹내장 예측은 TxGNN 점수만 높을 뿐 임상시험과 문헌이 전혀 없고, 기전적 연결도 가설 수준입니다. 허가 적응증과 작용 기전 데이터도 비어 있어 안전성 검토를 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기)의 PDF 본문 확보 및 파싱
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 안압 및 방수 역학에 대한 전임상·기전 연구 검토 문헌 조사
- 근거가 상대적으로 나은 만성 폐성심 등 다른 예측 적응증을 우선 검토할지 판단
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

