---
layout: default
title: Alteplase
parent: 모델 예측만 (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
monitor_inn: "ALTEPLASE"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
last_modified_at: 2026-11-20
description: "Alteplase: 예측 신규 적응증 헤파린 보조인자 2 결핍 (heparin cofactor 2 deficiency) (근거 수준 L5). 기존 적응증: 다음의 혈전용해 : 1. 급성심근경색증 2. 급성폐색전증 3. 급성허혈뇌졸중(증상 발현 후 4.5 시간…"
---

# Alteplase
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Alteplase: 조직 플라스미노겐 활성화제(혈전용해제) → 헤파린 보조인자 2 결핍 (heparin cofactor 2 deficiency)
{: .text-alpha }

## 한 문장 요약

Alteplase는 조직 플라스미노겐 활성화제 계열의 혈전용해제입니다.
TxGNN 모델은 **헤파린 보조인자 2 결핍(heparin cofactor 2 deficiency)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 현재 **0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음의 혈전용해 : 1. 급성심근경색증 2. 급성폐색전증 3. 급성허혈뇌졸중(증상 발현 후 4.5 시간 이내에 적절한 영상기법(예, 두개골 CT 또는 출혈을 민감하게 진 단할 수 있는 다른 진단 영상방법)으로 두개 내 출혈이 없음을 확인 후 가능한 신속하게 투여한다. 치료 효 과는… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199504213/EE)) |
| 예측 신규 적응증 | 헤파린 보조인자 2 결핍 (heparin cofactor 2 deficiency) |
| TxGNN 예측 점수 | 0.9972 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Alteplase 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “알테플라제는 피브린 존재 시 증강되는 플라스미노겐의 플라스민 전환 특성을 갖는 효소(세린 프로테아제)이다. 피브린이 없는 경우에는 플라스미노겐을 제한적으로만 전환시킨다. 알테플라제는 혈전 내 피브린에 결합하여 포획된 플라스미노겐을 플라스민으로 전환시키며, 이로써 국소 섬유소용해를 개시한다.” 영어 원문: "Alteplase is an enzyme (serine protease) that has the property of fibrin-enhanced conversion of plasminogen to plasmin. It produces limited conversion of plasminogen in the absence of fibrin. Alteplase binds to fibrin in a thrombus and converts the entrapped plasminogen to plasmin, thereby initiating local fibrinolysis." ([DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9), 버전 2026-01-20; 확인일 2026-11-19). 알려진 정보에 따르면 Alteplase는 혈전을 용해하는 약물로, 급성 혈전성 사건 치료에 쓰입니다.

헤파린 보조인자 2 결핍은 유전성 혈전 소인(thrombophilia)의 하나입니다. 환자에게 급성 혈전증이 생기면 이론상 Alteplase로 혈전을 녹일 수 있습니다.

다만 Alteplase는 혈전 자체를 치료할 뿐 근본적인 결핍을 교정하지 않습니다. 이 질환과 관련된 임상시험이나 문헌도 제공되지 않아, 현재는 모델 예측 수준입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199504213 | 액티라제주사50밀리그램(알테플라제) | 주사제 (바이알, 첨부용제 포함) | 허가 적응증 문구 확인 불가 |
| 199806573 | 액티라제주사20밀리그램(알테플라제) | 주사제 (바이알, 첨부용제 포함) | 허가 적응증 문구 확인 불가 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 등급(Major) 항목은 다음과 같습니다.
  - Deferasirox
  - Ibritumomab tiuxetan
  - Tositumomab 및 Tositumomab (I-131)
  - Abciximab
  - Acalabrutinib
  - Fondaparinux
  - Anisindione
  - Apixaban
- 중등도(Moderate) 항목으로는 Acetylsalicylic acid, Ibuprofen, Ketorolac, Fluvoxamine, Fosinopril, Aminocaproic acid, Aprotinin 등이 있습니다. 항응고제·항혈소판제·NSAID와의 병용 시 출혈 위험에 유의해야 합니다.

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 질환을 직접 다룬 임상시험과 문헌이 없고, 모델 예측만 존재합니다. Alteplase는 근본 결핍을 교정하지 못하므로 기전상 근거도 제한적입니다.

**진행하려면 필요한 것:**
- 헤파린 보조인자 2 결핍 환자에서 Alteplase를 사용한 임상 근거 확보
- 상세한 약물 작용 기전(MOA) 데이터
- 허가사항(경고·금기) 확인 및 출혈 위험 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

