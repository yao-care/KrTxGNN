---
layout: default
title: Miglitol
parent: 모델 예측만 (L5)
nav_order: 515
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Miglitol: 예측 신규 적응증 고전형 강직인간증후군 (Classic Stiff Person Syndrome) (근거 수준 L5). 기존 적응증: 2형 당뇨병 (허가 적응증 원문은 링크로만 제공되어 세부 문구는 확인하지 못함)"
monitor_inn: "MIGLITOL"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pancreatic agenesis", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Miglitol
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

## Miglitol: 2형 당뇨병에서 고전형 강직인간증후군으로
{: .text-alpha }

## 한 문장 요약

Miglitol은 장관 알파-글루코시다제 억제제로, 한국에서 당뇨병 치료제로 시판되고 있습니다. TxGNN 모델은 **고전형 강직인간증후군(Classic Stiff Person Syndrome)**에 효과가 있을 수 있다고 예측했습니다. 그러나 이 방향을 지지하는 **임상시험은 0건, 문헌도 0건**이며, 기전상 타당성도 낮습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 2형 당뇨병 (허가 적응증 원문은 링크로만 제공되어 세부 문구는 확인하지 못함) |
| 예측 신규 적응증 | 고전형 강직인간증후군 (Classic Stiff Person Syndrome) |
| TxGNN 예측 점수 | 0.9987 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 8건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 다만 Miglitol은 장관의 알파-글루코시다제를 억제하여 탄수화물 소화와 흡수를 늦추고, 식후 혈당 상승을 줄이는 약물로 알려져 있습니다. 전신 흡수도 거의 되지 않습니다.

강직인간증후군은 항-GAD65 항체와 GABA 신호 이상이 관여하는 자가면역성 신경계 질환입니다. 장관에서 국소적으로 작용하는 Miglitol과는 약리학적 연결고리가 뚜렷하지 않습니다. 중추신경계에 작용한다고 보기도 어렵습니다.

점수는 TxGNN 모델(딥러닝)이 산출한 것이며, 직접적인 약리 기전보다 모델이 관련 질환 사이에서 학습한 유사성을 반영한 결과일 가능성이 큽니다. 생물학적 근거는 아닙니다. 예를 들어 당뇨병 동반질환이나 GAD 자가면역과 얽힌 질환 간 유사성이 원인일 수 있습니다. 같은 점수(0.9987)를 받은 국소 강직사지증후군(Focal Stiff Limb Syndrome)도 같은 이유일 수 있습니다. 따라서 이 예측은 임상적으로 활용하기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

허가증은 총 8건이며, 아래는 주요 5건입니다. 허가 적응증은 허가사항 원문 링크로만 제공되어 요약하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202501983 | 미그린정 (케이엠에스제약) | 분홍색의 원형 필름코팅정 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501983/EE) 참조 |
| 201306313 | 미그보스필름코팅정 (대원제약) | 흰색의 원형 필름코팅정 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201306313/EE) 참조 |
| 202502113 | 미그씬정 (조아제약) | 분홍색의 원형 필름코팅정 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202502113/EE) 참조 |
| 202501984 | 미그스타정 (일화) | 분홍색의 원형 필름코팅정 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501984/EE) 참조 |
| 202600199 | 제이리톨정 (제이더블유중외제약) | 흰색 또는 미황색의 원형 필름코팅정 | [허가사항 원문](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600199/EE) 참조 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 보고서에 반영하지 못했으므로, 허가사항을 직접 참조하세요.

- **지식그래프 기반 금기 질환** (허가 문구가 아닌 모델 지식그래프의 약물-질환 관계): 신장질환, 요관축농증, 염증성 장질환, 감염성 질환, 궤양성 대장염, 저혈당, 외상
- **약물 상호작용**: 총 100건이 조회되었으며, 아래는 그중 일부입니다.
  - **중등도**: Phenylephrine, Acetazolamide, Formoterol, Pseudoephedrine, Epinephrine, Ethinylestradiol, Estradiol, Hydrocortisone, Salbutamol, Hydrochlorothiazide, Alpelisib, Aripiprazole, Triamcinolone, Asenapine, Asparaginase, Ethanol
  - **경미**: Ranitidine, Hydrocortisone(국소), Alclometasone(국소)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고전형 강직인간증후군에 대한 임상시험과 문헌이 전혀 없고, 기전상 연결도 불분명하며, 약물이 전신으로 거의 흡수되지 않습니다. 모델 점수는 매우 높지만 실제 근거는 L5 수준입니다.

**참고:** 같은 약물의 다른 예측 중 1형 당뇨병은 Miglitol과 인슐린 병용에 대한 완료된 Phase 3 공개 시험(NCT00213109)과 여러 소규모 임상 문헌이 있습니다. 다만 공개 라벨 설계이고 참여자 수가 보고되지 않았으며 대부분 오래된 소규모 연구입니다. 재창출 후보로 검토한다면 이쪽이 더 현실적입니다.

**진행하려면 필요한 것:**
- 강직인간증후군과 Miglitol을 잇는 기전적 가설과 전임상 근거
- Miglitol의 상세 작용 기전 데이터 확보
- 허가사항의 경고, 금기 정보 확보와 안전성 검토
- 현재 근거만으로는 임상 개발 진행을 권장하지 않음
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

