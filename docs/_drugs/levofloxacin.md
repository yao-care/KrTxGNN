---
layout: default
title: Levofloxacin
parent: 모델 예측만 (L5)
nav_order: 473
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-15
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder"]
description: "Levofloxacin: 예측 신규 적응증 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) (근거 수준 L5). 기존 적응증: ○ 유효균종 황색포도구균, 표피포도구균, 화농연쇄구균, 폐렴연쇄구균, 헤모필루스 인플루엔자, 헤모필루스…"
---

# Levofloxacin
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

## Levofloxacin: 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## 한 문장 요약

Levofloxacin은 광범위 플루오로퀴놀론계 항균제입니다. TxGNN 모델은 **점상 상피성 각결막염(punctate epithelial keratoconjunctivitis)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험은 없고 관련 문헌은 **1편**(미포자충 각결막염 집단 발생 보고)뿐이며 Levofloxacin의 효과를 보여주지 못합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 유효균종 황색포도구균, 표피포도구균, 화농연쇄구균, 폐렴연쇄구균, 헤모필루스 인플루엔자, 헤모필루스 파라인플루엔자, 폐렴 막대균, 모락셀라 카타랄리스, 클라미디아 뉴모니아, 레지오넬라 뉴모니아, 엔테로콕쿠스 피칼리스, 엔테로박터 클로아카이, 대장균, 프로테우스 미라빌리스, 녹농균… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200705151/EE)) |
| 예측 신규 적응증 | 점상 상피성 각결막염 (punctate epithelial keratoconjunctivitis) |
| TxGNN 예측 점수 | 0.9992 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Levofloxacin 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “레보플록사신은 플루오로퀴놀론계 항균제에 속한다. […] 레보플록사신은 퀴놀론계 항균제인 라세미체 오플록사신의 L-이성질체이다. 오플록사신의 항균 활성은 주로 L-이성질체에 있다. 레보플록사신 및 기타 플루오로퀴놀론계 항균제의 작용 기전은 DNA 복제, 전사, 복구 및 재조합에 필요한 효소인 세균의 토포이소머라제 IV 및 DNA 자이라제(둘 다 제II형 토포이소머라제임)의 억제를 포함한다.” 영어 원문: "Levofloxacin is a member of the fluoroquinolone class of antibacterial agents. […] Levofloxacin is the L-isomer of the racemate, ofloxacin, a quinolone antimicrobial agent. The antibacterial activity of ofloxacin resides primarily in the L-isomer. The mechanism of action of levofloxacin and other fluoroquinolone antimicrobials involves inhibition of bacterial topoisomerase IV and DNA gyrase (both of which are type II topoisomerases), enzymes required for DNA replication, transcription, repair and recombination." ([DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5), 버전 2026-11-05; 확인일 2026-11-19). 알려진 정보로 Levofloxacin은 광범위 항균 활성을 가진 플루오로퀴놀론계 약물이며, 안과용 플루오로퀴놀론은 세균성 결막염에 사용됩니다. 한국에는 점안액 제형의 허가도 있습니다.

그러나 점상 상피성 각결막염은 바이러스(아데노바이러스) 또는 미포자충에 의한 경우가 많고, 플루오로퀴놀론은 이들 병원체에 대한 확립된 활성이 없습니다. 연결된 유일한 문헌도 미포자충 각결막염 집단 발생 보고로, Levofloxacin의 이득을 보여주지 않습니다. 높은 예측 점수는 모델의 예측일 뿐 임상적 근거가 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | 집단 발생 보고 | American Journal of Ophthalmology | 대만 수영장 물 오염과 관련된 미포자충 각결막염 집단 발생 보고. Levofloxacin의 효과에 대한 자료는 없음 |

## 한국 시판 정보

일부 허가만 발췌한 목록입니다(총 20건). 허가 적응증은 허가사항 문서 링크로만 제공되어 요약할 수 없으며, 상세 내용은 해당 허가사항을 참조하세요.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199400461 | 제일크라비트정 | 필름코팅정 | 허가 문서 참조 |
| 199800676 | 크라비트주 | 주사제(바이알) | 허가 문서 참조 |
| 200600109 | 크라비트정500밀리그람 | 필름코팅정 | 허가 문서 참조 |
| 200400034 | 레포신주 | 주사제(바이알) | 허가 문서 참조 |
| 201308471 | 카바스타점안액(레보플록사신수화물) | 점안액 | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 등급(Major)으로는 Tramadol, Hydrocortisone이 있습니다. 중등도(Moderate) 상호작용으로는 Abiraterone, Acarbose, Famotidine, Formoterol, Ketorolac, Ibuprofen, Metformin, Pioglitazone 등이 있습니다. 경미(Minor) 등급으로는 Paclitaxel, Aldesleukin, Altretamine 등이 있습니다.

그 외 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이 질환을 직접 다룬 임상시험이 없고 문헌도 Levofloxacin의 효과를 뒷받침하지 않아 근거 수준이 L5입니다. 원인이 바이러스 또는 미포자충인 경우가 많아 항균제의 기전상 근거도 약합니다.

**진행하려면 필요한 것:**
- 점상 상피성 각결막염에서 Levofloxacin의 효과를 직접 평가한 임상 또는 전임상 연구
- 허가사항 기반의 경고·금기 정보 확보
- 상세 작용 기전(MOA) 자료
- 원인 병원체(세균, 바이러스, 미포자충)별 적용 가능성 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

