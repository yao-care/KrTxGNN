---
layout: default
title: Carboplatin
parent: 모델 예측만 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: 기존 허가 적응증에서 여성 유방암으로

## 한 문장 요약

Carboplatin은 DNA 교차결합을 일으키는 백금계 항암제로, 국내에 주사제 5개 허가가 유효한 상태로 시판 중입니다.
TxGNN 모델은 **여성 유방암(female breast carcinoma)**에 효과가 있을 수 있다고 예측하며, 현재 **45건의 임상시험**과 **20편의 문헌**이 이 방향과 관련되어 있습니다.
다만 유방암에서 carboplatin은 이미 삼중음성 유방암(TNBC) 등에서 사용·연구되고 있어 완전히 새로운 재창출 신호는 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 본문이 아닌 허가문서(PDF) 링크만 있어 요약할 수 없습니다. 허가사항 원문을 참조하세요. |
| 예측 신규 적응증 | 여성 유방암 (female breast carcinoma) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L1 (아래 판정 사유 참조) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 (단일 성분, 모두 유효) |
| 권장 결정 | Proceed with Guardrails |

**근거 수준 판정 사유:** 수집된 데이터에는 유방암 대상의 완료된 Phase 3 시험이 최소 3건 있습니다 (NCT00021255, NCT00047255, NCT02125344). 판정 규칙(완료된 Phase 3 RCT 2건 이상)에 따라 L1로 판정했습니다. 다만 대부분 carboplatin이 병용 요법의 일부로 포함된 시험이어서, carboplatin 단독 기여도를 보여 주는 직접 근거는 제한적입니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 carboplatin은 DNA 교차결합을 일으키는 백금계 세포독성 항암제입니다. 이 약은 여러 고형암에서 효능이 입증되어 있어, 기전상 유방암에도 적용 가능할 수 있습니다.

특히 상동재조합 결핍(HRD)이 있는 종양, 예컨대 BRCA 변이 유방암이나 삼중음성 유방암은 백금계 약물의 DNA 손상에 민감한 것으로 알려져 있습니다. 이것이 TxGNN 예측을 뒷받침하는 기전적 근거입니다. 무작위 Phase 2 시험(NCT00321633, 전이성 유전성 유방암에서 carboplatin vs docetaxel)과 선행화학요법 연구(GeparSixto, CALGB 40603)가 이 방향을 지지합니다.

주의할 점도 있습니다. 2025년 ASCO 관련 리뷰(PMID 41489230)에 따르면 조기 TNBC에서 carboplatin을 추가해도 생존 이익이 없었다는 결과(NRG-BR003)가 있습니다. HER2 양성 조기 유방암에서는 carboplatin을 생략해도 효능이 유지되고 내약성이 더 좋았다고 합니다. 따라서 유방암 전체가 아니라 아형별(TNBC, BRCA 변이 등)로 근거를 따져야 합니다.

## 임상시험 근거

유방암 관련 시험은 총 45건이며, 관련성이 높은 10건을 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | 완료 | 148 | 전이성 유전성 유방암에서 carboplatin과 docetaxel 직접 비교 (무작위) |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | 완료 | 263 | HER2 양성 진행성 유방암 1차 치료에서 docetaxel+trastuzumab에 carboplatin 추가 여부 비교 |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | 완료 | 3,222 | HER2 양성 수술 가능 유방암 보조요법에서 AC-T, AC-TH, TCH(docetaxel+carboplatin+trastuzumab) 비교 |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | 완료 | 961 | 고위험 조기 유방암 선행요법에서 용량 강화 ETC와 PM(Cb) 요법 비교 (GeparOcto) |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | 완료 | 45 | TNBC 선행요법으로 bevacizumab+docetaxel+carboplatin 평가 |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | 활성(모집 종료) | 68 | HER2 음성 수술 가능 유방암에서 carboplatin+nab-paclitaxel ± vorinostat 선행요법의 반응·바이오마커 평가 |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Phase 2 | 모집 중 | 185 | 조기 유방암 선행 전신요법에서 임상 반응과 병리학적 반응의 상관성 평가 (carboplatin은 요법의 일부) |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | 완료 | 92 | HER2 과발현 전이성 유방암 1차 치료로 paclitaxel+carboplatin+trastuzumab 평가 |
| [NCT00025688](https://clinicaltrials.gov/study/NCT00025688) | Phase 3 | 불명 | 미보고 | 65세 이상 전이성 유방암에서 주 1회 paclitaxel ± carboplatin 비교 |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | 모집 중 | 85 | 나이지리아 TNBC 환자에서 epirubicin+cyclophosphamide 후 docetaxel+carboplatin의 병리학적 완전관해율 평가 |

## 문헌 근거

20편 중 RCT를 우선하여 10편을 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT (Phase 2) | Lancet Oncol | TNBC 및 HER2 양성 조기 유방암에서 선행요법에 carboplatin 추가의 효능 평가 (GeparSixto) |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT (Phase 2) | Clin Cancer Res | Stage I-III TNBC에서 안트라사이클린 비포함·포함 carboplatin 선행요법 비교 (NeoSTOP) |
| [35044810](https://pubmed.ncbi.nlm.nih.gov/35044810/) | 2022 | RCT (Phase 2) | J Clin Oncol | TNBC 선행요법에서 carboplatin·bevacizumab 추가의 장기 성적과 유전체 상관 분석 (CALGB 40603) |
| [29501363](https://pubmed.ncbi.nlm.nih.gov/29501363/) | 2018 | RCT (Phase 3) | Lancet Oncol | TNBC 선행화학요법에 veliparib+carboplatin 또는 carboplatin 단독 추가 평가 (BrighTNess) |
| [41436191](https://pubmed.ncbi.nlm.nih.gov/41436191/) | 2025 | RCT (Phase 3) | BMJ | 고위험 조기 TNBC 보조요법에서 carboplatin 강화 요법과 표준 요법의 생존 비교 (CITRINE) |
| [41115255](https://pubmed.ncbi.nlm.nih.gov/41115255/) | 2026 | RCT (Phase 3) | J Clin Oncol | TNBC에서 taxane-안트라사이클린 선행화학요법에 백금 추가의 생존 영향 평가 |
| [29175149](https://pubmed.ncbi.nlm.nih.gov/29175149/) | 2018 | RCT (Phase 3) | Lancet Oncol | HER2 양성 유방암 선행요법에서 화학요법 포함 요법과 T-DM1+pertuzumab 비교 (KRISTINE) |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT (Phase 2b) | Nat Commun | HER2 양성 유방암에서 ARX788+pyrotinib과 표준 TCbHP(carboplatin 포함) 선행요법 비교 |
| [41489230](https://pubmed.ncbi.nlm.nih.gov/41489230/) | 2026 | Review | Cancer Investig | 조기 TNBC에서 carboplatin 추가 시 생존 이익이 없었다는 결과(NRG-BR003), HER2 양성에서 carboplatin 생략 시 효능 유지 |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | 진행성 유방암에서 paclitaxel-carboplatin 병용의 상승효과, 효능, 안전성 근거 정리 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199201568 | 카보티놀주사(카르보플라틴) | 주사제 (갈색 바이알) | [허가문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201568/EE) |
| 200004907 | 카보틴주(카르보플라틴)(수출용) | 주사제 (갈색 바이알) | [허가문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200004907/EE) |
| 200905067 | 칸플라틴주(카르보플라틴)(수출용) | 주사제 (갈색 바이알) | [허가문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200905067/EE) |
| 199101108 | 네오플라틴주(카르보플라틴) | 주사액 (갈색 바이알) | [허가문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199101108/EE) |
| 200210228 | 화이자카보플라틴주10mg/ml | 주사액 (투명 바이알) | [허가문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200210228/EE) |

5건 중 2건(카보틴주, 칸플라틴주)은 수출용 허가입니다. 제조사는 각각 한국유나이티드제약, 대한뉴팜, 한국코러스, 보령, 한국화이자제약입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (백금계 알킬화 유사 DNA 교차결합제) |
| 골수억제 위험 | 고 (혈소판감소증과 호중구감소증이 용량 제한 독성으로 알려져 있음) |
| 구토 유발성 등급 | 중~고 (고용량 투여 시 고위험으로 분류되는 경우가 많음) |
| 모니터링 항목 | CBC (분류 포함), 신기능, 간기능, 전해질 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 (조제·투여·폐기물 처리 시 보호구 착용) |

수집된 데이터에는 독성 관련 상세 정보가 없어 일반적인 약물 분류에 따라 기재했습니다. 정확한 내용은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

**약물 상호작용**: 조회된 상호작용은 총 100건이며, 상위 20건 중 대부분이 중등도(Moderate)입니다.
- **양성자 펌프 억제제**: rabeprazole, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole
- **아미노글리코사이드 계열**: kanamycin, neomycin, streptomycin
- **기타 항생제**: vancomycin, metronidazole, tinidazole (모두 중등도)
- **스타틴**: rosuvastatin, simvastatin (중등도)
- **경미(Minor)**: levofloxacin
- **등급 미상(Unknown)**: calcitriol, glimepiride, mesalazine, doxycycline, clotrimazole

경고 및 금기 항목은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방암에서는 완료된 Phase 3 시험과 다수의 무작위 Phase 2/3 문헌이 있고, 기전(HRD 종양의 백금 감수성)도 타당합니다. 그러나 효과는 아형에 따라 다릅니다. 조기 TNBC에서 carboplatin 추가의 생존 이익이 없었다는 결과와 HER2 양성에서 carboplatin을 생략해도 효능이 유지되었다는 결과가 있어, 무조건적 확대보다는 조건부 진행이 적절합니다.

**진행하려면 필요한 것:**
- 허가문서 원문에서 기존 허가 적응증과 경고·금기 확인
- 상세 작용 기전(MOA) 데이터 보강
- 대상 아형 한정(TNBC, BRCA 변이/HRD, HER2 상태)과 병기·치료 단계(선행/보조/전이성)별 근거 재정리
- carboplatin 추가 효과를 직접 비교한 Phase 3 결과(CITRINE, NRG-BR003 등)에 대한 정밀 검토
- 골수억제, 구토, 신기능 모니터링 계획과 병용약물(PPI, 아미노글리코사이드 등) 상호작용 관리 방안
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

