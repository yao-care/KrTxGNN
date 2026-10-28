---
layout: default
title: Procyclidine
parent: 모델 예측만 (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
monitor_inn: "Procyclidine"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "transaldolase deficiency", "progressive supranuclear palsy-corticobasal syndrome", "paralysis agitans, juvenile, of Hunt", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "fructose-1,6-bisphosphatase deficiency"]
last_modified_at: 2026-10-23
description: "Procyclidine: 예측 신규 적응증 라스무센 아급성 뇌염 (근거 수준 L5). 기존 적응증: 허가 적응증 본문을 확인할 수 없음 (허가 문서 링크만 제공됨)"
---

# Procyclidine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Procyclidine: 기존 허가 적응증에서 라스무센 아급성 뇌염으로
{: .text-alpha }

## 한 문장 요약

Procyclidine은 중추 작용 무스카린 길항제(항콜린제)로, 한국에서 단일 성분 제제 3건이 허가되어 있습니다. 다만 이번 보고서에 정리된 허가 자료에는 적응증이 문서 링크로만 제공되어 구체적인 허가 적응증 문구를 확인할 수 없었습니다.
TxGNN 모델은 **라스무센 아급성 뇌염(Rasmussen subacute encephalitis)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0건**으로 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문을 확인할 수 없음 (허가 문서 링크만 제공됨) |
| 예측 신규 적응증 | 라스무센 아급성 뇌염 |
| TxGNN 예측 점수 | 0.9974 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 3건 (모두 단일 성분 제제, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 procyclidine은 중추 신경계에서 무스카린 수용체를 차단하는 항콜린제로 알려져 있으나, 이번 자료에는 공식 기전 정보가 포함되어 있지 않습니다.

라스무센 뇌염은 난치성 발작을 동반하는 만성 면역 매개 국소 뇌염입니다. 항콜린 작용이 이 질환의 병태생리를 직접 다룬다고 볼 만한 기전은 확립되어 있지 않습니다. 높은 예측 점수(0.9974)는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아니며, 임상적 뒷받침도 없습니다.

참고로 상위 10개 예측 중 기전상 상대적으로 설득력이 있는 후보는 증상 조절 관점의 **소아기 파킨슨증(paralysis agitans, juvenile, of Hunt)**, **PLA2G6 관련 신경변성**, **진행성 핵상 마비-피질기저핵 증후군**입니다. 이들은 파킨슨증·근긴장이상 증상과 겹치지만, 이 역시 임상 근거는 없는 추측 단계입니다. 특히 비정형 파킨슨증에서는 항콜린제의 효과가 낮고 고령·인지장애 환자에서 내약성이 떨어집니다. ADHD의 경우 항콜린제의 인지·기억 저하 작용이 오히려 주의력을 악화시킬 수 있습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201210742 | 파마프로시클리딘정 (프로시클리딘염산염) | 연한 청색의 타원형 정제 | 허가 문서 링크만 제공됨 (본문 미확인) |
| 201206444 | 영프로마정 (프로시클리딘염산염) | 연한 청색의 타원형 정제 | 허가 문서 링크만 제공됨 (본문 미확인) |
| 199803128 | 프로이머정 (프로싸이클리딘염산염) | 연한 청색의 타원형 정제 | 허가 문서 링크만 제공됨 (본문 미확인) |

## 안전성 고려사항

허가사항의 경고·금기 정보는 확보되지 않았으므로 허가사항을 참조하세요.

**약물 상호작용** (DDInter 기준 총 70건 중 일부):
- **주요(Major)**: 염화칼륨(Potassium chloride), 시트르산칼륨(Potassium citrate)
- **중등도(Moderate)**: 히오시아민, 아트로핀, 글리코피로늄, 디사이클로민, 트로스피움, 메펜졸레이트, 메스코폴라민, 클리디늄 등 다른 항콜린제; 로페라마이드, 모르핀, 오피움, 엘룩사돌린 등 장운동 억제 또는 오피오이드 계열; 드로나비놀, 나빌론; 메토클로프라미드; 프람린타이드

항콜린 작용이 중복되는 약물과의 병용 시 주의가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
라스무센 뇌염에 대한 예측은 모델 점수만 있고 임상시험과 문헌이 전혀 없으며, 기전적 연관성도 확립되어 있지 않습니다. 허가 적응증 본문과 안전성 정보도 확보되지 않아 안전성 1차 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처(MFDS) 허가 문서에서 허가 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전(MOA) 데이터 확보
- 라스무센 뇌염과 항콜린제에 관한 문헌 검토
- 기전상 상대적으로 타당한 소아기 파킨슨증 등 증상 조절 후보에 대한 선별적 문헌 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

