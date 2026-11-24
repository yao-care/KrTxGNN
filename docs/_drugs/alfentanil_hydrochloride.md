---
layout: default
title: Alfentanil Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 37
evidence_level: L5
indication_count: 1
drugbank_id: DB00802
monitor_inn: "Alfentanil"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
last_modified_at: 2026-11-24
description: "Alfentanil Hydrochloride: 예측 신규 적응증 신장성 항이뇨호르몬 부적절 분비 증후군 (nephrogenic syndrome of inappropriate antidiuresis) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Alfentanil Hydrochloride
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Alfentanil Hydrochloride: 신장성 항이뇨호르몬 부적절 분비 증후군 (nephrogenic syndrome of inappropriate antidiuresis)
{: .text-alpha }

## 한 문장 요약

Alfentanil(알펜타닐염산염)은 주사제로 한국에 시판 중인 오피오이드 계열 약물입니다. TxGNN 모델은 **신장성 항이뇨호르몬 부적절 분비 증후군(nephrogenic syndrome of inappropriate antidiuresis)**에 효과가 있을 수 있다고 예측했지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 근거는 모델 예측 점수뿐이며, 기전상으로는 오히려 증상을 악화시킬 가능성이 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201305911/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199806838/EE) |
| 예측 신규 적응증 | 신장성 항이뇨호르몬 부적절 분비 증후군 (nephrogenic syndrome of inappropriate antidiuresis) |
| TxGNN 예측 점수 | 0.9951 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 정리되어 있지 않습니다. Alfentanil은 일반적으로 뮤(μ) 오피오이드 수용체 작용제로 알려져 있습니다.

신장성 항이뇨호르몬 부적절 분비 증후군(NSIAD)은 바소프레신 V2 수용체(AVPR2)의 기능획득 변이(예: R137C, R137L)로 발생합니다. 수용체가 지속적으로 활성화되어, 바소프레신 분비가 억제되어 있는데도 수분이 저류되고 저나트륨혈증이 나타납니다. 오피오이드가 항이뇨호르몬 분비와 신장의 수분 처리에 영향을 줄 수 있다는 점에서 연결 고리를 추정해 볼 수는 있습니다. 그러나 이 경로는 수용체의 상위 단계에서 작용합니다. NSIAD는 바소프레신 분비와 무관한 수용체 수준의 결함이므로 이 경로로는 교정되지 않습니다.

뮤 오피오이드 작용제는 항이뇨 작용과 저나트륨혈증(SIADH 유사 효과)을 유발하는 것으로 알려져 있어, 치료보다는 증상 악화 쪽의 효과 방향이 우려됩니다. 따라서 이 예측은 바소프레신/GPCR 경로에서 모델이 공유 이웃을 찾아낸 결과일 가능성이 높으며, 입증된 치료 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201305911 | 알페닐주사(알펜타닐염산염)(바이알) | 무색 투명한 액이 든 갈색 바이알제 | 대원제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201305911/EE) | 유효 |
| 199806838 | 하나알펜타닐주사 | 무색투명한 액이 든 갈색 투명한 앰플제 | 하나제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199806838/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측을 지지하는 임상시험과 문헌이 없어 근거 수준은 L5입니다. 뮤 오피오이드 작용제의 항이뇨 및 저나트륨혈증 유발 특성을 고려하면 NSIAD에서는 치료 효과보다 증상 악화 가능성이 더 큽니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 및 바소프레신 경로와의 관계 검토
- 허가사항(경고, 금기)의 확인 및 분석
- NSIAD 또는 관련 저나트륨혈증 모델에서 alfentanil의 영향을 평가하는 전임상 자료
- 효과 방향(치료 대 악화)에 대한 독립적인 문헌 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-05 | 삭제: “한국 허가 이력이 없으며” | 보고서가 다시 생성되어 이 문장이 없음(2026-11-16: 2026년 11월 16일 보고서가 새 예측(DrugBank ID로 찾은 TxGNN 예측)으로 다시 생성되어 이 문장이 더 이상 없음; 원래: 정정) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

