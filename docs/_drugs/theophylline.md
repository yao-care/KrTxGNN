---
layout: default
title: Theophylline
parent: 모델 예측만 (L5)
nav_order: 732
evidence_level: L5
indication_count: 6
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-11-24
description: "Theophylline: 예측 신규 적응증 혈전성 질환 (근거 수준 L5). 기존 적응증: 다음 질환의 기도폐쇄 장애에 의한 호흡곤란 등 여러 증상의 완화 : 기관지천식, 천식기관지염"
---

# Theophylline
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

## Theophylline: 기존 허가 적응증에서 혈전성 질환으로
{: .text-alpha }

## 한 문장 요약

Theophylline은 한국에서 건조시럽 단일제로 허가된 약물입니다. 다만 데이터상 허가 적응증 항목에는 문서 링크만 있고 구체적인 적응증 문구는 확인되지 않았습니다. TxGNN 모델은 **혈전성 질환(thrombotic disease)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험이나 문헌은 없어 **모델 예측만 있는 단계(L5)**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음 질환의 기도폐쇄 장애에 의한 호흡곤란 등 여러 증상의 완화 : 기관지천식, 천식기관지염 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200704931/EE)) |
| 예측 신규 적응증 | 혈전성 질환 |
| TxGNN 예측 점수 | 0.9962 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 4건) |
| 허가증 수 | 4건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Theophylline 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “Theophylline은 가역적 기도 폐쇄가 있는 환자의 기도에서 두 가지 뚜렷한 작용을 한다: 평활근 이완(즉, 기관지 확장)과 자극에 대한 기도 반응의 억제(즉, 비기관지확장성 예방 효과).” 영어 원문: "Theophylline has two distinct actions in the airways of patients with reversible obstruction: smooth muscle relaxation (i.e., bronchodilation) and suppression of the response of the airways to stimuli (i.e., non-bronchodilator prophylactic effects)." ([DailyMed: Theo-24 (theophylline anhydrous) prescribing information, ENDO USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7a108fa0-c230-475f-be93-6f864b98a410), 버전 2024-07-08; 확인일 2026-11-19). 다만 일반적으로 theophylline은 비선택적 포스포디에스터라제(PDE) 억제제이자 아데노신 수용체 길항제로 알려져 있습니다.

PDE 억제는 혈소판 내 cAMP를 높여 혈소판 응집을 약하게 억제할 수 있습니다. 반면 아데노신 길항 작용은 아데노신의 항혈소판 효과를 상쇄합니다. 따라서 실제 항혈전 효과가 어떨지는 불분명하며, 높은 예측 점수를 뒷받침하는 임상 데이터도 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

검색된 문헌 18편 중 혈전성 질환에 대한 theophylline의 효과를 직접 평가한 연구는 없습니다. 대부분 혈소판 관련 검체 처리법, 다른 약물(ticlopidine, milrinone 등)의 약동학·약리, 또는 관찰 연구입니다. 아래는 상대적으로 관련성이 높은 문헌이며, 모두 간접 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | 약리 연구 | General Pharmacology | Milrinone이 cAMP를 높여 혈소판 응집을 억제하며 아데노신 효과와 상호작용함 (theophylline 아님) |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | 프로스타사이클린과 트롬복산, 혈소판 응집 조절 개관 |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | 약동학 리뷰 | Clinical Pharmacokinetics | Ticlopidine의 약동학 (theophylline 아님) |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | 관찰 연구 | Inflammatory Bowel Diseases | 염증성 장질환에서 혈소판-백혈구 응집체 형성 |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | 관찰 연구 | Rheumatology | 베체트병 환자의 혈소판·호중구 활성화 |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | 임상 보고 | Minerva Cardioangiologica | Theophylline 니코틴산 유도체의 만성 폐쇄성 말초동맥질환 치료 (초록 없음, 다른 화합물) |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200704931 | 데올론건조시럽20%(테오필린)(수출용) | 백색의 분말 또는 입상으로 딸기향이 있는 건조시럽제 | 코오롱제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200704931/EE) | 유효 |
| 200302202 | 데오크레건조시럽20%(테오필린) | 백색의 분말 또는 입상으로 딸기향이 있는 건조시럽제 | 알보젠코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200302202/EE) | 유효 |

위 표는 허가 4건 중 2건입니다.

<!-- licenses:end -->

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

- **지식그래프상 금기 관계** (허가 문서가 아닌 TxGNN 지식그래프 기록): 고혈압, 간부전, 간질, 불안장애, 포르피린증, 신장질환, 담낭질환, 혈소판감소증, 갑상선기능저하증, 소화성궤양, 개방각 녹내장, 정신질환, 당뇨병, 당뇨병성 케톤산증, 양성 전립선 비대증, 호중구감소증, 무과립구증 등.
- **약물 상호작용** (총 100건 조회, 이 중 일부 표시):
  - 주요(Major): Bupropion
  - 중등도(Moderate): Famotidine, Ranitidine, Cimetidine, Omeprazole, Rabeprazole, Clarithromycin, Doxycycline, Tetracycline, Minocycline, Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide 등
  - 경미(Minor): Ephedrine

## 결론 및 다음 단계

**결정: Hold**

**사유:**
혈전성 질환을 직접 연구한 임상시험이나 문헌이 없고 근거는 모델 예측뿐입니다. 기전상 PDE 억제(항혈소판 방향)와 아데노신 길항(상쇄 방향)이 엇갈려 순 효과가 불분명합니다.

**진행하려면 필요한 것:**
- 허가 문서에서 허가 적응증과 경고·금기 정보 확보
- 상세한 작용 기전(MOA) 데이터 확보
- 혈전성 질환에서 theophylline의 항혈소판·항혈전 효과를 평가하는 전임상 또는 임상 연구
- 시판 상태(취소 여부) 확인

**참고:** 같은 약물의 다른 예측 중에서는 기관(trachea) 질환과 비강 질환 쪽이 상대적으로 더 많은 간접 근거를 가지지만, 이 역시 사람 대상의 직접 근거는 부족해 추가 검증이 필요합니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Theo-24 (theophylline anhydrous) prescribing information, ENDO USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7a108fa0-c230-475f-be93-6f864b98a410) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

