---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 432
evidence_level: L5
indication_count: 6
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lenalidomide: 골수형성이상증후군·다발골수종에서 골수성 백혈병(Myeloid Leukemia)으로

## 한 문장 요약

Lenalidomide는 해외에서 del(5q) 골수형성이상증후군(MDS) 관련 수혈의존성 빈혈 및 다발골수종 치료에 사용되어 온 면역조절 약물(IMiD)입니다. TxGNN 모델은 **골수성 백혈병(Myeloid Leukemia)**에도 효과가 있을 수 있다고 예측하며, 현재 **50건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다. 다만 한국에는 아직 허가·시판된 제품이 없고 안전성 자료도 확보되지 않은 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | (한국 허가 정보 없음) — 문헌상 해외 승인 기준: del(5q) MDS 관련 빈혈, 다발골수종 |
| 예측 신규 적응증 | 골수성 백혈병 (Myeloid Leukemia) |
| TxGNN 예측 점수 | 99.49% |
| 근거 수준 | L2 (완료된 Phase 2 RCT 다수 확인, AML 특이적 완료 Phase 3 RCT는 미확인) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

문헌 근거(PMID 39881283)에 따르면 Lenalidomide는 cereblon(CRBN) E3 유비퀴틴 라이게이즈 복합체에 결합하여 IKZF1/IKZF3 등 기질 단백질의 유비퀴틴화·분해를 유도함으로써 항백혈병·항골수종 효과를 나타내는 면역조절 기전을 가집니다(PMID 23316859).

MDS와 골수성 백혈병(AML)은 조혈모세포 클론 이상이라는 동일한 병태생리 축을 공유하며, 저·중등도 위험 MDS의 상당수가 시간에 따라 AML로 이행합니다(PMID 24656536). 실제로 시판후조사 임상시험(NCT02921815)은 del(5q) MDS 환자에서 Revlimid 투여 후 "AML로의 이행(Transformation to Acute Myeloid Leukemia)" 자체를 추적 관찰 항목으로 설정하고 있어, MDS-AML 스펙트럼 전반에 걸친 약리적 개입 가능성을 뒷받침합니다.

이러한 기전적 연속성 때문에 다수의 Phase 1/2 시험이 고용량 단독요법 또는 azacitidine·화학요법 병용으로 AML 환자를 대상으로 직접 진행되었으며, 계열 전반의 재창출 타당성을 강화합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2 | 완료 | 88 | 신규진단 고령 AML: 고용량 렌알리도마이드 단독 vs 순차 AZA+LEN vs AZA 단독 비교 |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Phase 2/3 | 모집 종료(진행 중) | 282 | 고위험 MDS/CMML에서 AZA+LEN vs AZA vs AZA+vorinostat 비교 |
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | 완료 | 27 | 5번 염색체 이상 동반 재발/불응 AML·고위험 MDS에서 렌알리도마이드 단독요법 |
| [NCT00546897](https://clinicaltrials.gov/study/NCT00546897) | Phase 2 | 완료 | 48 | 60세 이상 미치료 AML(5q 이상 없음)에서 안전성·유효성 |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Phase 2 | 완료 | 41 | 관해유도 화학요법 거부한 60세 이상 del(5q) AML 환자 |
| [NCT01743859](https://clinicaltrials.gov/study/NCT01743859) | Phase 2 | 완료 | 37 | 재발/불응 AML·고위험 MDS에서 AZA 순차 투여 후 렌알리도마이드 |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | 완료 | 41 | 재발/불응 AML에서 MEC 화학요법 + 렌알리도마이드 병용 |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | 완료 | 29 | 고위험 AML 관해 환자의 렌알리도마이드 유지요법 |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | 완료 | 37 | 진행성 MDS(AML 전단계)에서 렌알리도마이드 + 아자시티딘 병용 |
| [NCT02921802](https://clinicaltrials.gov/study/NCT02921802) | 해당없음(시판후조사) | 완료 | 4,626 | Revlimid 5mg 전수 시판후조사, 실사용 환경 안전성·유효성 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | American Journal of Hematology | MDS 진단·위험도분류·치료 최신 지견, AML 이행 위험 강조 |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | 체계적 문헌고찰/메타분석 | Hematology (Amsterdam) | AZA+렌알리도마이드 병용요법의 AML/MDS/CMML 효능·이상반응 메타분석 |
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | 체계적 문헌고찰/메타분석 | Cancer Management and Research | AML 치료에서 렌알리도마이드 효능·안전성 메타분석 |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | MDS 병태생리 전반 및 AML 이행(약 1/3 환자) 개관 |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opinion on Investigational Drugs | AML 신규 치료제로서 렌알리도마이드 고찰 |
| [35320468](https://pubmed.ncbi.nlm.nih.gov/35320468/) | 2022 | Review | Current Treatment Options in Oncology | IPSS 기반 위험분류에 따른 MDS 신규 치료전략 |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | 코호트 연구 | Blood | 렌알리도마이드가 TP53 변이 치료관련 골수종양(t-MN) 발생을 촉진할 가능성 — 안전성 신호 |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | 전향적 임상연구 | Haematologica | 동종이식 후 재발 MDS/AML/CMML에 AZA+렌알리도마이드+DLI(Azalena-Trial) |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Phase 1 용량증량 연구 | Bone Marrow Transplantation | 이식 후 고위험 MDS/AML 유지요법으로서 안전성·내약성 |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | 기전 연구 | Cellular & Molecular Biology Letters | KDM5C의 cereblon 안정화를 통한 AML 세포 렌알리도마이드 감수성 증강 기전 규명 |

---

## 한국 시판 정보

현재 한국에서 허가·시판 중인 Lenalidomide 제품이 없습니다 (미출시).

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적 면역조절제 (IMiD 계열, thalidomide 유사체) — 전통적 세포독성 화학요법이 아닌 cereblon(CRBN) 매개 표적 단백질 분해 기전 |
| 골수억제 위험 | 자료상 시판후조사(NCT02921802, 4,626명)와 다수 완료 임상에서 반복 추적된 항목 — 구체적 등급은 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(혈구검사), 2차 골수종양 발생 감시(TP53 변이 관련, PMID 35512188 참조) |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 골수성 백혈병 적응증은 완료된 Phase 2 RCT 다수(예: NCT01358734, NCT00360672 등)와 20편의 문헌(체계적 문헌고찰·메타분석 2편 포함)으로 뒷받침되어 기전적·임상적 타당성이 높습니다.
- 다만 한국 허가·시판 정보, 상세 MOA, 안전성(경고/금기/DDI) 자료가 전혀 확보되지 않아 곧바로 임상 적용 판단은 불가합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고·금기·DDI) 확보 — 현재 Blocking 등급 데이터 갭
- 상세 작용기전(MOA) 자료 확보 (DrugBank 등)
- 한국 내 임상시험 등록 및 국내 사용 경험 여부 확인
- 순위 2~6위 예측 적응증(비분류 MDS, 소아 불응성 혈구감소증 등)은 근거 수준이 L3~L5로 낮아 별도 Hold 권고
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

