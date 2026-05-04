---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Budesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Budesonide: 천식 및 호흡기 염증에서 아토피 습진으로

---

## 한 문장 요약

Budesonide는 강효 흡입성 글루코코르티코이드 계열 약물로, 전 세계적으로 천식, 만성폐쇄성폐질환(COPD), 알레르기 비염 등 호흡기 염증 질환 치료에 사용되어 왔으나 한국 내 허가 이력은 없습니다.
TxGNN 모델은 **아토피 습진(Atopic Eczema)**에 효과가 있을 수 있다고 예측하며 (예측 점수 99.96%),
현재 **2건의 임상시험**과 **20편의 문헌**이 이 방향을 참조하고 있으나, 인간 대상 직접 임상시험 근거는 아직 없습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 천식, COPD, 알레르기 비염 (국제 적응증 기준; 한국 미허가) |
| 예측 신규 적응증 | 아토피 습진 (Atopic Eczema) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미허가 (시판 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

Budesonide는 강효 glucocorticoid receptor 작용제로, NF-κB 경로를 억제하여 Th2 사이토카인(IL-4, IL-5, IL-13)을 하향 조절하고 호산구 침윤 및 상피 장벽 염증을 감소시킵니다. 외용 피질스테로이드(Topical Corticosteroids, TCS)는 아토피 습진의 제1선 표준 치료법으로 이미 확립되어 있으며, Budesonide는 이와 동일한 분자 표적(glucocorticoid receptor)에 작용합니다.

아토피 습진의 핵심 병리인 Th2 면역 편향(IL-4/IL-13 축 과활성화)과 피부 장벽 기능 장애는 천식 등 다른 아토피 질환과 공통 기전을 공유합니다. 흡입성 코르티코스테로이드로 개발된 Budesonide가 외용 제형으로 전환되었을 때 이론적 적용 가능성이 있으며, 소아 아토피 피부염 국소 치료에서의 실제 사용 사례가 문헌에 보고되어 있습니다(PMID 8864369). 개를 대상으로 한 무작위 이중맹검 위약 대조 시험에서도 0.025% Budesonide 제품(Barazone)이 아토피 피부염 증상(피부 병변, 소양증)을 유의미하게 개선하였습니다(PMID 21062310).

2024년 발표된 pH 감응성 나노입자 수화젤 제형 연구(PMID 38275852)는 Budesonide의 아토피 피부염 국소 전달 최적화 가능성을 최초로 직접 탐구한 전임상 연구로, 기전적 타당성을 현대적인 약제학적 접근으로 구체화하였습니다. 다만 인간 대상 무작위 대조 임상시험 데이터는 현재까지 존재하지 않으며, 이 예측은 기전 기반 가설 단계(L3)로 분류됩니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | 완료 | 58 | 알레르기 면역요법이 아토피 천명 소아(18개월~3세)의 천식 이환율을 예방하는지 평가; 아토피 습진 포함 고위험군 대상이나 Budesonide를 직접 검증하지 않음 |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | 불명 | 150 | 중증 소아 천식 표현형(0~12세) 면역·대사체·미생물군 통합 분석 관찰 연구; 아토피 표현형 포함 집단이나 아토피 습진 치료 효능을 직접 평가하지 않음 |

> 2건 모두 관련성 등급 C — Budesonide를 아토피 습진에 직접 평가한 등록 임상시험은 현재 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | 제형/전임상 | Gels (Basel) | Budesonide 탑재 pH 감응성 Eudragit L100 나노입자 수화젤이 소아 아토피 피부염 병변 부위 국소 전달을 개선할 수 있음을 전임상 수준에서 최초 입증 |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | 임상 연구 | Dermatology (Basel) | 아토피 피부염 소아에서 국소 글루코코르티코스테로이드(Budesonide 포함) 치료 시 IGF축 및 골·콜라겐 회전율 변화; 전신 흡수 및 성장 억제 기전 규명 |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | 무작위 이중맹검 위약 대조 (수의학) | J Vet Pharmacol Ther | 개 아토피 피부염에서 0.025% Budesonide 제품(Barazone) 주 1회 3주 치료 시 피부 병변 및 소양증 유의미하게 감소, 삶의 질 향상 |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | RCT | Allergologia et immunopathologia | 아토피·비아토피 영유아 반복성 천명에서 Budesonide 반응성 비교; 아토피 유아에서 더 강한 반응 관찰 |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | 단면 연구 | Contact Dermatitis | 아시아 피부과 센터 아토피 피부염 환자의 접촉 감작 패턴; Budesonide 포함 코르티코스테로이드 시리즈 첩포 반응 분석 |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | 관찰 연구 | Dermatitis | 아토피 피부염 청소년·성인에서 유럽 표준 및 코르티코스테로이드 시리즈 접촉 과민성 빈도 분석; Budesonide 알레르기 발생률 포함 |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | 관찰 연구 | JAAD | 아토피 피부염 성인에서 개인위생 용품·국소 약물로 인한 알레르기 접촉 피부염 분석; 피부 장벽 파괴가 Budesonide 등 코르티코스테로이드 감작 위험 증가 |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | 관찰 연구 | Contact Dermatitis | 이탈리아 SIDAPA 기준 시리즈 Budesonide 첩포 시험(2018–2019); 코르티코스테로이드 과민성 마커로서의 Budesonide 역할 재평가, 최근 20년간 감소 추세 확인 |
| [16925687](https://pubmed.ncbi.nlm.nih.gov/16925687/) | 2006 | 임상 연구 | Pediatric Allergy Immunol | 천식·알레르기 비염·아토피 피부염 소아에서 호기 응축액 pH 측정; 아토피 행진 스펙트럼 내 Budesonide 사용 집단 포함, 아토피 질환 공통 생체지표 탐색 |
| [36713411](https://pubmed.ncbi.nlm.nih.gov/36713411/) | 2022 | 증례 보고 | Front Immunol | IPEX 증후군 환자에서 Dupilumab(항-IL-4Rα) 치료 후 아토피 습진을 포함한 제2형 면역 질환 호전; IL-4/IL-13 억제 기전이 아토피 습진에도 유효함을 간접 시사 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question**

**사유:**
Budesonide의 Th2 항염증 기전은 아토피 습진의 병리와 이론적으로 부합하며 전임상 제형 연구(PMID 38275852) 및 수의학 무작위 대조 시험(PMID 21062310)이 초기 타당성을 지지하지만, 인간 대상 직접 임상시험이 전무하고 현재 문헌의 대부분은 치료 효능이 아닌 접촉 과민성(접촉 알레르기) 연구로 구성되어 근거 수준이 L3에 머물러 있습니다.

**진행하려면 필요한 것:**
- Budesonide 외용 제형(나노입자 수화젤 등)의 인간 대상 Phase 1/2 임상시험 설계
- 상세한 작용 기전(MOA) 데이터 보완 (DrugBank API 조회 필요)
- 기존 외용 코르티코스테로이드(hydrocortisone, mometasone 등)와의 비교 효능 및 안전성 데이터 확보
- HPA 축 억제 및 피부 위축 관련 장기 안전성 모니터링 계획 수립
- 한국 내 허가 전략 검토 (현재 미허가 상태)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

