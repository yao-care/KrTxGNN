---
layout: default
title: Enzalutamide
parent: 모델 예측만 (L5)
nav_order: 313
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Enzalutamide: 예측 신규 적응증 전립선암/뇌암 감수성 (prostate cancer/brain cancer susceptibility) (근거 수준 L5). 기존 적응증: 전립선암 (허가 적응증 본문은 허가 문서 링크로만 제공되어 원문 확인 필요)"
monitor_inn: "ENZALUTAMIDE"
predicted_indications: ["prostate cancer/brain cancer susceptibility", "prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "male reproductive organ cancer", "benign prostate phyllodes tumor"]
---

# Enzalutamide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

# 엔잘루타미드(Enzalutamide): 전립선암에서 전립선암/뇌암 감수성으로

## 한 문장 요약

엔잘루타미드는 안드로겐 수용체(AR) 억제제로, 원래 전립선암 치료에 사용되는 약입니다.
TxGNN 모델은 **전립선암/뇌암 감수성(prostate cancer/brain cancer susceptibility)**에 효과가 있을 것으로 예측했지만(점수 99.7%), 이 예측을 직접 뒷받침하는 **임상시험과 문헌은 0건**입니다.
이 질환명은 치료 대상이 되는 질병이라기보다 유전적 감수성 개념이어서, 현 단계에서는 보류(Hold)를 권고합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 전립선암 (허가 적응증 본문은 허가 문서 링크로만 제공되어 원문 확인 필요) |
| 예측 신규 적응증 | 전립선암/뇌암 감수성 (prostate cancer/brain cancer susceptibility) |
| TxGNN 예측 점수 | 99.71% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 7건 (모두 유효, 단일 성분) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 알려진 정보에 따르면 엔잘루타미드는 AR 신호전달을 차단하는 약물이며, 전립선암에서 이미 사용되고 있습니다. 따라서 이 예측은 전립선암과의 연관성을 반영했을 가능성이 높습니다.

반면 예측된 질환명은 "감수성"이라는 유전적 개념입니다. 치료로 개선할 수 있는 독립 질환이 아닙니다. 뇌암과의 연결은 AR 억제라는 기전만으로는 설명되지 않으며, 이를 지지하는 근거도 확인되지 않았습니다. 이 점수는 지식 그래프상 전립선암과의 근접성에서 나왔을 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 참고: 같은 약물의 다른 예측 후보

1순위 예측에는 근거가 없지만, 다른 후보 중에는 근거가 있는 항목이 있습니다.

| 순위 | 예측 질환 | 예측 점수 | 근거 수준 | 비고 |
|-----|---------|---------|---------|-----|
| 2 | 전립선 평활근종 | 99.57% | L5 | 임상시험·문헌 없음, 기전 추정만 가능 |
| 3 | 브레너 종양 | 99.55% | L5 | AR 억제와의 기전 연관 불명확 |
| 4 | 전립선 섬유종 | 99.53% | L5 | 임상시험·문헌 없음 |
| 5 | 양성 생식계 신생물 | 99.53% | L5 | 문헌 5편은 모두 전립선암 기전 연구이며 양성 종양을 직접 다루지 않음 |
| 6 | 남성 생식기관 암 | 99.51% | L1 | 사실상 전립선암으로, 신규 재창출이 아닌 기존 적응증 |
| 7 | 양성 전립선 엽상종양 | 99.48% | L5 | 임상시험·문헌 없음 |

6순위 후보의 주요 임상시험과 문헌은 다음과 같습니다. 모두 전립선암 대상이므로 기존 적응증의 근거로 보아야 합니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02446405](https://clinicaltrials.gov/study/NCT02446405) | Phase 3 | 진행 중(모집 종료) | 1125 | 전이성 전립선암 1차 ADT에서 엔잘루타미드 vs 기존 비스테로이드성 항안드로겐 (ENZAMET) |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) | Phase 3 | 진행 중(모집 종료) | 600 | 아비라테론 치료 후 mCRPC에서 mevrometostat + 엔잘루타미드 vs 엔잘루타미드 또는 도세탁셀 |
| [NCT03834493](https://clinicaltrials.gov/study/NCT03834493) | Phase 3 | 조기 종료 | 1244 | mCRPC에서 pembrolizumab + 엔잘루타미드 vs 위약 + 엔잘루타미드 (KEYNOTE-641) |
| [NCT07512076](https://clinicaltrials.gov/study/NCT07512076) | Phase 2 | 모집 예정 | 26 | 고령 진행성 전립선암 환자에서 엔잘루타미드 용량 최적화 |

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [42223064](https://pubmed.ncbi.nlm.nih.gov/42223064/) | 2026 | 임상시험 보고 | N Engl J Med | 전이성 전립선암에서 PARP 억제제(talazoparib) + AR 신호 억제제 + ADT 병용 효과. 이전 시험에서 talazoparib + 엔잘루타미드가 영상학적 무진행 생존기간과 전체 생존기간을 유의하게 개선 |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends Cancer | 진행성 전립선암 치료 발전과 향후 방향 정리 |
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | Review | JAMA | 전립선암 진단과 치료 개관 |

## 한국 시판 정보

허가 적응증 본문은 허가 문서 링크로만 제공되어, 아래 표에는 링크를 표기했습니다. 총 7건 중 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201307883 | 엑스탄디연질캡슐40mg (한국아스텔라스제약) | 연질캡슐 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307883/EE) 참조 |
| 202402841 | 엑스탄디정80밀리그램 (한국아스텔라스제약) | 필름코팅정 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402841/EE) 참조 |
| 202402842 | 엑스탄디정40밀리그램 (한국아스텔라스제약) | 필름코팅정 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402842/EE) 참조 |
| 202600225 | 엔잘엑스연질캡슐40밀리그램 (한국메나리니) | 연질캡슐 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600225/EE) 참조 |
| 202500452 | 아나미드연질캡슐40밀리그램 (알보젠코리아) | 연질캡슐 | [허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500452/EE) 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 호르몬 표적치료제 (AR 억제제). 전통적 세포독성 화학요법제는 아님 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번에 확인된 상호작용 약물은 총 100건입니다. 이 중 상위 20건의 등급은 다음과 같습니다.
  - **Major**: Bupropion, Dolasetron, Eliglustat
  - **Moderate**: Famotidine, Rabeprazole, Omeprazole, Hydrocortisone, Dexamethasone, Clarithromycin, Aprepitant, Loperamide, Alosetron, Alvimopan, Saxagliptin, Linagliptin, Empagliflozin, Chlorpropamide, Bisacodyl, Picosulfuric acid, Polyethylene glycol 등

주요 경고와 금기 정보는 이번 데이터에서 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환인 "전립선암/뇌암 감수성"은 유전적 감수성 개념이어서 치료 대상으로 정의하기 어렵습니다. 이를 직접 지지하는 임상시험과 문헌도 없고, 높은 점수는 이미 승인된 전립선암과의 연관성을 반영했을 가능성이 큽니다.

**진행하려면 필요한 것:**
- 구체적이고 치료 가능한 질환 단위로 예측 대상을 다시 정의 (예: 뇌암 하위 유형 중 AR 의존성이 확인된 질환)
- 뇌암에서 AR 억제의 기전적 근거와 전임상·임상 문헌 확보
- 허가사항(경고·금기, 작용 기전)을 확보한 뒤 안전성 검토 진행
- 재창출 논의는 전립선암 승인 범위 밖의 비승인 병용요법이나 특수 인구집단(예: 고령 환자 용량 최적화) 중심으로 한정
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

