---
layout: default
title: Paclitaxel
parent: 모델 예측만 (L5)
nav_order: 573
evidence_level: L5
indication_count: 2
monitor_inn: "Paclitaxel"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
last_modified_at: 2026-11-24
description: "Paclitaxel: 예측 신규 적응증 부수막 배아성 횡문근육종 (parameningeal embryonal rhabdomyosarcoma) (근거 수준 L5). 기존 적응증: 1. 난소암 1) 다른 화학요법제와 병용하여 1차 요법제로 사용 2) 표준 요법에 실패한 전이성 난소암의…"
---

# Paclitaxel
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

## Paclitaxel: 미세소관 안정화 항종양제 → 부수막 배아성 횡문근육종 (parameningeal embryonal rhabdomyosarcoma)
{: .text-alpha }

## 한 문장 요약

Paclitaxel은 미세소관을 안정화하는 항종양제로, 국내에서 단일 성분 제품으로 허가되어 있습니다.
TxGNN 모델은 **부수막 배아성 횡문근육종(parameningeal embryonal rhabdomyosarcoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험과 문헌은 **0건**으로 모델 예측 외의 근거가 없습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 난소암 1) 다른 화학요법제와 병용하여 1차 요법제로 사용 2) 표준 요법에 실패한 전이성 난소암의 치료에 2차 요법제로 사용 2. 유방암 1) 표준요법에 실패한 전이성 유방암의 치료에 2차 요법제로 사용 2) 결절 양성 유방암의 보조치료:표준 독소루비신 함유 병용 화학요법후… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200308579/EE)) |
| 예측 신규 적응증 | 부수막 배아성 횡문근육종 (parameningeal embryonal rhabdomyosarcoma) |
| TxGNN 예측 점수 | 0.9973 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 14건 / 전체 16건) |
| 허가증 수 | 16건 (유효 14건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Paclitaxel 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “주사용 현탁액용 파클리탁셀 단백질 결합 입자(알부민 결합)는 미세소관 억제제로서, 튜불린 이량체로부터 미세소관의 조립을 촉진하고 탈중합을 방지함으로써 미세소관을 안정화시킨다. 이러한 안정성은 필수적인 간기 및 유사분열 세포 기능에 필수적인 미세소관 망의 정상적인 동적 재구성을 억제한다.” 영어 원문: "Paclitaxel protein-bound particles for injectable suspension (albumin-bound) is a microtubule inhibitor that promotes the assembly of microtubules from tubulin dimers and stabilizes microtubules by preventing depolymerization. This stability results in the inhibition of the normal dynamic reorganization of the microtubule network that is essential for vital interphase and mitotic cellular functions." ([DailyMed: Paclitaxel Protein-Bound Particles For Injectable Suspension (Albumin-Bound) (paclitaxel) prescribing information, NorthStar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e9d5093-fbfc-470a-8520-811c46a8870c), 버전 2025-09-17; 확인일 2026-11-19). Paclitaxel은 일반적으로 미세소관을 안정화하여 세포분열을 억제하는 항종양제로 알려져 있어, 빠르게 분열하는 종양세포에 이론적으로 작용할 수 있습니다.

다만 횡문근육종의 표준 치료는 vincristine, actinomycin D, cyclophosphamide 기반의 병용 화학요법이며, paclitaxel은 확립된 역할이 없습니다. 항유사분열 기전에 근거한 연결고리는 현재로서는 이론적 추정에 그칩니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199604958 | 탁솔주(파클리탁셀) | 무색의 바이알에 들어있는 무색 또는 미황색의 점성이 있는 맑은 주사액 | (주)보령 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199604958/EE) | 유효 |
| 199801795 | 한신파클리탁셀주(수출용) | 무색-담황색의 투명한 점성주사액 | (주)한국신약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199801795/EE) | 유효 |
| 199803971 | 제넥솔주(파클리탁셀) | 이 약은 무색 바이알내에 무색-담황색의 투명한 점성액이 들어있는 주사제이… | (주)삼양바이오팜 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199803971/EE) | 유효 |
| 199901631 | 유니탁셀주(파클리탁셀)(수출명:NeotaxlInj.)(수출용) | 등명한 무색-미황색의 점성이 있는 용액이 든 갈색 바이알 주사제 | 한국유나이티드제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199901631/EE) | 유효 |
| 200103889 | 제넥솔피엠주(파클리탁셀) | 이 약은 무색투명한 바이알내에 백색~미황색의 가루 또는 다공질의 가벼운… | (주)삼양바이오팜 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200103889/EE) | 유효 |

위 표는 허가 16건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: Aprepitant, Cimetidine, Clarithromycin, Clotrimazole, Dexamethasone, Eliglustat, Metronidazole, Miconazole, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole, Troglitazone
  - 경미: Ascorbic acid, Levofloxacin
  - 등급 미상: Glimepiride, Doxycycline, Morphine, Metformin, Omeprazole

허가사항의 경고 및 금기는 이번 자료에서 확인되지 않았으므로 허가사항(첨부문서)을 참조하세요.

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (탁산 계열) |
| 골수억제 위험 | 고 (탁산 계열의 일반적 특성, 호중구감소 등) |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC(분획 포함), 간기능, 말초신경 증상 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

허가사항의 경고 및 주의사항을 함께 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 점수는 높지만 이 질환을 직접 다룬 임상시험이나 문헌이 없고, 표준 치료에서 paclitaxel의 역할도 확립되어 있지 않습니다.

**진행하려면 필요한 것:**
- 횡문근육종에 대한 paclitaxel의 전임상 및 임상 연구 근거 확보
- 작용 기전(MOA) 데이터 보완
- 허가사항의 경고·금기 정보 확인
- 소아 및 해당 질환 환자군에 대한 안전성 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Paclitaxel Protein-Bound Particles For Injectable Suspension (Albumin-Bound) (paclitaxel) prescribing information, NorthStar Rx LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e9d5093-fbfc-470a-8520-811c46a8870c) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

