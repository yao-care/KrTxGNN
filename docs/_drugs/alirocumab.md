---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# Alirocumab: 고콜레스테롤혈증에서 X-연관 어린선으로

## 한 문장 요약

Alirocumab은 PCSK9를 억제하는 완전 인간화 단클론항체로, 글로벌 시장에서 고콜레스테롤혈증 및 심혈관 질환 위험 감소에 사용됩니다.
TxGNN 모델은 예측 점수 기준 1위로 **X-연관 어린선(ichthyosis, X-linked, without steroid sulfatase deficiency)**을 제시하나,
이를 지지하는 **임상시험 및 문헌 근거가 전혀 존재하지 않아** 현 단계에서는 보류(Hold) 판정입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고콜레스테롤혈증, 심혈관 질환 위험 감소 (글로벌 승인 기준; 한국 미허가) |
| 예측 신규 적응증 | X-연관 어린선 (ichthyosis, X-linked, without steroid sulfatase deficiency) |
| TxGNN 예측 점수 | 99.43% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

작용 기전에 대한 상세 데이터가 현재 제공되지 않았습니다. 알려진 바에 따르면, Alirocumab은 혈중 PCSK9 단백질에 직접 결합하는 완전 인간화 단클론항체로서, 간세포 표면의 LDL 수용체가 PCSK9에 의해 분해되는 것을 차단합니다. 그 결과 LDL 수용체 밀도가 증가하고 혈중 LDL-콜레스테롤 청소율이 높아집니다.

X-연관 어린선(비스테로이드 설파타제 결핍형)은 스테로이드 설파타제(STS) 결핍과 무관한 희귀 유전성 피부 각화 질환으로, 주로 피부 각질층의 세포 간 지질 구성 이상 및 각질화 조절 장애에 의해 발생합니다. 이 질환의 핵심 병리 기전은 PCSK9–LDL 수용체 축과 직접적인 연관성이 없으며, 현재 문헌상 연결 고리가 보고된 바 없습니다.

TxGNN 모델의 높은 예측 점수(99.43%)는 지식 그래프 내 콜레스테롤 대사 관련 노드를 통한 비특이적 연결에서 비롯되었을 가능성이 높습니다. 이 적응증을 생물학적으로 뒷받침하는 기전 연구, 전임상 데이터, 또는 임상시험은 현재 존재하지 않습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

현재 관련 문헌이 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
X-연관 어린선과 Alirocumab의 PCSK9 억제 기전 간 생물학적 합리성이 부재하며, 이를 지지하는 임상시험 및 문헌 근거가 전혀 없습니다. 높은 TxGNN 점수는 지식 그래프의 비특이적 노드 연결에 기인할 가능성이 크며, 현 단계에서 추가 개발을 진행할 근거가 충분하지 않습니다.

**진행하려면 필요한 것:**
- Alirocumab 작용 기전(MOA) 상세 데이터 확보 (현재 데이터 갭)
- X-연관 어린선과 콜레스테롤 대사 간 연관성에 대한 기초·전임상 근거 탐색
- 한국 내 허가 및 시판 계획 확인
- 허가사항 기반 경고·금기사항 등 안전성 정보 보완

> **참고 — 더 나은 재창출 후보**: 이번 예측 목록 중 **cholesterol catabolic process disease** (예측 순위 5위, 근거 수준 L1, Proceed with Guardrails)는 1건의 완료된 Phase 3 임상시험과 19편의 문헌을 보유하며, Alirocumab의 PCSK9 억제 기전과 직접 부합합니다. 실질적인 재창출 검토는 이 후보를 우선 대상으로 하는 것을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

