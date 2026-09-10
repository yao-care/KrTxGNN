---
layout: default
title: Cefazedone
parent: 僅模型預測 (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Cefazedone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cefazedone: 세균 감염에서 골관절염(Osteoarthritis)으로

## 한 문장 요약

Cefazedone(DrugBank DB13778)은 세포벽 합성을 억제하는 세팔로스포린(cephalosporin)계 항생제로 분류되는 성분이며, 한국에는 허가된 제품이 없습니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에 효과가 있을 수 있다고 예측(점수 98.47%)했지만, 현재 이를 뒷받침하는 임상시험·문헌·ICTRP 등록은 **전무**하며, 모델 예측 외의 근거는 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미출시, 원 적응증 정보 미확인) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 98.47% |
| 근거 수준 | L5 (모델 예측만 존재, 실제 연구 없음) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 공식 작용기전(MOA) 데이터는 확보되지 않은 상태입니다(Blocking 데이터 갭). 다만 알려진 정보에 따르면 Cefazedone은 세팔로스포린계 항생제로, 세균의 penicillin-binding protein(PBP)에 결합해 세포벽 합성을 억제하는 방식으로 작용하는 것으로 분류됩니다.

이 항균 기전과 골관절염의 연골 퇴행·염증 기전 사이에는 알려진 연결고리가 없습니다. TxGNN 예측 근거 자체도 "항생제의 항균 기전과 골관절염의 병태생리 간에는 알려진 기전적 연관성이 없다"고 명시하고 있어, 이번 예측은 순수하게 지식그래프 패턴에 기반한 것으로 보이며 약리학적 타당성을 뒷받침할 근거는 아직 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 10개 적응증(골관절염 포함) 모두 임상시험·ICTRP·문헌 근거가 전혀 없는 순수 모델 예측(L5)이며, 약물 자체가 한국에 미출시 상태로 경고·금기·상호작용 등 안전성 자료도 확보되지 않아 초기 안전성 평가(S1) 진입이 불가능합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 원문 확보 — 현재 Blocking 데이터 갭(DG001)
- DrugBank 등을 통한 공식 작용기전(MOA) 확인 — 현재 High 데이터 갭(DG002)
- 골관절염 관련 최소 1건 이상의 전임상 또는 관찰연구 수준 근거 확보
- 위 자료 없이는 S0 단계를 벗어나지 않는 것을 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

