---
layout: default
title: Dostarlimab
parent: 모델 예측만 (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dostarlimab: 예측 신규 적응증 신생물성 용종 (Neoplastic Polyp) (근거 수준 L5). 기존 적응증: dMMR 재발성·진행성 자궁내막암 및 기타 dMMR 고형암 (한국 허가 적응증 원문은 링크로만 제공되어 확인하지 못함. 약리…"
monitor_inn: "Dostarlimab"
predicted_indications: ["neoplastic polyp", "paraneoplastic syndrome", "sympathetic paraganglioma", "laryngeal neoplasm", "sublingual gland carcinoma", "unilateral hyperactive labyrinth", "malignant endocrine neoplasm", "ovarian neoplasm", "mediastinal germ cell tumor", "urinary system neoplasm"]
---

# Dostarlimab
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

# Dostarlimab: dMMR 자궁내막암에서 신생물성 용종으로

## 한 문장 요약

Dostarlimab은 PD-1 차단 항체로, 원래 미스매치 복구 결핍(dMMR) 재발성·진행성 자궁내막암 등 고형암 치료에 사용되었습니다.
TxGNN 모델은 **신생물성 용종(Neoplastic Polyp)**에 효과가 있을 수 있다고 예측했지만, 이 방향을 직접 지지하는 **임상시험은 0건**, **문헌도 0편**입니다.
이 예측은 모델 점수만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | dMMR 재발성·진행성 자궁내막암 및 기타 dMMR 고형암 (한국 허가 적응증 원문은 링크로만 제공되어 확인하지 못함. 약리 자료 기준) |
| 예측 신규 적응증 | 신생물성 용종 (Neoplastic Polyp) |
| TxGNN 예측 점수 | 50% |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Dostarlimab은 PD-1(PDCD1)에 높은 친화력으로 결합하는 인간화 단일클론항체입니다. PD-1과 PD-L1, PD-L2의 상호작용을 모두 억제하여 종양이 면역 감시를 피하지 못하게 합니다. 이 작용 기전은 약리 자료에 근거한 설명이며, 허가사항 기반의 상세 기전 자료는 이번 데이터에 포함되어 있지 않습니다.

dMMR 종양은 돌연변이 부담이 크고 면역 반응에 민감하다고 알려져 있습니다. 이 때문에 dMMR 용종이나 Lynch 증후군 같은 용종증에서 PD-1 차단이 이론적으로 연결될 수 있습니다. 다만 이는 이론적 연결일 뿐입니다. 이를 뒷받침하는 임상시험이나 문헌은 이번 데이터에 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202204498 | 젬퍼리주(도스탈리맙) | 주사제 (바이알) | 허가 적응증 원문은 [MFDS 허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202204498/EE) 참조 |

제조사는 (주)글락소스미스클라인입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 면역치료 (항PD-1 항체). 전통적 세포독성 화학요법제가 아님 |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
신생물성 용종에 대한 예측은 점수(50%)만 있고, 임상시험과 문헌 근거가 전혀 없어 L5 수준입니다. 현재 데이터로는 재창출 타당성을 판단할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항 PDF에서 경고·금기·적응증 원문 확보
- dMMR 용종 및 Lynch 증후군 등 용종증에서의 PD-1 차단 관련 전임상·임상 근거 탐색
- 대상 질환 정의 구체화 (dMMR/MSI-H 여부 등 바이오마커 기준)

**참고:** 같은 약물의 다른 예측 적응증 중에는 근거가 더 충분한 것이 있습니다. 난소 종양은 niraparib 병용 Phase 3 임상시험이 있어 L1 수준이며, 별도의 평가를 권장합니다. 후두 종양과 비뇨기계 종양은 초기 임상시험 수준(L3)입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

