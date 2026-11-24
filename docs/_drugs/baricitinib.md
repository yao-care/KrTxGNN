---
layout: default
title: Baricitinib
parent: 모델 예측만 (L5)
nav_order: 125
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Baricitinib: 예측 신규 적응증 콜로보마성 소안구증-근위지단 이형성 증후군 (colobomatous microphthalmia-rhizomelic dyspl… (근거 수준 L5). 기존 적응증: 다음의 환자에서는 기존 치료제에 적절히 반응하지 않거나 내약성이 없는 경우에 한하여 이 약을 사용하여야한다…"
monitor_inn: "BARICITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Baricitinib
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

## Baricitinib: 허가 적응증에서 콜로보마성 소안구증-근위지단 이형성 증후군으로
{: .text-alpha }

## 한 문장 요약

Baricitinib은 한국에서 올루미언트정(1mg, 2mg, 4mg)으로 시판 중인 단일제입니다. TxGNN 모델은 **콜로보마성 소안구증-근위지단 이형성 증후군(colobomatous microphthalmia-rhizomelic dysplasia syndrome)**에 효과가 있을 수 있다고 예측했습니다. 그러나 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음의 환자에서는 기존 치료제에 적절히 반응하지 않거나 내약성이 없는 경우에 한하여 이 약을 사용하여야한다. (3. 원형 탈모증은 제외) -다음­ 가. 65세 이상 환자 나. 심혈관계 고위험군 환자 다. 악성 종양 위험이 있는 환자 1. 류마티스 관절염 하나 이상의… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201708281/EE)) |
| 예측 신규 적응증 | 콜로보마성 소안구증-근위지단 이형성 증후군 (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| TxGNN 예측 점수 | 0.9994 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Baricitinib 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “바리시티닙은 야누스 키나아제(JAK) 저해제이다. JAK는 세포막에서 사이토카인 또는 성장인자-수용체 상호작용으로 발생하는 신호를 전달하여 조혈 및 면역세포 기능의 세포 과정에 영향을 미치는 세포내 효소이다.” 영어 원문: "Baricitinib is a Janus kinase (JAK) inhibitor. JAKs are intracellular enzymes which transmit signals arising from cytokine or growth factor-receptor interactions on the cellular membrane to influence cellular processes of hematopoiesis and immune cell function." ([DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf), 버전 2026-10-09; 확인일 2026-11-19). 다만 Baricitinib은 일반적으로 JAK1/JAK2 억제제로 알려져 있으며, 염증성 JAK-STAT 신호 전달을 차단하는 약물입니다.

예측된 신규 적응증은 안구와 사지 뼈의 발생 이상을 특징으로 하는 희귀 발달 증후군입니다. 이 질환과 JAK-STAT 신호 전달 사이에서 이번에 확인된 자료만으로는 타당한 기전적 연결고리를 찾을 수 없습니다. 이런 증후군은 보통 발생 과정이나 유전적 원인으로 생기므로, 염증 경로를 억제한다고 교정될 것으로 기대하기 어렵습니다.

따라서 이 예측은 생물학적 근거보다는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 점수일 가능성이 큽니다. 가설을 세우는 참고 신호로만 보는 것이 적절합니다.

같은 분석에서 두 번째로 제시된 예측은 **손발가락 단지증-합지증 증후군(brachydactyly-syndactyly syndrome, 점수 0.9994)**이며, 이 역시 임상시험과 문헌 근거가 없고 같은 이유로 보류 대상입니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201708281 | 올루미언트정4밀리그램(바리시티닙) | 한면에는 “Lilly”, 다른 면에는 “4”가 음각된 분홍색의 원형 필름… | 한국릴리(유) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201708281/EE) | 유효 |
| 201708280 | 올루미언트정2밀리그램(바리시티닙) | 한면에는 “Lilly”, 다른 면에는 “2”가 음각된 밝은 분홍색의 타원… | 한국릴리(유) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201708280/EE) | 유효 |
| 202402172 | 올루미언트정1밀리그램(바리시티닙) | 한면에는 “Lilly”, 다른 면에는 “1”이 음각된 매우 밝은 분홍색의… | 한국릴리(유) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402172/EE) | 유효 |

<!-- licenses:end -->

제조사는 모두 한국릴리(유)입니다(허가 건수와 상태는 빠른 개요와 위 표 참조).

<!-- review:begin kr-lic-20261124c-baricitinib-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “제조사는 모두 한국릴리(유)이며, 3건 모두 유효한 단일제 허가입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-baricitinib-1 -->

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: 코르티코스테로이드 계열(Hydrocortisone, Triamcinolone, Betamethasone, Budesonide, Dexamethasone, Prednisolone, Prednisone), Deferiprone, 방사성의약품(Ibritumomab tiuxetan, Iobenguane I-131, Tositumomab I-131)
  - **Moderate**: Morphine, Acetylsalicylic acid(아스피린), Nitisinone, Opium
  - **Minor**: 아연 제제(Zinc acetate, gluconate, sulfate)

그 외 경고·금기 등 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없어 근거 수준이 L5에 머뭅니다. 또한 JAK-STAT 억제와 이 희귀 발달 증후군을 잇는 기전적 연결고리를 확인할 수 없습니다.

**진행하려면 필요한 것:**
- 허가 문서(첨부문서)의 적응증, 경고, 금기 정보 확보 및 분석
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 예측 질환의 병태생리와 JAK-STAT 경로 간 연관성에 대한 전임상·기전 연구 근거
- 관련 임상시험 및 문헌 탐색 (현재 등록 건 없음)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf) |
| 2026-11-24 | 단일·복합 표기: “제조사는 모두 한국릴리(유)이며, 3건 모두 유효한 단일제 허가입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

