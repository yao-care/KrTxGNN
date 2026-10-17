---
layout: default
title: Triptorelin
parent: 모델 예측만 (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Triptorelin: 예측 신규 적응증 다모증 (Hypertrichosis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 링크로만 제공되어 확인할 수 없음 (허가사항 원문 참조)"
monitor_inn: "Triptorelin"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "allergic urticaria", "familial male-limited precocious puberty", "precocious puberty", "familial isolated trichomegaly", "aromatase excess syndrome"]
---

# Triptorelin
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

# Triptorelin: GnRH 작용제 치료에서 다모증(Hypertrichosis)으로

## 한 문장 요약

Triptorelin은 GnRH(성선자극호르몬 분비호르몬) 작용제로, 국내에서 4건의 허가증으로 시판 중입니다. TxGNN 모델은 **다모증(Hypertrichosis)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 뒷받침하는 임상시험은 **0건**입니다. 문헌 **1편**은 다른 약물(사이클로스포린)이 유발한 다모증 증례로, Triptorelin의 치료 효과를 보여 주지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 링크로만 제공되어 확인할 수 없음 (허가사항 원문 참조) |
| 예측 신규 적응증 | 다모증 (Hypertrichosis) |
| TxGNN 예측 점수 | 99.997% |
| 근거 수준 | L5 (모델 예측 수준) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Triptorelin은 GnRH 작용제입니다. 지속 투여하면 뇌하수체 GnRH 수용체가 둔감화되어 LH/FSH와 성호르몬 분비가 억제됩니다.

이 안드로겐 억제가 모발 성장에 영향을 줄 가능성은 이론적으로 생각해 볼 수 있습니다. 그러나 이는 추정일 뿐이며, 이 연결을 지지하는 임상 자료는 없습니다. 유일한 문헌은 테스토스테론 차단제(Triptorelin 포함)를 쓰던 트랜스젠더 여성에서 사이클로스포린이 다모증을 일으킨 사례입니다. 이 사례는 다모증이 다른 약물의 부작용으로 나타났음을 보여 줄 뿐, Triptorelin이 다모증을 치료한다는 근거가 아닙니다. 매우 높은 TxGNN 점수는 지식 그래프상의 근접성을 반영한 것으로 보이며, 임상 근거로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case report | Cureus | 테스토스테론 차단제(Triptorelin 등)를 쓰던 트랜스젠더 여성에서 사이클로스포린이 전신 다모증을 유발한 증례. 안드로겐 억제 상태에서도 발생했다는 내용이며, Triptorelin의 치료 효과를 보여 주지 않음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200109188 | 디페렐린피알3.75밀리그람주 | 주사제 (바이알 및 용매 앰플) | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200109188/EE) 참조 |
| 199604919 | 데카펩틸-데포 | 주사제 (마이크로캡슐 바이알 및 용매) | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199604919/EE) 참조 |
| 199604920 | 데카펩틸주0.1밀리그램 | 프리필드 주사액 | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199604920/EE) 참조 |
| 201100197 | 동국트립토렐린아세트산염데포주사 (수출용) | 주사제 (바이알 및 앰플) | [허가 문서 링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201100197/EE) 참조 |

4건 모두 단일제이며 유효 상태입니다.

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 총 100건이 확인되었습니다. 이 중 중증도 **Major**는 Dolasetron입니다. 나머지 주요 항목은 대부분 **Moderate**이며 다음과 같습니다.
  - 당뇨병 치료제: Acarbose, Metformin, Pioglitazone, Glimepiride, Chlorpropamide, Alogliptin, Saxagliptin, Canagliflozin, Dapagliflozin, Empagliflozin, Albiglutide, Dulaglutide
  - 위장관계 약물: Famotidine, Loperamide, Bisacodyl, Picosulfuric acid, Polyethylene glycol
  - 기타: Clarithromycin, Palonosetron

주요 경고와 금기는 허가사항을 참조하세요.

## 참고: 다른 예측 적응증

이번 평가의 1순위 예측은 다모증이지만, 이번 데이터에서 가장 근거가 강한 예측은 8순위인 **중추성 성조숙증(Precocious puberty)**입니다.

- 완료된 Phase 3 시험이 NCT01278290, NCT04736602, NCT00564850, NCT00909844, NCT01467882, NCT05029622 등 6건입니다.
- 3개월 제형과 6개월 제형의 효능이 확인되었습니다.
- 다만 이는 이미 확립된 기존 용도에 가까워 엄밀한 의미의 재창출이 아닙니다.
- 가족성 남성 제한 성조숙증(testotoxicosis) 같은 말초성 형태는 GnRH 작용제에 반응하지 않으므로, 중추성(성선자극호르몬 의존성)에 한정해야 합니다.

이 적응증은 별도 보고서로 평가하는 것을 권장합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다모증에 대한 임상시험이 없고, 유일한 문헌은 다른 약물의 부작용 증례여서 Triptorelin의 효과를 뒷받침하지 못합니다. 기전상 연결도 추정 수준이며, 높은 TxGNN 점수만으로는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항 원문 확인: 기존 적응증, 경고, 금기
- 상세한 작용 기전 데이터 (MOA)
- 안드로겐 억제와 다모증의 관련성을 보여 주는 전임상 또는 임상 근거
- 근거가 충분한 성조숙증 등 다른 예측 적응증을 우선 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

