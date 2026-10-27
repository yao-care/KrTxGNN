---
layout: default
title: Rasburicase
parent: 모델 예측만 (L5)
nav_order: 645
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Rasburicase: 예측 신규 적응증 신장성 저요산혈증 (hypouricemia, renal) (근거 수준 L5). 기존 적응증: 허가 적응증 본문 미확인 (허가 문서 링크만 확인됨)"
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
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

## Rasburicase: 허가 적응증 정보 미확인에서 신장성 저요산혈증으로
{: .text-alpha }

## 한 문장 요약

Rasburicase는 요산을 알란토인으로 분해하는 재조합 요산 산화효소로, 한국에서 1건의 허가를 받아 시판 중입니다. 다만 이번 보고서에 사용된 데이터에는 허가 적응증 본문이 포함되어 있지 않습니다.
TxGNN 모델은 **신장성 저요산혈증(hypouricemia, renal)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험과 문헌은 0건**입니다. 게다가 기전상 요산이 이미 낮은 질환에서 요산을 더 낮추는 것이므로 오히려 부적절할 가능성이 큽니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 미확인 (허가 문서 링크만 확인됨) |
| 예측 신규 적응증 | 신장성 저요산혈증 (hypouricemia, renal) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 Rasburicase는 요산 산화효소 계열 약물로, 요산을 알란토인으로 전환하여 혈중 요산 농도를 낮추는 것으로 알려져 있습니다.

신장성 저요산혈증은 URAT1/GLUT9 기능 소실 등으로 혈중 요산이 비정상적으로 낮은 상태입니다. 여기에 요산을 더 줄이는 약물을 쓰는 것은 약리학적으로 역행하며 해로울 수 있습니다. 따라서 높은 TxGNN 점수는 요산 대사 경로와의 그래프상 연관성이 만든 인공적 결과일 가능성이 높고, 실제 치료적 연결로 보기 어렵습니다.

같은 방식으로 상위 10개 예측 중 다른 질환도 검토했습니다.
- **HPRT 부분 결핍증**: 급성 고요산혈증 위기에서 요산을 빠르게 낮춘다는 간접적 근거는 있습니다. 그러나 만성 관리는 allopurinol이나 febuxostat이 일반적이며, Rasburicase는 면역원성 때문에 반복 사용이 제한됩니다.
- **간성 포르피린증, 간폐증후군 등**: 뚜렷한 기전적 연결이 확인되지 않았습니다.
- **비경화성 문맥압항진증, 간문맥 경화증, 특발성 구리 연관 간경변, 원발성 문맥 혈전증**: 뚜렷한 기전적 연결이 확인되지 않았습니다. 앞의 세 질환은 점수가 동일해 그래프 구조에 따른 인공적 결과로 보입니다.
- **신세뇨관 산증, 페닐알라닌 대사 장애**: 뚜렷한 기전적 연결이 확인되지 않았습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200603896 | 패스터텍주1.5밀리그램(라스부리카제) | 동결건조분말 주사제 (무색 유리 바이알, 첨부용제로 용해) | 허가 문서 링크만 확인되어 적응증 본문 미확인 |

## 안전성 고려사항

- **약물 상호작용**: 총 13건이 확인되었습니다.
  - 주요(Major) 등급:
    - Prilocaine
    - Nitrous acid
  - 중등도(Moderate) 등급:
    - 국소·점안·비강용 마취제(Tetracaine, Lidocaine, Benzocaine, Cocaine, Proparacaine, Oxybuprocaine, Cinchocaine)
    - Idelalisib
- **예측 질환 관련 우려**: Rasburicase는 용혈과 메트헤모글로빈혈증을 일으킬 수 있습니다(특히 G6PD 결핍 시). 이는 포르피린증 관리를 복잡하게 하거나 간폐증후군의 산소 공급을 악화시킬 수 있습니다.

허가사항의 경고 및 금기는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
상위 예측 모두 임상시험과 문헌 근거가 없는 모델 예측(L5)뿐입니다. 1순위인 신장성 저요산혈증은 기전상 부적절하며, 나머지도 뚜렷한 기전적 연결이 없습니다. 안전성 정보(경고·금기)와 작용 기전 데이터도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증 본문) 확보: MFDS 첨부문서 PDF 다운로드 및 분석
- 작용 기전(MOA) 데이터 보완: DrugBank 조회
- 기전 타당성이 상대적으로 있는 HPRT 부분 결핍증 등 급성 고요산혈증 상황에 대한 문헌 및 임상시험 검색
- 메트헤모글로빈혈증·용혈 위험(G6PD 결핍 포함)에 대한 안전성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

