---
layout: default
title: Clomifene
parent: 모델 예측만 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
monitor_inn: "Clomifene"
predicted_indications: ["46,XY disorder of sex development due to testicular steroidogenesis defect", "longitudinal vaginal septum", "transverse vaginal septum", "symptomatic form of fragile X syndrome in female carrier", "blepharophimosis-epicanthus inversus-ptosis", "blepharophimosis-epicanthus inversus-ptosis due to 3q23 rearrangement syndrome", "partial trisomy/tetrasomy of the short arm of chromosome 18", "partial trisomy/tetrasomy of the short arm of chromosome 5", "partial trisomy/tetrasomy of the short arm of chromosome 12", "ovarian remnant syndrome"]
last_modified_at: 2026-10-31
description: "Clomifene: 예측 신규 적응증 46,XY disorder of sex development due to testicular steroidogenesis defect (근거 수준 L5). 기존 적응증: 허가 적응증 본문 확인 불가 (허가 문서 링크만 확인됨)"
---

# Clomifene
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Clomifene: 기존 적응증 정보 확인 불가에서 46,XY disorder of sex development due to testicular steroidogenesis defect로
{: .text-alpha }

## 한 문장 요약

Clomifene은 한국에서 허가된 단일 성분 제제(영풍클로미펜시트르산염정)가 있으나, 이번 보고서용으로 정리된 데이터에는 허가 적응증의 본문이 포함되어 있지 않습니다(링크 주소만 확인됨). TxGNN 모델은 **46,XY 성분화 이상(고환 스테로이드 생성 결함)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 뒷받침하는 **임상시험과 문헌은 각각 0건**입니다. 따라서 근거 수준은 L5(모델 예측만 존재)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 확인 불가 (허가 문서 링크만 확인됨) |
| 예측 신규 적응증 | 46,XY 성분화 이상(고환 스테로이드 생성 결함 기인) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 DrugBank 등에서 확보되지 않았습니다. 다만 약리학 데이터에는 Clomifene이 에스트로겐 수용체 알파(ESR1)에 작용하는 선택적 에스트로겐 수용체 조절제로 기록되어 있습니다. 이 약은 시상하부의 에스트로겐 음성 되먹임을 차단하여 GnRH, LH, FSH 분비를 높이며, 배란 장애에 의한 여성 불임(예: 다낭성 난소 증후군) 치료에 쓰이는 것으로 알려져 있습니다.

이론적으로는 높아진 성선자극호르몬이 잔존 라이디히 세포의 스테로이드 생성을 자극할 수 있습니다. 그러나 이 질환은 스테로이드 합성 효소 자체의 결함이므로 성선자극호르몬을 늘려도 반응하기 어렵습니다. 예측 점수는 높지만 기전은 추측 수준입니다.

참고로 2~10위 예측(세로 질중격, 가로 질중격, 취약 X 증후군 여성 보인자, BPES 및 하위형, 염색체 부분 삼염색체/사염색체, 난소 잔존 증후군)도 모두 L5이며 Hold입니다. 대부분 구조 이상이나 염색체 이상으로 약물 기전과 연결되지 않으며, 이 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영한 것일 수 있고 생물학적 근거는 아닙니다. 특히 난소 잔존 증후군은 잔존 조직을 자극해 증상을 악화시킬 수 있어 안전성 우려가 큽니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199502153 | 영풍클로미펜시트르산염정 | 등황색 원형 정제 | 적응증 본문 확인 불가 (허가 문서 링크만 확인됨) |

## 안전성 고려사항

- **약물 상호작용**: 총 3건이 조회되었습니다.
  - Bexarotene: 주요(Major) 등급 상호작용 (DDInter)
  - 에스트로겐 수용체 알파(ESR1) 및 VRAC: 약리학적 표적 정보이며 등급은 제시되지 않았습니다.
- 난소 잔존 증후군 예측에 대해서는 성선자극호르몬 자극으로 통증이나 낭종 등 증상이 악화될 수 있다는 우려가 있습니다.

허가사항의 경고 및 금기는 확보되지 않았으므로 허가사항(패키지 인서트)을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환에 대한 임상시험과 문헌이 모두 없고 기전도 추측 수준이어서 L5에 해당합니다. 또한 허가 적응증 본문과 경고·금기 정보가 없어 안전성 1차 검토도 진행할 수 없습니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(PDF)에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 상위 예측 질환(고환 스테로이드 생성 결함 등)에 대한 직접적인 임상시험 및 문헌 조사
- 시판 상태(허가 취소 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

