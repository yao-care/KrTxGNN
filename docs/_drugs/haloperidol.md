---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: 조현병(원 적응증)의 근거 재확인

## 한 문장 요약

Haloperidol은 D2 도파민 수용체를 강력하게 차단하는 1세대 항정신병약물로, 원래부터 조현병(schizophrenia) 치료의 표준 약제입니다.
TxGNN 모델도 동일하게 **조현병**을 최상위(1순위, 예측 점수 99.96%)로 예측했지만, 이는 신규 재창출이라기보다 **약물의 핵심/원 적응증을 모델이 재확인**한 결과이며, 이번 Evidence Pack에서는 해당 항목에 연결된 임상시험·문헌 데이터가 수집되지 않았습니다. 반면 2순위 schizophreniform disorder(20편 문헌)와 8순위 psychotic disorder(임상시험 50건, 문헌 20편)는 실제 근거가 두텁게 뒷받침되고 있어 검토 가치가 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 미기재 (약물 자체가 조현병 등 정신병적 장애의 표준 치료제로 알려져 있으나, 본 Evidence Pack의 `original_indications` 필드는 비어 있음) |
| 예측 신규 적응증 | 조현병 (Schizophrenia) — 단, 아래 설명대로 원 적응증의 재확인 성격 |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L1 (Evidence Pack 제공값 기준) — 단, 이번 데이터 수집에서는 해당 적응증에 연결된 임상시험·문헌 0건, 수집 한계로 판단됨 |
| 한국 시판 현황 | 미상장 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용기전(MOA) 데이터는 확보되지 않았습니다(Data Gap). 다만 예측 근거(rationale) 텍스트에 따르면, Haloperidol은 강력한 D2 도파민 수용체 길항작용을 통해 중뇌변연계 도파민 전달을 억제하여 조현병의 양성 증상(환각, 망상)을 완화하는 1세대 항정신병약물입니다.

여기서 중요한 점은, 이 예측이 "새로운" 적응증 발굴이 아니라 **약물의 핵심/원 적응증 자체를 모델이 다시 짚어낸 것**이라는 점입니다. 근거 텍스트도 "非典型意義上的「再利用」"(전형적 의미의 재창출이 아님)이라고 명시하고 있습니다. 실질적인 재창출 신호는 오히려 하위 순위 항목에서 나타납니다 — schizophreniform disorder(2순위)는 조현병과 병리기전(도파민 과활성)이 높은 유사성을 보이며, psychotic disorder(8순위)는 급성 정신병적 초조·공격행동 관리에 D2 길항제가 표준적으로 사용된다는 임상적 정합성을 갖고 있습니다.

---

## 임상시험 근거

predicted_indications[0](조현병)에는 등록된 임상시험 데이터가 없습니다.

현재 관련 임상시험 등록이 없습니다.

> 참고: 동일 Evidence Pack 내 8순위 "psychotic disorder" 항목에는 NCT01052389(Phase 4, GiSAS 장기치료 비교), NCT00485901(Phase 3, IM Olanzapine vs IM Haloperidol) 등 50건의 관련 임상시험이 확인되며, 조현병에 대한 haloperidol의 확립된 근거는 이 인접 적응증 데이터를 통해 간접적으로 뒷받침됩니다.

---

## 문헌 근거

predicted_indications[0](조현병)에는 연결된 문헌 데이터가 없습니다.

현재 관련 문헌이 없습니다.

> 참고: 2순위 "schizophreniform disorder"에는 PMID 11823268(RCT, Clozapine/Olanzapine/Risperidone/Haloperidol 비교), PMID 11476119(RCT, Risperidone vs Haloperidol) 등 20편의 문헌이 확인되며, 조현병 스펙트럼 질환 전반에 대한 haloperidol의 임상적 위치를 뒷받침합니다.

---

## 한국 시판 정보

현재 한국 내 허가 정보가 없습니다 (시판 현황: 미상장, 허가증 수: 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> DG001(Blocking): 허가사항 경고·금기 정보 미확보로 S1 안전성 초기평가 진입이 불가능한 상태입니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 한국 내 미상장·허가증 0건 상태로 국내 규제 경로가 확인되지 않았습니다.
- DG001(Blocking)로 분류된 허가사항 경고/금기 자료 부재로 안전성 초기평가(S1)에 진입할 수 없습니다.
- 1순위 예측(조현병)은 신규 재창출 신호가 아니라 원 적응증의 재확인 성격으로, 이 항목 단독으로는 재창출 프로젝트로서의 증분 가치가 제한적입니다. 실질적 검토 가치는 근거가 축적된 schizophreniform disorder(L2)와 psychotic disorder(L1, 임상시험 50건)에 있습니다.

**진행하려면 필요한 것:**
- TFDA/한국 허가사항 원문(경고, 금기, DDI) 확보
- DrugBank 등에서 상세 작용기전(MOA) 데이터 보완
- 한국 내 시판·허가 현황 재확인
- schizophreniform disorder 및 psychotic disorder를 대상으로 한 별도 평가 트랙 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

