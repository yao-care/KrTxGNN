---
layout: default
title: Efinaconazole
parent: 모델 예측만 (L5)
nav_order: 300
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Efinaconazole: 예측 신규 적응증 침샘 대세포암종 (salivary gland large cell carcinoma) (근거 수준 L5). 기존 적응증: 조갑진균증 (허가 적응증 원문은 허가증 PDF 링크로만 제공되어, 약물 분류와 제형을 근거로 기재)"
monitor_inn: "Efinaconazole"
predicted_indications: ["salivary gland large cell carcinoma", "salivary gland small cell carcinoma", "sarcomatoid carcinoma", "sarcomatoid mesothelioma", "sex hormone-producing adrenal cortex adenoma", "signet ring cell gastric adenocarcinoma", "sinonasal undifferentiated carcinoma", "sinus histiocytosis with massive lymphadenopathy", "skin sarcoma", "small intestinal Burkitt lymphoma"]
---

# Efinaconazole
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

## Efinaconazole: 조갑진균증에서 침샘 대세포암종으로
{: .text-alpha }

## 한 문장 요약

Efinaconazole은 외용 트리아졸계 항진균제로, 원래 조갑진균증(손발톱 진균 감염) 치료에 사용되었습니다.
TxGNN 모델은 **침샘 대세포암종(salivary gland large cell carcinoma)**에 효과가 있을 수 있다고 예측하지만, 점수가 50%로 변별력이 없고 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 조갑진균증 (허가 적응증 원문은 허가증 PDF 링크로만 제공되어, 약물 분류와 제형을 근거로 기재) |
| 예측 신규 적응증 | 침샘 대세포암종 (salivary gland large cell carcinoma) |
| TxGNN 예측 점수 | 50.0% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 16건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Efinaconazole은 진균의 라노스테롤 14-알파-디메틸라제(CYP51)를 억제하는 외용 트리아졸계 항진균제입니다. 다만 현재 상세한 작용 기전 데이터는 수집되지 않았으며, 위 내용은 약물 분류에 근거한 일반적 설명입니다.

침샘 대세포암종과의 기전적 연관성은 현재 데이터로 뒷받침되지 않습니다. 유일한 신호는 변별력이 없는 TxGNN 점수 0.5뿐입니다. 또한 외용제로 전신 노출이 매우 낮아, 전신 질환인 악성 종양에 적용하기에는 타당성이 더욱 낮습니다.

참고로 같은 후보군의 다른 예측(침샘 소세포암종, 육종양 암종, 육종양 중피종, 성호르몬 분비 부신피질 선종, 반지세포 위선암, 부비동 미분화암, 로사이-도르프만병, 피부 육종, 소장 버킷 림프종)도 모두 점수 0.5, 근거 수준 L5, 권장 결정 Hold입니다. 일부 아졸계 약물(예: ketoconazole)은 인체 스테로이드 합성 CYP를 억제해 부신 병변에 이론적 근거가 있지만, efinaconazole은 진균 CYP51에 선택적이고 전신 흡수가 낮아 이는 추측에 불과합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201702389 | 주블리아외용액 (동아에스티) | 외용액 (무색~미황색 투명한 액) | 허가증 참조 |
| 202401664 | 뉴블라외용액 (한국유니온제약) | 외용액 (무색~연한 노란색 투명한 액) | 허가증 참조 |
| 202401944 | 파마에피나코나졸외용액 (한국파마) | 외용액 (무색~미황색 투명한 액) | 허가증 참조 |
| 202401007 | 에피러쉬외용액 (휴온스) | 외용액 (무색~연한 노란색 투명한 액제) | 허가증 참조 |
| 202400367 | 주플리에외용액 (대웅제약) | 외용액 (무색~미황색 투명한 액제) | 허가증 참조 |

전체 16건의 허가가 모두 단일제이며 유효 상태입니다. 위는 주요 5건만 나열했습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수 0.5는 변별력이 없고, 임상시험과 문헌이 전혀 없으며, 기전적 연결고리도 확인되지 않았습니다. 외용제로서 전신 노출이 낮아 악성 종양 치료에 적용하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가증 PDF에서 허가 적응증과 경고·금기 정보 확보 (현재 안전성 검토를 진행할 수 없음)
- 상세한 작용 기전(MOA) 데이터 확보 (DrugBank 조회)
- 침샘 대세포암종과의 기전적 연관성을 보여주는 전임상 근거
- 투여 경로 적합성 평가 (외용제의 전신 질환 적용 가능성)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

