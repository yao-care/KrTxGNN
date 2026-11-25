---
layout: default
title: Mirtazapine
parent: 모델 예측만 (L5)
nav_order: 519
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-25
description: "Mirtazapine: 예측 신규 적응증 Ohdo 증후군 및 변이형 (Ohdo syndrome and variants) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 데이터에 포함되어 있지 않습니다(허가증 PDF 링크만 있음). 허가사항을 참조하세요"
monitor_inn: "MIRTAZAPINE"
predicted_indications: ["Ohdo syndrome and variants", "blepharophimosis - intellectual disability syndrome, Ohdo type", "benign paroxysmal torticollis of infancy"]
---

# Mirtazapine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

## Mirtazapine: 우울증 치료제에서 Ohdo 증후군 및 변이형으로
{: .text-alpha }

## 한 문장 요약

Mirtazapine은 한국에서 항우울제로 허가되어 시판 중인 단일성분 의약품입니다. TxGNN 모델은 **Ohdo 증후군 및 변이형(Ohdo syndrome and variants)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 모델 예측 점수만 있는 상태입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 데이터에 포함되어 있지 않습니다(허가증 PDF 링크만 있음). 허가사항을 참조하세요. |
| 예측 신규 적응증 | Ohdo 증후군 및 변이형 (Ohdo syndrome and variants) |
| TxGNN 예측 점수 | 0.9942 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

> 참고: 이 데이터에서는 허가 적응증 텍스트가 문서 링크로만 제공되어 구체적인 적응증을 확인할 수 없습니다. 제목의 "우울증"은 mirtazapine의 일반적인 약리 분류에 근거한 것이므로, 허가사항에서 확인이 필요합니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Mirtazapine 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “미르타자핀의 주요 우울장애 치료 작용기전은 명확하지 않다. 그러나 그 효능은 중추 시냅스전 α 2 -아드레날린성 억제성 자가수용체 및 이종수용체에 대한 길항제로서의 작용과 중추 노르아드레날린성 및 세로토닌성 활성의 증강을 통해 매개될 수 있다.” 영어 원문: "The mechanism of action of mirtazapine for the treatment of major depressive disorder, is unclear. However, its efficacy could be mediated through its activity as an antagonist at central presynaptic α 2 -adrenergic inhibitory autoreceptors and heteroreceptors and enhancing central noradrenergic and serotonergic activity." ([DailyMed: Remeronsoltab (mirtazapine) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98ad1917-a094-44f5-a28f-a64a8cfcd887), 버전 2025-08-06; 확인일 2026-11-19). 알려진 정보에 따르면 mirtazapine은 알파-2 아드레날린 수용체 길항 작용과 5-HT2/5-HT3, H1 수용체 길항 작용을 가진 약물입니다.

Ohdo 증후군(KAT6B 관련 변이 포함)은 지적장애와 안검열 축소를 특징으로 하는 희귀 유전질환으로, 염색질 조절과 발달 경로 이상이 원인입니다. Mirtazapine의 수용체 약리와 이 질환의 병태 사이에서 기전상 타당한 연결고리를 확인할 수 없습니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 생물학적 근거라기보다 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 높습니다.

같은 모델이 예측한 다른 후보인 "blepharophimosis - intellectual disability syndrome, Ohdo type"(점수 0.9911)은 위 질환과 사실상 같은 질환이므로 독립적인 근거로 볼 수 없습니다. "영아기 양성 발작성 사경"(점수 0.9911)은 편두통 계열 질환과의 연관성을 추측할 수는 있으나, 제공된 데이터로는 뒷받침되지 않습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200603875 | 레메론정15밀리그램(미르타자핀) | 미황색의 필름코팅 타원형 정제 | 한국오가논(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200603875/EE) | 유효 |
| 200808414 | 레메론정30밀리그램(미르타자핀) | 적갈색의 필름코팅 타원형 정제 | 한국오가논(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200808414/EE) | 유효 |
| 201707054 | 미르젠탁정15밀리그램(미르타자핀) | 미황색의 타원형 필름코팅정제 | 환인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707054/EE) | 유효 |
| 201601663 | 밀타오디정7.5밀리그램(미르타자핀) | 흰색의 원형 구강붕해 정제 | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201601663/EE) | 유효 |
| 200803427 | 미르탁스오디티정30밀리그램(미르타자핀) | 고유의 향이 있는 양면이 편평한 흰색 원형 속붕해성 정제 | 삼일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200803427/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

이 외에도 필름코팅정과 구강붕해정을 포함한 유효 허가가 더 있습니다(허가 건수와 상태는 빠른 개요 참조).

<!-- review:begin kr-lic-20261125c-mirtazapine-1 -->

> **검토 정정 (2026-11-25)**: 원래 문장: “이 외에도 필름코팅정과 구강붕해정을 포함해 총 20건의 유효 허가가 있습니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-25 데이터) 기준으로 수정했습니다: 이 페이지의 자료는 허가의 일부만 수록하고 있어(빠른 개요에 「최소 …건」으로 표시), 본문에 쓴 건수가 전체 건수가 아닙니다. 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261125c-mirtazapine-1 -->

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건입니다. 이 중 확인된 **주요(Major)** 등급은 다음과 같습니다.
  - Bupropion
  - Lorcaserin
  - Dolasetron
  - Palonosetron
  
  Famotidine, Loperamide, Aprepitant, Morphine, Dexamethasone, Cimetidine, Clarithromycin, Levofloxacin 등은 **중등도(Moderate)** 등급입니다.
- **지식 그래프상 금기 관련 질환** (라벨 문구가 아닌 모델 지식 그래프 기반): 간질, 조증 양극성 정동장애, 간질환, 담낭질환, 호중구감소증, 무과립구증, 기립성 저혈압, 고중성지방혈증, 비만, 뇌졸중 및 뇌혈관질환, 심근경색, 신기능 장애, 세로토닌 증후군, 약물 유발 좌불안석 등.
- **소아 사용 관련**: 영아기 양성 발작성 사경 예측과 관련해, mirtazapine은 젊은 환자에서 자살 관련 경고가 있는 약물입니다. 제공된 데이터는 소아 사용을 뒷받침하지 않습니다.

허가사항의 경고 및 금기 상세 내용은 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험과 문헌이 전혀 없고, 약물의 기전과 질환의 병태 사이에 타당한 연결도 확인되지 않습니다. 따라서 모델 예측만 있는 L5 수준이며, 이 점수는 TxGNN 모델(딥러닝)에서 나온 것으로 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 수 있고 생물학적 근거는 아닙니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서)에서 경고·금기·적응증 확인 (현재 안전성 선별 단계로 진행 불가)
- 상세한 약물 작용 기전(MOA) 데이터 확보
- Ohdo 증후군 및 관련 질환과 mirtazapine의 기전적 연결고리에 대한 전임상 또는 문헌 근거
- 소아 대상 사용 시 위험-이익 평가 및 안전성 모니터링 계획

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Remeronsoltab (mirtazapine) prescribing information, Organon LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98ad1917-a094-44f5-a28f-a64a8cfcd887) |
| 2026-11-25 | 허가 건수: “이 외에도 필름코팅정과 구강붕해정을 포함해 총 20건의 유효 허가가 있습니다.” → 건수를 쓰지 않도록 수정(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

