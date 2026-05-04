---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorphine: 오피오이드 사용 장애 치료에서 급성 간헐성 포르피린증으로

## 한 문장 요약

Buprenorphine은 μ-opioid 수용체 부분 작용제이자 κ-opioid 수용체 길항제로, 국제적으로 오피오이드 사용 장애(OUD) 치료 및 중등도~중증 통증 관리에 사용되는 반합성 오피오이드입니다.
TxGNN 모델은 **급성 간헐성 포르피린증(Acute Intermittent Porphyria)**에 효과가 있을 수 있다고 예측하나,
현재 이 방향을 지지하는 **임상시험 및 문헌 근거가 전무**합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 오피오이드 사용 장애(OUD) 치료, 중등도~중증 통증 (국내 허가 정보 없음) |
| 예측 신규 적응증 | 급성 간헐성 포르피린증 (Acute Intermittent Porphyria) |
| TxGNN 예측 점수 | 99.41% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 Evidence Pack에 상세한 작용 기전(MOA) 데이터가 포함되어 있지 않습니다. 알려진 정보에 따르면, Buprenorphine은 μ-opioid 수용체(MOR)에 대한 부분 작용제이자 κ-opioid 수용체(KOR) 길항제로 작용하며, 내인성 오피오이드 시스템의 여러 경로에 동시에 영향을 미칩니다. 이 다중 수용체 프로파일이 TxGNN 지식 그래프에서 다양한 신경계 및 대사 질환과의 간접 연결 경로를 형성한 것으로 보입니다.

급성 간헐성 포르피린증(AIP)은 헴(heme) 합성 경로 효소(Hydroxymethylbilane synthase)의 결핍으로 발생하는 희귀 상염색체 우성 대사 질환으로, 발작 시 극심한 복통·신경병증·자율신경 불안정이 특징입니다. AIP 발작 중 통증 관리를 위해 오피오이드 계열 약물이 임상적으로 일부 활용된 사례가 있어, Buprenorphine의 MOR 부분 작용이 증상 조절에 이론적으로 기여할 수 있다는 연결고리가 존재합니다.

그러나 이 예측의 타당성에는 중요한 제약이 있습니다. 첫째, 이는 AIP의 근본 원인인 헴 합성 이상을 수정하는 기전이 아닌, 순전히 증상 관리 차원의 연결입니다. 둘째, 일부 오피오이드 계열 약물은 AIP 환자에서 발작을 유도하는 포르피리아 유발 잠재성(porphyrogenic potential)을 가지는 것으로 알려져 있으며, Buprenorphine의 AIP 환자 안전성 데이터가 현재 충분하지 않습니다. TxGNN의 고점수(99.41%)는 지식 그래프 내 opioid–pain–neurological 간접 통계 연결을 반영하는 것으로 해석됩니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 한국 시판 정보

Buprenorphine은 현재 한국에서 허가된 제품이 없으며, 시판 중인 품목이 없습니다 (허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
모든 예측 적응증(6건)이 근거 수준 L5(TxGNN 모델 예측만 존재)에 해당하며, 급성 간헐성 포르피린증을 포함한 어느 적응증에 대해서도 임상시험 또는 문헌 근거가 전혀 존재하지 않습니다. 특히 오피오이드 계열 약물이 AIP 환자에서 발작을 유발할 수 있다는 안전성 우려가 제기되어 있어, 추가 검증 없이 진행하는 것은 적절하지 않습니다.

**진행하려면 필요한 것:**
- 상세한 작용 기전 데이터 확보 (DrugBank API를 통한 MOA 조회, DG002 해소)
- 한국 허가사항 기반 경고 및 금기 정보 확인 (DG001 해소 — TFDA/MFDS 허가사항 PDF 검토)
- Buprenorphine의 AIP 환자 안전성 평가 (포르피리아 유발 잠재성 문헌 검색)
- AIP 또는 관련 신경계 증상 관리에서의 오피오이드 사용 사례 보고서 재탐색
- 전임상 기전 연구 (AIP 동물 모델에서의 오피오이드 수용체 역할 검토)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

