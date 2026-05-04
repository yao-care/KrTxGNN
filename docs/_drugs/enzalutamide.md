---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Enzalutamide: 거세 저항성 전립선암에서 남성 생식기 종양으로

## 한 문장 요약

Enzalutamide는 강력한 2세대 안드로겐 수용체(AR) 신호 억제제로, 전 세계적으로 전이성·비전이성 거세 저항성 전립선암 치료에 사용되고 있으나 현재 한국에는 시판 허가가 없는 상태입니다. TxGNN 모델은 총 7개 적응증을 예측하였으며, 이 중 **남성 생식기 종양(Male Reproductive Organ Cancer)**이 임상 근거 수준 L1로 가장 높게 평가되어 본 보고서의 주요 분석 대상으로 선정되었습니다. **50건 이상의 임상시험**과 **20편의 문헌**이 이를 강력히 지지하며, 아시아 환자를 포함한 Phase 3 RCT가 다수 완료된 상태입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 거세 저항성 전립선암 (글로벌 허가 기반; 국내 미허가) |
| 예측 신규 적응증 | 남성 생식기 종양 (Male Reproductive Organ Cancer) |
| TxGNN 예측 점수 | 99.51% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank에 등록된 상세 MOA 데이터는 없으나, 임상시험 및 문헌 근거에 기반하면 Enzalutamide는 **3중 기전의 AR 신호 경로 억제제**입니다. ① AR과 리간드(안드로겐)의 결합 차단, ② AR의 핵 내 전위(nuclear translocation) 억제, ③ AR의 DNA 결합 차단을 통해 AR 신호 전달을 다단계로 봉쇄합니다. 이는 1세대 AR 길항제인 비칼루타미드보다 월등히 강력하며, 거세 후에도 잔존하는 AR 활성화 경로를 직접 타격합니다.

전립선암을 포함한 남성 생식기 종양은 안드로겐 의존적 성장을 핵심 특징으로 합니다. Enzalutamide는 이 경로를 다단계로 봉쇄하여, 화학요법 미경험 mCRPC, 비전이성 CRPC(nmCRPC), 전이성 호르몬 감수성 전립선암(mCSPC) 등 다양한 병기에서 효능이 확인되었습니다. PROSPER 연구(NCT02003924, n=1,401)에서는 nmCRPC 환자의 전이 무병 생존(MFS)을 HR≈0.29 수준으로 획기적으로 개선하였으며, 아시아 특정 Phase 3 연구(NCT02294461, n=395)는 한국 환자를 포함한 코호트에서 직접적인 임상 근거를 제공합니다.

AR-V7 변이에 의한 내성, 골 미세환경과의 상호작용, 신경내분비 분화 경로 등 내성 기전에 대한 활발한 연구가 병용 요법 개발로 이어지고 있습니다. AR 신호 경로에 기반한 명확한 치료 기전과 풍부한 임상 데이터는 남성 생식기 종양에 대한 TxGNN 예측의 높은 타당성을 뒷받침합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02003924](https://clinicaltrials.gov/study/NCT02003924) | Phase 3 | 완료 | 1,401 | **PROSPER**: 비전이성 거세 저항성 전립선암(nmCRPC)에서 enzalutamide vs 위약 — 전이 무병 생존(MFS) HR≈0.29로 획기적 개선, 글로벌 허가의 핵심 피벗 근거 |
| [NCT02294461](https://clinicaltrials.gov/study/NCT02294461) | Phase 3 | 완료 | 395 | **아시아 다국가 이중맹검 RCT**: 화학요법 미경험 전이성 mCRPC에서 PSA 진행까지의 시간 유의하게 개선 — 한국을 포함한 아시아 환자 직접 근거 |
| [NCT05352178](https://clinicaltrials.gov/study/NCT05352178) | Phase 3 | 진행 중 | 873 | 올리고전이성 호르몬 감수성 전립선암에서 MDT(전이 지향 치료) + 단기 ADT ± enzalutamide가 다발성 전이 무병 생존 및 mCRPC 무진행 생존에 미치는 영향 검증 중 |
| [NCT02288247](https://clinicaltrials.gov/study/NCT02288247) | Phase 3 | 완료 | 688 | 화학요법 미경험 mCRPC에서 enzalutamide 진행 후 docetaxel 추가 시 enzalutamide 지속 여부 — 대규모 순차 치료 전략 및 장기 안전성 데이터 확보 |
| [NCT01867333](https://clinicaltrials.gov/study/NCT01867333) | Phase 2 | 완료 | 57 | 전이성 CRPC에서 PROSTVAC 백신 + enzalutamide vs enzalutamide 단독 — 면역·AR 이중 억제 기전의 시너지 탐색, 병용 요법 방향성 제시 |
| [NCT01664923](https://clinicaltrials.gov/study/NCT01664923) | Phase 2 | 완료 | 396 | **STRIVE**: 1차 ADT 실패 전립선암에서 enzalutamide vs bicalutamide 무작위 이중맹검 비교 — enzalutamide의 우월한 임상적 유익 확인 |
| [NCT03103724](https://clinicaltrials.gov/study/NCT03103724) | Phase 2 | 완료 | 68 | 내장 전이를 동반한 mCRPC에서 enzalutamide의 3개월 질병 조절률(DCR) 및 AR-V7 내성 마커의 임상적 역할 탐색 |
| [NCT03809000](https://clinicaltrials.gov/study/NCT03809000) | Phase 2 | 진행 중 | 188 | **STEEL**: 전립선 절제술 후 PSA 재발에서 구제 방사선 + 표준 ADT vs 강화 ADT(enzalutamide 추가) 비교 — 무진행 생존 개선 여부 검증 |
| [NCT02278185](https://clinicaltrials.gov/study/NCT02278185) | Phase 2 | 완료 | 19 | 호르몬 감수성 전립선암에서 enzalutamide vs 표준 ADT의 대사 합병증(대사 증후군) 발생 비교 — 장기 안전성 및 대사 프로파일 보완 |
| [NCT03297385](https://clinicaltrials.gov/study/NCT03297385) | Phase 2 | 완료 | 50 | 전립선 절제술 전 3개월 neoadjuvant enzalutamide 투여: 수술 절제연 상태 및 AR/DNA 상호작용, 유전자 발현 변화를 통한 분자 기전 분석 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | Narrative Review | JAMA | 전립선암 진단·치료 전반을 다룬 권위 있는 리뷰; enzalutamide 포함 ARSI의 임상적 위치와 치료 체계 정립 |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Narrative Review | Trends Cancer | 진행성 전립선암 치료 최신 동향; enzalutamide, abiraterone 등 다중 승인 약제의 병기별 사용 전략 요약 |
| [37844613](https://pubmed.ncbi.nlm.nih.gov/37844613/) | 2023 | Translational | Nature | 골수 골수세포 화학주성 억제를 통한 전립선암 치료 내성 역전 — enzalutamide 내성 극복 병용 전략 제시 |
| [29460922](https://pubmed.ncbi.nlm.nih.gov/29460922/) | 2018 | Mechanistic Review | Nat Rev Urol | AR 억제제 치료 후 세포 가소성 및 신경내분비 분화에 의한 AR 독립적 내성 기전 — enzalutamide 내성 이해의 핵심 문헌 |
| [34752846](https://pubmed.ncbi.nlm.nih.gov/34752846/) | 2022 | Mechanistic/Translational | Cancer Lett | 골 전이 미세환경(PTH1R-TGFBR2 경로)에서 enzalutamide 내성 발생 기전 규명 — 내성 극복 병용 전략 시사 |
| [32989253](https://pubmed.ncbi.nlm.nih.gov/32989253/) | 2020 | Review/Mechanistic | Oncogene | AR-V7 splice variant이 enzalutamide/abiraterone 내성의 단순 마커인지 기능적 드라이버인지 검증 — 정밀 의학적 환자 선택 기준 제공 |
| [31614208](https://pubmed.ncbi.nlm.nih.gov/31614208/) | 2020 | Review | J Steroid Biochem | 전립선암에서 안드로겐 내분비 형성(intracrinology) 재조명; DHEA→안드로겐 전환 경로와 AR 억제제 치료의 합리적 근거 |
| [34489465](https://pubmed.ncbi.nlm.nih.gov/34489465/) | 2021 | Basic Research | Nat Commun | 단일세포 ATAC/RNA 시퀀싱으로 enzalutamide 치료 반응·내성 관련 전존재(pre-existing) 및 치료 지속 세포 아군 규명 |
| [33542074](https://pubmed.ncbi.nlm.nih.gov/33542074/) | 2021 | Basic Research | Clin Cancer Res | Enzalutamide 내성 발생 시 BCL-2·IKKB 의존성 확인 — BCL-2 억제제 병용을 통한 내성 극복 전략 제시 |
| [33483372](https://pubmed.ncbi.nlm.nih.gov/33483372/) | 2021 | Preclinical | Cancer Res | 페롭토시스(ferroptosis) 유도제가 진행성 전립선암(enzalutamide 내성 포함)에서 새로운 치료 접근법으로 기능함을 전임상 모델에서 입증 |

---

## 세포독성

Enzalutamide는 항종양제이나, 전통적 세포독성 화학요법제(cytotoxic agent)가 아닌 **표적 치료제(안드로겐 수용체 신호 억제제)** 계열에 속합니다.

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 — 2세대 안드로겐 수용체 신호 경로 억제제(ARSI); 비세포독성 항종양제 |
| 골수억제 위험 | 낮음 (직접적 골수억제 없음; 경도 빈혈은 보고됨) |
| 구토 유발성 등급 | 최소 (경구 AR 길항제; 구토 유발성 매우 낮음) |
| 모니터링 항목 | CBC, 간기능(ALT/AST/총 빌리루빈), PSA, 혈압, 발작 위험도 평가 (간질·경련 병력 확인 필수) |
| 취급 방호 | 일반 경구 항암제 취급 기준 준수; 세포독성 약물 수준의 특별 방호 불필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Enzalutamide는 비전이성 및 전이성 거세 저항성 전립선암에서 3건 이상의 완료된 대규모 Phase 3 RCT를 포함한 L1 수준의 강력한 임상 근거를 보유하고 있으며, 특히 아시아 다국가 연구(NCT02294461)는 한국 환자를 포함한 직접적 효능 데이터를 제공합니다. 한국 내 미시판 상태이나 임상적 필요성과 근거 기반이 충분하여 허가 신청 절차 진행을 권장합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 상세 MOA 데이터 보완 (현재 미기재 상태)
- 한국 MFDS 허가 신청을 위한 아시아 코호트(NCT02294461) 세부 하위군 데이터 검토
- 발작, 낙상, 고혈압, 피로 등 주요 이상반응에 대한 한국어 모니터링 가이드라인 수립
- 한국 내 보험급여 등재 전략 및 경제성 평가(비용-효과 분석) 계획 수립
- 국내 병용 ADT 제형과의 약물 상호작용 데이터 확인

> **참고**: 본 Evidence Pack에는 7개의 예측 적응증이 포함되어 있습니다. 남성 생식기 종양(L1)을 제외한 나머지 6개 항목 — 전립선암/뇌암 유전적 감수성(L5), 전립선 평활근종(L5), Brenner 종양(L5), 전립선 섬유종(L5), 양성 생식계 종양(L4), 양성 전립선 엽상 종양(L5) — 은 모두 Hold 또는 Research Question 단계로, 임상 전 또는 기전 검증이 선행되어야 합니다.

---
> ⚠️ 본 보고서는 연구 참고용이며 의료적 조언을 구성하지 않습니다. 모든 예측 결과는 임상 검증 후 활용되어야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

