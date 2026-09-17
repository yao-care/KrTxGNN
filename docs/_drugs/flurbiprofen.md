---
layout: default
title: Flurbiprofen
parent: 높은 근거 (L1-L2)
nav_order: 335
evidence_level: L1
indication_count: 10
---

# Flurbiprofen
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

TxGNN 상위 예측(1위 "osteoarthritis susceptibility")은 근거팩 자체가 "지식그래프 인접성에 의한 예측 오탐"이라 명시하고 근거 0건·Hold 권고를 부여했습니다. 이를 그대로 대표 적응증으로 쓰면 보고서가 사실상 공백이 되므로, 실질적 임상근거(L1, Proceed with Guardrails)가 확인된 **골관절염**을 대표 적응증으로 삼아 작성했습니다(류마티스 관절염·관절병증도 동일 계열 근거로 병기).

---

# Flurbiprofen: 국내 미상영 성분에서 골관절염 대증치료로

## 한 문장 요약

Flurbiprofen은 프로피온산 유도체 계열 비스테로이드성 소염진통제(NSAID)로, 한국에는 아직 허가·시판된 제품이 없습니다.
TxGNN 모델은 **골관절염(Osteoarthritis)**에 효과가 있을 것으로 예측하며, 현재 **2건의 임상시험**과 **19편의 문헌**이 이를 지지합니다.
다만 TxGNN이 가장 높은 점수로 예측한 "골관절염 감수성(osteoarthritis susceptibility)"은 유전적 위험 마커일 뿐 치료 가능한 질병이 아니며, 근거팩 자체가 이를 예측 오탐(artifact)으로 판정했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 국내 허가 정보 없음 (미상영). 국제적으로는 류마티스 관절염·골관절염 등 통증/염증성 질환의 대증치료제로 사용되어 온 성분 |
| 예측 신규 적응증 | 골관절염 (Osteoarthritis) |
| TxGNN 예측 점수 | 99.99% (rank 705) |
| 근거 수준 | L1 |
| 한국 시판 현황 | 미상영 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

공식 DrugBank MOA 필드는 미확보 상태([Data Gap])이지만, 근거팩 내 기전 분석에 따르면 Flurbiprofen은 비선택적 COX-1/COX-2 억제제로 프로스타글란딘 합성을 억제해 항염·진통 작용을 나타냅니다. 골관절염은 관절 연골 퇴행과 국소 염증이 통증을 유발하는 질환으로, COX 억제를 통한 대증(對症) 치료 기전이 이미 확립되어 있습니다. 실제로 S-flurbiprofen 첩포제(SFPP)가 여러 국가에서 슬관절 골관절염 적응증으로 다수의 Phase II/III RCT를 거쳐 사용되고 있어, 기전상 타당성이 높습니다.

같은 근거팩 내에서 류마티스 관절염(rank2, 99.99%, L1)과 관절병증(arthropathy, rank10, 99.97%, L2)도 유사한 수준의 실증거로 확인되어, "관절 염증성 질환군"에 대한 일관된 신호로 해석됩니다.

**주의**: TxGNN이 가장 높은 점수(99.998%)로 예측한 "osteoarthritis susceptibility"(및 3~6, 8~9위의 초희귀 유전 골격 증후군들)는 GDF5 유전자 노드와의 지식그래프 인접성에 의한 예측 오탐으로, 임상시험·문헌 근거가 전혀 없고 근거팩 자체가 "후속 평가 진입 불가(Hold)"로 명시하고 있습니다. 본 보고서에서는 제외했습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06566794](https://clinicaltrials.gov/study/NCT06566794) | N/A | 완료 | 12 | 베타차단제(carvedilol)·NSAID의 CYP 효소 매개 약물대사 영향 연구. 골관절염 치료제로서의 직접 유효성 시험은 아님 (관련성 등급 C) |
| [NCT02784041](https://clinicaltrials.gov/study/NCT02784041) | N/A | 불명 | 200 | 슬관절 전치환술 후 내전근관차단 vs 관절주위침윤 진통 효과 비교, NSAID 병용 포함 (관련성 등급 B, 결과 미확인) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35199483](https://pubmed.ncbi.nlm.nih.gov/35199483/) | 2022 | RCT (Phase III) | Int J Rheum Dis | S-flurbiprofen 첩포제 vs diclofenac 젤, 슬관절 골관절염 2주 무작위대조시험 |
| [27168463](https://pubmed.ncbi.nlm.nih.gov/27168463/) | 2017 | RCT (Phase III) | Mod Rheumatol | S-flurbiprofen 첩포제, flurbiprofen 패치 대비 활성대조 3상 시험 |
| [28442928](https://pubmed.ncbi.nlm.nih.gov/28442928/) | 2017 | RCT (Phase II) | J Pain Res | S-flurbiprofen 첩포제 위약대조 용량설정 2상 시험 |
| [36223938](https://pubmed.ncbi.nlm.nih.gov/36223938/) | 2022 | RCT | Drug Discov Ther | 듈록세틴+S-flurbiprofen 첩포제 vs 듈록세틴+기존 NSAID, 골관절염 만성통증 (OASIS DUAL) |
| [37545031](https://pubmed.ncbi.nlm.nih.gov/37545031/) | 2023 | RCT | Chin Med J | Flurbiprofen 카타플라즘 vs loxoprofen 카타플라즘, 슬관절 골관절염 |
| [3963030](https://pubmed.ncbi.nlm.nih.gov/3963030/) | 1986 | RCT | Am J Med | Flurbiprofen vs aspirin, 슬관절 골관절염 12주 다기관 시험 |
| [3515919](https://pubmed.ncbi.nlm.nih.gov/3515919/) | 1986 | RCT | Am J Med | Flurbiprofen vs sulindac, 고관절/슬관절 골관절염 이중맹검 시험 |
| [3044870](https://pubmed.ncbi.nlm.nih.gov/3044870/) | 1988 | RCT | J Int Med Res | Flurbiprofen vs diclofenac, 야간통·조조강직 교차시험 |
| [1307585](https://pubmed.ncbi.nlm.nih.gov/1307585/) | 1992 | RCT | J Postgrad Med | Flurbiprofen vs piroxicam, 슬관절 골관절염 비교 |
| [37662513](https://pubmed.ncbi.nlm.nih.gov/37662513/) | 2023 | Cohort | Cureus | S-flurbiprofen 첩포제의 중등도~말기 슬관절 골관절염 통증관리 효과 및 순응도 |

## 한국 시판 정보

현재 한국에 허가된 Flurbiprofen 제품이 없습니다 (미상영, 허가증 0건).

## 안전성 고려사항

국내 허가 정보가 없어 참조할 자국 첨부문서(허가사항)가 없는 상태입니다. 약물상호작용 데이터베이스 조회도 "not_found"로, 이는 상호작용이 없다는 의미가 아니라 조회 매칭 데이터 자체가 없었다는 뜻입니다. 해외 허가국(예: 미국 Ansaid, 일본 S-flurbiprofen 첩포제) 첨부문서의 경고·금기·상호작용 정보를 별도로 확보해 확인할 필요가 있습니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 골관절염(및 류마티스 관절염) 적응증에 대해 다수의 Phase II/III RCT를 포함한 L1 수준 근거가 확인되며, COX 억제 기전도 명확합니다.
- 다만 한국 내 허가·시판 이력이 전무하고(미상영), 국소 안전성 라벨(TFDA/식약처 급 자료)과 DrugBank MOA 레코드가 확보되지 않은 상태(Blocking/High 데이터 갭)이므로 안전성 초평가(S1) 이전 단계입니다.
- TxGNN 최상위 점수 예측(골관절염 감수성 등 유전 증후군 6건)은 근거 0건의 지식그래프 예측 오탐으로 판정되어 후속 검토 대상에서 제외합니다.

**진행하려면 필요한 것:**
- 해외 허가국 첨부문서(경고·금기·DDI) 확보 및 국내 도입 시 안전성 초평가(S1) 진행 (DG001, Blocking)
- DrugBank API 조회를 통한 공식 MOA 데이터 확보 (DG002, High)
- 국내 미상영 상태에서의 도입 여부(신규 허가 신청 필요성) 규제 검토
- arthropathy(관절병증)처럼 포괄적 병명은 OA/RA 근거와 중복 가능성이 있어 구체 적응증 범위 정리 필요
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

