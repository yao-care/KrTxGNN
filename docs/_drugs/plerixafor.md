---
layout: default
title: Plerixafor
parent: 모델 예측만 (L5)
nav_order: 608
evidence_level: L5
indication_count: 6
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
last_modified_at: 2026-11-20
description: "Plerixafor: 예측 신규 적응증 CMM7 (근거 수준 L5). 기존 적응증: 성인 (만18세 이상) : G-CSF와 병용하여, 비호지킨림프종 또는 다발골수종 성인 환자의…"
---

# Plerixafor
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Plerixafor: CXCR4 길항제 → CMM7 (CMM7)
{: .text-alpha }

## 한 문장 요약

Plerixafor는 CXCR4 수용체를 차단하는 조혈모세포 동원제 계열의 주사제입니다.
TxGNN 모델은 **CMM7(CMM7)**에 효과가 있을 수 있다고 예측했지만, 이 질환명은 의미가 모호해 정확한 질환으로 특정하지 못했습니다.
현재 이 예측을 직접 지지하는 **임상시험은 0건**, **문헌은 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 성인 (만18세 이상) : G-CSF와 병용하여, 비호지킨림프종 또는 다발골수종 성인 환자의 자가조혈모세포이식과 조혈모세포 채집시 말초혈액으로 조혈모세포의 가동화 증진 소아 (만1세 ~ 만18세 미만) : 아래와 같은 경우의 림프종 또는 고형악성종양 소아 환자의 자가조혈모세포이식과… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201000845/EE)) |
| 예측 신규 적응증 | CMM7 (CMM7) |
| TxGNN 예측 점수 | 0.9934 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Plerixafor 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “플레릭사포르는 CXCR4 케모카인 수용체의 억제제이며, 그 동족 리간드인 기질세포 유래 인자-1α(SDF-1α)의 결합을 차단한다. SDF-1α와 CXCR4는 인간 조혈모세포(HSC)의 골수 구획으로의 이동(trafficking) 및 귀소(homing)에 관여하는 것으로 알려져 있다.” 영어 원문: "Plerixafor is an inhibitor of the CXCR4 chemokine receptor and blocks binding of its cognate ligand, stromal cell-derived factor-1α (SDF-1α). SDF-1α and CXCR4 are recognized to play a role in the trafficking and homing of human hematopoietic stem cells (HSCs) to the marrow compartment." ([DailyMed: Mozobil (plerixafor) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ed08d2b-5051-46b2-aa37-1d6275bf9003), 버전 2025-09-22; 확인일 2026-11-19). 다만 약리학 데이터에 따르면 plerixafor는 CXCR4와 ACKR3를 표적으로 하며, CXCR4–CXCL12 결합을 방해하는 것으로 알려져 있습니다.

'CMM7'은 흑색종 관련 항목일 가능성이 언급되나, 정의된 질환으로 연결되지 않았습니다. 검색된 임상시험과 문헌이 없어 모델 예측 외에 기전적 연결고리를 확립할 수 없습니다. 추가 검토 전에 질환의 정체부터 명확히 해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201000845 | 모조빌주 | 무색~미황색의 투명한 액이 든 바이알 주사제 | 허가 적응증 텍스트가 문서 링크로만 제공됨 |
| 202303176 | 모빌리아주 | 무색~미황색의 투명한 액이 든 바이알 주사제 | 허가 적응증 텍스트가 문서 링크로만 제공됨 |

## 안전성 고려사항

- **약물 상호작용**: 약리학 데이터상 CXCR4와 ACKR3 수용체가 표적으로 확인되었으며, 등급이 부여된 약물 간 상호작용은 없습니다.

그 외 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
CMM7은 질환 정의가 모호하고, 이를 뒷받침하는 임상시험이나 문헌이 없어 모델 예측만 있는 상태(L5)입니다.

**진행하려면 필요한 것:**
- CMM7이 가리키는 질환의 명확한 정의 및 식별
- 해당 질환에 대한 전임상 또는 임상 연구 근거
- 허가사항(경고, 금기) 확인 및 작용 기전 데이터 보완

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Mozobil (plerixafor) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0ed08d2b-5051-46b2-aa37-1d6275bf9003) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

