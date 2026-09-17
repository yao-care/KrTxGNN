---
layout: default
title: Ribavirin
parent: 모델 예측만 (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
---

# Ribavirin
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

# Ribavirin: 적응증 정보 없음에서 만성 B형 간염 바이러스 감염으로

## 한 문장 요약

Ribavirin은 광범위 항바이러스제(구아노신 유사체)로서 주로 C형 간염(HCV) 치료 병용요법에 사용되어 온 약물이나, 원 적응증 및 작용기전(MOA) 상세 정보는 현재 확보되지 않았습니다. TxGNN 모델은 **만성 B형 간염 바이러스 감염(Chronic Hepatitis B Virus Infection)**에 효과가 있을 수 있다고 예측(점수 99.86%)하며, 임상시험 50건과 문헌 20편이 검색되었으나, **검토 결과 임상시험 대부분이 실제로는 C형 간염(HCV) 시험이며 HBV 적응증에 잘못 연결(disease mapping 오류)된 것으로 의심**되어 직접적 근거는 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (원 적응증/MOA 데이터 미확보) |
| 예측 신규 적응증 | 만성 B형 간염 바이러스 감염 (Chronic Hepatitis B Virus Infection) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L3 (단, 임상시험 근거 대부분이 disease mapping 오류로 실질적 근거는 더 낮을 가능성) |
| 한국 시판 현황 | 미상영 (허가 제품 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 Ribavirin의 상세 작용기전(MOA) 데이터는 확보되지 않았습니다. 다만 알려진 약리학적 특성상 Ribavirin은 구아노신 뉴클레오사이드 유사체로, IMPDH(이노신일인산탈수소효소) 억제, 치사적 돌연변이 유도, 면역조절 등 광범위 항바이러스 기전을 가지며, 특히 인터페론과 병용 시 HCV(RNA 바이러스)에 대해 명확한 상승효과를 보여왔습니다.

그러나 B형 간염 바이러스(HBV)는 DNA 바이러스로 HCV와 복제 기전이 근본적으로 다르며, HBV에 대한 Ribavirin의 직접적인 항바이러스 작용 근거는 확인되지 않습니다. 현재 검색된 문헌들은 대부분 **HBV/HCV 동시감염** 환자군에서 Ribavirin이 HCV 치료 성분으로 사용된 맥락을 다루고 있을 뿐, HBV 단독 치료 효과를 입증하는 근거는 아닙니다.

**⚠️ 데이터 품질 주의사항**: 검색된 임상시험 50건 중 대다수가 제목 검토 결과 실제로는 만성 C형 간염(HCV) 환자를 대상으로 한 peg-interferon/ribavirin 또는 DAA 병용요법 시험이며, HBV 적응증에 잘못 매핑된 것으로 판단됩니다. 이는 예측의 신뢰도를 낮추는 핵심 요인이므로, 진행 전 disease mapping 재검증이 필요합니다.

## 임상시험 근거

> 아래 표는 검색된 임상시험 중 일부를 발췌한 것입니다. **[grade: C]로 표시된 항목은 실제로는 HCV 시험으로, HBV 적응증과 무관함이 확인되었습니다.** HBV와 직접 관련된 시험(HBV/HCV 동시감염 포함)은 거의 없습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 완료 | 23 | HBV/HCV 동시감염 환자에서 direct antiviral agent 치료 중 HBV 재활성화 위험·발생률 평가 (HBV 관련성이 가장 높은 시험이나 ribavirin의 HBV 직접 치료 효과는 아님) |
| [NCT00215865](https://clinicaltrials.gov/study/NCT00215865) [grade: C] | Phase 3 | 완료 | 600 | 실제로는 만성 C형 간염(peg-IFN+ribavirin) 재치료 시험, HBV와 무관 — mapping 오류 사례 |
| [NCT01598090](https://clinicaltrials.gov/study/NCT01598090) [grade: C] | Phase 3 | 완료 | 881 | Genotype-1 만성 C형 간염 대상 peg-IFN lambda vs alfa + ribavirin + telaprevir 비교, HBV와 무관 — mapping 오류 사례 |
| [NCT01220947](https://clinicaltrials.gov/study/NCT01220947) [grade: C] | Phase 2 | 완료 | 421 | Danoprevir/ritonavir + Pegasys/Copegus, 만성 C형 간염 치료-naive 환자 대상, HBV와 무관 — mapping 오류 사례 |

나머지 46건은 관련성 검토(relevance grading)가 "pending" 상태이나, 제목 검토상 대부분 C형 간염 시험으로 추정됩니다. **HBV 특이적 ribavirin 단독/병용 요법을 직접 검증한 임상시험은 현재 확인되지 않습니다.**

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV 동시감염 시 peg-IFN+ribavirin 병용요법이 HCV RNA 양성 동시감염자에게 권고됨(HBV 자체 치료 근거는 아님) |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | HBV/HCV 동시감염의 치료 및 예후 업데이트 |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatol Int | HBV·HCV 동시감염의 바이러스 간 상호작용 및 장기 예후 고찰 |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | HBV/HCV 동시감염 치료는 간학 전문의에게 여전히 난제임을 지적 |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | HBV·HCV 각각의 표준치료(IFN±ribavirin, DAA) 비교, HCV는 완치 가능하나 HBV는 지속 억제만 가능함을 명시 |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Review | Semin Liver Dis | 만성 HBV·HCV 감염의 숙주 유전학적 결정요인 고찰 |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | 소아 만성 HBV·HCV 감염 치료 옵션(성인 대비 제한적 데이터) |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | HBV·HCV 치료 유도 청소반응의 면역학적 기전 비교 |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | 만성 HBV·HCV 감염에서 간세포암 예방을 위한 항바이러스 치료 전략 |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | 만성 HBV(IFN, lamivudine)와 HCV(IFN+ribavirin) 치료 전략 비교, HBV 단독요법에 ribavirin은 포함되지 않음 |

**주요 시사점**: 위 문헌들은 HBV와 HCV를 함께 다루는 리뷰가 대부분이며, ribavirin이 HBV 단독 치료제로 효과를 보인다는 직접적 근거는 없습니다. 오히려 다수 문헌이 "HBV는 lamivudine 등 별도 항바이러스제로 치료하며, ribavirin은 HCV 성분"이라는 점을 명확히 구분하고 있습니다.

## 한국 시판 정보

현재 한국에 Ribavirin 허가 제품이 없습니다 (미상영, 허가증 0건). 참조 가능한 국내 첨부문서 정보가 없습니다.

## 안전성 고려사항

안전성 정보(주요 경고, 금기, 약물상호작용)가 수집되지 않았으며, 국내 미상영 상태로 참조할 허가사항도 없습니다. 해외(TFDA/FDA 등) 첨부문서 확인이 별도로 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 높으나(99.86%), 검색된 임상시험 근거 대다수가 실제로는 C형 간염(HCV) 대상 시험이며 B형 간염(HBV) 적응증에 잘못 연결된 것으로 의심됩니다. HBV 특이적 ribavirin 치료 효과를 뒷받침하는 임상 근거가 확인되지 않으며, 안전성 자료(경고·금기·DDI)가 전혀 없어 S1 안전성 초기평가 진입이 불가능한 Blocking Data Gap 상태입니다.

**진행하려면 필요한 것:**
- Disease mapping 정확성 재검증 (50건 임상시험의 HBV/HCV 재분류)
- Ribavirin의 상세 작용기전(MOA) 데이터 확보 (DrugBank API 재조회)
- 해외(TFDA/FDA) 첨부문서를 통한 경고·금기·약물상호작용 정보 확보
- HBV(DNA 바이러스) 특이적 항바이러스 효과를 뒷받침하는 전임상/기전 연구 확보
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

