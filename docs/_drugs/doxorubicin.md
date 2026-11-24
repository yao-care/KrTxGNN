---
layout: default
title: Doxorubicin
parent: 높은 근거 (L1-L2)
nav_order: 292
evidence_level: L1
indication_count: 8
monitor_inn: "Doxorubicin"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)"]
last_modified_at: 2026-11-24
description: "Doxorubicin: 예측 신규 적응증 유잉육종 (근거 수준 L1). 기존 적응증: 악성 림프종(림프육종, 호지킨병 및 비호지킨병), 소화기암(위암, 간암, 직장암, 담낭 및 담관암…"
---

# Doxorubicin
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **8** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Doxorubicin: 허가 적응증 정보 미확인에서 유잉육종으로
{: .text-alpha }

## 한 문장 요약

Doxorubicin은 한국에서 단일성분 주사제로 허가되어 있으나, 이번 데이터에는 허가 적응증 본문이 없고 허가 문서 링크만 있어 구체적인 기존 적응증을 확인할 수 없습니다.
TxGNN 모델은 **유잉육종(Ewing sarcoma)**에 효과가 있을 수 있다고 예측하며, 이 질환을 직접 다룬 **여러 임상시험**(Phase 3 포함)과 **문헌**이 있습니다.
다만 이는 이미 표준 치료에 포함된 사용으로, 새로운 재창출이라기보다 기존 임상 근거를 확인하는 성격이 강합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 악성 림프종(림프육종, 호지킨병 및 비호지킨병), 소화기암(위암, 간암, 직장암, 담낭 및 담관암, 결장암, 췌장암), 급성골수성백혈병, 연조직골육종, 유방암, 난소암, 폐암, 기관지암, 방광암, 윌름즈종양 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201595/EE)) |
| 예측 신규 적응증 | 유잉육종 |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L1 |
| 한국 시판 현황 | 시판 중 (유효 허가 12건 / 전체 14건) |
| 허가증 수 | 14건 (유효 12건) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Doxorubicin 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “악성 세포에 대한 독소루비신염산염의 세포독성 효과 및 여러 장기에 대한 독성 효과는 독소루비신의 뉴클레오티드 염기 삽입(intercalation) 및 세포막 지질 결합 활성과 관련된 것으로 생각된다. 삽입은 뉴클레오티드 복제와 DNA 및 RNA 중합효소의 작용을 억제한다.” 영어 원문: "The cytotoxic effect of doxorubicin hydrochloride on malignant cells and its toxic effects on various organs are thought to be related to nucleotide base intercalation and cell membrane lipid binding activities of doxorubicin. Intercalation inhibits nucleotide replication and action of DNA and RNA polymerases." ([DailyMed: Oxderys (doxorubicin hydrochloride) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f280fb2e-5070-46e1-a4ed-ba191359cedd), 버전 2026-11-12; 확인일 2026-11-19). 알려진 정보에 따르면 Doxorubicin은 topoisomerase II 억제 및 DNA 삽입(intercalation)을 통해 작용하는 안트라사이클린 계열 세포독성 항암제입니다.

유잉육종에서는 VDC/IE, VAC/VAI 등 다제 병용 화학요법의 핵심 약물로 쓰입니다. 이 종양이 화학요법에 민감하다는 점과도 일치합니다. 따라서 높은 TxGNN 점수는 임상 현실과 부합하며, 새로운 발견이라기보다 확립된 표준 치료 사용을 재확인한 결과로 보는 것이 적절합니다.

## 임상시험 근거

유잉육종을 직접 대상으로 하고 Doxorubicin이 포함된 시험 중 대표적인 것을 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 완료 | 642 | 비전이성 유잉육종에서 표준 5제 요법(vincristine, doxorubicin, cyclophosphamide, ifosfamide, etoposide)에 VTC 추가 비교 |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 완료 | 278 | 비전이성 유잉육종에서 용량 강화 치료 대 표준 치료 비교 |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 완료 | 587 | 유잉육종에서 화학요법 압축 투여를 통한 강화 비교 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 활성, 모집 종료 | 312 | 전이성 유잉육종에서 다제 화학요법에 ganitumab 추가 |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 불명 | 1200 | EURO-E.W.I.N.G.99, 화학요법 및 방사선·줄기세포이식 비교 |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | 조기 종료 | 46 | 고위험 유잉육종에서 VAC+dexrazoxane에 ImmTher 추가 여부 비교 |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | 완료 | 정보 없음 | 고위험 유잉육종에서 VAC+dexrazoxane에 ImmTher 추가 여부 비교 |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | 완료 | 정보 없음 | doxorubicin 포함 다제 화학요법 후 절제·방사선 치료 |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | 활성, 모집 종료 | 83 | 신규 진단 유잉육종에서 irinotecan·temozolomide 추가 (doxorubicin은 기본 요법) |
| [NCT07194044](https://clinicaltrials.gov/study/NCT07194044) | Phase 1 | 모집 중 | 15 | 전이성 유잉육종 일정 최적화 접근 |

위 Phase 3 시험들은 대부분 doxorubicin 포함 표준 요법을 기반으로 다른 요소(추가 약물, 투여 간격, 용량)를 비교한 것입니다. Doxorubicin 단독 효과를 분리해 평가한 시험은 아닙니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 신규 진단 유잉육종·원시신경외배엽종양에서 표준 화학요법에 ifosfamide·etoposide 추가 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012, 신규 진단 유잉육종에서 두 가지 화학요법 요법 비교 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | 전이성 유잉육종에서 ganitumab과 간격 압축 화학요법 |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | 국소 유잉육종에서 간격 압축 화학요법의 효과 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT 프로토콜 | Trials | EURO EWING 2012 프로토콜 |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | 용량강도 분석 | J Natl Cancer Inst | 골육종·유잉육종에서 doxorubicin 용량강도와 반응·예후의 관계 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review | Cancer | 유잉육종 관리에 대한 국가 종양위원회 합의 권고안 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | 유잉육종의 현재 치료와 향후 접근 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | 유잉육종 개괄 |
| [30231396](https://pubmed.ncbi.nlm.nih.gov/30231396/) | 2018 | Review | ASCO Educ Book | 안트라사이클린 심독성의 예측과 예방 (소아 유잉육종 치료 포함) |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199201595 | 한국유나이티드염산독소루비신주(수출명:AdrosalforInj.10mg,AdricinforInj.10mg,AxibinforInj.10mg,Doxo… | 적등색의 케익상의 동결건조분말이 충진된 무색 바이알 | 한국유나이티드제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201595/EE) | 유효 |
| 199000353 | 일동아드리아마이신피.에프.에스.주사액10밀리그램(독소루비신염산염) | 염산독소루비신의 액상의 주사제 | 일동제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199000353/EE) | 유효 |
| 199806569 | 케릭스주사(리포좀화한독소루비신염산염) | 반투명한 빨간색의 리포좀화 한 수성현탁액이 무색투명한 바이알에 든 주사제 | 주식회사박스터코리아 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199806569/EE) | 유효 |
| 199001007 | 에이디마이신주사액(독소루비신염산염) | 적색의 등명한 액이든 바이알 주사제 | (주)보령 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199001007/EE) | 유효 |
| 199203366 | 독소루빈주사0.2%(독소루비신염산염) | 적등색의 투명액이 든 바이알 | (주)한독테바 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199203366/EE) | 유효 |

위 표는 허가 14건 중 5건입니다.

<!-- licenses:end -->

대표 허가는 위 표와 같습니다.

<!-- review:begin kr-lic-20261105-doxorubicin-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “총 12건이 모두 단일성분이며 유효 상태입니다. 이 중 수출용 허가도 여럿 포함되어 있습니다. 위 표는 대표 5건만 나열한 것입니다.” 삭제: 허가 건수나 상태가 성분 기준으로 다시 맞춘 2026-11-05 기준 식품의약품안전처(nedrug) 허가 자료와 맞지 않습니다. 현재 허가 건수와 상태는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261105-doxorubicin-1 -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (안트라사이클린 계열, topoisomerase II 억제제) |
| 골수억제 위험 | 고 |
| 구토 유발성 등급 | 중~고 |
| 모니터링 항목 | CBC(분류 포함), 간기능, 신기능, 심기능(심초음파 등) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

이 분류는 이번 데이터에 직접 기재된 내용이 아니라 약물 계열에 근거한 일반적 평가입니다. 자세한 내용은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 이 중 주요(Major) 상호작용은 다음과 같습니다.
  - Dolasetron
  - Cisapride
  - Papaverine
- 중등도(Moderate) 상호작용에는 ondansetron, granisetron, palonosetron, aprepitant, rolapitant, dexamethasone, clarithromycin, levofloxacin 등이 있습니다. 항구토제 및 QT 연장 관련 약물이 다수 포함되어 있습니다.
- 경미한(Minor) 상호작용으로는 ascorbic acid, metronidazole 등이 있습니다.

경고 및 금기 정보는 허가사항을 참조하세요. 안트라사이클린 심독성은 문헌에서도 주요 이슈로 언급됩니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유잉육종을 직접 다룬 완료된 Phase 3 시험이 여러 건 있고, Doxorubicin은 표준 다제 화학요법의 구성 약물입니다. 다만 허가 적응증 본문, 작용 기전, 경고·금기 정보가 없어 한국 허가 범위에 이 질환이 포함되는지 확인되지 않았습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항 PDF를 내려받아 적응증, 경고, 금기 확인
- DrugBank 등에서 작용 기전 데이터 보완
- 누적 용량에 따른 심독성 모니터링 계획 수립
- 한국 허가 적응증에 유잉육종이 포함되는지 확인하고, 포함되지 않으면 허가 외 사용 절차 검토

### 참고: 기타 예측 질환 (간략)

| 예측 질환 | TxGNN 점수 | 근거 수준 | 권고 |
|---------|-----------|---------|------|
| 폐 태아성 고분화 선암 | 0.9986 | L5 | Hold |
| 원발성 폐 림프종 | 0.9985 | L5 | Research Question |
| 폐 모세포종 | 0.9985 | L3 | Proceed with Guardrails |
| 단핵구성 백혈병 | 0.9974 | L5 | Hold |
| 질 포도상 배아성 횡문근육종 | 0.9972 | L5 | Hold |
| 뇌수막 주변 배아성 횡문근육종 | 0.9971 | L5 | Hold |
| 횡문근육종 | 0.9970 | L1 | Proceed with Guardrails |

원발성 폐 림프종, 폐 모세포종, 단핵구성 백혈병 등은 해당 질환을 직접 대상으로 한 doxorubicin 시험이 제시되지 않아 근거 수준을 L5로 조정했습니다. 횡문근육종도 제시된 Phase 3 시험들이 주로 연부조직육종 전반을 다룬 것이어서, 이 질환을 직접 연구한 근거가 충분한지 추가 검토가 필요합니다.

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-24 | 삭제: “총 12건이 모두 단일성분이며 유효 상태입니다. 이 중 수출용 허가도 여럿 포함되어 있습니다” | 정정 (2026-11-24 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Oxderys (doxorubicin hydrochloride) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f280fb2e-5070-46e1-a4ed-ba191359cedd) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

