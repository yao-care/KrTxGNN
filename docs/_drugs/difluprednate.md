---
layout: default
title: Difluprednate
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
---

# Difluprednate
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

# DIFLUPREDNATE: 술후 안구 염증에서 홍채 질환으로

## 한 문장 요약

DIFLUPREDNATE(Durezol®)는 고지용성 합성 당질코르티코이드로, FDA에서 술후 안구 염증 및 내인성 전포도막염 치료에 허가된 안구용 유화액입니다.
TxGNN 모델은 **홍채 질환(Iris Disease / 虹膜炎)**에 효과가 있을 수 있다고 예측하며,
현재 **4건의 임상시험**과 **2편의 문헌**이 이 방향을 지지합니다.

> ⚠️ **참고**: TxGNN 예측 상위 순위(1~9위)는 전임상·모델 예측 수준의 근거만 존재하거나 제제학적 부적합으로 모두 **Hold** 판정을 받았습니다. 홍채 질환(10위)이 유일하게 L1 근거와 함께 **Proceed with Guardrails** 판정을 받아 이 보고서의 주요 분석 대상으로 선정하였습니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 술후 안구 염증, 내인성 전포도막염 (FDA 허가; 한국 미허가) |
| 예측 신규 적응증 | 홍채 질환 (Iris Disease / 虹膜炎) |
| TxGNN 예측 점수 | 99.16% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

DIFLUPREDNATE는 6α,9-이중불소 치환된 합성 당질코르티코이드로, 0.05% 안구 유화액(Durezol®) 제형으로 FDA에서 내인성 전포도막염(Endogenous Anterior Uveitis) 및 술후 안구 염증 치료에 승인된 약물입니다. 상세한 작용 기전(MOA) 데이터는 현재 미확보 상태이나, 약물의 고지용성 구조가 각막 투과를 가능하게 하여 홍채·모양체 조직에 국소적으로 높은 농도를 달성하고, 당질코르티코이드 수용체(GR) 촉진을 통해 NF-κB 경로를 억제함으로써 IL-1β, PGE₂, TNF-α 등 전방 염증 매개물질을 효과적으로 감소시키는 것으로 알려져 있습니다.

홍채 질환(Iris Disease)은 전방 포도막염(Anterior Uveitis)의 핵심 아형인 홍채염(Iritis)을 포함하며, DIFLUPREDNATE의 기존 FDA 허가 적응증과 동일한 해부학적·병리학적 기전을 공유합니다. 전임상 약동학 연구(PMID 21182429)에서는 안구 투여 후 토끼 홍채 조직 내 활성 대사체(DFBA) 농도가 치료적 수준에 도달함을 확인하였으며, 이는 기전적 타당성을 추가로 뒷받침합니다.

주목할 점은, 이 예측이 기존 FDA 허가 범위와 사실상 중첩되므로 전통적 의미의 '약물 재창출'보다는 **한국 MFDS 신규 품목 허가 신청** 관점으로 접근하는 것이 더 적합합니다. Phase 3 임상시험(NCT00407056)에서 본 약물의 중증 전포도막염 치료 효능이 직접 확인되었으므로, 한국 허가 신청의 핵심 근거 자료로 활용 가능합니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00407056](https://clinicaltrials.gov/study/NCT00407056) | Phase 3 | 완료 | 20 | 0.05% DIFLUPREDNATE 안구 유화액의 중증 전포도막염(전방 포도막염 및 범포도막염 포함) 치료 효능을 직접 평가한 개방표지 연구. 홍채 질환 적응증의 핵심 직접 근거 **(Grade A)** |
| [NCT01124045](https://clinicaltrials.gov/study/NCT01124045) | Phase 3 | 완료 | 80 | 소아(0~3세) 백내장 수술 후 안구 염증 치료에서 Durezol™(DIFLUPREDNATE 0.05%) vs. Pred Forte™(prednisolone acetate 1%) 안전성·효능 비교 다기관 무작위 이중맹검 연구. DIFLUPREDNATE 안구 사용의 직접 근거 **(Grade B)** |
| [NCT03693989](https://clinicaltrials.gov/study/NCT03693989) | Phase 3 | 완료 | 178 | 수정체 유화술 후 안구 염증·통증 치료에서 안구 유화액 PRO-145 효능 평가 (이중맹검, 병행군, 다기관). 연구 약물이 본 품목은 아니나 동류 안구 유화액 제형의 간접 참고 자료 **(Grade C)** |
| [NCT05082415](https://clinicaltrials.gov/study/NCT05082415) | N/A | 완료 | 9,456 | 습성 AMD 환자에서 Brolucizumab 실제 임상 안전성 후향 코호트 연구(IRIS Registry 활용). 연구 약물 및 적응증이 모두 다르므로 직접 관련성 낮음 **(Grade C)** |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | 동물 연구 (PK/PD) | J Ocul Pharmacol Ther | 토끼 안구에서 DIFLUPREDNATE 유화액의 약동·약력학 특성 평가. 당질코르티코이드 수용체 결합 생체분석으로 홍채 조직 내 활성 대사체(DFBA) 치료 농도 도달 확인; 다른 안구용 코르티코이드 대비 최고 활성 수준 |
| [27594198](https://pubmed.ncbi.nlm.nih.gov/27594198/) | 2016 | 증례 보고 | Ophthalmology | 에볼라 생존자에서 발생한 범포도막염 및 홍채 색소부전의 장기 관리 사례 보고 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 안구용 코르티코이드 계열의 일반적 주의사항으로, 안내압 상승, 후낭하 백내장 형성, 이차 감염(진균·바이러스) 가능성에 대한 모니터링이 권장됩니다. 본 약물의 구체적 경고·금기 데이터는 FDA 허가사항(Durezol® Prescribing Information) 또는 MFDS 신청 자료를 통해 확인이 필요합니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
DIFLUPREDNATE 0.05% 안구 유화액은 FDA에서 내인성 전포도막염(홍채염 포함) 치료에 이미 허가받았으며, Phase 3 직접 임상시험(NCT00407056)이 L1 수준의 효능 근거를 제공합니다. 한국 미시판 상태이므로 약물 재창출보다 **MFDS 신규 품목 허가 신청**이 더 효율적이고 규제 경로가 명확한 접근입니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 보완 (DrugBank API 조회; Data Gap DG002 해소)
- FDA 허가사항(Durezol® PI) 기반 경고·금기·이상반응 정보 확보 (Data Gap DG001 해소)
- 안내압 상승·백내장 유발 등 안구 코르티코이드 장기 투여 관련 안전성 모니터링 계획 수립
- MFDS 품목 허가 신청을 위한 임상자료 패키지 준비 (NCT00407056 pivotal study 활용 검토)
- 국내 교차 임상시험 필요 여부에 대한 MFDS 사전 상담
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

