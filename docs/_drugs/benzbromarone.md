---
layout: default
title: Benzbromarone
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 1
---

# Benzbromarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Benzbromarone: 고요산혈증에서 신성 저요산혈증으로

## 한 문장 요약

Benzbromarone은 신장 근위세관의 URAT1(SLC22A12) 수송체를 억제하여 요산 재흡수를 차단하는 요산배설 촉진제(uricosuric agent)로, 원래 **고요산혈증 및 통풍** 치료에 사용되었습니다.
TxGNN 모델은 **신성 저요산혈증(Hypouricemia, Renal)**에 효과가 있을 수 있다고 예측하나, 이는 약리학적 기전상 방향성 모순을 내포한 가짜 양성(false positive)으로 판단됩니다.
현재 관련 임상시험 등록은 없으며, **20편의 문헌**이 수집되었으나 benzbromarone은 해당 질환에서 치료제가 아닌 진단 도구로 사용되었습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고요산혈증 / 통풍 (허가 데이터 없음) |
| 예측 신규 적응증 | 신성 저요산혈증 (Hypouricemia, Renal) |
| TxGNN 예측 점수 | 99.07% |
| 근거 수준 | L5 |
| 시판 현황 | ✗ 미시판 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | **Hold** |

---

## 이 예측이 타당한 이유는?

### ⚠️ 기전상 방향성 모순 (Directional Mismatch) — 전형적인 KG 예측 가짜 양성

Benzbromarone은 신장 근위세관 첨단막에 위치한 요산 수송체 **URAT1(SLC22A12)을 억제**하여 요산의 재흡수를 차단합니다. 그 결과 혈중 요산 농도가 낮아지고 요산 배설이 증가하므로, 고요산혈증과 통풍 치료에 사용되어 왔습니다.

반면, **신성 저요산혈증(Renal Hypouricemia)**의 주된 병인은 바로 URAT1의 **기능 소실 돌연변이(loss-of-function mutation)**입니다. 환자의 신장은 이미 요산을 재흡수하지 못하는 상태이며, 혈중 요산 농도는 극히 낮고(< 2 mg/dL) 요산 분획 배설률(FEua)은 비정상적으로 높습니다. 이미 기능을 잃은 URAT1에 억제제를 추가 투여하면 약리 작용 공간이 존재하지 않을 뿐만 아니라, 요산 과다 배설을 더욱 심화시켜 운동 후 급성 신부전, 혈뇨, 요로결석 등의 합병증을 악화시킬 위험이 있습니다.

TxGNN이 높은 점수(0.9907)를 산출한 이유는 **Drug → URAT1 → Disease** 경로의 공유 생물학적 표지자 연결 때문으로 추정되나, 모델이 "억제제(inhibitor)"와 "기능 소실(loss-of-function)" 사이의 **방향성 충돌**을 인식하지 못한 결과입니다. 수집된 20편의 문헌에서도 benzbromarone은 신성 저요산혈증의 **치료**가 아닌, 세뇨관 결함 유형을 분류하는 **진단 약리 탐침(pharmacological probe)**으로만 활용되었습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

> ⚠️ **주의**: 아래 문헌에서 benzbromarone은 신성 저요산혈증의 **치료제**가 아닌, 세뇨관 요산 운반 기전 유형(presecretory / postsecretory / secretion 결함)을 감별하는 **진단 탐침**으로 사용되었습니다. 문헌 자체가 이 적응증을 지지하지 않습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Narrative Review | Clinical Rheumatology | 저요산혈증 병인·분류 업데이트; URAT1 기능 소실이 신성 저요산혈증의 주요 원인으로 기술 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cross-sectional / Molecular | JASN | 일본 32명 환자에서 SLC22A12(URAT1) 돌연변이 분석; 유전형-표현형 상관관계 규명 |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case Report | Am J Kidney Dis | URAT1 돌연변이 형제 2명의 운동 후 급성 신부전 사례 |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Case Series | Clinical Nephrology | 22세부터 4회 반복 운동 후 급성 신부전 발생; 신생검에서 급성 세뇨관 괴사 확인 |
| [9510398](https://pubmed.ncbi.nlm.nih.gov/9510398/) | 1998 | Case Series | Internal Medicine (Tokyo) | 신성 저요산혈증 16명에서 혈뇨 위험인자 분석; 세뇨관 유형별 비교 |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Case Report | Nephron | Fanconi 증후군 동반 신성 저요산혈증에서 pyrazinamide/benzbromarone 탐침으로 요산 운반 분석 |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case Report | Acta Paediatrica | 14~25세 사이 운동 후 급성 신부전 4회 발생; benzbromarone 탐침으로 전분비 재흡수 결함 유형 확인 |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case Series | J Pediatrics | 소아 유전성 신성 저요산혈증 4명; pyrazinamide·benzbromarone이 요산 청소율 비율에 영향 없음 확인 |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case Report | Nephron | benzbromarone 투여 후 요산 청소율 추가 증가 확인; 유전성 신 요산 수송 이상 진단에 활용 |
| [9144014](https://pubmed.ncbi.nlm.nih.gov/9144014/) | 1997 | Case Report | Internal Medicine (Tokyo) | 신성 저요산혈증 + 신장결석 2례; BZB 억제 시험에서 전분비 재흡수 결함 유형 감별 |

---

## 시판 정보

허가 데이터가 없습니다. Benzbromarone은 현재 미시판 상태(허가 0건)입니다.

> **참고 맥락**: Benzbromarone은 1990년대 유럽 일부 국가에서 통풍 치료제로 시판되었으나, 중증 전격성 간부전(fulminant hepatic failure) 사례 보고가 축적되면서 2003년 전후로 주요 유럽 시장에서 자진 철수된 바 있습니다. 신규 적응증 검토 시 이 안전성 이력을 반드시 고려해야 합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 예측 점수는 99.07%로 매우 높으나, 이는 Benzbromarone(URAT1 억제제)과 신성 저요산혈증(URAT1 기능 소실 질환) 사이의 공유 표적으로 인한 지식 그래프 가짜 양성으로 판단됩니다. 약리학적 작용 공간이 존재하지 않으며 합병증 악화 위험이 있어, 임상 개발 진행은 권장되지 않습니다.

**진행하려면 필요한 것:**
- 이 후보는 임상 개발 진행이 부적합하므로 **제외(exclusion) 처리** 권장
- "억제제 → 기능 소실 질환" 방향성 충돌 패턴을 TxGNN 후처리 필터에 추가하여 유사 가짜 양성 방지
- Benzbromarone의 실제 적응증(고요산혈증)에 대한 KG 예측 결과 별도 검토 고려
- 신성 저요산혈증 치료 후보 탐색이 필요한 경우, URAT1 기능 보완 또는 합병증(운동 후 급성 신부전) 예방 기전을 가진 약물로 방향 전환 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

