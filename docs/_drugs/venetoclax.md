---
layout: default
title: Venetoclax
parent: 모델 예측만 (L5)
nav_order: 782
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "VENETOCLAX"
predicted_indications: ["Hodgkins lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Ewing sarcoma", "follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma"]
description: "Venetoclax: 예측 신규 적응증 Hodgkins lymphoma (근거 수준 L5). 기존 적응증: 만성 림프구성 백혈병 이전에 치료받은 적이 없는 만성 림프구성 백혈병 성인 환자에서 오비누투주맙과의 병용…"
---

# Venetoclax
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

## Venetoclax: Hodgkins lymphoma
{: .text-alpha }

## 한 문장 요약

Venetoclax는 BCL-2를 선택적으로 억제하는 경구 항종양제로, 한국에서 단일제 3개 품목이 시판 중입니다.
TxGNN 모델은 **전배중심 CLL/SLL(pregerminal center CLL/SLL, IGHV 비돌연변이 아형)**에 효과가 있을 수 있다고 예측하지만, 이 아형을 직접 다룬 **임상시험은 0건**이고 **문헌은 1편(B세포 수용체 구조·기능 리뷰)**뿐입니다.
이 예측은 이미 허가된 CLL/SLL의 하위 아형에 해당하므로 새로운 재창출 신호로 보기 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 림프구성 백혈병 이전에 치료받은 적이 없는 만성 림프구성 백혈병 성인 환자에서 오비누투주맙과의 병용 요법 이전에 적어도 하나의 치료를 받은 만성 림프구성 백혈병 성인 환자에서 리툭시맙과의 병용 요법 화학면역요법 및 B 세포 수용체 경로 저해제에 재발 또는 불응인 만성 림프구성… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201903544/EE)) |
| 예측 신규 적응증 | Hodgkins lymphoma |
| TxGNN 예측 점수 | 0.9951 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Venetoclax 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “베네토클락스는 항세포자멸사 단백질인 BCL-2의 선택적이고 경구 생체이용 가능한 저분자 억제제이다. BCL-2의 과발현은 CLL 및 AML 세포에서 확인되었으며, 이들 세포에서 BCL-2는 종양 세포 생존을 매개하고 화학요법제에 대한 내성과 관련이 있는 것으로 나타났다.” 영어 원문: "Venetoclax is a selective and orally bioavailable small-molecule inhibitor of BCL-2, an anti-apoptotic protein. Overexpression of BCL-2 has been demonstrated in CLL and AML cells where it mediates tumor cell survival and has been associated with resistance to chemotherapeutics." ([DailyMed: Venclexta (venetoclax) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b118a40d-6b56-cee3-10f6-ded821a97018), 버전 2026-05-20; 확인일 2026-11-19). 문헌에 따르면 venetoclax는 세포 사멸(미토콘드리아 세포자멸) 경로를 조절하는 BCL-2 단백질을 선택적으로 억제하는 경구 약물이며, CLL에서 특히 높은 반응률을 보입니다.

예측된 질환은 CLL/SLL 중 IGHV 유전자가 돌연변이되지 않은(U-CLL) 아형입니다. 이 아형은 배중심 이전 기원이며 예후가 불량한 것으로 알려져 있습니다. CLL/SLL은 BCL-2 의존성이 높은 질환이므로, 하위 아형에서도 효과가 있을 가능성은 이론적으로 타당합니다.

다만 이 예측은 상위 질환(CLL/SLL)과의 연관성이 반영된 결과일 가능성이 큽니다. 아형 자체에 대한 독립적 근거는 확인되지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Review | Cancers | 종양 B세포 수용체(BCR)의 구조와 기능이 CLL의 생물학과 임상에 주는 시사점을 정리했습니다. IGHV 비돌연변이(U-CLL, 예후 불량)와 돌연변이(M-CLL, 예후 양호) 아형을 구분합니다. venetoclax 시험은 아닙니다. |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201903544 | 벤클렉스타정50밀리그램(베네토클락스) | 한 면에 “V”, 다른 한 면에 “50”이 새겨진 베이지의 양면이 볼록한… | 한국애브비(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201903544/EE) | 유효 |
| 201903543 | 벤클렉스타정10밀리그램(베네토클락스) | 한 면에 “V”, 다른 한 면에 “10”이 새겨진 연한 노란색의 양면이… | 한국애브비(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201903543/EE) | 유효 |
| 201903542 | 벤클렉스타정100밀리그램(베네토클락스) | 한 면에 “V”, 다른 한 면에 “100”이 새겨진 연한 노란색의 양면이… | 한국애브비(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201903542/EE) | 유효 |

<!-- licenses:end -->

제조사는 한국애브비(주)입니다.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (BCL-2 억제제) |
| 골수억제 위험 | 문헌상 종양융해증후군과 골수억제가 가장 흔하게 나타나는 이상반응으로 보고됨 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC(혈구 수치), 신기능, 전해질·요산 등 종양융해증후군 관련 검사 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 확인되었으며, 이 중 주요(Major) 등급으로 확인된 항목은 다음과 같습니다.
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Eliglustat
  - Rolapitant
  - Fidaxomicin
  - Cobicistat
  - Deferiprone
  - Samarium (153Sm) lexidronam
- 중등도(Moderate) 상호작용에는 Alvimopan, Loperamide, Cimetidine, Miconazole, Rifaximin, Clotrimazole 등이 있습니다.
- 문헌에 따르면 posaconazole 같은 강한 CYP3A 억제제와 병용할 때는 venetoclax 용량 조정이 필요합니다(PMID 28161120).
- 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 예측은 이미 허가된 CLL/SLL의 하위 아형이어서 새로운 재창출 신호가 아니며, 아형 특이적 임상시험이 없고 연관 문헌도 venetoclax를 직접 다루지 않습니다.

**진행하려면 필요한 것:**
- 한국 허가사항에서 CLL/SLL 적응증 포함 여부를 확인해야 합니다. 이번 데이터에는 허가증 링크만 있어 본문을 확인하지 못했습니다.
- IGHV 비돌연변이 아형에 대한 venetoclax 임상 데이터 또는 하위 분석(예: MURANO 등의 아형별 결과)을 확인해야 합니다.
- 허가사항의 경고·금기, 종양융해증후군 위험 관리 방안 등 안전성 정보를 확보해야 합니다.

**참고: 동일 약물의 다른 예측 후보**

| 예측 질환 | 근거 수준 | 모델 권고 | 비고 |
|----------|---------|---------|------|
| 골수성 백혈병(AML) | L1 | Proceed with Guardrails | Phase 3(NCT06852222)는 모집 중이며, L1 판정은 외부 표준치료 근거에 의존하므로 허가 적응증 여부와 함께 확인이 필요합니다. |
| 만성 골수성 백혈병(BCR-ABL1 양성) | L2 | Proceed with Guardrails | 소규모 단일군 Phase 2 중심이며, 일부 시험은 조기 종결되었습니다. |
| 여포성 림프종 | L2 | Proceed with Guardrails | 단독요법의 효과는 제한적이고, 병용요법 Phase 2 근거가 있습니다. |
| 호지킨 림프종, 전이성 종양 | L3 | Research Question | 직접 근거가 없고 다른 질환 시험이 넓은 분류로 매칭된 결과입니다. |
| Ewing 육종, 악성 나선선종, t(8;21) AML, CLL/SLL 돌연변이 아형 | L4–L5 | Hold | 임상 근거가 없거나 간접적입니다. |

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Venclexta (venetoclax) prescribing information, AbbVie Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b118a40d-6b56-cee3-10f6-ded821a97018) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

