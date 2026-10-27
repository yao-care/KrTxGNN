---
layout: default
title: Nabumetone
parent: 모델 예측만 (L5)
nav_order: 533
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nabumetone: 예측 신규 적응증 골관절염 감수성 (osteoarthritis susceptibility) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 허가증 링크로만 제공되어 텍스트 확인 불가. 문헌상 골관절염·류마티스 관절염의 증상 치료"
monitor_inn: "Nabumetone"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome"]
---

# Nabumetone
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

## Nabumetone: 골관절염·류마티스 관절염 치료제에서 골관절염 감수성으로
{: .text-alpha }

## 한 문장 요약

Nabumetone은 활성 대사체 6-MNA를 통해 COX를 억제하는 비스테로이드성 소염진통제(NSAID) 전구약물로, 골관절염과 류마티스 관절염의 증상 치료에 사용되어 왔습니다.
TxGNN 모델은 **골관절염 감수성(osteoarthritis susceptibility)**에 효과가 있을 것으로 최상위 예측했지만(99.999%), 이 항목을 직접 지지하는 **임상시험과 문헌은 0건**입니다.
같은 예측 목록의 **골관절염(osteoarthritis)** 항목에는 임상시험 2건과 문헌 19편이 있어, 실제 검토 대상은 이쪽입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 허가증 링크로만 제공되어 텍스트 확인 불가. 문헌상 골관절염·류마티스 관절염의 증상 치료 |
| 예측 신규 적응증 | 골관절염 감수성 (osteoarthritis susceptibility) |
| TxGNN 예측 점수 | 99.999% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

> **참고:** 예측 목록 3위인 골관절염은 근거 수준 L2, 권장 결정 Proceed with Guardrails입니다. 다만 이는 이미 확립된 증상 치료 적응증이어서 진정한 의미의 재창출 신호는 아닙니다.

## 이 예측이 타당한 이유는?

현재 DrugBank 기반의 상세 작용 기전 데이터는 없습니다. 문헌에 따르면 nabumetone 자체는 비산성 전구약물이며, 흡수 후 간 초회통과 대사로 활성 대사체 6-MNA(6-methoxy-2-naphthylacetic acid)가 됩니다. 6-MNA는 COX-2를 우선적으로 억제하며 소염·진통 작용을 나타냅니다.

그러나 "골관절염 감수성"은 치료할 수 있는 임상 상태가 아니라 골관절염에 걸리기 쉬운 유전적 소인을 가리키는 용어입니다. nabumetone은 골관절염의 통증과 염증 증상을 완화할 뿐 감수성을 바꾸지 않으므로, 이 항목의 높은 점수는 지식 그래프에서 골관절염과 가까운 위치에 있는 데서 나온 결과로 보는 것이 합리적입니다.

임상적으로 의미 있는 해석은 골관절염 자체에 대한 프로스타글란딘 매개 통증·염증 억제입니다. 이 해석은 아래 근거로 뒷받침됩니다.

## 임상시험 근거

골관절염 감수성 항목에는 등록된 임상시험이 없습니다. 아래는 임상적으로 해석 가능한 **골관절염** 항목의 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02049606](https://clinicaltrials.gov/study/NCT02049606) | Phase 4 | 완료 | 134 | 무릎 골관절염 환자에서 LAYLA 정과 CENATONE 정의 유효성·안전성을 비교한 이중맹검, 무작위, 활성대조, 다기관 시험 |
| [NCT01638962](https://clinicaltrials.gov/study/NCT01638962) | 해당 없음 | 완료 | 93 | 경증~중등도 무릎 골관절염에서 진통제 사용 교육과 신경근 운동이 무릎 관절 부하에 미치는 영향을 비교. nabumetone이 주된 중재가 아니어서 간접적 근거 |

## 문헌 근거

골관절염 감수성 항목에 연결된 문헌은 없습니다. 아래는 **골관절염** 항목의 주요 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8587082](https://pubmed.ncbi.nlm.nih.gov/8587082/) | 1995 | RCT | J Rheumatol | 고관절·무릎·어깨 원발성 골관절염에서 nabumetone과 diclofenac SR의 유효성·안전성을 비교한 캐나다 다기관 시험 |
| [15086644](https://pubmed.ncbi.nlm.nih.gov/15086644/) | 2004 | RCT | J Am Geriatr Soc | 무릎 골관절염에서 rofecoxib 12.5 mg과 nabumetone 1,000 mg의 유효성·안전성 비교 |
| [9377610](https://pubmed.ncbi.nlm.nih.gov/9377610/) | 1997 | 무작위 이중맹검 시험 | Clin Ther | 무릎 골관절염 279명에서 Naprelan 1,000 mg과 nabumetone 1,500 mg을 4주간 비교 |
| [8851458](https://pubmed.ncbi.nlm.nih.gov/8851458/) | 1996 | 무작위 이중맹검 시험 | Clin Ther | 무릎 골관절염 347명에서 oxaprozin, nabumetone 1,500 mg, 위약을 6주간 비교 |
| [11770835](https://pubmed.ncbi.nlm.nih.gov/11770835/) | 2001 | 비교 임상시험 | Int J Clin Pharmacol Ther | 무릎 골관절염에서 naproxen CR 1,000 mg과 nabumetone 1,000 mg의 유효성·안전성 비교 |
| [10759624](https://pubmed.ncbi.nlm.nih.gov/10759624/) | 2000 | 리뷰/안전성 분석 | Aliment Pharmacol Ther | nabumetone과 diclofenac SR, piroxicam의 유효성 및 위장관 안전성 비교 |
| [20387351](https://pubmed.ncbi.nlm.nih.gov/20387351/) | 2009 | 비교 임상연구 | JNMA | 골관절염에서 aceclofenac과 nabumetone의 유효성 및 위장관 내약성 비교 |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Review | Drugs | 골관절염·류마티스 관절염에서 nabumetone의 치료적 사용과 안전성 프로필 |
| [10841070](https://pubmed.ncbi.nlm.nih.gov/10841070/) | 2000 | Review | Drugs | nabumetone의 약리·대사 특성. 다른 NSAID와 유사한 효능이며 6-MNA가 COX-2를 우선 억제 |
| [8356999](https://pubmed.ncbi.nlm.nih.gov/8356999/) | 1993 | 비교 효능 연구 | Am J Med | 골관절염·류마티스 관절염에서 nabumetone과 diclofenac, naproxen, ibuprofen, piroxicam을 비교한 무작위 공개 다기관 시험 |

## 한국 시판 정보

허가 적응증 원문은 텍스트가 아닌 허가증 링크로만 제공되어, 해당 링크에서 확인해야 합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201908446 | 나부민정(수출용) | 필름코팅정 | [허가증 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201908446/EE) 참조 |
| 200404646 | 나메톤정 | 필름코팅정 | [허가증 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200404646/EE) 참조 |
| 199200885 | 한독렐라펜정 | 제피정 | [허가증 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199200885/EE) 참조 |
| 200403776 | 코러스나부메톤정 | 필름코팅정 | [허가증 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200403776/EE) 참조 |
| 200411208 | 이텍스나부메톤정500mg | 필름코팅정 | [허가증 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200411208/EE) 참조 |

이 외에도 15건이 유효하며, 총 20건 모두 단일제이고 취소된 허가는 없습니다.

## 안전성 고려사항

허가사항의 경고·금기 정보는 이번 보고서에 반영되지 않았으므로 허가사항을 직접 확인해야 합니다.

- **약물 상호작용:** 데이터베이스에서 총 100건이 확인되었고, 아래는 상위 조회분 20건 중 주요 항목입니다.
  - **중등도:** hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide(코르티코스테로이드), acetylsalicylic acid, metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, vancomycin, potassium citrate, potassium bicarbonate, picosulfuric acid, sodium sulfate, polyethylene glycol(전해질 포함)
  - **경미:** ranitidine, cimetidine, linaclotide
- **NSAID 계열 일반 주의(문헌 근거):** 위장관, 신장, 심혈관 위험을 모니터링해야 합니다. 상호작용 건수가 많아 병용약 검토가 필요합니다.

## 결론 및 다음 단계

**결정: Hold** (골관절염 감수성 항목 기준)

**사유:**
골관절염 감수성은 유전적 소인을 가리키는 용어로 치료 대상이 될 수 없고, nabumetone의 COX 억제 기전과도 맞지 않으며, 지지하는 임상시험이나 문헌이 없습니다. 반면 골관절염(L2, Proceed with Guardrails)과 류마티스 관절염(L4, Research Question)은 이미 확립된 증상 치료 용도여서 신규 재창출 근거로 보기 어렵습니다.

**진행하려면 필요한 것:**
- 허가증 원문에서 허가 적응증, 경고, 금기 확인 (현재 안전성 검토를 진행할 수 없는 차단 수준의 공백)
- 상세 작용 기전 데이터 확보 (DrugBank 등)
- 재창출 목적이라면 "감수성" 대신 구체적인 임상 상태나 아형을 지정해 평가 대상을 재정의
- 골관절염 용도로 진행 시 위장관·신장·심혈관 모니터링 계획과 병용약(특히 코르티코스테로이드, 아스피린, 당뇨병약) 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

