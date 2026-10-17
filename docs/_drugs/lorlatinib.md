---
layout: default
title: Lorlatinib
parent: 모델 예측만 (L5)
nav_order: 484
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lorlatinib: 예측 신규 적응증 치은 섬유종증 (fibromatosis, gingival) (근거 수준 L5). 기존 적응증: ALK 양성 비소세포폐암 (허가 문서 링크만 제공되어 상세 문구는 확인되지 않음)"
monitor_inn: "LORLATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Lorlatinib
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

# Lorlatinib: ALK 양성 비소세포폐암에서 치은 섬유종증으로

## 한 문장 요약

Lorlatinib은 ALK/ROS1 티로신 키나제 억제제로, 한국에서 ALK 양성 비소세포폐암 치료에 허가되어 사용되고 있습니다.
TxGNN 모델은 **치은 섬유종증(fibromatosis, gingival)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.
따라서 이 예측은 모델 예측 단계(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ALK 양성 비소세포폐암 (허가 문서 링크만 제공되어 상세 문구는 확인되지 않음) |
| 예측 신규 적응증 | 치은 섬유종증 (fibromatosis, gingival) |
| TxGNN 예측 점수 | 99.81% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Lorlatinib은 뇌 투과성이 있는 3세대 ALK/ROS1 티로신 키나제 억제제이며, ALK 양성 비소세포폐암에서 효능이 입증되어 있습니다.

그러나 치은 섬유종증은 ALK나 ROS1 신호 전달에 의해 유발되는 질환으로 알려져 있지 않습니다. 기존 적응증과 신규 적응증 사이에서 확인된 기전적 연결고리는 없습니다. 높은 TxGNN 점수(99.81%)는 지식 그래프에서 나온 모델 예측일 뿐이며, 이를 뒷받침하는 임상시험이나 문헌이 없습니다.

참고로 같은 예측 목록의 다른 후보들도 대부분 같은 한계를 보입니다. 폐 관련 후보(폐문부 암종 등)는 승인된 폐암 적응증의 연장선에 가깝고, 신경모세포종 등은 다른 ALK 의존 종양에 대한 간접 근거만 있습니다. 이들은 엄밀한 의미의 재창출로 보기 어렵습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202105597 | 로비큐아정100밀리그램(롤라티닙) | 어두운 분홍색의 타원형 필름코팅정 | 허가사항 문서 참조 |
| 202105596 | 로비큐아정25밀리그램(롤라티닙) | 밝은 분홍색의 원형 필름코팅정 | 허가사항 문서 참조 |

두 제품 모두 한국화이자제약(주)가 허가를 보유하고 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 총 100건의 상호작용이 확인되었습니다(DDInter 기준). 이 중 상위 20건의 주요 항목은 다음과 같습니다.
  - **Major**: Dexamethasone, Clarithromycin
  - **Moderate**: Hydrocortisone, Betamethasone, Triamcinolone, Bupropion, Aprepitant, Morphine, Cimetidine, Alosetron, Chlorpropamide, Glimepiride, Dapagliflozin, Empagliflozin, Saxagliptin, Linagliptin, Dronabinol, Eliglustat, Naldemedine, Naloxegol
- 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
치은 섬유종증에 대한 임상시험과 문헌이 전혀 없고, ALK/ROS1 억제와의 기전적 연결고리도 확인되지 않았습니다. 높은 모델 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확인
- 작용 기전(MOA) 상세 데이터 보완
- 치은 섬유종증의 병태생리와 ALK/ROS1 경로의 연관성에 대한 전임상 근거
- 이 질환에 대한 문헌 및 임상시험 재검색
- 더 근거가 있는 후보(예: ALK 의존 종양) 우선 검토 고려
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

