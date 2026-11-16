---
layout: default
title: Anagrelide Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 74
evidence_level: L5
indication_count: 2
drugbank_id: DB00261
monitor_inn: "Anagrelide"
predicted_indications: ["reactive thrombocytosis", "inverse Klippel-Trenaunay syndrome"]
last_modified_at: 2026-11-16
description: "Anagrelide Hydrochloride: 예측 신규 적응증 반응성 혈소판증가증 (reactive thrombocytosis) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Anagrelide Hydrochloride
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

## Anagrelide Hydrochloride: 반응성 혈소판증가증 (reactive thrombocytosis)
{: .text-alpha }

## 한 문장 요약

Anagrelide Hydrochloride는 혈소판 수를 낮추는 약물로, 국내에서 단일성분 제제로 시판되고 있습니다.
TxGNN 모델은 **반응성 혈소판증가증(reactive thrombocytosis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험이나 문헌은 확인되지 않았습니다.
현재 확보된 근거는 본태성 혈소판증가증 등 관련 질환에 관한 **문헌 10편**이며, 모두 이번 예측 질환을 직접 다루지 않습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201803846/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200409939/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201803558/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201602615/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201803698/EE) |
| 예측 신규 적응증 | 반응성 혈소판증가증 (reactive thrombocytosis) |
| TxGNN 예측 점수 | 0.9983 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 7건) |
| 허가증 수 | 7건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 보충되지 않았습니다. 다만 문헌에 따르면 anagrelide는 거핵구의 성숙과 분화를 억제하여(거핵구 크기와 배수성 감소) 혈소판 수를 낮추며, PDE3 억제 작용도 가진 것으로 알려져 있습니다. 이 약은 본태성 혈소판증가증 같은 골수증식성 종양의 혈소판증가증에 사용됩니다.

반응성(이차성) 혈소판증가증은 염증, 감염, 철결핍, 비장절제 등에 반응하여 IL-6, 트롬보포이에틴 같은 사이토카인이 늘어서 생기며, 일반적으로 클론성 질환이 아닙니다. 혈소판을 낮추는 기전 자체는 생물학적으로 가능하지만, 반응성 혈소판증가증은 대개 세포감소 치료가 필요하지 않고 혈전 위험도 낮다는 점이 핵심 한계입니다.

TxGNN 점수(0.9983)는 본태성 혈소판증가증과의 질환 분류상 근접성을 반영한 것으로 보이며, 이 질환에 대한 독립적 근거는 아닙니다. 따라서 기대 효과는 클론성 질환에서 외삽한 간접적인 것입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

아래 문헌은 본태성 혈소판증가증 등 관련 질환을 다루며, 반응성 혈소판증가증에 대한 anagrelide 효과를 직접 검증한 연구는 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Med J Aust | 본태성 혈소판증가증 진단 시 반응성 혈소판증가증 감별이 필요하며, 혈소판 1000×10⁹/L 초과 시 혈소판 저하 치료 권고 |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leuk Lymphoma | 반응성 혈소판증가증은 대개 큰 문제가 없으나 클론성은 세포감소 치료 필요, anagrelide 치료 비평 |
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Rev Anticancer Ther | 반응성 혈소판증가증은 치료 개입이 필요 없고, anagrelide의 작용 기전과 치료 잠재력 정리 |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Cohort | Pediatr Blood Cancer | 소아 본태성 혈소판증가증과 반응성 혈소판증가증 12례 후향 분석 |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leuk Res | 골수증식성 종양의 극심한 혈소판증가증에서 혈소판성분채집술의 역할 |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki | 본태성 혈소판증가증 진단·치료, 반응성과의 감별 및 anagrelide 등 사용 |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | Am J Med Sci | 혈소판증가증의 임상 스펙트럼 개괄 |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case report | Eur J Case Rep Intern Med | anagrelide 치료 중인 본태성 혈소판증가증 환자의 급성 심근경색 1례 |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case report | Srp Arh Celok Lek | 본태성 혈소판증가증과 강직성 척추염 동반 환자에서 anagrelide 병용 치료 1례 |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case report | Medicine | 비장절제 후 혈소판증가증 환자의 2개 수지 재접합 성공 1례 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201803846 | 아나리드캡슐 0.5밀리그램 | 경질캡슐 | 허가사항 문서 참조 |
| 200409939 | 아그릴린캡슐 0.5밀리그램 | 경질캡슐 | 허가사항 문서 참조 |
| 201803558 | 아나리드캡슐 1밀리그램 | 경질캡슐 | 허가사항 문서 참조 |
| 201602615 | 아나그레캡슐 0.5밀리그램 | 경질캡슐 | 허가사항 문서 참조 |
| 201803698 | 아나그레캡슐 1밀리그램 | 경질캡슐 | 허가사항 문서 참조 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
반응성 혈소판증가증을 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 반응성 혈소판증가증은 일반적으로 혈소판 저하 치료가 필요하지 않고 혈전 위험도 낮아, 높은 예측 점수만으로 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 반응성 혈소판증가증 환자에서 anagrelide의 필요성과 효과를 직접 평가한 임상 또는 관찰 연구
- 허가사항 기반의 경고, 금기, 약물 상호작용 등 안전성 정보 확보
- 상세한 작용 기전(MOA) 데이터 보완
- 혈전 위험이 높은 반응성 혈소판증가증 하위 집단이 실제로 존재하는지에 대한 임상적 타당성 검토
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

