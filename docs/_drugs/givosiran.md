---
layout: default
title: Givosiran
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: 급성 간성 포르피린증에서 ALA 탈수효소 결핍 포르피린증으로

## 한 문장 요약

Givosiran(Givlaari)은 GalNAc-siRNA 기술로 간 내 ALAS1(ALA 합성효소 1)을 침묵시켜 독성 전구체 ALA·PBG 축적을 예방하는 RNAi 치료제로, 전 세계적으로 급성 간성 포르피린증(AHP) 치료에 허가되어 있으나 한국에서는 미허가 상태입니다. TxGNN 모델은 **ALA 탈수효소 결핍 포르피린증(ALAD Porphyria, Doss 포르피린증)**에 효과가 있을 수 있다고 예측하며, 현재 **8편의 관련 문헌**이 부분적 근거를 제공합니다. 단, 실제 ALAD 포르피린증 환자에서 무반응 증례가 보고되어 있어 현 단계에서는 연구 질문 수준에 머무릅니다.

> ⚠️ **예측 품질 주의**: 상위 1~8번 예측 질환(TxGNN 점수 동일: 99.9999%)은 간 문맥 고혈압, 간경화 관련 질환 등으로 Givosiran의 ALAS1 억제 기전과 병리 경로상 교집합이 없습니다. 동일 점수 클러스터는 지식 그래프의 노드 군집 효과로 판단되며, 이 보고서는 유일하게 기전적 타당성이 확인된 **순위 9번 예측(ALAD 포르피린증)**을 중심으로 분석합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 급성 간성 포르피린증 (AHP) — 해외 허가, 한국 미허가 |
| 예측 신규 적응증 | ALA 탈수효소 결핍 포르피린증 (Porphyria due to ALA dehydratase deficiency) |
| TxGNN 예측 점수 | 99.91% (전체 순위 #2,378) |
| 근거 수준 | L4 (기전 연구·사례 보고) |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Givosiran은 RNA 간섭(RNAi) 기전으로 작동하는 간 표적 치료제입니다. 약물에 결합된 GalNAc(N-아세틸갈락토사민) 리간드가 간세포 표면의 아시아로당단백질 수용체(ASGPR)와 결합하여 선택적으로 세포 내로 전달되고, 세포질에서 RISC(RNA 유도 침묵 복합체)를 통해 ALAS1 mRNA를 분해합니다. 그 결과 혈액·소변 내 ALA(δ-아미노레불린산)와 PBG(포르포빌리노겐) 수치가 저하되어 급성 발작이 예방됩니다.

ALA 탈수효소 결핍 포르피린증(ADP)은 헴 합성 경로의 2번째 효소인 ALAD가 심각하게 결핍되어 ALA가 체내에 축적되는 극희귀 상염색체 열성 질환입니다. 이론적으로 Givosiran이 ALAS1을 억제하여 ALA 생성을 상류에서 차단하면 ADP 환자의 ALA 부하도 줄일 수 있습니다. 실제로 FDA는 Givosiran을 ADP를 포함한 광의의 AHP 질환군에 허가하였으며, 이는 예측의 기전적 타당성을 일부 뒷받침합니다.

그러나 실제 임상 결과는 불확실합니다. ADP에서 ALA의 대사 경로는 급성 간헐성 포르피린증(AIP)과 다를 수 있으며, 납 노출 등 ADP 특유의 촉발 인자는 ALAS1 억제로 영향받지 않을 수 있습니다. PMID 35991568(증례 보고)에서 ADP 환자에게 Givosiran을 투여했을 때 치료 반응이 없었으며, 이는 현재 가장 중요한 임상 근거입니다. 전 세계 ADP 확진 환자 수가 10명 미만이어서 추가 임상 연구 자체가 매우 어려운 상황입니다.

---

## 임상시험 근거

현재 ALA 탈수효소 결핍 포르피린증에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | ⚠️ 증례 보고 | Front Genet | **[핵심]** ALAD 포르피린증 1례에서 Givosiran 무반응 — 재창출 가설에 대한 반박 증거 |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | RCT | J Intern Med | 급성 간헐성 포르피린증(AIP)에서 Givosiran RNAi 치료가 발작률을 유의하게 감소 |
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | Phase 3 보조 분석 | Orphanet J Rare Dis | ENVISION Phase 3 시험: AHP 질환 부담 평가 및 Givosiran 치료 효과 확인 |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Review | Blood | AHP에서 RNA 간섭 치료 기전 및 임상 근거 종합 (ADP 포함 4가지 AHP 아형 다룸) |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | 임상 지침/Review | Rev Clin Esp | 급성 간성 포르피린증 위기 치료 접근법 (ALAD 결핍 포르피린증 아형 포함) |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Phase 3 부분군 분석 | Sci Rep | 일본 AHP 환자 10명 대상 Givosiran 확장 접근 연구: 피하주사 2.5 mg/kg/월 안전성·유효성 확인 |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Review | Drug Des Dev Ther | Givosiran의 설계·개발·치료적 위치에 대한 종합 검토 |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK/PD 모델링 | CPT Pharmacometrics | Phase I~III 통합 데이터 기반 Givosiran 투여 후 요중 ALA 감소의 반기전적 PK/PD 모델 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
ALA 탈수효소 결핍 포르피린증(ADP)은 Givosiran의 ALAS1 억제 기전과 이론적 연관성이 있으나, 실제 ADP 환자에서 무반응 증례가 보고되었고 전 세계 확진 환자가 10명 미만이어서 임상 개발 가능성이 매우 제한적입니다. 상위 1~8번 TxGNN 예측(간 문맥 고혈압·경화 관련 질환 등)은 기전적 교집합이 전혀 없어 재창출 후보에서 제외합니다.

**진행하려면 필요한 것:**
- ALAD 포르피린증 특이적 ALA 대사 경로 분석 (AIP와의 병리 차이 규명)
- 전 세계 ADP 환자 레지스트리 데이터 접근 및 추가 증례 수집
- 작용 기전(MOA) 상세 데이터 확보 (DrugBank DB15066 API 조회 권장)
- 안전성 자료 확보 (FDA Prescribing Information 또는 한국 식약처 허가사항 참조)
- 상위 1~8번 예측에 대한 TxGNN 스코어 클러스터 원인 분석 (지식 그래프 노드 검토)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

