---
layout: default
title: Perampanel
parent: 모델 예측만 (L5)
nav_order: 592
evidence_level: L5
indication_count: 1
monitor_inn: "PERAMPANEL"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-10-28
description: "Perampanel: 예측 신규 적응증 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201504770/EE"
---

# Perampanel
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

## Perampanel: AMPA 수용체 길항제 → 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency)
{: .text-alpha }

## 한 문장 요약

Perampanel은 AMPA 수용체를 길항하는 항경련제 계열의 약물입니다. TxGNN 모델은 **베타-케토티올라제 결핍증(beta-ketothiolase deficiency)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201504770/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202300747/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202201453/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202201450/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202201600/EE;  |
| 예측 신규 적응증 | 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) |
| TxGNN 예측 점수 | 0.9979 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 19건 (단일 성분 제제 19건, 유효 19건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 Perampanel은 AMPA 수용체 길항 계열의 항경련제로 알려져 있습니다.

베타-케토티올라제 결핍증은 케톤체와 이소류신 대사에 관여하는 대사 질환입니다. AMPA 길항 작용과의 뚜렷한 기전적 연결 고리는 확인되지 않으며, 대사 위기 시 나타날 수 있는 발작 증상 정도가 접점일 수 있습니다. 따라서 이 예측은 모델의 인공적 산물(artifact)일 가능성이 높습니다.

이 질환을 직접 다룬 임상시험이나 문헌이 확인되지 않았으므로, 근거 수준은 모델 예측만 있는 L5로 판정했습니다.

## 한국 시판 정보

한국에는 단일 성분 Perampanel 허가가 총 19건 있으며, 모두 유효 상태입니다. 아래는 주요 5건입니다. 허가 적응증 텍스트는 허가 문서 링크로만 기록되어 있어 요약하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|------|
| 201504770 | 파이콤파필름코팅정4밀리그램 | 필름코팅정 | 한국에자이(주) |
| 202300747 | 페라넬정8밀리그램 | 필름코팅정 | 환인제약(주) |
| 202201453 | 페리콤파정8밀리그램 | 필름코팅정 | 명인제약(주) |
| 202003991 | 파이콤파현탁액0.5mg/mL | 현탁액제 | 한국에자이(주) |
| 202201600 | 페라넬정2밀리그램 | 필름코팅정 | 환인제약(주) |

## 안전성 고려사항

- **약물 상호작용**: 총 56건이 조회되었습니다. 이 중 확인된 항목은 대부분 중등도(Moderate)이며, 주요 항목은 다음과 같습니다.
  - 오피오이드 계열: Morphine, Codeine, Hydrocodone, Opium, Diphenoxylate, Difenoxin
  - 카나비노이드: Dronabinol, Nabilone
  - 기타 중추신경 억제 가능 약물: Ethanol, Promethazine, Chlorpheniramine, Dextromethorphan, Metoclopramide, Sibutramine
  - 항말라리아제: Chloroquine, Hydroxychloroquine
  - 코르티코스테로이드: Dexamethasone
  - 경미(Minor): Clarithromycin

경고 및 금기 등 그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 질환을 직접 연구한 임상시험과 문헌이 없고, AMPA 길항 작용과의 기전적 연결도 불분명하여 모델 예측만 존재하는 L5 수준입니다. 현 단계에서는 진행을 보류하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 허가사항(MFDS 첨부문서)의 경고 및 금기 정보 확인
- 베타-케토티올라제 결핍증과 AMPA 경로의 연관성을 보여주는 전임상 또는 기전 연구
- 이 질환 환자를 대상으로 한 임상 또는 관찰 연구 근거
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

