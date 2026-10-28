---
layout: default
title: Streptokinase
parent: 모델 예측만 (L5)
nav_order: 703
evidence_level: L5
indication_count: 5
monitor_inn: "Streptokinase"
predicted_indications: ["Prinzmetal angina", "hemoglobinopathy", "peripheral vascular disease", "peripheral arterial disease", "partial deletion of the short arm of chromosome 16"]
last_modified_at: 2026-10-28
description: "Streptokinase: 예측 신규 적응증 프린츠메탈 협심증 (근거 수준 L5). 기존 적응증: 허가 적응증 문구가 링크로만 제공되어 확인할 수 없음 (문헌상 혈전용해제로 기술됨)"
---

# Streptokinase
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

## Streptokinase: 혈전용해제에서 프린츠메탈 협심증으로
{: .text-alpha }

## 한 문장 요약

Streptokinase는 플라스미노겐을 활성화해 혈전을 녹이는 혈전용해 약물로, 국내에는 수출용 주사제로 허가되어 있습니다. TxGNN 모델은 **프린츠메탈 협심증(Prinzmetal angina)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 근거는 **증례 보고 1건과 종설 1편**뿐이고 등록된 임상시험은 없습니다. 이 질환의 핵심 병리는 관상동맥 경련이어서 기전상 연결고리도 약합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 문구가 링크로만 제공되어 확인할 수 없음 (문헌상 혈전용해제로 기술됨) |
| 예측 신규 적응증 | 프린츠메탈 협심증 |
| TxGNN 예측 점수 | 0.9980 |
| 근거 수준 | L5 (직접 관련 연구는 증례 보고 1건과 종설 1편) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 7건 (모두 단일 성분, 수출용 제품명) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 검토된 문헌에 따르면 streptokinase는 플라스미노겐을 플라스민으로 전환하고, 플라스민이 혈전의 피브린을 분해합니다. 그래서 심근경색, 말초동맥 폐색, 폐색전증 같은 혈전성 질환에 쓰여 왔습니다.

프린츠메탈 협심증과의 연결고리는 혈전입니다. 불안정 허혈 증후군에서 관상동맥 내 혈전이 관찰된 바 있고, 변이형 협심증 환자에게 심근경색이 생겨 streptokinase로 치료한 증례도 보고되었습니다. 다만 이 질환의 본질은 관상동맥 연축(vasospasm)이며, 표준 치료는 칼슘채널차단제와 질산염 같은 혈관확장제입니다. 혈전용해는 합병증인 심근경색에만 관련될 뿐 기저 질환에는 작용하지 않습니다. 높은 예측 점수는 이 약이 심근경색에 쓰여 온 이력을 반영한 것일 가능성이 큽니다.

## 문헌 근거

등록된 관련 임상시험은 없고, 문헌은 다음과 같습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15457281](https://pubmed.ncbi.nlm.nih.gov/15457281/) | 2004 | 증례 보고 | Kardiologia Polska | 변이형 협심증 환자(49세 남성)에게 발생한 심근경색을 streptokinase, 칼슘길항제, 질산염으로 치료해 성공했고 3년간 증상 없이 안정적임 |
| [6335445](https://pubmed.ncbi.nlm.nih.gov/6335445/) | 1984 | 종설 | Giornale Italiano di Cardiologia | 관상동맥 연축은 임상·혈관조영·생리학적 근거가 있을 때만 진단해야 하며, 변이형 협심증과 동의어가 아님 |
| [7315724](https://pubmed.ncbi.nlm.nih.gov/7315724/) | 1981 | 코호트/관찰 연구 | American Heart Journal | 불안정 협심증 등 불안정 허혈 증후군 환자의 혈관조영에서 관상동맥 내 혈전 소견이 관찰됨 (변이형 협심증을 직접 다룬 연구는 아님) |
| [2535772](https://pubmed.ncbi.nlm.nih.gov/2535772/) | 1989 | 진단 연구 | American Journal of Cardiology | 급성 심근경색의 항미오신 항체 영상 진단 연구이며, 일부 환자가 streptokinase 혈전용해 치료를 받음 (이 약의 효과를 평가한 연구는 아님) |

## 한국 시판 정보

허가 적응증 문구는 텍스트가 아닌 MFDS 문서 링크로만 제공되어, 아래 표에서는 링크 형태로 표시합니다. 제품명에 모두 "수출용"이 붙어 있어 국내 시판 여부는 별도 확인이 필요합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199904106 | 에스키나제주1,500,000IU(스트렙토키나제)(수출용) | 바이알 주사제 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199904106/EE) |
| 199800042 | 프로키나제주사750,000IU(스트렙토키나제)(수출용) | 바이알 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199800042/EE) |
| 199904108 | 에스키나제주250,000IU(스트렙토키나제)(수출용) | 바이알 주사제 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199904108/EE) |
| 201502392 | 유유스트렙토키나제주1,500,000IU(수출용) | 바이알 주사제 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201502392/EE) |
| 199904107 | 에스키나제주750,000IU(스트렙토키나제)(수출용) | 바이알 주사제 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199904107/EE) |

위 표는 전체 7건 중 5건이며, 나머지 2건은 한국코러스(주)의 에스나제주 150만단위와 75만단위입니다.

## 안전성 고려사항

**약물 상호작용**: 이 보고서용으로 수집한 데이터에서 총 100건의 상호작용이 확인되었으며, 그중 20건의 세부 정보가 있습니다.
- **주요(Major) 등급**: abciximab, acalabrutinib, apixaban, avapritinib, betrixaban, bivalirudin, deferasirox, ibritumomab tiuxetan, tositumomab(I-131). 대부분 항응고·항혈소판 계열이거나 출혈 위험을 높이는 약물입니다.
- **중등도(Moderate) 등급**: 아세틸살리실산(아스피린), ibuprofen, ketorolac, celecoxib, diclofenac(외용), aminocaproic acid, 오메가-3 지방산, 생강, fenfluramine, sibutramine.

경고 및 금기 정보는 수집되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 프린츠메탈 협심증의 핵심 병리인 관상동맥 연축에는 streptokinase가 작용하지 않고, 직접 근거도 증례 보고 1건 수준입니다.
- 혈전용해가 의미 있는 것은 심근경색 같은 혈전성 합병증에 한정되며, 이는 이 약의 기존 용도와 겹칩니다.
- 참고로 같은 약물의 다른 예측 질환인 말초동맥 폐색 관련 질환은 코크란 체계적 문헌고찰 등 더 많은 문헌이 있지만, 현재는 재조합 tPA와 우로키나제가 우선 사용됩니다.

**진행하려면 필요한 것:**
- MFDS 허가사항 원문(적응증, 경고, 금기)의 확보와 분석
- 상세 작용 기전(MOA) 데이터 확보
- 변이형 협심증에서 혈전용해제의 이득을 평가한 임상 근거(관찰 연구 이상)
- 수출용 허가 제품의 국내 실제 공급·시판 여부 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

