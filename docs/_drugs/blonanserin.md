---
layout: default
title: Blonanserin
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 9
---

# Blonanserin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Blonanserin: 조현병에서 망막 이영양증으로

## 한 문장 요약

Blonanserin은 도파민 D2 및 세로토닌 5-HT2A 수용체 길항제로 작용하는 비정형 항정신병 약물로, 조현병 치료에 사용됩니다.
TxGNN 모델은 **망막 이영양증(Retinal Dystrophy with or without Extraocular Anomalies)**에 효과가 있을 수 있다고 예측하며(예측 점수 99.98%),
현재 관련 임상시험 등록은 없고 검색된 **15편의 문헌** 모두 직접적인 근거를 제공하지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 조현병 (일본·한국 허가; 현 데이터베이스 미수록) |
| 예측 신규 적응증 | 망막 이영양증, 외안부 이상 동반 가능 (Retinal Dystrophy with/without Extraocular Anomalies) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 데이터베이스에 수록되어 있지 않습니다. 알려진 정보에 따르면, Blonanserin은 도파민 D2 수용체 및 세로토닌 5-HT2A 수용체의 길항제로 작용하는 비정형 항정신병 약물로, 일본 및 한국에서 조현병 치료에 사용되어 왔습니다.

망막의 무장돌기세포(amacrine cells)에는 D2 수용체가 발현되어 있으며, 이 수용체는 시봉세포(간상세포)와 추세포(원추세포)의 광적응 조절에 관여합니다. 이에 따라 D2 수용체 길항 작용이 망막 도파민 신호 전달에 이론적으로 영향을 미칠 수 있다는 연관성이 제기됩니다.

그러나 Blonanserin의 D2 길항 작용은 도파민 의존성 망막 보호 신호를 억제하는 방향으로 작용할 가능성이 높아, **기전 방향성 자체에 의문**이 있습니다. 유전성 망막 이영양증은 구조적·유전적 원인(예: RPGR, PRPF 유전자군 변이)에 의한 진행성 질환으로, 도파민 신호 조절만으로는 근본적 치료가 어렵습니다. 현재 이 예측을 지지하는 직접적인 전임상 또는 임상 증거는 확인되지 않으며, TxGNN 고점수는 지식 그래프 내 망막 질환 노드의 네트워크 위상(topology) 특성에 기인할 가능성이 높습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

검색된 15편의 문헌은 외안부 이상, 안구 운동 장애, 선천성 안과 기형 등 안과 일반 주제를 다루며, **Blonanserin의 망막 이영양증 치료 효능을 직접 보고한 연구는 포함되어 있지 않습니다.** 관련도가 높은 순으로 10편을 나열합니다.

| PMID | 연도 | 유형 | 저널 | 주요 내용 |
|------|------|------|------|---------|
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Original | Int J Mol Sci | 선천성 외안근 섬유화(CFEOM)에서 KIF21A·TUBB3 변이와 동반되는 시신경 두부 및 망막 이상 분석 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Case Series/Review | Doc Ophthalmol | Wagner-Stickler 유리체망막 변성: 근시·백내장·망막박리·감각신경성 난청 동반 스펙트럼 |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Original | Am J Ophthalmol | 시신경 공동형 이상에 동반되는 황반병증의 통합 병인론 및 영구적 치료법 제안 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | 소아 안와 병변의 영상 감별진단 (선천성·발달성 병변, 코츠병, 망막아세포종 포함) |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | 선천성 수정체 형태 이상의 종류, 발생 기전 및 전안부 이상과의 연관성 |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | 선천성 두개신경 이중신경지배 장애(CCDD) 분류, 진단 및 비선천성 형태와의 감별 |
| [37408430](https://pubmed.ncbi.nlm.nih.gov/37408430/) | 2023 | Review | Chin J Ophthalmol | 외안근의 구조·신경지배 및 근육 도르래(pulley) 이상과 사시의 연관성 최신 동향 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | 선천성 안검하수의 분류(단순형 vs. 복합형), 진단 기준 및 치료 원칙 |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | 안와 감염의 원인·임상 단계 분류 (부비동염 기원, 당뇨·면역저하 관련) |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Clinical Pearls | Semin Neurol | 복시의 체계적 병력 청취 및 신체 검진을 통한 감별진단 접근법 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험 등록이 전무하고, 검색된 문헌 중 Blonanserin과 망막 이영양증 간의 직접적 관련성을 다루는 연구가 없어 근거 수준이 L5(모델 예측만 존재)에 그치며, D2 길항 기전의 방향성 또한 치료 목적과 부합하지 않아 현시점에서 개발 추진을 지지하는 근거가 불충분합니다.

**진행하려면 필요한 것:**
- Blonanserin 상세 작용 기전(MOA) 데이터 확보 (DrugBank API 조회 필요)
- 한국 식약처(MFDS) 허가사항 내 경고·금기 데이터 확보 (허가사항 PDF 파싱)
- 망막 무장돌기세포에서의 D2 수용체 길항 효과에 관한 전임상 문헌 탐색
- TxGNN 고점수 원인 심층 분석 (지식 그래프 위상 효과 vs. 실제 생물학적 근거 구분)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

