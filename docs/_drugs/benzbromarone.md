---
layout: default
title: Benzbromarone
parent: 모델 예측만 (L5)
nav_order: 136
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Benzbromarone: 예측 신규 적응증 신성 저요산혈증 (Hypouricemia, renal) (근거 수준 L5). 기존 적응증: 다음의 경우에 있어서 고요산혈증의 개선 1. 통풍 2. 고요산혈증을 수반한 고혈압증"
monitor_inn: "BENZBROMARONE"
predicted_indications: ["hypouricemia, renal"]
---

# Benzbromarone
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

## Benzbromarone: 통풍·고요산혈증에서 신성 저요산혈증으로
{: .text-alpha }

## 한 문장 요약

Benzbromarone은 요산 배설을 촉진하는 약물(uricosuric)로, 한국에서 정제로 허가되어 시판 중입니다(허가 건수와 상태는 빠른 개요 참조).
TxGNN 모델은 **신성 저요산혈증(Hypouricemia, renal)**에 효과가 있을 수 있다고 예측했지만, 이 약은 이미 낮은 혈중 요산을 더 낮출 수 있어 **방향이 맞지 않는 거짓 양성 예측일 가능성이 높습니다.**
현재 임상시험은 없고, 지지 근거로 볼 수 있는 문헌 18편은 대부분 이 약을 진단 검사 도구로 사용한 증례·코호트 보고입니다.

<!-- review:begin kr-lic-20261124c-benzbromarone-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “Benzbromarone은 요산 배설을 촉진하는 약물(uricosuric)로, 한국에서 단일제 정제 2건이 허가되어 시판 중입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 단일·복합 표기와 건수를 본문에 고정해 쓰지 않고, 매주 갱신되는 허가 자료를 반영하는 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 2026-11-25에 식품의약품안전처 품목허가 상세 자료(2026-03)의 주성분명으로 품목별로 다시 확인한 결과, 이 자료에 수록된 허가 품목은 모두 단일 성분 제제입니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-benzbromarone-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음의 경우에 있어서 고요산혈증의 개선 1. 통풍 2. 고요산혈증을 수반한 고혈압증 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199500892/EE)) |
| 예측 신규 적응증 | 신성 저요산혈증 (Hypouricemia, renal) |
| TxGNN 예측 점수 | 0.9907 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Benzbromarone의 작용 기전(비공식 번역): “용질 운반체 계열 22 구성원 12 억제제”. 영어 원문: "Solute carrier family 22 member 12 inhibitor" ([ChEMBL CHEMBL388590 (benzbromarone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL388590), CC BY-SA 3.0; 확인일 2026-11-19). 다만 약리학적으로 benzbromarone은 신장 요산 재흡수 수송체인 URAT1(SLC22A12)을 억제하여 혈중 요산을 낮추는 약물로 알려져 있습니다.

신성 저요산혈증은 URAT1(SLC22A12) 또는 GLUT9(SLC2A9)의 기능 소실 변이로 신장의 요산 배설이 이미 과도하게 증가해 혈중 요산이 낮은 상태입니다. Benzbromarone의 작용 방향은 이 병태와 같은 방향이므로 치료가 아니라 **악화시킬 가능성**이 있습니다.

TxGNN의 높은 점수는 요산 수송 생물학(URAT1 등)을 매개로 한 약물-질환 간 네트워크 근접성을 반영한 것으로 보이며, 치료 관계를 의미하지 않는 것으로 판단됩니다. 또한 신성 저요산혈증 환자는 운동 후 급성 신부전 위험이 알려져 있어, 요산 소실이 더 커지면 위험이 추가될 수 있습니다. 이 평가에는 제공된 데이터 밖의 약리학 지식이 일부 사용되었습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

아래 문헌은 benzbromarone을 **치료제가 아니라 요산 수송 결함을 규명하는 진단 시험(benzbromarone/pyrazinamide 억제 시험)** 에 사용한 보고가 대부분입니다. 이 약이 신성 저요산혈증을 치료한다는 근거는 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | 저요산혈증(혈청 요산 < 2 mg/dL)의 원인과 임상 양상을 정리한 서술적 고찰 |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | 요산 대사 이상(고요산혈증·저요산혈증)의 개념과 분류 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort | J Am Soc Nephrol | 일본 신성 저요산혈증 환자 32명에서 SLC22A12(URAT1) 변이와 임상 특성 분석 |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Case series | Clin Nephrol | 운동 유발 급성 신부전과 만성 신기능 저하를 동반한 신성 저요산혈증 환자 |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case series | J Pediatr | 유전성 신성 저요산혈증 소아 4명에서 benzbromarone이 요산 청소율 비를 변화시키지 않음 |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | 운동 유발 급성 신부전을 보인 신성 저요산혈증 형제 사례 |
| [12862209](https://pubmed.ncbi.nlm.nih.gov/12862209/) | 2003 | Case report | Hypertens Res | 로사르탄·트리클로르메티아지드 치료 중 운동 유발 급성 신부전이 나타난 특발성 신성 저요산혈증 |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case report | Acta Paediatr | 반복적 운동 유발 급성 신부전 환자에서 benzbromarone/pyrazinamide 시험으로 근위세뇨관 재흡수 결함 시사 |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case report | Nephron | 신장 요산 수송 결함 환자에서 benzbromarone 투여 후 요산 청소율이 오히려 증가 |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Case report | Nephron | 현저한 신성 저요산혈증을 동반한 Fanconi 증후군에서 pyrazinamide·benzbromarone을 이용한 요산 수송 분석 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199500892 | 명인날카리신정50밀리그램(벤즈브로마론) | 백색의 원형정제. | 명인제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199500892/EE) | 유효 |
| 199502668 | 유리논정(벤즈브로마론) | 백색의 원형정제 | 한림제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199502668/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로, 이 약은 간독성과 연관되어 일부 시장에서 철수된 것으로 알려져 있습니다(제공 데이터 외 약리학 지식). 신성 저요산혈증에서는 운동 유발 급성 신부전 위험이 알려져 있어 요산 배설을 더 늘리는 접근은 위험을 키울 수 있습니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Benzbromarone은 요산 배설을 늘려 혈중 요산을 낮추는 약이므로, 이미 요산이 낮은 신성 저요산혈증에서는 치료 효과보다 증상 악화 가능성이 큽니다. 임상시험이 없고 문헌도 진단 시험 사례 위주여서 근거 수준은 L5(모델 예측만 있음)입니다.

**진행하려면 필요한 것:**
- 허가사항 문서에서 기존 적응증, 경고, 금기 정보 확보 (현재 링크만 있고 본문 없음)
- DrugBank 등에서 상세 작용 기전 데이터 확인
- 약효 방향 불일치(요산 저하 약물 vs. 저요산혈증)에 대한 약리학적 재검토 — 근거가 없다면 이 예측은 폐기하는 것이 타당함
- 간독성 및 급성 신손상 위험에 대한 안전성 평가

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [ChEMBL CHEMBL388590 (benzbromarone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL388590) |
| 2026-11-24 | 단일·복합 표기: “Benzbromarone은 요산 배설을 촉진하는 약물(uricosuric…” → 고정된 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 (2026-11-25 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

