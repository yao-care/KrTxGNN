---
layout: default
title: Zanamivir
parent: 모델 예측만 (L5)
nav_order: 789
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-15
description: "Zanamivir: 예측 신규 적응증 신우신염 (Pyelonephritis) (근거 수준 L5). 기존 적응증: 1. 성인 및 7세 이상 소아에서 인플루엔자 A 및 인플루엔자 B 바이러스 감염증의 치료(인플루엔자 감염의…"
monitor_inn: "zanamivir"
predicted_indications: ["pyelonephritis", "disorder of tyrosine metabolism"]
---

# Zanamivir
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

## Zanamivir: 인플루엔자에서 신우신염으로
{: .text-alpha }

## 한 문장 요약

Zanamivir는 흡입형 신경아미니다제 억제제로, 인플루엔자 치료에 사용되는 약입니다.
TxGNN 모델은 **신우신염(Pyelonephritis)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**이어서 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 성인 및 7세 이상 소아에서 인플루엔자 A 및 인플루엔자 B 바이러스 감염증의 치료(인플루엔자 감염의 초기증상 발현 48시간 이내에 투여를 시작해야 한다.) 2. 성인 및 7세 이상 소아에서 인플루엔자 A 및 인플루엔자 B 바이러스 감염증의 예방(인플루엔자 바이러스 감염증에 대한… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200008732/EE)) |
| 예측 신규 적응증 | 신우신염 (Pyelonephritis) |
| TxGNN 예측 점수 | 0.9984 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Zanamivir 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “자나미비르는 인플루엔자 바이러스에 대해 활성을 갖는 항바이러스제이다. […] 자나미비르는 감염된 세포의 원형질막으로부터 바이러스 입자를 방출시키고 호흡기에서 바이러스 확산을 촉진하는 효소인 인플루엔자 바이러스 뉴라미니다제(NA)의 억제제이다. 뉴라미니다제 억제 분석에서 자나미비르는 N1부터 N9까지의 모든 NA 효소 아형에 대해 활성을 나타낸다.” 영어 원문: "Zanamivir is an antiviral drug with activity against influenza virus. […] Zanamivir is an inhibitor of influenza virus neuraminidase (NA), an enzyme that releases viral particles from the plasma membrane of infected cells and promotes virus spread in the respiratory tract. In neuraminidase inhibition assays, zanamivir is active against all NA enzyme subtypes N1 to N9." ([DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d), 버전 2026-07-23; 확인일 2026-11-19). 알려진 정보에 따르면 zanamivir는 인플루엔자 A·B형 바이러스의 신경아미니다제를 억제하는 약물이며, 흡입으로 투여됩니다.

신우신염은 주로 대장균 등에 의한 세균성 신장 감염으로, 인플루엔자와는 병원체와 병태가 다릅니다. 세균에도 신경아미니다제(시알리다제)가 존재하지만, zanamivir가 항균제로 확립된 근거는 없습니다. 또한 흡입 투여 시 신장에 도달하는 전신 노출이 매우 적습니다. 따라서 기전상 뚜렷한 연결고리는 확인되지 않았으며, 높은 TxGNN 점수(0.9984)는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200008732 | 리렌자로타디스크5밀리그램(자나미비르) | 흡입용 분말 원형 디스크 (4포낭 호일포장) | 허가 적응증 본문 미확인 (허가사항 참조) |

## 안전성 고려사항

- **약물 상호작용**: 총 8건이 확인되었습니다.
  - 중등도: 인슐린 인간(흡입, 속효성)
  - 등급 미상: clarithromycin, loratadine, montelukast, ketotifen, fexofenadine, ibuprofen, diclofenac
- **지식 그래프상 금기 관련 질환**: 간질, 만성 폐쇄성 폐질환(COPD), 기관지 질환, 섬망 등이 연결되어 있습니다. 이는 허가 문서가 아닌 지식 그래프 기반 정보이므로 참고용으로만 보시기 바랍니다.

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
신우신염에 대한 임상시험과 문헌이 전혀 없고, 기전상 연결고리도 확인되지 않습니다. 높은 모델 점수만으로는 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가 적응증, 경고, 금기를 확인하기 위한 허가사항 문서 확보
- 작용 기전 데이터 보완
- 신우신염과의 기전적 타당성을 설명할 전임상 또는 임상 근거
- 흡입 제형의 전신·신장 노출 한계를 고려한 투여 경로 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Relenza (zanamivir) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4e68930-4e6d-4d27-b1f0-abf60d12e28d) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

