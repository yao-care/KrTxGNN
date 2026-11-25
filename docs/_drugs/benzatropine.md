---
layout: default
title: Benzatropine
parent: 모델 예측만 (L5)
nav_order: 135
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Benzatropine: 예측 신규 적응증 PLA2G6 연관 신경변성 (PLA2G6-associated neurodegeneration) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 이번 자료에서 확인되지 않았습니다. 허가증에는 문서 링크만 있습니다. 항콜린제로서 파킨슨증과 약물 유발…"
monitor_inn: "benzatropine"
predicted_indications: ["PLA2G6-associated neurodegeneration", "attention deficit-hyperactivity disorder"]
---

# Benzatropine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Benzatropine: 파킨슨증 치료제에서 PLA2G6 연관 신경변성으로
{: .text-alpha }

## 한 문장 요약

Benzatropine은 항콜린제로, 한국에서 허가를 받아 시판 중입니다(허가 건수와 상태는 빠른 개요 참조). TxGNN 모델은 **PLA2G6 연관 신경변성(PLA2G6-associated neurodegeneration)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험과 문헌은 없습니다**. 따라서 이 예측은 모델 점수에만 의존하는 가설 단계입니다.

<!-- review:begin kr-lic-20261124c-benzatropine-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Benzatropine은 항콜린제로, 한국에서 4건의 단일제 허가를 받아 시판 중입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-benzatropine-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 이번 자료에서 확인되지 않았습니다. 허가증에는 문서 링크만 있습니다. 항콜린제로서 파킨슨증과 약물 유발 추체외로 증상에 사용되는 약물입니다. |
| 예측 신규 적응증 | PLA2G6 연관 신경변성 (PLA2G6-associated neurodegeneration) |
| TxGNN 예측 점수 | 0.9917 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

> 참고: 두 번째 예측 적응증은 주의력결핍 과잉행동장애(ADHD, 점수 0.9903)이며, 마찬가지로 L5, Hold입니다. 이 보고서는 1순위 예측을 중심으로 작성했습니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Benzatropine 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “벤즈트로핀 메실산염은 항콜린 작용과 항히스타민 작용을 모두 가지고 있으나, 파킨슨증 치료에서 치료적으로 유의한 것으로 확립된 것은 전자뿐이다. 적출한 기니피그 회장에서 이 약물의 항콜린 활성은 아트로핀과 거의 같으나, 마취하지 않은 고양이에게 경구 투여한 경우에는 아트로핀 활성의 약 절반에 불과하다.” 영어 원문: "Benztropine mesylate possesses both anticholinergic and antihistaminic effects, although only the former have been established as therapeutically significant in the management of parkinsonism. In the isolated guinea pig ileum, the anticholinergic activity of this drug is about equal to that of atropine; however, when administered orally to unanesthetized cats, it is only about half as active as atropine." ([DailyMed: benztropine mesylate prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=01688e6f-7b22-41bf-9a85-1c88d90f99b6), 버전 2026-11-11; 확인일 2026-11-19). 알려진 정보에 따르면 benzatropine은 무스카린 수용체 길항 작용을 하는 항콜린제이며, 도파민 재흡수도 억제합니다. 파킨슨증과 약물 유발 추체외로 증상에 사용됩니다.

PLA2G6 연관 신경변성에는 영아기 신경축삭 이영양증과 PLA2G6 관련 근긴장이상-파킨슨증이 포함됩니다. 이 질환은 근긴장이상과 파킨슨양 증상으로 나타날 수 있습니다. 따라서 운동 증상을 완화하는 대증 치료로 쓰일 수 있다는 가설은 그럴듯하지만, 검증되지는 않았습니다.

다만 benzatropine이 PLA2G6 결핍, 지질 대사 이상, 신경변성 자체를 변화시킬 것으로는 기대하기 어렵습니다. 기존 적응증과의 유사성 평가도 아직 이루어지지 않았습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 198500629 | 명인벤즈트로핀메실산염정2밀리그램 | 흰색의 원형정제 | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198500629/EE) | 유효 |
| 198600614 | 명인벤즈트로핀메실산염정1밀리그램 | 흰색 원형의 정제 | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198600614/EE) | 유효 |
| 197100097 | 환인벤즈트로핀정(벤즈트로핀메실산염) | 백색의 원형정제 | 환인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197100097/EE) | 유효 |
| 198700736 | 환인벤즈트로핀정1밀리그램(벤즈트로핀메실산염) | 황색의 원형정제 | 환인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198700736/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 확보되지 않았습니다. 상세 내용은 허가사항을 참조하세요.

- **지식그래프 기반 금기 질환(허가문서가 아닌 모델 지식그래프 기준)**: 폐쇄각 녹내장과 개방각 녹내장, 양성 전립선 비대증, 마비성 장폐색, 중증 근무력증, 궤양성 대장염과 염증성 장질환, 이완불능증(achalasia), 관상동맥질환, 심장 전도 질환, 만성 폐쇄성 폐질환, 신장·간·담낭 질환, 고혈압과 저혈압, 위궤양, C. difficile 대장염 등이 있습니다.
- **약물 상호작용**: 총 78건이 확인되었습니다. 이 중 **주요(Major)** 등급은 염화칼륨과 구연산칼륨입니다. 중등도(Moderate) 등급에는 다음이 포함됩니다.
  - 다른 항콜린제: atropine, hyoscyamine, dicyclomine, glycopyrronium 등
  - 오피오이드: morphine, opium, loperamide 등
  - 기타: metoclopramide, dronabinol, nabilone, pramlintide 등
- **ADHD 예측과 관련한 우려**: 항콜린 작용은 주의력과 기억력 저하, 오남용 가능성과 연관됩니다. 소아 환자가 많은 질환이라 안전성 문제가 더 중요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
PLA2G6 연관 신경변성에 대한 임상시험과 문헌이 없고 TxGNN 점수(0.9917)만 있어 L5 수준입니다. 기대할 수 있는 효과도 질환 수정이 아니라 운동 증상의 대증 완화에 그칩니다.

**진행하려면 필요한 것:**
- 허가 적응증, 경고, 금기를 확인하기 위한 허가사항 문서(MFDS 첨부문서) 확보
- 작용 기전(MOA) 데이터 보강(DrugBank 조회)
- PLA2G6 연관 신경변성에서 항콜린제 사용에 관한 문헌과 임상시험 탐색
- 근긴장이상-파킨슨증 환자군에서의 증상 완화 가능성을 검증하는 소규모 탐색 연구 설계
- 소아 환자와 병용약물을 고려한 안전성 평가 계획(항콜린 부담, 상호작용 포함)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: benztropine mesylate prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=01688e6f-7b22-41bf-9a85-1c88d90f99b6) |
| 2026-11-24 | 단일·복합 표기: “Benzatropine은 항콜린제로, 한국에서 4건의 단일제 허가를 받아…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

