---
layout: default
title: Emtricitabine
parent: 모델 예측만 (L5)
nav_order: 308
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
description: "Emtricitabine: 예측 신규 적응증 고양이 후천성 면역결핍증후군 (feline acquired immunodeficiency syndrome) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 아닌 허가사항 문서 링크만 수록되어 있어 구체적 문구를 확인할 수 없음 (허가사항 참조)"
monitor_inn: "EMTRICITABINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Emtricitabine
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

## Emtricitabine: HIV 감염에서 고양이 면역결핍증후군(feline acquired immunodeficiency syndrome)으로
{: .text-alpha }

## 한 문장 요약

Emtricitabine은 뉴클레오시드 역전사효소 억제제(NRTI)로, 한국에서 복합제 제품(트루바다정, 데스코비정)으로 허가·시판되고 있습니다.
TxGNN 모델은 **고양이 후천성 면역결핍증후군(feline acquired immunodeficiency syndrome)**에 효과가 있을 수 있다고 예측합니다.
다만 이 예측을 지지하는 근거는 **임상시험 0건**, **문헌 1편(수의학 전임상 연구)**에 그치며, 사람에 대한 새로운 치료 적응증으로 보기는 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 아닌 허가사항 문서 링크만 수록되어 있어 구체적 문구를 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 고양이 후천성 면역결핍증후군 (feline acquired immunodeficiency syndrome) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 (전임상·수의학 연구 수준) |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, emtricitabine은 NRTI 계열 약물로 세포 내에서 인산화되어 역전사효소를 억제(사슬 종결)하는 것으로 알려져 있으며, 한국에서는 복합제(트루바다정, 데스코비정)의 성분으로 허가되어 있습니다.

고양이 면역결핍바이러스(FIV)는 HIV와 같은 렌티바이러스이며, 역전사효소 구조가 유사합니다. 따라서 NRTI 계열 약물의 활성은 생물학적으로 가능성이 있습니다. 다만 이는 NRTI 계열 일반 지식에 기반한 추론입니다.

근거가 되는 2023년 연구(PMID 37112803)는 dolutegravir, tenofovir, emtricitabine 병합 항레트로바이러스 요법을 FIV 감염 고양이에 투여해 약동학과 임상 결과를 평가했습니다. 그러나 확인 가능한 정보는 제목과 초록 일부뿐이어서 emtricitabine 단독 효과와 구체적 결과는 판단할 수 없습니다. 또한 이는 수의학 적응증이므로 사람 대상 임상적 의미는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | 전임상/수의학 연구 | Viruses | FIV 감염 고양이에서 병합 항레트로바이러스 요법(dolutegravir, tenofovir, emtricitabine)의 약동학과 임상 결과를 평가. 초록이 일부만 제공되어 구체적 효능 결과는 확인되지 않음 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201003484 | 트루바다정 | 파란색 장방형 필름코팅정 (“GILEAD”/“701” 음각) | 허가사항 문서 참조 |
| 201701115 | 데스코비정 200/25 mg | 파란색 직사각형 필름코팅정 (“GSI”/“225”) | 허가사항 문서 참조 |
| 201701116 | 데스코비정 200/10 mg | 회색 직사각형 필름코팅정 (“GSI”/“210”) | 허가사항 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 20건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - 중대(Major): leflunomide, teriflunomide
  - 중등도(Moderate): orlistat, naltrexone, cobicistat, methotrexate, cladribine, clofarabine, epirubicin, interferon beta-1a/1b, peginterferon beta-1a, asparaginase, pegaspargase, brentuximab vedotin, cabozantinib, idelalisib, tioguanine, trabectedin
  - 경미(Minor): eribulin
- **지식 그래프 기반 금기 관련 질환**: 지식 그래프(라벨 문구가 아님)에서 간부전·간질환, 신장질환, 젖산산증, 판코니 증후군, QT 연장 증후군, 만성 B형·C형 간염 등이 금기 관련 질환으로 연결되어 있습니다. 이는 허가사항 근거가 아니므로 참고용으로만 활용해야 합니다.

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
유일한 근거는 수의학 전임상 문헌 1편이며 임상시험이 없습니다. 또한 이 적응증은 동물 질환이어서 사람 대상 신규 치료 적응증으로서의 가치가 제한적입니다.

**참고 사항:**
- 동일 약물의 TxGNN 예측 2순위인 원숭이 면역결핍바이러스(SIV) 감염은 마카크 모델 연구가 다수 있으나, 이미 승인된 HIV 적응증의 전임상 모델 근거에 해당하며 새로운 사람 적응증은 아닙니다. 번역 연구 모델로서의 가치로 보는 것이 적절합니다.
- 3순위인 "운동실조 보행, 언어 상실, 대뇌 백질 감소를 동반한 신경발달장애"는 기전적 연관성이 확인되지 않고 임상시험과 문헌이 모두 없습니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 학습한 관련 질환 간 유사성을 반영할 수 있지만 생물학적 근거는 아닙니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·허가 적응증) 원문 확보 및 분석
- 상세 작용 기전(MOA) 데이터 확보
- PMID 37112803의 전문 확인을 통한 emtricitabine의 기여도 및 결과 검증
- 사람 대상 재창출 후보로 검토하려면 인체 질환 대상의 새로운 적응증 후보 재선별
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

