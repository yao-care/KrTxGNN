---
layout: default
title: Aceclofenac
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Aceclofenac
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

# Aceclofenac: 근골격 염증성 통증 치료에서 골관절염으로

---

## 한 문장 요약

Aceclofenac은 COX-1/COX-2를 억제하는 경구용 NSAID로, 해외에서 골관절염·류마티스관절염·강직성척추염 등 근골격 염증성 통증 치료에 널리 사용되고 있으나 **한국에서는 현재 허가 이력이 없는 약물**입니다.
TxGNN 모델은 1순위로 "osteoarthritis susceptibility(유전적 감수성)"를 예측하였으나, 이는 활동성 질환이 아닌 유전 소인을 지칭하므로 임상 적용 가능성이 없습니다. 실질적 근거가 가장 풍부한 **2순위 예측인 골관절염(Osteoarthritis)**을 핵심 적응증으로 분석하며, 현재 **5건의 임상시험**과 **20편의 문헌**(다수의 Phase IV RCT 및 메타분석 포함)이 이를 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 미허가 (해외에서 근골격 염증성 통증·관절염 치료에 사용) |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.92% (Rank 2; Rank 1은 감수성 표현형으로 임상 적용 불가) |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미상시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Aceclofenac은 phenylacetic acid 유도체로, COX-1 및 COX-2를 억제하여 프로스타글란딘 E2(PGE2) 합성을 감소시키고 관절 활막의 염증 반응을 완화합니다. 여기에 더해 IL-1β 및 TNF-α 억제, IL-1 수용체 길항제(IL-1Ra) 분비 촉진, 그리고 프로테오글리칸 합성 증가라는 추가 기전이 확인되어 있으며(PMID:11090115), 이는 단순한 NSAID를 넘어 연골 보호 특성을 갖는 약물임을 시사합니다.

골관절염은 관절 연골의 점진적 손상과 활막 염증이 핵심 병리 기전으로, Aceclofenac의 COX 억제·연골 기질 보호 효과가 직접적으로 적용됩니다. 실제로 Aceclofenac은 유럽, 인도, 스페인, 한국을 제외한 아시아 여러 국가에서 골관절염 적응증으로 허가되어 있으며, 다수의 무작위 대조 임상시험에서 diclofenac·piroxicam·naproxen 등 기존 NSAID와 동등한 효과가 입증되었습니다(PMID:8608684, PMID:16709320, PMID:28293447).

작용 기전 데이터는 DrugBank 조회를 통한 보완이 필요한 상태입니다. 그러나 문헌 기반의 기전 근거와 임상 결과가 충분히 축적되어 있어, 골관절염에서의 재창출 타당성은 기전·임상 양면에서 모두 높은 수준으로 뒷받침됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02682524](https://clinicaltrials.gov/study/NCT02682524) | Phase IV | 완료 | 191 | 무릎 골관절염 환자에서 Pelubiprofen CR 대비 Aceclofenac의 효능·안전성을 비교한 다기관 이중맹검 능동 대조 RCT; Aceclofenac이 대조 기준약으로 직접 포함됨 |
| [NCT00647517](https://clinicaltrials.gov/study/NCT00647517) | Phase IV | 완료 | 60 | 대만 중산의대병원에서 수행된 OA 및 염증성 관절염에서의 COX-2 NSAID 병용 요법 Phase IV 연구 |
| [NCT00635349](https://clinicaltrials.gov/study/NCT00635349) | Phase IV | 완료 | 143 | 무릎 OA 환자에서 Tramadol/APAP 유지 vs NSAID 유지를 비교한 다기관 무작위 공개 연구; NSAID군에 Aceclofenac 포함 가능 |
| [NCT03911570](https://clinicaltrials.gov/study/NCT03911570) | N/A | 완료 | 108 | 손 OA 환자에서 결정형 글루코사민설페이트의 증상 효과를 평가한 후향적 비교 연구 (Aceclofenac은 대조 배경 치료로 병용) |
| [NCT04170218](https://clinicaltrials.gov/study/NCT04170218) | N/A | 불명 | 405 | 프랑스 노인 무릎·고관절 OA 환자의 치료 질 지표를 평가한 다기관 관찰 연구 (Aceclofenac 직접 연구 아님) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28293447](https://pubmed.ncbi.nlm.nih.gov/28293447/) | 2017 | 체계적 고찰/메타분석 | European Journal of Rheumatology | OA 환자에서 Aceclofenac의 통증·기능·안전성을 다른 NSAID와 비교한 RCT 메타분석; 효능 동등, 위장관 내약성 우수 |
| [24639945](https://pubmed.ncbi.nlm.nih.gov/24639945/) | 2014 | RCT | Knee Surgery & Related Research | 만성 무릎 OA에서 Aceclofenac CR의 진통 효과 및 안전성 평가 4주 다기관 무작위 비교 임상시험 |
| [21277837](https://pubmed.ncbi.nlm.nih.gov/21277837/) | 2011 | RCT | The Journal of Pain | 무릎 OA에서 Aceclofenac CR 1일1회 vs 기존 Aceclofenac 1일2회를 비교한 6기관 이중맹검 RCT (N=285); 두 군 모두 통증·기능 유의한 개선 |
| [32991606](https://pubmed.ncbi.nlm.nih.gov/32991606/) | 2020 | RCT | PloS One | 증상성 무릎 OA에서 Pelubiprofen CR 90mg vs Aceclofenac 200mg의 효능·안전성 비교 Phase IV 비열등성 RCT; Aceclofenac 기준 비열등성 입증 |
| [34876850](https://pubmed.ncbi.nlm.nih.gov/34876850/) | 2021 | 서술적 고찰 | Journal of Pain Research | 근골격 질환에서 Aceclofenac의 진통·항염 효과 종합 리뷰; OA·RA·AS에서의 국가별 허가 현황 및 임상 데이터 정리 |
| [11511027](https://pubmed.ncbi.nlm.nih.gov/11511027/) | 2001 | 종합 리뷰 | Drugs | Aceclofenac의 통증·류마티스 질환 관리 재평가; 무릎 OA에서 diclofenac·piroxicam·naproxen과 동등한 효과 확인, 선호 위장관 프로파일 기술 |
| [16709320](https://pubmed.ncbi.nlm.nih.gov/16709320/) | 2006 | RCT | Current Medical Research and Opinion | OA에서 Aceclofenac vs Diclofenac 비교 이중맹검 RCT (인도); 효능 동등, GI 내약성 Aceclofenac 우세 |
| [8608684](https://pubmed.ncbi.nlm.nih.gov/8608684/) | 1995 | RCT | Clinical Rheumatology | 무릎 OA에서 Aceclofenac 100mg×2 vs Diclofenac 50mg×3 비교 12주 다기관 무작위 이중맹검 연구 (N=397); 두 군 모두 유의한 개선, 효능 동등 |
| [20387351](https://pubmed.ncbi.nlm.nih.gov/20387351/) | 2009 | 비교 연구 | JNMA | OA 환자에서 Aceclofenac과 Nabumetone의 효능 및 위장관 내약성 직접 비교 |
| [38937394](https://pubmed.ncbi.nlm.nih.gov/38937394/) | 2024 | 체계적 고찰/메타분석 | Drugs | 요통 및 OA에서 Paracetamol 병용 요법의 효과·안전성 체계적 고찰; NSAID 단독 vs 병용 비교 포함 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Aceclofenac의 골관절염 적응증은 해외에서 이미 확립된 적응증으로, Phase IV RCT 복수 건과 메타분석을 포함한 L1 수준의 강력한 임상 근거가 존재합니다. 한국에서는 현재 허가 이력이 없으나, 해외 데이터의 양과 질이 충분하여 허가 신청을 검토할 수 있는 단계입니다. 단, 안전성 데이터(MFDS 허가사항, DDI 등) 보완이 선행되어야 합니다.

**진행하려면 필요한 것:**
- MFDS 허가 또는 해외 허가 자료를 기반으로 한 주요 경고·금기·약물 상호작용 목록 확보
- DrugBank API를 통한 작용 기전(MOA) 상세 데이터 보완
- 한국 내 임상 데이터 확보 전략 수립 (해외 데이터 브리지 가능 여부 MFDS 사전 자문 권고)
- NSAID 계열 공통 위험(심혈관·신장·위장관)에 대한 특별 모니터링 계획 수립
- 한국 시판 NSAID(celecoxib, naproxen, ibuprofen 등)와의 경쟁 포지셔닝 분석

---

> ⚠️ **면책사항**: 본 보고서는 연구 참고용으로만 제공되며, 의료적 판단이나 처방의 근거로 사용할 수 없습니다. 모든 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

