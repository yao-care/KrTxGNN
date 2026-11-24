---
layout: default
title: Cabotegravir
parent: 모델 예측만 (L5)
nav_order: 167
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Cabotegravir: 예측 신규 적응증 류마티스 관절염 (Rheumatoid Arthritis) (근거 수준 L5). 기존 적응증: 바이러스학적으로 억제되어 있고 (HIV-1 RNA <50 copies/mL), 치료 실패 이력이 없으며…"
monitor_inn: "CABOTEGRAVIR"
predicted_indications: ["rheumatoid arthritis", "sclerosing cholangitis", "bronchitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "severe nonproliferative diabetic retinopathy"]
---

# Cabotegravir
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

## Cabotegravir: HIV 감염에서 류마티스 관절염으로
{: .text-alpha }

## 한 문장 요약

Cabotegravir는 HIV 인테그레이스 가닥 전이 억제제(INSTI)로, 국내에서 주사제(보카브리아주)로 시판되고 있습니다. TxGNN 모델은 **류마티스 관절염(rheumatoid arthritis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다. 따라서 이 예측은 컴퓨터 모델 예측 단계에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 바이러스학적으로 억제되어 있고 (HIV-1 RNA <50 copies/mL), 치료 실패 이력이 없으며 카보테그라비르또는 릴피비린에 알려진 또는 의심되는 내성이 없는 성인 환자에서 HIV-1 감염 치료를 위한 릴피비린 주사와의 병용요법 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202200534/EE)) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 0.9945 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Cabotegravir 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “카보테그라비르는 HIV-1 항레트로바이러스 약물이다. […] 카보테그라비르는 인테그라제 활성 부위에 결합하여 HIV 복제 주기에 필수적인 레트로바이러스 디옥시리보핵산(DNA) 통합의 가닥 전이 단계를 차단함으로써 HIV 인테그라제를 억제한다. 정제된 재조합 HIV-1 인테그라제를 이용한 가닥 전이 분석에서 카보테그라비르의 평균 50% 억제 농도(IC 50) 값은 3.0 nM이었다.” 영어 원문: "Cabotegravir is an HIV-1 antiretroviral drug. […] Cabotegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral deoxyribonucleic acid (DNA) integration that is essential for the HIV replication cycle. The mean 50% inhibitory concentration (IC 50 ) value of cabotegravir in a strand transfer assay using purified recombinant HIV-1 integrase was 3.0 nM." ([DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3), 버전 2025-04-11; 확인일 2026-11-19). 다만 Cabotegravir는 HIV 인테그레이스 가닥 전이 억제제(INSTI) 계열로 알려져 있으며, 바이러스 DNA가 숙주 유전체에 삽입되는 과정을 차단하는 방식으로 작용합니다.

이 기전은 자가면역성 관절 염증과 직접적인 연관성이 확립되어 있지 않습니다. 따라서 류마티스 관절염에 대한 기전적 연결고리는 현재 평가할 수 없으며, 가능한 가설을 먼저 세우고 전임상 단계에서 검증해야 합니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것이며, 모델이 학습한 관련 질환 간 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

참고로 모델이 예측한 다른 후보(경화성 담관염, 기관지염, 군발성 소안구-근위지 이형성 증후군, 중증 비증식성 당뇨망막병증)도 모두 L5 수준으로, 임상시험과 문헌 근거가 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202200534 | 보카브리아주(카보테그라비르) | 흰색 내지 옅은 분홍색을 띄는 자유유동 현탁액이 갈색투명한 유리 바이알에… | (주)글락소스미스클라인 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202200534/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 7건이 확인되었으며, 모두 중등도(Moderate)입니다. 모두 제산제 및 무기염류 성분입니다.
  - 탄산칼슘(Calcium carbonate)
  - 수산화알루미늄(Aluminum hydroxide)
  - 탄산마그네슘(Magnesium carbonate)
  - 수산화마그네슘(Magnesium hydroxide)
  - 산화마그네슘(Magnesium oxide)
  - 탄산수소나트륨(Sodium bicarbonate)
  - 시트르산나트륨(Sodium citrate)

그 외 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
류마티스 관절염에 대한 예측은 TxGNN 점수(0.9945)에만 근거하며, 임상시험과 문헌 근거가 전혀 없습니다. 작용 기전상의 연결고리도 확인되지 않고, 허가사항상의 경고·금기 정보도 확보되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서)의 경고 및 금기 정보 확보 (안전성 검토 진행의 필수 선행 조건)
- 작용 기전(MOA) 데이터 보완 (DrugBank 등)
- 류마티스 관절염과의 기전적 연결 가설 수립 및 전임상 검증
- 관련 임상시험 및 문헌 탐색
- 투여 경로(현재 주사제만 시판) 적합성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

