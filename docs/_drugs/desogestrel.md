---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

# Desogestrel: 피임에서 여드름으로

## 한 문장 요약

Desogestrel은 제3세대 고나나계(gonane) 프로게스틴으로, 경구 피임약(단독 제제 또는 에티닐에스트라디올과의 복합제)으로 전 세계적으로 널리 사용됩니다. TxGNN 모델은 10가지 새로운 적응증을 예측하였으며, **여드름(Acne)**이 **1건의 완료된 Phase 4 임상시험**과 **20편의 문헌**으로 가장 강한 근거(L2)를 가진 최우선 재창출 후보로 확인되었고, **무월경(Amenorrhea)** 역시 **2건의 임상시험**과 **16편의 문헌**으로 뒷받침됩니다. TxGNN 상위 점수의 7건은 유방 양성 질환 관련 예측으로 지식 그래프(KG) 구조 편향에 의한 위양성으로 판단됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 피임 (경구 피임약: 단독 프로게스틴 또는 EE 복합제) |
| 예측 신규 적응증 (최우선) | 여드름 (Acne) |
| TxGNN 예측 점수 | 99.91% (전체 순위 #6; 상위 5위는 유방 양성 질환 위양성) |
| 근거 수준 | L2 |
| 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 예측 적응증 전체 요약

본 Evidence Pack은 10개 적응증을 동시에 분석한 다중 예측(multi) 보고서입니다. 전체 예측 결과는 아래와 같습니다.

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 권장 결정 |
|------|--------|-----------|---------|---------|
| 1 | Breast Fibrocystic Disease | 99.96% | L5 | Hold (KG 위양성) |
| **2** | **Amenorrhea · 무월경** | **99.96%** | **L3** | **Proceed with Guardrails** |
| 3 | Apocrine Adenosis of Breast | 99.92% | L5 | Hold (KG 위양성) |
| 4 | Blunt Duct Adenosis of Breast | 99.92% | L5 | Hold (KG 위양성) |
| 5 | Benign Mammary Dysplasia | 99.92% | L5 | Hold (KG 위양성) |
| **6** | **Acne · 여드름** | **99.91%** | **L2** | **Proceed with Guardrails** |
| 7 | Fat Necrosis of Breast | 99.89% | L5 | Hold (KG 위양성) |
| 8 | Breast Abscess | 99.89% | L5 | Hold (KG 위양성) |
| **9** | **Lactation Disease · 수유 관련 질환** | **99.87%** | **L3** | **Research Question** |
| 10 | Breast Adenosis | 99.85% | L5 | Hold (KG 위양성) |

> **위양성 판정 근거**: 순위 1·3·4·5·7·8·10의 유방 양성 질환 7건은 공통적으로 임상시험과 문헌이 전무하며, Desogestrel의 작용 기전과 생물학적 연관성이 없거나 극히 낮습니다. KG 내 유방 질환 노드 군집이 인위적으로 높은 점수를 유발한 구조적 편향으로 해석됩니다.

---

## 이 예측이 타당한 이유는?

현재 DrugBank를 통한 Desogestrel의 상세 작용 기전(MOA) 정보가 수집되지 않았습니다. 알려진 약리학적 연구에 따르면, Desogestrel은 간에서 생물학적 활성형인 **에토노게스트렐(etonogestrel)**로 전환되는 전구호르몬(prohormone)입니다. 고나나계 구조를 가져 제2세대 프로게스틴 대비 안드로겐성이 현저히 낮습니다.

에토노게스트렐은 **5α-환원효소 활성을 경쟁적으로 억제**하여 테스토스테론의 DHT 전환을 방해하고, 간에서 성호르몬결합글로불린(SHBG) 합성을 증가시켜 유리 테스토스테론 수준을 낮춥니다. 이를 통해 피지선 과활성이 억제되어 여드름이 개선됩니다. 복합제(desogestrel+에티닐에스트라디올) 형태에서는 에스트로겐이 SHBG를 추가로 상승시켜 항안드로겐 효과를 더욱 강화합니다.

피임이라는 기존 적응증과 여드름·무월경 사이의 연결고리는 동일한 기전 축(HPO 축 억제 + 항안드로겐 효과)에서 출발합니다. PMID 2956138(과안드로겐성 소월경 청소년 연구, 1987)과 PMID 2976224(고안드로겐 여성 약력학 연구, 1988)는 EE+desogestrel 복합제가 과안드로겐혈증에 의한 여드름과 무월경을 모두 개선할 수 있음을 직접 보고합니다.

---

## 임상시험 근거

### 여드름 (Acne)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01466673](https://clinicaltrials.gov/study/NCT01466673) | Phase 4 | 완료 | 201 | norgestimate 함유 삼상 OC와 desogestrel 함유 이상 OC를 경증~중등도 여드름 여성에서 직접 비교. 여드름을 주요 치료 종점으로 설정한 최고 품질의 직접 비교 시험 |

### 무월경 (Amenorrhea)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | 완료 | 121 | 젊은 여성 운동선수의 체지방 변화와 생식 기능(운동성 무월경 포함) 연구. 호르몬 피임 개입을 포함하나 desogestrel이 유일한 개입은 아니며 무월경이 주요 치료 종점이 아님 (간접 근거) |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | 불명 | 42 | PCOS 가임기 여성에서 경구 피임약 vs. 호르몬 질내링의 안드로겐·인슐린·지질 지표에 대한 59주간 비교. 무월경이 직접 치료 종점이 아님 (간접 근거) |

### 수유 관련 질환 (Lactation Disease)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT06689150](https://clinicaltrials.gov/study/NCT06689150) | N/A | 완료 | 300 | Drospirenone 4mg, Desogestrel 75μg, Levonorgestrel 30μg 단독 피임약의 피임 효과·안전성 무작위 비교 시험. 수유 중 여성을 주요 대상군으로 포함하며 desogestrel 직접 평가 |
| [NCT00374972](https://clinicaltrials.gov/study/NCT00374972) | N/A | 철회 | 0 | 수유 기간 중 합산 호르몬 피임약 vs. 단독 프로게스틴 피임약의 수유 효과 비교 연구. 등록 없이 철회하여 유효 데이터 없음 |

---

## 문헌 근거

### 여드름 (Acne)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8894800](https://pubmed.ncbi.nlm.nih.gov/8894800/) | 1996 | RCT | Int J Fertil Menopausal Stud | Desogestrel OC(Marvelon) vs cyproterone acetate OC(Diane): 동양 여성 여드름 치료 직접 비교 |
| [8689881](https://pubmed.ncbi.nlm.nih.gov/8689881/) | 1996 | Controlled Trial | Contraception | EE+gestodene vs EE+desogestrel: 여드름 병변 수 감소 및 유리 안드로겐 지수(FAI) 개선 직접 비교 |
| [2956138](https://pubmed.ncbi.nlm.nih.gov/2956138/) | 1987 | Controlled Trial | Eur J Obstet Gynecol Reprod Biol | 과안드로겐성 소월경 청소년에서 EE+desogestrel 6개월 투여: LH·안드로겐 유의 감소 및 여드름 개선 |
| [2976224](https://pubmed.ncbi.nlm.nih.gov/2976224/) | 1988 | Controlled Trial | Acta Europaea Fertilitatis | 고안드로겐 청소년 19명에서 EE+desogestrel 12개월: 여드름 전반적 개선, 58%에서 다모증 경감 |
| [8200468](https://pubmed.ncbi.nlm.nih.gov/8200468/) | 1994 | Clinical Trial | Eur J Obstet Gynecol Reprod Biol | 이상(biphasic) desogestrel OC의 과안드로겐혈증 및 여드름 치료 효과·안전성 평가 (n=63) |
| [6084924](https://pubmed.ncbi.nlm.nih.gov/6084924/) | 1984 | RCT | Acta Derm Venereol | 여드름 여성에서 desogestrel+EE vs levonorgestrel+EE: SHBG 상승 및 유리 테스토스테론 감소 비교 |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Pharmacodynamic Study | Acta Obstet Gynecol Scand Suppl | Desogestrel 단독 및 EE 복합 투여 시 약력학: PCO-유사 여성 대상 안드로겐성 프로필 직접 평가 |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | 프로게스틴의 안드로겐성 체계적 검토: desogestrel의 낮은 안드로겐성 특성 및 여드름 적용 가능성 |
| [8178905](https://pubmed.ncbi.nlm.nih.gov/8178905/) | 1994 | Clinical/Metabolic Study | Am J Obstet Gynecol | 미국 최초 허가 desogestrel OC의 임상·대사 특성 및 내약성 광범위 검토 |
| [8520092](https://pubmed.ncbi.nlm.nih.gov/8520092/) | 1995 | Review | Ann Pharmacother | 제3세대 프로게스틴(desogestrel, norgestimate, gestodene) 비교: 화학·약동학·효능·내약성 |

### 무월경 (Amenorrhea)

※ PMID 2956138(1987)과 PMID 2976224(1988)는 과안드로겐성 소월경 청소년 연구로 무월경과도 직접 관련되나, 위 여드름 섹션에서 이미 제시되었습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Comparative Study | Gynecol Endocrinol | 심혈관 위험인자 여성에서 drospirenone 4mg vs desogestrel 75μg: 9주기에 걸친 출혈 패턴 및 무월경 발생률 직접 비교 |
| [11725730](https://pubmed.ncbi.nlm.nih.gov/11725730/) | 2001 | Clinical Study | J Reprod Med | 시상하부성 소월경 여성에서 OC의 EE 용량에 따른 골밀도 손실 및 골 미세구조에 대한 영향 평가 |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | Comparative RCT | Br J Obstet Gynaecol | Desogestrel 150μg+EE 20μg(Mercilon) vs +EE 30μg(Marvelon): 피임 효과·주기 조절·부작용 비교 |
| [23221134](https://pubmed.ncbi.nlm.nih.gov/23221134/) | 2012 | Clinical Study | Georgian Med News | 중추성 기능성 월경 장애(소월경·무월경) 여성 159명의 발병 기전 분석 및 호르몬 치료 효과 평가 |

---

## 안전성 고려사항

- **정맥혈전색전증(VTE) 위험**: 제3세대 프로게스틴 포함 복합 피임약(desogestrel+EE)은 제2세대 대비 VTE 상대위험도가 높다는 역학 연구가 있음 (PMID 10652979). 고위험군(혈전성 돌연변이 보유자, 35세 이상 흡연자 등) 대상 사용 시 개별 위험-이익 평가 필요
- **주기 조절 문제**: Desogestrel 75μg 단독제제(POP) 사용 시 불규칙 출혈 및 무월경 발생률이 높아 치료 순응도에 영향을 미칠 수 있음 (PMID 35261299). 복합제 대비 주기 예측성이 낮음

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
여드름 적응증에 대해 완료된 Phase 4 임상시험(NCT01466673, n=201)과 다수의 RCT·대조 임상 연구가 존재하며 (근거 수준 L2), Desogestrel의 항안드로겐 작용 기전은 여드름 병태생리와 직접 연결됩니다. 무월경(Amenorrhea) 역시 L3 수준의 근거와 명확한 HPO 축 기전 연결성을 가집니다. 단, 대부분의 근거가 복합제(desogestrel+EE) 기반이며, 단독 POP(75μg)에 대한 적용 시 추가 연구가 필요합니다.

**진행하려면 필요한 것:**
- 상세 작용 기전(MOA) 확보: DrugBank API를 통한 etonogestrel 활성 대사 경로 및 수용체 결합 데이터 조회
- 현지 허가사항·안전성 정보 수집: MFDS 또는 TFDA 仿單(경고·금기 포함) 다운로드 및 파싱 (현재 Blocking 데이터 갭)
- 단독 제제(POP, 75μg) vs 복합제(EE 포함) 간 여드름 치료 효능 비교 연구 설계
- VTE 위험 모니터링 계획 및 고위험군 스크리닝 기준 수립
- "Lactation Disease" 적응증 재정의 필요: 수유기 피임 관리(safe contraception during lactation) vs. 수유 장애(lactation disorder) 여부 명확화 후 별도 평가 진행
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

