---
layout: default
title: Mitomycin
parent: 모델 예측만 (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Mitomycin: 예측 신규 적응증 췌장 고형 가성유두암 (solid pseudopapillary carcinoma of pancreas) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 아닌 허가사항 문서 링크만 연결되어 있어 구체적 적응증 텍스트는 확인되지 않음"
monitor_inn: "mitomycin"
predicted_indications: ["solid pseudopapillary carcinoma of pancreas", "osteoclastic giant cell tumor of pancreas", "pancreatic carcinoma with mixed differentiation", "pancreatic intraductal papillary-mucinous carcinoma", "mixed ductal-endocrine carcinoma of pancreas", "pancreatic signet ring cell adenocarcinoma", "undifferentiated pancreatic carcinoma", "malignant exocrine pancreas neoplasm", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
---

# Mitomycin
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

## Mitomycin: 허가 적응증에서 췌장 고형 가성유두암으로
{: .text-alpha }

## 한 문장 요약

Mitomycin은 DNA 교차결합을 일으키는 세포독성 항종양제로, 한국에서 주사제(동결건조 분말)로 허가되어 시판 중입니다.
TxGNN 모델은 **췌장 고형 가성유두암(solid pseudopapillary carcinoma of pancreas)**에 효과가 있을 수 있다고 예측하지만(0.9986), 이 질환을 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측 수준에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 아닌 허가사항 문서 링크만 연결되어 있어 구체적 적응증 텍스트는 확인되지 않음 |
| 예측 신규 적응증 | 췌장 고형 가성유두암 (solid pseudopapillary carcinoma of pancreas) |
| TxGNN 예측 점수 | 0.9986 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 mitomycin은 DNA를 교차결합시키는 알킬화 계열의 세포독성 항종양제이며, 위암·췌장 선암 등 소화기 종양에서 사용된 이력이 있어 췌장 상피성 종양에도 기전상 적용 가능할 수 있습니다.

다만 고형 가성유두암은 드문 췌장 종양이며, 일반적인 세포독성 활성에 근거한 가설일 뿐입니다. 이 질환에 대한 임상시험이나 문헌이 없어 TxGNN의 매우 높은 점수도 모델 예측으로만 해석해야 합니다.

같은 췌장 계열의 다른 예측 질환 중에는 간접 근거가 있는 경우가 있습니다(아래 참고).

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

예측 1순위 질환(고형 가성유두암)에 대한 문헌은 없습니다. 참고로 같은 췌장 종양군의 다른 예측 질환에 연결된 문헌은 다음과 같으며, 모두 mitomycin의 효능을 직접 입증하지는 않는 간접 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Review | Strahlenther Onkol | 췌관성 췌장암의 보조·신보조 방사선화학요법 고찰 (췌장암 화학요법 관련, mitomycin 효능 입증은 아님) |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | 임상 연구 | Nihon Geka Gakkai Zasshi | 절제된 췌장암에서 면역화학요법(tegafur, mitomycin 등)에 tamoxifen 추가 시도 (tamoxifen 연구로, mitomycin 단독 근거 아님) |
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Case report | Pancreatology | 췌장 IPMN을 동반한 복막가성점액종을 복강 내 온열 화학관류로 관리한 증례 |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Review | Bull Cancer | 원발부위 불명암의 진단과 치료 개관 (췌장암·mitomycin에 특이적이지 않음) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199201621 | 한국유나이티드미토마이신씨주(수출용) | 동결건조 결정/분말 바이알(주사제) | 허가사항 문서 참조 |
| 199701737 | 한국유나이티드미토마이신씨주10밀리그람(수출용) | 동결건조 결정/분말 바이알(주사제) | 허가사항 문서 참조 |

두 제품 모두 수출용 제품(수출명: MITONCO for Inj., Mitocin for Inj.)이며, 제조사는 한국유나이티드제약(주)입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화/DNA 교차결합 계열) |
| 골수억제 위험 | 고 (지연성·누적성 골수억제가 알려져 있으며, 지식그래프상 혈소판감소증, 백혈구감소증, 빈혈이 금기 관련 질환으로 연결됨) |
| 구토 유발성 등급 | 중 |
| 모니터링 항목 | CBC(분류 포함), 혈소판, 신기능, 간기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

골수억제·구토 등급은 약물 계열의 일반 지식에 따른 것이며, 자세한 내용은 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

- **금기 관련 질환(지식그래프 기반, 허가사항 문구 아님)**: 신장 질환, 혈소판감소증, 혈액응고 질환, 빈혈, 대적혈구성 빈혈, 백혈구감소증, 용혈성 요독 증후군, 울혈성 심부전, 심부전, 구내염, 요관 농증
- **약물 상호작용**: 총 193건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - Major: Deferiprone, Samarium (153Sm) lexidronam
  - Moderate: Palifermin, Strontium chloride Sr-89, Fostamatinib
  - Minor: Levofloxacin
  - 그 외 다수(Warfarin, Dexamethasone, Prednisone, Ondansetron 등)는 등급 미분류

허가사항상의 경고·금기는 확인되지 않았으므로 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고형 가성유두암에 대한 임상시험과 문헌이 없고 TxGNN 예측 점수만 있는 L5 수준입니다. 상위 10개 예측 질환 모두 Hold이며, 일부에 연결된 문헌도 mitomycin 효능을 직접 입증하지 못하는 간접 근거입니다.

**진행하려면 필요한 것:**
- 허가사항 문서(경고·금기·적응증)의 확보 및 분석
- 상세한 작용 기전(MOA) 데이터 확보
- 췌장 고형 가성유두암에서 mitomycin의 효능을 다룬 전임상·임상 근거 탐색
- 상기 근거가 확보된 뒤 골수억제 및 약물 상호작용을 포함한 안전성 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

