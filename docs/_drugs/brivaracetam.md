---
layout: default
title: Brivaracetam
parent: 모델 예측만 (L5)
nav_order: 157
evidence_level: L5
indication_count: 1
monitor_inn: "BRIVARACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-10-27
description: "Brivaracetam: 예측 신규 적응증 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502767/EE"
---

# Brivaracetam
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Brivaracetam: 항간질 약물(SV2A 조절제) → 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency)
{: .text-alpha }

## 한 문장 요약

Brivaracetam은 시냅스 소포 단백질 SV2A에 작용하는 계열의 항경련제입니다.
TxGNN 모델은 **베타-케토티올라제 결핍증(beta-ketothiolase deficiency)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험은 0건, 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502767/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502491/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502405/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502492/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502741/EE;  |
| 예측 신규 적응증 | 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) |
| TxGNN 예측 점수 | 0.9914 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 20건 (유효 20건, 취소 0건, 일부 기록만 포함되었을 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 brivaracetam은 SV2A를 조절하는 항경련제 계열에 속하지만, 이 보고서용으로 수집한 데이터에서는 기전 정보를 확인할 수 없습니다.

베타-케토티올라제 결핍증은 케톤체 및 이소류신 대사에 관여하는 유전성 대사 질환입니다. SV2A 조절과의 뚜렷한 기전적 연결고리는 확인되지 않으며, 높은 예측 점수는 모델 구조에서 비롯된 인공적 결과일 가능성이 큽니다. 기존 약물과의 유사성 분석 역시 아직 수행되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

총 20건의 단일 성분 허가가 유효 상태로 기록되어 있으며, 아래는 주요 5건입니다. 허가 적응증은 PDF 링크로만 제공되어 본문을 확인할 수 없습니다. 목록은 일부일 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201901308 | 브리비액트정25밀리그램 | 회색의 타원형 필름코팅정 | 허가사항 문서 참조 |
| 201901306 | 브리비액트액 | 액제 | 허가사항 문서 참조 |
| 201901309 | 브리비액트정50밀리그램 | 노란색의 타원형 필름코팅정 | 허가사항 문서 참조 |
| 201901307 | 브리비액트정10밀리그램 | 흰색 혹은 유백색의 원형 필름코팅정 | 허가사항 문서 참조 |
| 202502491 | 브리바정10밀리그램 | 흰색 혹은 유백색의 원형 필름코팅정 | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 69건의 상호작용이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - 중등도: morphine, opium, dronabinol, nabilone, metoclopramide, promethazine, ethanol, diphenoxylate, difenoxin, sibutramine, clopidogrel
  - 경미: omeprazole, esomeprazole, lansoprazole, pantoprazole, dexlansoprazole, chlorpropamide, tolbutamide, cilostazol

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지지하는 임상시험과 문헌이 전혀 없고(근거 수준 L5), 기전적 연결고리도 불분명하여 높은 예측 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확보 및 분석
- 상세한 약물 작용 기전(MOA) 데이터
- 베타-케토티올라제 결핍증과 SV2A 조절 사이의 기전적 타당성에 대한 전임상 근거
- 해당 질환을 직접 다룬 임상시험 또는 문헌 근거
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

