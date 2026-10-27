---
layout: default
title: Rozanolixizumab
parent: 모델 예측만 (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Rozanolixizumab: 예측 신규 적응증 기관지염 (Bronchitis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없음 (참고: 해외에서는 항아세틸콜린 수용체 또는 항M…"
monitor_inn: "Rozanolixizumab"
predicted_indications: ["bronchitis", "plasma cell myeloma", "indolent plasma cell myeloma", "hemoglobinopathy", "gastric carcinoma", "partial deletion of the short arm of chromosome 16", "diffuse gastric adenocarcinoma", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyruvate kinase deficiency of red cells"]
---

# Rozanolixizumab
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

## Rozanolixizumab: 중증 근무력증 계열 적응증에서 기관지염으로
{: .text-alpha }

## 한 문장 요약

Rozanolixizumab은 신생아 Fc 수용체(FcRn)를 차단하는 인간화 IgG4 단클론항체로, 한국에서 리스티고주라는 제품명으로 허가되어 시판 중입니다. TxGNN 모델은 **기관지염(bronchitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건**, **문헌도 0편**입니다. 따라서 모델 예측만 있는 단계(L5)이며, 현 시점에서는 보류를 권장합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 문서 링크로만 제공되어 구체적인 내용을 확인할 수 없음 (참고: 해외에서는 항아세틸콜린 수용체 또는 항MuSK 항체 양성 전신 중증 근무력증에 승인됨) |
| 예측 신규 적응증 | 기관지염 (Bronchitis) |
| TxGNN 예측 점수 | 95.28% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 데이터베이스에 등록되어 있지 않습니다. 다만 약물 계열에 대한 일반 지식에 따르면, Rozanolixizumab은 FcRn을 차단하여 IgG의 재활용을 막고 혈중 IgG 농도를 낮추는 항체입니다. 이 때문에 병원성 IgG가 원인인 자가면역 질환에 쓰입니다.

기관지염은 대부분 바이러스성 또는 감염성이며 IgG가 병태의 중심이 아닙니다. 따라서 기존 적응증과 기관지염 사이에서 기전상 타당한 연결 고리는 확인되지 않았습니다. 오히려 IgG 감소는 감염 위험을 높일 수 있습니다. 높은 TxGNN 점수는 지식 그래프에 기반한 계산상의 예측일 뿐이며, 실제 근거로 해석해서는 안 됩니다.

참고로 이 약에 대해 예측된 다른 후보(형질세포 골수종, 위암, 지중해빈혈 등)도 모두 근거 수준이 L5이며 임상시험과 문헌이 없습니다. 이들 역시 기전상 연결이 약하거나 추측에 그칩니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202500983 | 리스티고주(로자놀릭시주맙) | 주사제 (투명 유리 바이알, 무색~옅은 갈색-노란색 투명 또는 약한 유백색 용액) | 허가 적응증 문서 링크로만 제공됨 (허가사항 참조) |

## 안전성 고려사항

- **약물 상호작용**: 약리학 데이터상 표적은 IgG 수용체 및 수송체인 FcRn(유전자명 FCGRT)입니다. 개별 약물 간 상호작용 항목은 확인되지 않았습니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
기관지염에 대한 임상시험과 문헌이 전혀 없고 기전상 연결도 확인되지 않아 근거는 모델 예측뿐입니다. IgG 감소에 따른 감염 위험 증가 가능성을 고려하면 위험 대비 이점도 불리해 보입니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)을 식약처 문서에서 내려받아 확인
- DrugBank 등에서 상세 작용 기전 데이터 확보
- 기관지염과 FcRn 억제 사이의 기전적 연결을 뒷받침하는 전임상 또는 관찰 연구 근거
- 감염 위험에 대한 안전성 평가
- 투여 경로 적합성 평가 (현재 미확인)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

