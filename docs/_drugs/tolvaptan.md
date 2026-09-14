---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 686
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: 적응증 미상에서 다낭성 신장질환(PKD3)으로

## 한 문장 요약

Tolvaptan(DB06212)은 원 적응증 정보가 확보되지 않은 상태이나, TxGNN 모델은 **다낭성 신장질환 3형(폴리시스틱 간질환 동반 여부 무관, PKD3)**에 효과가 있을 것으로 예측합니다. 현재 등록된 임상시험은 없지만, **20편의 문헌** 중 2건의 대형 Phase 3 RCT(TEMPO 3:4, REPRISE)를 포함한 다수의 근거가 이 방향을 강하게 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (원 적응증 미기재) |
| 예측 신규 적응증 | 다낭성 신장질환 3형, 폴리시스틱 간질환 동반 여부 무관 (PKD3) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

공식 MOA(작용 기전) 데이터는 확보되지 않았으나(DrugBank 조회 필요, High severity 데이터 갭), 근거 팩에 포함된 기전 분석에 따르면 Tolvaptan은 **바소프레신 V2 수용체 길항제**로, 신장 집합관에서 cAMP 생성을 억제하여 낭종 증식과 신장 용적 증가를 늦추는 것으로 알려져 있습니다.

이 기전은 다낭성 신장질환(ADPKD/PKD)의 병태생리와 직접적으로 연관되며, 실제로 두 건의 대형 Phase 3 RCT(TEMPO 3:4, REPRISE)가 일반 ADPKD 환자군에서 Tolvaptan의 신기능 보호 효과를 입증했습니다.

다만 예측된 적응증은 **PKD3**라는 특정 유전형 아형을 명시하고 있어, 기존 RCT들이 일반 ADPKD(주로 PKD1/PKD2)를 대상으로 했는지, PKD3 아형을 포함했는지에 대한 별도 확인이 필요합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (Phase 3, TEMPO 3:4) | NEJM | ADPKD 환자에서 Tolvaptan이 총 신장 용적 증가와 신기능 저하를 유의하게 감소시킴 |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (Phase 3, REPRISE) | NEJM | 후기 단계 ADPKD 환자에서도 Tolvaptan이 eGFR 감소를 유의하게 늦춤 |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT (소아, NCT02964273) | Pediatr Nephrol | 소아 ADPKD 환자 대상 Tolvaptan 안전성·약력학 평가 및 급속 진행 위험군 기저특성 분석 |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | 체계적 문헌고찰/메타분석 | Nefrologia | ADPKD에서 Tolvaptan의 유효성과 안전성을 종합 평가 |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Cochrane 체계적 문헌고찰 | Cochrane Database Syst Rev | ADPKD 진행 예방을 위한 중재법(Tolvaptan 포함) 비교 평가 |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | 합의문/리뷰 | Nephrol Dial Transplant | ERA 등 국제 학회의 ADPKD에서의 Tolvaptan 사용 최신 합의 권고안 |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD의 전반적 개요 및 치료 동향(Tolvaptan 포함) 리뷰 |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | 진료지침 (EASL) | J Hepatol | 낭성 간질환(다낭성 간질환 포함) 관리에 대한 EASL 임상진료지침 |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | ADPKD와 다낭성 간질환(PCLD)의 임상 경과 및 Tolvaptan의 역할 리뷰 |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Review | Curr Opin Nephrol Hypertens | ADPKD에서 Tolvaptan 이후의 신규 치료제 파이프라인 리뷰 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
두 건의 대형 Phase 3 RCT(TEMPO 3:4, REPRISE)가 일반 ADPKD에서 Tolvaptan의 유효성을 입증했고, 다수의 국제 가이드라인·합의문이 이를 뒷받침하여 근거 수준은 L1입니다. 다만 예측 적응증이 특정 유전형(PKD3)을 명시하고 있어 기존 RCT가 이 아형을 포함했는지 추가 확인이 필요하며, 안전성 자료 확보 전까지는 신중한 진행이 요구됩니다.

**진행하려면 필요한 것:**
- 허가사항(경고/금기/DDI) 자료 확보 — 현재 Blocking 데이터 갭으로 S1 안전성 초기평가 불가
- 공식 작용기전(MOA) 자료 확보 (DrugBank API 조회)
- PKD3 특이 유전형에 대한 하위군 분석 자료 확인
- 한국 내 허가/시판 계획 수립 (현재 미출시, 허가증 0건)

*참고: 예측 순위 2~10위 후보(신장-간-췌장 이형성증, 카리오메갈릭 간질성신염, 흉곽기형 등)는 근거 수준 L4~L5로 문헌·임상 근거가 매우 부족하거나 관련성이 낮아(예: 9위는 치주질환 문헌과의 키워드 오매칭) 모두 Hold로 평가되었습니다.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

