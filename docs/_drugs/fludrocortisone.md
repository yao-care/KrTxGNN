---
layout: default
title: Fludrocortisone
parent: 모델 예측만 (L5)
nav_order: 354
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Fludrocortisone: 예측 신규 적응증 원발성 피부 T세포 림프종 (primary cutaneous T-cell lymphoma) (근거 수준 L5). 기존 적응증: 허가 적응증 문구는 링크 형태로만 제공되어 확인 불가 (식약처 의약품안전나라 허가 문서 참조)"
monitor_inn: "fludrocortisone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "cystic teratoma", "spinal cord dermoid cyst", "dermoid cyst of ovary", "disease of orbital part of eye adnexa", "eye disease", "disease of orbital region", "exostosis"]
---

# Fludrocortisone
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

# Fludrocortisone: 허가 적응증 정보 미확인에서 원발성 피부 T세포 림프종으로

## 한 문장 요약

Fludrocortisone은 합성 미네랄로코르티코이드(부신피질호르몬)로, 한국에서는 플로리네프정으로 시판되고 있습니다. 다만 이번 보고서에 사용된 데이터에서는 허가 적응증의 구체적인 문구를 확인할 수 없었습니다.
TxGNN 모델은 **원발성 피부 T세포 림프종(primary cutaneous T-cell lymphoma)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
따라서 현재는 모델 예측만 있는 단계(L5)이며, 권장 결정은 **Hold**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 문구는 링크 형태로만 제공되어 확인 불가 (식약처 의약품안전나라 허가 문서 참조) |
| 예측 신규 적응증 | 원발성 피부 T세포 림프종 (primary cutaneous T-cell lymphoma) |
| TxGNN 예측 점수 | 99.58% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 fludrocortisone은 미네랄로코르티코이드 작용이 주되고 일부 글루코코르티코이드 작용도 가진 코르티코스테로이드입니다. 일반적으로 부신 기능부전 등에서 미네랄로코르티코이드 효과를 목적으로 사용됩니다.

글루코코르티코이드는 림프구를 억제하는 효과가 있어 림프종 치료에 일부 활용됩니다. 그러나 fludrocortisone 자체가 피부 T세포 림프종에 의미 있는 활성을 보인다는 근거는 없습니다. 이번 예측과 기존 적응증 사이의 연관성은 **추측 수준**입니다.

참고로 상위 예측 8건(낭성 기형종, 척수 유피낭종, 난소 유피낭종, 안와 질환, 외골종 등)도 모두 약리학적 근거가 뚜렷하지 않습니다. 이들은 모델 네트워크 구조에서 비롯된 결과일 가능성이 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

> 참고: 예측 순위 6위인 "안질환(eye disease)"에는 문헌 20편이 연결되어 있습니다. 이 중 기전상 의미가 있는 것은 망막 변성 모델에서 fludrocortisone의 항염증·신경보호 효과를 보고한 전임상 연구(PMID 34509498, 2021)와 지도모양 위축 환자 대상 1B상 안전성 연구(PMID 36161841, 2022) 정도입니다. 나머지는 부신 기능부전, 자가면역 다선증후군, 자율신경 이상, 신세뇨관 산증 등 기존 용도와 관련된 문헌이거나 녹내장 비-안압 치료 리뷰입니다. 다만 "안질환"은 범위가 너무 넓어 구체적인 임상 질문을 정하기 어렵고, 이 보고서의 주 예측(피부 T세포 림프종)과는 별개입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199907231 | 플로리네프정(미분화플루드로코르티손아세테이트) | 흰색의 양면이 볼록한 원형의 정제 | 허가 문서 링크로만 제공됨 (식약처 의약품안전나라 참조) |

## 안전성 고려사항

- **약물 상호작용**: 데이터에서 총 446건의 상호작용이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major**: Bupropion
  - **Moderate**: 혈당강하제 계열(Acarbose, Pioglitazone, Chlorpropamide, Alogliptin, Linagliptin, Canagliflozin, Dapagliflozin, Empagliflozin, Albiglutide, Dulaglutide), Amphotericin B, Aprepitant, Acetylsalicylic acid, Clarithromycin, 하제(Bisacodyl, Picosulfuric acid), 동화스테로이드(Oxandrolone, Oxymetholone)

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
원발성 피부 T세포 림프종에 대한 근거는 TxGNN 예측 점수(99.58%)뿐이며, 임상시험과 문헌이 없고 기전상 연결고리도 추측 수준입니다. 허가 문서의 경고·금기 정보도 확인되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가 문서(첨부문서)를 내려받아 허가 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 피부 T세포 림프종과 fludrocortisone의 연관성에 대한 전임상 또는 문헌 근거 탐색
- 장기적으로 미네랄로코르티코이드 부작용(고혈압, 저칼륨혈증, 체액 저류)에 대한 안전성 평가
- 대안으로, 상대적으로 문헌이 있는 망막 변성 등 좁게 정의된 안과 적응증을 별도 연구 질문으로 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

