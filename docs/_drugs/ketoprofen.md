---
layout: default
title: Ketoprofen
parent: 모델 예측만 (L5)
nav_order: 449
evidence_level: L5
indication_count: 9
monitor_inn: "Ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
last_modified_at: 2026-10-31
description: "Ketoprofen: 예측 신규 적응증 말단중간형 이형성증, Hunter-Thompson형 (근거 수준 L5). 기존 적응증: 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통…"
---

# Ketoprofen
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

## Ketoprofen: 퇴행성관절염 등 근골격계 통증·염증에서 말단중간이형성증 헌터-톰슨형으로
{: .text-alpha }

## 한 문장 요약

Ketoprofen은 비스테로이드성 소염진통제(NSAID)로, 한국에서 퇴행성관절염, 어깨관절주위염, 건·건초염, 근육통, 외상 후 종창·통증의 진통·소염에 허가되어 있습니다.
TxGNN 모델은 **말단중간형 이형성증, Hunter-Thompson형(acromesomelic dysplasia, Hunter-Thompson type)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0건**입니다.
따라서 현재는 모델 예측만 있는 단계(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통, 외상 후 종창·동통의 진통·소염 |
| 예측 신규 적응증 | 말단중간형 이형성증, Hunter-Thompson형 |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 18건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 Ketoprofen은 COX-1/COX-2를 억제하여 프로스타글란딘 합성을 줄이는 소염진통제로 알려져 있으며, 한국 허가 적응증도 이 소염·진통 작용에 기반합니다.

예측된 질환은 CDMP1/GDF5 기능상실로 생기는 희귀 골격 이형성증으로, 뼈 성장 신호 이상이 본질입니다. COX 억제가 이 발달 결함을 교정할 기전적 근거는 확인되지 않습니다. 기껏해야 근골격계 통증에 대한 대증적 진통 효과를 기대할 수 있는 정도입니다. 높은 점수는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

같은 상위 예측군(2~7위)도 대부분 희귀 골격·발달 이상 질환(brachyolmia, pseudoachondroplasia 등)입니다. 이 중 LACC1 결손에 의한 소아 관절염(9위)과 pseudoachondroplasia(7위)는 허가 적응증인 관절염 통증과 간접적으로 겹치지만, 이 역시 대증 치료 가설에 그칩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

확인된 허가는 최소 20건이며, 목록은 일부일 수 있습니다. 아래는 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199201803 | 케바논겔 | 겔 | 퇴행성관절염(골관절염), 어깨관절주위염, 건ㆍ건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |
| 201706431 | 제일케토파워카타플라스마 | 카타플라스마제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건·건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |
| 200002439 | 케바논첩부제 | 첩부제 | 퇴행성관절염(골관절염), 어깨관절주위염, 건ㆍ건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |
| 199400367 | 케노펜겔 | 겔 | 퇴행성관절염(골관절염), 어깨관절주위염, 건ㆍ건초염, 건주위염, 상완골상과염(테니스 엘보우 등), 근육통... |
| 198801250 | 부광케토프로펜주100밀리그램 | 주사제 | 허가 적응증 텍스트 없음(링크만 제공) |

## 안전성 고려사항

- **약물 상호작용**: 조회 결과 총 100건이 확인되었으며, 이 중 일부는 다음과 같습니다.
  - 중등도: Acetylsalicylic acid, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide, Metformin, Glimepiride, Chlorpropamide, Mesalazine, Balsalazide, Naltrexone, Potassium citrate, Potassium bicarbonate 등
  - 경미: Famotidine, Ranitidine, Cimetidine, Linaclotide

경고·금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환에 대한 임상시험과 문헌이 전혀 없고, COX 억제와 GDF5 결손 골 발달 이상을 잇는 기전적 근거도 확인되지 않습니다. 모델 점수만으로는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- Ketoprofen의 작용 기전 데이터 확보
- 예측 질환에 대한 전임상·임상 연구 또는 문헌 근거
- 허가사항(경고·금기) 확인 및 안전성 검토
- 현실적인 목표 설정: 질병 조절이 아닌 대증적 통증 완화(예: 이차성 관절 통증)로 가설을 한정하고, 이 경우 제형·투여 경로 적합성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

