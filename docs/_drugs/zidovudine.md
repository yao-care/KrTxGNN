---
layout: default
title: Zidovudine
parent: 모델 예측만 (L5)
nav_order: 728
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

# Zidovudine: HIV/AIDS에서 고양이 후천성면역결핍증후군(FIV)으로

## 한 문장 요약

Zidovudine(AZT)은 세계 최초로 승인된 항레트로바이러스제로, 원래 HIV 감염 및 AIDS 치료에 사용되어 온 약물입니다. TxGNN 모델은 **고양이 후천성면역결핍증후군(Feline AIDS, FIV)**에도 효과가 있을 수 있다고 예측하며(점수 99.96%), 현재 관련 **임상시험은 없고 20편의 동물모델 문헌**이 이를 뒷받침합니다. 다만 이 예측은 인체 적응증이 아닌 고양이를 대상으로 한 수의학 연구에 기반하고 있어 해석에 주의가 필요합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | HIV/AIDS(후천성면역결핍증후군) — 한국 허가 정보 없음, 국제적으로 알려진 원 적응증 및 근거 문헌 맥락에 기반 |
| 예측 신규 적응증 | 고양이 후천성면역결핍증후군 (Feline Acquired Immunodeficiency Syndrome, FIV) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L4 (동물 전임상 연구만 존재, 인체 임상시험 없음) |
| 한국 시판 현황 | 미판매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 DrugBank에 상세한 작용 기전(MOA) 데이터가 등록되어 있지 않습니다(Data Gap). 다만 Zidovudine은 뉴클레오사이드 역전사효소 억제제(NRTI) 계열 약물로 널리 알려져 있으며, HIV-1 역전사효소를 경쟁적으로 억제하여 바이러스 복제를 차단하는 기전으로 작용한다는 점은 다수의 근거 문헌에서 일관되게 확인됩니다.

고양이 면역결핍바이러스(FIV)와 원숭이 면역결핍바이러스(SIV)는 HIV와 유전적·구조적으로 상동성이 높은 렌티바이러스로, 오랫동안 HIV 항바이러스제의 전임상 동물모델로 활용되어 왔습니다. 문헌 근거(예: PMID 2475068, 2480079)에 따르면 AZT의 삼인산 대사체가 FIV 및 SIV의 역전사효소를 HIV-1과 유사한 기전으로 억제하는 것이 in vitro에서 확인되었습니다.

다만 이는 **AZT의 기존 항레트로바이러스 기전이 상동 바이러스 모델(고양이·원숭이)에서도 재현된다는 것을 보여주는 전임상적 확인**에 가까우며, 사람에게 발생하지 않는 고양이 질환(FIV)을 새로운 인체 임상 적응증으로 해석하기는 어렵습니다. TxGNN 지식그래프 상 HIV와 FIV/SIV 노드 간의 강한 기전적 유사성이 높은 예측 점수로 이어진 것으로 판단됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | 전임상(기전) | Antimicrob Agents Chemother | FIV의 역전사효소가 HIV-1과 유사하여 항레트로바이러스 화학요법 모델로 활용 가능함을 최초 제시 |
| [2480079](https://pubmed.ncbi.nlm.nih.gov/2480079/) | 1989 | 전임상(효소 억제) | Antimicrob Agents Chemother | AZT 유사체 삼인산이 인간 및 SIV 역전사효소를 선택적으로 강력히 억제 |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | 전임상(동물, FeLV) | Antimicrob Agents Chemother | 인터페론-α와 AZT 병용이 무증상 FeLV 유발 면역결핍증후군(FAIDS) 치료 효능 향상 |
| [2164083](https://pubmed.ncbi.nlm.nih.gov/2164083/) | 1990 | 전임상(동물, 예방) | J Acquir Immune Defic Syndr | AZT+인터페론-α+IL-2 병용이 FeLV-FAIDS 예방요법으로 시험됨 |
| [2163339](https://pubmed.ncbi.nlm.nih.gov/2163339/) | 1990 | 독성 연구 | Fundam Appl Toxicol | FeLV 감염 고양이에서 AZT 용량별 독성(골수억제 등) 평가 |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | 전임상(예방) | J Acquir Immune Defic Syndr | 예방적 AZT 투여가 FIV 감염 초기 바이레미아 및 림프구 감소를 억제(감염 자체는 예방 못함) |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | 전임상(약력학) | Arch Virol | AZT 및 사이클로스포린이 혈장 FIV 역가에 미치는 영향 비교 |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | 전임상(병용요법, in vitro) | Antiviral Res | ZDV+3TC+ABC 병용이 FIV 복제 억제에서 상가/상승 효과 확인 |
| [18550661](https://pubmed.ncbi.nlm.nih.gov/18550661/) | 2008 | 전임상(내성 분석) | J Virol | NRTI(AZT) 치료 중인 고양이에서 FIV gag/pol/env 유전자 계통분석 |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | 전임상(장기 추적) | J Feline Med Surg | FIV 감염 고양이에서 AZT 단독 후 병용요법으로 전환한 5–6년 장기 항레트로바이러스 치료 추적 결과 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (주요 경고, 금기, 약물 상호작용 데이터 모두 Data Gap이며, TFDA/한국 규제기관의 공식 허가사항 확인이 필요합니다.)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN이 최상위로 예측한 신규 적응증(고양이 후천성면역결핍증후군, FIV)은 인체 질환이 아닌 수의학적 동물모델 질환입니다. 근거 문헌 20편은 모두 1989~2016년 사이의 고양이 대상 전임상 연구로, HIV 연구용 동물모델에서 AZT의 기존 기전이 재현됨을 보여줄 뿐 인체 대상 임상시험 근거는 전무합니다. 이 예측을 사람 대상 신규 적응증 후보로 진행하기는 부적절합니다.

**진행하려면 필요한 것:**
- TxGNN 예측 파이프라인에서 동물 전용 질환(FIV, SIV 등 비인체 질환 노드)을 인체 적응증 후보에서 배제하는 필터링 로직 검토
- TFDA/한국 규제기관 공식 허가사항(경고, 금기, DDI) 확보 — 현재 Blocking 수준 Data Gap(DG001)으로 안전성 초기평가(S1) 진입 불가
- DrugBank 작용 기전(MOA) 데이터 보완(DG002)
- 참고: 본 Evidence Pack 5위 항목인 "AIDS related complex"는 이미 L1 근거 수준(Phase 3 RCT 다수, n=1,496~3,200 규모 포함)과 "Proceed with Guardrails" 평가를 자체적으로 확보하고 있어, 이는 AZT의 기존 적응증 연장 검토 대상으로 별도 보고서 작성을 권장합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

