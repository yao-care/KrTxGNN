---
layout: default
title: Plerixafor
parent: 높은 근거 (L1-L2)
nav_order: 559
evidence_level: L2
indication_count: 7
---

# Plerixafor
{: .fs-9 }

근거 수준: **L2** | 예측 적응증: **7** 건
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

# Plerixafor: 조혈모세포 동원에서 골수성 백혈병(Myeloid Leukemia)으로

## 한 문장 요약

Plerixafor는 CXCR4 길항제로, 원래 조혈모세포이식 전 말초혈액줄기세포 동원에 사용되어 온 약물입니다.
TxGNN 모델은 이 약물이 **골수성 백혈병(Myeloid Leukemia)**에도 효과가 있을 수 있다고 예측하며,
현재 **30건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.

> 참고: Evidence Pack에는 총 7개의 예측 적응증이 포함되어 있으나, TxGNN 점수가 가장 높은 상위 6건(형질세포골수종, CMM7, 소아 연수막 흑색종, 상피양세포 포도막흑색종, 기관지염, 외음부 흑색종)은 임상시험·문헌 근거가 전무하여 근거수준 L5·권장 Hold로 평가되었습니다. 실질적으로 검토 가능한 신호는 골수성 백혈병 하나이며, 본 보고서는 이를 중심으로 작성되었습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 조혈모세포 동원 (조혈모세포이식 전처치) — 한국 허가 자료 없음, 임상시험 기록(NCT01319864)상 해외 승인 언급 |
| 예측 신규 적응증 | 골수성 백혈병 (Myeloid Leukemia) |
| TxGNN 예측 점수 | 99.02% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미상장 (시판되지 않음) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

Plerixafor는 CXCR4 길항제로서, 백혈병 줄기세포와 CXCL12(SDF-1)를 발현하는 골수 기질세포 간의 부착을 차단합니다. 이를 통해 백혈병 세포를 보호성 골수 니치(niche)에서 이탈시켜 순환혈로 동원시키고, 결과적으로 화학요법에 대한 감수성을 높이는 "chemosensitization" 효과를 유도합니다.

이 약물은 원래 자가/동종 조혈모세포이식 전 말초혈액줄기세포를 동원하는 데 사용되어 왔습니다. 골수성 백혈병(AML) 역시 백혈병 줄기세포가 동일한 CXCR4/CXCL12 축을 통해 골수 니치에 정착·보호받기 때문에, 기존 적응증(정상 조혈모세포 동원)과 신규 적응증(백혈병 세포 동원 및 화학감작) 사이에는 명확한 기전적 연결고리가 있습니다.

실제로 Plerixafor는 cytarabine/daunorubicin, decitabine, sorafenib, MEC 요법 등 다양한 표준 화학요법과 병용하여 재발성/불응성 AML을 대상으로 한 다수의 1/2상 임상시험에서 검증되었으며, 이는 TxGNN 예측의 생물학적 타당성을 뒷받침합니다. 다만 현재까지는 Phase 3 확증 임상시험 데이터가 없다는 점에 유의해야 합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | 완료 | 39 | 재발/불응성 AML에서 Plerixafor+G-CSF 화학감작 병용요법 평가 |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | 완료 | 52 | AMD3100(Plerixafor)+Mitoxantrone/Etoposide/Cytarabine(MEC) 병용, 골수 미세환경-백혈병모세포 상호작용 차단을 통한 화학요법 세포독성 증강 가설 검증 |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | 완료 | 36 | 신규 진단 AML에서 Plerixafor+Cytarabine+Daunorubicin("7+3" 요법) 용량 증량 시험 |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | 완료 | 71 | 60세 이상 AML 환자 대상 Decitabine+Plerixafor priming 유도요법, 백혈병 줄기세포 동원을 통한 치료 반응 개선 가설 |
| [NCT01236144](https://clinicaltrials.gov/study/NCT01236144) | Phase 1/2 | 완료 | 113 | 고령 AML/고위험 MDS 환자에서 AC220, Plerixafor, Ganetespib를 화학요법과 병용하는 실행가능성 평가(AML18 파일럿) |
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | 완료 | 55 | 65세 이하 재발/불응성 AML에서 FLAG-Ida+G-CSF+Plerixafor 유도요법(PLERIFLAG 요법) |
| [NCT00822770](https://clinicaltrials.gov/study/NCT00822770) | Phase 1/2 | 완료 | 47 | AML/MDS/CML 환자의 동종 조혈모세포이식 전처치에 G-CSF+Plerixafor+Busulfan+Fludarabine 병용 안전성 평가 |
| [NCT00241358](https://clinicaltrials.gov/study/NCT00241358) | Phase 1/2 | 완료 | 92 | 진행성 혈액암 환자에서 AMD3100 동원 후 HLA 일치 형제 공여자 조혈모세포이식 안전성·유효성 평가 |
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | 완료 | 20 | 소아 재발성 급성백혈병/MDS에서 Plerixafor를 화학감작제로 사용, cytarabine+etoposide 병용 안전성 평가 |
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | 완료 | 33 | FLT3 변이 AML에서 Sorafenib+Plerixafor+G-CSF(Neupogen) 병용 최대 내약 용량 결정 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | RCT | Ann Hematol | 재발/불응성 AML에서 FLAG-Ida+고용량 정맥 Plerixafor 병용(PLERIFLAG 요법) Phase 1-2 시험 |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | RCT | Am J Hematol | FLT3-ITD 변이 재발/불응성 AML 28명에서 Sorafenib+Plerixafor+G-CSF 병용 Phase 1 시험 |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | RCT | Haematologica | 고령 신규진단 AML 69명에서 Decitabine+Plerixafor 병용 Phase 1 시험, 백혈병 줄기세포에 미치는 영향 평가 |
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase 1/2 시험 | Blood | 재발/불응성 AML 52명에서 CXCR4 길항제 Plerixafor 화학감작 Phase 1/2 시험 (핵심 근거 논문) |
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | 체계적 문헌고찰 | Leuk Res | Plerixafor+화학요법/조혈모세포이식의 급성백혈병 치료 활용에 대한 전임상·임상 연구 체계적 문헌고찰 및 메타분석 |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | AML에서 CXCR4를 치료 표적으로 삼는 CXCL12-CXCR4 축의 종양유발 과정 전반에 대한 최신 리뷰 |
| [32079173](https://pubmed.ncbi.nlm.nih.gov/32079173/) | 2020 | Review | Biology | AML 및 교모세포종에서 CXCR4 길항제의 줄기세포 동원제 및 치료 감작제로서의 역할 고찰 |
| [26822317](https://pubmed.ncbi.nlm.nih.gov/26822317/) | 2016 | Review | Am J Hematol | AML에서 자가강화형 백혈병 니치를 표적화하는 치료 전략에 대한 고찰 |
| [30150522](https://pubmed.ncbi.nlm.nih.gov/30150522/) | 2018 | Case Report | Cancers | Monosomy 7 동반 불응성 소아 AML 4세 환아에서 Plerixafor+Cytarabine+Melphalan 전처치 요법으로 완전관해 달성 증례 |
| [27822339](https://pubmed.ncbi.nlm.nih.gov/27822339/) | 2016 | Review | World J Stem Cells | AML 백혈병 줄기세포에 대한 새로운 발견과 치료적 기회에 대한 최신 리뷰 |

## 한국 시판 정보

Plerixafor는 현재 한국에서 허가된 제품이 없습니다(시판 현황: 미상장, 허가증 0건). 안전성·적응증 관련 공식 라벨 정보는 미국 FDA(Mozobil®) 등 해외 허가 자료를 별도로 확보해야 합니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (한국 내 허가 자료가 없어 주요 경고, 금기, 약물상호작용 정보를 확인할 수 없습니다.)

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
- 골수성 백혈병 적응증은 CXCR4/CXCL12 축 차단을 통한 화학감작이라는 명확한 기전적 근거를 가지며, 다수의 완료된 Phase 1/2 임상시험(NCT00906945, NCT00512252, NCT00990054 등)과 RCT급 문헌(PMID 29392425, 32697348, 29724902)이 이를 뒷받침합니다.
- 다만 Phase 3 확증 임상시험이 없고, 한국 내 허가·안전성 자료가 전무하여 즉시 진행보다는 가드레일 하에 추가 검증이 필요합니다.
- 그 외 6개 예측 적응증(형질세포골수종, CMM7, 소아 연수막 흑색종, 상피양세포 포도막흑색종, 기관지염, 외음부 흑색종)은 임상시험·문헌 근거가 전무하여 Hold를 유지합니다.

**진행하려면 필요한 것:**
- 미국/EU 허가사항(Mozobil®)의 경고·금기·DDI 정보 확보
- DrugBank API 재조회를 통한 상세 MOA 데이터 확보 (현재 Data Gap)
- Phase 3 확증 임상시험 설계 검토 (기존 시험은 대부분 Phase 1/2, 소규모)
- 한국 내 허가 여부 및 도입 전략 검토 (현재 미상장)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

