---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin: 호지킨 림프종에서 여포성 림프종으로

---

## 한 문장 요약

Brentuximab Vedotin(BV)은 CD30 양성 종양 세포를 표적으로 하는 항체-약물 접합체(ADC)로, 국제적으로 고전형 호지킨 림프종(cHL) 및 전신성 역형성 대세포 림프종(sALCL) 치료에 사용되어 왔으나 한국에서는 현재 허가 이력이 없는 약물입니다.
TxGNN 모델은 **여포성 림프종(Follicular Lymphoma)**에 효과가 있을 수 있다고 예측하며,
현재 **3건의 유효 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고전형 호지킨 림프종 (cHL), 전신성 역형성 대세포 림프종 (sALCL) ※ 국제 기준 (한국 미허가) |
| 예측 신규 적응증 | 여포성 림프종 (Follicular Lymphoma) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Brentuximab Vedotin은 항-CD30 단클론항체(brentuximab)에 강력한 세포독성 약물인 MMAE(monomethyl auristatin E)를 접합한 ADC입니다. CD30이 발현된 종양 세포에 항체가 결합하면 항체-CD30 복합체가 세포 내로 내재화(internalization)되고, 리소좀 내 단백질 분해에 의해 MMAE가 방출됩니다. 방출된 MMAE는 미세소관 해중합(microtubule depolymerization)을 유도하여 세포 주기를 G2/M 단계에서 정지시키고 세포 자멸사(apoptosis)를 일으킵니다. 상세 MOA 데이터는 현재 DrugBank에서 확인되지 않았으나, 임상 데이터에서 ADC 기전은 잘 확립되어 있습니다.

여포성 림프종(FL)은 일반적으로 CD30 음성으로 분류되나, 전환형(transformed) 또는 대세포형(large cell) 아형에서는 종양 세포의 약 10~30%에서 CD30 이상 발현이 확인됩니다. 특히 FL이 ALCL 또는 DLBCL로 고등급 전환(Richter-analog transformation)될 때 CD30 발현이 현저히 상승하는 사례가 보고되었으며(PMID 32476657), 이 경우 BV의 기전이 직접 적용 가능합니다.

BV의 기존 적응증인 cHL(Reed-Sternberg 세포 CD30 발현율 ~100%)과 FL은 모두 B세포 림프계 종양이며, CD30 발현 서브집단에서 동일한 항-CD30 ADC 기전이 적용됩니다. 다만 FL 전체 환자군 대비 CD30 양성 비율이 낮으므로, 면역조직화학(IHC)을 통한 CD30 양성(≥1%) 확인이 환자 선택의 필수 전제 조건입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | 모집 중 | 23 | 재발/불응 여포성 림프종에서 BV + Bendamustine 병용 효능·안전성 평가. 현재 진행 중인 본 적응증 대상 가장 직접적 시험 |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | 종료 | 20 | CD30⁺ 및/또는 EBV⁺ 림프종(FL 포함) 일선 치료에서 BV + Rituximab 조합 평가. 입력 어려움으로 종료된 것으로 추정되며 Phase 1 안전성 데이터 제공 |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | 종료 | 25 | 재발/불응 CD30⁺ DLBCL에서 Rituximab + Bendamustine ± BV 무작위 대조 시험. 초기 효능·안전성 신호 제공, 종료 사유 불명으로 원시 데이터 확인 필요 |

> **참고:** 철회(Withdrawn, n=0) 시험 3건(NCT04138875, NCT02623920, NCT04795869)은 데이터 없음으로 제외하였습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | 증례 보고 | Gulf J Oncol | Grade I FL이 CD30⁺ ALK1⁻ ALCL로 전환된 환자에서 BV + 고용량 메토트렉세이트 투여 후 완전 관해(CR) 달성. FL–BV 기전 연결의 직접적 임상 증거 |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | 리뷰 | Leuk Res Reports | FL을 포함한 인돌런트 비호지킨 림프종(iNHL)에서 면역치료 전략 체계적 검토. BV의 CD30⁺ 아형 적용 가능성 언급 |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Phase 2/코호트 | Blood Adv | CD30⁺(≥5%) R/R PTCL에서 BV + gemcitabine 유도 후 BV 유지요법의 전반적 반응률(ORR) 평가 (LYSA 연구). BV ADC 기전 실증 데이터 |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | 리뷰 | Blood | PTCL 공통 아형(PTCL-NOS, ALCL, TFH 유사 림프종) 현재 및 향후 치료 접근법. BV 포함 일선 레지멘(BV-CHP) 표준화 고찰 |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | 코호트 | Adv Ther | 미치료 CD30⁺ PTCL 환자에서 BV + CHOEP 실제 임상 단기 효능 및 안전성 후향적 연구 (n 미공개) |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | 코호트 | Eur J Haematol | 재발/불응 PTCL에서 BV + ICE 복합 요법 효능 평가. BV 구제 치료 레지멘 안전성 데이터 |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | 리뷰 | Hematology ASH | 헤마톨로지 학회 교육 자료: PTCL 관리에서 BV 역할 및 신규 제제 통합 전략 |
| [40517441](https://pubmed.ncbi.nlm.nih.gov/40517441/) | 2025 | 리뷰 | Hematol Oncol | PTCL의 차세대 치료 방향: WHO/ICC 2022 분류 기반 분자 표적 치료 전략 개요 |
| [28340875](https://pubmed.ncbi.nlm.nih.gov/28340875/) | 2017 | 리뷰 | Hematol Oncol Clin NA | 혈관면역모세포 T세포 림프종(AITL)에서 BV를 포함한 신규 치료 접근법 검토. CD30 발현 연관 TFH 표현형 논의 |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | 리뷰 | Bone Marrow Transplant | 림프종 자가 이식 후 유지 치료 현황. FL에서 rituximab 유지요법 및 BV 역할 맥락 검토 |

---

## 한국 시판 정보

현재 식품의약품안전처(MFDS) 허가 이력이 없습니다. Brentuximab Vedotin은 한국에서 미허가·미시판 약물로, 국내 처방을 위해서는 희귀의약품 지정 또는 개인 통관(특례 사용) 절차가 필요합니다.

---

## 세포독성

항체-약물 접합체(ADC)로서 MMAE(monomethyl auristatin E) 세포독성 탑재체를 포함하는 항종양제에 해당합니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 항체-약물 접합체 (ADC) — MMAE 탑재 항미세소관 세포독성 제제 |
| 골수억제 위험 | 중등도 (호중구감소증, 빈혈, 혈소판감소증이 임상시험에서 흔하게 보고됨) |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC (백혈구 분류 포함), 간기능·신기능 검사, 말초신경병증 증상 (MMAE 탑재 ADC의 주요 부작용) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요. ADC 특성상 특수 취급 절차(바이오해저드 표준) 적용 권장 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ※ 현재 한국 허가 데이터 및 DrugBank 경고·금기·약물 상호작용 정보가 수집되지 않았습니다. 해외 허가사항(FDA, EMA Adcetris® 처방 정보) 검토를 권장합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
CD30⁺ 여포성 림프종 서브집단에 대한 BV의 기전적 타당성이 확립되어 있고, 현재 모집 중인 Phase 2 임상시험(NCT04587687)이 진행 중이며, 개별 증례에서 FL → CD30⁺ ALCL 전환 후 BV 완전 관해 사례가 확인된 바 있어 탐색적 임상 개발을 조건부로 진행할 수 있는 근거가 충분합니다. 단, FL 전체 집단 대비 CD30 발현율이 낮아 생체지표 기반 환자 선택 없이는 전체 임상적 이익이 제한될 수 있습니다.

**진행하려면 필요한 것:**

- **CD30 IHC 선별 기준 수립:** FL 환자 조직에서 CD30 양성(≥1% 또는 ≥10%, 기준값 합의 필요) 확인을 필수 입력 조건으로 설정
- **MOA 데이터 보완:** DrugBank API를 통해 상세 작용 기전 및 DrugBank categories 재쿼리
- **안전성 프로파일 완성:** FDA/EMA Adcetris® 허가 문서에서 경고·금기·약물 상호작용 추출
- **한국 규제 경로 검토:** 희귀의약품 지정 가능성 또는 임상시험용 의약품 수입 절차(IND) 확인
- **NCT04587687 결과 추적:** 2026년 12월 완료 예정 시험 결과 모니터링
- **전환형 FL 코호트 우선 탐색:** CD30 발현율이 높은 전환형/대세포형 FL 서브집단을 우선 연구 대상으로 설정

---

> ⚠️ **면책 조항:** 본 보고서는 TxGNN 예측 모델 및 공개 데이터베이스 기반의 연구 참고용 자료이며, 의료 행위 또는 처방의 근거로 사용될 수 없습니다. 모든 약물 재창출 후보는 임상 검증을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

