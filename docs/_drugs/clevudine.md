---
layout: default
title: Clevudine
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 8
---

# Clevudine
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

# Clevudine: 만성 B형 간염에서 만성 C형 간염 바이러스 감염으로

## 한 문장 요약

Clevudine은 HBV DNA 중합효소(역전사효소)를 억제하는 뉴클레오사이드 유사체로, 한국에서 만성 B형 간염 치료에 허가되어 있으나 대만에서는 미허가 상태입니다.
TxGNN 모델은 1순위로 **만성 C형 간염 바이러스 감염(Chronic HCV Infection)**에 효과가 있을 수 있다고 예측하며 (예측 점수 99.96%),
수집된 **1건의 임상시험**과 **2편의 문헌**이 있으나 이 모두 HCV 특이적 증거가 아닌 것으로 확인되며, 기전적 불일치로 인해 이 예측은 **그래프 인접성 허위 신호(graph proximity artifact)**로 판단됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 B형 간염 바이러스 감염 (한국 허가; 대만 미허가) |
| 예측 신규 적응증 | 만성 C형 간염 바이러스 감염 (Chronic Hepatitis C Virus Infection) |
| TxGNN 예측 점수 | 99.96% |
| 근거 수준 | L4 |
| 대만 시판 현황 | ✗ 미판매 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 MOA 데이터가 제공되지 않았으나, 기존 문헌(PMID 23774432, PMID 17009935)에 따르면 Clevudine(L-FMAU)은 피리미딘 뉴클레오사이드 유사체입니다. 세포 내에서 5'-삼인산염으로 활성화되어 **HBV 역전사효소(RT)를 비경쟁적으로 억제**하며, 단백질 프라이밍 및 DNA 합성 단계를 동시에 차단합니다. 이는 HBV의 핵내 영구 저장소인 cccDNA 수준 감소로 이어져, 치료 중단 후에도 지속적인 바이러스 억제 효과(sustained suppression)를 나타냅니다.

**HCV 예측은 기전적으로 타당하지 않습니다.** HCV는 양성 단쇄 RNA 바이러스(Flaviviridae)로, NS5B RNA 의존성 RNA 중합효소(RdRp)를 통해 복제합니다. HBV 역전사효소와 HCV NS5B는 효소 기원, 구조, 기질 특이성이 근본적으로 다릅니다. Clevudine 삼인산염이 HCV NS5B를 억제한다는 체외 실험이나 임상 데이터는 보고된 바 없습니다.

TxGNN이 만성 HCV에 99.96%의 높은 점수를 부여한 것은, 지식 그래프 내에서 HBV와 HCV가 모두 "hepatitis(간염)" 상위 노드에 연결되어 있어 발생하는 **그래프 인접성 허위 신호**로 판단됩니다. 실제 생물학적 기전이 아닌 질환 분류 체계의 구조적 인접성이 반영된 결과입니다.

---

## 임상시험 근거

> ⚠️ **오분류 주의**: 수집된 1건은 실제 HBV 시험으로, 만성 HCV 적응증 증거로 사용할 수 없습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00823342](https://clinicaltrials.gov/study/NCT00823342) | Phase 3 | 종료 | 150 | **[오분류 — HBV 시험]** ANRS HB 05: HBeAg 음성 만성 B형 간염 환자에서 Clevudine 단독 vs Tenofovir 단독 vs 96주 병용요법 비교. 시험명의 "HB"는 Hepatitis B를 명시하며 HCV와 무관 |

---

## 문헌 근거

> ⚠️ **관련성 없음**: 수집된 문헌은 Clevudine의 HCV 특이적 데이터를 포함하지 않습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | 만성 B형 및 C형 간염의 현재 치료와 미래 전망 — Clevudine의 HCV 효능 데이터 미포함 |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatric Drugs | 소아 만성 간질환 의학적 관리 일반 리뷰 — HCV에 대한 Clevudine 데이터 없음 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

HBV 임상 경험(TxGNN 2순위 예측 관련)에서 확인된 주요 안전성 우려:
- **근병증(Myopathy)**: 24주 초과 장기 사용 시 발생 보고 (PMID 20196804). 여러 Phase 4 연구(NCT01264133, NCT01264094, NCT01264367 등)가 근육 관련 안전성 우려로 조기 종료됨
- CK(크레아틴키나아제) 정기 모니터링 필수

---

## 결론 및 다음 단계

**결정: Hold** (만성 C형 간염 바이러스 감염 예측)

**사유:**
만성 HCV에 대한 TxGNN 예측은 기전적 타당성이 없으며, 수집된 임상시험 및 문헌 모두 HCV 특이적 Clevudine 증거가 아닌 것으로 판명되었습니다. HCV NS5B RdRp는 Clevudine의 표적인 HBV 역전사효소와 구조적·기능적으로 근본적으로 다른 효소입니다.

**HCV 가설 검증에 필요한 것:**
- HCV NS5B 중합효소에 대한 Clevudine 삼인산염의 체외(in vitro) 억제 활성 측정
- HCV 복제 세포 모델(Huh-7/JFH1 등)에서의 전임상 항바이러스 활성 평가
- 기전적 타당성을 확인하는 구조-활성 관계(SAR) 연구

---

> **📌 실무 참고 — TxGNN 2순위 예측: B형 간염 바이러스 감염 (HBV)**
>
> 대만 미허가 상태에서 **HBV 적응증 신청**이 더 실질적이고 즉각적인 재창출 가치를 가집니다.
>
> | 항목 | 내용 |
> |------|------|
> | TxGNN 예측 점수 | 99.78% |
> | 임상시험 | 29건 (Phase 2/3/4, 완료된 Phase 3 RCT 포함) |
> | 문헌 | 20편 (기전 연구, 비교 임상, 동물 모델 포함) |
> | 근거 수준 | **L1** |
> | 핵심 근거 | [NCT00362635](https://clinicaltrials.gov/study/NCT00362635): 완료된 Phase 3 RCT, Clevudine 48주 vs Lamivudine 비교 (92명) |
> | 주요 안전 우려 | 장기 사용 시 근병증 위험 → CK 모니터링 계획 수립 필수 |
> | 권장 결정 | **Proceed with Guardrails** |

---

> **📋 전체 TxGNN 예측 요약 (8개 적응증)**
>
> | 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 기전 타당성 | 결정 |
> |------|--------|-----------|---------|-----------|------|
> | 1 | 만성 C형 간염 (HCV) | 99.96% | L4 | ❌ 기전 불일치 | **Hold** |
> | 2 | B형 간염 바이러스 감염 (HBV) | 99.78% | L1 | ✅ 직접 표적 | **Proceed with Guardrails** |
> | 3 | C형 간염 바이러스 감염 (HCV) | 99.56% | L4 | ❌ 기전 불일치 | **Hold** |
> | 4 | E형 간염 바이러스 감염 (HEV) | 99.31% | L5 | ❌ 기전 불일치 | **Hold** |
> | 5 | A형 간염 바이러스 감염 (HAV) | 99.30% | L5 | ❌ 기전 불일치 | **Hold** |
> | 6 | 동물 바이러스성 간염 | 99.28% | L3 | ✅ 모델 지지 근거 | Research Question |
> | 7 | Omsk 출혈열 (OHFV) | 99.25% | L5 | ❌ RNA 바이러스 | **Hold** |
> | 8 | Kyasanur Forest 병 (KFDV) | 99.23% | L5 | ❌ RNA 바이러스 | **Hold** |
>
> **패턴 분석**: 8개 예측 중 7개가 "간염" 또는 "바이러스성 감염" 노드 인접성에서 비롯된 허위 신호이며, HBV(2순위)만이 실제 생물학적 기전과 임상 증거를 갖춘 유효한 예측입니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

