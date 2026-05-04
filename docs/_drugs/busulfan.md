---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: 조혈모세포이식 전처치에서 골수이형성증후군으로

## 한 문장 요약

Busulfan은 이중기능성 알킬화제로, 국제적으로 만성골수성백혈병(CML) 치료 및 조혈모세포이식(HSCT) 전 골수제거 전처치에 사용되어 왔습니다.
TxGNN 모델은 **골수이형성증후군(Myelodysplastic Syndrome)**에 효과가 있을 것으로 예측하며,
기전적 타당성과 HSCT 전처치 분야의 확립된 임상 관행이 이 방향을 강력히 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 데이터 없음 (국제적으로 CML 및 HSCT 전처치에 사용) |
| 예측 신규 적응증 | 골수이형성증후군 (Myelodysplastic Syndrome) |
| TxGNN 예측 점수 | 99.62% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 (未上市) |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Busulfan은 세포 내 DNA의 구아닌 잔기에 공유 결합하여 가닥 간 교차결합(interstrand crosslink)을 형성하는 이중기능성 알킬화제입니다. 이 기전은 빠르게 분열하는 세포, 특히 이상 클론성 조혈줄기세포에 강한 세포독성을 나타냅니다. 상세 MOA 데이터가 현재 제한적이나, Busulfan은 수십 년간 임상에서 검증된 골수제거제로 그 기전적 효과는 폭넓게 확립되어 있습니다.

골수이형성증후군(MDS)은 비정상 조혈줄기세포의 클론성 증식으로 조혈 기능 장애를 초래하는 질환으로, 동종 조혈모세포이식(allo-HSCT)이 현재 유일한 치유적 치료법입니다. Busulfan은 MDS 환자의 allo-HSCT 전처치 방안—BuCy(Busulfan + Cyclophosphamide) 및 BuFlu(Busulfan + Fludarabine)—의 핵심 약물로 이미 광범위하게 적용되고 있습니다.

기전적으로 Busulfan의 강력한 골수제거 효과는 MDS 이상 클론 세포를 직접 제거하고, 공여 줄기세포 생착을 위한 조혈 공간을 확보하는 데 필수적으로 기여합니다. TxGNN 예측 점수 99.62%는 이 확립된 임상적 역할을 명확히 반영합니다.

---

## 임상시험 근거

현재 Evidence Pack 내 관련 임상시험 등록이 없습니다.

> **참고**: Busulfan의 MDS에 대한 HSCT 전처치 역할은 별도 등록 임상시험보다 기허가 적응증의 표준 임상 관행으로 확립되어 있습니다. MeSH 용어 `"Busulfan AND myelodysplastic syndromes AND transplantation conditioning"`을 이용한 보완 검색이 권장됩니다.

---

## 문헌 근거

현재 Evidence Pack 내 관련 문헌이 없습니다.

> **참고**: BuCy/BuFlu 전처치 방안 관련 문헌은 조혈모세포이식 분야에 다수 존재합니다. PubMed 직접 검색을 통한 근거 보완이 권장됩니다.

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (알킬화제 계열 — Bifunctional Alkylating Agent) |
| 골수억제 위험 | 고위험 — 전처치 목적으로 의도적 골수제거 유도; 범혈구감소증 필연 발생, HSCT 지지 요법(G-CSF, 수혈 등) 필수 |
| 구토 유발성 등급 | 고도 (High Emetogenic Risk) — 예방적 항구토제 병용 투여 필수 |
| 모니터링 항목 | CBC (분류 포함), 간기능 (AST/ALT/ALP/총빌리루빈), 신기능 (Cr/BUN), 혈청 Busulfan 농도 (TDM 강력 권장) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 — 전용 생물안전작업대(BSC), 방호복, 이중 장갑, 눈 보호구 착용 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
Busulfan은 MDS 환자의 allo-HSCT 전처치에서 이미 표준적 역할을 담당하는 약물로, TxGNN 예측(99.62%, L2 근거)은 이를 명확히 반영합니다. 다만 한국 내 미허가 상태이며 상세 안전성 데이터가 확인되지 않아, 사용 시 엄격한 임상 프로토콜과 규제 준수가 전제되어야 합니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가 현황 재확인 및 허가 외 사용(off-label) 법적 근거 검토
- DrugBank API 조회를 통한 상세 MOA 데이터 보완 (DG002 해소)
- MFDS/TFDA 허가사항 PDF에서 경고·금기·약물 상호작용 정보 추출 (DG001 해소)
- Busulfan TDM(치료약물 모니터링) 프로토콜 수립 — 목표 AUC 범위 정의 포함
- BuCy vs BuFlu 전처치 방안 선택 기준 및 비교 근거 문헌 검토
- 정맥주사 제형(Busulfex® IV) 국내 공급 체계 및 조달 가능성 확인
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

