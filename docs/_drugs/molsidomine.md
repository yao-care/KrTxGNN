---
layout: default
title: Molsidomine
parent: 모델 예측만 (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
monitor_inn: "Molsidomine"
predicted_indications: ["alopecia", "vascular disease", "hypotrichosis simplex of the scalp", "arterial thoracic outlet syndrome", "idiopathic spontaneous coronary artery dissection", "venous thoracic outlet syndrome", "visceral calciphylaxis", "neurogenic thoracic outlet syndrome", "hemangioendothelioma", "congenital hypotrichosis milia"]
last_modified_at: 2026-10-23
description: "Molsidomine: 예측 신규 적응증 탈모 (근거 수준 L5). 기존 적응증: 허가 문서가 링크로만 제공되어 허가 적응증 문구를 확인하지 못했습니다. 문헌상으로는 관상동맥질환 치료제로 기술됩니다"
---

# Molsidomine
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

## Molsidomine: 관상동맥질환 치료제에서 탈모로
{: .text-alpha }

## 한 문장 요약

Molsidomine은 체내에서 산화질소(NO)를 방출하는 전구약물로, 문헌에서는 관상동맥질환 치료에 쓰이는 약으로 소개됩니다. TxGNN 모델은 **탈모**에 효과가 있을 수 있다고 예측했지만, 이 방향을 직접 뒷받침하는 **임상시험은 0건, 문헌은 0편**이어서 현재는 모델 예측 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서가 링크로만 제공되어 허가 적응증 문구를 확인하지 못했습니다. 문헌상으로는 관상동맥질환 치료제로 기술됩니다. |
| 예측 신규 적응증 | 탈모 |
| TxGNN 예측 점수 | 1.0000 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 2건 (모두 단일 성분제, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 Molsidomine은 활성 대사체인 linsidomine(SIN-1)을 통해 NO를 방출하는 NO 공여체로 알려져 있습니다. NO는 혈관을 확장시키는 물질입니다.

이론상으로는 NO에 의한 혈관 확장이 두피 혈류를 개선할 수 있습니다. 혈관 확장 작용을 가진 minoxidil이 탈모 치료에 쓰이는 것과 비슷한 발상입니다. 그러나 이 연결은 추정에 불과하며, 이를 뒷받침하는 임상시험이나 문헌이 없습니다. 모델의 높은 예측 점수만으로 효과를 기대하기는 어렵습니다.

## 임상시험 근거

현재 탈모와 관련된 임상시험 등록이 없습니다.

## 문헌 근거

현재 탈모와 관련된 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199802244 | 몰시톤정4밀리그램 (에리슨제약) | 정제 (연분홍색 원형) | 허가 문서 링크만 확인되며 본문은 확인하지 못했습니다 |
| 199501832 | 몰시톤정2밀리그램 (에리슨제약) | 정제 (주황색 원형) | 허가 문서 링크만 확인되며 본문은 확인하지 못했습니다 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
탈모 예측을 뒷받침하는 임상시험과 문헌이 없고 기전 연결도 추정 수준이어서 근거 수준은 L5입니다. 허가 적응증 문구와 안전성 정보도 확인되지 않아 다음 단계로 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가 문서(첨부문서)를 내려받아 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전 데이터 확보
- 두피 혈류, 모낭에 대한 NO 공여체의 작용을 다룬 전임상 또는 임상 연구 탐색
- 참고로, 같은 약물의 두 번째 예측인 혈관질환은 완료된 Phase 4 시험(NCT01363661)과 관련 문헌이 있어 우선 검토할 만한 후보입니다. 다만 기존 사용 범위와 겹치는 부분이 있어 진정한 의미의 재창출인지는 별도로 판단해야 합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

