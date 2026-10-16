---
layout: default
title: Paclitaxel
parent: 모델 예측만 (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Paclitaxel: 예측 신규 적응증 여성 유방암 (Female Breast Carcinoma) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 허가사항 링크로만 제공됨. 일반적으로 파클리탁셀은 유방암, 난소암…"
---

# Paclitaxel
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

# Paclitaxel: 항암 화학요법제에서 여성 유방암(Female Breast Carcinoma)으로

## 한 문장 요약

Paclitaxel은 미세소관을 안정화하는 항종양 화학요법제로, 한국에서 14건의 단일제 허가증이 유효하며 시판 중입니다.
TxGNN 모델은 **여성 유방암(Female Breast Carcinoma)**에 효과가 있을 것으로 예측하며, 이 예측에는 **임상시험 40건 이상**과 **문헌 19편**이 연결되어 있습니다.
다만 유방암은 이미 확립된 표준 사용 영역이므로, 이 건은 엄밀한 의미의 재창출이라기보다 기존 사용의 타당성을 확인하는 성격에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 허가사항 링크로만 제공됨. 일반적으로 파클리탁셀은 유방암, 난소암, 비소세포폐암 등 고형암에 사용됨(일반 지식 기준) |
| 예측 신규 적응증 | 여성 유방암 (Female Breast Carcinoma) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L1 (완료된 Phase 3 임상시험 다수) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 14건 (모두 유효, 단일제) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 구조화 데이터는 없습니다. 다만 관련 자료에 따르면 Paclitaxel은 미세소관을 안정화해 유사분열 방추사의 해체를 막고, G2/M기 정지와 세포자멸사를 유도합니다. 그래서 빠르게 증식하는 종양세포에 특히 효과적입니다.

유방암은 이러한 증식성 종양의 대표적인 예입니다. 탁산 계열은 보조요법, 선행화학요법, 전이성 질환 치료의 핵심 약제로 쓰입니다. 호르몬 수용체 상태와 무관하게 세포독성을 나타내므로 삼중음성 유방암에서 ER 양성 질환까지 폭넓게 적용됩니다.

따라서 이번 예측은 새로운 질환으로의 확장이 아니라, 이미 확립된 유방암 사용을 모델이 재확인한 결과로 해석하는 것이 적절합니다. 이 점이 근거 수준이 높게 나오는 이유이기도 합니다.

## 임상시험 근거

관련성이 높은 시험을 우선해 10건을 나열했습니다. Phase 3 시험은 대부분 Paclitaxel이 병용 요법의 한 축이거나 비교 대조군입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | 완료 | 정보 없음 | 절제 불가능한 국소 재발·전이성 유방암에서 Gemcitabine + Paclitaxel vs Paclitaxel 단독 비교 |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | 완료 | 632 | HER2 음성 고위험 유방암 선행요법에서 nab-paclitaxel vs 용매 기반 paclitaxel의 병리학적 완전관해율 비교(ETNA) |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | 완료 | 478 | 림프절 양성 유방암 보조요법에서 Docetaxel vs Paclitaxel 순차 투여 비교 |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | 완료 | 580 | 1차 진행성·전이성 유방암에서 Lapatinib + Paclitaxel vs Paclitaxel 단독 |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | 완료 | 652 | HER2 양성 전이성 유방암에서 탁산 + Lapatinib vs 탁산 + Trastuzumab |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | 완료 | 455 | HER2 양성 유방암 선행요법에서 Paclitaxel + Lapatinib/Trastuzumab 비교(Neo-ALTTO) |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | 완료 | 280 | HER2 양성 수술 가능 유방암에서 FEC → Paclitaxel + Trastuzumab 순서 비교 |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | 완료 | 50 | 재발·전이성 유방암에서 주 1회 Paclitaxel + Trastuzumab 병용 효능 평가 |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | 불명 | 정보 없음 | 전이성 유방암에서 Docetaxel 또는 Paclitaxel 두 가지 투여 스케줄 무작위 비교 |
| [NCT00002826](https://clinicaltrials.gov/study/NCT00002826) | Phase 2 | 완료 | 36 | 전이성 유방암에서 PSC 833을 이용한 Paclitaxel 다제내성 조절 파일럿 |

## 문헌 근거

관련성이 낮은 문헌(예: 다른 질환의 증례 보고)은 제외하고, 검토·임상시험 중심으로 선별했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | 탁산(Paclitaxel, Docetaxel)이 진행성 유방암·폐암·난소암 치료의 근거 기반 구성 요소임을 정리 |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | 유방암 및 난소암에서의 Paclitaxel·Docetaxel 허가 확대 과정 검토 |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 | Cancer | 전이성 유방암에서 Doxorubicin + Paclitaxel 병용의 효능·독성 평가, 선행 보조 안트라사이클린 치료 이력의 중요성 |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Review | Cancer | 염증성 유방암의 다학제 치료에서 Paclitaxel의 역할 |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | 용량 탐색 연구 | Ann Oncol | 진행성 유방암에서 3시간 Paclitaxel 주입 + Cyclophosphamide의 최대 내약 용량 결정 |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | 종설 | Cancer | 유방암 화학요법의 발전 과정 정리 |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | 임상 연구 | Nat Commun | TEKT4 생식세포 변이가 유방암의 Paclitaxel 내성과 연관 |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | 전임상/종설 | Chem Biol Drug Des | Paclitaxel 병용 조합의 유방암 치료 잠재력과 in vivo 바이오마커 탐색 |

## 한국 시판 정보

총 14건의 허가증이 모두 유효합니다. 이 중 일부는 수출용입니다. 허가 적응증은 텍스트가 아닌 허가사항 원문 링크로만 제공되어, 아래 표에서는 링크로 대체했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199604958 | 탁솔주 (보령) | 주사액 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199604958/EE) 참조 |
| 200803520 | 아브락산주 (한국비엠에스제약) | 동결건조 주사제 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200803520/EE) 참조 |
| 199803971 | 제넥솔주 (삼양바이오팜) | 주사액 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199803971/EE) 참조 |
| 200301835 | 팍셀주 (한미약품) | 주사액 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200301835/EE) 참조 |
| 201605495 | 리포락셀액 (대화제약) | 액제 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605495/EE) 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (탁산 계열, 미세소관 안정화제) |
| 골수억제 위험 | 고 (호중구감소증 등. 지식그래프상 호중구감소증·혈소판감소증·빈혈과의 금기 관계도 확인됨) |
| 구토 유발성 등급 | 저 (일반 약물 분류 기준) |
| 모니터링 항목 | CBC(분류 포함), 간기능, 신기능, 말초신경병증 평가 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

위 분류는 약물 계열에 근거한 일반적 평가입니다. 상세 내용은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 이 중 상위 20건의 수준은 다음과 같습니다.
  - **중등도(Moderate)**: Aprepitant, Cimetidine, Clarithromycin, Clotrimazole, Dexamethasone, Eliglustat, Metronidazole, Miconazole, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole, Troglitazone
  - **경미(Minor)**: Ascorbic acid, Levofloxacin
  - **수준 미상**: Glimepiride, Doxycycline, Morphine, Metformin, Omeprazole
  - 상당수가 CYP 대사 경로 관련 약물이므로 병용 시 점검이 필요합니다.
- **지식그래프상 금기 관계**(허가 문구가 아닌 모델 지식그래프 기준의 참고 정보): 골수억제(호중구감소증, 무과립구증, 혈소판감소증, 빈혈), 말초신경병증, 간질환·고빌리루빈혈증(길버트 증후군 포함), 신장질환, 심근경색, 천식, 당뇨병 등이 연결되어 있습니다.

경고·금기 등 허가 문구 수준의 상세 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
유방암에서 Paclitaxel의 효능을 지지하는 완료된 Phase 3 임상시험이 다수 있어 근거 수준은 L1입니다. 다만 이는 이미 확립된 사용이며, 근거 상당수가 병용 요법 또는 비교 대조군 시험이라는 한계가 있습니다. 또한 세포독성 약물이므로 골수억제와 신경독성에 대한 안전 관리가 전제되어야 합니다.

**진행하려면 필요한 것:**
- 허가사항 원문(PDF) 확인을 통한 허가 적응증, 경고, 금기 상세 확보
- 구조화된 작용 기전(MOA) 데이터 보완
- 아형(ER 음성·양성, HER2 상태)별 Paclitaxel 단독 효능과 병용 요법의 기여도 구분
- 골수억제·말초신경병증 모니터링 계획과 주요 상호작용 약물(CYP 관련) 점검 체계

**참고:** 같은 약물의 다른 예측 중 ER 음성·양성 유방암, 호르몬 저항성 유방암은 임상 근거가 있어 같은 방향으로 평가됩니다. 반면 횡문근육종 계열 예측 2건은 임상시험과 문헌이 없고 모델 점수만 있으므로 보류(Hold)가 적절합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

