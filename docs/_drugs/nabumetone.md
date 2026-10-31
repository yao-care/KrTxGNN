---
layout: default
title: Nabumetone
parent: 모델 예측만 (L5)
nav_order: 533
evidence_level: L5
indication_count: 9
monitor_inn: "Nabumetone"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis"]
last_modified_at: 2026-10-31
description: "Nabumetone: 예측 신규 적응증 말단중간형 이형성증, Hunter-Thompson형 (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 없어 확인 불가 (허가사항 문서 링크만 제공됨)"
---

# Nabumetone
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

## Nabumetone: 허가 적응증 확인 불가에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Nabumetone은 한국에서 단일성분 제제로 허가된 비스테로이드성 소염진통제(NSAID)입니다. 다만 이번 데이터에는 허가 적응증의 본문 텍스트가 없고 링크만 있어, 구체적인 기존 적응증은 확인하지 못했습니다. TxGNN 모델은 **말단중간형 이형성증, Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측합니다. 그러나 이를 뒷받침하는 **임상시험과 문헌은 0건**이며, 근거 수준은 L5(모델 예측만 있음)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 없어 확인 불가 (허가사항 문서 링크만 제공됨) |
| 예측 신규 적응증 | 말단중간형 이형성증, Hunter-Thompson형 |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 (목록이 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 nabumetone은 NSAID이며, 활성 대사체 6-MNA가 COX를 억제하고 COX-2에 상대적으로 선택성을 보이는 것으로 알려져 있습니다. 다만 이 내용은 이번에 수집된 데이터가 아닌 일반 약리 지식입니다.

예측된 질환은 CDMP1/GDF5 기능 소실 변이로 생기는 희귀 골격 이형성증입니다. 연골과 뼈의 패턴 형성 이상이 원인입니다. Nabumetone이 GDF5/BMP 신호 경로에 작용한다는 근거는 없습니다. 따라서 0.9999라는 높은 점수는 TxGNN 모델(딥러닝)이 산출한 값이며, 모델이 학습한 관련 질환 간 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 생물학적·임상적 데이터의 뒷받침도 없습니다. 기대할 수 있는 것은 관절통에 대한 증상 완화 정도이며, 질환 자체를 개선하는 효과는 아닙니다.

## 한국 시판 정보

허가 적응증은 문서 링크로만 제공되어 본문을 확인할 수 없습니다. 아래는 목록 중 일부이며, 전체 목록이 아닐 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201908446 | 나부민정 (수출용) | 필름코팅정 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201908446/EE) 참조 |
| 200404646 | 나메톤정 | 필름코팅정 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200404646/EE) 참조 |
| 199200885 | 한독렐라펜정 | 제피정 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199200885/EE) 참조 |
| 200403776 | 코러스나부메톤정 | 필름코팅정 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200403776/EE) 참조 |
| 200411208 | 이텍스나부메톤정500mg | 필름코팅정 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200411208/EE) 참조 |

## 안전성 고려사항

허가사항의 경고·금기 정보는 이번 데이터에 포함되어 있지 않습니다. 자세한 내용은 허가사항을 참조하세요.

**약물 상호작용** (DDInter 기준, 총 100건 중 일부):
- **중등도**: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide(전신 코르티코스테로이드 계열), acetylsalicylic acid, metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, vancomycin 등
- **경미**: ranitidine, cimetidine, linaclotide

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만, 직접 연구한 임상시험이나 문헌이 없고 기전적 연결도 확인되지 않습니다. 이 질환은 유전적 골격 발달 이상이어서 COX 억제로 근본 병태를 교정하기 어렵습니다. 같은 후보 목록에서는 류마티스 결절증(rheumatoid nodulosis)이 기전상 가장 개연성이 높지만, 이 역시 직접 근거가 없습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 본문 확보
- 작용 기전 데이터 확보 (DrugBank 등)
- 예측 질환에 대한 전임상 또는 임상 근거 탐색
- 증상 완화 목적의 사용 가능성을 별도로 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

