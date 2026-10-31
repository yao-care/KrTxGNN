---
layout: default
title: Aceclofenac
parent: 모델 예측만 (L5)
nav_order: 17
evidence_level: L5
indication_count: 7
monitor_inn: "Aceclofenac"
predicted_indications: ["brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx", "Kummell disease"]
last_modified_at: 2026-10-31
description: "Aceclofenac: 예측 신규 적응증 brachyolmia-amelogenesis imperfecta syndrome (근거 수준 L5). 기존 적응증: 허가 문서가 링크로만 제공되어 구체적인 적응증 문구를 확인할 수 없음"
---

# Aceclofenac
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

## Aceclofenac: 기존 허가 적응증에서 brachyolmia-amelogenesis imperfecta syndrome으로
{: .text-alpha }

## 한 문장 요약

Aceclofenac은 한국에서 단일 성분 제제로 다수 허가된 비스테로이드성 소염진통제(NSAID)입니다. TxGNN 모델은 **brachyolmia-amelogenesis imperfecta syndrome**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 문서가 링크로만 제공되어 구체적인 적응증 문구를 확인할 수 없음 |
| 예측 신규 적응증 | brachyolmia-amelogenesis imperfecta syndrome |
| TxGNN 예측 점수 | 0.9989 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 18건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 aceclofenac은 COX-2 선호성 NSAID로 알려져 있으며, 염증과 통증을 줄이는 약물입니다.

예측 질환인 brachyolmia-amelogenesis imperfecta syndrome은 척추를 침범하는 희귀 유전성 골격·치아 질환으로, TGF-β 신호 경로와 관련된 LTBP3 변이가 연관되어 있습니다. COX 억제와 이 질환의 근본 병리 사이에 알려진 연결고리는 없습니다. 기껏해야 증상성 통증 완화에 NSAID를 쓸 수 있는 정도이며, 이는 질병 자체를 변화시키는 효과가 아닙니다.

따라서 이 예측은 TxGNN 모델(딥러닝)이 계산한 결과이며, 관련 질환 간에 모델이 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다. 기전상 타당성은 현재 입증되지 않았습니다.

## 한국 시판 정보

아래는 현재 확인된 단일 성분 허가 중 주요 5건입니다. 허가 적응증 문구는 링크 형태의 문서 참조만 제공되어 본문을 요약할 수 없었습니다. 전체 목록은 일부일 수 있습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201402186 | 아세틸론정 | 흰색의 원형 필름코팅제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201402186/EE) |
| 200411098 | 아세민정 | 흰색의 원형 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200411098/EE) |
| 201906109 | 아클페낙CR서방정 | 흰색의 장방형 서방성 필름코팅정 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201906109/EE) |
| 201502927 | 휴니즈아세클로페낙정 | 흰색의 원형 필름코팅정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201502927/EE) |
| 199400486 | 에어탈정 | 코팅된 흰색의 정제 | [허가 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199400486/EE) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환을 직접 다룬 임상시험이나 문헌이 없고, 기전상 연결고리도 확인되지 않아 근거 수준이 L5입니다. 모델 점수가 높더라도 현재 데이터만으로는 진행을 정당화하기 어렵습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서) 원문을 확보하여 기존 적응증, 경고, 금기 확인
- 작용 기전(MOA) 데이터 보강 (예: DrugBank 조회)
- 이 질환과 aceclofenac에 대한 PubMed 및 임상시험 등록 검색
- 증상성 통증 관리 목적으로 한정할 경우, 질병 수정 효과와 구분한 별도의 평가 계획
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

