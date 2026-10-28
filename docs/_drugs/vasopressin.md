---
layout: default
title: Vasopressin
parent: 모델 예측만 (L5)
nav_order: 780
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Vasopressin: 예측 신규 적응증 선천성 프로트롬빈 결핍증 (Congenital Prothrombin Deficiency) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 문서 링크로만 제공되어 본문 확인 필요)"
monitor_inn: "VASOPRESSIN"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
---

# Vasopressin
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

## Vasopressin: 허가 적응증 정보 미확인에서 선천성 프로트롬빈 결핍증으로
{: .text-alpha }

## 한 문장 요약

Vasopressin은 한국에서 한림제약의 주사제로 허가·시판 중인 약물이지만, 이번 데이터에서는 허가 적응증 본문이 확인되지 않았습니다.
TxGNN 모델은 **선천성 프로트롬빈 결핍증(Congenital Prothrombin Deficiency)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이며 간접적인 **문헌 3편**(사례 보고 2건, 리뷰 1건)만 있습니다.
이 문헌들은 다른 응고인자 결핍증을 다루고 있어 직접적인 근거로 보기 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 문서 링크로만 제공되어 본문 확인 필요) |
| 예측 신규 적응증 | 선천성 프로트롬빈 결핍증 (Congenital Prothrombin Deficiency) |
| TxGNN 예측 점수 | 0.9963 |
| 근거 수준 | L5 (모델 예측 중심, 직접 근거 없음) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

> 참고: 데이터에는 근거 수준이 L4로 기재되어 있으나, 이 보고서의 판정 규칙(직접적인 기전 연구나 전임상 연구가 없고 간접 문헌만 존재)에 따라 L5로 판정했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 vasopressin과 유사체인 desmopressin(DDAVP)은 V2 수용체를 통해 혈장 factor VIII과 von Willebrand factor 수치를 높이는 것으로 알려져 있습니다. 이는 일부 출혈성 질환에서 타당한 기전입니다.

그러나 이 기전은 프로트롬빈(factor II)을 직접 증가시키지 않습니다. 따라서 매우 높은 TxGNN 점수(0.9963)는 계산상 예측일 뿐, 프로트롬빈 결핍증에 대한 직접적인 기전으로 뒷받침되지 않습니다. 검색된 문헌도 factor VIII/factor V 결핍증과 후천성 혈우병 A를 다루고 있어 간접적, 계열 수준의 관련성만 지지합니다. 또한 DDAVP 보고는 vasopressin이 아닌 desmopressin에 관한 것입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | 후천성 혈우병 A의 진단, 원인, 임상 양상 및 치료 옵션. factor VIII 자가항체로 인한 중증 출혈 질환 |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | 선천성 factor V·VIII 복합 결핍증 환자에서 DDAVP 투여 사례 |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | factor V·VIII 복합 결핍증 임신부의 factor VIII 농축제 보충 하 제왕절개 관리 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198401223 | 한림바소프레신주사액 (수출명: 페트레신주사액, 헤모프레신주사액) | 무색투명한 앰플제 (주사액) | 허가 적응증 본문은 확인되지 않음 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 확인되었으며, 이 중 주요(Major) 등급은 다음과 같습니다.
  - Dolasetron
  - Cisapride
  - Papaverine
  - Macimorelin
- 중등도(Moderate) 상호작용 예: Famotidine, Epinephrine, Loperamide, Chlorpropamide, Clarithromycin, Levofloxacin, Ondansetron, Heparin 등
- 경미(Minor) 상호작용 예: Metronidazole

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 임상시험이 없고, 문헌은 다른 응고인자 결핍증과 다른 약물(desmopressin)을 다루고 있습니다. vasopressin이 프로트롬빈을 직접 증가시키는 기전도 확인되지 않아 현재로서는 진행을 뒷받침하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기 포함) 확보: MFDS 허가 문서를 내려받아 분석
- 작용 기전(MOA) 데이터 보충 (DrugBank 조회)
- 프로트롬빈 결핍증과 vasopressin의 직접적인 기전 연결성 검토
- 프로트롬빈 결핍증을 직접 다룬 임상 또는 전임상 근거 탐색

---

## 참고: 두 번째 예측 적응증 (약인성 골다공증)

두 번째 예측인 **약인성 골다공증(Drug-induced Osteoporosis)**은 TxGNN 점수 0.9962이지만, 제공된 임상시험과 문헌이 모두 없어 근거 수준은 L5이며 권장 결정은 Hold입니다. Vasopressin 수용체가 골세포에서 보고되었고 저나트륨혈증과 골 손실의 연관성도 제기되었으나, 이는 이번에 평가되지 않은 가설 수준입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

