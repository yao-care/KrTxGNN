---
layout: default
title: Hydroquinone
parent: 모델 예측만 (L5)
nav_order: 405
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-05
description: "Hydroquinone: 예측 신규 적응증 지루각화증 (Seborrheic Keratosis) (근거 수준 L5). 기존 적응증: 간반, 흑피증(기미), 주근깨, 노인성 검은반점, 기타 불필요한 부위의 과도한 멜라닌 색소 침착 피부의 점차적인 표백"
monitor_inn: "HYDROQUINONE"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
---

# Hydroquinone
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

## Hydroquinone: 기미·과색소침착에서 지루각화증으로
{: .text-alpha }

## 한 문장 요약

Hydroquinone은 간반, 기미, 주근깨, 노인성 검은반점 등 과도한 멜라닌 색소 침착 피부를 점차 표백하는 데 사용되는 외용 크림 성분입니다.
TxGNN 모델은 **지루각화증(Seborrheic Keratosis)**에 효과가 있을 수 있다고 예측하지만, 직접적인 임상시험은 없고 **간접 문헌 1편**만 있어 근거는 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 간반, 흑피증(기미), 주근깨, 노인성 검은반점, 기타 불필요한 부위의 과도한 멜라닌 색소 침착 피부의 점차적인 표백 |
| 예측 신규 적응증 | 지루각화증 (Seborrheic Keratosis) |
| TxGNN 예측 점수 | 0.9973 |
| 근거 수준 | L5 (직접 임상시험 없음, 간접 관찰 연구 1건 및 기전적 추정만 있음) |
| 한국 시판 현황 | 시판 중 (유효 허가 17건 / 전체 18건) |
| 허가증 수 | 18건 (유효 17건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Hydroquinone 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “히드로퀴논을 국소 적용하면 티로신이 3,4-디히드록시페닐알라닌(도파)으로 효소적으로 산화되는 것을 억제하고(Denton, C. et al., 1952)1 기타 멜라닌세포 대사 과정을 억제함으로써(Jimbow, K. et al., 1974)2 피부의 가역적인 탈색소가 일어난다. 햇빛이나 자외선에 노출되면 탈색된 부위에 재색소침착이 일어난다(Parrish, L.A. et al., 1978)3.” 영어 원문: "Topical application of hydroquinone produces a reversible depigmentation of the skin by inhibition of the enzymatic oxidation of tyrosine to 3,4-dihydroxyphenylalanine (dopa) (Denton, C. et al., 1952)1 and suppression of other melanocyte metabolic processes (Jimbow, K. et al., 1974)2. Exposure to sunlight or ultraviolet light will cause repigmentation of bleached areas (Parrish, L.A. et al., 1978)3." ([DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b), 버전 2026-07-10; 확인일 2026-11-19). 다만 일반적으로 hydroquinone은 티로시naze(tyrosinase)를 억제하여 멜라닌 합성을 줄이는 것으로 알려져 있으며, 이 때문에 색소 침착 질환에 사용됩니다.

지루각화증은 갈색~검은색을 띠는 경우가 많아 색소를 옅게 하는 효과는 기대할 수 있습니다. 그러나 지루각화증은 색소 질환만이 아니라 표피가 증식하는 양성 병변이므로, 탈색이 병변 자체를 치료하지는 못합니다. 따라서 기전상의 연관성은 제한적이며, 높은 TxGNN 점수는 계산상의 예측일 뿐 직접적인 임상 자료로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | 전향적 관찰 연구 | J Plast Reconstr Aesthet Surg | 아시아 환자의 안면 색소 질환에 대한 병합 치료 알고리즘 연구. 지루각화증에 대한 hydroquinone의 직접 효과를 보여주는 것은 아니며 간접 근거에 해당 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202200063 | 도미나라이트크림(히드로퀴논) | 유백색의 크림제 | 간반, 흑피증(기미), 주근깨, 노인성 검은반점, 기타 불필요한 부위의 과도한 멜라닌 색소 침착 피부의 점차적인 표백에 사용합니다. |
| 200204181 | 네오퀸크림4%(히드로퀴논) | 백색의 크림 | 간반, 흑피증(기미), 주근깨, 노인성 검은반점, 기타 불필요한 부위의 과도한 멜라닌 색소 침착 피부의 점차적인 표백에 사용합니다. |
| 199101003 | 도미나크림(히드로퀴논) | 흰 노란색의 크림제 | 간반, 흑피증(기미), 주근깨, 노인성 검은반점, 기타 불필요한 부위의 과도한 멜라닌 색소 침착 피부의 점차적인 표백에 사용합니다. |
| 201501564 | 엘더킨크림4%(히드로퀴논) | 유백색의 크림제 | 간반, 흑피증(기미), 주근깨, 노인성 검은반점, 기타 불필요한 부위의 과도한 멜라닌 색소 침착 피부의 점차적인 표백에 사용합니다. |
| 201907481 | 멜라토닝크림(히드로퀴논) | 유백색 불투명 크림제 | 간반, 흑피증(기미), 주근깨, 노인성 검은반점, 기타 불필요한 부위의 과도한 멜라닌 색소 침착 피부의 점차적인 표백에 사용합니다. |

## 안전성 고려사항

- **지식그래프상 금기 관련 질환**: 일광화상, 부신피질기능저하증(애디슨병), 피부위축, 모세혈관확장증, 유전성 출혈성 모세혈관확장증, 모세혈관 질환, 말초혈관질환, 간헐적 파행, 말초동맥질환, 아토피 습진, 피부염. 이는 라벨 문구가 아니라 지식그래프의 약물-질환 금기 연결이므로 참고용입니다.

그 외 상세한 경고, 금기, 약물 상호작용은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
지루각화증에 대한 직접적인 임상시험이나 문헌이 없고, 간접 관찰 연구 1건뿐입니다. 또한 지루각화증은 양성 표피 증식성 병변이라 탈색 작용만으로는 치료 기전을 설명하기 어렵습니다.

**진행하려면 필요한 것:**
- 지루각화증에 대한 hydroquinone의 직접 임상 또는 전임상 근거
- 상세한 작용 기전 데이터 (MOA)
- 허가사항(경고·금기) 확인 및 안전성 검토
- 투여 경로 적합성(외용 크림) 평가

*참고: 2~4순위 예측(외음부 역모낭각화증, 발진, 태선 질환)도 모두 근거가 간접적이거나 없어 Hold 판정입니다.*

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

