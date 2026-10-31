---
layout: default
title: Dexlansoprazole
parent: 모델 예측만 (L5)
nav_order: 272
evidence_level: L5
indication_count: 4
monitor_inn: "DEXLANSOPRAZOLE"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
last_modified_at: 2026-10-31
description: "Dexlansoprazole: 예측 신규 적응증 위십이지장염 (gastroduodenitis) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802449/EE"
---

# Dexlansoprazole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Dexlansoprazole: 프로톤 펌프 억제제 → 위십이지장염 (gastroduodenitis)
{: .text-alpha }

## 한 문장 요약

Dexlansoprazole은 프로톤 펌프 억제제(PPI) 계열의 약물로, 한국에서 단일 성분 제제로 허가되어 있습니다.
TxGNN 모델은 **위십이지장염(gastroduodenitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 예측을 지지하는 **임상시험과 문헌은 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802449/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207344/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207343/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802450/EE |
| 예측 신규 적응증 | 위십이지장염 (gastroduodenitis) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 Dexlansoprazole은 PPI 계열 약물로, 위산 분비를 억제하는 것이 일반적인 약리 특성입니다.

위와 십이지장의 염증은 위산과 관련될 수 있으므로, 위산 억제가 증상 완화에 도움이 될 가능성은 기전상 있습니다. 그러나 이 예측을 뒷받침하는 임상시험이나 문헌이 연결되어 있지 않으며, 현재 근거는 TxGNN 모델 점수뿐입니다. 약물과 질환 간 유사성 분석도 아직 완료되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201802449 | 덱시라졸캡슐60밀리그램(덱스란소프라졸) | 경질캡슐 (과립 충전) | 적응증 텍스트 없음 (허가 문서 링크만 제공) |
| 201207344 | 덱실란트디알캡슐60밀리그램(덱스란소프라졸) | 경질캡슐 (과립 충전) | 적응증 텍스트 없음 (허가 문서 링크만 제공) |
| 201207343 | 덱실란트디알캡슐30밀리그램(덱스란소프라졸) | 경질캡슐 (과립 충전) | 적응증 텍스트 없음 (허가 문서 링크만 제공) |
| 201802450 | 덱시라졸캡슐30밀리그램(덱스란소프라졸) | 경질캡슐 (과립 충전) | 적응증 텍스트 없음 (허가 문서 링크만 제공) |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 일부는 다음과 같습니다.
  - 주요(Major): Acalabrutinib, Atazanavir
  - 중등도(Moderate): Fosamprenavir, Foscarnet, Fostamatinib, Furosemide, Gefitinib, Hydrochlorothiazide, Amphotericin B, Amikacin, Amphetamine, Ampicillin, Bosutinib, Bumetanide 등
  - 경미(Minor): Acetylsalicylic acid, Axitinib, Brivaracetam, Cyanocobalamin 등

허가사항의 경고 및 금기 정보는 허가 문서를 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
위십이지장염에 대한 예측은 모델 점수에만 의존하며, 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 또한 작용 기전 데이터와 허가사항의 경고·금기 정보가 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가 문서에서 적응증, 경고 및 금기 정보 확보
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 위십이지장염에 대한 임상시험 또는 문헌 근거 탐색
- 기존 적응증과 예측 질환 간 유사성 분석 및 투여 경로 적합성 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

