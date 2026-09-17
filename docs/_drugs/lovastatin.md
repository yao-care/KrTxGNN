---
layout: default
title: Lovastatin
parent: 모델 예측만 (L5)
nav_order: 451
evidence_level: L5
indication_count: 6
---

# Lovastatin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Lovastatin: 원발성 고콜레스테롤혈증에서 동형접합 가족성 고콜레스테롤혈증(HoFH)으로

## 한 문장 요약

Lovastatin은 HMG-CoA 환원효소 억제제(스타틴 계열)로, 원래 원발성 고콜레스테롤혈증 치료에 사용되어 온 약물입니다.
TxGNN 모델은 **동형접합 가족성 고콜레스테롤혈증(Homozygous Familial Hypercholesterolemia, HoFH)**에도 효과가 있을 수 있다고 예측하며(예측 점수 99.89%),
현재 **3건의 관련 3상 임상시험**(단, lovastatin이 아닌 ezetimibe·alirocumab 등 병용/비교 약물 시험)과 **19편의 문헌**이 근거로 확인됩니다. 다만 문헌 중 lovastatin을 직접 다룬 연구는 대부분 1980~90년대의 소규모 사례군 연구이며, LDL 수용체 잔존 기능에 따라 반응이 크게 달라진다는 점이 확인됩니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 원발성 고콜레스테롤혈증 (Primary Hypercholesterolemia) |
| 예측 신규 적응증 | 동형접합 가족성 고콜레스테롤혈증 (Homozygous Familial Hypercholesterolemia, HoFH) |
| TxGNN 예측 점수 | 99.89% (rank 2901) |
| 근거 수준 | L3 (관찰/사례 연구 수준) |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

DrugBank 상 Lovastatin의 공식 작용기전(MOA) 데이터는 확보되지 않았습니다(Data Gap, DG002). 다만 근거 문헌들(PMID 3046888, 7229037, 1611649 등)에서 공통적으로 확인되는 바에 따르면, Lovastatin은 HMG-CoA 환원효소를 억제하여 간세포 내 콜레스테롤 합성을 낮추고, 이에 대한 보상 반응으로 세포 표면 LDL 수용체(LDLR) 발현을 증가시켜 혈중 LDL-C를 낮추는 스타틴 계열 약물입니다.

HoFH는 LDLR 유전자의 이중대립유전자(biallelic) 변이로 LDL 수용체 기능이 심각하게 저하되어 극심한 고LDL혈증과 조기 죽상경화증을 유발하는 희귀 유전질환입니다. 스타틴의 작용기전이 LDL 수용체 상향조절에 의존하므로, 기전상으로는 HoFH에도 적용 가능성이 있습니다.

그러나 근거 문헌은 이 기전적 가정에 중요한 단서를 답니다. PMID 3397806은 "수용체-음성(receptor-negative)" HoFH 환자에서 lovastatin이 LDL 농도나 대사회전에 **효과가 없었다**고 보고한 반면, PMID 2252289·1785747 등은 "수용체-결손(receptor-defective)"형 환자에서 병용요법(콜레스티라민 등)과 함께 부분적 반응을 보고합니다. 즉 HoFH 환자군 내에서도 잔존 LDLR 활성 정도에 따라 lovastatin 반응이 크게 갈리므로, 예측된 적응증 확장은 "전체 HoFH"가 아니라 "잔존 수용체 활성이 있는 아형"에 한정될 가능성이 높습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 완료 | 18 | 8~17세 소아·청소년 HoFH 환자에서 alirocumab(PCSK9 억제제)의 LDL-C 저하 효과 평가 (lovastatin 아님) |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 완료 | 44 | atorvastatin 또는 simvastatin에 ezetimibe를 추가한 장기 안전성·내약성 평가 (lovastatin 아님) |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 완료 | 50 | atorvastatin 또는 simvastatin에 ezetimibe를 추가한 효능·안전성 평가 (lovastatin 아님) |

**주의:** 위 3건은 모두 HoFH 환자 대상 3상 완료 시험이지만, 시험 약물은 alirocumab·ezetimibe이며 lovastatin을 직접 평가한 임상시험은 등록되어 있지 않습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | 사례군 연구 (n=3) | The Journal of Pediatrics | 수용체-음성 HoFH 소아에서 lovastatin(2mg/kg/day) 투여 시 LDL 농도·대사회전에 유의한 변화 없음 |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | 사례 연구 (n=2) | Anales Espanoles de Pediatria | lovastatin+probucol+콜레스티라민 병용요법으로 총콜레스테롤 41.7% 감소 |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | 사례 연구 (n=1) | European Journal of Pediatrics | LDL 혈장분리반출술에 lovastatin 병용, 황색종 호전 등 장기 내약성 확인 |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | 사례 연구 | Anales Espanoles de Pediatria | 수용체-결손형 환자에서 콜레스티라민+lovastatin 병용 시 반응 양호 |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | 사례 보고 (n=1) | JAMA | 간이식 후 소아 HoFH 환자에서 lovastatin(mevinolin) 병용으로 정상 콜레스테롤 수치 달성 |
| [8637439](https://pubmed.ncbi.nlm.nih.gov/8637439/) | 1996 | 사례 연구 | Metabolism: Clinical and Experimental | 시토스테롤혈증 동반 HoFH 환자에서 콜레스티라민과 lovastatin의 상반된 효과 관찰 |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | 리뷰 | Annals of the New York Academy of Sciences | 소아·청소년 이상지질혈증 치료에서 lovastatin 포함 약물요법 개관 |
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | RCT (다른 약물) | Circulation | ezetimibe+atorvastatin/simvastatin 병용, HoFH 다기관 이중맹검 RCT (n=50) |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | 기전 연구 | Arteriosclerosis, Thrombosis, and Vascular Biology | 동일 LDLR 변이에서도 잔존 수용체 발현이 개인마다 달라 PCSK9 억제제(및 스타틴) 반응이 상이함을 규명 |
| [7229037](https://pubmed.ncbi.nlm.nih.gov/7229037/) | 1981 | 기전 연구 | The Journal of Clinical Investigation | HoFH 섬유아세포에서 스타틴 계열(ML-236b)의 스테롤 합성·LDL 수용체 활성에 대한 초기 기전 규명 |

---

## 안전성 고려사항

TFDA/식약처 수준의 경고문, 금기, 약물상호작용 데이터가 모두 확보되지 않았습니다(DG001, Blocking 등급 — S1 안전성 초평가 진입 불가). 안전성 평가를 진행하려면 별도로 원 라벨(허가사항) 정보 확보가 선행되어야 합니다.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 안전성 데이터(경고·금기·DDI)가 전면 Data Gap 상태이며 Blocking 등급으로 분류되어 있어, 최소한의 안전성 초평가(S1)조차 진행할 수 없습니다.
- lovastatin을 직접 HoFH에서 평가한 임상시험은 없고, 문헌 근거는 대부분 1980~90년대의 소규모·비대조 사례 연구이며, 일부는 오히려 "효과 없음"을 보고합니다(PMID 3397806). 반응이 LDLR 잔존 활성(수용체-음성 vs 수용체-결손)에 크게 좌우되어 예측의 실제 적용 범위가 제한적입니다.
- 현재 한국에 lovastatin 허가 제품이 없어(미출시, 0건), 재창출을 실행하려면 신규 허가/도입 절차가 별도로 필요합니다.
- HoFH 표준 치료는 이미 PCSK9 억제제(alirocumab, evolocumab) 등 최신 약제로 이동한 상태로, 오래된 저강도 스타틴의 재창출 가치가 상대적으로 낮습니다.

**진행하려면 필요한 것:**
- TFDA/식약처 원 라벨 기반 경고·금기·DDI 데이터 확보 (DG001 해소)
- DrugBank API를 통한 공식 MOA 데이터 확보 (DG002 해소)
- LDLR 유전형(수용체-음성 vs 수용체-결손)별 반응 계층화 데이터 확보
- 한국 내 허가/도입 가능성 검토 (현재 0건 허가 상태)
- 현행 표준요법(PCSK9 억제제 등) 대비 lovastatin 병용의 임상적 부가가치 재평가
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

