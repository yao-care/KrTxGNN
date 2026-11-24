---
layout: default
title: Latanoprost
parent: 모델 예측만 (L5)
nav_order: 462
evidence_level: L5
indication_count: 9
monitor_inn: "LATANOPROST"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
last_modified_at: 2026-11-24
description: "Latanoprost: 예측 신규 적응증 내장 칼시필락시스 (visceral calciphylaxis) (근거 수준 L5). 기존 적응증: 다음 질환의 안압하강: ㆍ성인 개방각 녹내장, 만성 폐쇄각 녹내장, 고안압 ㆍ소아 소아 녹내장, 고안압"
---

# Latanoprost
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Latanoprost: 프로스타글란딘 F2α 유사체(FP 수용체 작용제) → 내장 칼시필락시스 (visceral calciphylaxis)
{: .text-alpha }

## 한 문장 요약

Latanoprost는 프로스타글란딘 F2α 유사체로, 국소 점안제 형태로 사용되는 약물입니다.
TxGNN 모델은 **내장 칼시필락시스(visceral calciphylaxis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 예측을 지지하는 **임상시험과 문헌은 모두 0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 다음 질환의 안압하강: ㆍ성인 개방각 녹내장, 만성 폐쇄각 녹내장, 고안압 ㆍ소아 소아 녹내장, 고안압 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201803532/EE)) |
| 예측 신규 적응증 | 내장 칼시필락시스 (visceral calciphylaxis) |
| TxGNN 예측 점수 | 0.9983 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Latanoprost 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “라타노프로스트는 방수 유출을 증가시킴으로써 안압(IOP)을 낮추는 것으로 여겨지는 프로스타글란딘 F 2α 유사체이다. 동물 및 사람을 대상으로 한 연구에 따르면 주된 작용기전은 포도막공막 유출의 증가이다.” 영어 원문: "Latanoprost is a prostaglandin F 2α analogue that is believed to reduce the intraocular pressure (IOP) by increasing the outflow of aqueous humor. Studies in animals and man suggest that the main mechanism of action is increased uveoscleral outflow." ([DailyMed: Xelpros (latanoprost) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34ad5cf6-4df0-4104-bddd-4c7631133ded), 버전 2025-12-18; 확인일 2026-11-19). 알려진 정보에 따르면 latanoprost는 눈에 국소 투여하는 FP 수용체 작용제로, 눈에서 혈관 확장 작용을 나타냅니다. 모델은 이 혈관 관련 특성을 근거로 혈관 질환과 연관지었을 가능성이 있습니다.

그러나 명확한 기전적 연결고리는 확립되어 있지 않습니다. 칼시필락시스는 주로 신부전 환자에서 혈관 석회화, 소혈관 혈전, 조직 허혈이 나타나는 질환입니다. 점안 투여 시 전신 노출이 낮아 관련 효과를 기대하기 어렵습니다. 이 예측은 어떤 임상시험이나 문헌으로도 뒷받침되지 않습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201803532 | 잘로스트S점안액(라타노프로스트) | 무색 투명한 액이 녹색의 투명한 플라스틱 용기에 든 점안제 | (주)태준제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201803532/EE) | 유효 |
| 200501988 | 옵티스트점안액(라타노프로스트)(수출용) | 무색투명한 플라스틱용기에 무색 투명한 액이 든 점안제 | 경동제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200501988/EE) | 유효 |
| 200502576 | 잘로스트플러스점안액 | 무색 투명한 플라스틱 용기에 든 무색 투명한 점안액 | (주)태준제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502576/EE) | 유효 |
| 202402442 | 라타노프리점안액(라타노프로스트)(1회용) | 무색 투명한 액이 무색 투명한 플라스틱 용기에 든 점안제 | (주)옵투스제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402442/EE) | 유효 |
| 202403034 | 라노프점안액(라타노프로스트)(1회용) | 무색 투명한 액이 무색 투명한 플라스틱 용기에 든 점안제 | 국제약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202403034/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조회 결과 100건이 확인되었으나 위험 등급은 모두 "미상"입니다. 일부 예시는 Calcitriol, Glimepiride, Doxycycline, Atropine, Metformin, Prednisone, Simvastatin 등입니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
내장 칼시필락시스에 대해 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 기전상 연결고리도 불분명하고, 점안 투여로는 전신 노출이 낮아 타당성이 낮습니다.

**진행하려면 필요한 것:**
- 칼시필락시스와 프로스타글란딘 FP 수용체 경로의 연관성을 보여주는 전임상 또는 기전 연구
- 상세한 약물 작용 기전(MOA) 데이터
- 허가사항(경고 및 금기) 확인
- 전신 투여 시 노출 및 안전성 평가 (현재 점안제 제형만 있음)

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Xelpros (latanoprost) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34ad5cf6-4df0-4104-bddd-4c7631133ded) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

