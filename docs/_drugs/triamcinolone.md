---
layout: default
title: Triamcinolone
parent: 모델 예측만 (L5)
nav_order: 761
evidence_level: L5
indication_count: 8
monitor_inn: "Triamcinolone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
last_modified_at: 2026-11-20
description: "Triamcinolone: 예측 신규 적응증 알로페시아 뮤시노사 (모낭 점액증) (근거 수준 L5). 기존 적응증: 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염(입안염) 및 설염(혀염)에 의한 염증의 완화"
---

# Triamcinolone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Triamcinolone: 구내염·설염 염증에서 알로페시아 뮤시노사(모낭 점액증)로
{: .text-alpha }

## 한 문장 요약

Triamcinolone은 합성 코르티코스테로이드로, 한국에서는 미란 또는 궤양을 수반하는 난치성 구내염 및 설염의 염증 완화 등에 사용되는 약입니다.
TxGNN 모델은 **알로페시아 뮤시노사(Alopecia Mucinosa, 모낭 점액증)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 없고 **증례 보고 2편**만 확인되어 근거는 매우 제한적입니다(근거 수준 L5).

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 미란(짓무름) 또는 궤양을 수반하는 난치성 구내염(입안염) 및 설염(혀염)에 의한 염증의 완화 |
| 예측 신규 적응증 | 알로페시아 뮤시노사 (모낭 점액증) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Triamcinolone 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “연구에 따르면 triamcinolone acetonide 60 mg ~ 100 mg을 단회 근육주사한 후 24 ~ 48시간 이내에 부신 억제가 나타나며, 이후 점차 정상으로 회복되어 보통 30 ~ 40일 후 정상화된다. 이 결과는 이 약으로 달성되는 치료 작용의 지속 기간이 긴 것과 밀접한 상관관계가 있다.” 영어 원문: "Studies indicate that following a single intramuscular dose of 60 mg to 100 mg of triamcinolone acetonide, adrenal suppression occurs within 24 to 48 hours and then gradually returns to normal, usually in 30 to 40 days. This finding correlates closely with the extended duration of therapeutic action achieved with the drug." ([DailyMed: Kenalog-40 (triamcinolone acetonide) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ce116aa-b330-4da9-9cdd-ba8e6be0c4ad), 버전 2026-01-05; 확인일 2026-11-19). 알려진 정보에 따르면 Triamcinolone은 항염 및 면역억제 작용이 강한 코르티코스테로이드이며, 한국에서 구내염·설염 등의 염증 완화에 허가된 단일 성분 제제가 다수 있습니다.

알로페시아 뮤시노사는 모낭 주위 염증 세포 침윤과 점액 침착이 특징입니다. 따라서 국소 도포 또는 병변 내 코르티코스테로이드는 국소 병변에 흔히 고려되는 접근으로, 생물학적으로 그럴듯합니다.

다만 수집된 문헌은 증례 수준에 그치며, 그중 Triamcinolone을 직접 검증한 연구는 없습니다. 예측은 어디까지나 계산 모델에 기반한 가설입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23968145](https://pubmed.ncbi.nlm.nih.gov/23968145/) | 2014 | 증례 보고 | Int J Dermatol | 특발성 모낭 점액증에서 bexarotene 겔로 치료에 성공한 증례(Triamcinolone 아님) |
| [14170262](https://pubmed.ncbi.nlm.nih.gov/14170262/) | 1964 | 증례 보고 | Hifuka kiyo. Acta dermatologica | 알로페시아 뮤시노사(Pinkus) 증례 보고(초록 없음) |

## 한국 시판 정보

허가 목록은 일부일 수 있습니다. 아래는 허가 적응증 문구가 확인되는 주요 허가입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200804589 | 아프타치정 | 이중정 | 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 201600837 | 마스클린페이스트 | 페이스트 | 만성 박리성 치은염, 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 201605133 | 마스원큐페이스트 | 페이스트 | 만성 박리성 치은염, 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |
| 200501062 | 이벤탁연고 | 연고 | 만성 박리성 치은염, 미란 또는 궤양을 수반하는 난치성 구내염 및 설염의 완화 |
| 198500023 | 오라메디연고 | 연고 | 만성 박리성 치은염, 미란 또는 궤양을 수반하는 난치성 구내염 및 설염에 의한 염증의 완화 |

## 안전성 고려사항

- **약물 상호작용**: 데이터에 100건의 상호작용이 보고되어 있으며, 확인된 목록에서 중대(Major) 등급은 **Adalimumab**입니다. 중등도(Moderate) 등급에는 Zidovudine, Isotretinoin, Acarbose, Acebutolol, Acetazolamide, Ketorolac, Nifedipine, Ibuprofen, Ethinylestradiol, Aldesleukin, Alemtuzumab, Aliskiren 등이 있습니다. 경미(Minor) 등급에는 Formoterol, Salbutamol이 있습니다.

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
알로페시아 뮤시노사를 직접 연구한 임상시험이 없고, 문헌도 오래된 증례와 다른 약물(bexarotene)의 증례뿐이므로 근거 수준은 L5입니다. 생물학적 타당성은 있으나 이 예측을 뒷받침하는 직접 근거가 없습니다.

**진행하려면 필요한 것:**
- Triamcinolone(병변 내·국소)을 모낭 점액증에 사용한 증례 또는 증례집 문헌 검색
- 허가사항(경고·금기) 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 투여 경로(국소/병변 내)와 국내 허가 제형의 적합성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Kenalog-40 (triamcinolone acetonide) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4ce116aa-b330-4da9-9cdd-ba8e6be0c4ad) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

