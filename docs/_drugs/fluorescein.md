---
layout: default
title: Fluorescein
parent: 모델 예측만 (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluorescein: 예측 신규 적응증 Prinzmetal 협심증 (Prinzmetal angina) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 제공되지 않았고 허가증 링크만 확인됩니다 (식약처 의약품안전나라 허가 문서 참조)"
monitor_inn: "Fluorescein"
predicted_indications: ["Prinzmetal angina", "antithrombin deficiency type 2", "rheumatoid arthritis", "factor 5 excess with spontaneous thrombosis", "hemoglobinopathy", "heparin cofactor 2 deficiency", "thrombophilia", "hyperthyroidism", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
---

# Fluorescein
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

## Fluorescein: 진단 목적 사용에서 Prinzmetal 협심증으로 (예측)
{: .text-alpha }

## 한 문장 요약

Fluorescein(플루오레세인나트륨)은 주사용 진단 형광 색소로, 한국에서는 한국알콘의 주사제로 허가되어 시판 중입니다. TxGNN 모델은 **Prinzmetal 협심증(Prinzmetal angina)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 이 예측은 모델 점수에만 근거하며 기전상의 근거가 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 제공되지 않았고 허가증 링크만 확인됩니다 (식약처 의약품안전나라 허가 문서 참조) |
| 예측 신규 적응증 | Prinzmetal 협심증 (Prinzmetal angina) |
| TxGNN 예측 점수 | 0.9981 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Fluorescein은 진단용 형광 색소이며, 혈관확장 작용이나 항경련(anti-vasospastic) 작용은 알려져 있지 않습니다.

Prinzmetal 협심증은 관상동맥 경련으로 생기는 질환입니다. 기존 용도(진단용 색소)와의 약리학적 연관성은 확인되지 않았습니다. 따라서 높은 TxGNN 점수(0.9981)는 TxGNN 모델(딥러닝)이 관련 질환 사이에서 학습한 유사성을 반영할 뿐, 생물학적 근거나 기전상 타당성을 뒷받침하지 않습니다.

참고로 상위 10개 예측(항트롬빈 결핍 2형, 류마티스 관절염, 제5인자 과다, 혈색소병증, 헤파린 보조인자 2 결핍, 혈전성향증, 갑상선기능항진증, 16번 염색체 단완 부분 결손, 베타 지중해빈혈 등) 모두 같은 한계를 보입니다. 일부 항목에서 검색된 문헌은 fluorescein을 **치료제가 아니라 진단 도구**(각막 염색, 형광 안저 혈관조영)로 사용한 연구였습니다. 이는 치료 효과의 근거가 되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200511259 | 후루오레사이트주사10%(플루오레세인나트륨)(바이알) | 주사제 (무색 유리 바이알에 충전된 적색 용액) | 허가 적응증 본문 미제공 (허가증 문서 참조) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Prinzmetal 협심증에 대한 임상시험과 문헌이 없고, 기전상 근거도 없습니다. 예측은 모델 점수에만 의존합니다. 상위 10개 예측도 모두 L4~L5 수준이며, 문헌이 있는 경우에도 진단 목적 사용에 해당해 치료적 재창출 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서)의 적응증, 경고, 금기 정보 확보
- 상세한 약물 작용 기전(MOA) 데이터
- Fluorescein과 관상동맥 경련 사이의 기전적 연관성을 보여주는 전임상 근거
- 투여 경로 적합성 평가 (현재 주사제만 허가되어 있음)
- 이 예측을 지지하는 임상시험 또는 치료 효과를 다룬 문헌
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

