---
layout: default
title: Fluorometholone
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Fluorometholone
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

# Fluorometholone: 적응증 정보 없음에서 감염성 전방 포도막염으로

## 한 문장 요약

Fluorometholone은 한국에 시판 중인 제품이 없고 작용기전(MOA) 및 기존 적응증 자료도 확보되지 않은 상태입니다.
TxGNN 모델은 **감염성 전방 포도막염(Infectious Anterior Uveitis)**에 효과가 있을 수 있다고 예측하지만,
현재 이를 뒷받침하는 임상시험은 없고 **문헌 1편**만 존재하며, 그 문헌마저 "비감염성" 포도막염을 다루고 있어 예측과 근거 사이에 불일치가 있습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 허가 자료 없음, MOA 자료 갭) |
| 예측 신규 적응증 | 감염성 전방 포도막염 (Infectious Anterior Uveitis) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Fluorometholone은 국소(안과용) 코르티코스테로이드 계열로,
확보된 문헌에서는 전방 포도막염 치료에 사용되는 국소 스테로이드(dexamethasone, prednisolone acetate, loteprednol, fluorometholone 등) 중 하나로 언급됩니다.

다만 이 유일한 문헌은 제목에서부터 **"비감염성(non-infectious)" 포도막염**을 다루고 있음을 명시하고 있어,
TxGNN이 예측한 **"감염성(infectious)" 전방 포도막염**과는 병인론적으로 맞지 않습니다. 감염성 병인의 경우 병원체 조절이 선행되어야 하며,
스테로이드 단독 사용은 감염을 은폐하거나 악화시킬 위험이 있어 기전상 예측과 근거 문헌 사이에 불일치가 존재합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [29739028](https://pubmed.ncbi.nlm.nih.gov/29739028/) | 2018 | Review | Klinische Monatsblätter für Augenheilkunde | 비감염성 전방 포도막염에서 국소 코르티코스테로이드의 안내 투과율을 비교, prednisolone acetate 1%가 1차 선택이며 loteprednol과 fluorometholone은 상대적으로 투과력이 낮음을 기술 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
관련 임상시험이 전무하고, 유일한 문헌은 예측된 "감염성" 적응증이 아닌 "비감염성" 포도막염을 다루고 있어 근거와 예측 간 불일치가 있습니다. 국내 시판 이력과 허가 자료도 없어 현 단계에서 진행을 권장하기 어렵습니다.

**진행하려면 필요한 것:**
- 작용기전(MOA) 및 기존 적응증 데이터 (DrugBank 등)
- TFDA/MFDS 수준의 허가사항, 경고 및 금기 정보
- "감염성 전방 포도막염"에 특이적인 임상시험 또는 관찰 연구 근거
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

