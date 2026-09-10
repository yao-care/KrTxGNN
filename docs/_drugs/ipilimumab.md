---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ipilimumab: 흑색종 면역치료에서 비피부형 흑색종으로

## 한 문장 요약

Ipilimumab은 anti-CTLA-4 단일클론항체로, 기존에는 흑색종(피부형) 면역치료의 핵심 약제로 사용되어 왔습니다.
TxGNN 모델은 **비피부형 흑색종(Non-cutaneous Melanoma, 포도막·점막 흑색종 등)**에도 효과가 있을 수 있다고 예측하며,
현재 **50건의 임상시험**과 **5편의 문헌**이 이 방향을 부분적으로 지지합니다.
다만 비피부형 아형에 특이적인 근거는 아직 제한적입니다.

> 참고: TxGNN은 이보다 높은 점수(99.06%)로 **choroideremia(맥락막결손증)**도 예측했으나, 관련 임상시험·문헌이 전혀 없고 면역관문억제제의 알려진 안구 관련 이상반응(포도막염 등)과 기전상 상충되어 근거팀 자체 평가에서 **Hold**로 판정되었습니다. 이에 본 보고서는 실질적 근거가 확보된 비피부형 흑색종을 중심으로 작성합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 흑색종(피부형) — 국내(한국) 허가 자료 없음(미출시) |
| 예측 신규 적응증 | 비피부형 흑색종 (Non-cutaneous Melanoma) |
| TxGNN 예측 점수 | 99.02% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

공식 DrugBank MOA 필드는 비어 있으나(데이터 미확보), 근거 자료에 따르면 Ipilimumab은 anti-CTLA-4 단일클론항체로, T세포의 억제성 공동자극 신호(CTLA-4)를 차단하여 항종양 면역반응을 활성화합니다. 이 기전은 흑색종(피부형 포함) 면역치료의 기존 약리학적 기반이며, 이론적으로는 흑색종의 다른 조직학적 아형(포도막·점막 흑색종 등 비피부형)에도 동일하게 적용될 수 있습니다.

다만 비피부형 흑색종, 특히 포도막 흑색종은 종양변이부담(TMB)이 낮고 면역미세환경이 피부형과 다르며, checkpoint inhibitor에 대한 반응률이 일반적으로 피부형보다 낮은 것으로 알려져 있습니다. 따라서 기전상 외삽은 가능하나 아형별 반응 차이를 고려한 신중한 해석이 필요합니다. 실제로 근거로 확보된 임상시험 대부분은 흑색종 일반 집단(피부형 위주)을 대상으로 하며, 비피부형에 특이적으로 설계된 대규모 시험은 아직 부족합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00324155](https://clinicaltrials.gov/study/NCT00324155) | Phase 3 | 완료 | 681 | 미치료 Stage III/IV 흑색종에서 Dacarbazine+Ipilimumab vs Dacarbazine+위약 비교(피벗 시험, 아형 특이적이지 않음) |
| [NCT03068455](https://clinicaltrials.gov/study/NCT03068455) | Phase 3 | 완료 | 1844 | 완전절제 Stage IIIb/c/d~IV 흑색종에서 보조요법으로 Nivolumab+Ipilimumab vs Nivolumab 단독 비교 |
| [NCT02339571](https://clinicaltrials.gov/study/NCT02339571) | Phase 2/3 | 진행 중 | 600 | 절제불가 Stage III/IV 흑색종에서 Nivolumab+Ipilimumab±Sargramostim 병용 효과 평가 |
| [NCT01783938](https://clinicaltrials.gov/study/NCT01783938) | Phase 2 | 완료 | 138 | 진행성/전이성 흑색종에서 Nivolumab 후속 Ipilimumab 순차 병용의 안전성·유효성 |
| [NCT04133948](https://clinicaltrials.gov/study/NCT04133948) | Phase 1/2 | 완료 | 44 | Stage III 피부형/원발불명 흑색종에서 Domatinostat+Nivolumab±Ipilimumab 선행보조요법 |
| [NCT01730157](https://clinicaltrials.gov/study/NCT01730157) | Early Phase 1 | 중단 | 6 | **간전이 포도막 흑색종(비피부형)** 환자에서 간동맥화학색전술+전신 Ipilimumab 병용 파일럿 연구 |
| [NCT02506153](https://clinicaltrials.gov/study/NCT02506153) | Phase 3 | 진행 중(모집 종료) | 1301 | 고위험 절제 흑색종 보조요법으로 고용량 인터페론 또는 Ipilimumab vs Pembrolizumab 비교 |
| [NCT02905266](https://clinicaltrials.gov/study/NCT02905266) | Phase 3 | 완료 | 106 | 미치료 절제불가/전이성 흑색종에서 Nivolumab+Ipilimumab 다양한 투여 요법 비교 |
| [NCT01950390](https://clinicaltrials.gov/study/NCT01950390) | Phase 2 | 완료 | 169 | 절제불가 Stage III/IV 흑색종에서 Ipilimumab±Bevacizumab 병용 효과 |
| [NCT01323517](https://clinicaltrials.gov/study/NCT01323517) | Phase 2 | 완료 | 26 | 사지 진행성 절제불가 흑색종에서 Ipilimumab+Melphalan/Dactinomycin 국소관류 병용 |

※ 위 시험 대부분은 흑색종 일반(주로 피부형) 집단을 대상으로 하며, 비피부형에 특이적인 시험은 NCT01730157(포도막 흑색종) 정도로 제한적입니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Review | Current Cancer Drug Targets | 흑색종 보조요법 리뷰. 비피부형 흑색종은 전체 흑색종의 약 5%에 불과함을 명시 |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discovery Medicine | Anti-PD-1 단독/Ipilimumab 병용요법의 진행성 흑색종 치료 현황 정리 |
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohort | The Medical Journal of Australia | 기치료 절제불가/전이성 **피부형·포도막·점막 흑색종**에서 Ipilimumab 반응을 아형별로 비교 — 비피부형 반응률이 상대적으로 낮음을 시사 |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohort | Current Oncology | 연령별(65세 기준) Anti-PD-1±Ipilimumab 진행성 흑색종 생존 결과 비교 |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | 대장 전이 흑색종 증례 — 면역치료 관련 위장관 이상반응(천공 등) 보고 |

---

## 세포독성 (항종양약)

Ipilimumab은 세포독성 화학요법이 아닌 면역관문억제제(Immunotherapy)로 분류됩니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 (Anti-CTLA-4 면역관문억제제, 전통적 세포독성 약물 아님) |
| 골수억제 위험 | 데이터 없음 — 일반적으로 면역관문억제제는 골수억제보다 면역관련 이상반응(irAE, 대장염·간염·내분비 이상 등)이 주요 우려사항. 허가사항 경고 및 주의사항 참조 |
| 구토 유발성 등급 | 데이터 없음 — 허가사항 참조 |
| 모니터링 항목 | 간기능·갑상선/부신기능 등 면역관련 이상반응 관련 지표(구체적 모니터링 스케줄은 허가사항 참조) |
| 취급 방호 | 구체적 데이터 없음 — 항암제 표준 취급 규정 준수 권장 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Ipilimumab의 anti-CTLA-4 기전은 흑색종 면역치료의 확립된 약리학적 기반이며, 완료된 Phase 3 RCT(NCT00324155, NCT03068455 등)를 포함해 근거 수준 L2에 해당하는 임상 데이터가 존재합니다. 다만 비피부형 흑색종에 특이적인 대규모 근거는 아직 부족해 가드레일 하에 진행이 적절합니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전(MOA) 및 DrugBank 카테고리 데이터 확보
- 국내(한국) 허가사항의 경고·금기·DDI 정보 (현재 전부 데이터 갭)
- 포도막·점막 흑색종 등 비피부형 아형에 특이적인 전향적 임상시험 근거 확보
- choroideremia 예측 신호는 근거 부재 및 기전 상충으로 별도 조사 없이 Hold 유지 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

