---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Anastrozole
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

# Anastrozole: 호르몬 수용체 양성 유방암에서 여성 유방암으로

---

## 한 문장 요약

Anastrozole은 3세대 비스테로이드계 아로마타제 억제제(AI)로, 전 세계적으로 폐경 후 호르몬 수용체 양성(ER+) 유방암의 보조 치료 및 예방에 사용되고 있으나 현재 한국 내 식약처 허가 품목은 확인되지 않았습니다.
TxGNN 모델은 **여성 유방암(Female Breast Carcinoma)**에 효과가 있을 수 있다고 예측하며,
현재 **50건 이상의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 글로벌 허가: ER+ 유방암 보조 치료·예방 (한국 미허가) |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.68% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Anastrozole은 아로마타제(CYP19A1) 효소를 고선택적으로 차단하는 비스테로이드계 억제제입니다. 아로마타제는 지방 조직, 근육, 유방 등 말초 조직에서 안드로겐을 에스트로겐으로 전환하는 핵심 효소로, anastrozole이 이를 억제하면 혈청 에스트라디올(E₂) 농도가 85% 이상 감소합니다. ER+ 유방암 세포는 에스트로겐 신호에 의존해 증식하므로, anastrozole은 이 구동 인자를 제거함으로써 항종양 효과를 나타냅니다. ER 음성 유방암에는 효과가 없습니다.

글로벌 임상에서 anastrozole은 ATAC(Arimidex, Tamoxifen, Alone or in Combination) 대규모 Phase 3 RCT(9,366명)에서 tamoxifen 대비 무병생존율을 유의하게 연장하였고, IBIS-II 예방 시험(3,864명)에서는 고위험 폐경 후 여성에서 유방암 발생률을 장기적으로 낮추는 효과가 입증되었습니다. 이 두 랜드마크 연구를 포함해 복수의 완료된 Phase 3 RCT가 존재하여 L1 근거 수준이 성립됩니다.

한국 내 허가 품목 부재는 약물 효능 미입증이 아닌 국내 허가 신청 현황을 반영합니다. Anastrozole은 미국 FDA(Arimidex®), EMA, 일본 PMDA 등 주요 규제 기관에서 ER+ 유방암 치료 및 예방 목적으로 광범위하게 허가되어 있으며, TxGNN 예측 점수(99.68%)는 이 확립된 기전적 연관성과 정확히 일치합니다. 따라서 한국 내 도입 타당성은 매우 높다고 판단됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00078832](https://clinicaltrials.gov/study/NCT00078832) | Phase 3 | 완료 | 3,864 | IBIS-II: 고위험 폐경 후 여성에서 anastrozole이 위약 대비 유방암(침윤성 및 DCIS) 발생률을 유의하게 감소, 5년 이상 장기 추적에서 보호 효과 지속 확인 |
| [NCT01626222](https://clinicaltrials.gov/study/NCT01626222) | Phase 3b | 완료 | 301 | 4EVER: NSAI(anastrozole/letrozole) 치료 후 진행된 HR+ 전이성 유방암에서 everolimus+exemestane의 실세계 효능·안전성·삶의 질 평가 |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | 모집 완료 | 4,486 | POETIC: 폐경 후 HR+ 유방암에서 수술 전후 AI(anastrozole 포함) 투여가 표준 보조요법 대비 재발 감소 여부 평가; Ki67을 예측 바이오마커로 활용 |
| [NCT02246621](https://clinicaltrials.gov/study/NCT02246621) | Phase 3 | 모집 완료 | 493 | 비스테로이드계 AI(anastrozole 또는 letrozole) + abemaciclib(CDK4/6 억제제) vs. 위약 — HR+/HER2- 전이성 유방암 1차 치료 무작위 비교 |
| [NCT02918084](https://clinicaltrials.gov/study/NCT02918084) | Phase 3 | 모집 완료 | 1,000 | 폐경 후 내분비 반응성 조기 유방암에서 화학요법과 AI의 동시 투여 vs. 순차 투여 보조 치료 비교 |
| [NCT04134598](https://clinicaltrials.gov/study/NCT04134598) | Phase 3 | 모집 완료 | 926 | EUROPA: ≥70세 Luminal A형 조기 유방암에서 단독 내분비요법(anastrozole 포함) vs. 단독 방사선 치료 무작위 비교; 삶의 질 및 재발 통제 동시 평가 |
| [NCT00287534](https://clinicaltrials.gov/study/NCT00287534) | Phase 2 | 완료 | 1,059 | 조기 유방암 보조 치료에서 tamoxifen 2년 사용 후 anastrozole로 전환 vs. tamoxifen 5년 지속 — 효능 및 내약성 비교 |
| [NCT04436744](https://clinicaltrials.gov/study/NCT04436744) | Phase 2 | 완료 | 221 | Giredestrant(신규 SERD) vs. anastrozole + palbociclib 신보조 치료 비교, ER+/HER2- 조기 유방암 (anastrozole이 대조 표준 치료로 사용) |
| [NCT04188548](https://clinicaltrials.gov/study/NCT04188548) | Phase 1 | 모집 완료 | 500 | EMBER: 신규 SERD(LY3484356) 단독 또는 anastrozole 병용 — ER+ 진행성/전이성 유방암 안전성 및 효능 탐색 |
| [NCT06154590](https://clinicaltrials.gov/study/NCT06154590) | N/A | 미개시 | 100 | 조기 유방암 보조 치료에서 anastrozole vs. tamoxifen 비교; 결합 요법 중단 배경 포함한 설계 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT 장기 추적 | Lancet | IBIS-II 장기 추적: anastrozole이 고위험 여성에서 유방암 예방 효과를 5년 이상 지속적으로 유지하며 혈장 에스트로겐 수치와 예방 효과 상관관계 확인 |
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | Phase 3 RCT | Lancet | ATAC 5년 결과: anastrozole이 tamoxifen 대비 무병생존율 유의 개선(HR 0.87), 자궁내막암·혈전색전증 위험 감소, 골절·관절통 증가 |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | RCT | Lancet | IBIS-II DCIS: 폐경 후 HR+ DCIS 환자에서 anastrozole이 tamoxifen 대비 동등 이상 유방암 재발 억제 효과, 특정 부작용 프로파일 상이 |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | 메타분석 | Oncotarget | RCT 메타분석: anastrozole vs. tamoxifen 생존 이익 종합 분석, 무병생존 우위 확인 및 부작용 프로파일 비교 제시 |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | 약물 리뷰 | Expert Opin Drug Safety | anastrozole 안전성 프로파일 종합 정리: tamoxifen 대비 우수한 무병생존율, 복수 RCT 결과 기반 |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | 체계적 문헌고찰 | Rev Assoc Med Bras | anastrozole의 유방암 화학예방 및 치료에서의 PK/PD 특성, 개인 간 변이, 임상 근거 체계적 정리 |
| [32701512](https://pubmed.ncbi.nlm.nih.gov/32701512/) | 2020 | GWAS 분석 | JCI Insight | 아로마타제 억제제 약물유전체학: CSMD1 SNP와 anastrozole 치료 후 원격 재발 위험 연관, 추가 작용 기전(면역 조절) 제시 |
| [16761927](https://pubmed.ncbi.nlm.nih.gov/16761927/) | 2006 | 전문가 리뷰 | Expert Rev Anticancer Ther | anastrozole 최신 임상 개발 현황 및 ATAC 시험 심층 분석, 보조 치료에서 tamoxifen 대체제로의 위상 정립 |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | 서술적 리뷰 | Oncology | 진행성 → 조기 → 예방 전 스펙트럼에서 anastrozole의 역할: 2차 치료, ATAC 결과, IBIS-II 예비 데이터 종합 |
| [12113022](https://pubmed.ncbi.nlm.nih.gov/12113022/) | 2001 | 약리학 리뷰 | Expert Rev Anticancer Ther | anastrozole의 약리학적·임상적 프로파일 정립: 작용 기전, PK/PD, 초기 Phase 2/3 근거, tamoxifen 대비 내약성 장점 |

---

## 한국 시판 정보

현재 한국 식품의약품안전처(MFDS)에 등록된 anastrozole 허가 품목이 확인되지 않습니다. Anastrozole은 AstraZeneca의 Arimidex® 브랜드명을 포함하여 미국 FDA, EMA, 일본 PMDA 등 주요 국가에서 ER+ 유방암 보조 치료 및 고위험군 예방 목적으로 허가되어 있습니다. 한국 내 미허가 상태는 약물의 효능 미입증이 아닌 국내 허가 신청 이력이 없음을 반영합니다.

---

## 세포독성

Anastrozole은 전통적 세포독성 화학요법제가 아닌 **표적 내분비 치료제(Targeted Endocrine Therapy)**입니다. 다만 항종양 약물로서 아래 특성을 참고하시기 바랍니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (비스테로이드계 아로마타제 억제제; 세포독성 기전 없음) |
| 골수억제 위험 | 낮음 (아로마타제 억제제는 일반적으로 골수억제를 유발하지 않음) |
| 구토 유발성 등급 | 매우 낮음 (경구 투여, 오심·구토 발생률 미미) |
| 모니터링 항목 | 골밀도(BMD/DXA), 관절통·근육통, 지질 프로파일, 간기능 (장기 투여 시) |
| 취급 방호 | 임산부 또는 가임기 여성의 노출 주의; 일반 경구 항암제 취급 규정 준수 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Anastrozole은 ATAC, IBIS-II를 포함한 복수의 완료된 대규모 Phase 3 RCT에 기반하여 L1 최고 수준의 근거를 보유한 약물이며, TxGNN 예측(99.68%)이 이미 글로벌에서 확립된 기전 및 임상 적응증과 완전히 일치합니다. 한국 내 허가 품목 부재는 도입 기회를 의미하며, 기존 글로벌 임상 근거가 충분하여 추가적인 대규모 임상시험 없이도 도입 근거를 갖출 수 있습니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가 신청을 위한 안전성·효능 자료 패키지 구성 (글로벌 허가 데이터 활용 가능)
- 국내 anastrozole 제품의 인정 적응증·경고·금기 포함 한국어 허가사항 원본 확보 및 검토
- 한국 폐경 후 여성 대상 골밀도 감소 및 관절통 위험 최소화 모니터링 프로토콜 수립
- ER/PR 수용체 검사 및 폐경 상태 확인을 포함한 환자 선택 기준 명확화
- 국내 유방암 표준 치료 가이드라인(NCCN Korea 적용 여부) 내 anastrozole 위치 분석
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

