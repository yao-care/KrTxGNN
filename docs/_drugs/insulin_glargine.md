---
layout: default
title: Insulin Glargine
parent: 모델 예측만 (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Insulin Glargine: 예측 신규 적응증 자가면역성 난소염 (autoimmune oophoritis) (근거 수준 L5). 기존 적응증: 2세 이상의 어린이와 청소년 및 성인에서의 인슐린 요법을 필요로 하는 당뇨병"
monitor_inn: "INSULIN GLARGINE"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Insulin Glargine: 당뇨병에서 자가면역성 난소염으로
{: .text-alpha }

## 한 문장 요약

Insulin glargine은 지속형 인슐린 제제로, 원래 당뇨병 혈당 조절에 사용되는 약입니다.
TxGNN 모델은 **자가면역성 난소염(autoimmune oophoritis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 2세 이상의 어린이와 청소년 및 성인에서의 인슐린 요법을 필요로 하는 당뇨병 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201507921/EE)) |
| 예측 신규 적응증 | 자가면역성 난소염 (autoimmune oophoritis) |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 7건 / 전체 7건) |
| 허가증 수 | 7건 (유효 7건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Insulin Glargine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “인슐린 글라진 제품을 포함한 인슐린의 주된 작용은 포도당 대사의 조절이다. 인슐린 및 그 유사체는 특히 골격근과 지방에서 말초 포도당 흡수를 촉진하고 간의 포도당 생성을 억제함으로써 혈당을 낮춘다.” 영어 원문: "The primary activity of insulin, including insulin glargine products, is regulation of glucose metabolism. Insulin and its analogs lower blood glucose by stimulating peripheral glucose uptake, especially by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Langlara (insulin glargine-aldy) prescribing information, Lanexa Biologics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5328761e-59d3-ca7a-e063-6394a90ae810), 버전 2026-10-15; 확인일 2026-11-19). 알려진 정보에 따르면, insulin glargine은 단일 성분 지속형 인슐린 제제이며, 당뇨병에서의 혈당 조절 효능이 확립되어 있습니다.

다만 자가면역성 난소염에 대한 직접적인 치료 기전은 확인되지 않습니다. 가능한 설명은 자가면역성 다내분비 증후군이 자가면역성 당뇨병과 함께 나타나는 경우가 많다는 점입니다. 이는 동반 질환과의 연관성일 뿐, 난소의 자가면역 과정에 대한 치료 효과가 아닙니다. Insulin glargine이 난소염에 면역조절 작용을 한다는 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201507921 | 베이사글라퀵펜100단위/밀리리터 | 프리필드 펜 주사제 | 허가사항 문서 참조 |
| 201801065 | 글라지아프리필드펜 | 프리필드 펜 주사제 | 허가사항 문서 참조 |
| 201505654 | 투제오주솔로스타 | 펜 모양 주사제 | 허가사항 문서 참조 |
| 200109054 | 란투스주바이알 | 바이알 주사제 | 허가사항 문서 참조 |
| 201707854 | 솔리쿠아펜주(30-60) | 펜 모양 주사제 | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 확인되었으며, 대부분 중등도(Moderate) 수준입니다. 주요 항목은 다음과 같습니다.
  - 혈당 영향 가능 약물: 하이드로코르티손, 에티닐에스트라디올, 에스트라디올, 히드로클로로티아지드, 아세타졸아미드
  - 교감신경 작용제: 페닐에프린, 에피네프린, 슈도에페드린, 살부타몰, 포르모테롤
  - 베타차단제: 아세부톨롤
  - 다른 당뇨병 치료제: 메트포르민, 피오글리타존, 알로글립틴, 알비글루티드
  - 기타: 독시사이클린, 알코올(에탄올), 알펠리십
  - 경미(Minor)한 항목: 국소 하이드로코르티손, 국소 알클로메타손

허가사항의 경고 및 금기 정보는 이번 자료에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌 근거가 전혀 없고 TxGNN 점수만 높은 L5 단계입니다. 예측은 동반 자가면역 당뇨병과의 연관성에서 비롯된 것으로 보이며, 난소 자가면역 과정에 대한 직접적인 치료 효과를 시사하지 않습니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS)의 경고·금기 정보 확보 (현재 안전성 검토를 진행할 수 없는 차단 수준의 공백)
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 자가면역성 난소염에서 insulin glargine의 효과를 다룬 임상 또는 전임상 연구 탐색
- 동반 당뇨병 관리와 난소염 자체 치료를 구분하는 평가 설계

## 참고: 다른 예측 적응증

상위 10개 예측 가운데 대부분은 근거가 없는 L5(Hold)입니다. 주목할 점은 다음과 같습니다.

- **췌장 무형성(pancreatic agenesis, 점수 0.9943)**: 인슐린 결핍성 당뇨병에 대한 인슐린 보충은 생리학적으로 타당하고 표준 지지요법입니다. 다만 검색된 문헌 4편은 모두 간접 근거(제2형 당뇨병 인슐린 치료, 이차성 당뇨병, 당뇨 고양이, MODY5 증례)이며, 이는 재창출이 아니라 결핍 호르몬의 보충입니다. 근거 수준 L4, 연구 질문(Research Question) 단계입니다.
- **약물 유발 국소 지방이영양증 등 국소 지방이영양증 계열(순위 7~10)**: 인슐린 주사 자체가 주사 부위 지방이영양증의 알려진 원인이므로 치료 후보가 아니라 안전성 문제입니다.
- **경직인간증후군, 티아민 반응성 기능장애 증후군**: 동반된 당뇨병 관리에만 해당하며, 신경학적 병리나 SLC19A2 수송체 결함에는 효과가 기대되지 않습니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Langlara (insulin glargine-aldy) prescribing information, Lanexa Biologics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5328761e-59d3-ca7a-e063-6394a90ae810) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

