---
layout: default
title: Crizotinib
parent: 모델 예측만 (L5)
nav_order: 236
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Crizotinib: 예측 신규 적응증 치은 섬유종증 (fibromatosis, gingival) (근거 수준 L5). 기존 적응증: 한국 허가증에는 적응증 본문 대신 허가사항 문서 링크만 확인됩니다. 문헌상 ALK 양성 비소세포폐암(NSCLC)에 사용됩니다"
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
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

## Crizotinib: 비소세포폐암에서 치은 섬유종증으로
{: .text-alpha }

## 한 문장 요약

Crizotinib은 ALK/ROS1/MET 표적 티로신 키나제 억제제로, 한국에서 잴코리캡슐이라는 이름으로 시판되고 있습니다.
TxGNN 모델은 **치은 섬유종증(fibromatosis, gingival)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
이 예측은 모델 점수에만 근거하므로 현재로서는 보류가 적절합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가증에는 적응증 본문 대신 허가사항 문서 링크만 확인됩니다. 문헌상 ALK 양성 비소세포폐암(NSCLC)에 사용됩니다. |
| 예측 신규 적응증 | 치은 섬유종증 (fibromatosis, gingival) |
| TxGNN 예측 점수 | 99.81% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 2건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Crizotinib은 ALK, ROS1, MET 수용체 티로신 키나제를 억제하는 약물이며, ALK 또는 ROS1 변이가 있는 비소세포폐암에서 효능이 확인되어 있습니다.

그러나 치은 섬유종증과 ALK/ROS1/MET 억제 사이에 타당한 기전적 연결고리는 현재 데이터로 확인되지 않습니다. 예측 점수는 높지만(99.81%) 뒷받침하는 임상시험이나 문헌이 없어, 기전상 적용 가능하다고 판단하기 어렵습니다.

참고로 다른 예측 질환 중에는 근거가 더 있는 것도 있습니다. 다만 다음과 같은 한계가 있습니다.
- **폐 양성 신생물(lung benign neoplasm)**: ALK 양성 NSCLC의 3상 RCT 문헌이 많지만, 이는 이미 허가된 적응증의 근거입니다. 질환 분류 체계의 매핑 결과일 뿐 새로운 적응증의 신호는 아닙니다.
- **폐 생식세포종양(lung germ cell tumor)**: 종양 종류를 가리지 않는 바스켓 임상시험 2건이 연결되지만, 이 조직형에 대한 직접 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201112195 | 잴코리캡슐250밀리그램(크리조티닙) | 경질캡슐 (상하부 분홍색) | 허가사항 문서 참조 |
| 201112194 | 잴코리캡슐200밀리그램(크리조티닙) | 경질캡슐 (상부 분홍색, 하부 흰색) | 허가사항 문서 참조 |

두 제품 모두 한국화이자제약(주)이 제조·판매하는 단일제입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (ALK/ROS1/MET 티로신 키나제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 간기능, 심전도(QT 간격, 서맥) 등. 허가사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건의 상호작용이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Clarithromycin, Cisapride, Dolasetron, Eliglustat, Granisetron
  - **Moderate**: Famotidine, Metformin, Loperamide, Bupropion, Aprepitant, Dexamethasone, Bisacodyl, Budesonide 등
- **문헌에서 확인된 안전성 신호**: 치명적 급성 간부전 사례, 서맥·QT 연장·심실세동·심낭염 등의 심장독성 사례가 보고되어 있습니다. 이 때문에 간기능과 심전도 모니터링이 필요합니다.

경고 및 금기 등 허가사항 기반 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
치은 섬유종증에 대해서는 TxGNN 예측 점수만 있고 임상시험이나 문헌이 없으며, 기전적 연결고리도 확인되지 않습니다. 또한 한국 허가 문서의 경고·금기 정보가 확보되지 않아 안전성 검토도 진행할 수 없는 상태입니다.

**진행하려면 필요한 것:**
- 한국 허가사항(MFDS 첨부문서)의 경고·금기 정보 확보 (안전성 검토의 필수 선행 조건)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 치은 섬유종증과 ALK/ROS1/MET 경로의 연관성을 보여주는 전임상 또는 기전 연구 근거
- 간독성·심장독성 위험을 고려한 위험-편익 평가 (섬유종증은 양성 질환이므로 특히 중요)
- 예측 순위 2위 이하의 후보는 대부분 근거 수준이 L5이거나 기존 적응증과 중복되므로, 우선순위 재검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

