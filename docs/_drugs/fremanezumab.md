---
layout: default
title: Fremanezumab
parent: 모델 예측만 (L5)
nav_order: 365
evidence_level: L5
indication_count: 1
monitor_inn: "FREMANEZUMAB"
predicted_indications: ["atrophoderma vermiculata"]
last_modified_at: 2026-11-20
description: "Fremanezumab: 예측 신규 적응증 위축성 벌레먹은 모양 피부위축증 (atrophoderma vermiculata) (근거 수준 L5). 기존 적응증: 성인에서의 편두통의 예방 체중 45kg 이상인 6-17세 소아에서의 삽화성 편두통의 예방"
---

# Fremanezumab
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

## Fremanezumab: 항CGRP 단클론 항체 → 위축성 벌레먹은 모양 피부위축증 (atrophoderma vermiculata)
{: .text-alpha }

## 한 문장 요약

Fremanezumab은 항CGRP 계열의 유전자재조합 단클론 항체 주사제로, 한국에서 허가를 받아 사용되고 있습니다.
TxGNN 모델은 **위축성 벌레먹은 모양 피부위축증(atrophoderma vermiculata)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 성인에서의 편두통의 예방 체중 45kg 이상인 6-17세 소아에서의 삽화성 편두통의 예방 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202105577/EE)) |
| 예측 신규 적응증 | 위축성 벌레먹은 모양 피부위축증 (atrophoderma vermiculata) |
| TxGNN 예측 점수 | 0.9904 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Fremanezumab 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “프레마네주맙-vfrm은 칼시토닌 유전자 관련 펩티드 (CGRP) 리간드에 결합하여 CGRP가 수용체에 결합하는 것을 차단하는 인간화 단일클론항체이다.” 영어 원문: "Fremanezumab-vfrm is a humanized monoclonal antibody that binds to calcitonin gene-related peptide (CGRP) ligand and blocks its binding to the receptor." ([DailyMed: Ajovy (fremanezumab-vfrm) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e344ea-5916-4947-b6f2-4a76ccc04b6b), 버전 2026-06-05; 확인일 2026-11-19). 작용 기전은 출처와 함께 위에 인용되어 있습니다 ([DailyMed](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e344ea-5916-4947-b6f2-4a76ccc04b6b)).

위축성 벌레먹은 모양 피부위축증은 모낭 주위에 위축성 변화가 나타나는 희귀 피부질환이며, CGRP 신호와의 연관성은 확립되어 있지 않습니다. 제공된 데이터에서는 두 질환 사이의 기전적 연결고리를 뒷받침하는 근거를 찾을 수 없습니다.

TxGNN 점수(0.9904)는 모델의 예측값일 뿐이며, 네트워크상의 통계적 연관성을 반영했을 가능성이 있습니다. 생물학적으로 의미 있는 관계라고 단정할 수 없으므로, 연구 가설로 다루려면 모낭 또는 진피 위축에서 CGRP의 역할에 대한 체계적 문헌 검토가 먼저 필요합니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202105577 | 아조비프리필드시린지주(프레마네주맙,유전자재조합) | 프리필드시린지 주사제 | 허가 문서 참조 |
| 202105576 | 아조비오토인젝터주(프레마네주맙,유전자재조합) | 오토인젝터 장착 프리필드시린지 주사제 | 허가 문서 참조 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측 질환에 대한 임상시험과 문헌이 모두 없고, 기전적 연결고리도 확인되지 않아 모델 예측만 존재하는 L5 수준입니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기)의 확보 및 안전성 검토
- 작용 기전(MOA) 데이터 확보
- CGRP와 모낭·진피 위축 관련 체계적 문헌 검토
- 위축성 벌레먹은 모양 피부위축증을 직접 다룬 전임상 또는 임상 연구 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Ajovy (fremanezumab-vfrm) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e344ea-5916-4947-b6f2-4a76ccc04b6b) |
| 2026-11-20 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [DailyMed: Ajovy (fremanezumab-vfrm) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e344ea-5916-4947-b6f2-4a76ccc04b6b) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

