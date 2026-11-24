---
layout: default
title: Anastrozole
parent: 모델 예측만 (L5)
nav_order: 75
evidence_level: L5
indication_count: 5
monitor_inn: "Anastrozole"
predicted_indications: ["neuroblastoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "monocytic leukemia"]
last_modified_at: 2026-11-24
description: "Anastrozole: 예측 신규 적응증 신경모세포종 (neuroblastoma) (근거 수준 L5). 기존 적응증: 1. 폐경기 이후 여성의 진행성 유방암의 치료(이 요법 이전의 타목시펜 치료시 임상반응을 나타내지 않는…"
---

# Anastrozole
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

## Anastrozole: 방향화효소 억제제 → 신경모세포종 (neuroblastoma)
{: .text-alpha }

## 한 문장 요약

Anastrozole은 방향화효소(아로마타아제) 억제제 계열의 약물입니다. TxGNN 모델은 **신경모세포종(neuroblastoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 따라서 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 폐경기 이후 여성의 진행성 유방암의 치료(이 요법 이전의 타목시펜 치료시 임상반응을 나타내지 않는 에스트로겐 수용체 음성인 환자에서, 이 약의 유효성은 입증되지 않았다.) 2. 호르몬 수용체 양성인 폐경기 이후 여성의 조기 유방암의 보조 치료 조기 유방암의 보조 요법으로 2 ∼… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200808866/EE)) |
| 예측 신규 적응증 | 신경모세포종 (neuroblastoma) |
| TxGNN 예측 점수 | 0.9953 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Anastrozole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “많은 유방암의 성장은 에스트로겐에 의해 자극되거나 유지된다. 폐경 후 여성에서 에스트로겐은 주로 부신 안드로겐(주로 안드로스텐디온 및 테스토스테론)을 에스트론 및 에스트라디올로 전환하는 아로마타아제 효소의 작용으로부터 유래한다. […] 아나스트로졸은 선택적 비스테로이드성 아로마타아제 억제제이다.” 영어 원문: "The growth of many cancers of the breast is stimulated or maintained by estrogens. In postmenopausal women, estrogens are mainly derived from the action of the aromatase enzyme, which converts adrenal androgens (primarily androstenedione and testosterone) to estrone and estradiol. […] Anastrozole is a selective non-steroidal aromatase inhibitor." ([DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de), 버전 2026-03-02; 확인일 2026-11-19). Anastrozole은 방향화효소 억제제로 알려져 있으나, 이 보고서를 위해 수집된 데이터에서는 신경모세포종과 연결되는 기전을 확인할 수 없었습니다.

신경모세포종은 대표적인 에스트로겐 의존성 종양이 아니며, 방향화효소 의존 기전이 있다는 근거도 제시된 데이터에서 확인되지 않습니다. 0.9953이라는 높은 점수는 네트워크 기반 예측 결과일 뿐, 실제 생물학적 타당성을 입증하지는 않습니다. 이 예측은 인공적인 결과일 가능성이 높습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200808866 | 에이덱스정(아나스트로졸) | 흰색의 원형 필름코팅정 | 광동제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200808866/EE) | 유효 |
| 200806188 | 테바아나스트로졸정1밀리그램 | 한면에 93, 다른 면에 A10이 각인된 흰색 내지 밝은 회색의 원형 필… | (주)한독테바 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200806188/EE) | 유효 |
| 200009025 | 아리미덱스정(아나스트로졸) | 백색의 원형 필름코팅정 | 한국아스트라제네카(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200009025/EE) | 유효 |
| 200805384 | 아나스토정(아나스트로졸) | 흰색의 원형 필름코팅정 | (주)보령 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200805384/EE) | 유효 |

<!-- licenses:end -->

4건 모두 단일 성분 제제이며 유효 상태로 기록되어 있습니다.

## 세포독성

Anastrozole은 호르몬 치료제로, 기존 세포독성 항암제와는 성격이 다릅니다. 세포독성 관련 데이터는 확인되지 않았으므로 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

- **약물 상호작용**: 100건의 상호작용 후보가 조회되었으며, 모두 위험 등급이 확인되지 않았습니다. 일부 예시는 다음과 같습니다.
  - Bupropion, Pantoprazole, Glimepiride, Morphine, Metformin
  - Omeprazole, Rosiglitazone, Simvastatin, Prednisone, Acetylsalicylic acid

세부 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
신경모세포종에 대해 직접 연구한 임상시험이나 문헌이 없고, 모델 점수 외에 기전적 근거도 확인되지 않습니다. 근거 수준은 L5로, 현 단계에서 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 신경모세포종과 방향화효소 경로의 연관성을 보여주는 전임상 또는 기전 연구
- 허가사항(경고, 금기)의 확보 및 분석
- 상세한 작용 기전(MOA) 데이터
- 소아 환자 대상 안전성 및 내분비 영향 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

