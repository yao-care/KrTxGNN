---
layout: default
title: Rifampicin
parent: 중등도 근거 (L3-L4)
nav_order: 601
evidence_level: L3
indication_count: 10
---

# Rifampicin
{: .fs-9 }

근거 수준: **L3** | 예측 적응증: **10** 건
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

# Rifampicin: 결핵(항균 치료제)에서 결막염(Conjunctivitis)으로

## 한 문장 요약

Rifampicin은 세균의 RNA 중합효소를 억제하는 광범위 항균제로, 전세계적으로 결핵을 비롯한 다양한 세균 감염 치료에 사용되어 온 약물입니다. TxGNN 모델은 **결막염(Conjunctivitis)**에도 효과가 있을 수 있다고 예측하며(예측 점수 99.95%), 현재 등록된 임상시험은 없으나 **20편의 문헌**(트라코마 대상 대조 시험 포함)이 이 방향을 뒷받침합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 결핵 등 세균 감염 치료 (rifamycin 계열 항생제; 한국 허가 데이터 없음) |
| 예측 신규 적응증 | 결막염 (Conjunctivitis) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question (추가 연구 필요 단계) |

---

## 이 예측이 타당한 이유는?

DrugBank의 정식 작용기전(MOA) 데이터는 아직 수집되지 않았지만, 근거 문헌들은 일관되게 rifampicin이 **세균의 DNA 의존성 RNA 중합효소(RNA polymerase)를 억제**하여 살균 작용을 나타낸다는 점을 보여줍니다. 이 기전은 포도상구균, 수막구균, 트라코마 클라미디아(*Chlamydia trachomatis*) 등 결막염을 일으키는 주요 병원균에 대해 직접적인 항균 활성을 가집니다.

특히 트라코마(trachoma)는 클라미디아 감염으로 인한 만성 결막염의 대표적 질환으로, 1970년대부터 국소(연고) 형태의 rifampicin이 테트라사이클린과 대등한 효능으로 치료에 사용된 역사적 경험이 있습니다. 즉 이번 예측은 완전히 새로운 기전을 제시하는 것이 아니라, 기존에 알려진 항균 스펙트럼의 자연스러운 확장에 해당합니다.

실제로 문헌에는 수막구균성 결막염 환자에게 전신 rifampin을 투여해 합병증 없이 치료한 증례, 다양한 결막염 원인균에 대한 항생제 감수성 조사 등이 다수 포함되어 있어, 이 예측은 알고리즘적 노이즈라기보다 실제 약리학적 근거에 기반한 것으로 판단됩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1096630](https://pubmed.ncbi.nlm.nih.gov/1096630/) | 1975 | 대조 임상시험(구식) | American Journal of Ophthalmology | 튀니지 학동 대상 통제 시험에서 1% rifampicin 연고가 5% 붕산 대조군보다 우수한 임상 개선을 보였으며 테트라사이클린과 유사한 효능 확인 |
| [6635446](https://pubmed.ncbi.nlm.nih.gov/6635446/) | 1983 | Review | Reviews of Infectious Diseases | 중량 기준 rifampin이 *C. trachomatis*에 가장 강력한 항생제이며, 트라코마 국소치료에서 테트라사이클린과 동등한 효과 |
| [5411121](https://pubmed.ncbi.nlm.nih.gov/5411121/) | 1970 | 기전 연구 | Nature | rifampicin 및 유도체(rifamycin SV)의 항트라코마 활성을 실험적으로 입증 |
| [19941479](https://pubmed.ncbi.nlm.nih.gov/19941479/) | 2010 | Review | Current Medicinal Chemistry | 부룰리 궤양·트라코마 등 소외열대질환 개관에서 rifampin 병용요법이 치료 옵션으로 언급 |
| [33457332](https://pubmed.ncbi.nlm.nih.gov/33457332/) | 2020 | 균주 감수성 조사 | Advanced Biomedical Research | 이란 카샨 지역 결막염 환자 분리균의 세균학적 원인 및 항생제 감수성 조사 |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | 균주 감수성 조사 | J Ophthalmic Inflamm Infect | 나이지리아 라고스 결막염 환자의 세균학적 원인·내성 양상 및 플라스미드 분석 |
| [15228931](https://pubmed.ncbi.nlm.nih.gov/15228931/) | 2004 | 균주 감수성 조사 | Anales de Pediatría | 세균성 결막염의 주요 병원체 및 항생제 감수성 분석, 국소 항생제 치료 필요성 강조 |
| [8363150](https://pubmed.ncbi.nlm.nih.gov/8363150/) | 1993 | 후향적 미생물학 연구 | Anales Españoles de Pediatría | 신생아 결막염 50례 분석, 페니실린 제외 대부분 약물에 높은 세균 감수성 확인 |
| [14686993](https://pubmed.ncbi.nlm.nih.gov/14686993/) | 2003 | 증례 보고 | Clin Microbiol Infect | 6세 소아 원발성 수막구균성 결막염 증례, 국소치료 후 전신 rifampin 투여로 합병증 없이 치유 |
| [21191558](https://pubmed.ncbi.nlm.nih.gov/21191558/) | 2010 | 균주 감수성 조사 | Rev Esp Quimioter | 결막염을 유발하는 *Corynebacterium macginleyi* 균주의 항생제 감수성 분석 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question (Hold에 준하는 추가 연구 필요 단계)**

**사유:**
트라코마(만성 클라미디아성 결막염)에 대한 1970~80년대 대조 시험과 항균 기전상 타당성은 확인되나, 현재 결막염 적응증을 목표로 한 등록 임상시험이 전무하며 근거 대부분이 30년 이상 경과한 소규모 시험·병원체 감수성 조사·증례 보고 수준(L3)에 머물러 있습니다. 한국 내 허가 및 시판 이력도 없어 즉시 진행 가능한 단계가 아닙니다.

**진행하려면 필요한 것:**
- TFDA(한국 규제기관) 수준의 rifampicin 허가사항·경고·금기사항 확보 (현재 Blocking 데이터 갭)
- DrugBank 등 공식 자료를 통한 상세 작용기전(MOA) 확보
- 현대적 진단 기준에 따른 세균성/클라미디아성 결막염 대상 전향적 임상시험 설계
- 국소(점안) 제형 개발 가능성 및 안전성 자료 확보
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

