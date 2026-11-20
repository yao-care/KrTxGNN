---
layout: default
title: Fenofibrate
parent: 모델 예측만 (L5)
nav_order: 342
evidence_level: L5
indication_count: 1
monitor_inn: "FENOFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-11-15
description: "Fenofibrate: 예측 신규 적응증 콜레스테롤 에스터 전이 단백질 결핍증 (근거 수준 L5). 기존 적응증: 원발성 고지혈증 : 고콜레스테롤혈증(IIa형), 고콜레스테롤혈증과 고트리글리세라이드혈증의 복합형(IIb형…"
---

# Fenofibrate
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

## Fenofibrate: 지질 이상 치료에서 콜레스테롤 에스터 전이 단백질 결핍증으로
{: .text-alpha }

## 한 문장 요약

Fenofibrate는 한국에서 단일 성분 및 피타바스타틴과의 복합제 형태로 허가된 약물입니다. TxGNN 모델은 **콜레스테롤 에스터 전이 단백질 결핍증(cholesterol-ester transfer protein deficiency)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 없고 **3편의 전임상·기전 문헌**만 간접적으로 관련되어 있습니다. 따라서 근거 수준은 L5이며, 현재는 보류를 권장합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 원발성 고지혈증 : 고콜레스테롤혈증(IIa형), 고콜레스테롤혈증과 고트리글리세라이드혈증의 복합형(IIb형, Ⅲ형), 고트리글리세라이드혈증 (IV형) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201902160/EE)) |
| 예측 신규 적응증 | 콜레스테롤 에스터 전이 단백질 결핍증 |
| TxGNN 예측 점수 | 0.9961 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Fenofibrate 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “Antara의 활성 부분은 페노피브르산이다. 동물과 인간 모두에서 페노피브르산의 약리학적 효과는 페노피브레이트의 경구 투여를 통해 연구되었다. 임상에서 관찰되는 페노피브르산의 지질 조절 효과는 형질전환 마우스를 이용한 생체 내 연구와 인간 간세포 배양을 이용한 시험관 내 연구에서 PPAR 알파 수용체의 활성화로 설명되었다.” 영어 원문: "The active moiety of Antara is fenofibric acid. The pharmacological effects of fenofibric acid in both animals and humans have been studied through oral administration of fenofibrate. The lipid-modifying effects of fenofibric acid seen in clinical practice have been explained in vivo in transgenic mice and in vitro in human hepatocyte cultures by the activation of PPAR alpha receptor." ([DailyMed: Antara (fenofibrate) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=24790a18-0291-4b88-a724-acac43b616ce), 버전 2025-10-01; 확인일 2026-11-19). 다만 수집된 문헌에 따르면 fenofibrate는 PPARα 작용제로서 HDL 콜레스테롤을 높이고 중성지방과 LDL 콜레스테롤을 낮추며, 인지질 전이 단백질(PLTP) 유전자 발현을 유도합니다. PLTP 유도가 CETP 활성 부족을 일부 보완할 가능성이 이론적으로 제기됩니다.

그러나 약리학적 근거는 약합니다. CETP 결핍증은 HDL-C가 크게 상승하는 희귀 유전 질환으로, 흔히 양성 경과를 보이거나 장수와 연관되기도 하여 지질을 추가로 조절해야 할 임상적 필요가 분명하지 않습니다. 높은 예측 점수(0.9961)는 검증된 치료 기회보다는 지질 대사 유전자와 PPARα/CETP 경로 사이의 네트워크 근접성을 반영했을 가능성이 큽니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | 전임상 | J Cardiovasc Pharmacol Ther | 사람 ApoB100/CETP 형질전환 마우스에서 CETP 억제와 PPARα 작용제(fenofibrate) 병용 시 HDL-C 상승, LDL-C 감소 |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | 전임상 | J Biol Chem | fenofibrate 투여 마우스에서 PLTP 유전자 유도가 HDL 확대를 설명 |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | 전임상 | Front Physiol | 혈장 HDL 수치와 분변 콜레스테롤 배출·콜레스테롤 유출 능력 간 상관이 없어 HDL 기능의 중요성을 시사 |

세 편 모두 CETP 결핍증 자체를 직접 다룬 연구가 아니며 간접 근거에 해당합니다.

## 한국 시판 정보

데이터에 수록된 허가증은 최소 20건이며, 목록이 일부일 수 있습니다. 허가 적응증 칸에는 텍스트 대신 허가 문서 링크만 제공되어 구체적인 적응증을 확인할 수 없습니다. 아래는 단일 성분 제제 중 주요 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201902160 | 페노딜정160밀리그램 | 흰색의 장방형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201902160/EE) |
| 201908692 | 리페돌정160밀리그램 | 흰색의 장방형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201908692/EE) |
| 202500240 | 네오페노정48밀리그램 | 분홍색의 타원형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500240/EE) |
| 202007619 | 페노웰정145밀리그램 | 흰색의 타원형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202007619/EE) |
| 202001689 | 페노피정160밀리그램 | 흰색의 장방형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202001689/EE) |

## 안전성 고려사항

- **지식그래프상 금기 관계**: 지식그래프에 기록된 관계로서 허가사항 문구가 아닙니다. 간부전, 간질환, 췌장염, 담낭질환·담석증, 혈소판감소증, 근병증·횡문근융해, 신기능 장애, 빈혈, 백혈구감소증·호중구감소증·무과립구증 등이 포함됩니다.
- **약물 상호작용**: 총 100건이 조회되었으며, 목록에 표시된 항목은 모두 중등도입니다. 주요 항목은 설포닐우레아계 혈당강하제(acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), 여러 인슐린 제제, chenodeoxycholic acid, esomeprazole입니다.

상세한 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환을 직접 연구한 임상시험이나 문헌이 없고, 지지 문헌은 간접적인 전임상·기전 연구뿐입니다. CETP 결핍증은 치료 필요성 자체가 불분명하며, 높은 모델 점수는 네트워크 근접성에 기인했을 가능성이 큽니다.

**진행하려면 필요한 것:**
- CETP 결핍증 환자를 직접 대상으로 한 연구 또는 치료 필요성에 대한 임상적 근거
- 상세한 작용 기전 데이터 (DrugBank 조회)
- 허가사항(경고·금기·적응증)의 원문 확보 및 분석 (MFDS 허가 문서)
- 전체 허가증 목록과 시판 상태(취소 여부) 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Antara (fenofibrate) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=24790a18-0291-4b88-a724-acac43b616ce) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

