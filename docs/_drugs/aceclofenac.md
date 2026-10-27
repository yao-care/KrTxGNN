---
layout: default
title: Aceclofenac
parent: 모델 예측만 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aceclofenac: 예측 신규 적응증 골관절염 감수성 (osteoarthritis susceptibility). 실질 평가는 골관절염 (Osteoarthritis… (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 이번 자료에서 확인되지 않았습니다. 문헌상 통증과 염증 질환(골관절염, 류마티스관절염, 강직성척추염…"
monitor_inn: "Aceclofenac"
predicted_indications: ["brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "brachyolmia", "pseudoachondroplasia"]
---

# Aceclofenac
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

## Aceclofenac: 소염·진통제에서 골관절염으로
{: .text-alpha }

## 한 문장 요약

Aceclofenac은 비스테로이드성 소염진통제(NSAID)로, 근골격계의 통증과 염증 치료에 사용되어 왔습니다.
TxGNN 모델의 1순위 예측은 "골관절염 감수성(osteoarthritis susceptibility)"입니다. 이는 유전적 위험 표지에 가까워 실제 치료 대상으로 보기 어렵고, 임상적 의미는 2순위인 **골관절염(Osteoarthritis)**에 반영됩니다.
골관절염에는 **임상시험 2건**과 **문헌 20편**이 있고, 이 중 aceclofenac을 직접 다룬 근거가 다수 있습니다. 다만 이는 이미 시판 중인 용도를 확인하는 수준이며, 새로운 용도 발굴이라고 보기는 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 이번 자료에서 확인되지 않았습니다. 문헌상 통증과 염증 질환(골관절염, 류마티스관절염, 강직성척추염, 요통 등)에 사용됩니다. |
| 예측 신규 적응증 | 골관절염 감수성 (osteoarthritis susceptibility). 실질 평가는 골관절염 (Osteoarthritis) 기준 |
| TxGNN 예측 점수 | 99.97% (골관절염 감수성), 99.92% (골관절염) |
| 근거 수준 | 골관절염 L3 (완료된 Phase 3 RCT는 없고 Phase 4 RCT와 RCT 메타분석이 있음), 골관절염 감수성 L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 단일제, 유효) |
| 권장 결정 | 골관절염: Proceed with Guardrails / 골관절염 감수성: Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 자료에 없습니다. 알려진 정보에 따르면 aceclofenac은 COX-2를 매개로 한 프로스타글란딘 합성을 억제하는 NSAID입니다. IL-1β와 TNF-α를 줄일 가능성도 보고되어 있습니다. 이 작용으로 골관절염의 통증과 염증이 완화됩니다.

1순위인 "골관절염 감수성"은 치료할 수 있는 임상 질환이 아니라 유전적 위험 라벨입니다. 그래프상 골관절염과 가까워서 점수가 높게 나왔을 가능성이 큽니다. 이 항목에 대한 임상시험과 문헌은 없습니다. 따라서 실질적인 평가는 골관절염 적응증으로 합니다.

골관절염은 aceclofenac의 기존 시판 용도와 일치합니다. 모델 예측이 타당하다는 점은 확인되지만, 새로운 용도를 찾은 것은 아닙니다.

## 임상시험 근거

골관절염 관련 시험입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02682524](https://clinicaltrials.gov/study/NCT02682524) | Phase 4 | 완료 | 191 | 무릎 골관절염에서 PlbCR와 aceclofenac의 효능·안전성을 비교한 다기관 이중맹검 RCT입니다. Aceclofenac은 활성 대조약입니다. |
| [NCT00635349](https://clinicaltrials.gov/study/NCT00635349) | Phase 4 | 완료 | 143 | 무릎 골관절염에서 tramadol/acetaminophen 유지요법과 NSAID 유지요법을 비교했습니다. 대조 NSAID가 aceclofenac이라는 근거는 불분명해 간접 근거입니다. |

참고로 인접 질환인 류마티스관절염 시험도 있습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04144101](https://clinicaltrials.gov/study/NCT04144101) | Phase 4 | 완료 | 40 | 류마티스관절염에서 저용량 etoricoxib(60 mg/일)과 aceclofenac(100 mg 하루 2회)을 비교한 소규모 파일럿 RCT입니다. |

## 문헌 근거

골관절염 관련으로, RCT와 메타분석을 우선하고 이어서 종설 순으로 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28293447](https://pubmed.ncbi.nlm.nih.gov/28293447/) | 2017 | RCT 메타분석 | European Journal of Rheumatology | 골관절염에서 aceclofenac의 통증, 기능, 안전성을 다른 NSAID나 진통제와 비교했습니다. |
| [16709320](https://pubmed.ncbi.nlm.nih.gov/16709320/) | 2006 | RCT | Current Medical Research and Opinion | 인도에서 시행한 이중맹검 비교시험으로, 골관절염에서 aceclofenac과 diclofenac의 효능과 안전성을 비교했습니다. |
| [24639945](https://pubmed.ncbi.nlm.nih.gov/24639945/) | 2014 | RCT | Knee Surgery & Related Research | 무릎 골관절염에서 aceclofenac 서방형(CR)의 4주 효능과 안전성을 평가했습니다. |
| [21277837](https://pubmed.ncbi.nlm.nih.gov/21277837/) | 2011 | RCT | The Journal of Pain | 285명을 대상으로 한 6주 이중맹검 시험입니다. Aceclofenac CR 하루 1회와 일반 정제 하루 2회를 비교했습니다. |
| [20387351](https://pubmed.ncbi.nlm.nih.gov/20387351/) | 2009 | RCT/비교연구 | JNMA (Nepal) | 골관절염에서 aceclofenac과 nabumetone의 효능과 위장관 내약성을 비교했습니다. |
| [32991606](https://pubmed.ncbi.nlm.nih.gov/32991606/) | 2020 | Phase 4 RCT | PLoS One | 증상이 있는 무릎 골관절염에서 pelubiprofen CR과 aceclofenac(200 mg/일)의 비열등성을 4주간 평가했습니다. |
| [23581533](https://pubmed.ncbi.nlm.nih.gov/23581533/) | 2013 | RCT | Current Medical Research and Opinion | 무릎 골관절염에서 aceclofenac과 diclofenac의 위장관 안전성과 내약성을 비교했습니다. |
| [8608684](https://pubmed.ncbi.nlm.nih.gov/8608684/) | 1995 | RCT | Clinical Rheumatology | 무릎 골관절염 397명을 12주간 비교했습니다. Aceclofenac과 diclofenac 모두 증상이 유의하게 개선되었습니다. |
| [34876850](https://pubmed.ncbi.nlm.nih.gov/34876850/) | 2021 | 종설 | Journal of Pain Research | 근골격계 질환에서 aceclofenac의 진통·소염 효과를 정리했습니다. |
| [11511027](https://pubmed.ncbi.nlm.nih.gov/11511027/) | 2001 | 종설 | Drugs | 무릎 골관절염에서 aceclofenac이 diclofenac, piroxicam, naproxen과 비슷한 수준으로 통증을 줄이고 기능을 개선한다고 정리했습니다. |

인접 질환인 류마티스관절염에도 RCT가 있습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8778950](https://pubmed.ncbi.nlm.nih.gov/8778950/) | 1996 | RCT | Rheumatology International | 12주 이중맹검 시험에서 aceclofenac의 효능이 indomethacin과 비슷했습니다. |
| [8588120](https://pubmed.ncbi.nlm.nih.gov/8588120/) | 1995 | RCT | Rheumatology International | 3개월 이중맹검 시험에서 aceclofenac과 ketoprofen을 비교했습니다. |

## 한국 시판 정보

한국에는 총 20건의 허가가 있고, 모두 단일제이며 유효합니다. 아래는 주요 5건입니다. 허가 적응증은 허가사항 문서 링크로만 제공되어 요약하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|-------|
| 199400486 | 에어탈정 | 필름코팅정 | (주)대웅제약 |
| 199801524 | 세나펜정 | 필름코팅정 | 대원제약(주) |
| 199802092 | 에이서정 | 필름코팅정 | 경동제약(주) |
| 200411098 | 아세민정 | 필름코팅정 | (주)한국피엠지제약 |
| 201906109 | 아클페낙CR서방정 | 서방성 필름코팅정 | 엔비케이제약(주) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

NSAID 계열에서 일반적으로 알려진 주의사항은 다음과 같습니다.
- 위장관, 심혈관, 신장 위험을 모니터링해야 합니다.
- 최소 유효 용량을 최단 기간 사용하는 것이 원칙입니다.
- 류마티스관절염에서 methotrexate와 병용할 때는 NSAID 상호작용에 유의해야 합니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails (골관절염) / Hold (골관절염 감수성)**

**사유:**
골관절염은 aceclofenac의 기존 시판 용도이며, Phase 4 RCT와 다수의 비교 RCT, RCT 메타분석이 효능과 안전성을 뒷받침합니다. 다만 완료된 Phase 3 시험은 없어 근거 수준은 L3로 평가했고, 새로운 용도는 아니므로 위험 관리를 전제로 진행하는 것이 적절합니다. 1순위인 골관절염 감수성은 치료 대상이 될 수 없는 유전적 위험 라벨이고 임상 근거도 없어 보류합니다.

**진행하려면 필요한 것:**
- 허가사항에서 경고, 금기, 적응증 원문을 확보해 안전성 검토를 마쳐야 합니다.
- 작용 기전 데이터를 보강해야 합니다.
- 위장관, 심혈관, 신장 위험에 대한 모니터링 계획을 세워야 합니다.
- 류마티스관절염 등 인접 적응증은 소규모 시험 위주이므로 추가 근거가 필요하며, DMARD 보조요법으로 한정해야 합니다.
- 골격 이형성증 등 희귀 유전질환(brachyolmia, pseudoachondroplasia 등) 예측은 기전적 연결도 임상 근거도 없어 우선순위를 두지 않는 것이 좋습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

