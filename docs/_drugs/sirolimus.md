---
layout: default
title: Sirolimus
parent: 모델 예측만 (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
---

# Sirolimus
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Sirolimus: 신장 이식 거부반응 예방에서 지방육종(Liposarcoma)으로

## 한 문장 요약

Sirolimus(라파마이신)는 원래 신장 이식 후 거부반응을 예방하는 면역억제제로 개발되었습니다.
TxGNN 모델은 **지방육종(Liposarcoma)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.89%),
현재 관련 완료 임상시험은 등록되어 있지 않고 **12편의 문헌**(대부분 기전·전임상 연구)이 이 방향을 뒷받침합니다.
참고로 이번 Evidence Pack에는 지방육종 외에도 9건의 추가 예측 적응증이 포함되어 있으며,
그중 **림프관평활근종증(LAM)**은 이미 해외에서 Sirolimus의 승인 적응증으로 확립되어 있습니다(하단 "기타 예측 적응증 후보" 참조).

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 신장 이식 거부반응 예방 (면역억제제) — 국내 규제 자료상 허가 이력 없음 |
| 예측 신규 적응증 | 지방육종 (Liposarcoma) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L4 (전임상/기전 연구 중심, 완료된 임상시험 없음) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 기반 상세 작용 기전(MOA) 데이터는 확보되지 않았습니다(자료 공백, TFDA 수준 라벨 정보도 미확보). 다만 문헌 전반에서 Sirolimus가 **mTOR(mammalian target of rapamycin) 억제제**로 반복적으로 기술되고 있으며, 원래 신장 이식 후 거부반응 예방을 위한 면역억제제로 사용되어 왔습니다.

mTOR 경로 활성화는 탈분화 지방육종(dedifferentiated liposarcoma)을 포함한 여러 연조직육종에서 확립된 발암 기전 중 하나입니다. 실제로 Ishii 등(2016, PMID 26518767)은 탈분화 지방육종 99예에서 Akt/mTOR 및 MAPK 경로 활성화를 면역조직화학적으로 확인했으며, 이는 mTOR 억제제 적용의 이론적 근거가 됩니다.

같은 계열(rapalog) 약물인 everolimus는 지방육종/평활근육종 대상 Phase 2 시험(SAR-096, PMID 37967116)에서 CDK4 억제제와 병용 평가되었고, 여러 PDOX(patient-derived orthotopic xenograft) 마우스 모델 연구(PMID 37400145, 36309387)에서 rapamycin과 chloroquine 병용이 탈분화 지방육종 억제 효과를 보였습니다. 다만 이들 연구는 sirolimus 단독요법을 직접 검증한 완료 임상시험은 아니며, 대부분 전임상 또는 기전 연구 단계입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | 신장 이식 후 sirolimus 유지요법이 cyclosporine 대비 암 발생 위험을 낮춤 (525명 무작위 배정) |
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 임상시험 | Clin Cancer Res | Ribociclib(CDK4 억제제)+Everolimus(mTOR 억제제) 병용이 탈분화 지방육종·평활근육종에서 상승효과 시사 |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | 연조직육종 신규 표적치료제 종합 리뷰(GIST, 유상피육종 등 표적치료 승인 현황 포함) |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | 진행성 육종 대상 분자표적 치료제 임상시험 결과 리뷰 |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | 희귀 결합조직 종양·육종의 표적치료 리뷰 (mTOR 경로 포함 6개 분자 아형 분류) |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | 기전/면역조직화학 연구 | Tumour Biol | 탈분화 지방육종 99예에서 Akt/mTOR·MAPK 경로 활성화 확인, mTOR 억제제의 항종양 효과 시험 |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | 전임상 (PDOX 마우스모델) | Cancer Genomics Proteomics | Chloroquine+Rapamycin 병용 오토파지 억제가 고분화 지방육종에 효과적 |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | 전임상 (PDOX 마우스모델) | In Vivo | Chloroquine+Rapamycin 병용이 탈분화 지방육종 PDOX 모델에서 종양 성장 억제 |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | 전임상 (in vitro/in vivo) | Mol Cancer Ther | 차세대 mTOR 키나아제 억제제 MLN0128이 골·연조직육종에서 강력한 항종양 활성 |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | 관찰 연구 | Transplant Proc | 면역억제제 장기 사용 신장 이식 환자의 악성종양 발생 스크리닝 연구 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠ TFDA 수준 경고·금기 데이터와 작용기전(MOA) 데이터가 확보되지 않은 상태이며, 이는 안전성 초기평가(S1) 진입을 막는 **차단(Blocking)** 등급 자료 공백입니다.

---

## 기타 예측 적응증 후보 (참고)

이번 Evidence Pack에는 지방육종 외 9건의 예측 적응증이 함께 포함되어 있습니다. 근거 수준이 상대적으로 높은 후보를 참고용으로 정리합니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 | 비고 |
|------|-----------|-----------|----------|----------|------|
| 7 | 림프관평활근종증 (LAM) | 99.68% | L1 | Go | MILES 시험(NCT00414648, Phase3 완료, NEJM 2011) 등 다수 완료 임상시험 존재. 해외에서는 이미 승인된 적응증 |
| 6 | Lymphangiomyoma | 99.79% | L1 | Proceed with Guardrails | LAM과 밀접히 연관된 용어, 유사한 Phase 2/3 완료 시험 다수 |
| 3 | 투명세포신세포암 (ccRCC) | 99.84% | L1 | Proceed with Guardrails | Rapalog 계열(everolimus, temsirolimus)이 표준치료 일부이나, sirolimus 분자 자체의 직접 Phase 3 RCT는 부족 |
| 10 | 미분류 신세포암 | 99.66% | L2 | Proceed with Guardrails | Everolimus 대상 다수 완료 Phase 2 RCT(ASPEN, ESPN 등) 존재 |
| 5 | 양성 PEComa | 99.80% | L3 | Proceed with Guardrails | Sirolimus 직접 반응 사례보고 및 전향적 코호트 연구 존재 |
| 9 | RCC (Xp11.2/TFE3 전좌) | 99.66% | L4 | Hold | 관련 시험은 cabozantinib(비-mTOR 기전) 1건뿐, 직접 근거 부족 |
| 2 | 난소 점액양 지방육종 | 99.85% | L5 | Hold | 임상/문헌 근거 전무, 모델 추론만 존재 |
| 4 | 자궁 PEComa | 99.80% | L5 | Hold | 임상/문헌 근거 전무 |
| 8 | 신경모세포종 관련 RCC | 99.66% | L5 | Hold | 임상/문헌 근거 전무 |

**시사점**: LAM(rank 7)은 사실상 이미 확립된 sirolimus 승인 적응증으로, TxGNN 모델이 알려진 유효 적응증을 정확히 재발견했다는 점에서 모델 신뢰도를 뒷받침합니다. 다만 본 데이터셋 기준 한국 시판 허가는 확인되지 않아, 국내 재창출 전략 수립 시 LAM을 지방육종보다 우선 검토할 가치가 있습니다.

---

## 결론 및 다음 단계

**결정: Hold** (지방육종 적응증 기준)

**사유:**
mTOR 경로가 탈분화 지방육종의 확립된 발암 기전이라는 점, 그리고 rapalog 계열 약물의 병용요법 Phase 2 시험이 진행된 점은 기전적 타당성을 지지합니다. 그러나 sirolimus 단독요법을 지방육종에서 직접 평가한 완료 임상시험이 전무하고, 근거 대부분이 전임상·기전 연구 수준(L4)에 머물러 있어 현 단계에서 임상 개발을 진행하기에는 근거가 부족합니다.

**진행하려면 필요한 것:**
- TFDA(또는 KFDA) 수준 공식 라벨의 경고·금기 정보 확보 (현재 차단 등급 자료 공백)
- DrugBank 기반 상세 작용기전(MOA) 및 약물 분류 데이터 확보
- Sirolimus 단독 또는 rapalog 계열의 지방육종 대상 Phase 1/2 개념 증명(PoC) 시험 설계 검토
- 국내 미시판 상태 확인 및 허가 전략(신규 허가 신청 경로) 별도 검토
- (참고) LAM 적응증의 경우 이미 L1 근거가 확보되어 있어, 국내 허가 확대 관점에서 우선순위가 더 높을 수 있음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

