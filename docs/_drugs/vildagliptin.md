---
layout: default
title: Vildagliptin
parent: 모델 예측만 (L5)
nav_order: 784
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Vildagliptin: 예측 신규 적응증 고전형 강직인간증후군 (Classic Stiff Person Syndrome) (근거 수준 L5). 기존 적응증: 제2형 당뇨병 (허가 문서는 링크로만 제공되어 본문 확인 불가, 약리 데이터의 임상 용도 기준)"
monitor_inn: "VILDAGLIPTIN"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Vildagliptin
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

## Vildagliptin: 제2형 당뇨병에서 고전형 강직인간증후군으로
{: .text-alpha }

## 한 문장 요약

Vildagliptin은 DPP-4 억제제로, 원래 제2형 당뇨병 치료에 사용되었습니다. TxGNN 모델은 **고전형 강직인간증후군(Classic Stiff Person Syndrome)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다. 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 제2형 당뇨병 (허가 문서는 링크로만 제공되어 본문 확인 불가, 약리 데이터의 임상 용도 기준) |
| 예측 신규 적응증 | 고전형 강직인간증후군 (Classic Stiff Person Syndrome) |
| TxGNN 예측 점수 | 0.9988 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 정리되어 있지 않습니다. 약리 데이터에 따르면 Vildagliptin은 DPP-4(dipeptidyl peptidase 4)를 주요 표적으로 하는 억제제이며, DPP8, DPP9, TRPV4와의 상호작용도 보고되어 있습니다. DPP-4 억제는 활성 GLP-1과 GIP를 증가시켜 인슐린 분비를 개선하고 글루카곤 분비를 억제합니다.

강직인간증후군은 GAD65 항체와 관련된 자가면역성 신경계 질환입니다. DPP-4 억제제와 GABA 신경계 기능 이상 사이에는 확립된 기전적 연결고리가 없습니다. 이 점수는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영했을 가능성이 있으며, 생물학적 근거는 아닙니다.

같은 점수(0.9988)를 받은 국소 강직사지증후군(focal stiff limb syndrome)이 함께 예측된 점도 주의할 만합니다. 이는 약물 고유의 생물학보다 질환 분류 체계의 공통 노드에서 예측이 전파되었음을 시사합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

한국에서 총 20건의 허가증이 유효하며(취소 0건), 아래는 주요 5건입니다. 허가 적응증은 본문이 아닌 허가 문서 링크로만 제공됩니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200803516 | 가브스메트정50/850밀리그램 (한국노바티스) | 황색의 타원형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200803516/EE) |
| 201908043 | 에이브스정50밀리그램 (안국약품) | 흰색 내지 밝은 노란빛의 원형 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201908043/EE) |
| 202101225 | 빌다글정50밀리그램 (한미약품) | 흰색 내지 밝은 노란색의 원형 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202101225/EE) |
| 202200347 | 가블리정 (신풍제약) | 흰색 내지 밝은 노란빛의 원형 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202200347/EE) |
| 202302280 | 다야브스메트정50/850밀리그램 (한국휴텍스제약) | 노란색의 타원형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202302280/EE) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
모델 예측 점수만 높을 뿐 임상시험과 문헌이 전혀 없고(L5), DPP-4 억제와 강직인간증후군 사이에 알려진 기전적 연결도 없습니다. 같은 점수의 인접 질환이 함께 예측된 점은 이 신호가 질환 분류 체계에서 비롯된 인공물일 가능성을 시사합니다.

**진행하려면 필요한 것:**
- 강직인간증후군에서 DPP-4 억제 또는 GLP-1 경로가 어떻게 작용하는지 보여주는 기전 연구 또는 전임상 근거
- 허가사항(경고, 금기)의 확보와 안전성 검토
- 상세한 약물 작용 기전(MOA) 데이터 보완
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

