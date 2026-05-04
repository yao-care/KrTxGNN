---
layout: default
title: Beraprost
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Beraprost
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

# Beraprost: 폐동맥 고혈압에서 폐동정맥 기형으로

## 한 문장 요약

Beraprost는 경구 투여 가능한 프로스타사이클린(Prostacyclin) 유사체로, 해외에서 폐동맥 고혈압(PAH) 치료에 활용되어 온 약물입니다.
TxGNN 모델은 **폐동정맥 기형(Pulmonary Arteriovenous Malformation, PAVM)**에 효과가 있을 수 있다고 예측하며,
현재 **임상시험 0건**과 **문헌 1편**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 폐동맥 고혈압 (해외 허가 기반; 한국 허가 기록 없음) |
| 예측 신규 적응증 | 폐동정맥 기형 (Pulmonary Arteriovenous Malformation) |
| TxGNN 예측 점수 | 98.06% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미상시 (허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 제공되지 않았습니다. 다만, 복수의 PAH 관련 문헌에서 Beraprost는 **IP(Prostacyclin I₂) 수용체 촉진제**로 일관되게 기술됩니다. IP 수용체 활성화는 세포 내 cAMP를 증가시켜 폐혈관 평활근 이완, 혈소판 응집 억제, 혈관 평활근세포 증식 억제로 이어지며, 이 기전이 폐혈관 저항(PVR) 상승을 특징으로 하는 다양한 PAH 아형의 치료 근거가 됩니다.

폐동정맥 기형(PAVM)은 본질적으로 **구조적 혈관 이상**으로, 유전성 출혈성 모세혈관 확장증(HHT/Rendu-Osler-Weber 병)과 밀접하게 연관됩니다. PAVM에서 PAH가 합병되는 경우, Beraprost의 혈관 확장 효과가 이론적으로 폐혈관 저항 완화에 부가적 역할을 할 수 있습니다.

그러나 PAVM의 핵심 병태생리는 혈관 긴장도 조절 이상이 아닌 해부학적 구조 문제라는 점에서, Beraprost가 PAVM 자체를 교정할 수 없습니다. PAH 동반 시에만 보조적 역할이 가능하며, PAH 적응증 대비 기전적 연관성은 상당히 제한적입니다. 현 단계는 기전 가설 수준입니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15929019](https://pubmed.ncbi.nlm.nih.gov/15929019/) | 2005 | Case Series/Review | Deutsche medizinische Wochenschrift | HHT(Rendu-Osler-Weber 병) 환자에서 폐 침범과 동반된 폐동맥 고혈압의 10년 경과 기술; Beraprost를 직접 평가한 연구는 아님 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Research Question**

**사유:**
폐동정맥 기형은 구조적 혈관 이상으로, Beraprost의 IP 수용체 경로와의 기전적 연관성이 이론적 수준에 머무릅니다. 직접적 임상시험이 전무하고 지지 문헌도 간접적 증례 보고 1건에 불과하여, 현 단계에서 임상 진행 또는 투자 의사결정을 뒷받침할 근거가 충분하지 않습니다.

**진행하려면 필요한 것:**
- Beraprost 작용 기전(MOA) 상세 데이터 확보 (DrugBank API 조회)
- 한국 MFDS 안전성 정보 확보 (경고, 금기, 약물 상호작용)
- IP receptor 경로와 HHT/PAVM 병태생리의 연관성에 대한 기초 및 전임상 연구 검토
- PAVM 동반 PAH 환자 대상 탐색적 증례 보고 또는 레지스트리 데이터 수집
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

