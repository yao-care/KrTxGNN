---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Basiliximab
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

# Basiliximab: 이식 거부반응 예방에서 다발성 골수종으로

## 한 문장 요약

Basiliximab은 CD25(IL-2 수용체 α 사슬)를 차단하는 키메릭 단클론항체로, 국제적으로 신장이식 후 급성 거부반응 예방에 사용되어 왔으나 한국에는 현재 허가 이력이 없습니다.
TxGNN 모델은 **다발성 골수종(Plasma Cell Myeloma)**에 효과가 있을 수 있다고 예측하며,
현재 **3건의 임상시험**과 **3편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이식 거부반응 예방 (국제 허가 기준, 한국 내 허가 이력 없음) |
| 예측 신규 적응증 | 다발성 골수종 (Plasma Cell Myeloma) |
| TxGNN 예측 점수 | 95.61% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Basiliximab은 활성화 T 세포 표면에 발현되는 IL-2 수용체의 α 사슬(CD25)에 특이적으로 결합하는 키메릭 단클론항체입니다. CD25/IL-2 신호 경로를 차단함으로써 T 세포의 활성화와 증식을 억제하며, 국제적으로는 신장이식 후 급성 거부반응 예방의 유도 요법으로 사용됩니다. 작용 기전의 세부 데이터(MOA)는 이번 Evidence Pack에 포함되지 않아 추가 확인이 필요합니다.

다발성 골수종 치료 경로에서 자가조혈모세포이식(ASCT) 및 동종조혈모세포이식(allo-HSCT)은 표준 치료 선택지입니다. Basiliximab이 이 적응증에서 기여할 수 있는 경로는 두 가지입니다: (1) 동종이식 상황에서 CD25/IL-2 경로 차단을 통해 GvHD를 예방하고, (2) 자가이식 상황에서 면역을 억제하는 조절 T 세포(Treg)를 선택적으로 고갈시켜 이식편대골수종(Graft-versus-Myeloma) 효과를 강화하는 것입니다.

단, Basiliximab 자체에는 직접적인 항골수종 활성이 없습니다. 이식 치료를 안전하게 시행하거나 이식 후 면역 반응을 조율하는 보조적 역할로서의 기전 연결이며, 연결 고리는 간접적이나 생물학적으로 타당합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | 완료 | 30 | 다발성 골수종 ASCT 환자에서 Basiliximab을 이용한 조절 T 세포(Treg) 고갈의 안전성 및 실현 가능성 평가 |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | 완료 | 17 | 비청수성(비골수제거) 동종이식 후 GvHD 예방을 위한 Basiliximab + cyclosporine 병용 효과 평가 (골수종 환자 포함 가능) |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | N/A | 조기 종료 | 10 | 이식 후 GvHD 예방에서 Basiliximab + cyclosporine vs. cyclosporine 단독 비교 (소규모 조기 종료, 증거 효력 낮음) |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Phase 1 임상 연구 | J Immunother Cancer | 다발성 골수종 ASCT 환자에서 이식 후 Treg가 빠르게 재구성되며 골수종 세포에 대한 면역 반응을 억제함을 확인; Basiliximab을 이용한 Treg 고갈이 이식 후 면역 강화에 기여할 가능성 제시 |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | 회고적 증례 시리즈 | Bone Marrow Transplant | 동종조혈모세포이식 후 스테로이드 불응성 급성 GvHD 환자 17명(다발성 골수종 포함)에서 Basiliximab의 내약성 및 치료 반응 평가 |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | 증례 보고 | Am J Kidney Dis | 다발성 골수종으로 인한 신부전 환자 4명의 신장이식 사례 보고; Basiliximab 유도 요법 적용 포함 |

---

## 한국 시판 정보

한국 내 Basiliximab 허가 이력이 없습니다 (한국의약품안전처 시판 허가 0건). 국제적으로는 **Simulect®** (Novartis) 브랜드명으로 신장이식 후 급성 거부반응 예방에 허가되어 있습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다발성 골수종에서 Basiliximab의 예측 역할은 직접적인 항골수종 활성이 아닌 이식 치료 보조(GvHD 예방 및 Treg 고갈)에 한정되며, 현재 근거는 소규모 Phase 1 파일럿 연구(n=30)와 회고적 증례 시리즈에 불과하여 독립적인 적응증으로 인정받기에 근거가 부족합니다.

**진행하려면 필요한 것:**
- Basiliximab의 작용 기전 세부 데이터(MOA) 확보 (현재 Data Gap)
- 한국 내 도입 가능성 및 허가 경로 사전 검토 (현재 미허가)
- 다발성 골수종 ASCT 또는 allo-HSCT 환경에서 충분한 규모의 무작위 대조 임상시험 설계
- Treg 고갈 전략이 GvM 효과 및 장기 무사건 생존율에 미치는 영향 측정을 위한 바이오마커 연구
- 스테로이드 불응성 GvHD 치료에서의 골수종 특이적 치료 결과 데이터 수집
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

