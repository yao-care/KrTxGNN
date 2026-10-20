---
layout: default
title: Gefitinib
parent: 모델 예측만 (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Gefitinib: 예측 신규 적응증 치은 섬유종증 (Fibromatosis, gingival) (근거 수준 L5). 기존 적응증: 허가증에 적응증 텍스트가 아닌 허가사항 문서 링크만 수록되어 있어 이 보고서에서 확인하지 못했습니다. 문헌상 gefitini…"
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
---

# Gefitinib
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

# Gefitinib: 비소세포폐암에서 치은 섬유종증으로

## 한 문장 요약

Gefitinib은 EGFR 티로신 키나제 억제제로, 한국에서 EGFR 변이 양성 비소세포폐암 치료에 사용되는 약물입니다. TxGNN 모델은 **치은 섬유종증(Fibromatosis, gingival)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험과 문헌은 현재 0건**입니다. 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 텍스트가 아닌 허가사항 문서 링크만 수록되어 있어 이 보고서에서 확인하지 못했습니다. 문헌상 gefitinib은 EGFR 변이 양성 비소세포폐암에 사용됩니다. |
| 예측 신규 적응증 | 치은 섬유종증 (Fibromatosis, gingival) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 6건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 이 보고서에 수록되어 있지 않습니다. 다만 수집된 문헌에 따르면 gefitinib은 EGFR 티로신 키나제를 선택적으로 억제하여 세포 증식, 생존, 혈관신생에 관여하는 신호전달을 차단하는 약물입니다.

치은 섬유종증(유전성 치은 섬유종증)과 EGFR 억제 사이에 확립된 기전적 연관성은 확인되지 않았습니다. 이번 예측은 지식 그래프상의 근접성에서 비롯된 모델 예측으로 보이며, 임상시험이나 문헌의 뒷받침이 없습니다.

참고로 예측 순위 상위 10건 중 폐 관련 질환(폐 섬유종, 폐 과오종, 폐문부 암종 등)은 gefitinib의 폐암 적응증과의 그래프 근접성 때문일 가능성이 높습니다. 그중 폐문부 암종은 사례 보고 1건이 있으나 기존 비소세포폐암 적응증의 범위를 넘는 독립 적응증의 근거는 되지 못합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201502377 | 스펙사정250밀리그램(게피티니브) | 갈색의 원형 필름코팅정 | 허가사항 문서 참조 |
| 201503147 | 제피티닙정250밀리그램(게피티니브) | 갈색의 원형 필름코팅정제 | 허가사항 문서 참조 |
| 201502268 | 이레피논정(게피티니브) | 갈색의 원형 필름코팅정 | 허가사항 문서 참조 |
| 201503506 | 이레티닙정250밀리그램(게피티니브) | 갈색의 원형 필름코팅정 | 허가사항 문서 참조 |
| 200307971 | 이레사정(게피티니브) | 갈색의 원형 필름코팅정 | 허가사항 문서 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (EGFR 티로신 키나제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요. 문헌상 간질성 폐질환, 피부독성, QT 연장 관련 보고가 있어 호흡기·피부·심전도·간기능 관찰이 고려됩니다. |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **금기 관련 지식 그래프 신호**: 간 질환, 담낭 질환, 간질성 폐질환, 폐 섬유증, 염증 후 폐 섬유증이 약물-질환 금기 관계로 연결되어 있습니다. 이는 허가사항 문구가 아닌 지식 그래프 기반 정보입니다.
- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 위산 억제제(중등도): famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole
  - CYP 관련 가능성이 있는 약물(중등도): clarithromycin, aprepitant, dexamethasone, miconazole, clotrimazole, naltrexone, troglitazone
  - 등급 미상: calcitriol, glimepiride
- **신규 적응증 관련 우려**: 피부독성이 흔한 약물이므로, 피부 기저막 질환 등 피부 취약 질환에서는 특히 주의가 필요합니다.

그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
치은 섬유종증에 대해서는 TxGNN 점수(99.89%)만 있고 임상시험과 문헌이 전혀 없으며, EGFR 억제와의 기전적 연관성도 확립되지 않았습니다. 근거 수준은 L5로, 현재로서는 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- EGFR 신호전달과 치은 섬유종증 병태생리의 연관성에 대한 기전 연구 및 전임상 근거
- 허가사항(경고·금기·적응증)의 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 폐 섬유증·간질성 폐질환 등 지식 그래프상 금기 신호의 검토
- 폐암 관련 예측 질환(폐문부 암종, 폐구 신생물)은 기존 비소세포폐암 적응증과의 중복 여부 및 EGFR 변이 상태 기준을 별도로 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

