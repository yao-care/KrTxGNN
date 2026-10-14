---
layout: default
title: Telmisartan
parent: 모델 예측만 (L5)
nav_order: 721
evidence_level: L5
indication_count: 10
---

# Telmisartan
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Telmisartan: 고혈압에서 허혈성 뇌졸중 감수성으로

## 한 문장 요약

Telmisartan은 안지오텐신 II 1형(AT1) 수용체 차단제(ARB)로, 한국에서 고혈압 계열 단일제 및 복합제로 시판되고 있습니다.
TxGNN 모델은 **허혈성 뇌졸중 감수성(obsolete susceptibility to ischemic stroke)** 에 효과가 있을 수 있다고 예측하지만, 이 용어 자체로 확인된 **임상시험은 0건, 문헌도 0건**입니다. 현재는 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고혈압 (허가 적응증 원문은 링크로만 제공되어 있어, 약물 분류와 평가 자료를 근거로 요약) |
| 예측 신규 적응증 | 허혈성 뇌졸중 감수성 (obsolete susceptibility to ischemic stroke) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 정리되어 있지 않습니다. 다만 평가 자료에 따르면 Telmisartan은 AT1 수용체를 차단해 혈압을 낮추는 약물입니다. 혈압 조절은 뇌졸중 예방의 가장 중요한 요인이므로, 고혈압에서의 효능이 뇌졸중 위험 감소로 이어질 수 있다는 기전상 연결이 가능합니다.

다만 해당 질환명은 이미 폐기된(obsolete) 용어이며, 치료 대상이 되는 임상 질환이라기보다 "감수성(susceptibility)"이라는 위험 개념에 가깝습니다. 이 정확한 용어로는 시험이나 문헌이 확인되지 않았습니다. 뇌졸중 관련 근거는 별도의 유사 적응증 항목(뇌졸중, 뇌혈관 질환 등)에서 따로 평가되었습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가증은 총 20건(모두 유효, 취소 0건)입니다. 아래는 주요 5건이며, 허가 적응증 원문은 각 허가사항 링크로만 제공됩니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201605614 | 투탑스정80/10밀리그램 (일동제약) | 이중정 | [허가사항 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605614/EE) |
| 201606795 | 텔미더블정40/10밀리그램 (녹십자) | 이중정 | [허가사항 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606795/EE) |
| 201802585 | 트레블정80/5/10밀리그램 (셀트리온제약) | 필름코팅정 | [허가사항 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802585/EE) |
| 201701432 | 티살탄플러스정80/12.5밀리그램 (서울제약) | 정제 | [허가사항 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201701432/EE) |
| 202101318 | 텔로바틴정40/10밀리그램 (제뉴파마) | 필름코팅정 | [허가사항 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202101318/EE) |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었고, 그중 20건이 데이터에 수록되어 있습니다.
  - **Major**: 칼륨 보충제(Potassium citrate, Potassium bicarbonate). 고칼륨혈증 위험에 유의해야 합니다.
  - **Moderate**: 코르티코스테로이드(Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide), SGLT2 억제제(Canagliflozin, Dapagliflozin, Empagliflozin), 인슐린(Insulin human, Insulin aspart), Exenatide, 아세틸살리실산, Morphine, Bupropion, Dronabinol, 장정결제(Picosulfuric acid, Polyethylene glycol, Sodium sulfate) 등.

경고와 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만(99.99%), 예측된 질환명이 폐기된 용어이자 치료 대상이 아닌 감수성 개념입니다. 이 용어로 확인된 임상시험과 문헌도 없어 모델 예측 외의 근거가 없습니다.

**진행하려면 필요한 것:**
- 질환 정의를 정리하고, 실제 임상 질환(뇌졸중, 뇌혈관 질환)으로 평가 대상을 재설정
  - 같은 예측 목록의 "stroke disorder"와 "cerebrovascular disorder"는 TRIDENT 3상(NCT02699645)과 ONTARGET 등으로 근거 수준 L1로 평가되었습니다. 이 항목들로 평가를 옮기는 것이 현실적입니다.
  - 다만 이 효과는 혈압 강하와 복합제 효과에 크게 기인해 Telmisartan 단독 효과로 분리되지 않았고, 두 항목은 서로 겹치므로 독립된 근거로 계산하면 안 됩니다.
- 허가사항 PDF에서 경고·금기와 허가 적응증 원문을 확인해 안전성 선별 수행
- 상세한 작용 기전(MOA) 데이터 보완
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

