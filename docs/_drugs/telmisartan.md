---
layout: default
title: Telmisartan
parent: 모델 예측만 (L5)
nav_order: 721
evidence_level: L5
indication_count: 9
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
last_modified_at: 2026-10-31
description: "Telmisartan: 예측 신규 적응증 변이형 협심증 (Prinzmetal angina) (근거 수준 L5). 기존 적응증: 이번 보고서용으로 정리된 자료에는 허가 적응증 본문이 없고 허가 문서 링크만 있어 확인할 수 없음"
---

# Telmisartan
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

## Telmisartan: 한국 허가 제품에서 변이형 협심증(Prinzmetal angina)으로
{: .text-alpha }

## 한 문장 요약

Telmisartan은 안지오텐신 II 1형(AT1) 수용체 차단제로, 한국에서 단일제와 복합제 형태로 다수 허가되어 있습니다.
TxGNN 모델은 **변이형 협심증(Prinzmetal angina)**에 효과가 있을 수 있다고 예측하지만(점수 0.9998), 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이번 보고서용으로 정리된 자료에는 허가 적응증 본문이 없고 허가 문서 링크만 있어 확인할 수 없음 |
| 예측 신규 적응증 | 변이형 협심증 (Prinzmetal angina) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 다만 Telmisartan은 AT1 수용체 차단제이면서 PPAR-gamma를 부분적으로 활성화하는 것으로 알려져 있습니다. 이 두 작용이 혈관 내피 기능을 개선하고 혈관 연축을 줄일 가능성이 있어, 변이형 협심증의 병태(관상동맥 연축)와 이론상 연결됩니다.

그러나 이는 가설 수준의 설명입니다. 이 질환과 Telmisartan을 직접 연구한 임상시험이나 문헌이 확인되지 않았습니다. 기존 적응증과 신규 적응증의 유사성도 아직 평가되지 않았습니다. 높은 TxGNN 점수만으로 효능을 기대하기는 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

확인된 허가는 최소 20건이며 목록이 일부일 수 있습니다. 제품명에 암로디핀, 히드로클로로티아지드 등 병용 성분이 드러나는 복합제는 단일 성분 Telmisartan의 허가 근거로 쓰지 않으므로 아래 표에서 제외했습니다. 단일 성분으로 확인되는 제품은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| [201701087](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201701087/EE) | 미르텔정80밀리그램 (삼천당제약) | 백색 또는 미백색의 양쪽이 볼록한 원형 정제 | 허가 문서 링크 참조 (적응증 본문 미확인) |
| [201209572](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201209572/EE) | 텔미칸정80밀리그램 (제일약품) | 흰색 또는 거의 흰색의 양면이 볼록한 원형 정제 | 허가 문서 링크 참조 (적응증 본문 미확인) |
| [201605171](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605171/EE) | 텔미카르정40밀리그램 (경보제약) | 흰색의 장타원형 정제 | 허가 문서 링크 참조 (적응증 본문 미확인) |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 확인되지 않았으므로 허가사항을 참조하세요.

**약물 상호작용** (총 100건 중 일부 확인)
- **Major**: Potassium citrate, Potassium bicarbonate
- **Moderate**: Hydrocortisone, Dexamethasone, Betamethasone, Budesonide, Triamcinolone, Acetylsalicylic acid, Bupropion, Morphine, Dronabinol, Canagliflozin, Dapagliflozin, Empagliflozin, Exenatide, Insulin human, Insulin aspart, Picosulfuric acid, Sodium sulfate, Polyethylene glycol (3350 with electrolytes 포함)

## 결론 및 다음 단계

**결정: Hold**

**사유:**
변이형 협심증에 대해 Telmisartan을 직접 연구한 임상시험이나 문헌이 없고 모델 예측만 있어 근거 수준이 L5입니다. 허가사항의 경고와 금기 정보도 확인되지 않아 안전성 검토를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 변이형 협심증 또는 관상동맥 연축에 대한 Telmisartan의 전임상·임상 연구 확보
- 작용 기전(MOA) 데이터 보강 (예: DrugBank)
- 식약처 허가사항(적응증, 경고, 금기)의 내용 확인
- 동일 약물의 다른 예측 질환(예: 뇌내출혈)은 별도 평가 필요
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

