---
layout: default
title: Sorafenib
parent: 모델 예측만 (L5)
nav_order: 699
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-04
monitor_inn: "sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
description: "Sorafenib: 예측 신규 적응증 지방육종 (liposarcoma) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200800233/EE"
---

# Sorafenib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Sorafenib: 지방육종 (liposarcoma)
{: .text-alpha }

## 한 문장 요약

Sorafenib은 RAF/MEK/ERK, VEGFR, PDGFR, KIT 등을 억제하는 다중 키나제 억제제로, 한국에서 시판 중입니다.
TxGNN 모델은 **지방육종(liposarcoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 대상으로 한 연구는 확인되지 않아 근거 수준은 **L5**입니다.
육종 전체를 다룬 연성조직육종 2상 시험과 전임상 연구가 간접적으로 참고될 뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200800233/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202007416/EE |
| 예측 신규 적응증 | 지방육종 (liposarcoma) |
| TxGNN 예측 점수 | 0.9982 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Sorafenib은 RAF/MEK/ERK 신호전달과 VEGFR, PDGFR, KIT를 억제하는 다중 키나제 억제제입니다. 이 기전은 연성조직육종에서 혈관신생과 MAPK 신호를 억제할 가능성이 있습니다. 다만 현재 데이터에는 상세한 작용 기전 기록이 없어, 위 내용은 일반적으로 알려진 약리 지식에 근거합니다.

전임상 연구에서는 악성 말초신경초종 세포주와 탈분화 지방육종 세포주에서 성장 억제가 보고되었습니다. 그러나 이는 세포 수준의 결과이며, 지방육종 환자를 대상으로 sorafenib을 직접 평가한 시험은 없습니다.

임상 신호는 연성조직육종 전체를 대상으로 한 2상 시험에서만 나왔습니다. 지방육종은 이 시험에서 소수 하위군에 불과했고, 효과는 제한적이며 미미했습니다. 따라서 지방육종에 대한 근거는 약합니다.

## 임상시험 근거

지방육종만을 대상으로 한 임상시험은 없습니다. 아래는 연성조직육종 전체를 대상으로 한 시험으로, 간접 근거일 뿐입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | 완료 | 51 | 진행성 연성조직육종에서 sorafenib 단독 단일군 시험. 지방육종 특이적 결과가 아니며 조직형이 혼합됨 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 시험 (SWOG S0505) | Cancer | 진행성 연성조직육종에서 sorafenib 평가 |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 시험 | Ann Surg Oncol | 사지 국소 진행 연성조직육종에서 수술 전 방사선 + sorafenib 병용 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 연성조직육종의 조직형별 치료 동향 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | 조직형에 따른 연성조직육종 약물치료 |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | 전임상 | Mol Cancer Ther | 악성 말초신경초종 및 탈분화 지방육종 세포주에서 성장 및 MAPK 신호 억제 |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | 전임상 | Am J Pathol | 탈분화 지방육종 이종이식 모델과 PI3K 경로 억제 반응 |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review (전임상) | Front Oncol | 육종 PDOX 마우스 모델과 palbociclib 병용 전략 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200800233 | 넥사바정200밀리그램(소라페닙토실레이트(미분화)) | 빨강색의 원형 필름코팅정 | 허가증 PDF 참조 |
| 202007416 | 소라닙정200밀리그램(소라페닙토실레이트(미분화)) | 분홍색의 원형 필름코팅정 | 허가증 PDF 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (다중 키나제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 509건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - Major: Dolasetron
  - Moderate: Famotidine, Loperamide, Dexamethasone, Bisacodyl, Cholic Acid, Clarithromycin, Picosulfuric acid, Levofloxacin, Palonosetron, Naltrexone, Lactulose 등
  - Minor: Dapagliflozin, Naloxegol, Metronidazole

허가사항상의 경고 및 금기는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지방육종을 직접 대상으로 한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 연성조직육종 전체 2상 시험에서도 지방육종 하위군의 효과는 제한적이고 미미했습니다.

**진행하려면 필요한 것:**
- 지방육종 환자를 대상으로 한 직접적인 임상 또는 전임상 근거
- 연성조직육종 2상 시험에서 지방육종 하위군 결과의 별도 분석
- 허가사항(경고, 금기)과 상세 작용 기전 데이터 확보

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

