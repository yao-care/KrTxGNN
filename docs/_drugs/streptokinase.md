---
layout: default
title: Streptokinase
parent: 높은 근거 (L1-L2)
nav_order: 703
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Streptokinase: 예측 신규 적응증 심근경색 (Myocardial Infarction) (근거 수준 L1). 기존 적응증: 허가 적응증 본문이 데이터에 포함되어 있지 않음(허가증 PDF 링크만 제공됨)"
---

# Streptokinase
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

# Streptokinase: 혈전 용해제에서 심근경색으로

## 한 문장 요약

Streptokinase는 플라스미노겐을 활성화하여 혈전을 용해하는 혈전용해제로, 한국에서 7건의 허가증이 유효한 상태입니다(모두 수출용 허가).
TxGNN 모델은 **심근경색(myocardial infarction)**에 효과가 있을 것으로 예측하며, 현재 **7건의 임상시험**과 **20편의 문헌**이 이 방향을 다루고 있습니다.
다만 심근경색은 이 약의 표준적인 사용 분야로 진정한 의미의 재창출이라기보다 기존 용도를 재확인한 예측에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 포함되어 있지 않음(허가증 PDF 링크만 제공됨) |
| 예측 신규 적응증 | 심근경색 (Myocardial Infarction) |
| TxGNN 예측 점수 | 99.83% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 7건 |
| 권장 결정 | Proceed with Guardrails |

> 참고: 근거 수준 L1은 완료된 Phase 3 시험이 2건 이상이라는 기준에 따른 판정입니다. 다만 해당 시험 중 일부는 streptokinase 자체가 아닌 다른 혈전용해제(테넥테플라제, 재조합 스타필로키나제)를 다루고 있어 해석에 주의가 필요합니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Streptokinase는 플라스미노겐과 복합체를 형성하여 플라스미노겐을 플라스민으로 전환하고, 플라스민이 피브린 혈전을 분해하여 관상동맥 폐색을 해소하고 혈류를 회복시킵니다.

급성 심근경색은 관상동맥 내 피브린이 풍부한 혈전에 의한 폐색이 핵심 병태이므로, 혈전용해 기전이 그대로 적용됩니다. 이는 신규 용도라기보다 표준적인 혈전용해 사용에 해당합니다.

주의할 점은 출혈 위험, 항스트렙토키나제 항체 및 이전 노출 이력(알레르기 반응, 효능 저하), 그리고 피브린 선택성 약제나 일차 PCI(경피적 관상동맥 중재술)가 선호되는 현재 진료 환경입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00000507](https://clinicaltrials.gov/study/NCT00000507) | Phase 3 | 완료 | 미보고 | 급성 경색 초기 정맥 내 streptokinase가 심근 손상을 줄이는지 평가 |
| [NCT00000503](https://clinicaltrials.gov/study/NCT00000503) | Phase 3 | 완료 | 미보고 | 비수술적 관상동맥 재관류가 경색 크기에 미치는 영향 평가 |
| [NCT01305226](https://clinicaltrials.gov/study/NCT01305226) | Phase 3 | 완료 | 120 | 급성 심근경색에서 재조합 스타필로키나제(THR-100) vs streptokinase 비교 |
| [NCT02182011](https://clinicaltrials.gov/study/NCT02182011) | Phase 3 | 완료 | 49 | 급성 심근경색에서 TNK-tPA, rt-PA, streptokinase의 응고촉진 효과(TAT) 비교 |
| [NCT00627809](https://clinicaltrials.gov/study/NCT00627809) | Phase 4 | 완료 | 53 | ST 상승 심근경색에서 일차 PCI에 관상동맥 내 저용량 streptokinase 병용 시 경색 크기·좌심실 용적 평가 |
| [NCT03677466](https://clinicaltrials.gov/study/NCT03677466) | 해당 없음 | 완료 | 60 | 일차 STEMI에서 재관류 전략별 심근 내 출혈 빈도 평가(간접 관련) |
| [NCT02893280](https://clinicaltrials.gov/study/NCT02893280) | 해당 없음 | 철회 | 0 | 스리랑카 급성 관상동맥 증후군 감사 프로젝트(근거 없음) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8130384](https://pubmed.ncbi.nlm.nih.gov/8130384/) | 1994 | Review | Drugs & Aging | 대규모 무작위 시험(ISIS-2 등)에서 고령 환자의 심근경색 후 정맥 내 streptokinase의 생존 이득 확인 |
| [2191849](https://pubmed.ncbi.nlm.nih.gov/2191849/) | 1990 | Review | Drugs | GISSI, ISIS-2, ISAM 등 3만 명 이상 대상 시험에서 정맥 내 streptokinase의 효과 입증 |
| [10572811](https://pubmed.ncbi.nlm.nih.gov/10572811/) | 1999 | 메타분석/Review | J Accid Emerg Med | 가속 alteplase(t-PA)와 streptokinase의 결과 비교 |
| [3312370](https://pubmed.ncbi.nlm.nih.gov/3312370/) | 1987 | Review | J Am Coll Cardiol | 관상동맥 내·정맥 내 streptokinase 무작위 시험 검토 |
| [481511](https://pubmed.ncbi.nlm.nih.gov/481511/) | 1979 | 대조 시험 | N Engl J Med | 유럽 11개 센터에서 streptokinase 24시간 주입 시 6개월 사망률 유의하게 감소 |
| [2146913](https://pubmed.ncbi.nlm.nih.gov/2146913/) | 1990 | 메타분석 | Ann Intern Med | 경색 부위(전벽/하벽)별 정맥 내 streptokinase의 조기 사망률 영향 분석 |
| [3396164](https://pubmed.ncbi.nlm.nih.gov/3396164/) | 1988 | 무작위 시험 하위 분석 | Circulation | 정맥 내 streptokinase 후 경색 관련 동맥 개통률 68.5%, 좌심실 기능 평가 |
| [10163575](https://pubmed.ncbi.nlm.nih.gov/10163575/) | 1996 | Review | PharmacoEconomics | 사망률 감소 측면에서 alteplase 등과 동등한 효능, 약물경제학적 평가 |
| [10611814](https://pubmed.ncbi.nlm.nih.gov/10611814/) | 1999 | 증례 보고 | Rev Esp Cardiol | 투여 6시간 후 발열, 간비대, 황달 발생(streptokinase 유발 황달) |
| [9339259](https://pubmed.ncbi.nlm.nih.gov/9339259/) | 1997 | Review | Arch Mal Coeur Vaiss | 항스트렙토키나제 항체 생성과 그 임상적 함의 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199904106 | 에스키나제주1,500,000IU(스트렙토키나제)(수출용) | 바이알 주사제(분말) | 허가 적응증 본문 정보 없음 |
| 199800042 | 프로키나제주사750,000IU(스트렙토키나제)(수출용) | 바이알(분말) | 허가 적응증 본문 정보 없음 |
| 199904108 | 에스키나제주250,000IU(스트렙토키나제)(수출용) | 바이알 주사제(분말) | 허가 적응증 본문 정보 없음 |
| 201502392 | 유유스트렙토키나제주1,500,000IU(수출용) | 바이알 주사제(분말) | 허가 적응증 본문 정보 없음 |
| 199904107 | 에스키나제주750,000IU(스트렙토키나제)(수출용) | 바이알 주사제(분말) | 허가 적응증 본문 정보 없음 |

7건 모두 단일 성분 제제이며 유효 상태입니다. 제품명에 "(수출용)"이 표기되어 있어 국내 유통 여부는 허가사항에서 확인이 필요합니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터에 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Abciximab, Apixaban, Betrixaban, Bivalirudin, Acalabrutinib, Avapritinib, Deferasirox, Ibritumomab tiuxetan, Tositumomab (I-131). 대부분 출혈 위험 증가와 관련된 항응고·항혈소판 계열입니다.
  - **Moderate**: Acetylsalicylic acid, Ibuprofen, Ketorolac, Celecoxib, Diclofenac(외용), Aminocaproic acid, Omega-3 지방산, Ginger, Fenfluramine, Sibutramine 등.
- **문헌에서 확인된 위험**: 출혈, 항스트렙토키나제 항체 형성에 따른 알레르기 반응·효능 저하, 간 손상(황달) 증례 보고.

경고·금기 등 허가사항 기반 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
심근경색에서 streptokinase의 정맥 내 혈전용해는 대규모 무작위 시험과 다수의 문헌으로 확립된 표준 사용입니다. 다만 일부 임상시험은 다른 혈전용해제를 다루고, 현재는 피브린 선택성 약제와 일차 PCI가 선호되며 출혈·면역원성 위험이 있어 조건부 진행이 적절합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증 본문) 확보: 현재 허가 적응증 본문과 안전성 정보가 없어 안전성 선별 단계로 진행할 수 없음
- 작용 기전 데이터 보완(DrugBank 등)
- 출혈 위험 및 항스트렙토키나제 항체·이전 노출 이력 확인 계획
- 국내 허가가 수출용이므로 국내 사용 가능성 확인
- 일차 PCI 및 피브린 선택성 약제와의 비교 위치 설정

## 기타 예측 적응증 요약

| 순위 | 예측 질환 | 예측 점수 | 근거 수준 | 권장 |
|-----|---------|---------|---------|-----|
| 2 | 변이형 협심증 (Prinzmetal angina) | 99.80% | L4 | Hold |
| 3 | 헤모글로빈병증 | 99.76% | L5 | Hold |
| 4 | 관상동맥 혈전증 | 99.71% | L1 | Proceed with Guardrails |
| 5 | 중격 심근경색 | 99.71% | L3 | Research Question |
| 6 | 후하벽 심근경색 | 99.71% | L4 | Hold |
| 7 | 후측벽 심근경색 | 99.71% | L4 | Hold |
| 8 | 말초혈관질환 | 99.65% | L3 | Research Question |
| 9 | 말초동맥질환 | 99.60% | L3 | Research Question |
| 10 | 16번 염색체 단완 부분 결실 | 99.56% | L5 | Hold |

관상동맥 혈전증의 L1 판정은 인공판막 혈전증 Phase 3 시험에 근거하므로 관상동맥 질환과는 간접적인 관련입니다. 변이형 협심증은 혈관연축이 주 병태여서 혈전용해의 기전적 근거가 약하고, 헤모글로빈병증과 염색체 결실은 임상 근거가 없어 모델 예측만 존재합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

