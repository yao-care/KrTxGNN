---
layout: default
title: Arformoterol Tartrate
parent: 모델 예측만 (L5)
nav_order: 82
evidence_level: L5
indication_count: 5
drugbank_id: DB01274
monitor_inn: "Arformoterol"
predicted_indications: ["hyperlucent lung", "respiratory malformation", "tracheal stenosis", "Rienhoff syndrome", "tracheal calcification"]
last_modified_at: 2026-11-20
description: "Arformoterol Tartrate: 예측 신규 적응증 과투명 폐 (hyperlucent lung) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Arformoterol Tartrate
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

## Arformoterol Tartrate: 과투명 폐 (hyperlucent lung)
{: .text-alpha }

## 한 문장 요약

Arformoterol tartrate는 장기 지속형 베타2 아드레날린 작용제(LABA) 계열의 흡입제 성분이며, 허가 적응증은 현지 데이터에 기재되어 있지 않습니다.
TxGNN 모델은 **과투명 폐(hyperlucent lung)**에 효과가 있을 수 있다고 예측합니다(예측 점수 0.9975).
다만 이 방향을 직접 지지하는 임상시험과 문헌은 **0건**이며, 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202105306/EE) |
| 예측 신규 적응증 | 과투명 폐 (hyperlucent lung) |
| TxGNN 예측 점수 | 0.9975 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 허가되었으나 미시판 (수출용 허가만 유효: 1건 / 전체 1건) |
| 허가증 수 | 1건 (국내 0건 · 유효 0건 / 수출용 1건 · 유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Arformoterol Tartrate 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “포르모테롤의 (R,R)-거울상이성질체인 아포모테롤은 선택적 지속성 베타 2 -아드레날린 수용체 작용제(베타 2 -작용제)로서, 라세미 포르모테롤((S,S)- 및 (R,R)-거울상이성질체를 모두 포함)보다 2배 더 강력한 효력을 갖는다. (S,S)-거울상이성질체는 베타 2 -작용제로서 (R,R)-거울상이성질체보다 효력이 약 1,000배 약하다.” 영어 원문: "Arformoterol, the (R,R)-enantiomer of formoterol, is a selective long-acting beta 2 -adrenergic receptor agonist (beta 2 -agonist) that has two-fold greater potency than racemic formoterol (which contains both the (S,S) and (R,R)-enantiomers). The (S,S)-enantiomer is about 1,000-fold less potent as a beta 2 -agonist than the (R,R)-enantiomer." ([DailyMed: Arformoterol Tartrate Inhalation Solution (arformoterol tartrate) prescribing information, Aucta Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8c0d81db-fbf5-405f-9311-d3d78992d9a3), 버전 2025-02-11; 확인일 2026-11-19). 일반 약리학 지식에 따르면 arformoterol은 formoterol의 (R,R)-거울상이성질체로, 기관지 평활근을 이완시키는 장기 지속형 베타2 작용제입니다.

과투명 폐는 Swyer-James-MacLeod 증후군이나 폐기종성 변화처럼 폐 일부의 투과성이 증가해 보이는 영상 소견입니다. 흔히 폐쇄성 기도 질환을 동반하므로, 기관지 확장제가 동반된 기도 폐쇄 증상을 완화할 가능성은 있습니다.

그러나 이 연관성은 일반 약리학 지식에 근거한 추정일 뿐입니다. 높은 예측 점수는 모델 내에서 호흡기 질환 관련 항목과 가깝다는 의미이며, 이 약이 해당 소견을 치료한다는 근거가 아닙니다. 구조적 이상 자체를 교정하는 기전은 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202105306 | 코로빈액티베어(수출용) | 흡입제 (흰색 가루가 충전된 포낭을 원형 플라스틱 기구에 장착) | 현지 데이터에 기재되지 않음 |

이 허가는 수출용이며 국내 판매용 허가는 없습니다. 제조사는 한국유나이티드제약(주)입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 과투명 폐에 대한 임상시험과 문헌이 없어 근거 수준이 L5입니다. 높은 예측 점수만으로는 임상 적용을 뒷받침할 수 없습니다.
- 국내에는 수출용 허가만 있고, 작용 기전과 안전성 데이터도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서)의 경고 및 금기 정보 확보: 식약처 사이트에서 첨부문서를 내려받아 분석
- 작용 기전 데이터 보완: DrugBank 조회 등
- 과투명 폐 환자에서 베타2 작용제의 효과를 평가한 임상시험 또는 문헌 탐색
- 과투명 폐의 원인 질환(예: Swyer-James-MacLeod 증후군, 폐기종)별 적용 대상 정의와 안전성 검토
- 국내 판매용 허가 여부 및 제형·투여 경로 적합성 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Arformoterol Tartrate Inhalation Solution (arformoterol tartrate) prescribing information, Aucta Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8c0d81db-fbf5-405f-9311-d3d78992d9a3) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

