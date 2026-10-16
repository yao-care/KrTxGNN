---
layout: default
title: Nusinersen
parent: 모델 예측만 (L5)
nav_order: 555
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nusinersen: 예측 신규 적응증 고알도스테론증 (Hyperaldosteronism) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 데이터에 텍스트로 제공되지 않아(허가 문서 링크만 있음) 허가사항 확인 필요"
monitor_inn: "Nusinersen"
predicted_indications: ["hyperaldosteronism", "ophthalmomyiasis", "multilocular clear cell renal cell carcinoma", "galactosemia", "mucinous tubular and spindle renal cell carcinoma", "sarcomatoid renal cell carcinoma", "rhinitis", "malignant peritoneal solitary fibrous tumor", "potassium deficiency disease", "central nervous system angiosarcoma"]
---

# Nusinersen
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

# Nusinersen: 척수성 근위축증에서 고알도스테론증으로

## 한 문장 요약

Nusinersen(제품명 스핀라자주)은 SMN2 유전자의 스플라이싱을 조절하는 안티센스 올리고뉴클레오타이드로, 한국에서 허가를 받아 시판 중입니다. TxGNN 모델은 **고알도스테론증(hyperaldosteronism)**에 효과가 있을 수 있다고 예측했지만, 점수는 50%로 정보가치가 없는 수준입니다. 이 예측을 지지하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 데이터에 텍스트로 제공되지 않아(허가 문서 링크만 있음) 허가사항 확인 필요 |
| 예측 신규 적응증 | 고알도스테론증 (Hyperaldosteronism) |
| TxGNN 예측 점수 | 50.0% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 이번 보고서용으로 수집된 데이터에서 기전 정보는 확인되지 않았습니다. 일반적으로 알려진 바로는 Nusinersen은 SMN2 pre-mRNA의 스플라이싱을 조절해 SMN 단백질 생성을 늘리는 안티센스 올리고뉴클레오타이드이며, 척수성 근위축증 치료를 목적으로 합니다.

고알도스테론증은 알도스테론 분비 조절 이상으로 생기는 내분비 질환으로, SMN 단백질 결핍이나 SMN2 스플라이싱과의 기전적 연관성이 확립되어 있지 않습니다. 예측 점수 0.5는 모델이 사실상 판단을 내리지 못한 값에 가깝고, 이를 뒷받침하는 임상시험이나 문헌도 없습니다. 따라서 현 시점에서 이 예측은 타당성을 주장하기 어렵습니다.

같은 방식으로 평가된 다른 예측 질환(안구 파리유충증, 다방성 투명세포 신세포암, 갈락토스혈증, 비염, 칼륨 결핍증, 중추신경계 혈관육종 등)도 모두 점수 50%, 근거 수준 L5이며 임상시험과 문헌이 없습니다. 이들 역시 기전적 연결고리가 확인되지 않아 Hold로 판단됩니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201708641 | 스핀라자주(뉴시너센나트륨) | 무색투명한 액이 무색투명한 유리 바이알에 든 주사제 | 허가사항 문서 참조 (바이오젠코리아유한회사) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수가 0.5로 정보가치가 없고, 임상시험과 문헌 근거가 전혀 없습니다. Nusinersen의 기전과 고알도스테론증 사이에 알려진 연관성도 없어 근거 수준은 L5에 머뭅니다.

**진행하려면 필요한 것:**
- 허가사항의 적응증, 경고, 금기 정보 확보(허가 문서 확인 및 파싱)
- Nusinersen의 작용 기전 데이터 보강
- 고알도스테론증과의 기전적 연관성을 보여주는 전임상 또는 문헌 근거
- 모델 예측을 재검증하거나 더 변별력 있는 점수 확보
- 투여 경로(척수강 내 투여) 적합성 평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

