---
layout: default
title: Clobetasone
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
---

# Clobetasone
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

# Clobetasone: 피부 염증 질환에서 원발성 피부 T세포 림프종으로

---

## 한 문장 요약

Clobetasone은 글루코코르티코이드 수용체(GR) 작용제로, 습진·건선 등 피부 염증 질환에 사용되는 중등도 효능의 국소 외용 코르티코스테로이드입니다.
TxGNN 모델은 **원발성 피부 T세포 림프종(Primary Cutaneous T-cell Lymphoma, CTCL)**에 효과가 있을 수 있다고 예측하나,
현재 이 방향을 직접 지지하는 임상시험이나 문헌은 등록되어 있지 않습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 피부 염증 질환 (습진, 건선 등, 국소 외용 코르티코스테로이드) |
| 예측 신규 적응증 | 원발성 피부 T세포 림프종 (Primary Cutaneous T-cell Lymphoma) |
| TxGNN 예측 점수 | 99.97% |
| 근거 수준 | L4 |
| 시판 현황 | ✗ 미시판 (허가 이력 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 DrugBank에서 Clobetasone의 상세 작용 기전(MOA) 데이터는 확인되지 않았습니다. 그러나 같은 코르티코스테로이드 계열 약물로서, Clobetasone은 GR 활성화를 통해 NF-κB 신호를 억제하고 항염증 사이토카인(TNF-α, IL-6, IL-1β)을 하향조절하며, 림프구 세포자멸사(apoptosis)를 유도하는 것으로 알려져 있습니다.

원발성 피부 T세포 림프종(CTCL)의 기전적 관점에서, GR 활성화는 BIM 상향조절 및 MCL-1 하향조절을 통해 악성 T세포의 세포자멸사를 직접 유도합니다. 실제로 고효능 국소 코르티코스테로이드(예: clobetasol propionate)는 조기 CTCL(IA/IB기 균상식육종, Mycosis Fungoides) 치료에서 **NCCN Category 1** 표준요법으로 권고되고 있습니다. Clobetasone은 clobetasol에 비해 효능이 낮지만, 동일한 GR 활성화 기전을 공유하므로 계열 근거(class evidence)로서 기전적 타당성을 가집니다.

한편, 이 예측은 TxGNN 지식 그래프 모델 점수와 기전적 유추에 근거한 탐색 수준의 가설임을 명확히 해야 합니다. Clobetasone 자체를 CTCL에 적용한 직접적인 임상시험 또는 문헌 근거는 현재까지 존재하지 않으며, 계열 내 고효능 약물(clobetasol)과의 효능 차이에 대한 별도 검토가 필요합니다.

---

## 임상시험 근거

현재 Clobetasone과 원발성 피부 T세포 림프종에 관한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 Clobetasone과 원발성 피부 T세포 림프종에 관한 관련 문헌이 없습니다.

---

## 시판 정보

Clobetasone(DB13158)은 현재 허가된 제품이 없으며, 미시판 상태입니다(허가증 0건).

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Clobetasone의 CTCL 적용 가능성은 GR 매개 악성 T세포 세포자멸사 기전을 통해 이론적으로 타당하나, 직접적인 임상시험 및 문헌 근거가 전혀 없는 L4 수준의 탐색 가설에 머물러 있습니다. 진전을 위해서는 전임상 근거 확보와 안전성 데이터 수집이 선행되어야 합니다.

**진행하려면 필요한 것:**
- Clobetasone 상세 MOA 데이터 확보 (DrugBank API 조회)
- 허가사항 경고·금기 정보 확보 (TFDA 仿單 PDF 파싱)
- Clobetasone vs. Clobetasol의 CTCL 적응증 내 효능 비교 문헌 탐색
- 전임상 수준의 CTCL 세포주(예: HH, HuT78) 대상 GR 반응성 데이터 확인
- 동일 계열 저효능 코르티코스테로이드의 CTCL 치료 사례 보고(case report) 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

