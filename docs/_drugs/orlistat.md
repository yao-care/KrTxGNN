---
layout: default
title: Orlistat
parent: 모델 예측만 (L5)
nav_order: 566
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Orlistat: 예측 신규 적응증 비타민 과잉증 (Hypervitaminosis) (근거 수준 L5). 기존 적응증: 체질량지수(BMI) 30 kg/m² 이상 또는 다른 위험인자(예, 고혈압, 당뇨, 이상지질혈증)가 있는…"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
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

## Orlistat: 비만에서 비타민 과잉증으로
{: .text-alpha }

## 한 문장 요약

Orlistat은 위장관 및 췌장 리파제를 억제하여 식이 지방 흡수를 줄이는 약으로, 한국에서 비만 치료제로 허가·시판되고 있습니다.
TxGNN 모델은 **비타민 과잉증(Hypervitaminosis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험과 문헌은 각각 0건**입니다. 예측 점수는 높지만 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 체질량지수(BMI) 30 kg/m² 이상 또는 다른 위험인자(예, 고혈압, 당뇨, 이상지질혈증)가 있는 27 kg/m² 이상의 비만환자에 있어 저칼로리 식이와 함께 체중감소 또는 체중유지를 포함한 비만치료 또는 체중 재증가의위험감소 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202008845/EE)) |
| 예측 신규 적응증 | 비타민 과잉증 (Hypervitaminosis) |
| TxGNN 예측 점수 | 0.9942 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Orlistat 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “올리스타트는 위장관 리파아제의 가역적 억제제이다. 올리스타트는 위 및 췌장 리파아제의 활성 세린 잔기 부위와 공유 결합을 형성함으로써 위 및 소장 내강에서 치료 활성을 나타낸다.” 영어 원문: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), 버전 2026-09-30; 확인일 2026-11-19). 알려진 정보에 따르면 Orlistat은 위장관 및 췌장 리파제 억제제로, 식이 지방 흡수를 약 30% 줄입니다. 지용성 비타민(A, D, E, K)은 식이 지방과 함께 흡수되므로, 이론적으로는 이들 비타민의 흡수도 감소합니다. 이것이 지용성 비타민 과잉을 줄일 수 있다는 가설의 근거입니다.

다만 이 가설은 Orlistat의 이미 알려진 효과와 방향이 반대입니다. Orlistat은 오히려 지용성 비타민 결핍 위험이 있어 종합비타민 보충이 권고됩니다. 높은 TxGNN 점수(0.9942)는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 뿐 생물학적 근거가 아니며 임상 근거로 뒷받침되지 않습니다.

실제 적용은 지용성 비타민(A, D 등) 과잉이 경미하고 드문 경우로 제한될 것입니다. 이런 경우에도 보충제 중단, 식이 조절, 중증 비타민 D 중독 시 수액·글루코코르티코이드·비스포스포네이트 같은 기존 치료가 우선입니다. Orlistat을 쓰면 위장관 부작용과 다른 지용성 비타민 결핍 위험이 따릅니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202008845 | 리피스림캡슐60밀리그램(오르리스타트) | 흰색 또는 미백색의 분말 또는 과립이 든 상, 하부 노란색의 경질캡슐제 | 주식회사 노바엠헬스케어 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202008845/EE) | 유효 |
| 202000480 | 올다운캡슐120밀리그램(오르리스타트) | 백색 또는 미백색의 분말 또는 과립이 든 상, 하부 청록색의 경질캡슐 | (주)휴비스트제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202000480/EE) | 유효 |
| 200903409 | 리피다운캡슐120밀리그램(오르리스타트) | 흰색 내지 연한노란색의 펠렛이 든 청록색의 경질캡슐제 | 한미약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200903409/EE) | 유효 |
| 201000300 | 마이다운캡슐60밀리그램(오르리스타트) | 내수용: 흰색 또는 미백색의 분말 또는 과립이 든 상, 하부 노란색의 경… | (주)제뉴파마 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201000300/EE) | 유효 |
| 202204145 | 제로비정120밀리그램(오르리스타트) | 청록색의 장방형 필름코팅정 | 대한뉴팜(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202204145/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

위 표는 허가 중 5건만 나열한 것입니다(허가 건수와 상태는 빠른 개요 참조).

<!-- review:begin kr-lic-20261124c-orlistat-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “위 표는 전체 20건 중 5건만 나열한 것이며, 20건 모두 단일 성분제로 유효 상태입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-orlistat-1 -->

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 총 100건의 상호작용이 확인되었으며, 대부분 중등도(Moderate)입니다. 주요 항목은 다음과 같습니다.
  - 당뇨병 치료제: acarbose, albiglutide, alogliptin, metformin, canagliflozin, chlorpropamide
  - 항바이러스제(HIV): abacavir, lamivudine, atazanavir, emtricitabine
  - 심혈관계: amiodarone
  - 항암제 및 관련 약물: asparaginase(E. coli 및 Erwinia chrysanthemi 제제), brentuximab vedotin, calaspargase pegol, clofarabine
  - 기타: cannabidiol
  - 경미(Minor) 수준: 비타민 D 계열(cholecalciferol, calcifediol, calcitriol)
- **지식 그래프상 금기 관련 질환**: 간부전, 원발성 고옥살산뇨증, 신경성 식욕부진증, 신경성 폭식증, 비타민 결핍 질환, 담즙정체증(양성 재발성 및 가족성 간내 담즙정체 포함), 약물 유발 간손상. 이는 허가사항 문구가 아닌 지식 그래프의 약물-질환 연결 정보입니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
비타민 과잉증에 대한 임상시험과 문헌이 없고 근거 수준은 L5(모델 예측만 존재)입니다. 또한 Orlistat의 알려진 효과(지용성 비타민 결핍 위험)와 방향이 상충하며, 기존 치료법이 이미 확립되어 있습니다.

**진행하려면 필요한 것:**
- 허가사항(경고 및 금기) 확보: 식약처 허가 문서를 내려받아 분석
- 작용 기전(MOA) 데이터 보완: DrugBank 조회
- 지용성 비타민 과잉 환자에서의 효과와 다른 비타민 결핍 위험을 평가하는 전임상 또는 소규모 탐색 연구 근거
- 기존 치료 대비 Orlistat의 이점을 입증할 비교 근거

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |
| 2026-11-24 | 단일·복합 표기: “위 표는 전체 20건 중 5건만 나열한 것이며, 20건 모두 단일 성분제…” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

