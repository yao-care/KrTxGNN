---
layout: default
title: Glimepiride
parent: 모델 예측만 (L5)
nav_order: 382
evidence_level: L5
indication_count: 9
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-30
description: "Glimepiride: 예측 신규 적응증 고전형 전신 경직 증후군 (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문이 자료에 없음)"
---

# Glimepiride
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

## Glimepiride: 제2형 당뇨병 치료제에서 전신 경직 증후군(Classic Stiff Person Syndrome)으로
{: .text-alpha }

## 한 문장 요약

Glimepiride는 설포닐우레아 계열 약물로, 한국에서 허가된 단일 성분 제제가 다수 유통되고 있습니다. 다만 이번 자료에는 허가 적응증의 본문 텍스트가 포함되어 있지 않아 구체적인 허가 적응증은 확인할 수 없습니다.
TxGNN 모델은 **고전형 전신 경직 증후군(Classic Stiff Person Syndrome)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문이 자료에 없음) |
| 예측 신규 적응증 | 고전형 전신 경직 증후군 |
| TxGNN 예측 점수 | 0.9975 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 최소 20건 (목록이 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 glimepiride는 췌장 베타세포의 KATP 채널을 차단해 인슐린 분비를 촉진하는 설포닐우레아 계열로 알려져 있으나, 이번 자료에서는 확인되지 않았습니다.

전신 경직 증후군은 자가면역 질환으로, 항 GAD65 항체와 관련이 있으며 제1형 당뇨병과 자주 동반됩니다. 따라서 이번 예측은 당뇨병 및 GAD 관련 유전자와의 네트워크상 근접성을 반영했을 가능성이 높습니다. 치료 기전에 근거한 것으로 보기는 어렵습니다.

설포닐우레아의 KATP 채널 차단이 GABA 신경전달 결핍이나 근육 경직을 개선한다는 근거는 알려져 있지 않습니다. 같은 점수(0.9975)를 보이는 국소 경직 사지 증후군(focal stiff limb syndrome)도 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성이 반영된 결과일 수 있으며, 생물학적 근거는 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

아래는 자료에 포함된 허가 중 일부이며, 전체 목록이 아닐 수 있습니다. 모두 단일 성분 제제로 분류되어 있습니다. 허가 적응증 칸에는 본문 대신 허가 문서 링크만 제공되어 있어 내용을 기재하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202000415 | 그루리스정4밀리그램 | 정제 | 허가 문서 참조 |
| 200402623 | 그리메피드정1밀리그램 | 정제 | 허가 문서 참조 |
| 201903394 | 베아릴정1밀리그램 | 정제 | 허가 문서 참조 |
| 201603555 | 뉴글리필드정2밀리그램 | 정제 | 허가 문서 참조 |
| 200300409 | 유글렉스정2밀리그램 | 정제 | 허가 문서 참조 |

## 안전성 고려사항

- **금기(지식 그래프 기반)**: 아래는 허가 문서가 아니라 TxGNN 지식 그래프의 약물-질병 금기 관계이며, 허가사항으로 확인된 내용은 아닙니다. 신장 질환, 간 질환, 담낭 질환, 울혈성 심부전, 뇌하수체 기능저하증(성장호르몬 결핍 및 저성선자극호르몬성 성선기능저하증 포함), 골다공증, 흉선 질환, 감염성 질환 등이 기록되어 있습니다.
- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 이 중 20건이 제공되었습니다. 대부분 중등도입니다.
  - 중등도: phenylephrine, acebutolol, acetazolamide, famotidine, ranitidine, acitretin, formoterol, pseudoephedrine, ketorolac, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, albiglutide, salbutamol, ethanol, nitazoxanide, hydrochlorothiazide
  - 경미: 국소 hydrocortisone, 국소 alclometasone

허가사항의 경고 및 주의사항은 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
전신 경직 증후군에 대한 임상시험과 문헌이 없고, 기전상 연결고리도 확인되지 않습니다. 높은 TxGNN 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성이 반영된 결과일 수 있으며, 생물학적 근거는 아닙니다. 같은 모델이 예측한 다른 후보(국소 경직 사지 증후군, 지방이영양증 계열, 췌장 무발생 등)도 모두 L5 수준이며, 췌장 무발생은 잔존 베타세포가 없어 기전상 효과를 기대하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가 적응증과 경고·금기를 확인하기 위한 허가사항 본문 확보
- 작용 기전(MOA) 데이터 보강
- 전신 경직 증후군과 glimepiride를 연결하는 전임상 또는 임상 근거 탐색
- 근거 확보 전까지는 추가 투자 없이 보류
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

