---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: 염증성 질환에서 斑禿으로

## 한 문장 요약

Betamethasone은 강효 합성 글루코코르티코이드(부신피질호르몬)로, 다양한 전신 및 국소 염증성·자가면역 질환의 치료에 사용됩니다. TxGNN 모델은 **斑禿(Alopecia Areata)**에 효과가 있을 수 있다고 예측하며 (예측 점수 99.97%), 현재 **7건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 염증성·자가면역 질환 (국내 미허가) |
| 예측 신규 적응증 | 斑禿 (Alopecia Areata) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 기반의 공식 작용 기전(MOA) 데이터는 확보되지 않았습니다. 그러나 Betamethasone은 강효 합성 글루코코르티코이드(GR-α 작용제)로 널리 알려져 있으며, GR-α 활성화를 통해 NF-κB 및 AP-1 경로를 억제하고, IL-1β·TNF-α·IFN-γ 등 염증성 사이토카인의 전사를 차단합니다.

斑禿은 CD8⁺ T 세포가 모낭을 자가면역으로 공격하는 비반흔성 탈모 질환으로, 모낭 주변에 IFN-γ/IL-15/JAK-STAT 신호 축이 고밀도로 활성화됩니다. Betamethasone의 GR-α 매개 면역억제 작용은 이 모낭 주변 염증 침윤을 직접 억제하고, 손상된 모낭 "면역 특권(immune privilege)" 미세환경을 회복시키는 기전과 정합합니다.

투여 방식 측면에서, 구강 미니펄스(oral mini-pulse, 주 1회 고용량) 요법은 HPA 축 억제 위험을 최소화하면서 치료 효과를 유지할 수 있는 현행 주요 임상 전략으로, 다수의 RCT에서 중등도~중증 斑禿 환자에서 유의한 발모 반응이 확인되었습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | 완료 | 60 | 중등도~중증 斑禿에서 azathioprine 주간 펄스 vs. betamethasone 구강 미니펄스 직접 비교; betamethasone에 대한 최고 등급 직접 RCT 근거 |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | 완료 | 40 | 斑禿에서 국소 5% 미녹시딜 + 강효 국소 코르티코스테로이드 병용 vs. 병변내 트리암시놀론 주사 효능 비교 |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | 완료 | 50 | 국소형 斑禿에서 국소 betamethasone vs. latanoprost 무작위 비교; 두 약제 간 첫 직접 비교 연구 |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | 불명 | 59 | 국소형 斑禿에서 국소 cetirizine 1% vs. betamethasone valerate 0.1% 효능·안전성 직접 비교 |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | 불명 | 60 | 반상형 斑禿에서 betamethasone valerate 0.1%를 대조군으로 하는 국소 pentoxifylline 2% 및 metformin 10% 비교; 안전성 자료 포함 |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | 모집 중 | 250 | Central Centrifugal Cicatricial Alopecia(CCCA) 다기관 전향적 치료 결과 연구 (斑禿 아님, 간접 참고) |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | 불명 | 30 | CCCA에서 clobetasol propionate 0.05% 폼 안전성·효능 연구 (斑禿 아님, 간접 참고) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 네트워크 메타분석 | Cochrane Database Syst Rev | 斑禿 치료 옵션(면역억제제·접촉 면역요법 등) 네트워크 메타분석; 전체 근거 지형 제시 |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | RCT | Cureus | 중등도~중증 斑禿에서 구강 betamethasone 미니펄스의 효능·안전성 전향적 평가 |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | 斑禿에서 미세침 경피를 통한 compound betamethasone 전달 RCT; 병변내 주사 대비 통증 감소 |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | 斑禿에서 cyclosporine vs. betamethasone 미니펄스 무작위 병렬군 비교 (n=60) |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iran J Pharm Res | 중증 斑禿에서 구강 betamethasone 펄스 vs. methotrexate vs. 병용 이중맹검 RCT (n=36); betamethasone 단독 vs. 병용 효능 비교 |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | RCT | Cureus | 斑禿에서 국소 betamethasone dipropionate vs. minoxidil 효능 직접 비교 |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | RCT | Arch Dermatol Res | 斑禿에서 분획 CO₂ 레이저 단독 vs. betamethasone valerate 병용 치료 효능·안전성 비교 (n=30) |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | 체계적 문헌고찰 | Dermatol Pract Concept | 斑禿에서 코르티코스테로이드 펄스 요법의 효능·재발률·부작용·예후인자 종합 검토 |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | J Dermatol Treat | 국소형 斑禿에서 병변내 betamethasone vs. triamcinolone 동일 환자 내 무작위 비교; betamethasone 병변내 사용 근거 최초 RCT |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | 비교 연구 | Dermatol Ther | 斑禿에서 latanoprost vs. minoxidil·betamethasone 등 6개 군 이중맹검 무작위 비교 (n=108) |

---

## 한국 시판 정보

현재 한국 내 Betamethasone 허가 기록이 없습니다 (허가증 0건, 미시판). 국제적으로는 경구제, 국소제(크림·연고·로션), 주사제 등 다양한 제형으로 광범위하게 허가·시판되고 있습니다. 구체적인 허가 정보 및 투여 용량은 각국 공식 의약품 허가 자료를 참조하시기 바랍니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Cochrane 네트워크 메타분석, 완료된 Phase 2 RCT(NCT06786689)를 포함한 다수의 임상시험과 문헌이 betamethasone의 斑禿 치료 효능을 지지합니다. 구강 미니펄스 방식은 현재 임상에서 검증된 투여 전략이나, 한국 공식 허가 데이터 및 안전성 정보가 미확보 상태이므로 모니터링 체계를 갖춘 조건부 진행이 권장됩니다.

**진행하려면 필요한 것:**
- 공식 작용 기전(MOA) 데이터 확보 (DrugBank API 조회, DG002 해소)
- 허가사항 안전성 정보(경고·금기) 확보 (TFDA/MFDS 仿單 PDF 다운로드 및 파싱, DG001 해소)
- 투여 경로별(구강 미니펄스 / 국소 / 병변내) 이점-위험 비교 분석 수행
- HPA 축 억제·감염 위험·대사 이상 등 장기 코르티코스테로이드 부작용에 대한 모니터링 계획 수립

---
> **면책 조항**: 본 보고서는 연구 참고용으로만 작성되었으며, 의료 조언을 구성하지 않습니다. 모든 약물 재창출 후보는 임상 검증 후 적용되어야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

