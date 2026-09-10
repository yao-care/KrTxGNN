---
layout: default
title: Fusidic Acid
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Fusidic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fusidic Acid: 세균 감염증에서 노출성 각막염 속발 감염으로

## 한 문장 요약

Fusidic Acid(Sodium Fusidate)는 그람양성균(특히 황색포도상구균·MRSA)에 작용하는 항생제로, 한국에는 아직 허가·시판되지 않은 상태입니다. TxGNN 모델은 **노출성 각막염(Exposure Keratitis)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 뒷받침하는 임상시험은 없고 관련성이 확정되지 않은 **사례 시리즈 문헌 1편**만 존재해 근거가 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 데이터 없음 (한국 미허가, 등록된 라이선스 0건) |
| 예측 신규 적응증 | 노출성 각막염 (Exposure Keratitis) |
| TxGNN 예측 점수 | 99.95% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미출시 (한국 미허가) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

DrugBank 공식 작용기전(MOA) 필드는 현재 데이터 갭 상태입니다(DG002, 중요도 High). 다만 Evidence Pack에 포함된 재창출 근거 서술에 따르면, Fusidic acid(sodium fusidate)는 세균 리보솜에서 신장인자 EF-G의 방출을 차단해 단백질 합성을 억제하는 항생제로, 그람양성균—특히 황색포도상구균(MRSA 포함)—에 주로 작용합니다.

노출성 각막염은 눈꺼풀 폐쇄부전으로 각막 표면이 건조·손상되면서 세균(특히 황색포도상구균) 속발 감염이 흔히 동반되는 질환입니다. Fusidic acid 안과용 국소 제제(예: Fucithalmic)는 여러 국가에서 세균성 결막염·각막염 치료에 이미 승인되어 안전성 자료가 성숙한 편이지만, "노출성 각막염 속발 감염"만을 표적으로 한 직접 대조시험은 아직 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case Series | Cornea | Tsukamurella균에 의한 안과 감염의 최대 규모 사례 시리즈(임상 양상·위험인자·치료·경과 보고, 안구 임플란트 감염 첫 사례 포함). Fusidic acid 치료 결과를 직접 다룬 연구는 아니며 관련성 판정은 미확정(pending) |

## 한국 시판 정보

현재 한국에 허가된 제품이 없습니다 (총 허가증 0건, 미출시).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

*(참고: 경고·금기 항목은 데이터 갭이며, 이 중 TFDA 첨부문서 정보 부재는 Blocking 등급으로 분류되어 S1 안전성 초기평가 진입 자체를 막고 있습니다.)*

## 결론 및 다음 단계

**결정: Hold**

**사유:**
1위 예측 적응증(노출성 각막염)의 근거가 fusidic acid를 직접 다루지 않은 사례 시리즈 1편(관련성 미확정, tier 3)뿐이며 임상시험 등록이 전무해 근거 수준이 L4에 그칩니다. 여기에 경고·금기 등 안전성 정보가 전부 데이터 갭 상태이고, 이 중 하나는 S1 안전성 초기평가 진입을 막는 Blocking 이슈(DG001)로 분류되어 있어 현재로서는 진행이 불가합니다. 참고로 5위 예측인 post-bacterial disorder는 Fusidic acid 본체를 사용한 완료된 Phase 3 RCT(NCT02570490, n=716)가 있어 근거 수준이 더 높으므로, 후속 평가 시 함께 검토할 가치가 있습니다.

**진행하려면 필요한 것:**
- TFDA(해당국 규제기관) 공식 첨부문서에서 경고·금기 정보 확보 (DG001, Blocking)
- DrugBank 공식 MOA 데이터 확보 (DG002, High)
- 노출성 각막염 속발 세균감염에서 fusidic acid 국소 제제의 직접 임상 데이터 축적
- 한국 내 유사 적응증(세균성 결막염·각막염) 국소 안과용 제제 허가 현황 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

