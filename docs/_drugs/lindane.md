---
layout: default
title: Lindane
parent: 모델 예측만 (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Lindane: 예측 신규 적응증 경부 신경모세포종 (Cervical Neuroblastoma) (근거 수준 L5). 기존 적응증: (겔제) 머리이, 사면발이, 옴과 같은 동물성 기생충 감염증 (액제) 머리이, 사면발이 (로오숀제) 옴"
monitor_inn: "Lindane"
predicted_indications: ["cervical neuroblastoma", "benign neoplasm of tongue", "epiglottis neoplasm", "odontogenic cyst", "pre-malignant neoplasm", "benign neoplasm of hypopharynx", "schwannoma of jugular foramen", "cystic neoplasm", "benign neoplasm of buccal mucosa", "inner ear neoplasm"]
---

# Lindane
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Lindane: 외부 기생충 감염 치료제에서 경부 신경모세포종으로
{: .text-alpha }

## 한 문장 요약

Lindane은 국소 도포용 살충·살진드기제(옴, 이 치료)로 알려진 약물입니다.
TxGNN 모델은 **경부 신경모세포종(Cervical Neuroblastoma)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다. 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | (겔제) 머리이, 사면발이, 옴과 같은 동물성 기생충 감염증 (액제) 머리이, 사면발이 (로오숀제) 옴 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201235/EE)) |
| 예측 신규 적응증 | 경부 신경모세포종 (Cervical Neuroblastoma) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미시판 (취소된 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 0건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Lindane의 작용 기전(비공식 번역): “GABA-A 수용체 음성 알로스테릭 조절제”. 영어 원문: "GABA-A receptor negative allosteric modulator" ([ChEMBL CHEMBL15891 (lindane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL15891), CC BY-SA 3.0; 확인일 2026-11-19). 알려진 정보에 따르면 Lindane은 GABA-A 수용체(염소 이온 채널) 길항제로, 국소 외용 살충제로 사용되어 왔습니다.

이 기전과 신경모세포종 등 종양 사이에서 확립된 연관성은 없습니다. 예측 점수(0.9991)는 TxGNN 모델(딥러닝)에서 나온 값으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으며 생물학적 근거는 아닙니다. 오히려 Lindane의 신경독성(경련)과 발암 가능성 분류는 종양 치료 목적의 사용에 불리합니다.

같은 방식으로 예측된 상위 10개 질환(양성 혀 종양, 후두개 종양, 치성 낭종, 전암성 종양, 하인두 양성 종양, 경정맥공 신경초종, 낭성 종양, 협점막 양성 종양, 내이 종양)도 모두 L5 수준으로 임상시험과 문헌이 없고, 기전상 근거도 확인되지 않았습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 199201235 | 신신린단액(린단) | 이 약은 무색 투명한 점조성의 액제이다. | 신신제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201235/EE) | 유효기간만료 |
| 199701446 | 신신린단로오숀 | 백색-미백색의 현탁성 로오숀제 | 신신제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199701446/EE) | 유효기간만료 |

<!-- licenses:end -->

## 안전성 고려사항

- **금기(지식그래프 기반, 허가사항 문구 아님)**: 간질, 간경변, 아토피 피부염, 건선, 유사건선, 물질 남용/의존, 피부 질환, 광선각화증, 지루각화증과 관련된 금기 관계가 보고되어 있습니다.
- **약물 상호작용**: 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Bupropion, Iopamidol, Iohexol
  - **Moderate**: Morphine, Levofloxacin, Metoclopramide, Promethazine, Ephedrine, Phentermine, Diethylpropion, Sibutramine, Opium, Dronabinol 등
- **기타 우려(예측 평가 시 언급)**: 신경독성(경련 위험), 전신 흡수 우려, 발암성 관련 분류가 지적되었습니다.

허가사항의 경고·금기 문구는 이번 자료에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌 근거가 전혀 없고 기전상 연결고리도 확인되지 않아, 모델 예측(L5)만으로는 진행할 수 없습니다. 신경독성과 발암성 우려로 안전성 측면에서도 신규 적응증 개발에 불리합니다.

**진행하려면 필요한 것:**
- 허가증 PDF에서 기존 적응증, 경고, 금기 정보 확보 (식약처 의약품안전나라)
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 신경모세포종 등 예측 질환에 대한 전임상 또는 기전 연구 근거
- 신경독성 및 전신 노출 위험에 대한 안전성 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [ChEMBL CHEMBL15891 (lindane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL15891) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

