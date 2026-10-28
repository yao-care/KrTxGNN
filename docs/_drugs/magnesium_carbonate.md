---
layout: default
title: Magnesium Carbonate
parent: 모델 예측만 (L5)
nav_order: 490
evidence_level: L5
indication_count: 4
monitor_inn: "MAGNESIUM CARBONATE"
predicted_indications: ["gastroduodenitis", "gastroparesis (disease)", "stomach disease", "duodenal obstruction"]
last_modified_at: 2026-10-28
description: "Magnesium Carbonate: 예측 신규 적응증 위십이지장염 (gastroduodenitis) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501043/EE"
---

# Magnesium Carbonate
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

## Magnesium Carbonate: 제산제 → 위십이지장염 (gastroduodenitis)
{: .text-alpha }

## 한 문장 요약

Magnesium Carbonate(탄산마그네슘)는 산을 중화하는 제산제 계열 성분입니다. TxGNN 모델은 **위십이지장염(gastroduodenitis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 없고 시험관 내 모델 문헌 1편만 있어 근거는 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501043/EE; 이 약은 위산과다, 속쓰림, 위부불쾌감, 위부팽만감, 체함, 구역, 구토, 위통, 신트림, 소화불량, 식욕감퇴(식욕부진), 과식, 소화촉진, 소화불량으로 인한 위부팽만감에 사용합니다.; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202204430/EE |
| 예측 신규 적응증 | 위십이지장염 (gastroduodenitis) |
| TxGNN 예측 점수 | 0.9994 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 (모두 유효, 단일 성분 제제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 탄산마그네슘은 위산을 중화하는 제산제로 알려져 있으며, 이 완충 작용이 위·십이지장 점막 염증에 동반되는 증상을 완화할 가능성은 있습니다.

다만 이는 증상 완화에 대한 추정일 뿐, 염증 자체를 치료한다는 근거는 아닙니다. 검토된 문헌도 인공 위-십이지장 모델에서 제산제의 효능을 평가한 시험관 내 연구 1편이어서 임상적 근거를 제공하지 못합니다. 이 질환을 직접 다룬 연구가 없으므로 근거 수준은 L5로 판정합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8763049](https://pubmed.ncbi.nlm.nih.gov/8763049/) | 1996 | 시험관 내 모델 | Therapie | 위, 근위 십이지장, 원위 십이지장을 모사한 컴퓨터 제어 인공 위-십이지장 모델로 제산제 효능을 평가한 연구. 임상 결과는 없음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202501043 | 일양쓰리쏙정 | 흰색의 원형 정제 | 허가 적응증 본문이 기록되어 있지 않음 |
| 200402122 | 디젠정 | 황색의 장방형 필름코팅정 | 위산과다, 속쓰림, 위부불쾌감, 위부팽만감, 체함, 구역, 구토, 위통, 신트림, 소화불량... |
| 202204430 | 맥스타제유디정 | 연두색의 타원형 필름코팅정 | 허가 적응증 본문이 기록되어 있지 않음 |

## 안전성 고려사항

- **약물 상호작용** (총 100건 조회, 주요 항목):
  - 중대(Major): Dolutegravir
  - 중등도(Moderate): Acalabrutinib, Doxycycline, Alendronic acid, Cholecalciferol, Acetylsalicylic acid, Atazanavir, Risedronic acid, Atropine, Azithromycin 등
  - 경미(Minor): Famotidine, Ranitidine, Alprazolam, Atenolol 등

허가사항의 경고 및 금기 정보는 이번 자료에 없으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
위십이지장염에 대한 임상시험이 없고 문헌도 시험관 내 모델 1편뿐이어서 근거 수준이 L5입니다. TxGNN 점수는 높지만(0.9994) 이를 뒷받침하는 임상 근거가 없습니다.

**진행하려면 필요한 것:**
- 위십이지장염 환자를 대상으로 한 임상 연구 또는 관찰 연구
- 작용 기전(MOA) 데이터 확보
- 허가사항(첨부문서)의 경고·금기 정보 확인
- Dolutegravir 등 주요 약물 상호작용에 대한 복용 간격 등 관리 방안 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

