---
layout: default
title: Tramadol
parent: 모델 예측만 (L5)
nav_order: 751
evidence_level: L5
indication_count: 9
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
last_modified_at: 2026-10-23
description: "Tramadol: 예측 신규 적응증 Hunter-Thompson형 말단중간부 이형성증 (근거 수준 L5). 기존 적응증: 이 보고서용으로 정리된 데이터에는 허가 적응증 본문이 없고 허가 문서 링크만 있어 확인할 수 없습니다"
---

# Tramadol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Tramadol: 알려진 진통 용도에서 선천성 골이형성증(Hunter-Thompson형 말단중간부 이형성증)으로
{: .text-alpha }

## 한 문장 요약

Tramadol은 mu-오피오이드 수용체 작용과 세로토닌·노르에피네프린 재흡수 억제 작용을 가진 진통제로, 한국에서 단일 성분 제품으로 다수 허가되어 있습니다.
TxGNN 모델은 **Hunter-Thompson형 말단중간부 이형성증(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0편**입니다.
따라서 이 예측은 모델 점수만 있는 단계(L5)이며, 현재로서는 보류가 적절합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이 보고서용으로 정리된 데이터에는 허가 적응증 본문이 없고 허가 문서 링크만 있어 확인할 수 없습니다 |
| 예측 신규 적응증 | Hunter-Thompson형 말단중간부 이형성증 |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 최소 20건 (목록은 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 알려진 바에 따르면 tramadol은 mu-오피오이드 수용체 작용제이자 세로토닌·노르에피네프린 재흡수 억제제로, 통증 조절에 사용됩니다.

Hunter-Thompson형 말단중간부 이형성증은 CDMP1/GDF5 유전자 변이로 뼈 성장에 이상이 생기는 유전성 골격 질환입니다. Tramadol은 뼈 발달 경로에 작용하지 않으므로 질환 자체를 개선할 기전상 근거는 확인되지 않습니다. 증상으로서의 통증을 완화할 수는 있어도, 그 이상의 가능성을 뒷받침하는 자료는 없습니다.

높은 예측 점수(0.9999)는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아니며, 임상시험이나 문헌으로 확인된 것도 아닙니다.

같은 방식으로 예측된 다른 질환(brachyolmia-amelogenesis imperfecta 증후군, myosclerosis, brachyolmia, pseudoachondroplasia, 소아 특발성 관절염, LACC1 결핍 소아 관절염, 류마티스 결절증, 류마티스인자 양성 다관절 소아 특발성 관절염)도 모두 질환 개선 기전은 확인되지 않았고, 통증 완화라는 간접적 근거만 이론상 가능합니다.

## 한국 시판 정보

허가 목록은 일부일 수 있으며, 아래는 그중 주요 5건입니다. 허가 적응증 본문은 정리된 데이터에 포함되어 있지 않아 허가 문서 링크로만 확인됩니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200713092 | 트라칸정 | 필름코팅정 | 허가 문서 참조 |
| 202201142 | 울트라셋세미정 | 필름코팅정 | 허가 문서 참조 |
| 198300327 | 트리돌캡슐50mg | 경질캡슐 | 허가 문서 참조 |
| 198600090 | 타마돌주사 | 주사제(앰플) | 허가 문서 참조 |
| 201600211 | 트라놀주 | 주사제(앰플) | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 일부를 아래에 정리했습니다.
  - 주요(Major) 등급: Alvimopan, Bupropion, Cisapride, Dexfenfluramine, Diethylpropion, Dolasetron, Dronabinol, Ephedrine, Fenfluramine
  - 중등도(Moderate) 등급: Atropine, Bisacodyl, Castor oil, Cimetidine, Clarithromycin, Clidinium, Dicyclomine, Eliglustat, Eluxadoline, Famotidine, Glycerin
- **소아 사용 관련 주의**: 소아 특발성 관절염 등 소아 질환이 예측된 경우, 소아에서의 오피오이드 사용은 호흡억제와 CYP2D6 초고속 대사 문제 등 안전성 우려가 있으며 tramadol에는 소아 사용 제한이 있습니다.

주요 경고와 금기 등 그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 질환에 대한 임상시험과 문헌이 없고, 질환 개선 기전도 확인되지 않아 근거는 모델 점수뿐입니다. 소아 관련 예측 질환에서는 안전성 우려도 있습니다.

**진행하려면 필요한 것:**
- 허가사항(적응증, 경고, 금기) 원문 확보 및 분석
- 작용 기전 데이터 보강 (DrugBank 조회)
- 예측 질환에 대한 전임상 또는 임상 근거 탐색
- 증상 완화 목적의 사용을 검토할 경우, 대상 질환별 통증 관리 필요성과 소아 안전성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

