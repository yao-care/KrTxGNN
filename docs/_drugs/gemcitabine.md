---
layout: default
title: Gemcitabine
parent: 모델 예측만 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Gemcitabine: 예측 신규 적응증 여성 유방암 (Female Breast Carcinoma) (근거 수준 L5). 기존 적응증: 허가증에는 허가사항 문서 링크만 수록되어 있어 적응증 본문을 확인할 수 없음"
monitor_inn: "Gemcitabine"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "endometrial mixed adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "mucin-rich endometrial endometrioid adenocarcinoma"]
---

# Gemcitabine
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

# Gemcitabine: 허가 적응증에서 여성 유방암으로

## 한 문장 요약

Gemcitabine은 뉴클레오시드 유사체 계열의 세포독성 항암제로, 국내에서는 주사제로 20건이 허가되어 시판 중입니다. TxGNN 모델은 **여성 유방암(female breast carcinoma)**에 효과가 있을 수 있다고 예측하며, 현재 **임상시험 35건**과 **문헌 20편**이 이 방향과 관련되어 있습니다. 다만 유방암은 이미 일부 지역에서 확립된 사용처로 보이므로, 진정한 의미의 신규 재창출 후보로 보기는 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에는 허가사항 문서 링크만 수록되어 있어 적응증 본문을 확인할 수 없음 |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L1 (Phase 3 RCT 근거 있음, 아래 참고) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 (모두 유효) |
| 권장 결정 | Proceed with Guardrails |

> 근거 수준 참고: 완료된 Phase 3 RCT는 NCT00006459(젬시타빈+파클리탁셀 vs 파클리탁셀)와 NCT00093795 두 건입니다. 두 시험 모두 완료되었으나 NCT00006459는 참여자 수가 기재되어 있지 않고, NCT00093795는 젬시타빈이 세 번째 군에만 포함된 보조요법 시험입니다. 그래서 L1 판정에는 일정한 한계가 있습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이 보고서에 수집되지 않았습니다. 알려진 정보에 따르면 Gemcitabine은 뉴클레오시드 유사체로서 DNA 합성과 리보뉴클레오티드 환원효소를 억제하는 세포독성 항암제입니다. 이 기전은 빠르게 증식하는 유방 종양 세포에도 적용될 수 있습니다.

유방암에서는 파클리탁셀, 도세탁셀, 백금계 약물, 트라스투주맙 등과의 병용요법이 오래전부터 연구되어 왔습니다. 문헌 고찰에서도 전이성 유방암에서 단독요법 반응률 16~37%, 병용요법에서는 더 높은 반응률이 보고되었습니다. 다만 Gemcitabine은 이미 일부 지역에서 유방암에 사용되고 있어, TxGNN의 예측은 기존 임상 지식과 대체로 일치하는 결과로 해석됩니다.

## 임상시험 근거

관련성이 높은 시험을 선별하여 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | 완료 | 미기재 | 절제 불가능한 국소 재발성/전이성 유방암에서 젬시타빈+파클리탁셀 vs 파클리탁셀 비교 |
| [NCT00093795](https://clinicaltrials.gov/study/NCT00093795) | Phase 3 | 완료 | 4,894 | 림프절 양성 유방암 보조요법에서 TAC, dd AC→P, dd AC→P+젬시타빈 비교 |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | 불명 | 1,206 | 수술 전 요법에서 도세탁셀에 카페시타빈 또는 젬시타빈 추가 시 pCR 비교 |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase 3 | 불명 | 800 | 예후 불량 조기 유방암에서 에피루비신/사이클로포스파미드 후 파클리탁셀±젬시타빈 |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | 불명 | 미기재 | tAnGo: ER/PgR 저발현 조기 유방암 보조요법에서 젬시타빈 추가 효과 |
| [NCT00006007](https://clinicaltrials.gov/study/NCT00006007) | Phase 2 | 완료 | 59 | 전이성 유방암에서 페메트렉시드+젬시타빈 (단일군, 소규모) |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | 완료 | 50 | 전이성 유방암에서 nab-파클리탁셀+젬시타빈 |
| [NCT00244933](https://clinicaltrials.gov/study/NCT00244933) | Phase 2 | 완료 | 19 | 전이성 유방암에서 젬시타빈+제니스테인 (소규모) |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | 완료 | 30 | 안트라사이클린·탁산 치료 후 전이성 유방암에서 젬시타빈 단독 |
| [NCT07528768](https://clinicaltrials.gov/study/NCT07528768) | Phase 2 | 모집 예정 | 750 | 아프리카계 여성의 전이성 삼중음성 유방암에서 젬시타빈 vs 파클리탁셀 (2027년 시작 예정) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology (Williston Park) | 전이성 유방암에서 젬시타빈+파클리탁셀 병용; 2상 시험 221명 중 114명(52%) 반응 |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology (Williston Park) | 젬시타빈+백금계 병용의 전이성 유방암에서의 임상적 이득 |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology (Williston Park) | 젬시타빈+도세탁셀 병용 근거와 2상 결과 |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology (Williston Park) | 진행성 유방암에서 젬시타빈·안트라사이클린·탁산 병용 |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Seminars in Oncology | 단독요법 반응률 16~37%, 병용요법 및 표적치료와의 병용 |
| [14754469](https://pubmed.ncbi.nlm.nih.gov/14754469/) | 2004 | Review | Clin Breast Cancer | HER2 양성 전이성 유방암에서 젬시타빈+트라스투주맙 병용 근거 |
| [12057045](https://pubmed.ncbi.nlm.nih.gov/12057045/) | 2002 | Review | Clin Breast Cancer | 유방암 수술 전 보조요법으로서의 젬시타빈 |
| [11252883](https://pubmed.ncbi.nlm.nih.gov/11252883/) | 2001 | Review | Oncology (Williston Park) | 진행성 유방암에서 젬시타빈+비노렐빈 병용 |
| [12057039](https://pubmed.ncbi.nlm.nih.gov/12057039/) | 2002 | 전임상 | Clin Breast Cancer | 유방암·폐암 세포주에서 젬시타빈+트라스투주맙 효과 |
| [34973989](https://pubmed.ncbi.nlm.nih.gov/34973989/) | 2022 | 전임상 | Int J Biol Macromol | 젬시타빈·5-FU 탑재 MIL-100 나노복합체 약물전달체의 유방암 효과 |

## 한국 시판 정보

허가증 20건 중 주요 5건입니다. 허가 적응증 본문은 허가사항 문서 링크로만 제공되어 있어 표에는 기재하지 않았습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201506534 | 젬탄액상주 (종근당) | 액상 주사제(바이알) | 허가사항 문서 참조 |
| 201402859 | 화이자젬시타빈액상주 (한국화이자제약) | 액상 주사제(바이알) | 허가사항 문서 참조 |
| 200600254 | 젬자주200밀리그램 (보령) | 동결건조 주사제 | 허가사항 문서 참조 |
| 202401967 | 인퓨젬주10밀리그램/밀리리터 (리퓨어헬스케어) | 수액용 플라스틱 용기 주사제 | 허가사항 문서 참조 |
| 200709600 | 젬타빈주2그램 (한국유나이티드제약) | 동결건조 주사제 | 허가사항 문서 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (뉴클레오시드 유사체/항대사제) |
| 골수억제 위험 | 중등도 (백혈구감소증, 혈소판감소증, 빈혈과 연관된 금기 질환이 지식그래프에 존재) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(분류 포함), 간기능, 신기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환**(허가사항 본문이 아닌 TxGNN 지식그래프 기준): 신장 질환, 간 질환, 담낭 질환, 혈소판감소증, 감염성 질환, 빈혈, 대적혈구성 빈혈, 간질성 폐질환, 백혈구감소증, 용혈성 요독 증후군
- **약물 상호작용**: 총 100건이 확인되었습니다. 상위 목록에서 중등도는 Naltrexone, 경미한 수준은 Levofloxacin이며, 그 외 Calcitriol, Doxycycline, Pantoprazole, Metformin, Morphine 등은 등급이 미분류입니다.
- **문헌상 보고된 이상반응**: 젬시타빈 유발 망막병증 증례(2017)가 보고되어 있습니다.

허가사항의 경고 및 금기 본문은 현재 확보되지 않았으므로 허가사항을 직접 확인하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방암에서 젬시타빈+파클리탁셀을 비교한 완료된 Phase 3 RCT와 다수의 Phase 2 병용 시험, 문헌 고찰이 있어 근거는 비교적 탄탄합니다. 그러나 이미 확립된 사용처일 가능성이 높아 신규 재창출 후보로서의 새로움은 제한적이고, 허가사항 기반 안전성 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고·금기·적응증 본문) 확인 및 국내 허가 적응증에 유방암이 포함되는지 검토
- 작용 기전(MOA) 데이터 보완
- NCT00006459, NCT00093795의 결과 데이터를 확인하여 L1 판정의 타당성 검증
- 골수억제 등 혈액학적 독성 모니터링 계획 수립

**참고: 다른 예측 적응증**
순위 2~10의 예측 적응증(점막성 선암 등)은 대부분 직접적인 임상 근거가 없습니다. 직장·대장·경부·담낭 점액성 선암과 난소 관련 선암 등은 Hold 권고입니다. 자궁내막 혼합 선암과 점액성 선암은 후향 연구와 2상 시험 및 부인과 암 근거가 있어 추가 연구 질문(Research Question) 단계입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

