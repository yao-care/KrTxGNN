---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: 천식에서 기관지염으로

## 한 문장 요약

Dupilumab(Dupixent®)은 IL-4/IL-13 신호를 동시에 차단하는 완전 인간 단클론항체로, 전 세계적으로 중등도-중증 천식 및 아토피 피부염 치료에 승인되어 있습니다.
TxGNN 모델은 **기관지염(Bronchitis)**에도 효과가 있을 수 있다고 예측하며,
현재 **1건의 임상시험**과 **6편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 데이터베이스 미등재 (글로벌: 중등도-중증 천식, 아토피 피부염 등 FDA/EMA/MFDS 승인) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미등재 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

> 현재 DrugBank API 조회를 통한 공식 MOA 데이터가 확보되지 않았습니다. 알려진 정보에 따르면, dupilumab은 IL-4 수용체 알파(IL-4Rα)를 표적으로 하는 완전 인간 IgG4 단클론항체로, IL-4와 IL-13 두 사이토카인의 신호 전달을 동시에 차단합니다. 이 기전은 FDA(2017), EMA(2017), 한국 MFDS에서 중등도-중증 아토피 피부염 및 천식 적응증으로 승인받은 근거가 됩니다.

IL-4와 IL-13은 Th2(2형) 면역 반응의 핵심 매개체로서, 기도 내 호산구 침윤, 점액 과다분비, IgE 계급 전환, 기도 리모델링을 유도합니다. **기관지염과 천식은 상하 기도 연속대(united airway disease)** 개념 안에서 공통된 Type 2 염증 기전을 공유합니다. 특히 **호산구성 기관지염(eosinophilic bronchitis)** 및 **소성 기관지염(plastic bronchitis)** 표현형에서는 IL-4/IL-13 과발현이 기도 점액 과다분비와 기도 리모델링의 주요 원인으로 지목됩니다.

소아 소성 기관지염에서 dupilumab 효과를 보고한 증례 시리즈(PMID 38488768)가 이 가능성을 최초로 제시하고 있으며, 비용종 없는 만성 비부비동염(CRSsNP)을 대상으로 한 Phase 2 임상시험(NCT04362501)은 상하 기도 Type 2 염증 전반에 걸친 dupilumab의 잠재적 효능을 간접 지지합니다. 다만, 기관지염을 직접 대상으로 한 무작위대조시험은 현재 존재하지 않으며, 표현형 선별(호산구 수, FeNO 등)을 전제로 한 탐색적 연구가 선행되어야 합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | 완료 | 33 | 비용종 없는 만성 비부비동염(CRSsNP) 대상 dupilumab 임상 효능 평가. 상하 기도 Type 2 염증 연속대 맥락에서 기관지염과의 기전적 연관성을 간접 지지하며, 다양한 질환 내형(endotype) 정보 제공 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | RCT 개방 연장 (TRAVERSE) | Lancet Respir Med | 중등도-중증 천식에서 dupilumab 장기 안전성·효능 확인 — 1년 이상 연장 치료 후에도 악화 감소 및 폐기능 개선 지속 |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | 체계적 문헌고찰·메타분석 | J Asthma | 비조절 천식에서 dupilumab RCT 데이터 통합 분석 — 연간 급성 악화율 감소 및 FEV1 개선 확인 |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | 종합 리뷰 | Tuberc Respir Dis | COPD 급성 악화 예방을 위한 약물치료 종합 검토 — dupilumab 포함 신규 생물학적 제제의 역할 논의 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | 내러티브 리뷰 | Expert Opin Pharmacother | 흡연 유발 만성 기관지염·폐기종 동반 천식(천식-COPD 중복) 관리 과제 논의 — 주요 임상시험에서 배제된 집단의 치료 불확실성 기술 |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | 증례 시리즈 | Pediatr Pulmonol | 호산구성 소아 소성 기관지염에서 dupilumab 포함 신규 치료 효과 보고 — **기관지염에 대한 직접 적용의 최초 임상 근거** |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | 임상 영상 연구 | Chest | 프레드니솔론 의존성 천식에서 항-T2 생물학적 치료 후 MRI로 폐 환기 결손 개선 확인 — Type 2 차단이 기도 폐쇄를 역전시킴을 시각적으로 입증 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question**

**사유:**
기관지염에 대한 기전적 타당성(IL-4/IL-13 경로를 통한 호산구성 기도 염증 억제)은 충분하나, 현재 근거는 간접 지지 수준(L3)에 머물러 있으며 기관지염을 주요 대상으로 한 무작위대조시험이 존재하지 않습니다. 호산구성·소성 기관지염 표현형에 대한 표현형 선별 기준이 확립된 후 탐색적 임상시험 진입을 고려할 수 있습니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 공식 MOA 데이터 확보 (현재 데이터 공백)
- 한국 MFDS 허가 현황 및 급여 기준 재확인 (한국 MFDS 데이터베이스 직접 조회 필요)
- 호산구성 기관지염 / 소성 기관지염 표현형 선별 기준 개발 (혈중 호산구 수 ≥300/μL, FeNO ≥25 ppb, 혈청 IgE 상승 등 Type 2 바이오마커 활용)
- 기관지염을 직접 대상으로 하는 탐색적 Phase 2 임상시험 설계
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

