---
layout: default
title: Eculizumab
parent: 모델 예측만 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Eculizumab: 예측 신규 적응증 주기성 조혈 (cyclic hematopoiesis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 확인되지 않음 (허가증에는 식약처 첨부문서 링크만 있음)"
monitor_inn: "Eculizumab"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
---

# Eculizumab
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

## Eculizumab: 발작성 야간 혈색소뇨증 등 보체 매개 질환에서 주기성 조혈(cyclic hematopoiesis)로
{: .text-alpha }

## 한 문장 요약

Eculizumab은 보체 C5를 표적으로 하는 단클론항체로, 한국에서 솔리리스주와 에피스클리주로 허가되어 시판 중입니다. 다만 허가 적응증의 구체적인 내용은 이번 보고서에 편성된 데이터에 포함되어 있지 않습니다.
TxGNN 모델은 **주기성 조혈(cyclic hematopoiesis, 주기성 호중구감소증)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 이 예측은 모델 예측 수준(L5)에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 확인되지 않음 (허가증에는 식약처 첨부문서 링크만 있음) |
| 예측 신규 적응증 | 주기성 조혈 (cyclic hematopoiesis) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 eculizumab은 보체 C5를 억제하여 말단 보체 경로를 차단하는 항체 의약품입니다. 이 기전은 보체 과활성화가 병태의 핵심인 질환에서 효과를 기대할 수 있습니다.

그러나 주기성 호중구감소증은 주로 *ELANE* 변이로 발생하며, 보체 매개 질환이 아닙니다. 따라서 C5 억제를 적용할 근거가 뚜렷하지 않습니다. 높은 TxGNN 점수는 지식 그래프에 기반한 예측일 뿐, 기전상의 연결고리가 확인된 것은 아닙니다.

같은 상위 예측 목록(상위 10위)의 다른 질환도 대부분 선천성 호중구감소증 계열입니다. 이들 역시 보체와의 연관성을 뒷받침하는 자료가 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201000790 | 솔리리스주 (에쿨리주맙) | 주사제 (무색투명한 액, 바이알) | 허가 적응증 본문 확인 불가 (식약처 첨부문서 참조) |
| 202400147 | 에피스클리주 (에쿨리주맙) | 주사제 (무색투명한 액, 바이알) | 허가 적응증 본문 확인 불가 (식약처 첨부문서 참조) |

- 솔리리스주는 한국아스트라제네카, 에피스클리주는 삼성바이오에피스가 제조·판매합니다.

## 안전성 고려사항

- **약물 상호작용**: 총 4건이 확인되었으며 모두 경미(Minor) 수준입니다. 상대 약물은 사람 면역글로불린 G(정맥, 피하, 근육, 정맥·피하 병용 제제)입니다.
- **감염 위험(검토 의견)**: eculizumab은 수막구균 등 협막 세균 감염 위험을 높이는 것으로 알려져 있습니다. 호중구감소증 환자에게 사용하면 중대한 안전성 문제가 될 수 있습니다. 면역결핍 질환(p14 결핍 등)에서도 같은 우려가 있습니다.

주요 경고와 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 신규 적응증에 대한 임상시험과 직접 관련 문헌이 없고, 근거 수준은 L5(모델 예측만 있음)입니다. 또한 질환 기전이 보체와 무관해 보이며 감염 위험이 커질 수 있어, 현 시점에서는 재창출을 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 확인: 식약처 첨부문서 내용의 수집·분석
- 작용 기전(MOA) 데이터 보강
- 주기성 호중구감소증에서 보체 C5 억제의 기전적 연관성을 보여주는 전임상 또는 문헌 근거
- 호중구감소 환자에서의 감염 위험 평가와 안전성 모니터링 계획
- 예측 순위 1위 외 다른 후보 질환에 대해서도 직접 근거 탐색
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

