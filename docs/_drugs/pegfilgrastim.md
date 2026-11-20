---
layout: default
title: Pegfilgrastim
parent: 모델 예측만 (L5)
nav_order: 582
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Pegfilgrastim: 예측 신규 적응증 중증 비증식성 당뇨망막병증 (severe nonproliferative diabetic retinopathy) (근거 수준 L5). 기존 적응증: 악성 종양에 대한 세포독성 화학요법을 투여 받는 환자의 발열성 호중구감소증의 발생과 호중구감소증의 기간…"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
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

## Pegfilgrastim: 허가 적응증 확인 필요에서 중증 비증식성 당뇨망막병증으로
{: .text-alpha }

## 한 문장 요약

Pegfilgrastim은 장기 지속형 G-CSF(과립구 집락자극인자) 제제로 한국에서 시판 중이지만, 허가 적응증 본문은 이번에 정리된 데이터에서 확인되지 않았습니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(severe nonproliferative diabetic retinopathy)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험과 문헌은 0건**으로 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 악성 종양에 대한 세포독성 화학요법을 투여 받는 환자의 발열성 호중구감소증의 발생과 호중구감소증의 기간 감소 (만성 골수성 백혈병과 골수이형성증후군은 제외함) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202400068/EE)) |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (severe nonproliferative diabetic retinopathy) |
| TxGNN 예측 점수 | 0.9989 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Pegfilgrastim 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “페그필그라스팀 제품은 특정 세포 표면 수용체에 결합하여 조혈세포에 작용하는 집락자극인자로서, 이를 통해 증식, 분화, 분화 결정(commitment) 및 최종 세포의 기능적 활성화를 자극한다.” 영어 원문: "Pegfilgrastim products are colony-stimulating factor that acts on hematopoietic cells by binding to specific cell surface receptors, thereby stimulating proliferation, differentiation, commitment, and end cell functional activation." ([DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83), 버전 2026-10-29; 확인일 2026-11-19). 알려진 정보에 따르면 Pegfilgrastim은 호중구 생성을 촉진하는 장기 지속형 G-CSF이며, 조혈 전구세포와 내피 전구세포를 동원하는 것으로 알려져 있습니다.

이 특성에서 망막 혈관 회복과의 연관성을 가설로 세울 수 있습니다. 그러나 이번 데이터에서는 이를 뒷받침하는 근거가 없습니다. 반대로 G-CSF가 유발하는 염증과 신생혈관 형성이 망막 병변을 악화시킬 수도 있어 효과의 방향 자체가 불확실합니다. 따라서 이 연관성은 추측 단계이며 전임상 및 기전 연구를 통한 검증이 필요합니다.

참고로 상위 범주인 **당뇨망막병증(diabetic retinopathy)**도 점수 0.9973로 함께 예측되었습니다. 두 예측은 포괄 관계이므로 독립된 근거로 볼 수 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202400068 | 싸이쎄그프리필드시린지주6mg/0.6mL (싸이젠코리아) | 프리필드시린지 주사제 | 본문 미확인 (허가사항 문서 참조) |
| 201203772 | 뉴라스타프리필드시린지주 (한국쿄와기린) | 프리필드시린지 주사제 | 본문 미확인 (허가사항 문서 참조) |

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었으며, 이 중 일부 상세 항목은 모두 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 항암제 및 세포독성 약물: Paclitaxel, Mercaptopurine, Azacitidine, Arsenic trioxide, Altretamine, Trimetrexate, Abemaciclib
  - 면역·항체 치료제: Alemtuzumab, Aldesleukin, Belantamab mafodotin, Asparaginase
  - 방사성 의약품: Iobenguane (I-131), Tositumomab (I-131), Ibritumomab tiuxetan, Fludeoxyglucose (18F)
  - 기타: Pegvaliase, Levamisole, Acalabrutinib, Avapritinib

주요 경고와 금기는 이번 데이터에서 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없는 L5 단계입니다. 작용 기전 데이터와 허가 경고·금기 정보도 확보되지 않았고, G-CSF가 망막 병변을 악화시킬 가능성도 배제할 수 없어 현 시점에서 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항 문서에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 당뇨망막병증 모델에서 G-CSF의 효과와 병적 신생혈관 형성 위험을 평가하는 전임상·기전 연구
- 관련 임상시험 및 문헌 재검색
- 투여 경로 적합성 평가 (이번 데이터에서는 미확인)

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

