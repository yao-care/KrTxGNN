---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: 허가 적응증 미확인에서 하벽·후벽심근경색(Posteroinferior MI)으로

## 한 문장 요약

Lisinopril은 ACE 억제제(ACEi) 계열 약물이나, 본 Evidence Pack에는 한국 내 허가 적응증 데이터와 작용기전(MOA) 상세 정보가 확보되어 있지 않습니다.
TxGNN 모델은 **하벽·후벽심근경색(Posteroinferior Myocardial Infarction)**에 효과가 있을 수 있다고 예측하지만(예측 점수 99.90%), 이 적응증(아형)을 직접 지지하는 **임상시험이나 문헌은 현재 0건**이며, 기전적 외삽(class-level extrapolation)에 근거한 예측입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 허가 정보 미확보) |
| 예측 신규 적응증 | 하벽·후벽심근경색 (Posteroinferior Myocardial Infarction) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L4 (기전 연구 수준, 해당 적응증 임상시험/문헌 0건) |
| 한국 시판 현황 | 미시판 (허가증 0건) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터는 확보되어 있지 않습니다. 다만 Evidence Pack에 포함된 기전 근거(rationale)에 따르면, Lisinopril은 ACE 억제제(ACEi)로서 RAAS(레닌-안지오텐신-알도스테론계)를 억제하고 후부하를 낮추며 심실 재형성(remodeling)을 억제합니다. ACEi 계열은 심근경색 후 표준 이차예방 약물군으로, SAVE·GISSI-3·ISIS-4 등 고전적 대규모 임상시험을 통해 이 기전이 검증된 바 있습니다.

그러나 이는 일반적인 "심근경색 후" 적응증 수준의 기전 근거이며, "하벽·후벽심근경색"이라는 해부학적 아형(subtype)에 특화된 전용 임상시험이나 문헌은 본 데이터셋에 존재하지 않습니다. 즉 이번 예측은 약물군(class) 수준의 기전을 특정 해부학적 라벨로 외삽한 결과로 해석해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

(TFDA 수준의 경고문/금기 정보 및 약물상호작용 데이터가 확보되지 않았으며, 이는 Blocking 등급의 데이터 갭으로 분류되어 있습니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 적응증(하벽·후벽심근경색)에 특화된 임상시험·문헌 근거가 전무하며, 기전 수준의 약물군 외삽에 불과합니다.
- 허가사항(경고/금기) 데이터가 확보되지 않아 안전성 초기 평가(S1) 자체가 불가능한 상태입니다 (Blocking Data Gap).
- 한국 내 미시판 약물로 허가 트랙 정보도 없습니다.

**진행하려면 필요한 것:**
- TFDA(또는 해당 규제기관) 공식 라벨 확보 및 경고/금기 파싱
- DrugBank 등에서 상세 MOA 데이터 확보
- "하벽·후벽심근경색" 아형에 특화된 임상시험/문헌 검색 재수행

---

**참고:** 동일 Evidence Pack 내 9위 후보 **"chronic pulmonary heart disease(만성 폐성심)"**는 lisinopril을 직접 다룬 문헌 2편(Pribylov 2006, Verbitskii 2003)이 존재하여 근거 수준(L3)이 본 후보보다 높습니다. 다만 첨부된 임상시험 5건은 모두 lisinopril과 무관한 약물(vericiguat, furosemide 등)로, 인구집단 중복에 의한 오연결로 판단됩니다. 우선순위 재검토 시 참고하시기 바랍니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

