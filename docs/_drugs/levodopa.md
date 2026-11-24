---
layout: default
title: Levodopa
parent: 모델 예측만 (L5)
nav_order: 472
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Levodopa: 예측 신규 적응증 라스무센 아급성 뇌염 (Rasmussen subacute encephalitis) (근거 수준 L5). 기존 적응증: 레보도파/도파탈탄산효소(Dopadecarboxylase ; DDC) 억제제 표준치료제로 개선되지 않는…"
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
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

## Levodopa: 파킨슨병에서 라스무센 아급성 뇌염으로
{: .text-alpha }

## 한 문장 요약

Levodopa는 도파민 전구체로, 한국에서 카르비도파·엔타카폰 또는 벤세라지드와의 복합 형태로 허가되어 시판 중입니다.
TxGNN 모델은 **라스무센 아급성 뇌염(Rasmussen subacute encephalitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험은 0건**, **문헌도 0편**입니다. 근거는 모델 예측 점수뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 레보도파/도파탈탄산효소(Dopadecarboxylase ; DDC) 억제제 표준치료제로 개선되지 않는 파킨슨씨병 환자의 운동 동요 증상(end-of-dose motor fluctuations)의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201506801/EE)) |
| 예측 신규 적응증 | 라스무센 아급성 뇌염 (Rasmussen subacute encephalitis) |
| TxGNN 예측 점수 | 0.9906 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Levodopa 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “도파민의 대사 전구체인 레보도파는 혈액-뇌 장벽을 통과하며, 뇌에서 도파민으로 전환되는 것으로 추정된다. 이것이 레보도파가 파킨슨병의 증상을 완화하는 기전으로 생각된다.” 영어 원문: "Levodopa, the metabolic precursor of dopamine, crosses the blood-brain barrier and presumably is converted to dopamine in the brain. This is thought to be the mechanism whereby levodopa relieves symptoms of Parkinson's disease." ([DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb), 버전 2026-07-20; 확인일 2026-11-19). 알려진 정보에 따르면 Levodopa는 도파민 전구체로서 뇌 내에서 도파민으로 전환되어 도파민 결핍을 보충하며, 말초 탈카르복실화 억제제(카르비도파, 벤세라지드)나 COMT 억제제(엔타카폰)와 복합되어 사용됩니다.

라스무센 뇌염은 T세포 매개 신경 손상, 난치성 국소 발작, 진행성 편측 대뇌 위축을 특징으로 하는 희귀 만성 염증성 뇌질환입니다. 도파민 보충이 이 면역 매개 병리를 직접 설명할 기전적 근거는 확인되지 않습니다. 도파민계의 신경염증 조절이나 운동 증상 완화를 통한 간접적 연관을 가정할 수는 있으나 추측에 불과하며, 이번 데이터만으로는 검증할 수 없습니다. 높은 TxGNN 점수 외에 이 예측을 뒷받침하는 자료가 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201506801 | 트리도파정50/12.5/200밀리그램 | 적갈색의 원형 필름코팅정 | 제일약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201506801/EE) | 유효 |
| 201504271 | 트리도파정125/31.25/200밀리그램 | 밝은 적갈색의 타원형 필름코팅정 | 제일약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201504271/EE) | 유효 |
| 201506120 | 트리레보정75/18.75/200밀리그램(레보도파, 카르비도파, 엔타카폰) | 밝은 적갈색의 타원형 필름코팅정 | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201506120/EE) | 유효 |
| 202502529 | 원도파정50/200밀리그램(벤세라지드, 레보도파) | 십자눈금이 새겨져 있는 분홍색의 원형 정제 | 삼일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502529/EE) | 유효 |
| 199203393 | 마도파에취비에스캡슐125 | 흰색 또는 미황색 가루로 충진된 상부-암녹색, 하부-담청색의 경질 캡슐제 | (주)한국로슈 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199203393/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: Epinephrine, Ephedrine, Bupropion, Metronidazole, Pyridoxine, Metoclopramide, Iron, 항콜린제 계열(Atropine, Hyoscyamine, Methscopolamine, Glycopyrronium, Clidinium, Dicyclomine, Mepenzolate)
  - 경미: 제산제(Aluminum hydroxide, Calcium carbonate, Magaldrate, Magnesium carbonate/hydroxide/oxide)
- **지식 그래프상 금기 질환(허가사항 문구가 아닌 모델 지식 그래프 기반)**: 협우각 녹내장·개방각 녹내장, 정신병적 장애(조현정동장애 등), 흑색종, 심근경색, 심장 전도 질환, 갑작스러운 심정지, 기립성 저혈압, 간질환, 신장질환, 당뇨병·당뇨병성 케톤산증, 소화성 궤양(위궤양), 간질, 불안장애, 약물 유발 이상운동증 등

허가사항의 경고 및 금기 원문은 이번 데이터에 포함되어 있지 않으므로, 반드시 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험과 문헌이 전혀 없고 기전적 연관성도 불분명하여 근거 수준이 L5에 머뭅니다. 허가사항의 경고·금기 정보가 확보되지 않아 안전성 1차 검토도 진행할 수 없습니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(경고, 금기, 적응증 원문) 확보 및 분석
- DrugBank에서 작용 기전(MOA) 데이터 확보
- 라스무센 뇌염과 도파민계 경로의 연관성을 다룬 전임상·문헌 근거 탐색
- 관련 임상시험 등록 여부 재확인 및 투여 경로 적합성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Inbrija (levodopa) prescribing information, Merz Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=077c0f39-a3a2-4b2b-a184-09131889dcfb) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

