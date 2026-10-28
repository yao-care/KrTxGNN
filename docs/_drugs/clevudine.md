---
layout: default
title: Clevudine
parent: 모델 예측만 (L5)
nav_order: 221
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Clevudine: 예측 신규 적응증 만성 C형 간염 바이러스 감염 (chronic hepatitis C virus infection) (근거 수준 L5). 기존 적응증: 만성 B형 간염 (허가증에는 적응증 본문 없이 문서 링크만 등록되어 있어, 임상시험·문헌 자료를 근거로 기재)"
monitor_inn: "CLEVUDINE"
predicted_indications: ["chronic hepatitis C virus infection", "hepatitis C virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease"]
---

# Clevudine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **7** 건
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

## 클레부딘: 만성 B형 간염에서 만성 C형 간염으로
{: .text-alpha }

## 한 문장 요약

클레부딘(Clevudine)은 원래 만성 B형 간염 치료에 사용되는 뉴클레오시드 유사체 항바이러스제입니다.
TxGNN 모델은 **만성 C형 간염 바이러스 감염(chronic hepatitis C virus infection)**에도 효과가 있을 수 있다고 예측했지만, 이 적응증을 직접 검증한 **임상시험은 0건**이고 **문헌 2편**은 B형·C형 간염을 함께 다룬 일반 리뷰뿐입니다. 따라서 현재는 모델 예측 단계(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 만성 B형 간염 (허가증에는 적응증 본문 없이 문서 링크만 등록되어 있어, 임상시험·문헌 자료를 근거로 기재) |
| 예측 신규 적응증 | 만성 C형 간염 바이러스 감염 (chronic hepatitis C virus infection) |
| TxGNN 예측 점수 | 0.9996 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 등록되어 있지 않습니다. 다만 클레부딘은 피리미딘계 L-뉴클레오시드 유사체(L-FMAU)로 알려져 있습니다. 세포 안에서 활성형인 삼인산체로 바뀌어 B형 간염 바이러스(HBV)의 DNA 중합효소(역전사효소)를 억제하고, 바이러스 DNA 합성을 막습니다.

C형 간염 바이러스(HCV)는 DNA가 아닌 RNA 바이러스로, NS5B RNA 의존성 RNA 중합효소를 통해 복제합니다. 클레부딘이 억제하는 HBV 중합효소와는 표적 계열이 다르므로, 기전상 C형 간염에 효과가 있다고 볼 근거는 확인되지 않았습니다.

이 높은 예측 점수는 TxGNN 모델(딥러닝)이 산출한 값이며, 검증된 기전이 아니라 모델이 관련 질환들 사이에서 학습한 유사성을 반영한 것일 수 있습니다. 즉 지금은 "간염 관련 항바이러스제"라는 연관성만 있을 뿐, HCV에 대한 직접 근거는 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wiener medizinische Wochenschrift | 만성 B형·C형 간염의 현재 치료와 향후 전망. B형 간염에서는 페그인터페론이 라미부딘 단독요법보다 효과적일 수 있다고 정리 |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatric drugs | 소아 만성 간질환의 내과적 관리(치료 가능·잠재적 완치 가능 질환 중심). 클레부딘의 C형 간염 효능을 직접 다룬 자료는 아님 |

두 편 모두 클레부딘의 C형 간염 효과를 직접 검증한 연구가 아닙니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200607938 | 레보비르캡슐30밀리그램(클레부딘) | 경질캡슐 (부광약품) | 허가 문서 링크로만 등록됨 ([허가 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200607938/EE)) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로, 클레부딘 관련 문헌에는 장기 투여 시 미토콘드리아성 근병증이 보고되어 있습니다(PMID 28960041). 어떤 적응증이든 사용하려면 CK 등 근육 관련 모니터링이 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
HCV는 HBV와 복제 기전과 표적 효소가 달라 기전적 근거가 없고, 이 적응증을 직접 검증한 임상시험이나 문헌도 없습니다. 예측 점수(0.9996)는 높지만 모델 예측일 뿐이므로 지금은 개발을 진행할 수 없습니다.

**진행하려면 필요한 것:**
- HCV 복제 모델(레플리콘 등)에서 클레부딘의 항바이러스 활성을 확인하는 전임상(in vitro) 연구
- HCV NS5B 중합효소에 대한 억제 가능성을 검토하는 기전 연구
- 허가사항(경고·금기)의 확보 및 분석, 근병증 위험에 대한 모니터링 계획
- 현재 HCV 표준치료제(직접작용 항바이러스제)와 비교한 필요성 평가

**참고:** 같은 예측 목록의 B형 간염(2순위)은 클레부딘의 기존 허가 적응증입니다. 여러 Phase 3 RCT가 있어 근거 수준은 L1이고 결정은 Proceed with Guardrails이지만, 신규 적응증이 아니라 허가 범위 내 사용입니다. 이 경우에도 근병증 모니터링과 엔테카비르·테노포비르 등 1차 약제와의 위험·이익 비교가 필요합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

