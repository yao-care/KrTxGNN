---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: 만성 B형 간염에서 만성 C형 간염 바이러스 감염으로

## 한 문장 요약

Entecavir는 HBV DNA 중합효소(역전사효소)를 직접 억제하는 뉴클레오시드 유사체로, 전 세계적으로 만성 B형 간염 치료 1차 약제로 허가되어 있으나 한국에는 아직 시판되지 않습니다.
TxGNN 모델은 **만성 C형 간염 바이러스 감염(Chronic Hepatitis C Virus Infection)**에 효과가 있을 가능성을 예측하지만(점수 99.98%),
검색된 **40건의 임상시험**과 **20편의 문헌** 중 Entecavir의 HCV 직접 치료 효과를 입증하는 연구는 존재하지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 B형 간염 (전 세계 허가; 한국 허가 없음) |
| 예측 신규 적응증 | 만성 C형 간염 바이러스 감염 (Chronic HCV Infection) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 한국 규제 데이터베이스에 Entecavir의 공식 MOA 상세 정보가 수집되지 않은 상태입니다. 알려진 정보에 따르면, Entecavir는 **구아노신 뉴클레오시드 유사체**로 체내에서 삼인산(triphosphate) 형태로 활성화된 후 HBV DNA 중합효소의 세 가지 기능 단계—프라이머 합성, 음성 가닥 역전사, 양성 가닥 DNA 합성—를 경쟁적으로 억제합니다. 내성 장벽이 높고 바이러스 억제력이 강력하여 미국 FDA·EMA 등 전 세계 주요 규제 기관에서 만성 B형 간염 1차 치료제로 허가받았습니다.

반면, C형 간염 바이러스(HCV)는 **양성 단일가닥 RNA 바이러스(Flaviviridae 과)**로서 NS5B RNA 의존성 RNA 중합효소(RdRp)를 사용하여 복제합니다. Entecavir의 표적 효소인 HBV DNA 중합효소(역전사효소)와 HCV NS5B RdRp는 구조·기능·서열에서 근본적으로 다릅니다. **기전적 직접 연결 고리가 존재하지 않으며**, 현재 표준 HCV 치료는 NS5B를 효과적으로 억제하는 DAA(직접 작용 항바이러스제, 예: sofosbuvir)입니다.

TxGNN의 높은 예측 점수는 HBV와 HCV의 강한 역학적 공동 이환(co-morbidity) 관련성에서 비롯된 것으로 추정됩니다. 두 바이러스는 전파 경로를 공유하여 공동감염이 빈번하며, 실제 임상 현장에서 Entecavir는 DAA 치료 중 HBV 재활성화 예방 목적으로 HCV/HBV 공동감염 환자에게 사용됩니다. 이러한 공동 발생 패턴이 지식 그래프 추론에 영향을 미쳐 모델이 과대 평가를 한 것으로 분석됩니다.

---

## 임상시험 근거

만성 C형 간염 바이러스 감염 적응증으로 검색된 임상시험 중 가장 관련성이 높은 시험입니다. 검색된 40건 중 Entecavir의 HCV 직접 치료 효능을 평가한 시험은 없으며, 대부분은 HBV 연구이거나 HBV/HCV 공동감염 맥락에서 HBV 관리를 평가한 연구입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | 불명 | 60 | HCV/HBV 공동감염 환자에서 만성 HCV의 DAA 치료 중 예방적 핵산 유사체(NUC)가 HBV 임상 재활성화를 예방하는지 3군 오픈라벨 무작위 비교; Entecavir는 HBV 예방 성분으로 포함 |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 완료 | 23 | 만성 HCV/HBV 공동감염 환자에서 직접 항-HCV 치료(DAA) 중 HBV 복제 재활성화 발생률·이환율·위험 인자 전향적 조사; Entecavir는 HBV 치료 성분으로 포함 |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | 완료 | 130 | Arabinoxylan 쌀겨 추출물(MGN-3/Biobran)을 이용한 간세포암 및 B형·C형 간염 치료 무작위 임상 연구; HCV가 언급되나 Entecavir의 직접적인 HCV 효능 평가 없음 |
| [NCT03662568](https://clinicaltrials.gov/study/NCT03662568) | Phase 1 | 완료 | 56 | 건강 피험자 대상 Morphothiadine Mesilate/Ritonavir와 Entecavir 또는 TDF의 약물-약물 상호작용(DDI) 및 약동학 평가; HCV 직접 치료 연구 아님 |

> ⚠️ **Entecavir가 HCV를 직접 치료 목적으로 평가한 임상시험은 현재 등록되어 있지 않습니다.**

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | 임상 연구 | Viruses | 항-HCV 항체 양성 만성 HBV 환자 66명을 대상으로, NUC(핵산 유사체) 치료 중 HCV 재활성화 발생 여부 및 바이러스 부하 변화를 코호트 연구로 분석 |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | HBV/HCV 공동감염 치료의 최신 발전; 높은 간경변·간세포암 발생 위험과 치료 전략 논의 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | HBV 및 HCV 치료 항바이러스제(entecavir, lamivudine 등)의 신기능 영향 종합 검토 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | 만성 HBV 및 HCV 치료 현황(pegylated IFN, lamivudine, entecavir 포함) 및 미래 치료 전망 검토 |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Review | Clin Res Hepatol Gastroenterol | 소아의 HBV 및 HCV 감염 관리 현황과 전망; 수직 감염 경로, 자연 경과, 치료 옵션 비교 |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | 사례 보고/Review | Clin Res Hepatol Gastroenterol | HBV/HCV 공동감염의 역학(유병률 과소 추정), 중증 간 손상·간경변·간세포암 고위험도, 치료 과제 분석 |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | 임상 연구 | J Gastroenterol Hepatol | 만성 HCV 환자가 DAA 치료를 받는 중 HBV 재활성화 위험 조사; 예방적 항바이러스제(NUC 포함)의 역할 논의 |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | 임상 연구 | J Viral Hepat | 인터페론 없는 항-HCV 치료 중 HBV 재활성화 발생 특성 분석; HBV 공동감염자 25명·해소된 HBV 감염자 765명 포함 |

---

## 한국 시판 정보

현재 Entecavir는 **한국에 시판 허가된 품목이 없습니다** (총 0건). 전 세계적으로 만성 B형 간염 치료제로 허가되어 있으며(예: 미국 FDA 승인 상품명 Baraclude®), 국내 시판을 위해서는 식품의약품안전처(MFDS)에 별도의 품목 허가 신청이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Entecavir와 만성 C형 간염 바이러스 감염 사이에는 근본적인 기전적 불일치가 있습니다. HBV DNA 중합효소(역전사효소)를 표적으로 하는 Entecavir는 HCV가 사용하는 NS5B RNA 의존성 RNA 중합효소에 대한 직접적인 억제 메커니즘을 갖지 않으며, 현존하는 40건의 임상시험 어디에서도 HCV 자체에 대한 직접 치료 효능이 평가되거나 확인된 바 없습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 상세 데이터 수집 (DrugBank API 조회 권장; 현재 데이터 공백)
- 한국 MFDS 허가 신청을 위한 안전성 프로파일(경고, 금기, DDI) 확보
- Entecavir의 HCV NS5B RdRp에 대한 in vitro 억제 활성 데이터 확인 (기전적 가능성 낮음으로 판단)
- **우선 검토 권장**: TxGNN 예측 2위 **만성 B형 간염 바이러스 감염 (근거 수준 L1, Proceed with Guardrails)** — Entecavir의 전 세계 허가 적응증이며 풍부한 Phase 3 임상 근거를 보유하고 있으므로, 한국 MFDS 허가 신청이 최우선 과제로 판단됩니다
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

