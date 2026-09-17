---
layout: default
title: Cefuroxime
parent: 모델 예측만 (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
---

# Cefuroxime
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Cefuroxime: 세균 감염증에서 세균성 관절염으로

## 한 문장 요약

Cefuroxime은 제2세대 세팔로스포린계 항생제로, 다양한 세균 감염증 치료에 광범위하게 사용되어 온 약물입니다.
TxGNN 모델은 **세균성 관절염(Bacterial Arthritis)**에 효과가 있을 수 있다고 예측하며, 현재 관련 임상시험 등록은 없으나 **20편의 문헌**(급성 화농성 관절염 치료 사례, 활막액 약동학 연구 포함)이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 허가 데이터 없음; 문헌상으로는 세균 감염증 전반에 사용되는 항생제) |
| 예측 신규 적응증 | 세균성 관절염 (Bacterial Arthritis) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L3 (코호트 연구·약동학 연구 수준) |
| 한국 시판 현황 | 미상영 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 Cefuroxime의 상세한 작용기전(MOA) 데이터는 확보되지 않았습니다. 다만 문헌 근거에 따르면 Cefuroxime은 세균 세포벽 합성을 억제하는 베타락탐계 항생제로서, 정맥주사 후 활막액(synovial fluid)에 치료 농도로 충분히 침투하는 것이 약동학 연구로 확인되었습니다.

화농성(세균성) 관절염을 유발하는 주요 병원균(Staphylococcus aureus, Streptococcus pyogenes 등)과 라임 관절염 관련 Borrelia 균종에 대해 Cefuroxime이 항균 활성을 가진다는 점도 문헌에서 뒷받침됩니다.

즉, 이 예측은 완전히 새로운 기전을 가정하는 것이 아니라 Cefuroxime의 기존 항균 스펙트럼과 조직 침투력을 관절 감염이라는 특정 병소로 확장 적용하는 것에 가깝습니다. 실제로 1980년대부터 급성 화농성 관절염 치료에 Cefuroxime을 사용한 임상 경험이 존재하여, TxGNN 예측의 타당성을 뒷받침합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6695158](https://pubmed.ncbi.nlm.nih.gov/6695158/) | 1984 | 코호트 | Scand J Infect Dis | 급성 화농성 관절염 환자 17명에서 Cefuroxime 사용, cloxacillin/ampicillin군과 비교 |
| [28784675](https://pubmed.ncbi.nlm.nih.gov/28784675/) | 2017 | 약동학 연구 | Antimicrob Agents Chemother | 슬관절경 환자 10명 대상, Cefuroxime 1,500mg 정맥투여 후 활막액 내 농도 평가 |
| [34756070](https://pubmed.ncbi.nlm.nih.gov/34756070/) | 2021 | 네트워크 메타분석 | Microbiology Spectrum | 라임 관절염 포함 라임병 치료제 40년간 경구/주사 항생제 효능·안전성 비교 |
| [23599360](https://pubmed.ncbi.nlm.nih.gov/23599360/) | 2013 | 코호트 | J Antimicrob Chemother | Penicillin 감수성 S. aureus 균혈증에서 penicillin·dicloxacillin·cefuroxime 치료 성적 비교 |
| [24924733](https://pubmed.ncbi.nlm.nih.gov/24924733/) | 2014 | 진료지침 | Z Rheumatol | 독일 류마티스학회의 라임 관절염 진단·치료 권고안 |
| [27976670](https://pubmed.ncbi.nlm.nih.gov/27976670/) | 2016 | 리뷰 | Nature Reviews Disease Primers | 라임 보렐리아증의 병태생리 및 단계별(피부→관절 등) 임상경과 총설 |
| [21393124](https://pubmed.ncbi.nlm.nih.gov/21393124/) | 2011 | 리뷰 | J Antimicrob Chemother | 성인 자연관절 화농성 관절염 10년 경험 분석, 경험적 항생제 요법 지침 마련 |
| [29290233](https://pubmed.ncbi.nlm.nih.gov/29290233/) | 2017 | 진료지침 | Arch Pediatr | 프랑스 소아감염학회의 소아 골관절 감염 항생제 치료 권고 |
| [12765486](https://pubmed.ncbi.nlm.nih.gov/12765486/) | 2003 | 리뷰 | Paediatric Drugs | 소아 라임병 진단·치료·예방에 관한 문헌 총설 |
| [17113969](https://pubmed.ncbi.nlm.nih.gov/17113969/) | 2006 | 리뷰 | Clin Dermatol | 유주성 홍반 및 라임 관절염의 진단·치료·예후 총설 |

---

## 한국 시판 정보

현재 한국 내 허가된 Cefuroxime 제품이 없습니다 (미상영, 허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
세균성 관절염에 대한 예측은 코호트 연구 및 약동학 연구(활막액 침투 확인) 수준의 근거(L3)로 뒷받침되며, Cefuroxime의 기존 항균 스펙트럼 범위 내 확장 적용이라는 점에서 기전적 개연성이 있습니다. 다만 TFDA 첨부문서상 경고·금기 정보가 확보되지 않아(Blocking 등급 데이터 갭) 안전성 초기평가(S1) 단계를 아직 완료할 수 없습니다.

**진행하려면 필요한 것:**
- TFDA 공식 첨부문서(경고/금기 사항) 확보 — 안전성 초기평가 진입을 위한 필수 선행 조건
- DrugBank 등을 통한 작용기전(MOA) 상세 데이터 보완
- 한국 내 허가·시판 현황 확인
- 세균성 관절염 적응증에 대한 전향적 임상시험 설계 검토 (현재 등록된 관련 임상시험 없음)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

