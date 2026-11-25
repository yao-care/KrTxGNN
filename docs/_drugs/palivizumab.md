---
layout: default
title: Palivizumab
parent: 모델 예측만 (L5)
nav_order: 576
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Palivizumab: 예측 신규 적응증 설소 양성 종양 (benign neoplasm of tongue) (근거 수준 L5). 기존 적응증: RSV질환에 대한 위험이 높은 소아에서 RSV(Respiratory Syncytial Virus)로 인해…"
monitor_inn: "Palivizumab"
predicted_indications: ["benign neoplasm of tongue", "epiglottis neoplasm", "cervical neuroblastoma", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "tumor of testis and paratestis", "cystic neoplasm", "schwannoma of jugular foramen", "mesenchymoma", "thyroglossal duct cyst"]
---

# Palivizumab
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

## Palivizumab: RSV 예방에서 설소 양성 종양(Benign Neoplasm of Tongue)으로
{: .text-alpha }

## 한 문장 요약

Palivizumab은 RSV(호흡기세포융합바이러스)의 F 단백질을 표적으로 하는 인간화 단일클론항체로, 한국에서 시나지스주사액으로 시판되고 있습니다.
TxGNN 모델은 **설소 양성 종양(benign neoplasm of tongue)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 예측은 모델 계산에만 근거합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | RSV질환에 대한 위험이 높은 소아에서 RSV(Respiratory Syncytial Virus)로 인해 입원이 필요한 심각한 하기도 질환의 예방 - 재태 기간 35주 이하로 태어나고 RSV 계절 시작시점에 생후 6개월 이하인 소아 - 최근 6개월 이내에… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605448/EE)) |
| 예측 신규 적응증 | 설소 양성 종양 (benign neoplasm of tongue) |
| TxGNN 예측 점수 | 0.9994 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Palivizumab의 작용 기전(비공식 번역): “융합 당단백질 F0 억제제”. 영어 원문: "Fusion glycoprotein F0 inhibitor" ([ChEMBL CHEMBL1201586 (palivizumab): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1201586), CC BY-SA 3.0; 확인일 2026-11-19). 알려진 정보에 따르면 Palivizumab은 RSV F 단백질에 결합해 바이러스를 중화하는 단일클론항체입니다.

설소 양성 종양에는 RSV와 관련된 병리나 F 단백질 표적이 알려져 있지 않습니다. 따라서 이 약이 효과를 내려면 아직 확인되지 않은 비표적(off-target) 기전이 필요합니다. 높은 TxGNN 점수(0.9994)는 계산상의 예측일 뿐이며, 기전상 타당성을 입증하지 못합니다.

같은 모델이 예측한 다른 후보(상위 10건: 후두개 신생물, 경부 신경모세포종, 하인두 양성 종양, 구강저 양성 종양, 고환 및 부고환 종양, 낭성 신생물, 경정맥공 신경초종, 중간엽종, 갑상설관 낭종)도 모두 마찬가지로 기전적 연관성이 확인되지 않았고 임상시험·문헌 근거가 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201605448 | 시나지스주사액50밀리그램(팔리비주맙) | 투명 내지 약간의 유백색의 액이 무색투명한 바이알에 든 주사제 | 한국아스트라제네카(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605448/EE) | 유효 |
| 201605447 | 시나지스주사액100밀리그램(팔리비주맙) | 투명 내지 약간의 유백색의 액이 무색투명한 바이알에 든 주사제 | 한국아스트라제네카(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605447/EE) | 유효 |

<!-- licenses:end -->

두 제품 모두 한국아스트라제네카(주)가 허가를 보유하고 있습니다(허가 건수와 상태는 빠른 개요와 위 표 참조).

<!-- review:begin kr-lic-20261124c-palivizumab-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “두 제품 모두 한국아스트라제네카(주)가 허가를 보유한 단일제이며 유효 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-palivizumab-1 -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 매우 높지만 임상시험과 문헌 근거가 전혀 없고(L5), 항RSV 항체와 해당 질환 사이에 확인된 기전적 연관성도 없습니다. 현재로서는 재창출을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증)의 확인 및 정리
- 상세한 작용 기전(MOA) 데이터 확보
- 설소 양성 종양과 RSV F 단백질 또는 다른 표적 사이의 기전적 연관성에 대한 전임상 근거
- 관련 임상시험 또는 문헌 근거 (현재 없음)
- 투여 경로 적합성 평가 (현재 미평가)

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [ChEMBL CHEMBL1201586 (palivizumab): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1201586) |
| 2026-11-24 | 단일·복합 표기: “두 제품 모두 한국아스트라제네카(주)가 허가를 보유한 단일제이며 유효 상…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

