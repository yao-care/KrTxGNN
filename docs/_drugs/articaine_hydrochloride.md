---
layout: default
title: Articaine Hydrochloride
parent: 모델 예측만 (L5)
nav_order: 92
evidence_level: L5
indication_count: 4
drugbank_id: DB09009
monitor_inn: "Articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma"]
last_modified_at: 2026-11-24
description: "Articaine Hydrochloride: 예측 신규 적응증 통풍 (gout) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Articaine Hydrochloride
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

## Articaine Hydrochloride: 통풍 (gout)
{: .text-alpha }

## 한 문장 요약

Articaine Hydrochloride는 치과 등에서 사용되는 아미드계 국소마취제입니다. TxGNN 모델은 **통풍(gout)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 직접 뒷받침하는 임상시험과 문헌은 **0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201202809/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308019/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308020/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502597/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502596/EE) |
| 예측 신규 적응증 | 통풍 (gout) |
| TxGNN 예측 점수 | 0.9958 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 5건) |
| 허가증 수 | 5건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 일반적으로 articaine은 전압 의존성 나트륨 채널을 차단하는 아미드계 국소마취제로 알려져 있습니다.

그러나 이 기전과 요산 대사 또는 통풍성 염증 사이에서 타당한 연결 고리는 제공된 데이터에서 확인되지 않습니다. 국소마취 효과가 급성 통풍 통증을 완화할 수는 있어도 증상 완화 수준에 그치며, 질병 경과를 바꾸는 효과로 보기는 어렵습니다. 높은 예측 점수(0.9958)는 모델 예측일 뿐이며, 이를 지지하는 실제 연구는 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201202809 | 유니온아티카인·에피네프린주1/10만(수출용) | 무색 투명한 액체가 충진된 무색의 카트리지식 앰플 주사제 | 한국유니온제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201202809/EE) | 유효 |
| 200308019 | 셉타네스트주1/100,000 | 무색투명한 액체가 충진된 카트리지식 앰플 | 신원덴탈(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308019/EE) | 유효 |
| 200308020 | 셉타네스트주1/200,000 | 무색투명한 액체가 충진된 카트리지식 앰플 | 신원덴탈(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308020/EE) | 유효 |
| 200502597 | 휴온스아티카인에피네프린주1/20만(수출용) | 무색 투명한 액체가 충진된 무색의 카트리지식 앰플 주사제 | (주)휴온스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502597/EE) | 유효 |
| 200502596 | 휴온스아티카인에피네프린주1/10만 | 무색 투명한 액체가 충진된 무색의 카트리지식 앰플 주사제 | (주)휴온스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502596/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
통풍에 대한 임상시험과 문헌이 전혀 없고, 기전상 연결 고리도 확인되지 않아 모델 예측만 존재하는 L5 수준입니다. 추가 근거 없이는 진행을 권고하기 어렵습니다.

**진행하려면 필요한 것:**
- 통풍에 대한 전임상 또는 임상 연구 근거
- 작용 기전(MOA) 데이터 확보 및 통풍 병태와의 기전적 연관성 검토
- 허가사항(경고, 금기)의 확보 및 안전성 검토
- 투여 경로 적합성 평가 (현재 주사제 카트리지 제형만 확인됨)
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

