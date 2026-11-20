---
layout: default
title: Safinamide
parent: 모델 예측만 (L5)
nav_order: 679
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-15
description: "Safinamide: 예측 신규 적응증 라스무센 아급성 뇌염 (Rasmussen subacute encephalitis) (근거 수준 L5). 기존 적응증: 운동 동요 증상(end of dose motor fluctuations)이 있는 특발성 파킨슨병 환자에서…"
monitor_inn: "safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Safinamide
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

## Safinamide: 파킨슨병 치료제에서 라스무센 아급성 뇌염으로
{: .text-alpha }

## 한 문장 요약

Safinamide는 한국에서 에퀴피나필름코팅정50밀리그램(사피나미드메실산염)으로 허가된 약으로, 허가 적응증의 상세 내용은 이번 자료에서 확인되지 않았습니다. 일반적으로 MAO-B 억제제로서 파킨슨병 치료에 사용되는 것으로 알려져 있습니다.
TxGNN 모델은 **라스무센 아급성 뇌염(Rasmussen subacute encephalitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 운동 동요 증상(end of dose motor fluctuations)이 있는 특발성 파킨슨병 환자에서 레보도파 함유 제제의보조요법 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202004635/EE)) |
| 예측 신규 적응증 | 라스무센 아급성 뇌염 (Rasmussen subacute encephalitis) |
| TxGNN 예측 점수 | 0.9963 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Safinamide 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “PD에서 XADAGO가 치료 효과를 나타내는 정확한 기전은 알려져 있지 않다. XADAGO는 모노아민 산화효소 B(MAO-B)의 억제제이다. MAO-B 활성의 억제는 도파민의 이화작용을 차단함으로써 뇌에서 도파민 농도의 증가와 그에 따른 도파민성 활성의 증가를 초래하는 것으로 생각된다.” 영어 원문: "The precise mechanism by which XADAGO exerts its therapeutic effects in PD is unknown. XADAGO is an inhibitor of monoamine oxidase B (MAO-B). Inhibition of MAO-B activity, by blocking the catabolism of dopamine, is thought to result in an increase in dopamine levels and a subsequent increase in dopaminergic activity in the brain." ([DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2), 버전 2026-10-05; 확인일 2026-11-19). 다만 이번 평가에서 정리된 기전 분석에 따르면, safinamide는 가역적 MAO-B 억제제이며 전압 의존성 나트륨 채널 차단과 글루탐산 방출 억제 작용도 가지는 것으로 알려져 있습니다.

라스무센 뇌염은 T세포 매개 신경염증으로 만성 국소 발작과 진행성 편측 대뇌 위축이 나타나는 질환입니다. 글루탐산 과다와 흥분독성이 병태에 기여할 수 있어, safinamide의 나트륨 채널 및 글루탐산 조절 작용이 항경련 또는 신경보호 측면에서 이론적 근거가 될 수 있습니다.

그러나 면역 매개 병리 자체에 영향을 준다는 직접적인 근거는 없습니다. 0.9963이라는 높은 점수는 계산상 예측일 뿐이며, 임상시험이나 문헌의 뒷받침이 없습니다.

### 다른 예측 후보

| 순위 | 예측 질환 | TxGNN 점수 | 근거 수준 | 기전상 연관성 요약 |
|------|----------|-----------|----------|------------------|
| 2 | 척수염 (myelitis) | 0.9946 | L5 | MAO-B 억제의 산화 스트레스 감소와 글루탐산 조절로 신경보호 가능성은 있으나, 염증성 탈수초와의 연결은 추측 수준입니다. |
| 3 | PLA2G6 관련 신경변성 (PLAN) | 0.9922 | L5 | 알파-시누클레인 병리와 파킨슨증 표현형이 파킨킨병과 일부 겹쳐 증상 완화 가능성은 있으나, 질병 경과 변화 근거는 없습니다. |

두 후보 모두 임상시험과 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202004635 | 에퀴피나필름코팅정50밀리그램(사피나미드메실산염) | 백색의 양면이 볼록한 원형 필름코팅정 | 허가증 문서 참조 (한국에자이(주), 단일제, 유효) |

## 안전성 고려사항

- **약물 상호작용**: DDI 조회 결과 총 110건이 확인되었으며, 이 중 주요 항목은 다음과 같습니다.
  - **Major**: Bupropion
  - **Moderate**: 인슐린 제제 전반(insulin aspart, degludec, detemir, glargine, glulisine, human isophane/regular/inhalation), 설폰요소제 및 혈당강하제(chlorpropamide, glimepiride, acetohexamide, nateglinide, repaglinide, empagliflozin), 식욕억제제(phentermine, diethylpropion), isometheptene, metoclopramide, rosuvastatin

허가사항상의 경고 및 금기는 이번 자료에서 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
세 가지 예측 질환 모두 근거 수준이 L5로, 임상시험과 문헌 없이 TxGNN 모델 점수에만 의존하고 있습니다. 허가 적응증과 작용 기전, 허가사항상 안전성 정보도 확인되지 않아 현 단계에서는 진행을 판단하기 어렵습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항 문서를 내려받아 허가 적응증, 경고, 금기 확인 (안전성 스크리닝의 필수 선행 조건)
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 라스무센 뇌염, 척수염, PLA2G6 관련 신경변성에 대한 임상시험 및 문헌 추가 검색
- 경구 투여 외 필요한 투여 경로 및 제형 적합성 평가
- 병용 가능성이 높은 약물(인슐린, 혈당강하제, bupropion 등)에 대한 상호작용 관리 계획

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Xadago (safinamide mesylate) prescribing information, MDD US Operations LLC, a subsidiary of Supernus Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4d65f28-983f-42b4-bb23-023ae0fe81b2) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

