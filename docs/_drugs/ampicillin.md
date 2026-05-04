---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: 세균성 감염증에서 후두염으로

## 한 문장 요약

Ampicillin은 광범위 스펙트럼 β-lactam 계열 항생제로, 세균성 감염증 치료에 수십 년간 사용되어 온 약물입니다.
TxGNN 모델은 **후두염(Laryngitis)**에 효과가 있을 수 있다고 예측하며 (예측 점수 99.97%),
현재 **1건의 임상시험**과 **20편의 문헌**이 이 방향의 검토를 지지하나, 직접적 무작위대조시험(RCT) 근거는 존재하지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 세균성 감염증 (허가 데이터베이스 내 등재 없음) |
| 예측 신규 적응증 | 후두염 (Laryngitis) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미허가 (허가 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Ampicillin의 상세 작용 기전(MOA) 데이터는 확보되지 않았습니다. 알려진 정보에 따르면, Ampicillin은 광범위 페니실린 계열 β-lactam 항생제로, 세균의 세포벽 합성에 필수적인 PBP(Penicillin-Binding Protein)를 억제하여 세균을 사멸합니다. 그람 양성균(연쇄구균, 장구균)과 일부 그람 음성균(*H. influenzae*, *E. coli* 등)을 포함한 광범위한 항균 스펙트럼을 보유합니다.

세균성 후두염은 *Haemophilus influenzae*(급성 후두개염), A군 연쇄구균(*Streptococcus pyogenes*), *Streptococcus pneumoniae* 등이 원인이 될 수 있으며, β-lactamase 비생성 균주는 이론적으로 Ampicillin의 항균 범위에 포함됩니다. 역사적으로 1970~1980년대에 소아 *H. influenzae* 후두개염 치료 표준 요법으로 Ampicillin이 광범위하게 사용된 바 있어, 기전상 연결고리는 존재합니다.

그러나 이 예측에는 중요한 현실적 한계가 있습니다. 첫째, 후두염의 90% 이상은 바이러스성(파라인플루엔자바이러스, 인플루엔자바이러스 등)이므로 항생제의 효과를 기대하기 어렵습니다. 둘째, β-lactamase 생성 *H. influenzae* 균주가 증가하면서 Ampicillin 단독 사용의 임상적 효용이 크게 감소하였고, 현행 진료지침은 세균성 후두염에 Amoxicillin-Clavulanate 또는 2~3세대 세팔로스포린을 우선 권고합니다. TxGNN 예측 점수(99.97%)는 지식 그래프 내 공출현 패턴을 반영하는 것으로, 실제 임상적 재창출 가능성과는 별개로 해석해야 합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | 완료 | 363 | CLAVAMOX® (Amoxicillin/Clavulanate) 소아 시판 후 특별사용조사 — 후두염을 포함한 다수 감염증 대상. Ampicillin 단독제제가 아니며 후두염이 주요 평가변수가 아니어서 직접 근거로서 관련성 낮음 (Grade C) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | 진료지침 품질평가 | CoDAS | 후두염·인두염 진료지침의 방법론적 질 AGREE II 기준 평가 — 표준 치료 근거 체계 분석 |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | 후향적 증례분석 | Anaesth Intensive Care | 소아 급성 후두개염 161례 분석; *H. influenzae* 원인, 전신마취 하 비인두 삽관과 항생제 병행 치료 강조 |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | 증례보고/고찰 | Ann Otol Rhinol Laryngol | 자발성 후두 농양의 현대적 증례 및 역사적 고찰; 항생제 시대 이후 드물어진 세균성 후두 합병증 |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | 증례보고 | Ann Emerg Med | 성인 급성 후두개염 3례; 굴곡내시경으로 진단 확인, 기도 폐쇄 위험 및 항생제 치료 기술 |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | 후향적 연구 | West J Med | 성인 급성 후두개염 9례(평균 53세); 삽관 필요 환자에서 증상 지속시간 짧음, 조기 진단 중요성 |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | 증례보고 | Auris Nasus Larynx | COVID-19 감염이 급성 후두개염으로 발현된 사례; 광범위 괴사성 병변, 기도 관리 및 항생제 역할 논의 |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | 관찰연구 | Eur Arch Otorhinolaryngol | 당뇨 동반 경부 농양 환자의 병원균 분포 및 항생제 선택 전략; 광범위 항생제 필요성 분석 |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | 증례보고 | Auris Nasus Larynx | 골수이식 후 발생한 후두 방선균증; 장기 페니실린 치료로 완치 — β-lactam의 후두 감염 적용 가능성 확인 |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | 증례보고 | Acta Otorrinolaringol Esp | 성문방 후두 농양 2례; 드문 질환으로 신속 진단 및 항생제 치료 시작이 생명 위협 예방에 결정적 |
| [7487676](https://pubmed.ncbi.nlm.nih.gov/7487676/) | 1995 | 동물실험 | Auris Nasus Larynx | Chinchilla 모델에서 Ampicillin + Ibuprofen 병용의 급성 중이염 치료 효과 평가 — Ampicillin 직접 사용 이비인후과 감염 연구 |

---

## 한국 시판 정보

규제 데이터베이스 조회 결과, Ampicillin은 현재 등록된 허가 제품이 없습니다 (미허가, 未上市). 한국 내 실제 시판 현황은 식품의약품안전처(MFDS) nedrug 데이터베이스를 통한 별도 확인이 필요합니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Ampicillin의 후두염 재창출을 직접 지지하는 RCT 근거가 없으며 (근거 수준 L4), 후두염 대다수가 바이러스성인 점과 β-lactamase 내성 균주 증가로 인해 Ampicillin 단독 사용의 현대적 임상 가치가 제한적입니다. 기전적 연결고리는 존재하나 실제 임상 효과를 뒷받침하는 근거가 불충분하여 현 단계에서 적극적 재창출 추진은 어렵습니다.

**진행하려면 필요한 것:**
- Ampicillin 상세 MOA 데이터 확보 (DrugBank API 조회, DG002 해소)
- 한국 MFDS 허가 현황 및 안전성 정보(허가사항·경고·금기) 확인 (DG001 해소)
- 세균성 후두염에서 원인균별 β-lactam 감수성 최신 역학 데이터 검토
- Ampicillin-Sulbactam 복합제로의 확장 시 근거 재평가 (내성 우회 가능성)
- 바이러스성 후두염 제외 후 세균성 후두염만을 대상으로 한 하위군 분석 가능성 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

