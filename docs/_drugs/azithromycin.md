---
layout: default
title: Azithromycin
parent: 모델 예측만 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Azithromycin: 예측 신규 적응증 고아밀라제혈증 (Hyperamylasemia) (근거 수준 L5). 기존 적응증: 확인 불가 (허가증 원문 링크만 제공됨)"
monitor_inn: "AZITHROMYCIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
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

## Azithromycin: 세균 감염에서 고아밀라제혈증으로
{: .text-alpha }

## 한 문장 요약

Azithromycin은 마크로라이드계 항생제로, 한국에서 단일제 3건이 허가되어 시판 중입니다(허가증 원문은 링크로만 제공되어 구체적 적응증 문구는 확인되지 않았습니다).
TxGNN 모델은 **고아밀라제혈증(hyperamylasemia)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 지지하는 **임상시험과 문헌은 0건**입니다.
고아밀라제혈증은 치료 대상 질환이라기보다 검사 소견이어서 재창출 후보로서의 타당성이 낮습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가증 원문 링크만 제공됨) |
| 예측 신규 적응증 | 고아밀라제혈증 (Hyperamylasemia) |
| TxGNN 예측 점수 | 99.81% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Azithromycin은 마크로라이드계 항생제로, 세균 감염 치료에 사용되는 약물입니다.

고아밀라제혈증은 혈중 아밀라제 수치가 높아진 검사 소견으로, 췌장염, 신부전, 침샘 질환 등 다양한 원인에서 나타납니다. 이 소견 자체를 표적으로 하는 항균 또는 면역조절 기전은 뚜렷하지 않으며, 이번 데이터에서도 두 질환을 연결할 기전적 근거는 확인되지 않았습니다. 따라서 이 예측은 지식 그래프 기반의 통계적 연관성에 그친 것으로 보입니다.

참고로 TxGNN 점수 순위 상위 10개 예측 중에서는 다음 항목이 상대적으로 근거가 있었습니다. 다만 이들도 직접적인 임상 근거는 아닙니다.
- **단클론 감마글로불린병증(monoclonal gammopathy)**: 마크로라이드가 골수종 세포에서 자가포식을 차단하고 bortezomib 감수성을 높인다는 전임상 연구(PMID 23546223)가 있습니다.
- **패혈성 흑사병(septicemic plague)**: *Yersinia pestis*에 대한 시험관 내 활성 연구가 있으나, 해당 연구에서는 azithromycin의 활성이 낮았다고 보고되었습니다(PMID 8540736).
- **선천성 혈액 질환(겸상적혈구병)**: 급성 흉부 증후군 예방 및 폐기능 개선 시험 2건이 있었으나 모두 등록 0명으로 철회되었습니다.

## 임상시험 근거

고아밀라제혈증에 대해 현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

고아밀라제혈증에 대해 현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200903777 | 비씨아지트로마이신정(수출용) | 흰색의 캡슐모양 필름코팅정제 | 허가증 원문 참조 |
| 200201923 | 아지토멕스캅셀(수출용) | 백색 분말 충진 캅셀제 | 허가증 원문 참조 |
| 200003314 | 지로신캅셀(수출용) | 백색 분말, 상하 적갈색 캅셀제 | 허가증 원문 참조 |

3건 모두 수출용 제품입니다.

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않아 허가사항을 참조해야 합니다. 아래는 약물 지식 그래프에서 확인된 금기 관련 질환과 약물 상호작용입니다.

- **지식 그래프상 금기 관련 질환** (허가 문구가 아닌 그래프 연관 정보): QT 연장 증후군(선천성 포함), 토르사드 드 푸앵트, 간 질환, 담낭 질환, *Clostridium difficile* 대장염, 신생아 괴사성 장염, 중증 근무력증(성인 발병형 포함), 신경근 접합부 질환, 청력 장애 및 청각계 질환
- **약물 상호작용** (조회된 총 100건 중 일부):
  - **Major**: Cisapride, Dolasetron (QT 연장 위험과 관련된 병용)
  - **Moderate**: Famotidine, Loperamide, Clarithromycin, Levofloxacin, Granisetron, 알루미늄·마그네슘 함유 제산제, 완하제(Bisacodyl, Lactulose 등)
  - **Minor**: Amoxicillin, Metronidazole

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고아밀라제혈증 예측은 모델 점수(99.81%)만 있고 임상시험과 문헌이 없으며(L5), 검사 소견이라는 질환 특성상 기전적 연결도 불분명합니다. 현 단계에서는 진행을 권장하지 않습니다.

**진행하려면 필요한 것:**
- 허가증 원문(MFDS 첨부문서)에서 적응증, 경고, 금기 정보 확보 (현재 안전성 검토 진행을 막는 차단 요소)
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 고아밀라제혈증과 azithromycin 사이의 생물학적 연결에 대한 가설 정립 및 문헌 검색
- 대안 검토: 근거가 상대적으로 있는 단클론 감마글로불린병증(전임상 근거, L4) 또는 겸상적혈구병의 폐 합병증(철회된 시험만 존재, L4)을 연구 질문 후보로 고려할 수 있으나, 이 역시 임상 근거는 없는 상태입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

