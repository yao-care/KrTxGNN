---
layout: default
title: Perphenazine
parent: 모델 예측만 (L5)
nav_order: 594
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Perphenazine: 예측 신규 적응증 망막 이영양증 (retinal dystrophy with or without extraocular anomalies) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가정보 PDF 링크로만 제공). 약물 분류는 페노티아진계 항정신병약"
monitor_inn: "PERPHENAZINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "syndromic myopia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "hydranencephaly (disease)", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "atypical glycine encephalopathy"]
---

# Perphenazine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Perphenazine: 페노티아진계 항정신병약에서 망막 이영양증 예측으로
{: .text-alpha }

## 한 문장 요약

Perphenazine은 페노티아진계 항정신병약으로, 한국에서 주사제와 정제 형태로 허가되어 시판 중입니다.
TxGNN 모델은 **망막 이영양증(retinal dystrophy with or without extraocular anomalies)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**입니다. 문헌 1편은 같은 계열 약물(thioridazine)의 **망막 독성** 사례 보고라서 치료 효과를 지지하지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가정보 PDF 링크로만 제공). 약물 분류는 페노티아진계 항정신병약 |
| 예측 신규 적응증 | 망막 이영양증 (retinal dystrophy with or without extraocular anomalies) |
| TxGNN 예측 점수 | 0.9996 |
| 근거 수준 | L5 (모델 예측만 있고 치료 효과를 지지하는 연구 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 perphenazine은 도파민 D2 수용체를 차단하는 페노티아진계 항정신병약입니다. 그러나 이 기전과 유전성 망막 이영양증을 연결할 수 있는 근거는 확인되지 않았습니다.

수집된 문헌에서 망막과 관련된 내용은 thioridazine(다른 페노티아진계 약물)에 의한 색소성 망막병증 사례뿐입니다. 이는 치료 효과가 아니라 **계열 약물의 망막 독성 신호**에 해당합니다. 따라서 높은 예측 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영했을 가능성이 있으며, 생물학적 근거를 의미하지는 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [14129300](https://pubmed.ncbi.nlm.nih.gov/14129300/) | 1964 | 증례 보고 | Am J Psychiatry | 하루 최대 1,400 mg의 thioridazine 투여와 관련된 색소성 망막병증 1례 (초록 없음, 제목 기준 요약). 치료 효과가 아닌 독성 보고 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199600631 | 페로친주(페르페나진염산염)(수출용) | 앰플 주사제 | 적응증 본문 미확인 ([허가정보 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199600631/EE) 참조) |
| 198500622 | 명인페르페나진정4밀리그램 | 정제 (분홍색, 원형) | 적응증 본문 미확인 ([허가정보 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198500622/EE) 참조) |

## 안전성 고려사항

- **지식그래프상 금기 질환**: 허가사항이 아니라 TxGNN 지식그래프(PrimeKG)의 약물-질환 금기 연결에서 가져온 정보이므로 참고용입니다. 주요 항목은 다음과 같습니다.
  - 심혈관계: QT 연장 증후군, torsades de pointes, 기립성 저혈압, 심근경색, 심정지
  - 신경계: 간질, 기저핵 질환, 근긴장이상, 안검경련
  - 혈액계: 호중구감소증, 무과립구증, 혈소판감소증, 빈혈
  - 기타: 간 질환, 담낭 질환, 고혈당, 개방각 녹내장, 양성 전립선 비대증, 조증, 약물 남용/의존, 비만
- **약물 상호작용**: 조회된 상호작용은 총 100건입니다. 이 중 심각도 **Major**로 확인된 항목은 다음과 같습니다.
  - Bupropion
  - Morphine
  - Potassium citrate

  Moderate 등급에는 Epinephrine, Metformin, Pioglitazone, Atropine, Clarithromycin 등이 있습니다.
- **계열 약물 망막 독성**: 같은 페노티아진계 약물에서 색소성 망막병증이 보고되어 있습니다. 망막 질환을 대상으로 하는 재창출에서는 반드시 고려할 안전성 신호입니다.

허가사항상 경고 및 금기는 허가정보 PDF를 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
망막 이영양증에 대한 임상시험과 치료 효과를 지지하는 문헌이 없고, 유일한 문헌은 계열 약물의 망막 독성을 보고합니다. 기전상 연결고리도 확인되지 않아 현재 단계에서 진행할 근거가 없습니다.

**진행하려면 필요한 것:**
- 허가정보 PDF에서 적응증, 경고, 금기 확인
- 작용 기전 데이터 확보 (DrugBank 등)
- 망막 이영양증에 대한 전임상 또는 기전 연구와 망막 독성 위험 평가

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

