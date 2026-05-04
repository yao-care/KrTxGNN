---
layout: default
title: Diclofenac
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: 소염·진통에서 골관절염 감수성으로

## 한 문장 요약

> Diclofenac은 COX-1/COX-2를 억제하여 염증 매개물질(PGE2) 생성을 차단하는 비스테로이드성 소염진통제(NSAID)로, 전 세계적으로 관절통·근골격계 염증·류마티스 질환 치료에 광범위하게 사용되어 왔습니다.
> TxGNN 모델은 **골관절염 감수성(Osteoarthritis Susceptibility)**에 효과가 있을 수 있다고 예측하며,
> 현재 **1건의 임상시험**과 **5편의 문헌**이 이 방향을 간접적으로 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 관절통, 근골격계 염증, 류마티스 관절염, 강직성 척추염 (글로벌 허가 기준) |
| 예측 신규 적응증 | 골관절염 감수성 (Osteoarthritis Susceptibility) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Diclofenac은 아라키돈산과 경쟁하여 COX-1/COX-2에 결합함으로써 프로스타글란딘 E2(PGE2) 생성을 억제합니다. PGE2는 관절 내 활막염(synovitis)과 통증 감각화(pain sensitization)의 핵심 매개물질이며, Diclofenac의 이중 COX 억제 기전은 관절 조직에서의 항염증 효과와 직접 연결됩니다. 국소 외용 제형(겔, 패치)의 경우 관절 조직까지 직접 침투하여 전신 부작용을 최소화하면서도 치료 효과를 발휘할 수 있다는 제형 상의 이점도 존재합니다.

골관절염 감수성(OA susceptibility)이란 실제 OA 치료가 아닌, 유전적·환경적 고위험군의 OA 발병 경향을 의미합니다. COX-2 유전자 다형성(예: rs20417)이 OA 발병 위험과 관련 있다는 연구가 발표된 바 있어, 이론적으로 COX-2 억제제가 화학적 예방(chemoprevention)의 잠재력을 가질 수 있습니다. 그러나 현재까지 OA 고위험군을 대상으로 한 직접 예방 목적의 임상 RCT는 존재하지 않으며, 수집된 모든 근거는 OA **치료** 연구에서의 간접 외삽입니다.

TxGNN의 예측 신뢰도는 높지만(99.82%), 이 예측의 실제 임상 적용 가능성은 아직 연구 질문 수준에 머물러 있습니다. 인접 예측인 골관절염 치료(rank 2)에는 다수의 Phase 3 RCT(L1 수준)가 존재하여 기전적 타당성을 간접적으로 뒷받침하나, 감수성 예방 적용에 대한 직접 근거 확보가 반드시 선행되어야 합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04402047](https://clinicaltrials.gov/study/NCT04402047) | N/A | 미확인 | 108 | 수지 골관절염 환자에서 전침(전기침) vs 국소 Diclofenac 소듐 겔 비교 RCT. OA 발병 예방이 아닌 치료 비교 연구이며, 임상시험 상태가 미확인(UNKNOWN)으로 결과 신뢰도 제한 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28497473](https://pubmed.ncbi.nlm.nih.gov/28497473/) | 2017 | Cochrane Overview | Cochrane Database Syst Rev | 급성·만성 통증에서 국소 진통제의 Cochrane 리뷰 종합. OA(수지·슬관절) 및 신경병증성 통증에서 국소 Diclofenac 등 NSAID의 근거를 체계적으로 검토 |
| [38183573](https://pubmed.ncbi.nlm.nih.gov/38183573/) | 2024 | 모델 기반 메타분석 | Pain Ther | 아세트아미노펜과 국소 Diclofenac 병용이 경도~중등도 OA 통증에 미치는 효과 평가. 두 약물의 상보적 기전 및 오피오이드 절감 효과 분석 |
| [30860559](https://pubmed.ncbi.nlm.nih.gov/30860559/) | 2019 | 후향적 코호트 | JAMA | 슬관절 OA 환자에서 트라마돌 vs NSAID(Diclofenac 포함) 전체 사망률 비교. 트라마돌군에서 사망률이 높아 NSAIDs의 상대적 안전성 재조명 |
| [14575648](https://pubmed.ncbi.nlm.nih.gov/14575648/) | 2003 | 안전성 리뷰 | Toxicol Appl Pharmacol | Diclofenac 유발 특발성 간독성(idiosyncratic hepatotoxicity) 검토. 투여 1~3개월 후 지연 발생하며, 환자별 유전적 감수성 인자가 주요 위험 요인 |
| [3142593](https://pubmed.ncbi.nlm.nih.gov/3142593/) | 1988 | RCT (안전성) | BMJ | NSAID(naproxen, piroxicam, diclofenac, indomethacin) 투여 시 ranitidine의 위십이지장 손상 예방 효과 평가. Diclofenac 포함 NSAID군에서 위장관 보호 전략의 필요성 확인 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
골관절염 감수성(OA susceptibility)에 대한 Diclofenac의 예방적 적용은 COX-2 기전을 통한 이론적 합리성이 존재하나, 고위험군을 직접 대상으로 한 임상 근거가 전무하며 수집된 모든 근거가 치료 연구에서의 간접 외삽에 그쳐 현재 S1(연구 질문) 단계에 머물러 있습니다.

**진행하려면 필요한 것:**
- OA 유전적 고위험군(COX-2 다형성 rs20417 보유자 등)을 대상으로 한 전향적 예방 임상시험 설계
- COX-2 유전자 다형성과 Diclofenac 반응성 간 연관성 검증 연구
- 약물 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회 권장)
- 한국 식약처(MFDS) 허가 현황 및 仿單 안전성 정보 확인
- OA 감수성 예방 vs. OA 치료 중 우선 개발 적응증 전략 결정 *(OA 치료 적응증에는 Phase 3 RCT 기반 L1 수준의 강력한 근거가 이미 존재함)*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

