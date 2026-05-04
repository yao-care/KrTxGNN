---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam: 뇌전증 보조치료에서 열성 감염 관련 뇌전증 증후군으로

## 한 문장 요약

Clobazam은 1,5-벤조디아제핀 계열의 항경련제로, 해외에서는 렌녹스-가스토 증후군(LGS) 등 난치성 뇌전증의 보조치료제로 사용되고 있으나 국내에는 미허가 상태입니다.
TxGNN 모델은 **열성 감염 관련 뇌전증 증후군(Febrile Infection-Related Epilepsy Syndrome, FIRES)**에 효과가 있을 수 있다고 예측하며,
현재 **0건의 임상시험**과 **2편의 관련 문헌**이 확인되었으나 Clobazam을 FIRES에 직접 적용한 연구는 포함되어 있지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 뇌전증 보조치료 (해외 승인; 국내 미허가) |
| 예측 신규 적응증 | 열성 감염 관련 뇌전증 증후군 (FIRES) |
| TxGNN 예측 점수 | 99.82% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미허가 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Clobazam은 1,5-벤조디아제핀 계열 약물로서 GABA-A 수용체의 양성 알로스테릭 조절제로 알려져 있으며, 해외에서는 렌녹스-가스토 증후군(LGS)을 포함한 뇌전증 보조치료제로 사용됩니다. 이 GABA-A 강화 기전은 발작 임계치를 높여 뇌전증 발작의 빈도와 강도를 억제하는 원리입니다.

FIRES는 이전에 건강했던 환자에서 열성 질환 이후 발생하는 초난치성 뇌전증 중첩증(New-Onset Refractory Status Epilepticus, NORSE)의 아형입니다. 기존 항경련제 대부분에 내성을 보이며, 미다졸람·바르비투르산염 등 고용량 마취제 투여가 불가피한 중증 응급 질환입니다. 벤조디아제핀 계열은 급성 발작 및 뇌전증 중첩증의 1차 치료제로 확립되어 있으므로, Clobazam의 GABA-A 강화 기전이 기전적으로 FIRES의 발작 억제에 적용 가능할 수 있습니다.

다만, FIRES는 표준 벤조디아제핀 치료에도 내성을 보이는 매우 특수한 초난치성 질환이며, Clobazam의 경구 투여 특성(발현 시간 및 투여 경로의 한계)을 고려하면 급성 뇌전증 중첩증 관리보다는 만성기 유지치료 맥락에서의 역할이 보다 합리적입니다. 현재 Clobazam을 FIRES에 직접 평가한 임상시험이나 관찰 연구가 전무하여, 이 예측은 기전적 유사성에만 근거합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Case Series | Epileptic Disorders | FIRES 환자의 미다졸람 의존성 이탈 시 경장 로라제팜이 효과적인 대체 전략임을 보고 *(로라제팜 연구; Clobazam 직접 평가 아님)* |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Case Report | Cureus | 13세 FIRES 환자에서 페람파넬이 바르비투르산염 의존성 감소에 유망한 역할을 보임 *(페람파넬 연구; Clobazam 직접 평가 아님)* |

> **주의:** 확인된 2편의 문헌은 Clobazam이 아닌 로라제팜(벤조디아제핀)과 페람파넬을 다룬 연구로, Clobazam의 FIRES 적용을 직접 지지하는 근거로 보기 어렵습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
FIRES에 대한 Clobazam의 직접적인 임상 근거가 전무하며, 확인된 2편의 문헌도 Clobazam이 아닌 다른 약물(로라제팜, 페람파넬)을 대상으로 한 연구입니다. 또한 국내 미허가 약물로서 규제적 진입 경로 확보 자체가 선행 과제입니다.

**진행하려면 필요한 것:**
- Clobazam의 상세한 작용 기전(MOA) 데이터 확보 (DrugBank API 조회)
- 국내(MFDS) 허가 가능성 검토 및 규제 경로 분석
- FIRES 또는 NORSE 맥락에서 벤조디아제핀 계열 전반에 관한 체계적 문헌 고찰 수행
- TFDA 허가사항 PDF 다운로드 및 경고·금기사항 분석 (현재 안전성 데이터 공백)
- 국제 사례(미국 FDA 승인 LGS 적응증 자료)를 활용한 안전성 프로파일 보완
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

