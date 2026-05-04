---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin: 세균 감염에서 단클론 감마글로불린병증으로

## 한 문장 요약

Amoxicillin은 β-lactam 계열 광범위 항생제로, 페니실린 결합 단백질(PBP)을 억제하여 세균 세포벽 합성을 차단하는 기전으로 다양한 세균 감염 치료에 사용됩니다.
TxGNN 모델의 8개 예측 중 근거 수준이 가장 높은 **단클론 감마글로불린병증(Monoclonal Gammopathy)**, 특히 세균성 항원 구동 **면역증식성 소장질환(IPSID, α 중쇄 질환)** 아형에서의 재창출 가능성이 주목되며,
현재 **1건의 임상시험**과 **11편의 문헌**이 이 가설을 부분적으로 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 세균 감염 (Bacterial Infections) |
| 예측 신규 적응증 | 단클론 감마글로불린병증 (Monoclonal Gammopathy) |
| TxGNN 예측 점수 | 99.22% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Amoxicillin은 β-lactam 계열 항생제로, 세균의 세포벽 합성에 필수적인 PBP(Penicillin-Binding Proteins)에 결합하여 펩티도글리칸 교차결합 형성을 저해합니다. 이 기전은 통상적인 단클론 감마글로불린병증—MGUS, 다발성 골수종, Waldenström 대구형적혈구혈증 등—의 치료와는 직접적인 관련이 없습니다. 그러나 특정 아형인 **면역증식성 소장질환(IPSID)**에서는 예외적인 생물학적 타당성이 성립합니다.

IPSID(지중해 림프종, Immunoproliferative Small Intestinal Disease)는 *Helicobacter pylori*, *Campylobacter jejuni* 등 세균이 소장 점막 B세포를 지속적으로 자극하여 단클론 증식을 유도하고, 절단형 IgA α 중쇄(일종의 단클론 면역글로불린 이상)를 생산하는 희귀 림프종 전구 질환입니다. IPSID **초기 단계**에서는 원인 세균 제거—amoxicillin 포함 H. pylori 삼제요법 등—만으로도 조직학적 완전 관해가 가능하다는 증례 보고가 복수 존재하며, 이는 TxGNN 예측의 핵심 기전적 근거를 이룹니다.

⚠️ **핵심 제한 사항**: 이 기전적 연결은 IPSID 아형에만 특이적으로 적용됩니다. 다른 단클론 감마글로불린병증에는 생물학적 근거가 없으며, TxGNN 고득점(0.9922)은 감염-면역글로불린병증 간 지식 그래프의 간접 경로 연결을 반영한 것으로 해석됩니다. 연구 대상을 IPSID 아형으로 명확히 제한하지 않으면 임상적 의미가 없습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | Phase N/A | 조기 종료 | 351 | 저위험 호중구감소증 암 환자 발열 치료에서 Amoxicillin-Clavulanate + Ciprofloxacin vs Moxifloxacin 단독 비교. 단클론 감마글로불린병증 직접 치료를 목적으로 하지 않으며 조기 종료됨 (관련성 C등급) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/) | 1996 | Case Series | Internal Medicine (Tokyo) | 지중해 림프종(IPSID) 환자에서 항생제 단독 치료로 완전 관해 및 단클론 IgA α 중쇄 음성 전환 보고 |
| [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/) | 2010 | Case Series | J Gastrointest Cancer | H. pylori 제균(amoxicillin 포함 삼제요법) 후 IPSID 조직학적 완전 관해 사례 |
| [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/) | 1997 | Case Report | Lancet | H. pylori 제균 후 IPSID 관해 최초 보고 |
| [16253033](https://pubmed.ncbi.nlm.nih.gov/16253033/) | 2005 | Case Report | Arch Pathol Lab Med | 비분비형 IPSID 원위 소장·림프절 침범 증례—면역표현형 및 분자생물학적 특성 기술 |
| [35619805](https://pubmed.ncbi.nlm.nih.gov/35619805/) | 2022 | Case Report | Front Public Health | 대구형적혈구혈증 환자의 파종성 노카르디아증에서 Amoxicillin/Clavulanate 항균 감수성 확인 (간접) |
| [21908119](https://pubmed.ncbi.nlm.nih.gov/21908119/) | 2011 | Case Report | Med Maladies Infect | 단클론 감마글로불린병증 환자에서 Rothia dentocariosa 폐렴 발생 (면역저하 환자 감염 감수성 관련) |
| [20513124](https://pubmed.ncbi.nlm.nih.gov/20513124/) | 2010 | Observational | Am J Hematol | 다발성 골수종에서 갈락토만난 검사 위양성 고발생률 분석 (항감염 진단 맥락) |
| [22092390](https://pubmed.ncbi.nlm.nih.gov/22092390/) | 2012 | Retrospective Cohort | J Oral Pathol Med | 다발성 골수종 및 유방암의 비스포스포네이트 관련 악골괴사 치료 비교—amoxicillin 보조 항생제 포함 표준화 프로토콜 |
| [20015614](https://pubmed.ncbi.nlm.nih.gov/20015614/) | 2010 | Case Series | Int J Oral Maxillofac Surg | 보존적 치료 불응 비스포스포네이트 관련 악골괴사 40례 외과적 처치—amoxicillin 보조요법 포함 |
| [18639371](https://pubmed.ncbi.nlm.nih.gov/18639371/) | 2009 | Retrospective Case Series | Br J Oral Maxillofac Surg | 비스포스포네이트 관련 악골괴사에서 약물 중단 후 병적 골절 진행 사례—amoxicillin 보조 사용 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
단클론 감마글로불린병증 전체 범주에 대한 amoxicillin 재창출 근거는 매우 제한적이나, IPSID(면역증식성 소장질환) 특이 아형에서 항생제 기반 H. pylori 제균요법이 완전 관해를 유도한다는 생물학적 타당성은 인정됩니다. 다만 현재 근거가 소규모 증례 보고·시리즈 수준에 머물고, 직접적인 대상 임상시험이 부재하여 즉각적인 개발 진행은 불가합니다.

**진행하려면 필요한 것:**
- 연구 대상을 **IPSID(지중해 림프종, α 중쇄 질환)** 아형으로 명확히 한정하여 연구 질문 재설계
- Amoxicillin 포함 H. pylori 제균요법의 IPSID 완전 관해율에 대한 **체계적 문헌고찰** 수행
- 한국 내 IPSID 환자 접근 가능성 및 유병률 파악 (극희귀 질환이므로 다기관 등록 연구 필요)
- Amoxicillin 작용 기전(MOA) 및 약동학 데이터 보완 (현재 미확보)
- 한국 MFDS 허가 현황 재확인 및 시판 경로 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

