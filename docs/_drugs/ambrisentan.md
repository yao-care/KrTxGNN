---
layout: default
title: Ambrisentan
parent: 모델 예측만 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ambrisentan: 예측 신규 적응증 결합조직질환 연관 폐동맥 고혈압 (PAH associated with connective tissue disease) (근거 수준 L5). 기존 적응증: 폐동맥 고혈압 (허가증에 적응증 원문 대신 허가 문서 링크만 등록되어 있음)"
monitor_inn: "AMBRISENTAN"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Ambrisentan
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

## Ambrisentan: 폐동맥 고혈압에서 결합조직질환 연관 폐동맥 고혈압으로
{: .text-alpha }

## 한 문장 요약

Ambrisentan은 엔도텔린 A 수용체 길항제로, 한국에서 폐동맥 고혈압 치료제로 허가되어 시판되고 있습니다.
TxGNN 모델은 여러 신규 적응증을 예측했으며, 이 보고서는 근거가 가장 많은 **결합조직질환 연관 폐동맥 고혈압(PAH-CTD)**을 중심으로 평가합니다. 현재 **2건의 임상시험**과 **19편의 문헌**이 이 방향을 지지합니다.

> 참고: TxGNN 점수 1위 예측은 폐동맥 정맥기형(점수 99.41%)이지만 근거가 문헌 1건(증례 보고)뿐이고 기전적 연관성이 약해 보류(Hold) 대상입니다. 반면 6위인 결합조직질환 연관 PAH(점수 99.30%)는 가장 근거가 풍부하여 이를 대표 후보로 삼았습니다. 두 후보는 아래 "다른 예측 적응증 요약"에서 함께 정리합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 폐동맥 고혈압 (허가증에 적응증 원문 대신 허가 문서 링크만 등록되어 있음) |
| 예측 신규 적응증 | 결합조직질환 연관 폐동맥 고혈압 (PAH associated with connective tissue disease) |
| TxGNN 예측 점수 | 99.30% |
| 근거 수준 | L2 (완료된 Phase 2 시험 1건 및 Phase 4 시험 1건, 메타분석·체계적 문헌고찰 포함) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 이번 보고서용 자료에 포함되어 있지 않습니다. 다만 알려진 정보에 따르면 ambrisentan은 선택적 엔도텔린 A 수용체 길항제로, 폐혈관 수축과 평활근 증식을 억제합니다. 이는 폐동맥 고혈압(WHO 1군)의 핵심 경로입니다.

결합조직질환 연관 PAH는 WHO 1군 PAH의 하위 유형이며, 특히 전신 경화증의 혈관병증에는 엔도텔린이 강하게 관여합니다. 따라서 ambrisentan의 기전은 이 집단에도 그대로 적용될 수 있습니다. 문헌에서도 ambrisentan이 특발성·유전성 PAH와 결합조직질환 연관 PAH에 사용되는 약제로 소개됩니다.

중요한 점은 ambrisentan이 이미 1군 PAH에 허가되어 있어, 이 예측은 완전히 새로운 질환이라기보다 **허가 범위 내 하위 집단**에 가깝다는 것입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | 완료 | 38 | 전신 경화증 동반 경계성 PAH의 조기 치료, 무작위·이중맹검·위약대조 개념증명 시험 |
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | 완료 | 25 | 전신 경화증 연관 PAH에서 ambrisentan+tadalafil 병용 36주 공개 단일군 시험 (6분 보행거리, NYHA 분류, 혈역학 평가) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | 메타분석 | BMJ Open | 결합조직질환 연관 PAH 임상시험 메타분석 |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | 체계적 문헌고찰·메타분석 | Internal and Emergency Medicine | 결합조직질환 PAH 치료의 RCT 메타분석 (기능 등급, 생존, 6분 보행거리 등) |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | 하위군 분석 | Annals of the Rheumatic Diseases | AMBITION 시험의 CTD-PAH 하위군에서 ambrisentan+tadalafil 초기 병용요법 평가 |
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | 사후 분석 | Annals of the Rheumatic Diseases | AMBITION 시험 mITT 집단의 CTD-PAH에서 초기 병용요법과 단독요법 비교 |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | 하위군 분석 | Respiratory Medicine | ARIES-E 시험의 CTD-PAH 환자에서 ambrisentan 3년 효능·안전성 |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | 임상 연구 | Am J Respir Crit Care Med | 피부경화증 연관 PAH에서 ambrisentan+tadalafil 초기 병용요법 |
| [28425346](https://pubmed.ncbi.nlm.nih.gov/28425346/) | 2017 | Review | Therapeutic Advances in Respiratory Disease | Ambrisentan의 PAH 사용 고찰, 운동능력·혈역학 개선 및 허용 가능한 부작용 |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | PAH 진단과 치료 개관 |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals | 결합조직질환 연관 PAH 치료의 최근 진전 |
| [33087021](https://pubmed.ncbi.nlm.nih.gov/33087021/) | 2020 | 증례 보고 | Modern Rheumatology Case Reports | 혼합결합조직병 PAH 2례에서 폐혈관확장제에 대한 상반된 반응 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200902796 | 볼리브리스정5밀리그램(암브리센탄) | 연한 분홍색의 볼록한 정사각형 정제 | 허가 문서 참조 (nedrug.mfds.go.kr) |
| 200902797 | 볼리브리스정10밀리그램(암브리센탄) | 진한 분홍색의 볼록한 달걀형 정제 | 허가 문서 참조 (nedrug.mfds.go.kr) |

두 제품 모두 (주)글락소스미스클라인이 허가받았으며 유효 상태입니다.

## 안전성 고려사항

- **금기(지식그래프 기반, 허가사항 아님)**: 울혈성 심부전, 빈혈, 대적혈구성 빈혈, 폐정맥폐쇄성질환
- **약물 상호작용**: 총 100건이 조회되었으며 주요 항목은 다음과 같습니다.
  - 중등도: Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin, Eliglustat, Naltrexone
  - 경미: Clarithromycin, Miconazole, Omeprazole
  - 그 외 Calcitriol, Pantoprazole, Doxycycline, Morphine, Metformin, Simvastatin 등은 등급 미상
- **추가 주의(근거 분석 기반)**: 간기능 모니터링, 배아·태아 독성(임신 금기), 부종, 빈혈

허가사항의 경고·금기 원문은 확보하지 못했으므로 허가사항을 참조하세요.

## 다른 예측 적응증 요약

| 순위 | 예측 적응증 | 점수 | 근거 수준 | 권장 |
|-----|-----------|------|---------|------|
| 1 | 폐동맥 정맥기형 | 99.41% | L4 | Hold (문헌은 HHT 환자의 PAH 증례 1건뿐이며, 혈관확장이 단락을 악화시킬 가능성) |
| 2 | 선천성 심질환 연관 PAH | 99.37% | L3 | Proceed with Guardrails (ambrisentan 코호트 연구 PMID 21371683 포함, 단락 생리·혈역학 모니터링 필요) |
| 3 | 주혈흡충증 연관 PAH | 99.30% | L5 | Hold (근거 없음) |
| 4 | HIV 연관 PAH | 99.30% | L4 | Research Question (소규모 증례군 위주, 항레트로바이러스제 상호작용 주의) |
| 5 | 만성 용혈성 빈혈 연관 PAH | 99.30% | L5 | Hold (빈혈·부종 악화 우려) |
| 7–10 | 치아·치주 기형 증후군, 단순 두피 모발감소증, 다모증, Dandy-Walker 기형 증후군 | 99.12–99.19% | L5 | Hold (기전적 근거 없음, 지식그래프 산물로 판단) |

## 결론 및 다음 단계

**결정: Proceed with Guardrails** (결합조직질환 연관 PAH 기준)

**사유:**
완료된 Phase 2 및 Phase 4 시험, 메타분석, 체계적 문헌고찰, AMBITION·ARIES-E 하위군 분석이 이 집단에서의 사용을 뒷받침합니다. 다만 두 시험은 규모가 작고(n=38, n=25) Phase 3가 아니며, 이 적응증은 이미 허가된 1군 PAH의 하위 집단이므로 신규 적응증이라기보다 허가 범위 내 사용 근거 정리에 가깝습니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고·금기)의 확보 및 분석 (현재 확보되지 않아 안전성 선별 단계로 넘어갈 수 없음)
- 작용 기전 데이터 보완 (DrugBank 조회)
- 간기능, 배아·태아 독성, 부종, 빈혈에 대한 모니터링 계획
- 울혈성 심부전, 빈혈, 폐정맥폐쇄성질환 환자 제외 또는 주의 기준 설정
- 기존 허가 적응증 텍스트의 확인 (현재 허가 문서 링크만 확인됨)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

