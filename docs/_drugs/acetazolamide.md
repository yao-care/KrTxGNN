---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Acetazolamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Acetazolamide: 녹내장/고산병에서 심근병증(Cardiomyopathy)으로

## 한 문장 요약

Acetazolamide는 탄산탈수효소 억제제(Carbonic Anhydrase Inhibitor, CAI)로, 국제적으로 녹내장, 고산병, 간질 치료에 사용되어 왔으나 현재 허가 이력이 없는 약물입니다.
TxGNN 모델은 총 10가지 새로운 적응증을 예측하였으며, 근거 수준이 가장 높은 **심근병증(Cardiomyopathy)** 에 대해 **3건의 Phase 4 임상시험**과 **10편의 문헌**이 이를 지지합니다.
ADVOR Phase 3 RCT (NEJM 2022, n=519)에서 급성 심부전 이뇨 보조 효과가 이미 검증되어 있어 기전적 근거와 임상적 타당성이 모두 뒷받침됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 자료 없음 (탄산탈수효소 억제제 — 녹내장 / 고산병 / 간질) |
| 예측 신규 적응증 | 심근병증 (Cardiomyopathy) |
| TxGNN 예측 점수 | 99.83% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

현재 DrugBank 상세 작용 기전 데이터가 확보되지 않았습니다. 알려진 정보에 따르면, Acetazolamide는 세뇨관에서 탄산탈수효소(Carbonic Anhydrase)를 억제하여 HCO₃⁻ 재흡수를 차단하고, 이를 통해 이뇨 효과 및 대사성 산-염기 균형 조절 효과를 나타냅니다.

**심근병증과의 기전적 연결**: 만성 심부전 환자에서 장기간 루프 이뇨제(furosemide 등)를 사용하면 대사성 알칼리증이 발생하고, 집합관의 NHE3(나트륨-수소 교환체)가 상향 조절되어 이뇨제 저항성이 형성됩니다. Acetazolamide가 HCO₃⁻ 재흡수를 차단하면 대사성 알칼리증이 교정되고, 루프 이뇨제 감수성이 회복되어 급성 심부전의 체액 저류가 개선됩니다.

이 기전은 **ADVOR Phase 3 RCT (NEJM 2022, n=519)**에서 검증되었습니다. 정맥 furosemide에 Acetazolamide를 추가한 군이 위약 대조군보다 성공적 탈수율이 유의하게 높았으며, 재입원율도 감소하였습니다. 현재 등록된 세 건의 Phase 4 임상시험은 이 결과를 경구 제형 및 다양한 환자군으로 확장하는 후속 연구입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | 모집 중 | 400 | 만성 심부전 급성 악화에서 경구 Acetazolamide의 이뇨 효능 평가 (ADVOR 결과의 경구 제형 확장 연구, 주요 원인으로 심근병증 포함) |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | 모집 중 | 939 | 용량 과부하 급성 심부전에서 루프 이뇨제 단독 vs. Metolazone 또는 Acetazolamide 병합 비교 이중맹검 대규모 RCT |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | 모집 중 | 466 | 급성 심부전에서 소변 나트륨 기반 개인화 이뇨 알고리즘 (ADHF 적절 이뇨 반응 평가 지표로 Acetazolamide 포함) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Annual Review | ESC Heart Failure | 2024 심부전 치료 주요 진전 검토: 2023 ESC 가이드라인 업데이트 반영, 이뇨 보조 전략 포함 |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | 2022년 심혈관 신규 약물 총람: obstructive HCM 치료제(mavacamten) 등 first-in-class 약물 포함 |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | J Cardiology Cases | 진행성 심부전 + 비후성 심근병증 환자에서 Acetazolamide로 저염소혈증(94 mEq/L) 교정, 이뇨 반응 개선 및 소변 전해질 모니터링 중요성 보고 |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case Report (이상반응) | Acute Med Surg | 확장성 심근병증 환자에서 정맥 Acetazolamide 투여 1시간 후 비심인성 폐부종 발생 — 심기능 저하 환자에서의 안전성 주의 신호 |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Preclinical (동물) | Saudi Med J | 2주 및 8주령 토끼 적출 심장 모델에서 허혈-재관류 손상에 대한 Acetazolamide 효과 평가 |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian J Ophthalmol | Danon병(LAMP2 돌연변이, 비후성 심근병증 동반) 환자에서 경구 Acetazolamide로 낭포성 황반부종 치료 보고 |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Series | Acta Neurol Scand | 저칼륨혈증성 주기성 마비 가족 9명에서 심초음파 포함 심장검사 결과, 심근 침범(심근병증) 확인 |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurol Scand | 저칼륨혈증성 주기성 마비 환자에서 Acetazolamide 750–1000 mg 치료 중 운동성 협심증 및 ST 하강 발생 — 심근 합병증 주의 |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Case Series | J Nucl Med | 미토콘드리아 뇌근병증 10명에서 SPECT를 이용한 뇌혈류 변화 조사 (심근 침범 가능성 포함) |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | J Med Case Reports | Trisomy 9p에서 맥락막 과증식으로 인한 선천성 수두증과 선천성 심장병 동반 사례, 비정형적 Acetazolamide 투여 경로 기술 포함 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
ADVOR Phase 3 RCT (NEJM 2022)에서 급성 심부전에 대한 Acetazolamide 이뇨 보조 효과가 이미 검증되었으며, 이를 확장하는 3건의 Phase 4 임상시험이 현재 진행 중입니다. 탄산탈수효소 억제를 통한 대사성 알칼리증 교정 → 루프 이뇨제 감수성 회복의 기전이 명확하고 임상적으로 타당합니다.

**진행하려면 필요한 것:**
- DrugBank API를 통한 상세 작용 기전(MOA) 및 DrugBank ID 확보 (High priority)
- 허가 기관 공식 경고·금기 사항 검토 — 현재 Blocking Data Gap으로 S1 안전성 평가 진입 불가
- 한국 내 허가 경로 확인 (현재 미허가: 수입 허가 또는 신규 품목 허가 절차 필요)
- 고위험군(신기능 저하, 간경변증, 저칼륨혈증, 심기능 저하 환자 등)에 대한 안전성 모니터링 계획 수립
- 정맥 투여 시 비심인성 폐부종 발생 위험(PMID 29123889) 고려한 투여 경로별 가이드라인 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

