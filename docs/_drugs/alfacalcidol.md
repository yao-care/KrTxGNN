---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 5
---

# Alfacalcidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Alfacalcidol: 신성 골이영양증에서 가족성 고립성 부갑상선기능저하증으로

## 한 문장 요약

Alfacalcidol은 PTH-비의존성 활성 비타민 D 유사체(1α-hydroxycholecalciferol)로, 만성 신장병 관련 골무기질 장애·이차성 부갑상선기능항진증·저칼슘혈증 등 칼슘-인 대사 이상 치료에 사용됩니다.
TxGNN 모델은 **PTH 분비 장애형 가족성 고립성 부갑상선기능저하증(Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion)**에 효과가 있을 것이라 예측하며, 예측 점수는 **99.61%**입니다.
이 희귀 유전 아형에 대한 전용 임상시험 및 직접 문헌은 없으나, 기전적 연관성은 극히 강력하며 alfacalcidol은 일반 부갑상선기능저하증 치료의 표준 약물 계열에 이미 해당합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 신성 골이영양증, 이차성 부갑상선기능항진증, 저칼슘혈증 (국제 허가 기반; 한국 시판 기록 없음) |
| 예측 신규 적응증 | PTH 분비 장애형 가족성 고립성 부갑상선기능저하증 (Familial Isolated Hypoparathyroidism) |
| TxGNN 예측 점수 | 99.61% |
| 근거 수준 | L4 (기전 연구 기반; 이 특정 아형 대상 임상 데이터 없음) |
| 한국 시판 현황 | ✗ 미시판 (허가 기록 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Alfacalcidol(1α-hydroxycholecalciferol)은 간에서 CYP2R1/CYP27A1에 의해 25-수산화되어 칼시트리올(1,25-dihydroxyvitamin D₃)로 활성화되는 전구약물입니다. 신장 세뇨관의 CYP27B1(1α-hydroxylase)에 의한 활성화 단계를 완전히 우회하여 PTH에 의존하지 않고 활성 VDR 배위체를 직접 공급합니다. 이를 통해 소장 내 칼슘·인산염 흡수 촉진, 신세뇨관 칼슘 재흡수 강화, 뼈 무기질화 지원이 이루어집니다. 공식 작용 기전 데이터(MOA)는 현재 데이터 공백(DG002)으로 확인 중입니다.

"PTH 분비 장애형 가족성 고립성 부갑상선기능저하증"의 핵심 병태생리는 다음과 같습니다: PTH 분비 유전적 결함 → 혈중 PTH 부족 → 신세뇨관 1α-hydroxylase 활성 저하 → 칼시트리올 생성 감소 → 지속적 저칼슘혈증 → 근경련·경련·QT 연장 등의 증상. Alfacalcidol은 이 경로에서 PTH 의존 단계를 정확히 대체하므로, 기전적으로 이 질환의 칼슘 대사 이상을 직접 교정할 수 있습니다. 관련 유전자(GCM2, PTH, SOX3 등) 변이에 의한 원인과 무관하게 공통 병태생리에 작용한다는 점이 이 예측의 핵심 생물학적 근거입니다.

다만 본 Evidence Pack에는 이 희귀 아형을 직접 대상으로 한 임상시험 또는 문헌 데이터가 전혀 포함되어 있지 않습니다. 일반 부갑상선기능저하증(수술 후·자가면역성)에서 활성 비타민 D 아날로그는 이미 국제 가이드라인상 표준 치료이므로, 근거 공백은 alfacalcidol 자체의 한계가 아닌 이 특정 희귀 유전 아형에 대한 전용 연구 부재에서 비롯된 것으로 해석됩니다.

---

## 임상시험 근거

현재 이 적응증(PTH 분비 장애형 가족성 고립성 부갑상선기능저하증)에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 이 적응증에 대한 직접 관련 문헌이 없습니다.

> **참고**: 2순위 예측 적응증 "Dahlberg-Borer-Newcomer 증후군"에는 부갑상선기능저하증·저칼슘혈증과 기전적으로 연관된 주변 문헌 20편이 확인됩니다 (주요 목록은 아래 별첨 참조).

---

## Dahlberg-Borer-Newcomer 증후군 관련 참고 문헌 (2순위 예측)

> 이 문헌들은 2순위 예측 적응증과 연관되어 수집된 것으로, alfacalcidol의 기전 연관성 이해를 돕기 위한 참고 자료입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [29545131](https://pubmed.ncbi.nlm.nih.gov/29545131/) | 2018 | Review | Nephrologie & therapeutique | CKD에서 이차성 부갑상선기능항진증의 alfacalcidol 및 활성 비타민 D 유사체 활용 |
| [31485552](https://pubmed.ncbi.nlm.nih.gov/31485552/) | 2019 | Review | JBMR Plus | FGF23-매개 저인산혈증에서 1α-수산화 조절 기전 및 신흥 치료 전략 |
| [6262039](https://pubmed.ncbi.nlm.nih.gov/6262039/) | 1981 | Review | Drugs | 비타민 D 및 유사체(alfacalcidol 포함)의 약리학 및 치료적 사용 총괄 |
| [30333271](https://pubmed.ncbi.nlm.nih.gov/30333271/) | 2018 | RCT | Acta Med Indonesiana | 허약 증후군 노인에서 alfacalcidol의 염증 마커 및 T세포 아형에 대한 이중맹검 RCT |
| [16279662](https://pubmed.ncbi.nlm.nih.gov/16279662/) | 2005 | Review | Nippon Rinsho | 부갑상선기능저하증의 병태생리·진단·치료 종합 리뷰 |
| [32580149](https://pubmed.ncbi.nlm.nih.gov/32580149/) | 2020 | Registry | Endocrine Connections | 러시아 만성 부갑상선기능저하증 환자 등록 데이터베이스 구축 및 임상 발현 분석 |
| [28993435](https://pubmed.ncbi.nlm.nih.gov/28993435/) | 2017 | Case Series | Endocrine Connections | 부갑상선기능저하증 소아에서 급성 질환이 칼슘 항상성에 미치는 영향 (활성 VD 관리 포함) |
| [31968342](https://pubmed.ncbi.nlm.nih.gov/31968342/) | 2020 | Observational | Am J Nephrol | 갑상선전절제술 후 부갑상선기능저하증에서 칼슘-알칼리 증후군 발생 위험 (고용량 칼슘·비타민 D 치료 연관) |
| [39034346](https://pubmed.ncbi.nlm.nih.gov/39034346/) | 2024 | Case Report | Hormones | CYP27B1 돌연변이에 의한 VDDR1A(1α-수산화 결핍 구루병)에서 alfacalcidol의 치료 역할 |
| [39168248](https://pubmed.ncbi.nlm.nih.gov/39168248/) | 2024 | Experimental | Virologica Sinica | 비타민 D 유사체의 항바이러스 활성(SFTS 바이러스) 확인 — 기전 다양성 참고 |

---

## 신세뇨관산증 관련 문헌 (5순위 예측, L3 근거)

> 5순위 예측 적응증 "신세뇨관산증(Renal Tubular Acidosis)"은 **L3 근거 수준**, "Proceed with Guardrails" 권고로, 직접적인 alfacalcidol 사용 사례가 가장 많이 확인된 적응증입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [6893175](https://pubmed.ncbi.nlm.nih.gov/6893175/) | 1980 | Case Series | Contrib Nephrology | 다양한 유형의 Fanconi 증후군 6명에서 alfacalcidol(1α-OHVD₃) 투여 시 혈장 활성 VD 회복 및 비타민 D₂ 대비 200–250배 효과 확인 |
| [11518137](https://pubmed.ncbi.nlm.nih.gov/11518137/) | 2001 | Case Report | Internal Medicine | Sjögren 증후군 동반 RTA-1 및 골연화증 환자에서 알칼리 보충 + **alfacalcidol** 병용 치료로 골연화증 신속 호전 |
| [22740247](https://pubmed.ncbi.nlm.nih.gov/22740247/) | 2013 | Case Report | Modern Rheumatology | Sjögren 증후군 연관 RTA로 인한 골연화증에서 alfacalcidol·중탄산소다·리세드로네이트 병용으로 24개월 내 골밀도 정상화 성공 |
| [33398781](https://pubmed.ncbi.nlm.nih.gov/33398781/) | 2021 | Case Report | CEN Case Reports | 비정형 RTA + 비타민 D 결핍 동반 골연화증에서 활성 비타민 D 선행 치료력 확인 |
| [28509074](https://pubmed.ncbi.nlm.nih.gov/28509074/) | 2012 | Case Report + Review | CEN Case Reports | Sjögren 증후군 연관 원위부 RTA 골연화증 — 1α-수산화 기능 저하와 alfacalcidol 필요성 기술 |
| [36412607](https://pubmed.ncbi.nlm.nih.gov/36412607/) | 2023 | Case Report | Kidney Blood Press Res | 졸레드론산 유발 Fanconi 증후군 및 원위 RTA에서 저인산혈증 기전 및 치료 접근 |
| [9134837](https://pubmed.ncbi.nlm.nih.gov/9134837/) | 1997 | Case Report | Nippon Jinzo Gakkai | 성인 특발성 Fanconi 증후군에서 alfacalcidol 포함 치료 중 장기 골밀도 추적 |
| [6709109](https://pubmed.ncbi.nlm.nih.gov/6709109/) | 1984 | Case Report | Neth J Med | 원발성 담즙성 간경변 + RTA + 비장-신장 단락 환자에서 alfacalcidol의 25-수산화 확인 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 주요 안전성 데이터(경고·금기·약물상호작용)는 현재 데이터 공백(DG001)으로 확인 중입니다. TFDA, EMA, 또는 MFDS 허가사항 PDF를 통한 조회가 권고됩니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
"PTH 분비 장애형 가족성 고립성 부갑상선기능저하증"이라는 희귀 유전 아형에 대한 전용 임상시험 및 직접 문헌 근거가 전무하며, 한국 내 미시판 약물이라는 규제 장벽과 안전성 정보 공백(DG001)이 해소되지 않은 상태입니다. 기전적 타당성은 극히 강력하나 현 단계에서는 근거 생성 및 규제 검토가 선행되어야 합니다.

**진행하려면 필요한 것:**
- Alfacalcidol 공식 MOA 데이터 확보 (DrugBank API 조회 — DG002 해소)
- 한국·글로벌 허가사항 기반 안전성 정보 확보 (MFDS·EMA·TFDA 仿單 PDF 조회 — DG001 해소)
- 일반 부갑상선기능저하증에서의 활성 비타민 D 아날로그 체계적 문헌고찰 수행
- 이 유전 아형(GCM2·PTH·SOX3 변이 등)에서의 alfacalcidol 또는 calcitriol 사용 증례 보고 수집
- 한국 희귀의약품 규제 경로(식약처 희귀의약품 지정 제도) 및 미시판 약물 도입 타당성 검토

> **우선 검토 권고**: 5순위 예측 적응증 **신세뇨관산증(Renal Tubular Acidosis)** 은 L3 근거 수준(alfacalcidol 직접 사용 사례 8편), "**Proceed with Guardrails**" 권고로 현 예측 목록 중 가장 즉시 실행 가능성이 높습니다. 별도 보고서 작성을 권고합니다.

---

> ⚠️ **면책 고지**: 본 보고서는 TxGNN 모델 기반 연구 참고 자료로만 활용되어야 하며, 의료 조언이나 처방 근거로 사용할 수 없습니다. 모든 약물 재창출 후보는 임상 검증 과정을 거쳐야 합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

