---
layout: default
title: Tulobuterol
parent: 모델 예측만 (L5)
nav_order: 771
evidence_level: L5
indication_count: 4
monitor_inn: "TULOBUTEROL"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
last_modified_at: 2026-11-03
description: "Tulobuterol: 예측 신규 적응증 호흡기 기형 (respiratory malformation) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201310337/EE"
---

# Tulobuterol
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Tulobuterol: 호흡기 기형 (respiratory malformation)
{: .text-alpha }

## 한 문장 요약

Tulobuterol은 베타-2 아드레날린 수용체 작용제 계열의 경피흡수제 성분입니다.
TxGNN 모델은 **호흡기 기형(respiratory malformation)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험이나 문헌은 확인되지 않았습니다. 현재 근거는 모델 예측 수준(L5)에 머뭅니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201310337/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201003161/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201003180/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201003158/EE; https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201003174/EE;  |
| 예측 신규 적응증 | 호흡기 기형 (respiratory malformation) |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Tulobuterol은 베타-2 작용제 계열로, 기관지 평활근 이완을 통한 기관지 확장 작용이 기대됩니다.

다만 호흡기 기형은 구조적인 선천성 결함입니다. 기관지 확장은 증상을 일시적으로 완화할 수는 있어도 해부학적 결함 자체를 교정하지는 못합니다. 따라서 기전상 뚜렷한 연결고리는 확인되지 않으며, 높은 예측 점수는 호흡기 질환과 관련된 노드와의 근접성을 반영했을 가능성이 큽니다.

## 문헌 근거

이 질환을 직접 다룬 문헌은 없습니다. 아래 1편은 소아 천식 연구로, 약물의 기관지 확장 작용에 대한 참고 자료일 뿐입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [2876923](https://pubmed.ncbi.nlm.nih.gov/2876923/) | 1986 | 임상 연구 | The Journal of International Medical Research | 소아 천식 환자 대상 용량 탐색 및 terbutaline 비교 연구. Tulobuterol은 빠르고 지속적인 기관지 확장 작용을 보임 |

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 한국 시판 정보

현재 확인된 허가는 최소 20건이며, 목록이 일부일 수 있습니다. 모두 단일 성분 경피흡수제입니다. 주요 5건은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201310337 | 네오날린패취0.5밀리그램 | 서방성 경피흡수제 | 적응증 본문 미확인 (허가 문서 PDF 링크만 제공) |
| 201003161 | 레스날린패취1밀리그램 | 서방성 경피흡수제 | 적응증 본문 미확인 (허가 문서 PDF 링크만 제공) |
| 201003180 | 노테몬패취1밀리그램 | 서방성 경피흡수제 | 적응증 본문 미확인 (허가 문서 PDF 링크만 제공) |
| 201003158 | 호쿠테롤패취1밀리그램 | 서방성 경피흡수제 | 적응증 본문 미확인 (허가 문서 PDF 링크만 제공) |
| 201003174 | 투브롤패취1밀리그램 | 서방성 경피흡수제 | 적응증 본문 미확인 (허가 문서 PDF 링크만 제공) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
호흡기 기형을 직접 다룬 임상시험이나 문헌이 없고, 구조적 결함에 대해 기관지 확장제가 작용할 기전적 근거도 불분명합니다. 현재는 모델 예측만 있는 L5 단계입니다.

**진행하려면 필요한 것:**
- 호흡기 기형 환자를 대상으로 한 임상 또는 전임상 근거
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고, 금기)에 대한 확인 및 안전성 검토
- 호흡기 기형 병태에서 증상 완화 목적의 사용이 타당한지에 대한 임상 전문가 검토

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

