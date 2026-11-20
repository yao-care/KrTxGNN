---
layout: default
title: Trifarotene
parent: 모델 예측만 (L5)
nav_order: 763
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-15
description: "Trifarotene: 예측 신규 적응증 혈장 아연 상승 (zinc, elevated plasma) (근거 수준 L5). 기존 적응증: 만 9세 이상에서 면포, 구진, 농포가 나타나는 중등도 여드름의 국소치료(얼굴 또는 몸통)"
monitor_inn: "Trifarotene"
predicted_indications: ["zinc, elevated plasma", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome"]
---

# Trifarotene
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Trifarotene: 여드름에서 혈장 아연 상승으로
{: .text-alpha }

## 한 문장 요약

Trifarotene은 선택적 레티노산 수용체 감마(RAR-γ) 작용제로, 원래 여드름 치료용 국소 크림으로 사용되었습니다.
TxGNN 모델은 **혈장 아연 상승(zinc, elevated plasma)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만 9세 이상에서 면포, 구진, 농포가 나타나는 중등도 여드름의 국소치료(얼굴 또는 몸통) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202103414/EE)) |
| 예측 신규 적응증 | 혈장 아연 상승 (zinc, elevated plasma) |
| TxGNN 예측 점수 | 0.9940 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Trifarotene 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “트리파로텐은 레티노산 수용체(RAR)의 작용제로, 특히 RAR의 감마 아형에서 활성을 나타낸다. RAR의 자극은 세포 분화 및 염증 매개를 포함한 다양한 과정과 관련된 표적 유전자의 조절을 초래한다.” 영어 원문: "Trifarotene is an agonist of retinoic acid receptors (RAR), with particular activity at the gamma subtype of RAR. Stimulation of RAR results in modulation of target genes which are associated with various processes, including cell differentiation and mediation of inflammation." ([DailyMed: Aklief (trifarotene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=62d910db-85a6-4696-b69b-4bd2f3080cfc), 버전 2024-09-16; 확인일 2026-11-19). 다만 약리 자료에 따르면 Trifarotene은 레티노산 수용체(RARα, RARβ, RARγ)와 상호작용하며, 특히 RAR-γ 작용제로 알려져 있습니다. 피부 모낭 각질화와 염증을 조절하여 여드름에 사용됩니다. 대사 안정성이 매우 낮아 국소 사용 시 전신 노출이 제한적일 것으로 보입니다.

반면 혈장 아연 상승은 피부 질환이 아닌 생화학적 이상 소견입니다. RAR-γ 신호전달이 이를 교정한다는 그럴듯한 기전적 연결고리는 확인되지 않았습니다. 따라서 TxGNN 점수(0.9940)는 TxGNN 모델(딥러닝)이 산출한 계산적 예측일 뿐이며, 관련 질환 간에 모델이 학습한 유사성을 반영할 수 있으나 생물학적 근거는 아니고, 치료적 타당성은 뒷받침되지 않습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202103414 | 아크리프크림0.005%(트리파로텐), 갈더마코리아(주) | 흰색~미황색의 크림 | 허가증 문서 링크로만 제공됨 ([MFDS 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202103414/EE)) |

## 안전성 고려사항

- **약물 상호작용**: 통상적인 약물 간 상호작용 항목은 확인되지 않았습니다. 약리 자료상 RARα, RARβ, RARγ 세 가지 레티노산 수용체와 상호작용하는 것으로 나타납니다.
- 국소 제제로 전신 노출이 제한적일 것으로 예상되나, 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
혈장 아연 상승에 대한 근거는 TxGNN 예측 점수뿐이며, 임상시험과 문헌이 없고 기전적 연결고리도 확인되지 않습니다. 또한 혈장 아연 상승은 국소 피부 도포제의 치료 대상으로 적합하지 않습니다. 허가 적응증과 안전성 정보(경고·금기)도 확인되지 않아 안전성 검토 단계로 넘어갈 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(경고, 금기, 적응증 본문) 확보 및 분석
- 상세한 작용 기전(MOA) 데이터 확보
- 혈장 아연 상승과 RAR-γ 신호전달 사이의 기전적 연결을 뒷받침하는 전임상 또는 문헌 근거
- 국소 투여 경로로 전신 질환을 다룰 수 있는지에 대한 투여경로 적합성 검토
- 대안으로, 피부 질환 후보(예: 피지선 모낭충증)를 우선 재평가하는 방안 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Aklief (trifarotene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=62d910db-85a6-4696-b69b-4bd2f3080cfc) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

