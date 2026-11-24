---
layout: default
title: Clarithromycin
parent: 모델 예측만 (L5)
nav_order: 219
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Clarithromycin: 예측 신규 적응증 다클론성 과점도 증후군 (Polyclonal Hyperviscosity Syndrome) (근거 수준 L5). 기존 적응증: ○ 유효균종 황색포도구균, 폐렴연쇄구균, 스트렙토콕쿠스 피오게네스(그룹 A-베타용혈성), 리스테리아…"
monitor_inn: "CLARITHROMYCIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
---

# Clarithromycin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **5** 건
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

## Clarithromycin: 세균 감염증에서 다클론성 과점도 증후군으로
{: .text-alpha }

## 한 문장 요약

Clarithromycin은 마크로라이드 계열 항생제로, 한국에서 단일제로 20건의 허가증이 유효하게 시판되고 있습니다.
TxGNN 모델은 **다클론성 과점도 증후군(Polyclonal Hyperviscosity Syndrome)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 유효균종 황색포도구균, 폐렴연쇄구균, 스트렙토콕쿠스 피오게네스(그룹 A-베타용혈성), 리스테리아 모노사이토제니 스, 스트렙토콕쿠스 아갈락티에(그룹 B), 스트렙토콕쿠스 비리단스, 인플루엔자균, 파라인플루엔자균, 모락 셀라 카타랄리스, 레기오넬라 뉴모필라, 보르데텔라 백일해… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201906074/EE)) |
| 예측 신규 적응증 | 다클론성 과점도 증후군 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 예측 점수 | 0.9935 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Clarithromycin 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “클라리스로마이신은 마크로라이드계 항균제이다. […] 클라리스로마이신은 감수성 세균의 50S 리보솜 소단위에 결합하여 단백질 합성을 억제함으로써 항균 작용을 나타낸다.” 영어 원문: "Clarithromycin is a macrolide antimicrobial drug. […] Clarithromycin exerts its antibacterial action by binding to the 50S ribosomal subunit of susceptible bacteria resulting in inhibition of protein synthesis." ([DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460), 버전 2026-11-12; 확인일 2026-11-19). 알려진 정보에 따르면 Clarithromycin은 마크로라이드계 항생제이며, 항균 작용 외에 면역조절 및 항염증 작용이 보고되어 있습니다.

다만 다클론성 과점도 증후군은 다클론성 면역글로불린 증가로 혈액 점도가 높아지는 상태입니다. Clarithromycin과의 기전적 연결은 이번 데이터에서 확인되지 않으며, 추정 수준에 머뭅니다. 높은 TxGNN 점수 외에 이를 뒷받침하는 근거가 없습니다.

참고로 같은 약물에 대해 예측된 다른 후보는 다음과 같습니다.

| 순위 | 예측 질환 | 점수 | 근거 수준 | 비고 |
|------|----------|------|----------|------|
| 2 | 고아밀라아제혈증 (Hyperamylasemia) | 0.9935 | L5 | 증례 보고 1편, 간접적 연관 |
| 3 | 선천성 무알부민혈증 | 0.9921 | L5 | 근거 없음, 생물학적 개연성 매우 낮음 |
| 4 | 점상 상피성 각결막염 | 0.9911 | L5 | 관찰 연구 1편, 마크로라이드의 안구 표면 염증 적용 가능성 |
| 5 | 혈액형 부적합 | 0.9907 | L5 | 근거 없음 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201906074 | 클래리마신정500mg(클래리트로마이신) | 노란색의 타원형 필름코팅정 | (주)마더스제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201906074/EE) | 유효 |
| 201507840 | 클라이신정500mg(클래리트로마이신) | 황색의 장방형 필름코팅정 | (주)씨티씨바이오 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201507840/EE) | 유효 |
| 201902148 | 클래정250mg(클래리트로마이신) | 노란색의 타원형 필름코팅정 | (주)보령바이오파마 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201902148/EE) | 유효 |
| 200707458 | 크래리신정500밀리그램(클래리트로마이신) | 바닐라향이 나는 노란색의 장방형 필름코팅정 | 명문제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200707458/EE) | 유효 |
| 201604097 | 클래니즈정250mg(클래리트로마이신) | 바닐라향이 나는 노란색의 타원형 필름코팅정 | (주)휴온스메디텍 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201604097/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

이 외에도 건조시럽(수출용)을 포함해 총 20건이 유효합니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 그중 일부는 다음과 같습니다.
  - 주요(Major): Abemaciclib, Fentanyl, Acalabrutinib
  - 중등도(Moderate): Paclitaxel, Tramadol, Nifedipine, Ethinylestradiol, Hydrocortisone 등
  - 경미(Minor): Dolutegravir, Zidovudine, Loratadine
- **지식 그래프상 금기 관련 질환**(허가사항이 아닌 모델 지식 그래프 기준): QT 연장 증후군, 심실 빈맥, 토르사드 드 푸앵트, 간부전·간질환, 신장 질환, 포르피린증, 중증 근무력증, 담즙정체, 골다공증, *Clostridium difficile* 대장염 등.

허가사항상의 경고 및 금기는 이번 데이터에 없으므로, 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다클론성 과점도 증후군에 대해서는 임상시험과 문헌이 전혀 없고 TxGNN 점수만 있어 근거 수준이 L5입니다. 기전 데이터도 없어 개연성을 평가할 수 없습니다. 허가사항의 경고·금기 정보도 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서) 확보: 적응증, 경고, 금기 (현재 차단 수준의 누락)
- 작용 기전(MOA) 데이터 보완 (DrugBank 조회)
- 다클론성 과점도 증후군 관련 문헌 및 임상시험 탐색
- 근거가 상대적으로 나은 후보(점상 상피성 각결막염, L4)에 대한 전문 검토로 우선순위 재평가
- QT 연장 및 CYP3A4 관련 상호작용 등 심장·약물 상호작용 위험 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

