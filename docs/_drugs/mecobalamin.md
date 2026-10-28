---
layout: default
title: Mecobalamin
parent: 모델 예측만 (L5)
nav_order: 495
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Mecobalamin: 예측 신규 적응증 경화성 담관염 (Sclerosing Cholangitis) (근거 수준 L5). 기존 적응증: 말초성 신경장애"
monitor_inn: "MECOBALAMIN"
predicted_indications: ["sclerosing cholangitis", "multiple endocrine neoplasia", "bone Paget disease"]
---

# Mecobalamin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

## Mecobalamin: 말초성 신경장애에서 경화성 담관염으로
{: .text-alpha }

## 한 문장 요약

Mecobalamin은 활성형 비타민 B12로, 한국에서 말초성 신경장애 치료에 사용되고 있습니다.
TxGNN 모델은 **경화성 담관염(Sclerosing Cholangitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 즉, 모델 예측만 있는 초기 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 말초성 신경장애 |
| 예측 신규 적응증 | 경화성 담관염 (Sclerosing Cholangitis) |
| TxGNN 예측 점수 | 0.9950 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 17건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Mecobalamin은 메틸화 반응과 신경 수초(myelin) 유지에 관여하는 활성형 비타민 B12이며, 말초성 신경장애에서의 사용이 허가되어 있습니다.

그러나 이 기전과 경화성 담관염의 담도 염증 및 섬유화를 직접 연결하는 확립된 근거는 없습니다. 이번 예측 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으며 생물학적 근거는 아닙니다.

참고로 같은 모델이 예측한 다른 후보(다발성 내분비 종양, 뼈 파제트병; 각각 0.9934, 0.9931)도 동일하게 임상시험과 문헌 근거가 없고 기전적 연결이 불분명합니다. 높은 점수는 생물학적 근거보다는 네트워크상의 근접성을 반영했을 가능성이 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 197800391 | 메코민캡슐 | 경질캡슐제 | 말초성 신경장애 |
| 198500436 | 엠코발500마이크로그램캡슐 | 경질캡슐제 | 말초성 신경장애 |
| 199801474 | 파마메코발라민정 | 당의정 | 말초성 신경장애 |
| 200003493 | 맥타정 | 필름코팅정 | 요(허리)통, 수족저림, 신경통, 어깨ㆍ목 결림 증상의 완화 |
| 202301564 | 메코이에프정 | 필름코팅정 | 육체피로, 임신 및 수유기, 체력저하 시 비타민 E, B1, B6의 보급... |

## 안전성 고려사항

- **약물 상호작용**: 총 13건이 확인되었습니다.
  - 보통(Moderate): Arsenic trioxide, Chloramphenicol
  - 경미(Minor): 위산 억제제 11종 (Famotidine, Ranitidine, Cimetidine, Nizatidine, Rabeprazole, Omeprazole, Esomeprazole, Lansoprazole, Dexlansoprazole, Pantoprazole, Ranitidine bismuth citrate)
- **지식 그래프상 금기 관련 질환**: 칼륨 결핍증, 만성 위축성 위염, 레베르 유전성 시신경병증. 이는 지식 그래프의 약물-질환 금기 연결에 근거한 것이며 허가사항 문구가 아닙니다.

허가사항의 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
경화성 담관염 예측은 TxGNN 점수(0.9950)만 있고 임상시험과 문헌 근거가 전혀 없으며, 기전적 연결도 확인되지 않았습니다. 현 단계에서는 진행을 권장하기 어렵습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고·금기) 확보 및 안전성 검토
- 상세한 작용 기전(MOA) 데이터 확보
- 비타민 B12/메틸화와 경화성 담관염 간 기전 연관성에 대한 전임상 또는 문헌 근거
- 관련 임상시험 및 문헌 재검색
- 투여 경로 적합성 평가 (현재 미확정)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

