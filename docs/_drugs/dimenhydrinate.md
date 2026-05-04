---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 2
---

# Dimenhydrinate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# DIMENHYDRINATE: 멀미에서 알레르기성 두드러기로

## 한 문장 요약

DIMENHYDRINATE는 Diphenhydramine과 8-chlorotheophylline의 복합염으로, 원래 멀미(구역·구토) 예방 및 치료에 사용됩니다.
TxGNN 모델은 **알레르기성 두드러기(Allergic Urticaria)**에 효과가 있을 수 있다고 예측하며,
현재 관련 **임상시험 0건**과 **문헌 1편**이 이 방향과 관련됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 멀미, 구역, 구토 (H1 항히스타민계 항구토제) |
| 예측 신규 적응증 | 알레르기성 두드러기 (Allergic Urticaria) |
| TxGNN 예측 점수 | 99.74% |
| 근거 수준 | L4 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

DIMENHYDRINATE는 Diphenhydramine과 8-chlorotheophylline의 복합염입니다. 체내에서 Diphenhydramine으로 분해되어 활성을 나타내며, Diphenhydramine은 제1세대 H1 수용체 길항제로서 히스타민 H1 수용체를 차단해 혈관투과성 증가, 가려움증, 팽진(wheal) 형성을 억제합니다.

알레르기성 두드러기의 핵심 병리는 IgE 매개 비만세포 활성화 → 히스타민 대량 방출로, H1 길항제는 EAACI/GA²LEN/EDF/WAO 가이드라인에서 두드러기의 제1선 치료로 명확히 인정하고 있습니다. 따라서 DIMENHYDRINATE의 활성 성분인 Diphenhydramine의 기전과 알레르기성 두드러기 병태생리 간의 기전적 연관성은 매우 강합니다(★★★★★).

다만, DIMENHYDRINATE 염 복합체 자체를 대상으로 한 알레르기성 두드러기 직접 임상시험 데이터는 현재 확인되지 않습니다. Diphenhydramine 단방에 비해 DIMENHYDRINATE에 특화된 근거가 부족하며, 현재 단계에서는 기전 기반 가설 수준에 해당합니다. 아울러 현재 한국 내 시판 허가(총 0건)도 없어 즉각적인 임상 적용보다 연구 질문 수립이 먼저 필요합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | 약동학 연구 | Veterinary Dermatology | 건강한 개에서 DIMENHYDRINATE 경구 투여 시 Diphenhydramine으로 전환되며 우수한 흡수율을 보임; 히스타민 유발 팽진 형성에 대한 약동학·약역학적 효과 확인. 인체 데이터 없음 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
활성 성분인 Diphenhydramine의 H1 길항 기전은 알레르기성 두드러기와 강한 기전적 연관성을 가지나, DIMENHYDRINATE 자체에 대한 인체 임상 근거가 전무하고 현재 한국 내 허가 이력도 없어 즉각적인 재창출 추진보다 연구 질문 정립 단계에 해당합니다.

**진행하려면 필요한 것:**
- DIMENHYDRINATE 규제 자료 확보: 국내외 허가사항(경고, 금기, 이상반응) PDF 수집 및 파싱 [DG001 해소]
- 작용 기전 상세 데이터 보완: DrugBank API 조회를 통한 MOA 확인 [DG002 해소]
- 인체 대상 Diphenhydramine vs. DIMENHYDRINATE 두드러기 치료 효능 비교 문헌 추가 검색
- 차순위 예측 적응증 **한랭 두드러기(Cold Urticaria, 예측 점수 99.23%)** 에 대한 동반 검토 — 현재 임상시험·문헌 모두 0건으로 근거 수준 L5, 별도 보류 유지
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

