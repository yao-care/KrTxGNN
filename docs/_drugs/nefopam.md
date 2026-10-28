---
layout: default
title: Nefopam
parent: 모델 예측만 (L5)
nav_order: 540
evidence_level: L5
indication_count: 10
monitor_inn: "Nefopam"
predicted_indications: ["craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "tetanic cataract", "mature cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic cataract", "lumbar spinal stenosis"]
last_modified_at: 2026-10-28
description: "Nefopam: 예측 신규 적응증 두개골 유합증 백내장 (craniostenosis cataract) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201601070/EE"
---

# Nefopam
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

## Nefopam: 중추성 비마약성 진통제 → 두개골 유합증 백내장 (craniostenosis cataract)
{: .text-alpha }

## 한 문장 요약

Nefopam은 세로토닌·노르에피네프린·도파민 재흡수를 억제하는 중추작용 비마약성 진통제입니다.
TxGNN 모델은 **두개골 유합증 백내장(craniostenosis cataract)**에 효과가 있을 수 있다고 예측하지만(예측 점수 0.9998), 이를 직접 뒷받침하는 임상시험이나 문헌은 **0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201601070/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707840/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201704469/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201601358/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201606703/EE;  |
| 예측 신규 적응증 | 두개골 유합증 백내장 (craniostenosis cataract) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 18건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DrugBank에 기록되어 있지 않습니다. 알려진 정보에 따르면 Nefopam은 세로토닌·노르에피네프린·도파민 재흡수를 억제하고 전압의존성 나트륨·칼슘 채널을 조절하는 진통제입니다.

이러한 작용과 백내장 병태생리를 연결할 만한 타당한 기전은 확인되지 않았습니다. 동일한 점수(0.9998)가 여러 백내장 아형에서 반복되어 나타나므로, 질환 특이적 신호라기보다 모델 구조에서 비롯된 공통 현상일 가능성이 있습니다. 따라서 이 예측은 모델 출력일 뿐 생물학적 근거는 없는 것으로 판단합니다.

## 한국 시판 정보

한국에서는 단일 성분 허가증 18건이 모두 유효합니다. 대부분 주사제(앰플)이며, 캡슐제도 1건 있습니다.

| 허가번호 | 제품명 | 제형 | 제조사 |
|---------|------|------|------|
| 201601070 | 명문네포팜염산염주 | 앰플 주사제 | 명문제약(주) |
| 201707840 | 페인솔루주 | 앰플 주사제 | 유니메드제약(주) |
| 201704469 | 네포큐어주 | 앰플 주사제 | 한화제약(주) |
| 201601358 | 네프콤주사액 | 앰플 주사제 | (주)경보제약 |
| 201205549 | 올페인캡슐 | 경질캡슐 | (주)한국팜비오 |

허가 적응증 문구는 이번 데이터에 텍스트로 포함되어 있지 않습니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측된 두개골 유합증 백내장에 대한 임상시험과 문헌이 없고, 기전상 연관성도 확인되지 않아 근거 수준은 L5입니다. 모델 점수만으로 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 약물 작용 기전(MOA) 상세 데이터 확보
- 허가사항의 경고·금기·적응증 원문 확인
- 이 질환 또는 수정체 혼탁에 대한 전임상·기전 연구 근거
- 백내장 아형에서 동일 점수가 반복되는 원인 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

