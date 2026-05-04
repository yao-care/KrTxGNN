---
layout: default
title: Dexibuprofen
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Dexibuprofen
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

# Dexibuprofen: 염증성 통증에서 골관절염으로

## 한 문장 요약

Dexibuprofen은 이부프로펜의 활성 S(+) 거울상이성질체인 NSAID로, 류마티스 관절염·급성 통증·원발성 생리통 등에 사용되어 온 약물이지만 현재 한국에는 미등록 상태입니다. TxGNN 모델은 **골관절염(Osteoarthritis)**에 효과가 있을 수 있다고 예측하며, 현재 **2건의 임상시험**과 **11편의 문헌**(복수의 RCT 포함)이 이 방향을 강력하게 지지합니다. 해당 적응증에 대한 근거 수준은 **L1**로 평가됩니다.

> **선정 근거 안내**: TxGNN Rank 1 예측(osteoarthritis susceptibility, 99.95%)은 실제 치료 가능 표현형이 아닌 유전적 위험 표현형으로, 근거 수준 L5 / Hold 판정. 본 보고서는 임상적으로 가장 유의미한 **Rank 3 골관절염(L1, Proceed with Guardrails)**을 중심으로 기술합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미등록 (류마티스 관절염·급성 통증·생리통에 사용되는 NSAID) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미등록 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Dexibuprofen은 이부프로펜의 S(+) 광학이성질체로, COX-1 및 COX-2를 비선택적으로 억제함으로써 아라키돈산으로부터 PGE₂·TXA₂의 생성을 감소시켜 항염·진통 효과를 발휘합니다. 라세미체인 이부프로펜과 달리 비활성 R(-) 이성질체를 포함하지 않으므로, 이론상 동등한 효과를 더 낮은 용량으로 달성하면서 위장관 부담을 줄일 수 있다는 약동학적 이점이 있습니다. 브랜드명 Seractil로 유럽 시장에서 판매된 이력이 있습니다.

골관절염의 핵심 병리는 관절 연골의 퇴행성 분해로 인한 활막 염증과 COX-2 유도성 PGE₂가 매개하는 통증 신호 증폭입니다. 이는 NSAID가 직접 작용할 수 있는 표적 기전과 정확히 일치하며, COX 억제 계열 약물은 골관절염 통증 관리의 1차 약물 중 하나로 이미 광범위하게 사용됩니다. TxGNN의 예측이 기존 약리 기전 및 L1 수준의 임상 근거와 일치한다는 점에서 이번 예측의 신뢰도는 높습니다.

한국에서 Dexibuprofen은 현재 미등록이지만, 동일 COX 억제 기전을 공유하는 이부프로펜은 한국 내 허가·시판 중입니다. 오스트리아를 포함한 유럽 시장에서 고관절·무릎 골관절염 환자를 대상으로 한 Phase 4 완료 RCT(482명)가 이미 존재하므로, 한국 MFDS 진입 시 외국 임상시험 자료 활용(브리징 전략)을 통한 효율적 허가 접근이 가능할 것으로 판단됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01066676](https://clinicaltrials.gov/study/NCT01066676) | Phase 4 | 완료 | 482 | 고관절·무릎 골관절염 환자에서 Dexibuprofen Gebro 400mg 경구 현탁액 vs Ibuprofen 400mg의 내약성·안전성·효능 비교; 비열등성 설계 |
| [NCT01638962](https://clinicaltrials.gov/study/NCT01638962) | N/A | 완료 | 93 | 경증~중등도 무릎 골관절염에서 신경근육 운동 지도 vs 진통제 사용 지도의 관절 부하 비교; Dexibuprofen이 대조 약물로 활용됨 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24740137](https://pubmed.ncbi.nlm.nih.gov/24740137/) | 2014 | RCT | Wiener klinische Wochenschrift | 고관절·무릎 OA 489명에서 Dexibuprofen vs Ibuprofen 경구 현탁액의 안전성·내약성 비열등성 확인 (14일 치료) |
| [12708604](https://pubmed.ncbi.nlm.nih.gov/12708604/) | 2003 | RCT | Int J Clin Pharmacol Ther | 고관절 OA에서 Dexibuprofen vs Celecoxib 효능·내약성 직접 비교 |
| [10667832](https://pubmed.ncbi.nlm.nih.gov/10667832/) | 2000 | RCT | Int J Clin Pharmacol Ther | 고관절 OA에서 Dexibuprofen 용량-반응 연구 (WOMAC 골관절염 지수 활용, vs 라세미체 이부프로펜) |
| [11771571](https://pubmed.ncbi.nlm.nih.gov/11771571/) | 2001 | RCT / 장기연장 | Clinical Rheumatology | 고관절 OA 178명에서 Dexibuprofen 600/1200mg vs Ibuprofen 2400mg 동등 효능 확인; 류마티스 질환 1년 장기 내약성 연구 병행 |
| [9123945](https://pubmed.ncbi.nlm.nih.gov/9123945/) | 1997 | RCT | Wiener klinische Wochenschrift | 무릎 골관절염(Gonarthrosis) 110명에서 Dexibuprofen 900mg vs Diclofenac 150mg 이중맹검 동등성 시험; Lequesne 기능 지수 개선 동등 |
| [9013382](https://pubmed.ncbi.nlm.nih.gov/9013382/) | 1996 | Systematic Review | J Clin Pharmacol | 골관절염·RA·강직성 척추염 포함 이중맹검 RCT 재평가; Mann-Whitney 통계 활용 다질환 종합 분석 |
| [11771569](https://pubmed.ncbi.nlm.nih.gov/11771569/) | 2001 | Clinical Overview | Clinical Rheumatology | GCP 기준 8건 임상시험(1,463명), 메타분석 5건 포함 종합 임상 데이터 리뷰; OA 포함 다적응증 검토 |
| [37529187](https://pubmed.ncbi.nlm.nih.gov/37529187/) | 2023 | ML 예측 연구 | Clinics in Orthopedic Surgery | 한국 OA 환자 대상 NSAID 유발 위궤양 예측 모델 개발 (한국 코호트 기반 안전성 참고 자료) |
| [20361843](https://pubmed.ncbi.nlm.nih.gov/20361843/) | 2010 | 관찰적 안전성 연구 | Rev Esp Enferm Dig | 캡슐 내시경으로 평가한 만성 NSAID 사용 시 소장 점막 손상 빈도·중증도 (NSAID 계열 안전성 참고) |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Review | Crit Rev Ther Drug Carrier Syst | OA·RA 등 관절염에서 NSAID 미세캡슐 약물 전달 시스템 검토; Dexibuprofen 포함 |

---

## 한국 시판 정보

Dexibuprofen은 현재 한국에 등록된 허가증이 없으며 시판되지 않습니다. 동일 약리 계열(이부프로펜 계열 NSAID)인 이부프로펜 및 관련 제제는 한국 내 정식 허가·시판 중입니다.

---

## 안전성 고려사항

한국 허가 기반 안전성 데이터(경고·금기·약물 상호작용)가 수집되지 않았습니다. 안전성 정보는 Dexibuprofen 제품 허가사항(유럽 Seractil 또는 Dexibuprofen Gebro 제품 정보)을 참조하세요.

NSAID 계열 공통 위험으로는 위장관 출혈·궤양, 심혈관계 위험 증가, 신기능 저하, NSAIDs 과민반응 등이 알려져 있습니다. 한국 코호트(PMID 37529187) 데이터에 따르면 OA 환자의 NSAID 사용 시 위궤양 위험을 사전에 평가하는 것이 권고됩니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
골관절염에 대해 Dexibuprofen의 효능·안전성을 직접 평가한 Phase 4 완료 RCT(482명)와 복수의 이중맹검 RCT가 이미 존재하며, L1 수준의 근거가 재창출 타당성을 강하게 뒷받침합니다. 다만 한국 시장에서 규제 데이터가 전무하여 허가 진입 전 별도의 브리징 전략이 필요합니다.

**진행하려면 필요한 것:**
- MFDS 제출용 브리징 데이터 계획 수립 (기존 유럽 Phase 4 RCT 자료 활용 가능성 법적·규제 검토)
- 상세 안전성 정보 확보: TFDA/MFDS 기준 경고·금기·약물상호작용 데이터
- Dexibuprofen 공식 작용기전(MOA) 데이터 보완 (DrugBank API 조회)
- 한국 OA 환자 대상 위장관 안전성 모니터링 계획 수립 (한국 코호트 특성 반영)
- 이부프로펜 대비 임상적 차별화 포지셔닝 근거 정리 (S(+) 순수 이성질체의 GI 이점)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

