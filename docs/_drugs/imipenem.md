---
layout: default
title: Imipenem
parent: 모델 예측만 (L5)
nav_order: 418
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-15
monitor_inn: "Imipenem"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "eosinophilia-myalgia syndrome"]
description: "Imipenem: 예측 신규 적응증 미만성 피부경화증 (diffuse scleroderma) (근거 수준 L5). 기존 적응증: ○ 유효균종 포도구균, 연쇄구균, 대장균, 시트로박터, 클레브시엘라, 엔테로박터, 세라티 아, 푸로테우스…"
---

# Imipenem
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

## Imipenem: 미만성 피부경화증 (diffuse scleroderma)
{: .text-alpha }

## 한 문장 요약

Imipenem은 세균 세포벽 합성을 억제하는 카바페넴계 항생제입니다. TxGNN 모델은 **미만성 피부경화증(diffuse scleroderma)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 유효균종 포도구균, 연쇄구균, 대장균, 시트로박터, 클레브시엘라, 엔테로박터, 세라티 아, 푸로테우스, 슈도 모나스, 인 플루엔자균, 아시네토박터, 박테로이드, 펩토구균, 펩토연쇄구균 ○ 적응증 - 기관지염, 기관지확장증(감염 시), 만성호흡기질환의 2차 감염, 폐렴, 폐농양… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200703652/EE)) |
| 예측 신규 적응증 | 미만성 피부경화증 (diffuse scleroderma) |
| TxGNN 예측 점수 | 0.9999 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 11건 / 전체 13건) |
| 허가증 수 | 13건 (유효 11건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Imipenem의 작용 기전(비공식 번역): “세균 페니실린 결합 단백질 억제제” 영어 원문: "Bacterial penicillin-binding protein inhibitor" ([ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708), CC BY-SA 3.0; 확인일 2026-11-19). 일반적으로 Imipenem은 세균의 페니실린 결합 단백질(PBP)을 억제해 세포벽 합성을 막고 균을 죽이는 광범위 항생제입니다.

미만성 피부경화증은 자가면역 기전과 섬유화가 핵심인 질환입니다. 항균 작용으로 이 질환을 설명할 만한 기전적 연결고리는 확인되지 않았습니다. 예측 점수가 높더라도 이는 모델 내부의 연관성에서 나온 값일 뿐, 이를 지지하는 임상시험이나 문헌이 없습니다. 따라서 현 단계에서 이 예측은 가설 수준으로만 볼 수 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200703652 | 자니심주사(수출용) | 백색~미황색 가루가 든 무색 투명 바이알 (주사제) | 허가사항 PDF 참조 |

## 안전성 고려사항

**약물 상호작용** (총 15건 확인)

- **주요(Major) 등급**: Bupropion, Iohexol, Iopamidol
- **중등도(Moderate) 등급**: Polyethylene glycol (3350 포함 전해질 제제), Dicoumarol, Warfarin, Lindane, Aminophylline, Dyphylline, Oxtriphylline, Theophylline, Cyclosporine, Ethinylestradiol, Mycophenolic acid, Pemetrexed

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 미만성 피부경화증에 대한 임상시험과 문헌이 전혀 없고, 항생제인 Imipenem과 자가면역 섬유화 질환 사이에 뚜렷한 기전적 연결도 없습니다.
- 근거 수준은 L5(모델 예측만 존재)이며, 현재 근거로는 추가 개발을 정당화하기 어렵습니다.

**진행하려면 필요한 것:**
- 항균 작용 외에 면역조절·항섬유화 효과를 시사하는 전임상 또는 기전 연구
- 미만성 피부경화증을 직접 다룬 임상시험 또는 문헌 근거
- 상세한 작용 기전 데이터 확보
- 허가사항 기반의 경고·금기 정보 확인 (현재 수집되지 않음)

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [ChEMBL CHEMBL43708 (imipenem): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL43708) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

