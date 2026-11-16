---
layout: default
title: Ambroxol Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 54
evidence_level: L5
indication_count: 4
drugbank_id: DB06742
monitor_inn: "Ambroxol"
predicted_indications: ["nasal cavity disease", "vulvovaginal candidiasis", "faucial diphtheria", "cervical disc degenerative disorder"]
last_modified_at: 2026-11-16
description: "Ambroxol Hydrochloride: 예측 신규 적응증 비강 질환 (nasal cavity disease) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Ambroxol Hydrochloride
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

## Ambroxol Hydrochloride: 비강 질환 (nasal cavity disease)
{: .text-alpha }

## 한 문장 요약

Ambroxol hydrochloride는 기도 점액 분비를 조절하는 점액용해·분비촉진제 계열 약물입니다.
TxGNN 모델은 **비강 질환 (nasal cavity disease)**에 효과가 있을 수 있다고 예측합니다.
다만 이 질환을 직접 다룬 임상시험은 **0건**이고, 연결된 문헌은 급성 기침을 다룬 **1편**(간접 근거)뿐이어서 근거는 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198900635/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199602639/EE); 이 약은 점액분비장애로 인한 급·만성기관지염, 천식성기관지염에 사용합니다.; [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198801976/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198901574/EE); https://nedrug.mf |
| 예측 신규 적응증 | 비강 질환 (nasal cavity disease) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 수집되지 않았습니다. 일반적으로 알려진 약리 특성은 다음과 같습니다.

- 기도 점액 청소를 촉진합니다.
- 폐 표면활성물질(surfactant) 생성을 자극합니다.
- 나트륨 채널(Nav)을 차단하는 약한 국소마취 작용이 있습니다.
- 항염 작용이 있습니다.

이런 특성은 상기도의 점액 과분비와 자극 증상을 완화할 수 있어, 비강 질환에 생물학적으로 적용 가능하다는 가설을 세울 수 있습니다.

그러나 연결된 문헌은 2015년 급성 기침 치료에 관한 리뷰 1편뿐입니다. 이는 상·하기도 증상에 대한 간접 근거일 뿐 비강 질환을 직접 다루지 않습니다. 0.9991이라는 높은 TxGNN 점수는 계산 모델의 예측값이지 임상 근거가 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Review | Vestnik otorinolaringologii | 인플루엔자·급성 호흡기 바이러스 감염에 동반된 급성 기침의 새로운 치료 가능성을 다룬 리뷰. 비강 질환을 직접 연구한 내용은 아님 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
비강 질환을 직접 연구한 임상시험이나 문헌이 없고, 근거는 모델 예측과 간접 문헌 1편뿐입니다(L5). 기전상 가능성은 있으나 현 시점에서 진행을 뒷받침하기에는 부족합니다.

**진행하려면 필요한 것:**
- 비강 질환(비염, 비부비동염 등)에서 ambroxol을 직접 평가한 임상시험 및 문헌 검색과 검증
- 작용 기전 데이터 보강
- 허가사항(경고·금기) 확인 후 안전성 검토
- 비강 적용에 적합한 투여 경로와 제형의 타당성 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “대만 허가 이력이 없어” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “대만 허가 이력·작용” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-05 | 삭제: “**[High]** 대만 허가 현황 재확인 — TFDA 데이터베이스에서 "AMBROXOL" 성분명으로 재검색 (조회 시 `AMBROXOL`과 `AMBROXOL HYDROCHLORIDE` 두 형태 모두 시도)” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

