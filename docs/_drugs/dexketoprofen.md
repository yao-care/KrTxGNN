---
layout: default
title: Dexketoprofen
parent: 모델 예측만 (L5)
nav_order: 271
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dexketoprofen: 예측 신규 적응증 건염 (Tendinitis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 확인되지 않았습니다(허가증 원문 링크만 확인됨). 허가사항을 참조하세요"
monitor_inn: "dexketoprofen"
predicted_indications: ["tendinitis", "fibromyalgia", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis", "migraine disorder", "headache disorder", "migraine with brainstem aura", "exostosis", "congenital hypotrichosis milia"]
---

# Dexketoprofen
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## 덱스케토프로펜(Dexketoprofen): 기존 진통 적응증에서 건염(Tendinitis)으로
{: .text-alpha }

## 한 문장 요약

덱스케토프로펜은 NSAID(비스테로이드 소염진통제) 계열 약물로, 한국에서는 주사제(케랄주)로 시판되고 있습니다.
TxGNN 모델은 **건염(Tendinitis)**에 효과가 있을 수 있다고 예측하지만, 직접 근거는 없습니다. 관련 임상시험은 **0건**이고, 간접 근거인 **문헌 1편**(비외상성 근골격계 통증 RCT)만 확인되었습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 확인되지 않았습니다(허가증 원문 링크만 확인됨). 허가사항을 참조하세요. |
| 예측 신규 적응증 | 건염 (Tendinitis) |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L5 (직접 근거 없음, 간접 근거만 존재) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 덱스케토프로펜은 COX-1/COX-2를 억제하는 NSAID입니다. 프로스타글란딘 매개 염증과 통증을 줄이므로 힘줄 염증(건염)의 증상 완화에도 적용될 가능성이 있습니다.

다만 근거는 간접적입니다. 확인된 문헌은 응급실에서 비외상성 근골격계 통증 환자를 대상으로 정맥 투여 덱스케토프로펜과 파라세타몰을 비교한 연구 1건뿐이며, 건염 환자만을 대상으로 한 연구가 아닙니다. 따라서 TxGNN의 높은 점수는 계산상의 예측으로 보는 것이 안전합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT (간접 근거) | The American Journal of Emergency Medicine | 응급실 내 비외상성 근골격계 통증에서 정맥 덱스케토프로펜과 파라세타몰의 통증 완화 효과를 비교했습니다. 건염에만 국한된 연구는 아닙니다. |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200706794 | 케랄주(덱스케토프로펜트로메타몰) | 주사제 (무색투명한 액, 황갈색 유리 앰플) | 허가증 원문 참조 ([링크](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200706794/EE)) |

제조사는 한국메나리니(주)이며, 단일제로 유효한 허가입니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
건염에 대한 직접적인 임상시험과 문헌이 없고 간접 근거 1편뿐이어서 현 단계에서는 진행을 보류하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 건염 환자를 직접 대상으로 한 임상시험 또는 문헌 근거
- 허가사항의 경고·금기 정보 확인 (안전성 검토의 선행 조건)
- 상세한 작용 기전(MOA) 데이터 보완

**참고:** 같은 약물의 다른 예측 적응증 중 **편두통(Migraine disorder)**은 근거 수준 L1, 권장 결정 "Proceed with Guardrails"로, 훨씬 강한 근거를 갖고 있습니다. 응급실 급성 편두통 대상 임상시험 5건(위약 대조 Phase 4 NCT02159547 포함)과 RCT 메타분석(PMID 31725614)이 있습니다. 별도의 우선 검토 대상으로 고려할 만합니다. 이 경우에도 NSAID 공통 주의사항(위장관, 신장, 심혈관, 출혈 위험)을 가드레일로 적용해야 합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

