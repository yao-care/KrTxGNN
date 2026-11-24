---
layout: default
title: Lenograstim
parent: 모델 예측만 (L5)
nav_order: 467
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Lenograstim: 예측 신규 적응증 혈소판 분비 장애 (primary release disorder of platelets) (근거 수준 L5). 기존 적응증: 1-1. 고형암에 대해 항암화학요법을 받고 있는 환자의 호중구감소증 1-2. 혈액종양에 대해 항암화학요법을…"
monitor_inn: "LENOGRASTIM"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "severe nonproliferative diabetic retinopathy"]
---

# Lenograstim
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Lenograstim: 기존 적응증에서 혈소판 분비 장애로
{: .text-alpha }

## 한 문장 요약

Lenograstim은 재조합 인간 과립구 집락자극인자(G-CSF)로, 한국에서 3건의 허가를 받아 시판 중입니다.
TxGNN 모델은 **혈소판 분비 장애(primary release disorder of platelets)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 예측 점수는 높으나 모델 예측에만 의존하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1-1. 고형암에 대해 항암화학요법을 받고 있는 환자의 호중구감소증 1-2. 혈액종양에 대해 항암화학요법을 받고 있는 환자의 호중구감소증 2. 조혈모세포이식시의 호중구수 증가촉진 3. 골수이형성증후군에 따른 호중구감소증 4. 재생불량성빈혈에 따른 호중구감소증 5. 선천성ㆍ특발성… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199300329/EE)) |
| 예측 신규 적응증 | 혈소판 분비 장애 (primary release disorder of platelets) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Lenograstim의 작용 기전(비공식 번역): “과립구 집락 자극 인자 수용체 효능제”. 영어 원문: "Granulocyte colony stimulating factor receptor agonist" ([ChEMBL CHEMBL2109128 (lenograstim): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109128), CC BY-SA 3.0; 확인일 2026-11-19). 알려진 정보에 따르면 Lenograstim은 재조합 인간 G-CSF로, 호중구 전구세포의 증식과 분화를 촉진하여 과립구 계열에 작용합니다.

반면 혈소판 방출 장애는 혈소판 과립 내용물이나 방출 경로의 내재적 기능 결함입니다. G-CSF 수용체 신호전달과의 기전적 연관성은 확립되어 있지 않습니다. 따라서 높은 TxGNN 점수(0.9991)는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영한 것일 뿐, 생물학적 근거가 아니며 기전적·임상적 근거로 뒷받침되지 않습니다.

TxGNN이 함께 제시한 다른 예측들도 같은 한계를 보입니다.

| 순위 | 예측 질환 | TxGNN 점수 | 기전적 평가 |
|------|---------|-----------|-----------|
| 2 | Glanzmann 혈소판무력증 | 0.9989 | 혈소판 integrin αIIbβ3 결핍이 원인이며 G-CSF는 이 경로를 표적으로 하지 않음 |
| 3 | 가성 폰빌레브란트병 | 0.9988 | 혈소판 GPIbα 기능획득 변이가 원인이며 G-CSF의 역할이 알려져 있지 않음 |
| 4 | 중증 비증식성 당뇨망막병증 | 0.9961 | 골수 유래 전구세포 동원이라는 간접적·추측성 가능성만 있으며, 호중구 매개 염증과 병적 혈관신생을 촉진할 안전성 우려가 있음 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199300329 | 뉴트로진주50마이크로그램(레노그라스팀)(유전자재조합) | 이 약은 동결건조한 백색의 분말 또는 덩어리가 들어있는 무색투명한 바이알… | 제이더블유중외제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199300329/EE) | 유효 |
| 199300330 | 뉴트로진주100마이크로그램(레노그라스팀)(유전자재조합) | 이 약은 동결건조한 백색의 분말 또는 덩어리가 들어있는 무색투명한 바이알… | 제이더블유중외제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199300330/EE) | 유효 |
| 199300331 | 뉴트로진주250마이크로그램(레노그라스팀)(유전자재조합) | 이 약은 동결건조한 백색의 분말 또는 덩어리가 들어있는 무색투명한 바이알… | 제이더블유중외제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199300331/EE) | 유효 |

<!-- licenses:end -->

제조사는 모두 제이더블유중외제약(주)입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로 당뇨망막병증 예측과 관련하여, G-CSF가 망막의 호중구 매개 염증과 병적 혈관신생을 촉진할 가능성은 이론적 안전성 우려로 검토가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
네 가지 예측 모두 임상시험과 문헌 근거가 전혀 없는 L5 수준이며, 혈소판 기능 질환에 대해서는 G-CSF와의 기전적 연관성도 확인되지 않습니다. 현재 데이터만으로는 재창출 검토를 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 한국 허가 적응증 및 경고·금기 정보 확보 (허가사항 PDF 확인)
- 작용 기전(MOA) 데이터 보충
- 예측 질환과 G-CSF 사이의 기전적 연결 가능성을 보여주는 전임상 또는 문헌 근거
- 관련 임상시험 및 문헌 재검색
- 투여 경로 적합성 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [ChEMBL CHEMBL2109128 (lenograstim): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109128) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

