---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: 류마티스 관절염에서 강직성 척추염(Ankylosing Spondylitis)으로

## 한 문장 요약

Tocilizumab은 IL-6 수용체를 표적으로 하는 인간화 단일클론항체로, 문헌상 류마티스 관절염·전신형/다관절형 소아특발성관절염 치료에 주로 사용되어 왔습니다 (공식 허가 적응증 문서는 자료 없음). TxGNN 모델은 **강직성 척추염(Ankylosing Spondylitis)**에도 효과가 있을 수 있다고 99.99% 점수로 예측했으나, 실제로는 **9건의 임상시험**과 **19편의 문헌** 중 해당 적응증을 직접 검증한 2건의 Phase 3 RCT가 모두 **유효성 부족으로 조기 종료(TERMINATED)**되어 예측과 상반되는 부정적 신호가 확인됩니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 류마티스 관절염, 소아특발성관절염 등 (문헌 근거 기반 — 공식 허가 적응증 문서는 Data Gap) |
| 예측 신규 적응증 | 강직성 척추염 (Ankylosing Spondylitis) |
| TxGNN 예측 점수 | 99.99% (rank 493) |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

## 이 예측이 타당한 이유는?

공식 작용기전(MOA) 문서는 확인되지 않았으나(Data Gap), 수집된 문헌에 따르면 Tocilizumab은 IL-6 수용체(IL-6R)에 결합해 IL-6 신호전달을 차단하는 재조합 인간화 단일클론항체입니다. 류마티스 관절염, 거대세포동맥염, 전신형/다관절형 소아특발성관절염 등 IL-6가 핵심 병인으로 작용하는 질환에서 효능이 입증되어 있습니다.

그러나 강직성 척추염(AS)의 병리 기전은 주로 **IL-17/TNF 축**이 주도하며, IL-6의 역할은 상대적으로 제한적입니다. 실제로 이 가설을 직접 검증한 두 건의 핵심 Phase 3 RCT(NCT01209689, NCT01209702)가 모두 **유효성 부족을 이유로 조기 종료**되었습니다. 즉 TxGNN의 높은 예측 점수에도 불구하고, 실제 임상시험 결과는 이 적응증 확장에 불리한 근거를 제공합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | TERMINATED | 113 | TNF길항제 불충분반응 AS 환자 대상 위약대조 RCT — **유효성 부족으로 조기 종료(음성 신호)** |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | TERMINATED | 306 | TNF-naive AS 환자 대상 Ⅱ/Ⅲ상 seamless 위약대조 시험 — **동일하게 조기 종료** |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | COMPLETED | 1431 | Inflectra(인플릭시맙) 실사용 관찰연구, TCZ 직접 시험 아님 |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | RECRUITING | 2500 | 전신 염증질환 환자군 사이토카인 프로파일 종단관찰, AS 특이적이지 않음 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | UNKNOWN | 750000 | 생물학적제제 치료 환자의 타 면역매개질환 발생 위험 관찰연구 |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | COMPLETED | 60 | RA 환자에서 TCZ의 Tfh세포 효과 기전연구, AS 아님 |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | RECRUITING | 10000 | 한국 류마티스학회 생물학적제제 레지스트리(AS 포함 안전성 관찰) |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | NOT_YET_RECRUITING | 52 | Takayasu 동맥염 대상 세쿠키누맙(IL-17) 평가, TCZ 아님·미모집 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | NOT_YET_RECRUITING | 80 | 견관절 치환술 예정 류마티스 환자 면역억제제 관리 연구, 미모집 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Ann Rheum Dis | BUILDER-1/2 연구: AS 환자에서 Tocilizumab의 단기 증상 개선 효능 평가 (핵심 근거, 제목상 긍정적 결론 아님에 유의) |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Review(네트워크 메타분석) | Medicine | AS 생물학적제제 요법 비교 효과 네트워크 메타분석 |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | AS에서 IL-6 길항의 이론적 근거 및 한계 정리 |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clin Exp Rheumatol | RA·AS에서 생물학적제제 치료 개관, TNF-α 축의 중요성 강조 |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | TNF 억제제 불응 AS 환자의 대체 치료 옵션 검토 |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clin Rheumatol | AS·nr-axSpA 환자의 생물학적제제 관련 중증감염 위험 정량 분석 |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Cohort/Review | Semin Arthritis Rheum | RA·PsA·AS에서 2차 생물학적제제 선택 전략 |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporos Int | RA·AS에서 생물학적제제의 전신 골 영향 |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case Report | Joint Bone Spine | TNF길항제 불응 AS+크론병 환자에서 Tocilizumab 사용 사례 |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Front Med | AS 관련 AA 아밀로이드증에 Tocilizumab 성공 치료 사례 2건 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 매우 높지만(99.99%), 이를 직접 검증한 두 건의 핵심 Phase 3 RCT(NCT01209689, NCT01209702)가 모두 유효성 부족으로 조기 종료되어 실제 임상 근거는 예측과 반대 방향을 가리킵니다. AS의 병리 기전이 IL-17/TNF 축 중심이라는 점도 IL-6 억제 기전의 상대적 약점을 뒷받침합니다. 근거 수준(L2)에도 불구하고 방향성이 부정적이므로 이 적응증에 대한 추가 투자는 보류를 권장합니다.

**진행하려면 필요한 것:**
- BUILDER-1/2 연구(PMID 23765873)의 상세 결과(효능 지표별 세부 데이터) 확인
- 공식 작용기전(MOA) 및 허가 적응증 문서 확보 (DG001, DG002 해소)
- 한국 내 허가/시판 현황 자료 (현재 0건, 미출시)
- AS 이외 하위집단(예: IL-6 우세 표현형)에 대한 바이오마커 기반 재평가 여부 검토

---

**참고 — 동일 Evidence Pack 내 더 강한 근거를 가진 예측**: 이번 후보(rank 1, AS)보다 rank 7 **다관절형 소아특발성관절염(polyarticular JIA)**과 rank 10 **RF양성 다관절형 JIA**는 각각 L1 근거 수준에 완료된 Phase 3 핵심시험(WA19977, CHERISH 등)을 보유하며 "Proceed with Guardrails"로 평가되었습니다. 이는 이미 공지된 적응증과 유사하지만, 별도 평가 보고서로 다룰 가치가 있습니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

