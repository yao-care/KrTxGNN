---
layout: default
title: Flubendazole
parent: 모델 예측만 (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Flubendazole: 예측 신규 적응증 방광 암종 (urinary bladder carcinoma) (근거 수준 L5). 기존 적응증: 회충, 요충, 편충, 십이지장충의 감염 및 이들 혼합감염의 치료"
monitor_inn: "Flubendazole"
predicted_indications: ["urinary bladder carcinoma", "urinary bladder neoplasm", "infiltrating bladder urothelial carcinoma", "non-invasive bladder urothelial carcinoma", "bladder urachal urothelial carcinoma", "bladder squamous papilloma", "bladder signet ring cell adenocarcinoma", "bladder mixed adenocarcinoma", "bladder colonic type adenocarcinoma", "bladder colloid adenocarcinoma"]
---

# Flubendazole
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

## Flubendazole: 장내 기생충 감염에서 방광 암종으로
{: .text-alpha }

## 한 문장 요약

Flubendazole은 회충, 요충, 편충, 십이지장충 감염 치료에 사용되는 구충제입니다.
TxGNN 모델은 **방광 암종(urinary bladder carcinoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 임상시험과 문헌은 없습니다. 가장 가까운 근거는 **방광 신생물(urinary bladder neoplasm)** 예측에 연결된 **전임상 문헌 2편**이며, 모두 flubendazole이 아닌 유사 약물인 fenbendazole을 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 회충, 요충, 편충, 십이지장충의 감염 및 이들 혼합감염의 치료 |
| 예측 신규 적응증 | 방광 암종 (urinary bladder carcinoma) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 5건 |
| 권장 결정 | Hold |

> 참고: 예측 순위 2위인 방광 신생물(점수 0.9999)은 간접적인 전임상 문헌이 있어 L4로 평가되며, 별도로 "연구 과제(Research Question)"로 분류됩니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 flubendazole은 벤즈이미다졸계 구충제입니다. 이 계열은 전임상 연구에서 튜불린에 결합해 미세소관 중합을 방해하는 것으로 알려져 있으며, 이는 빠르게 증식하는 종양세포에도 영향을 줄 수 있습니다.

다만 이는 계열 수준의 추론이며, 방광암에 대한 flubendazole 고유의 근거는 아닙니다. 구충 적응증과 방광암 사이에 직접적인 임상적 연관성은 확인되지 않았습니다. 상위 예측이 방광암의 여러 아형(침윤성, 비침윤성, 요막관, 인환세포 선암 등)에 집중된 점은 실제 생물학적 특이성보다는, TxGNN 모델(딥러닝)이 관련 질환들 사이에서 학습한 유사성을 반영한 결과일 가능성이 높으며, 생물학적 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

예측 1위(방광 암종)에 대한 문헌은 없습니다. 아래는 2위 예측(방광 신생물)에 연결된 문헌이며, 모두 fenbendazole 연구로 flubendazole 자체의 결과가 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41861111](https://pubmed.ncbi.nlm.nih.gov/41861111/) | 2026 | 전임상 | Advanced Science | Fenbendazole 기반 방광 내 주입 나노플랫폼(FBZ@BSA@PDA)이 페롭토시스 유도, 면역원성 세포사멸, 광열치료를 결합해 방광암에 대한 상승 효과를 보고 (제목·초록 기준) |
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | 전임상 | J Exp Clin Cancer Res | 방광 내 주입용 CRISPR-Cas13a와 fenbendazole 병용요법 연구 (제목·초록 기준) |

두 연구 모두 병용 설계라서 단독 약물 효과를 분리해 볼 수 없고, 사람 대상 임상 자료도 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199400891 | 알콤정 | 정제 | 회충, 요충, 편충, 십이지장충의 감염 및 이들 혼합감염의 치료 |
| 199300228 | 젤콤현탁액 | 현탁액(시럽제) | 회충, 요충, 편충, 십이지장충의 감염 및 이들 혼합감염의 치료 |
| 199400833 | 훌벤현탁액 | 현탁액(시럽제) | 회충, 요충, 편충, 십이지장충의 감염 및 이들 혼합감염의 치료 |
| 198800154 | 젤콤정 | 정제 | 회충, 요충, 편충, 십이지장충의 감염 및 이들 혼합감염의 치료 |
| 200403781 | 플루졸정 (수출용) | 정제 | 수출용 제품 (허가 적응증 본문 없음) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
방광암 예측은 TxGNN 점수만 높고(0.9999) 임상시험과 직접 문헌이 없어 L5 수준입니다. 방광 신생물에서 확인된 문헌 2편도 fenbendazole의 전임상 병용 연구라서 flubendazole의 근거로 쓸 수 없습니다.

**진행하려면 필요한 것:**
- Flubendazole 단독의 방광암 세포주 및 동물모델 전임상 데이터
- DrugBank 등에서 상세 작용 기전(MOA) 확보
- 허가사항(MFDS 첨부문서)의 경고·금기 정보 확보 및 안전성 검토
- 방광 내 주입 등 투여 경로 적합성 평가. 현재 시판 제형은 경구 정제와 현탁액뿐입니다.
- 방광암 아형별 평가에 앞서, 상위 일반 범주(방광 암종/신생물)에 대한 근거 보강
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

