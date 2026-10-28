---
layout: default
title: Givosiran
parent: 모델 예측만 (L5)
nav_order: 376
evidence_level: L5
indication_count: 9
monitor_inn: "Givosiran"
predicted_indications: ["primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "chronic hepatitis C virus infection", "glycogen storage disease due to hepatic glycogen synthase deficiency", "chronic hepatitis B virus infection", "disorder of phenylalanine metabolism"]
last_modified_at: 2026-10-23
description: "Givosiran: 예측 신규 적응증 원발성 문맥혈전증 (근거 수준 L5). 기존 적응증: 한국 허가 적응증 본문이 링크로만 제공되어 구체적 내용을 확인할 수 없음 (일반적으로 알려진 용도: 급성 간포르피린증)"
---

# Givosiran
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

## Givosiran: 급성 간포르피린증에서 원발성 문맥혈전증으로
{: .text-alpha }

## 한 문장 요약

Givosiran은 간세포의 ALAS1을 표적으로 하는 GalNAc 결합 siRNA로, 급성 간포르피린증 치료에 사용되는 약물입니다. TxGNN 모델은 **원발성 문맥혈전증(primitive portal vein thrombosis)**에 효과가 있을 수 있다고 예측하지만, 이 방향을 직접 지지하는 **임상시험과 문헌은 한 건도 없습니다**. 따라서 이 예측은 모델 점수에만 의존하는 가설 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 적응증 본문이 링크로만 제공되어 구체적 내용을 확인할 수 없음 (일반적으로 알려진 용도: 급성 간포르피린증) |
| 예측 신규 적응증 | 원발성 문맥혈전증 |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가 건수 | 1건 (단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 수집되지 않았습니다. 일반적으로 알려진 바에 따르면 Givosiran은 간세포의 ALAS1 발현을 억제하여 포르피린 전구체(ALA, PBG)를 줄이는 siRNA입니다.

문맥혈전증은 응고 및 혈관 병리와 관련된 질환으로, 헴 생합성 조절과의 기전적 연결고리가 확립되어 있지 않습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영했을 가능성이 있으며, 생물학적 근거는 아니고 이를 뒷받침하는 임상 또는 전임상 근거도 없습니다.

## 다른 상위 예측 질환

동일한 점수대 및 하위 순위에서 다음 질환들도 예측되었으나, 모두 임상시험과 문헌이 없고 기전적 근거도 부족합니다(모두 L5, Hold).

| 순위 | 질환 | TxGNN 점수 | 평가 |
|------|------|-----------|------|
| 2 | 특발성 구리 연관 간경변 | 1.0000 | 구리 대사와 ALAS1 억제 간 연관성 없음 |
| 3 | 간폐증후군 | 1.0000 | 폐내 혈관 확장 병리로 ALAS1과 무관 |
| 4 | 조기 발병 가족성 비경변성 문맥압항진증 | 1.0000 | 문맥 혈역학 질환으로 기전적 근거 없음 |
| 5 | 간문맥 경화증 | 1.0000 | 문맥 섬유화 병리를 다루지 못함 |
| 6 | 만성 C형 간염 바이러스 감염 | 0.9997 | 숙주 ALAS1 표적이며 항바이러스 활성 없음 |
| 7 | 간 글리코겐 합성효소 결핍 글리코겐 저장병 | 0.9996 | GYS2 결손과 직접적 대사 연결 없음 |
| 8 | 만성 B형 간염 바이러스 감염 | 0.9994 | HBV 전사체를 표적하지 않음 |
| 9 | 페닐알라닌 대사 장애 | 0.9990 | PAH 결핍과 헴 합성 조절 간 연관 없음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202600588 | 기브라리주(기보시란나트륨) | 주사제 (무색~노란색 투명 용액, 유리 바이알) | 허가 적응증 본문은 링크로만 제공됨 ([허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600588/EE)) |

제조사는 (주)메디팁이며, 단일 성분 제제입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 87건이 확인되었으며, 그중 주요(Major) 등급은 **Eliglustat**입니다. 나머지 대부분은 중등도(Moderate) 등급입니다. 대표 항목은 다음과 같습니다.
  - 항진균제: Amphotericin B (일반, 지질 복합체, 콜레스테릴 황산염, 리포좀 제형)
  - 아미노글리코사이드·글리코펩타이드계 항생제: Vancomycin, Kanamycin, Neomycin, Streptomycin
  - 염증성 장질환 치료제: Mesalazine, Balsalazide, Olsalazine, Sulfasalazine
  - 기타: Alosetron, Naltrexone, Metoclopramide, Exenatide, Fenfluramine, Dexfenfluramine, Caffeine

주요 경고와 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
원발성 문맥혈전증에 대한 임상시험과 문헌이 전혀 없고, 헴 생합성 억제와 혈전 병리 사이에 기전적 연결도 확인되지 않습니다. TxGNN 점수가 매우 높지만 이는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영한 것일 뿐 생물학적 근거가 아니므로 근거 수준은 L5입니다.

**진행하려면 필요한 것:**
- 허가 적응증 본문 및 경고·금기 정보 확보 (한국 허가 문서 분석)
- 상세 작용 기전(MOA) 데이터 확보
- ALAS1 억제와 문맥혈전증 간 연관성을 보여주는 전임상 또는 기전 연구
- 한국 시판 상태(취소 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

