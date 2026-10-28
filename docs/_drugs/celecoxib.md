---
layout: default
title: Celecoxib
parent: 모델 예측만 (L5)
nav_order: 199
evidence_level: L5
indication_count: 7
monitor_inn: "Celecoxib"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
last_modified_at: 2026-10-23
description: "Celecoxib: 예측 신규 적응증 말단중간이형성증 Hunter-Thompson형 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 텍스트가 링크로만 제공되어 내용을 확인할 수 없음)"
---

# Celecoxib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## Celecoxib: 라이선스 적응증에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Celecoxib은 선택적 COX-2 억제제로, 한국에서 단일 성분 제제로 다수 허가되어 있습니다. 다만 허가 적응증 본문은 이번 데이터에 포함되어 있지 않습니다.
TxGNN 모델은 **말단중간이형성증 Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험과 문헌은 0건**입니다.
따라서 이 예측은 모델 점수만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 텍스트가 링크로만 제공되어 내용을 확인할 수 없음) |
| 예측 신규 적응증 | 말단중간이형성증 Hunter-Thompson형 |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 최소 20건 (목록이 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 celecoxib은 COX-2를 선택적으로 억제해 프로스타글란딘 생성을 줄이는 소염진통제로 알려져 있으나, 이번 데이터에서는 확인되지 않았습니다.

이 질환은 CDMP1/GDF5 기능 소실 변이로 생기는 희귀 골격 이형성증이며, 연골 형성 과정의 BMP 신호에 영향을 줍니다. COX-2/프로스타글란딘 억제에서 이러한 유전적 성장인자 결함의 교정으로 이어지는 기전적 경로는 제공된 데이터로 뒷받침되지 않습니다.

높은 점수는 생물학적 근거라기보다 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성(예: 골격·근골격계 표현형 중복)을 반영했을 가능성이 큽니다. 같은 이유로 다른 상위 예측(brachyolmia 관련 질환, myosclerosis, 꼬리뼈 과가동성, 류마티스 결절증, WHIM 증후군)도 모두 L5이며 Hold입니다.

## 한국 시판 정보

목록은 일부일 수 있으며, 아래는 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201902742 | 셀렉시브캡슐100mg | 캡슐 | 적응증 텍스트 미확인 |
| 201405736 | 유콕스캡슐200밀리그램 | 경질캡슐 | 적응증 텍스트 미확인 |
| 201500145 | 유니브렉스캡슐200밀리그램 | 캡슐 | 적응증 텍스트 미확인 |
| 201601081 | 베아콕시브캡슐100밀리그램 | 경질캡슐 | 적응증 텍스트 미확인 |
| 202002057 | 랙시브정100밀리그램 | 필름코팅정 | 적응증 텍스트 미확인 |

## 안전성 고려사항

허가사항의 경고·금기 정보는 이번 데이터에 포함되어 있지 않습니다. 안전성 정보는 허가사항을 참조하세요.

**약물 상호작용** (총 100건 조회, 아래는 일부):
- **Major**: Eliglustat
- **Moderate**: Hydrocortisone, Metformin, Cimetidine, Levofloxacin, Metronidazole, Naltrexone, Mesalazine, Balsalazide, Olsalazine 등
- 설포닐우레아(Glimepiride, Glipizide, Glyburide, Chlorpropamide, Acetohexamide)와 Nateglinide, Exenatide 등 혈당강하제도 Moderate 수준으로 보고되었습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 예측 점수는 매우 높지만 이 질환을 직접 다룬 임상시험이나 문헌이 없고 기전적 연결고리도 확인되지 않아, 모델 예측만 존재하는 L5 단계입니다.
- 허가사항의 경고·금기 정보가 없어 안전성 검토도 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가사항 문서에서 적응증, 경고, 금기 확인
- 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- 이 질환(GDF5/BMP 경로 관련)에 대한 전임상·기전 연구 문헌 검토
- 다른 상위 예측 중 근거 가능성이 있는 후보(꼬리뼈 과가동성, 류마티스 결절증)는 별도 문헌 조사 후 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

