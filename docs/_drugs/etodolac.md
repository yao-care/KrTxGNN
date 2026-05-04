---
layout: default
title: Etodolac
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Etodolac
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

# Etodolac: 관절염 치료에서 골관절염으로

## 한 문장 요약

Etodolac은 COX-2 우선적 억제 NSAID(비스테로이드 항염증제)로, 미국·유럽 등 해외에서 골관절염, 류마티스 관절염, 강직성 척추염 및 통증 치료에 허가되어 있으나 한국에는 현재 미허가 상태입니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에 효과가 있을 것으로 예측하며(예측 점수 99.97%),
현재 **3건의 임상시험**과 **20편의 문헌**(다수의 완료된 RCT 포함)이 이를 강력히 지지합니다.

> **분석 참고**: TxGNN 최고 순위 예측은 '골관절염 유전적 감수성(rank 1)'이지만, 이는 이미 발병한 질환이 아닌 유전적 위험 상태로 임상 근거가 전무하여 Hold 판정을 받았습니다. 임상 근거 수준이 L1인 '골관절염(rank 3)'을 본 보고서의 주요 분석 대상으로 선정합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (해외 허가: 골관절염, 류마티스 관절염, 강직성 척추염, 통증) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

한국 허가 데이터베이스에는 Etodolac의 작용 기전 자료가 존재하지 않지만, 다수의 국제 문헌에서 기전이 명확히 확립되어 있습니다. Etodolac은 **피란노카르복실산(pyranocarboxylic acid) 계열 최초의 NSAID**로, 아라키돈산 대사 경로에서 COX-2 효소를 우선적으로 억제합니다. 이를 통해 **프로스타글란딘(특히 PGE₂) 합성을 감소**시켜 관절 내 염증과 통증을 완화합니다. COX-1 대비 COX-2 선택성이 높아 동계열 비선택적 NSAID 대비 위장관 부작용이 적은 것으로 알려져 있습니다.

골관절염의 핵심 병리는 관절 연골 손상과 만성 저등급 염증으로, COX-2가 매개하는 PGE₂가 통증 신호 전달 및 관절 내 사이토카인 연쇄반응을 증폭시킵니다. PMID 2150570을 포함한 다수의 체외 연구에서 Etodolac은 단순 증상 억제를 넘어 **연골세포 보호 효과**—기질 메탈로프로테아제(MMP) 억제 및 프로테오글리칸 합성 촉진—를 보여, 항염증과 연골 보호라는 이중 기전을 갖는 것으로 확인됩니다.

결정적으로, **Etodolac은 이미 미국 FDA, EMA 등 주요 해외 규제기관에서 골관절염 및 류마티스 관절염 치료제로 정식 허가받아 수십 년간 사용**되어 왔습니다. TxGNN 예측은 이처럼 확립된 글로벌 근거를 재확인하는 것이며, 한국 미허가는 안전성·유효성 증거 부족이 아닌 **시장 공백(market gap)**으로 판단됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT07308470](https://clinicaltrials.gov/study/NCT07308470) | Phase 2 | 모집 예정 | 30 | Etodolac 고체지질나노입자 겔(SLN 겔)을 물리치료 보조제로 적용한 무릎 OA 무작위 임상시험. Etodolac을 직접 연구 약물로 하는 OA 적응증 최신 시험으로, 새로운 약물전달 전략을 평가 |
| [NCT01638962](https://clinicaltrials.gov/study/NCT01638962) | N/A | 완료 | 93 | 경증~중등도 무릎 OA 환자에서 신경근 운동 vs 진통제(NSAID 포함) 비교 단맹검 RCT. 두 군 간 동등한 통증 완화 효과를 전제로 무릎 관절 부하 감소의 차이를 분석 |
| [NCT02180516](https://clinicaltrials.gov/study/NCT02180516) | N/A | 완료 | 9,984 | RA·OA·요통 등에서 Meloxicam과 여타 NSAID(Etodolac 포함) 간 위장관 이상반응 발생률을 비교한 대규모 실사용(real-world) 안전성 코호트 연구 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1286486](https://pubmed.ncbi.nlm.nih.gov/1286486/) | 1992 | RCT | Clinical Therapeutics | 무릎 OA 환자 172명 대상 Etodolac 600mg/일 vs Diclofenac 150mg/일 8주 이중맹검 RCT; 두 군 모두 2주 시점부터 통계적으로 유의한 통증 감소 확인 |
| [8565029](https://pubmed.ncbi.nlm.nih.gov/8565029/) | 1995 | RCT | Clinical Therapeutics | 무릎 OA 환자 254명에서 Etodolac 400mg bid vs Naproxen 500mg bid vs 위약 4주 이중맹검 무작위 연구; Etodolac과 Naproxen 모두 위약 대비 주요 효능 지표에서 유의한 개선 |
| [1828415](https://pubmed.ncbi.nlm.nih.gov/1828415/) | 1991 | RCT | Curr Med Res Opin | 무릎 OA 환자 220명에서 Etodolac 300mg bid vs Piroxicam 20mg qd 8주 이중맹검 RCT; Etodolac군에서 모든 효능 평가지표 유의한 개선(p<0.05) |
| [20639739](https://pubmed.ncbi.nlm.nih.gov/20639739/) | 2010 | RCT | The Clinical Journal of Pain | 무릎 OA 급성 악화 환자에서 Etodolac+아세트아미노펜 복합 고정용량 vs Etodolac 단독 이중맹검 무작위 비교; 복합 제형의 우월한 효능 평가 |
| [24194981](https://pubmed.ncbi.nlm.nih.gov/24194981/) | 2013 | RCT | Pain Research and Treatment | 무릎 OA 환자 60명에서 Etodolac 600mg 단독 vs Etodolac+Eperisone 병용 8주 무작위 비교; 복합요법의 효능 및 내약성 우위 평가 |
| [18405470](https://pubmed.ncbi.nlm.nih.gov/18405470/) | 2008 | 체계적 고찰 | Health Technology Assessment | Etodolac·Meloxicam·Celecoxib 등 COX-2 선택적 NSAID 7종의 OA·RA 임상효과 및 비용효과 체계적 고찰; Etodolac의 유효성과 위장관 안전성 프로파일 종합 분석 |
| [2150570](https://pubmed.ncbi.nlm.nih.gov/2150570/) | 1990 | 임상/체외 | Rheumatology International | OA에서 Etodolac의 임상 효능 및 연골세포 대사 영향 검토; 위약 대비 우월한 임상 효능 및 연골세포 프로테오글리칸 합성 보호 효과(연골 보호 가능성) 확인 |
| [7744125](https://pubmed.ncbi.nlm.nih.gov/7744125/) | 1994 | 임상시험 | Eur J Rheumatol Inflamm | OA·RA 환자에서 Etodolac 장기 치료의 효능 및 안전성; 단기 및 장기 치료 모두에서 복수의 효능 지표 유의한 개선, 비교 NSAID 대비 동등한 효능 |
| [39345034](https://pubmed.ncbi.nlm.nih.gov/39345034/) | 2024 | Review | Therapeutic Delivery | 골관절염에서 Etodolac의 활용 현황, 경구·국소 약물전달 과제, SLN 겔 등 나노치료 전략 및 병용 시너지 가능성을 다룬 최신 종합 리뷰 |
| [2528441](https://pubmed.ncbi.nlm.nih.gov/2528441/) | 1989 | 임상시험 | Curr Med Res Opin | 무릎·고관절·척추 OA 환자 57명에서 Etodolac 200mg bid 2주 개방 임상시험; 안정 시 통증, 운동 시 통증, 관절 부종, 계단 보행 통증 등 모든 지표에서 유의한 개선 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **데이터 공백 안내**: 한국 MFDS 허가 정보가 존재하지 않아 국내 기준 경고·금기·약물상호작용 데이터를 확인할 수 없습니다. 한국 시장 도입 전 해외 허가사항(FDA, EMA) 기반 안전성 자료 검토 및 MFDS 제출을 위한 안전성 문서화가 필요합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Etodolac은 이미 미국·유럽에서 골관절염 치료제로 수십 년간 허가 사용되어 온 약물로, 다수의 완료된 RCT와 20편 이상의 문헌이 OA에서의 효능을 뒷받침합니다(근거 수준 L1). 한국 미허가는 안전성·유효성 증거 부족이 아닌 시장 공백에서 기인하며, TxGNN 예측(99.97%) 역시 글로벌 임상 근거와 완전히 일치합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 작용 기전(MOA) 상세 데이터 보완
- MFDS 허가 신청용 안전성 자료 구성 (미국 FDA·EMA 허가사항 기반)
- 한국 환자군에서의 약동학(PK) 추가 데이터 필요 여부 검토
- 심혈관질환·신장질환·소화성 궤양 등 고위험군 대상 안전성 모니터링 계획 수립
- 국내 기허가 COX-2 선택적 NSAID 대비 시장 포지셔닝 전략 수립
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

