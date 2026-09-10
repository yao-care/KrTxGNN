---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: 고콜레스테롤혈증에서 저칼륨혈증(Potassium Deficiency Disease)으로

## 한 문장 요약

Inclisiran은 PCSK9 mRNA를 표적하는 siRNA 약물로, 원래 고콜레스테롤혈증·죽상경화성 심혈관질환에서 LDL-C를 낮추는 데 사용됩니다(한국 미시판, 상세 작용기전 자료는 아직 확보되지 않음). TxGNN 모델은 **저칼륨혈증(Potassium Deficiency Disease)**에 효과가 있을 수 있다고 예측했지만, 현재 이를 뒷받침하는 **임상시험 0건, 문헌 0편**으로 순수 모델 출력에 불과합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고콜레스테롤혈증 / 죽상경화성 심혈관질환 (LDL-C 저하) — 한국 미시판, 상세 MOA 자료 없음 |
| 예측 신규 적응증 | 저칼륨혈증 (Potassium Deficiency Disease) |
| TxGNN 예측 점수 | 99.93% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Inclisiran은 PCSK9(mRNA) 억제를 통해 LDL-C를 낮추는 siRNA 약물이며, 이 경로는 저칼륨혈증과 같은 전해질 대사 질환과 알려진 생리학적 연관성이 없습니다.

Evidence Pack 내 자체 평가에서도 이 예측을 "PCSK9 抑制與鉀離子代謝無已知生理連結, 判斷為知識圖譜雜訊(noise node)"로 명시하고 있습니다. 즉 TxGNN의 고득점(99.93%)은 지식그래프 상의 노드 근접성에서 비롯된 수치일 뿐, 실제 약리학적 타당성을 뒷받침하는 임상시험이나 문헌은 전혀 확보되지 않았습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 신규 적응증(저칼륨혈증)에 대해 임상시험·문헌 근거가 전무하며, 평가 자료 자체가 이를 지식그래프 잡음(noise node)으로 판정했습니다. 또한 원 약물의 MOA 및 한국 허가사항(경고·금기)이 모두 확보되지 않아 안전성 초기 평가(S1) 단계에도 진입할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- Inclisiran의 상세 작용기전(MOA) 데이터 (DrugBank API 재조회)
- 한국 허가사항(경고/금기) 확보 — 현재 Blocking 데이터 갭
- 저칼륨혈증 적응증에 대한 최소 전임상/기전 연구 확보 (현재 L5 → L4 이상 필요)

---

**참고**: 동일 Evidence Pack 내 다른 예측 후보 중 "aortic malformation"(rank 8, L4·S1)에는 관련 임상시험 2건이 존재하나, 시험 설계상 가족성 고콜레스테롤혈증(FH) 대상 연구로 의심되어 질병 라벨링 오류 가능성이 지적되고 있습니다. 재평가 시 함께 검토를 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

