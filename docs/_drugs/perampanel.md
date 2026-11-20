---
layout: default
title: Perampanel
parent: 모델 예측만 (L5)
nav_order: 592
evidence_level: L5
indication_count: 1
monitor_inn: "PERAMPANEL"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-11-15
description: "Perampanel: 예측 신규 적응증 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) (근거 수준 L5). 기존 적응증: 1. 단독요법 - 부분발작: 뇌전증 환자의 이차성 전신발작을 동반하거나 동반하지 않는 부분발작의 치료(만…"
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
| 기존 적응증 | 1. 단독요법 - 부분발작: 뇌전증 환자의 이차성 전신발작을 동반하거나 동반하지 않는 부분발작의 치료(만 4세 이상) 2. 부가요법 - 부분발작: 뇌전증 환자의 이차성 전신발작을 동반하거나 동반하지 않는 부분발작의 치료(만 4세 이상) - 일차성 전신 강직-간대발작: 특발성 전신성… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201504770/EE)) |
| 예측 신규 적응증 | 베타-케토티올라제 결핍증 (beta-ketothiolase deficiency) |
| TxGNN 예측 점수 | 0.9979 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 19건 / 전체 19건) |
| 허가증 수 | 19건 (유효 19건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Perampanel 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “페람파넬은 시냅스후 뉴런에 있는 이온통로형 α-아미노-3-하이드록시-5-메틸-4-이속사졸프로피온산(AMPA) 글루타메이트 수용체의 비경쟁적 길항제이다. 글루타메이트는 중추신경계의 주요 흥분성 신경전달물질이며, 뉴런의 과흥분으로 인해 발생하는 여러 신경학적 질환에 관여한다.” 영어 원문: "Perampanel is a non-competitive antagonist of the ionotropic α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA) glutamate receptor on post-synaptic neurons. Glutamate is the primary excitatory neurotransmitter in the central nervous system and is implicated in a number of neurological disorders caused by neuronal over excitation." ([DailyMed: Fycompa (perampanel) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122), 버전 2022-12-28; 확인일 2026-11-19). 다만 Perampanel은 AMPA 수용체 길항 계열의 항경련제로 알려져 있습니다.

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

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Fycompa (perampanel) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

