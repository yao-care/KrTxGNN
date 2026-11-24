---
layout: default
title: Pertuzumab
parent: 모델 예측만 (L5)
nav_order: 595
evidence_level: L5
indication_count: 6
monitor_inn: "Pertuzumab"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
last_modified_at: 2026-11-24
description: "Pertuzumab: 예측 신규 적응증 외배엽간엽종 (ectomesenchymoma) (근거 수준 L5). 기존 적응증: ○ 전이성 유방암 - 전이성 질환에 대해 항-HER2 치료 또는 화학요법 치료를 받은 적이 없는, HER2…"
---

# Pertuzumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Pertuzumab: HER2 표적 단일클론항체 → 외배엽간엽종 (ectomesenchymoma)
{: .text-alpha }

## 한 문장 요약

Pertuzumab은 HER2(ERBB2)를 표적으로 하는 항체 의약품입니다.
TxGNN 모델은 **외배엽간엽종(ectomesenchymoma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 전이성 유방암 - 전이성 질환에 대해 항-HER2 치료 또는 화학요법 치료를 받은 적이 없는, HER2 양성 환자로서 전이성 또는 절제 불가능한 국소 재발성 유방암 환자에게 도세탁셀과 병용투여 ○ 조기 유방암 - 국소진행성, 염증성 또는 초기 단계(지름 2㎝ 초과)인 HER2 양성… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106366/EE)) |
| 예측 신규 적응증 | 외배엽간엽종 (ectomesenchymoma) |
| TxGNN 예측 점수 | 0.9971 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Pertuzumab 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “퍼투주맙은 인간 표피성장인자수용체 2 단백질(HER2)의 세포외 이량체화 도메인(Subdomain II)을 표적으로 하며, 이를 통해 HER2가 EGFR, HER3 및 HER4를 포함한 다른 HER 계열 구성원과 리간드 의존적으로 이종이량체를 형성하는 것을 차단한다. 그 결과, 퍼투주맙은 두 가지 주요 신호전달 경로인 미토겐 활성화 단백질(MAP) 키나아제 및 포스포이노시티드 3-키나아제(PI3K)를 통한 리간드 유발 세포내 신호전달을 억제한다.” 영어 원문: "Pertuzumab targets the extracellular dimerization domain (Subdomain II) of the human epidermal growth factor receptor 2 protein (HER2) and, thereby, blocks ligand-dependent heterodimerization of HER2 with other HER family members, including EGFR, HER3, and HER4. As a result, pertuzumab inhibits ligand-initiated intracellular signaling through two major signal pathways, mitogen-activated protein (MAP) kinase, and phosphoinositide 3-kinase (PI3K)." ([DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff), 버전 2026-04-30; 확인일 2026-11-19). 다만 약리 정보상 pertuzumab은 HER2(ERBB2) 수용체를 표적으로 하는 항체입니다.

외배엽간엽종은 신경외배엽성 성분과 간엽성 성분이 섞인 희귀 종양입니다. 이 종양이 HER2 신호에 의존한다는 근거는 확립되어 있지 않습니다. 따라서 기전상의 연결고리는 현재 뒷받침되지 않으며, 이 예측은 모델 점수에만 근거합니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202106366 | 페스코피하주사1200/600밀리그램(퍼투주맙/트라스투주맙) | 무색내지 옅은 황색의 액체가 충전된 무색투명한 바이알 주사제 | (주)한국로슈 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106366/EE) | 유효 |
| 201307522 | 퍼제타주(퍼투주맙) | 무색 또는 연한 갈색액이 충전된 바이알 주사제 | (주)한국로슈 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307522/EE) | 유효 |
| 202106365 | 페스코피하주사600/600밀리그램(퍼투주맙/트라스투주맙) | 무색내지 옅은 황색의 액체가 충전된 무색투명한 바이알 주사제 | (주)한국로슈 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202106365/EE) | 유효 |

<!-- licenses:end -->

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (HER2 표적 항체) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: Idelalisib과 중등도(Moderate) 수준의 상호작용이 보고되어 있습니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
외배엽간엽종에 대한 임상시험과 문헌이 모두 없고, HER2 기반의 기전적 연결도 확립되어 있지 않습니다. 모델 예측만 있는 L5 단계이므로 진행을 보류합니다.

**진행하려면 필요한 것:**
- 외배엽간엽종에서 HER2 발현 여부를 확인하는 전임상 또는 병리 연구
- 상세한 작용 기전(MOA) 데이터 보완
- 허가사항의 경고 및 금기 정보 확보와 안전성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

