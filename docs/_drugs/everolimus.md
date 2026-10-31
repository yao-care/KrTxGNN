---
layout: default
title: Everolimus
parent: 모델 예측만 (L5)
nav_order: 332
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-31
monitor_inn: "Everolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "dermatofibrosarcoma protuberans", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "embryonal extrahepatic bile duct rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "prostate embryonal rhabdomyosarcoma"]
description: "Everolimus: 예측 신규 적응증 지방육종 (liposarcoma) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804620/EE"
---

# Everolimus
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Everolimus: 지방육종 (liposarcoma)
{: .text-alpha }

## 한 문장 요약

Everolimus는 mTOR 억제제로, 한국에서 신세포암 등 항종양 치료와 이식 관련 면역억제 목적으로 허가된 약물입니다(허가 정보 일부는 원문 링크만 확인되어 세부 적응증은 허가사항을 참조해야 합니다).
TxGNN 모델은 **지방육종(Liposarcoma)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험(Phase 2)**과 **4편의 문헌**이 이 방향과 관련되어 있습니다.
다만 이 근거는 ribociclib 병용 단일군 시험이 중심이어서, everolimus 자체의 효과를 입증하는 수준은 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201804620/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202004977/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202002237/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201904234/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202004979/EE;  |
| 예측 신규 적응증 | 지방육종 (liposarcoma) |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 (엄격한 판정 기준 적용 시: 완료된 Phase 2/3 RCT 없음, 진행 중인 단일군 Phase 2만 존재) |
| 한국 시판 현황 | 시판 중 (유효 허가 16건 / 전체 16건) |
| 허가증 수 | 16건 (유효 16건) |
| 권장 결정 | Hold (연구 질문 단계) |

> 참고: 이 예측 적응증에 대한 사전 평가 등급은 L2였으나, 해당 시험은 무작위배정이 아닌 단일군 시험이고 아직 진행 중이므로 본 보고서의 판정 기준에서는 L2 조건(완료된 Phase 2/3 RCT)을 충족하지 않습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, everolimus는 mTORC1을 억제하는 rapamycin 유사체이며, 세포 성장과 증식, 혈관신생 신호를 차단하는 것으로 알려져 있습니다.

탈분화 지방육종(DDLPS)은 CDK4/MDM2 증폭이 특징이며, PI3K/AKT/mTOR 경로 활성화도 흔하게 나타납니다. 따라서 mTOR 억제제(everolimus)와 CDK4/6 억제제(ribociclib)를 병용하면 서로 다른 증식·생존 신호를 동시에 차단할 수 있다는 가설이 가능합니다. 이 가설은 전임상 모델에서 상승적 성장 억제가 관찰된 것에 근거합니다.

다만 이 근거는 초기 단계 자료에 한정되며, 기전상의 타당성이 곧 임상적 효능을 의미하지는 않습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 진행 중(모집 종료) | 48 | 진행성 탈분화 지방육종(DDL) 및 평활근육종(LMS)에서 ribociclib + everolimus 병용의 항종양 활성 평가. 단일군, 2개 코호트, 기존 전신치료 1회 이상 받은 환자 대상 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 임상시험 보고 | Clin Cancer Res | DDL과 LMS에서 CDK4/6 억제제 ribociclib + mTOR 억제제 everolimus 병용을 평가한 Phase 2 시험 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | 육종 PDOX 마우스 모델에서 CDK 억제제 palbociclib 병용요법 탐색 (everolimus 특이적이지 않음) |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 전임상 | Anticancer Res | Eribulin과 다양한 항암제의 병용 효과 (everolimus 특이적이지 않음) |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | 전임상 | Oncogene | XPO1 억제제 KPT-330이 DDLPS 전사 조절 회로를 교란 (everolimus 특이적이지 않음) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200904535 | 아피니토정10밀리그램 (한국노바티스) | 흰색 내지 엷은 미황색의 장방형 정제 | 허가사항 참조 |
| 200904536 | 아피니토정5밀리그램 (한국노바티스) | 흰색 내지 엷은 미황색의 장방형 정제 | 허가사항 참조 |
| 200603862 | 써티칸정0.25밀리그램 (한국노바티스) | 백색~황색 원형 정제 | 허가사항 참조 |
| 202004977 | 에베로즈정2.5밀리그램 (삼양바이오팜) | 흰색 내지 엷은 미황색의 장방형 정제 | 허가사항 참조 |
| 202002237 | 에리니토정5밀리그램 (광동제약) | 흰색 내지 황백색의 타원형 정제 | 허가사항 참조 |

그 외 종근당 써티로벨정 등을 포함하여 총 16건의 단일제 허가가 유효합니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (mTOR 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건의 상호작용이 확인되었습니다. 이 중 주요(Major) 등급은 다음과 같습니다.
  - Amphotericin B (지질 복합체 포함)
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
- 중등도(Moderate) 등급으로는 당뇨병 치료제(metformin, glimepiride, SGLT2 억제제, DPP-4 억제제, GLP-1 작용제 등)와 cimetidine 등이 확인되었습니다.
- 경미(Minor) 등급으로는 zinc sulfate가 있습니다.

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지방육종에 대한 직접 근거는 ribociclib 병용 단일군 Phase 2 시험 1건뿐이며, 아직 진행 중이어서 everolimus 단독 기여도를 판단할 수 없습니다. 그 밖의 문헌은 everolimus와 직접 관련이 없는 전임상 또는 리뷰입니다.

**진행하려면 필요한 것:**
- 진행 중인 Phase 2 시험(NCT03114527)의 최종 결과 확인 (예상 완료 2026년 12월)
- 허가사항의 경고·금기·적응증 원문 확보 (현재 확인 불가)
- 작용 기전(MOA) 데이터 보완
- 지방육종에서 everolimus 단독 또는 대조군 비교 근거 확보

---

### 참고: 다른 예측 적응증

- **투명세포 신세포암**: 다수의 Phase 3 임상시험과 RCT 문헌이 있으나, 이미 허가된 적응증과 일치하는 기존 사용이며 새로운 재창출 발견이 아닙니다. 최근 근거에서는 후발 약제가 everolimus를 능가한 사례가 많아 주로 비교군 또는 기반 요법 역할입니다.
- **횡문근육종**(0.9974): 소아 고형암 Phase 1 및 Phase 1/2(lenvatinib 병용) 시험이 있으나 횡문근육종에서의 효능은 확립되지 않았습니다.
- **그 외**(난소 점액양 지방육종, 피부섬유육종, 횡문근육종 하위 유형, 신경모세포종 연관 신세포암): 임상시험과 직접 근거가 없어 모델 예측 수준(L5)이며 보류가 적절합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

