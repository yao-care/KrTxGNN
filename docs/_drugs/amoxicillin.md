---
layout: default
title: Amoxicillin
parent: 모델 예측만 (L5)
nav_order: 68
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Amoxicillin: 예측 신규 적응증 고아밀라아제혈증 (Hyperamylasemia) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크 형태로만 확인되어 구체적 내용을 기재할 수 없음 (항생제로서 세균 감염 치료)"
monitor_inn: "AMOXICILLIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Amoxicillin: 세균 감염에서 고아밀라아제혈증으로
{: .text-alpha }

## 한 문장 요약

Amoxicillin은 베타락탐계 항생제로, 세균의 세포벽 합성을 억제하여 감염 치료에 사용되어 왔습니다.
TxGNN 모델은 **고아밀라아제혈증(Hyperamylasemia)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크 형태로만 확인되어 구체적 내용을 기재할 수 없음 (항생제로서 세균 감염 치료) |
| 예측 신규 적응증 | 고아밀라아제혈증 (Hyperamylasemia) |
| TxGNN 예측 점수 | 0.9963 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 12건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Amoxicillin은 세균 세포벽 합성을 억제하는 베타락탐계 항생제이며, 단독제 외에 클라불란산 또는 설박탐과의 복합 제형으로도 허가되어 있습니다.

그러나 고아밀라제혈증은 아밀라제 수치가 상승하는 상태로, 항균 작용과 직접적인 연관이 확인되지 않습니다. Amoxicillin이 아밀라제 조절에 작용한다는 알려진 기전은 없으며, 이 예측은 TxGNN 모델(딥러닝)의 점수로서 관련 질환 사이에서 모델이 학습한 유사성을 반영할 수 있을 뿐, 생물학적 근거는 아닙니다.

참고로 같은 모델이 제시한 상위 예측들(다클론성 과점도 증후군, 선천성 무알부민혈증, 혈액형 부적합, 전악성 혈액계 질환, 단클론 감마병증, 후천성 말초신경병증 동반 혈액질환, 패혈성 페스트)도 대부분 타당한 기전이나 임상 근거가 없습니다. 패혈성 페스트만 항균제 관점에서 생물학적으로 그럴듯하지만, 베타락탐은 세포 내 페스트균에 활성이 낮고 1차 치료제도 아닙니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200801301 | 아시박탐주1.5그램 | 주사제 (바이알) | 허가사항 문서 참조 |
| 201109013 | 아목신캡슐250밀리그램(수출용) | 경질캡슐제 | 허가사항 문서 참조 |
| 201109014 | 아목신캡슐500밀리그램(수출용) | 경질캡슐제 | 허가사항 문서 참조 |
| 199200517 | 아모크라주1.2그램 | 주사제 (바이알) | 허가사항 문서 참조 |
| 200607737 | 유한아목시실린정250밀리그람(수출용) | 제피정 | 허가사항 문서 참조 |

이 외에도 총 12건의 유효 허가가 있으며, 모두 단일 성분 허가로 분류되어 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 수집된 데이터에서 100건의 상호작용이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **주의 필요(Major)**: Methotrexate, 콜레라 생백신(Vibrio cholerae CVD 103-HgR)
  - **중등도(Moderate)**: Doxycycline, Minocycline, Demeclocycline, Ethinylestradiol, Estradiol, Mycophenolate mofetil, Entecavir, Dicoumarol, Anisindione, Balsalazide 등
  - **경미(Minor)**: Allopurinol, Amiloride, Azithromycin, Clarithromycin, Erythromycin
- **지식 그래프상 금기 관련 질환**(허가 문서가 아닌 모델 지식 그래프 기준): 간부전·간질환, 신장질환, 담즙정체, 포르피린증, 긴 QT 증후군, 심실빈맥, 중증근무력증, *Clostridium difficile* 대장염, 골다공증, 골절, 전염성 단핵구증 등

허가사항의 경고 및 금기 항목은 허가 문서를 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고아밀라아제혈증에 대한 임상시험과 문헌이 없고, 기전적 연결고리도 확인되지 않아 모델 점수(0.9963)만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (허가사항 PDF 확인)
- 상세 작용 기전(MOA) 데이터 보완
- 고아밀라아제혈증과 Amoxicillin의 연관성을 뒷받침하는 전임상 또는 임상 근거
- 다른 후보(예: 패혈성 페스트)는 항균제로서의 타당성이 있어 별도 연구 질문으로 검토할 수 있으나, 베타락탐의 한계로 우선순위는 낮음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

