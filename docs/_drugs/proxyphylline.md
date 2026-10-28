---
layout: default
title: Proxyphylline
parent: 모델 예측만 (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Proxyphylline: 예측 신규 적응증 심장 질환 (heart disease) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증이 문서 링크로만 제공되어 구체적인 내용을 확인하지 못했습니다)"
monitor_inn: "Proxyphylline"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "pulmonary valve disease", "disorder of fucoglycosan synthesis", "Jeune syndrome situs inversus", "interventricular septum aneurysm"]
---

# Proxyphylline
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

## Proxyphylline: 기관지 확장 계열 약물에서 심장 질환으로
{: .text-alpha }

## 한 문장 요약

Proxyphylline은 테오필린 유사 크산틴 계열 약물로, 한국에서는 수출용 앰플 주사제로 허가되어 있습니다. TxGNN 모델은 **심장 질환(heart disease)**에 효과가 있을 수 있다고 예측하지만, 현재 뒷받침하는 근거는 **1978년 개 대상 전임상 연구 1편**뿐이며 임상시험은 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증이 문서 링크로만 제공되어 구체적인 내용을 확인하지 못했습니다) |
| 예측 신규 적응증 | 심장 질환 (heart disease) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 (전임상 연구만 존재) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold (추가 연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Proxyphylline은 테오필린 유사체인 크산틴 유도체로, 포스포디에스테라제(PDE) 억제와 아데노신 수용체 길항 작용을 통해 혈관 확장과 양성 변력·변시 효과를 낼 수 있습니다. 이 점이 심장 질환 예측과 연결될 수 있는 이론적 근거입니다.

다만 근거는 간접적입니다. 유일한 문헌은 Proxyphylline, 루틴, 스위트클로버 추출물이 들어 있는 복합제(Theo-Esberiven)를 개의 적출 심장에 투여한 연구로, 관상동맥 혈류가 증가했다고 보고합니다. 복합제 효과가 Proxyphylline 단독보다 약 1.7배 컸으므로 Proxyphylline 자체의 효과로 보기 어렵습니다. 또한 "심장 질환"은 매우 넓은 범주이고, 크산틴 계열은 심장 질환 환자에서 부정맥 위험이 있어 신중한 접근이 필요합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [640535](https://pubmed.ncbi.nlm.nih.gov/640535/) | 1978 | 전임상 (동물 연구) | Nihon Yakurigaku Zasshi | 개 적출 심장에서 Proxyphylline 및 복합제가 관상동맥 혈류를 증가시켰으며 심박수와 심근 수축력도 증가했습니다. 복합제의 관상동맥 혈류 증가 효과는 Proxyphylline 단독의 약 1.7배였습니다. |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200103166 | 메리난주(수출용) | 갈색 앰플제 (무색~미황색 액체) | 허가 적응증 상세 내용은 허가사항 문서를 참조하세요. |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

다만 이 보고서를 위해 수집한 데이터에서는 약물 상호작용 정보가 확인되지 않았습니다. 크산틴 계열 약물은 심장 질환 환자에서 부정맥 위험이 있다는 점을 고려해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만, 뒷받침하는 근거는 복합제를 사용한 오래된 동물 실험 1편뿐이며 사람 대상 임상 근거가 없습니다. 허가 적응증과 안전성 정보도 확인되지 않아 현 단계에서는 연구 질문 수준으로 보는 것이 적절합니다.

**진행하려면 필요한 것:**
- 허가사항 문서(첨부문서)를 내려받아 허가 적응증, 경고, 금기 확인
- 상세한 약물 작용 기전 데이터 (MOA)
- Proxyphylline 단독 투여에 대한 심혈관 효과 연구
- 구체적인 심장 질환 하위 유형 설정 및 부정맥 위험 평가

**참고: 그 외 예측 질환**
라우브리-페치 증후군, 피에르 로뱅 증후군(염색체 이상 동반형 및 유전성), 7번 염색체 장완 부분 결실, 구순구개열 증후군, 폐동맥 판막 질환, 푸코글리칸 합성 장애, 죠엥 증후군, 심실중격 동맥류 등 나머지 9개 예측 질환은 모두 임상시험과 직접 관련 문헌이 없고 기전적 연결고리도 확인되지 않아 근거 수준 L5, 권장 결정 Hold입니다. 푸코글리칸 합성 장애와 연결된 1977년 문헌 1편은 복합 혈관 활성 제제의 뇌혈류 연구로, 해당 질환과 관련이 없습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

