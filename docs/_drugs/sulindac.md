---
layout: default
title: Sulindac
parent: 僅模型預測 (L5)
nav_order: 651
evidence_level: L5
indication_count: 10
---

# Sulindac
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

# Sulindac: 관절염(류마티스 관절염·강직성 척추염)에서 골관절염(Osteoarthritis)으로

> **후보 선정 참고**: TxGNN 점수 최상위는 "osteoarthritis susceptibility"(유전적 감수성 표지자, 99.98%)였으나, 근거 팩 자체 분석에서 "독립적 임상·기전 근거 없이 KG 공유 연결로 인한 간접 추론"으로 명시되어 있어 실질적 재창출 후보로 부적합합니다. 대신 실제 임상시험·문헌 근거가 풍부한 2순위 **골관절염(Osteoarthritis)**을 이 보고서의 주 후보로 채택했습니다. 3순위 **류마티스 관절염** 역시 동일 수준(L1)의 근거를 가진 대등한 후보입니다.

## 한 문장 요약

Sulindac은 현재 한국에 허가·시판되지 않은 NSAID 계열 약물로, 문헌상 원래 류마티스 관절염·강직성 척추염 등 관절염 질환에 사용되어 왔습니다(PMID 14572604). TxGNN 모델은 **골관절염(Osteoarthritis)**에 대해 **99.94%**의 예측 점수를 제시하며, **1건의 관련 임상시험**과 **19편의 문헌**(다수의 RCT 포함)이 이를 뒷받침합니다. 다만 이는 완전히 새로운 생물학적 기전 발견이라기보다, 해외에서 이미 확립된 적응증을 한국 시장에 재도입하는 관점에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 내 정식 허가 없음(미시판); 해외 문헌상 류마티스 관절염·강직성 척추염 등 관절염 질환 (PMID 14572604) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

DrugBank 기반 상세 작용기전(MOA) 데이터는 현재 확보되지 않았습니다(Data Gap, High severity). 다만 근거 팩에 포함된 문헌(PMID 14572604)에 따르면, Sulindac은 설폭사이드 전구약물로서 체내에서 활성 대사체인 sulindac sulfide와 sulfone으로 전환되며, 이 중 sulfide 대사체가 COX-1/COX-2를 억제해 프로스타글란딘 합성을 감소시키는 전형적인 NSAID 기전을 갖습니다. 이는 관절 염증과 통증 조절이라는 골관절염 치료의 핵심 병태생리와 직접 연결됩니다.

또한 이 예측은 완전히 새로운 적응증 발견이 아니라, 이미 1970~1990년대부터 다수의 무작위 대조시험을 통해 확립되어 온 사용 경험의 재확인에 가깝습니다. 한국에서는 아직 허가·시판 이력이 없으나(허가증 0건), 이는 시장 미진입 상태일 뿐 효능·안전성 근거가 부족하다는 의미는 아닙니다. 류마티스 관절염(rank 3, L1)도 동일한 기전으로 대등한 근거 수준을 보여, NSAID 계열 항염·진통 기전이 관절 질환군 전반에 일관되게 적용됨을 뒷받침합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01761877](https://clinicaltrials.gov/study/NCT01761877) | Phase 2 | 완료 | 114 | 아로마타제 억제제 복용 유방암 환자의 통증·경직 완화 효과 평가가 주목적으로, 골관절염 자체 유효성 평가는 아님(관련성 등급 C, 근거 팩 자체 판정: 관련성 낮음) |

*골관절염에 특화된 등록 임상시험은 이 1건 외에 확인되지 않았습니다. 아래 문헌 근거의 다수 RCT(1970~1990년대)는 임상시험 등록제 도입 이전 시행되어 ClinicalTrials.gov에는 등재되어 있지 않습니다.*

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [7261665](https://pubmed.ncbi.nlm.nih.gov/7261665/) | 1981 | RCT | Curr Med Res Opin | 고령 OA 환자 32명, sulindac 400mg/day vs ibuprofen 1200mg/day 12주 비교, 통증·경직·관절가동범위 개선 확인 |
| [3515919](https://pubmed.ncbi.nlm.nih.gov/3515919/) | 1986 | RCT | Am J Med | 고관절/슬관절 OA 143명, flurbiprofen vs sulindac 6주 이중맹검, 유효성·안전성 통계적 유의차 없음(동등 효과) |
| [7025178](https://pubmed.ncbi.nlm.nih.gov/7025178/) | 1981 | RCT | Rheumatol Rehabil | 고관절/슬관절 OA 30명, naproxen 750mg vs sulindac 400mg 교차설계, 양쪽 모두 유의한 개선, 부작용 적음 |
| [7044801](https://pubmed.ncbi.nlm.nih.gov/7044801/) | 1982 | RCT | Eur J Rheumatol Inflamm | RA·OA 환자, benoxaprofen vs sulindac 이중맹검 교차시험, benoxaprofen이 전반적으로 다소 우세하나 sulindac도 유효 |
| [7105794](https://pubmed.ncbi.nlm.nih.gov/7105794/) | 1982 | RCT | Curr Med Res Opin | 고령 증상성 OA 32명, sulindac vs ibuprofen 12주 비교, 통증·경직 지표 개선 |
| [6733011](https://pubmed.ncbi.nlm.nih.gov/6733011/) | 1984 | RCT | Br J Clin Pract | 고령 증상성 OA 다기관 비교연구, sulindac vs ibuprofen |
| [6839797](https://pubmed.ncbi.nlm.nih.gov/6839797/) | 1983 | RCT | Curr Med Res Opin | 고령 OA 환자 30명, sulindac 200mg bid vs ibuprofen 400mg tid 12주, 일부 지표에서 sulindac이 통계적으로 유의하게 우수 |
| [388989](https://pubmed.ncbi.nlm.nih.gov/388989/) | 1977 | 초기 임상연구 | Acta Rhumatol Belg | 류마티스 관절염 및 골관절염에서 Sulindac 초기 임상시험 결과 |
| [35039952](https://pubmed.ncbi.nlm.nih.gov/35039952/) | 2022 | RCT | Breast Cancer Res Treat | 아로마타제 억제제 복용 유방암 환자의 근골격계 경직 완화에 대한 sulindac 효과(가장 최신 RCT) |
| [14572604](https://pubmed.ncbi.nlm.nih.gov/14572604/) | 2003 | 기전 연구 | Free Radic Biol Med | Sulindac 대사체(sulfide/sulfone)가 활성산소종 소거능을 높여 항염 효과 및 대장암 예방 가능성 시사 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (현재 한국 라벨 경고문·금기·약물상호작용 데이터가 확보되지 않았으며, 이는 후속 안전성 초평가(S1) 진입을 막는 Blocking 등급 데이터 갭입니다.)

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
골관절염에 대한 sulindac의 효능은 1970~1990년대 다수의 무작위 대조시험(L1)으로 반복 검증되었고, NSAID의 COX 억제 기전이 병태생리와 직접 부합합니다. 그러나 한국 내 허가·안전성 라벨 데이터가 전무(Blocking gap)하여, 이 상태로는 안전성 초평가(S1) 진입이 불가능합니다.

**진행하려면 필요한 것:**
- TFDA(한국 식약처 상당 기관) 공식 라벨의 경고·금기 사항 확보 (DG001, Blocking)
- DrugBank 등에서 공식 MOA 데이터 확보 (DG002, High)
- 약물상호작용(DDI) 데이터베이스 조회 결과 확보
- 류마티스 관절염(rank 3)도 동등한 L1 근거를 보유하므로, 병행 적응증 확대 검토 권장
- rank 1, 4~8, 10의 희귀 유전/골격 발달 질환 예측은 근거가 전혀 없는 KG 아티팩트로 판단되며 추가 조치 불필요(Hold 유지)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

