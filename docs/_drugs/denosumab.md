---
layout: default
title: Denosumab
parent: 모델 예측만 (L5)
nav_order: 260
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Denosumab: 예측 신규 적응증 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) (근거 수준 L5). 기존 적응증: 허가 적응증 원문 확인 불가 (허가증에 링크만 제공됨)"
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Denosumab: 골다공증 등 뼈 질환에서 중증 비증식성 당뇨망막병증으로
{: .text-alpha }

## 한 문장 요약

Denosumab은 한국에서 10건의 허가증으로 시판 중인 RANKL 중화 단클론항체 주사제입니다. 다만 허가 적응증 원문은 데이터에 링크로만 제공되어 구체적인 적응증은 확인하지 못했습니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 지지하는 **임상시험은 0건, 문헌은 0편**입니다. 같은 질환군인 당뇨망막병증에서도 간접 문헌 2편만 확인되어 가설 수준의 예측입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문 확인 불가 (허가증에 링크만 제공됨) |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 0.9963 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 10건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Denosumab은 RANKL(RANK 리간드)을 중화하는 단클론항체입니다. RANKL은 파골세포의 형성과 활성에 관여하므로, 뼈 흡수를 억제하는 약물로 사용됩니다.

신규 적응증과의 연관성은 가설 단계입니다. RANKL/RANK/OPG 신호가 당뇨병 환자의 혈관 석회화, 염증, 미세혈관 기능 이상에 영향을 줄 가능성이 제기될 수 있습니다. 그러나 RANKL 억제가 망막 신생혈관, 혈관 누출, 망막병증 진행에 영향을 준다는 직접적인 증거는 없습니다. 기존 적응증과 신규 적응증 사이의 기전적 유사성 평가도 아직 이루어지지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

중증 비증식성 당뇨망막병증에 대한 직접 문헌은 없습니다. 아래는 상위 질환군인 **당뇨망막병증**(예측 순위 2위)에서 검색된 간접 문헌입니다. 두 연구 모두 망막병증에 대한 Denosumab의 효과를 직접 검증하지 않았습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | 코호트 연구 (관찰연구) | Diabetes Obes Metab | 골다공증 환자에서 Denosumab이 비스포스포네이트 대비 제2형 당뇨병 발생, 족부 궤양 위험, 전체 사망률을 낮추는 것으로 보고됨. 제목이 잘려 있어 망막병증 결과는 확인 불가 |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | 관찰/코호트 연구 | Cureus | 제2형 당뇨병 성인의 FRAX 골절 위험 평가 도구 사용 평가. 망막병증 결과와 무관 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202500817 | 오보덴스프리필드시린지 (삼성바이오에피스) | 프리필드시린지 주사제 | 허가 적응증 원문 확인 불가 |
| 202600308 | 이잠비아프리필드시린지 (에이치케이이노엔) | 프리필드시린지 주사제 | 허가 적응증 원문 확인 불가 |
| 202402753 | 스토보클로프리필드시린지 (셀트리온) | 프리필드시린지 주사제 | 허가 적응증 원문 확인 불가 |
| 201404453 | 엑스지바주 (암젠코리아) | 바이알 주사제 | 허가 적응증 원문 확인 불가 |
| 201404452 | 프롤리아프리필드시린지 (암젠코리아) | 프리필드시린지 주사제 | 허가 적응증 원문 확인 불가 |

이 밖에 5건의 허가(오센벨트주, 엑스브릭주, 메디팁데노수맙프리필드시린지, 덴브레이스주, 엑스지바프리필드시린지)가 유효하며, 총 10건 모두 단일제입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었으며, 확인된 주요 항목은 모두 중등도(Moderate) 수준입니다.
  - 코르티코스테로이드: Hydrocortisone, Prednisone, Prednisolone, Methylprednisolone, Dexamethasone, Betamethasone, Budesonide, Triamcinolone
  - 면역억제·면역조절 약물: Tacrolimus, Dupilumab, Mercaptopurine
  - 방사성의약품·기타: Ibritumomab tiuxetan, Tositumomab, Iobenguane (I-131), Levamisole, Trimetrexate
  - 부신피질자극호르몬 계열: Corticotropin, Tetracosactide

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만(0.9963), 중증 비증식성 당뇨망막병증을 직접 지지하는 임상시험과 문헌이 없어 근거 수준이 L5에 머뭅니다. 작용 기전 데이터와 허가 적응증 원문도 확보되지 않아 가설 생성 단계로 판단합니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 확인 (허가사항 PDF 확인)
- 작용 기전(MOA) 데이터 보충 (DrugBank 조회)
- RANKL 억제와 망막 신생혈관·혈관 누출·망막병증 진행 사이의 전임상 기전 근거
- 당뇨망막병증 결과를 직접 평가하는 관찰연구 또는 임상시험
- 주사제(전신 투여)의 망막 질환 적용 타당성 및 투여 경로 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

