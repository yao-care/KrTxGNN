---
layout: default
title: Telmisartan
parent: 모델 예측만 (L5)
nav_order: 721
evidence_level: L5
indication_count: 9
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Telmisartan: 예측 신규 적응증 변이형 협심증 (Prinzmetal angina) (근거 수준 L5). 기존 적응증: 텔미사르탄 또는 암로디핀 단독요법으로 혈압이 적절하게 조절되지 않는 본태성 고혈압"
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
| 기존 적응증 | 텔미사르탄 또는 암로디핀 단독요법으로 혈압이 적절하게 조절되지 않는 본태성 고혈압 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201605614/EE)) |
| 예측 신규 적응증 | 변이형 협심증 (Prinzmetal angina) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Telmisartan 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “Angiotensin II는 안지오텐신 전환효소(ACE, kininase II)가 촉매하는 반응에서 angiotensin I로부터 생성된다. Angiotensin II는 레닌-안지오텐신계의 주요 승압 물질로, 그 작용에는 혈관수축, 알도스테론의 합성 및 분비 자극, 심장 자극, 나트륨의 신장 재흡수가 포함된다. […] Telmisartan은 혈관 평활근 및 부신 등 여러 조직에서 angiotensin II가 AT 1 수용체에 결합하는 것을 선택적으로 차단함으로써 angiotensin II의 혈관수축 및 알도스테론 분비 작용을 차단한다.” 영어 원문: "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the reninangiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Telmisartan blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: telmisartan prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56a72ddf-c2a2-45ce-91b1-1fcfbff52c10), 버전 2026-11-02; 확인일 2026-11-19). 다만 Telmisartan은 AT1 수용체 차단제이면서 PPAR-gamma를 부분적으로 활성화하는 것으로 알려져 있습니다. 이 두 작용이 혈관 내피 기능을 개선하고 혈관 연축을 줄일 가능성이 있어, 변이형 협심증의 병태(관상동맥 연축)와 이론상 연결됩니다.

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

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: telmisartan prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56a72ddf-c2a2-45ce-91b1-1fcfbff52c10) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

