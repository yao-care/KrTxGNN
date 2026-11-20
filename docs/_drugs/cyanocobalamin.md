---
layout: default
title: Cyanocobalamin
parent: 모델 예측만 (L5)
nav_order: 238
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
description: "Cyanocobalamin: 예측 신규 적응증 비오틴 대사 질환 (Biotin Metabolic Disease) (근거 수준 L5). 기존 적응증: 임신·수유기, 발육기, 노년기의 비타민 D 보급, 뼈·이의 발육불량, 구루병의 예방 (마이칼큐정 허가 기준)"
monitor_inn: "CYANOCOBALAMIN"
predicted_indications: ["biotin metabolic disease"]
---

# Cyanocobalamin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Cyanocobalamin: 비타민 B12 보충에서 비오틴 대사 질환으로
{: .text-alpha }

## 한 문장 요약

Cyanocobalamin(시아노코발라민)은 비타민 B12 제제로, 한국에서 비타민 보급과 안구 증상 완화 등의 용도로 허가되어 있습니다.
TxGNN 모델은 **비오틴 대사 질환(Biotin Metabolic Disease)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**이며 **문헌 1편**(생물공학적 비타민 생산에 관한 리뷰)만 확인됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 임신·수유기, 발육기, 노년기의 비타민 D 보급, 뼈·이의 발육불량, 구루병의 예방 (마이칼큐정 허가 기준) |
| 예측 신규 적응증 | 비오틴 대사 질환 (Biotin Metabolic Disease) |
| TxGNN 예측 점수 | 0.9960 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Cyanocobalamin 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “임상약리학 비타민 B12는 성장, 세포 증식, 조혈, 그리고 핵단백질 및 미엘린 합성에 필수적이다.” 영어 원문: "CLINICAL PHAMRACOLOGY Vitamin B12 is essential to growth, cell reproduction, hematopoiesis, and nucleoprotein and myelin synthesis." ([DailyMed: cyanocobalamin prescribing information, SOLA Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e559c6c8-2973-77fb-e053-2995a90af43d), 버전 2025-12-08; 확인일 2026-11-19). 알려진 정보에 따르면 cyanocobalamin은 수용성 비타민 B12 제제로, 단일 성분 제제와 복합 영양 제제 형태로 널리 쓰이고 있습니다.

다만 B12 의존 효소(methylmalonyl-CoA mutase, methionine synthase)는 비오틴 의존 카르복실화 효소(propionyl-CoA carboxylase 등)와 프로피온산·원탄소 대사 경로에서 인접해 있습니다. 이 예측 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 관련 질환 간에 학습한 유사성을 반영했을 가능성이 있을 뿐 생물학적 근거는 아닙니다.

그러나 이 예측은 사실상 모델 점수에만 의존합니다. 비오틴 결핍증(biotinidase 결핍, holocarboxylase synthetase 결핍 등)의 표준 치료는 비오틴 보충이며, cyanocobalamin이 이러한 질환을 직접 치료한다는 기전적 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | 비타민 및 보조효소의 생물공학적 생산 공정 개관. 비오틴 대사 질환에 대한 치료 효과를 직접 다루지는 않음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202300936 | 마이칼큐정 | 필름코팅정제 | 임신·수유기, 발육기, 노년기의 비타민 D 보급, 뼈, 이의 발육불량, 구루병의 예방 |
| 200811904 | 틴클점안액 | 점안액 | 눈의 피로, 결막충혈, 수영 후 눈의 불쾌감 또는 먼지나 땀이 눈에 들어갔을 때, 자외선 및 기타광선에 의한 눈의 염증... |
| 199803691 | 아이루비로즈점안액 | 점안액 | 눈의 피로, 결막충혈, 수영 후 눈의 불쾌감 또는 먼지나 땀이 눈에 들어갔을 때, 자외선 및 기타광선에 의한 눈의 염증... |
| 201803073 | 헤모닉스주(시아노코발라민) | 주사제(앰플) | 허가 적응증 텍스트는 링크로만 제공됨 |
| 202503371 | 마이칼유정 | 필름코팅정제 | 허가 적응증 텍스트는 링크로만 제공됨 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었으며, 일부는 다음과 같습니다.
  - 경미(Minor): famotidine, ranitidine, cimetidine, nizatidine(H2 차단제), omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole, pantoprazole(양성자펌프억제제), potassium chloride
  - 등급 미상(Unknown): metformin, glimepiride, rosiglitazone, acarbose, mesalazine, doxycycline, morphine, sucralfate

  위산억제제 및 metformin 등은 비타민 B12 흡수에 영향을 줄 수 있으므로 병용 시 주의가 필요합니다. 그 밖의 경고·금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측은 TxGNN 점수(0.9960)에만 의존하며(근거 수준 L5), 지지하는 임상시험이 없고 문헌도 직접 관련성이 낮은 리뷰 1편뿐입니다. 비오틴 대사 질환의 표준 치료는 비오틴 보충이므로 cyanocobalamin의 치료적 타당성은 현재 확인되지 않습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 및 B12-비오틴 대사 경로 연계에 대한 기전 분석
- 비오틴 대사 질환(biotinidase 결핍, holocarboxylase synthetase 결핍 등)에 대한 직접적인 전임상·임상 근거
- 허가사항(경고·금기) 확인: 현재 허가 문서 내용이 확보되지 않아 안전성 검토가 불가능함
- 허가 적응증 원문 확인: 다수 허가증의 적응증이 링크로만 제공되어 내용 확인이 필요함
- 투여 경로 적합성 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: cyanocobalamin prescribing information, SOLA Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e559c6c8-2973-77fb-e053-2995a90af43d) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

