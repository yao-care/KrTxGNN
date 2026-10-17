---
layout: default
title: Acetazolamide
parent: 모델 예측만 (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetazolamide: 예측 신규 적응증 운동 유발성 악성 고열증 (exercise-induced malignant hyperthermia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 포함되어 있지 않아 확인할 수 없음 (허가 문서 링크만 제공됨)"
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
---

# Acetazolamide
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

# Acetazolamide: 허가 적응증에서 운동 유발성 악성 고열증으로

## 한 문장 요약

Acetazolamide는 한국에서 주사제와 정제로 허가·시판 중인 탄산탈수효소 억제제 계열 약물입니다. TxGNN 모델은 **운동 유발성 악성 고열증(exercise-induced malignant hyperthermia)**에 효과가 있을 수 있다고 예측하지만, 이 적응증을 직접 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 포함되어 있지 않아 확인할 수 없음 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 운동 유발성 악성 고열증 (exercise-induced malignant hyperthermia) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 acetazolamide는 탄산탈수효소를 억제하여 산-염기 균형과 이온 이동에 영향을 주는 것으로 알려져 있습니다. 이 때문에 근육의 이온 조절에 영향을 줄 가능성을 이론적으로 생각해 볼 수 있습니다.

그러나 악성 고열증은 주로 리아노딘 수용체(ryanodine receptor)와 칼슘 조절 이상으로 발생합니다. 이번에 정리된 데이터에서는 탄산탈수효소 억제가 이 질환과 연결된다는 근거를 찾을 수 없었습니다. 따라서 이 예측은 지식 그래프에 기반한 가설일 뿐, 검증된 기전적 연결고리가 아닙니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199701927 | 졸라딘주사 (아세타졸아미드) | 동결건조 분말 주사제 (유리 바이알) | 허가 문서 참조 (MFDS 허가 문서 링크만 제공됨) |
| 201403403 | 아세타졸정 (아세타졸아미드) | 흰색 원형 정제 | 허가 문서 참조 (MFDS 허가 문서 링크만 제공됨) |

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 이 중 일부를 확인했습니다.
  - **주의 필요 (Major)**: Acetylsalicylic acid(아스피린), Cisapride
  - **중등도 (Moderate)**: 당뇨병 치료제(Acarbose, Acetohexamide, Alogliptin, Canagliflozin, Dapagliflozin, Chlorpropamide, Albiglutide, Dulaglutide), 스테로이드(Dexamethasone, Betamethasone, Beclomethasone), Amphotericin B 제제, 변비약(Bisacodyl, Castor oil)
  - **경미 (Minor)**: Doxycycline
- **후보 질환별 안전 신호** (문헌 및 기전 검토 기준):
  - 장폐색 및 가성 장폐색: acetazolamide 유발 무력성 장폐색(adynamic ileus) 증례가 보고되어, 이득보다 위해 가능성이 큽니다.
  - 심근병증: 정맥 투여 후 비심인성 폐부종이 유발된 증례가 있습니다.
  - 간경변성 심근병증: 신장의 암모니아 저류가 증가하여 간성 뇌증을 유발할 수 있습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
운동 유발성 악성 고열증에 대한 임상시험과 문헌이 없고, 탄산탈수효소 억제와 이 질환의 병태생리 사이에 기전적 연결도 확인되지 않았습니다. 근거 수준은 L5로, 점수는 높지만 모델 예측에 그칩니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고, 금기, 허가 적응증)을 내려받아 확인
- 작용 기전(MOA) 데이터 보강 (예: DrugBank 조회)
- 악성 고열증과의 기전적 연결을 검증하는 전임상 연구 또는 문헌 검토
- 상위 후보 중 심근병증 계열은 간접적인 심부전 이뇨 근거만 있으므로, 우선순위를 재검토하고 장폐색 계열은 안전 신호 때문에 진행하지 않을 것을 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

