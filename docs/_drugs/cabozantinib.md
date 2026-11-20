---
layout: default
title: Cabozantinib
parent: 모델 예측만 (L5)
nav_order: 168
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
description: "Cabozantinib: 예측 신규 적응증 지방육종 (Liposarcoma) (근거 수준 L5). 기존 적응증: 1) 신장세포암의 치료 (1) 이전에 VEGF(Vascular endothelial growth…"
monitor_inn: "Cabozantinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Cabozantinib: 신세포암에서 지방육종(Liposarcoma)으로
{: .text-alpha }

## 한 문장 요약

Cabozantinib은 VEGFR2, MET, AXL 등을 억제하는 경구 키나제 억제제로, 한국에서는 신세포암 치료 적응증으로 허가·시판되고 있습니다.
TxGNN 모델은 **지방육종(Liposarcoma)**에 효과가 있을 수 있다고 예측하며, 현재 **1건의 임상시험**(연부조직육종 혼합 대상, 병용요법)과 **1편의 문헌**(1상)이 이 방향을 제한적으로 지지합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1) 신장세포암의 치료 (1) 이전에 VEGF(Vascular endothelial growth factor) 표적요법으로 치료 받은 적이 있는 진행성 신장세 포암 환자에서의 단독요법 (2) 진행성 신장세포암 환자에서의 1차 치료로서 니볼루맙과의 병용요법 2) 간세포암의 치료 :… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707241/EE)) |
| 예측 신규 적응증 | 지방육종 (Liposarcoma) |
| TxGNN 예측 점수 | 0.9983 |
| 근거 수준 | L5 (완료된 RCT 없음, 지방육종 특이 자료 희소) |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Cabozantinib 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “시험관 내 생화학적 및/또는 세포 분석에서 카보잔티닙은 MET, VEGFR-1, -2 및 -3, AXL, RET, ROS1, TYRO3, MER, KIT, TRKB, FLT-3 및 TIE-2의 티로신 키나제 활성을 억제하는 것으로 나타났다. 이들 수용체 티로신 키나제는 정상적인 세포 기능뿐만 아니라 종양 발생, 전이, 종양 혈관신생, 약물 내성 및 종양 미세환경 유지와 같은 병리학적 과정에도 관여한다.” 영어 원문: "In vitro biochemical and/or cellular assays have shown that cabozantinib inhibits the tyrosine kinase activity of MET, VEGFR-1, -2 and -3, AXL, RET, ROS1, TYRO3, MER, KIT, TRKB, FLT-3, and TIE-2. These receptor tyrosine kinases are involved in both normal cellular function and pathologic processes such as oncogenesis, metastasis, tumor angiogenesis, drug resistance, and maintenance of the tumor microenvironment." ([DailyMed: Cabometyx (cabozantinib) prescribing information, Exelixis, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3850cce2-6137-42e5-a792-d318c4a4b3b5), 버전 2025-10-19; 확인일 2026-11-19). 이번 평가에서 정리된 분석에 따르면 Cabozantinib은 VEGFR2, MET, AXL을 억제합니다. 이 경로들은 혈관신생과 종양 진행에 관여하며, 연부조직육종에서도 역할이 있는 것으로 알려져 있습니다.

신세포암은 혈관신생 의존성이 높은 종양이어서 VEGFR 억제가 효과를 보입니다. 연부조직육종도 혈관신생과 수용체 티로신 키나제 신호가 종양 진행에 기여하므로, 기전상 적용 가능성은 있습니다.

다만 지방육종에 특이적인 자료는 매우 적습니다. 유일한 2상 시험은 여러 연부조직육종을 함께 다루고 면역관문억제제와 병용하므로, Cabozantinib 단독 효과를 분리해서 판단하기 어렵습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | 진행 중 (모집 종료) | 66 | 진행성 연부조직육종에서 ipilimumab+nivolumab 단독과 Cabozantinib 병용을 비교하는 무작위 시험입니다. 지방육종은 일부 하위군일 가능성이 높고 결과는 아직 보고되지 않았습니다. |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 시험 | American Journal of Clinical Oncology | 사지 연부조직육종에서 수술 전 Cabozantinib과 방사선 병용의 안전성을 평가했습니다. 병용 시 누공·천공 위험에 대한 우려가 배경이며, Cabozantinib은 여러 연부조직육종 아형에서 활성을 보이는 것으로 소개됩니다. |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201707241 | 카보메틱스정40밀리그램 (입센코리아) | 노란색 삼각형 필름코팅정 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707241/EE) |
| 201707240 | 카보메틱스정60밀리그램 (입센코리아) | 노란색 타원형 필름코팅정 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707240/EE) |
| 201707242 | 카보메틱스정20밀리그램 (입센코리아) | 노란색 원형 필름코팅정 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707242/EE) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (다중 티로신 키나제 억제제: VEGFR2, MET, AXL) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 고혈압, 수족증후군, 설사, 출혈 (병용요법 시 용량 관리 포함) |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 주요 등급(Major)은 다음과 같습니다.
  - Acetylsalicylic acid
  - Cisapride
  - Clarithromycin
  - Dolasetron
  - Granisetron
  - Levofloxacin

  Loperamide, Aprepitant, Dexamethasone, Bisacodyl 등은 중등도(Moderate)입니다.
- **방사선 병용 시 주의**: 방사선 치료와 병용할 때 누공 또는 천공 위험이 우려되어 별도의 안전성 평가가 필요합니다.

경고·금기 항목은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만, 지방육종에 특이적인 근거는 혼합 연부조직육종 대상의 병용요법 2상(결과 미보고) 1건과 1상 문헌 1편뿐입니다. 이 자료로는 Cabozantinib 단독의 지방육종 효과를 판단할 수 없어, 현 단계에서는 연구 과제 수준으로 보는 것이 적절합니다.

**진행하려면 필요한 것:**
- 허가 적응증 문구와 경고·금기 정보 확보 (허가증 PDF 파싱)
- DrugBank 기반 상세 작용 기전 데이터 보완
- NCT05836571의 지방육종 하위군 결과 확인
- 지방육종 단독 또는 Cabozantinib 단일요법 임상 자료 확보
- 주요 상호작용 약물 병용 및 방사선 병용 시 안전성 모니터링 계획 수립

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Cabometyx (cabozantinib) prescribing information, Exelixis, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3850cce2-6137-42e5-a792-d318c4a4b3b5) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

