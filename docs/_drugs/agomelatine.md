---
layout: default
title: Agomelatine
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatine: 주요 우울 장애에서 불안장애로

## 한 문장 요약

Agomelatine은 유럽 및 호주에서 주요 우울 장애(Major Depressive Disorder, MDD) 치료에 승인된 약물로, MT1/MT2 멜라토닌 수용체 작용 및 5-HT2C 세로토닌 수용체 길항이라는 독자적인 이중 기전을 가진 항우울제입니다.
TxGNN 모델은 **불안장애(Anxiety Disorder)**에 효과가 있을 수 있다고 예측하며, 현재 **0건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
2025년에 발표된 시스템 고찰 및 네트워크 메타분석(PMID 38804215)을 포함한 다수의 고품질 문헌이 광범위 불안장애(GAD)에 대한 Agomelatine의 임상적 효능을 확인하고 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 주요 우울 장애 (유럽·호주 승인) |
| 예측 신규 적응증 | 불안장애 (Anxiety Disorder) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L2 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

본 Evidence Pack에 공식 MOA 데이터가 포함되지 않았으나, Agomelatine의 약리 기전은 다수의 문헌을 통해 잘 규명되어 있습니다. Agomelatine은 MT1/MT2 멜라토닌 수용체 작용제이자 5-HT2C 세로토닌 수용체 길항제로서, 기존 항우울제(SSRI/SNRI)와 전혀 다른 경로로 작동하는 최초의 멜라토닌 계열 항우울제입니다. 기존 단극성 우울증 치료에 사용된 이 기전이 불안장애에도 적용 가능한 이유는 세 가지 경로로 설명됩니다.

**첫째**, 5-HT2C 수용체 길항 작용은 편도체의 과활성화를 억제하여 직접적인 항불안 효과를 나타냅니다. **둘째**, MT1/MT2 수용체 작용으로 수면의 질이 개선되어 불안 증상을 간접적으로 완화합니다. **셋째**, 전전두엽에서의 노르에피네프린(NE) 및 도파민(DA) 분비 증가가 광범위 불안의 인지-정서 회로 과활성을 억제합니다.

MDD와 광범위 불안장애(GAD)는 공병률이 높고 신경생물학적 공통 기반을 공유하므로, Agomelatine의 이중 기전은 두 질환 모두에 이론적으로 적용 가능합니다. 실제로 유럽에서는 GAD를 대상으로 한 Phase 3 위약 대조 임상시험이 수행된 바 있으며(본 데이터셋 NCT 데이터베이스 미포함), 2025년 발표된 네트워크 메타분석(PMID 38804215)은 GAD 성인 환자에서 Agomelatine이 다수의 승인 약물 대비 우수한 효능과 내약성을 보였음을 확인하였습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

> **참고:** 유럽에서 수행된 GAD 대상 Phase 3 위약·활성 대조 임상시험(Stein et al., 2014; PMID 24569045 등)이 존재하나, 본 데이터셋의 NCT 데이터베이스에 포함되지 않았습니다. 이 점이 임상시험 건수 0건으로 나타나는 원인이며, 근거 수준 L2 판정의 근거가 됩니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [38804215](https://pubmed.ncbi.nlm.nih.gov/38804215/) | 2025 | Systematic Review + NMA | Int Clin Psychopharmacol | 성인 GAD에서 Agomelatine 대 승인 약물의 효능·내약성 비교 네트워크 메타분석; 관해율 및 이상반응으로 인한 중단율 분석 |
| [30712879](https://pubmed.ncbi.nlm.nih.gov/30712879/) | 2019 | Systematic Review + NMA | Lancet | GAD 약물치료 비교 시스템 고찰 및 네트워크 메타분석; 다수의 약물 선택지 간 비교 근거 제시 |
| [33343351](https://pubmed.ncbi.nlm.nih.gov/33343351/) | 2020 | Systematic Review + NMA | Front Pharmacol | GAD 이중맹검 RCT 네트워크 메타분석: HAM-A ≤7 관해율 및 내약성 비교 |
| [33537871](https://pubmed.ncbi.nlm.nih.gov/33537871/) | 2021 | Meta-analysis | Adv Ther | 위약 대조 3개 연구 통합 데이터셋: Agomelatine 25-50mg의 GAD 불안 증상 및 기능 장애 유의미한 개선 확인 |
| [35795687](https://pubmed.ncbi.nlm.nih.gov/35795687/) | 2022 | Review | Ther Adv Psychopharmacol | GAD 치료에서 Agomelatine의 독특한 작용 기전(5-HT2C 길항 + MT 촉효) 및 임상 적용 고찰 |
| [34417992](https://pubmed.ncbi.nlm.nih.gov/34417992/) | 2021 | Review | Adv Ther | GAD 근거 기반 약물치료 고찰; SSRI/SNRI 대안으로서 Agomelatine의 역할 및 네트워크 메타분석 지지 근거 |
| [32702221](https://pubmed.ncbi.nlm.nih.gov/32702221/) | 2020 | Meta-analysis | Clin Psychopharmacol Neurosci | GAD에서 Agomelatine의 효능 및 안전성 메타분석; 기존 약물 대비 우수한 치료 옵션 가능성 제시 |
| [24569045](https://pubmed.ncbi.nlm.nih.gov/24569045/) | 2014 | RCT | J Clin Psychiatry | GAD에서 Agomelatine의 단기 위약 대조 및 활성 대조 임상 연구; 규제 기관 요구 추가 시험 |
| [28730851](https://pubmed.ncbi.nlm.nih.gov/28730851/) | 2017 | Review | Expert Opin Pharmacother | GAD 단기·유지 치료에서 Agomelatine의 임상 효능 및 내약성 평가; 1차 치료 한계 극복 가능성 |
| [25999720](https://pubmed.ncbi.nlm.nih.gov/25999720/) | 2015 | Review | Neuropsychiatr Dis Treat | 기존 GAD 약물에 반응하지 않는 환자를 위한 Agomelatine의 임상 프로파일 및 부작용 고찰 |

---

## 한국 시판 정보

현재 Agomelatine은 한국에서 시판 허가를 받지 않았습니다 (허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
GAD에 대한 Agomelatine의 효능을 지지하는 다수의 시스템 고찰, 네트워크 메타분석 및 Phase 3 임상 데이터가 존재하며, 5-HT2C 길항 및 MT1/MT2 작용의 이중 기전은 불안장애의 핵심 병리 기전(편도체 과활성, 수면 장애, 인지-정서 회로 이상)과 합리적으로 연결됩니다.

**진행하려면 필요한 것:**
- TFDA 仿單(약품 설명서) PDF 다운로드 및 파싱을 통한 경고·금기 사항 확인 (**블로킹 데이터 갭 해소 필수**)
- DrugBank API 조회를 통한 공식 MOA 데이터 보완
- 유럽 Phase 3 GAD 임상시험 원문 확보 및 시험 설계·결과 상세 검토
- 한국 시판 가능성 검토를 위한 규제 전략 수립 및 품목 허가 신청 가능성 평가
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

