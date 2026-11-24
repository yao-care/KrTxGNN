---
layout: default
title: Risdiplam
parent: 모델 예측만 (L5)
nav_order: 658
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Risdiplam: 예측 신규 적응증 여드름 (acne) (근거 수준 L5). 기존 적응증: 5q 척수성 근위축증의 치료"
monitor_inn: "Risdiplam"
predicted_indications: ["acne (disease)"]
---

# Risdiplam
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Risdiplam: 척수성 근위축증에서 여드름 (Acne)으로
{: .text-alpha }

## 한 문장 요약

Risdiplam은 SMN2 pre-mRNA 스플라이싱 조절제로, 원래 척수성 근위축증(SMA) 치료에 사용되는 약물입니다.
TxGNN 모델은 **여드름(acne)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건**, **문헌도 0편**으로 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 5q 척수성 근위축증의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202007490/EE)) |
| 예측 신규 적응증 | 여드름 (acne) |
| TxGNN 예측 점수 | 0.9945 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Risdiplam 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “리스디플람은 SMN 단백질 결핍을 초래하는 5q 염색체 돌연변이로 인한 척수성 근위축증(SMA) 환자를 치료하기 위해 고안된 생존 운동뉴런 2(SMN2) 스플라이싱 조절제이다. 시험관 내 분석과 SMA 형질전환 동물 모델 연구에서 리스디플람은 SMN2 전령 리보핵산(mRNA) 전사체의 엑손 7 포함과 뇌 내 전장 SMN 단백질 생성을 증가시키는 것으로 나타났다.” 영어 원문: "Risdiplam is a survival of motor neuron 2 (SMN2) splicing modifier designed to treat patients with spinal muscular atrophy (SMA) caused by mutations in chromosome 5q that lead to SMN protein deficiency. Using in vitro assays and studies in transgenic animal models of SMA, risdiplam was shown to increase exon 7 inclusion in SMN2 messenger ribonucleic acid (mRNA) transcripts and production of full-length SMN protein in the brain." ([DailyMed: Evrysdi (risdiplam) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eceb9a99-7191-4be5-87c3-0102707cf98e), 버전 2026-11-02; 확인일 2026-11-19). 알려진 정보에 따르면 risdiplam은 SMN2 exon 7 포함을 촉진하는 스플라이싱 조절제로, SMA에서 SMN 단백질 발현을 늘리는 약물입니다.

SMA는 신경근 질환이고 여드름은 피지선·모낭의 염증성 피부질환이어서 두 질환 사이에 뚜렷한 기전적 연결고리가 확인되지 않습니다. 이번 점수는 TxGNN 모델(딥러닝)이 산출한 것으로, 모델이 학습한 관련 질환 간 유사성을 반영할 수 있으나 생물학적 근거는 아닙니다. 이를 뒷받침하는 임상시험이나 문헌이 없어 기전적 타당성을 검증할 수 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202007490 | 에브리스디건조시럽0.75mg/mL(리스디플람) | 갈색 유리병에 든 분말 또는 덩어리가 있거나 고화된 분말로서 녹였을 때… | (주)한국로슈 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202007490/EE) | 유효 |
| 202501458 | 에브리스디정5밀리그램(리스디플람) | 연한 노란색의 원형 필름코팅정 | (주)한국로슈 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202501458/EE) | 유효 |

<!-- licenses:end -->

두 제품 모두 (주)한국로슈가 보유한 단일 성분 제제입니다.

## 안전성 고려사항

- **약물 상호작용**: DDInter 기준 중등도(Moderate) 상호작용 2건이 보고되었습니다.
  - Metformin
  - Methylnaltrexone

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
여드름 예측은 TxGNN 점수(0.9945)가 높지만 임상시험과 문헌이 전혀 없고 기전적 연결고리도 불분명한 L5 단계입니다. 현 시점에서는 재창출 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서)의 경고·금기 정보 확보 및 안전성 검토
- DrugBank 등에서 작용 기전(MOA) 데이터 확보 후 여드름 병태생리와의 연관성 분석
- 전임상 또는 기전 연구, 관련 문헌 및 임상시험 근거 확보
- 투여 경로(경구) 적합성 검토. 여드름은 통상 국소 치료가 중심이므로 필요합니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Evrysdi (risdiplam) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eceb9a99-7191-4be5-87c3-0102707cf98e) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

