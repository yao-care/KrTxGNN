---
layout: default
title: Bedaquiline
parent: 모델 예측만 (L5)
nav_order: 130
evidence_level: L5
indication_count: 4
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
last_modified_at: 2026-10-27
description: "Bedaquiline: 예측 신규 적응증 외음질 칸디다증 (vulvovaginal candidiasis) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201401310/EE"
---

# Bedaquiline
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

## Bedaquiline: 항결핵제(ATP 합성효소 억제) → 외음질 칸디다증 (vulvovaginal candidiasis)
{: .text-alpha }

## 한 문장 요약

Bedaquiline은 한국에서 단일 성분 제제로 허가된 약물입니다. TxGNN 모델은 **외음질 칸디다증(vulvovaginal candidiasis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201401310/EE |
| 예측 신규 적응증 | 외음질 칸디다증 (vulvovaginal candidiasis) |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 바에 따르면 bedaquiline의 표적은 마이코박테리아의 ATP 합성효소 소단위 c이며, 이는 검증된 항진균 표적이 아닙니다.

따라서 외음질 칸디다증에 적용할 수 있는 기전상 근거는 확립되어 있지 않습니다. 높은 예측 점수는 모델 내부의 연관 패턴에 따른 결과일 가능성이 크며, 임상적·문헌적 뒷받침은 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201401310 | 서튜러정100밀리그램(베다퀼린푸마르산염) | 흰색 내지 거의 흰색의 양면이 볼록한 원형 정제 | 허가 문서 링크만 제공되어 적응증 본문은 확인되지 않음 |

## 안전성 고려사항

- **약물 상호작용**: 이번 보고서용으로 수집된 데이터에서 총 100건의 상호작용이 확인되었습니다. 주요(Major) 등급으로 표시된 약물은 다음과 같습니다.
  - Dexamethasone
  - Clarithromycin
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)
  - Dolasetron
  - Palonosetron
  - Sodium sulfate
- 중등도(Moderate) 상호작용으로는 Acarbose, Famotidine, Doxycycline, Pioglitazone, Loperamide, Bupropion, Minocycline, Tetracycline, Naltrexone 등이 있습니다.

경고·금기 등 그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
외음질 칸디다증에 대한 임상시험과 문헌이 전혀 없고, 기전상 근거도 확립되어 있지 않습니다. 모델 점수만으로는 진행을 정당화하기 어렵습니다.

**진행하려면 필요한 것:**
- 항진균 활성에 대한 전임상(in vitro·in vivo) 근거
- 상세한 약물 작용 기전 데이터 (MOA)
- 허가사항의 경고·금기 정보 확보
- 주요 상호작용 약물에 대한 안전성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

