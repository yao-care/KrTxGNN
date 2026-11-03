---
layout: default
title: Hydroxyurea
parent: 모델 예측만 (L5)
nav_order: 407
evidence_level: L5
indication_count: 6
monitor_inn: "Hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin E disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
last_modified_at: 2026-11-03
description: "Hydroxyurea: 예측 신규 적응증 여성 유방암 (female breast carcinoma) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200501440/EE"
---

# Hydroxyurea
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

## Hydroxyurea: 여성 유방암 (female breast carcinoma)
{: .text-alpha }

## 한 문장 요약

Hydroxyurea는 리보뉴클레오타이드 환원효소를 억제하는 항대사제 계열의 약물입니다.
TxGNN 모델은 **여성 유방암(female breast carcinoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 없고 문헌도 대부분 전임상 연구이거나 간접적인 자료입니다. 따라서 근거 수준은 **L5**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200501440/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199301690/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200607038/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501759/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606000/EE |
| 예측 신규 적응증 | 여성 유방암 (female breast carcinoma) |
| TxGNN 예측 점수 | 0.9997 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 5건) |
| 허가증 수 | 5건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Hydroxyurea는 리보뉴클레오타이드 환원효소를 억제하여 dNTP 풀을 고갈시키고 DNA 복제 스트레스를 유발합니다. 현재 상세한 작용 기전 데이터는 별도로 확보되어 있지 않으며, 위 내용은 수집된 문헌에 근거한 설명입니다.

복제 스트레스 반응 경로(ATR/RPA2 등)에 의존하는 유방암 세포에서는 이러한 기전이 관련될 수 있습니다. 다만 수집된 연구에서 hydroxyurea는 대부분 치료제가 아니라 복제 스트레스를 유도하는 도구 화합물로 사용되었습니다.

임상 자료는 1990~1992년의 오래된 병용 화학요법 소규모 연구가 전부이고, 그 외에는 나노입자 및 in silico 전임상 연구입니다. 따라서 기전상 가능성은 있으나 유방암 치료 효과를 입증하는 근거로는 부족합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

유방암을 직접 다룬 hydroxyurea 임상 문헌은 확인되지 않았습니다. 아래는 관련성이 있는 주요 문헌입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | 1상 임상 | Am J Clin Oncol | 대장, 췌장, 위, 유방의 진행성 암 환자 20명에서 5-FU·류코보린 후 hydroxyurea를 allopurinol 보호하에 투여하는 요법의 1상 연구 |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | 1/2상 병용 화학요법 | Cancer Chemother Pharmacol | 5-FU, 류코보린, hydroxyurea, 시스플라틴과 방사선 병용 연구 (유방암 특이적이지 않음) |
| [2245491](https://pubmed.ncbi.nlm.nih.gov/2245491/) | 1990 | 파일럿 임상 | Cancer Chemother Pharmacol | 시스플라틴 전 사이타라빈·hydroxyurea 병용의 독성 평가 |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In silico/전임상 | Drug Research | PI3K/AKT/mTOR 경로를 표적으로 한 hydroxyurea 지질 접합체 설계 |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | 전임상 | Naunyn-Schmiedeberg's Arch Pharmacol | Hydroxyurea 탑재 나노입자의 pH 의존적 약물 방출 및 세포주기 정지 평가 |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | 전임상 | DNA Repair | 발프로산이 RPA2 과인산화 DNA 복구 경로를 억제하여 유방암 세포의 hydroxyurea 감수성을 높임 |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | 전임상 | DNA Repair | 2-hexyl-4-pentynoic acid가 RPA2 과인산화를 통해 유방암 세포의 DNA 복구에 영향 |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | 증례 보고 | Case Rep Hematol | 유방암과 본태성 혈소판증가증이 동반된 환자의 치료 경험 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200501440 | 유니온히드록시우레아캡슐(수출용) | 캡슐 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200501440/EE) 참조 |
| 199301690 | 하이드린캡슐500밀리그램 | 캡슐 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199301690/EE) 참조 |
| 200607038 | 히드레아캡슐(수출용) | 캡슐 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200607038/EE) 참조 |
| 201501759 | 하이드린캡슐250밀리그램 | 경질캡슐 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201501759/EE) 참조 |
| 201606000 | 제일히드록시우레아캡슐(수출용) | 캡슐 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606000/EE) 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (항대사제, 리보뉴클레오타이드 환원효소 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 혈구 수치(CBC), 간·신기능 등 (허가사항 참조) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **약물 상호작용**: 수집된 상호작용 정보는 총 100건이며, 대부분 중증도가 분류되지 않았습니다(Unknown). 확인된 항목 중 레보플록사신은 경미한(Minor) 수준입니다. 그 밖에 독시사이클린, 암포테리신 B, 하이드로코르티손, 파모티딘, 아스피린, 판토프라졸, 메트포르민, 오메프라졸 등이 목록에 포함되어 있으나, 중증도는 확인되지 않았습니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
여성 유방암을 직접 연구한 임상시험이 없고, 문헌도 대부분 전임상 연구이거나 1990년대 초의 소규모 병용 요법 연구입니다. TxGNN 점수가 높지만 이를 뒷받침할 직접적인 근거가 부족하여 근거 수준은 L5입니다.

**진행하려면 필요한 것:**
- 유방암에서 hydroxyurea의 치료 효과를 직접 평가한 임상시험 또는 임상 연구
- 허가사항(경고, 금기) 및 허가 적응증 텍스트 확보
- 작용 기전 데이터 보완
- 유방암 환자에서의 안전성 및 골수억제 모니터링 계획

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

