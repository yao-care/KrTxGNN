---
layout: default
title: Tranilast
parent: 僅模型預測 (L5)
nav_order: 693
evidence_level: L5
indication_count: 10
---

# Tranilast
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

# Tranilast: 켈로이드·비후성 반흔에서 치은종(Epulis)으로

## 한 문장 요약

Tranilast는 일본에서 켈로이드 및 비후성 반흔 치료제로 승인되어 사용되어 온 약물로, TGF-β1 매개 섬유아세포 증식과 콜라겐 합성을 억제하는 기전이 알려져 있습니다. TxGNN 모델은 이 약물이 **치은종(Epulis)**에도 효과가 있을 수 있다고 예측했으며, 이를 뒷받침하는 임상시험은 없지만 **치은 섬유아세포를 이용한 시험관 내(in vitro) 연구 1건**이 기전적 근거를 제공합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (참고: 일본에서 켈로이드·비후성 반흔 치료제로 승인된 이력 있음) |
| 예측 신규 적응증 | 치은종 (Epulis) |
| TxGNN 예측 점수 | 99.98% |
| 근거 수준 | L4 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Tranilast의 공식 작용기전(MOA) 데이터는 현재 확보되어 있지 않습니다. 다만 근거 자료에 따르면 tranilast는 TGF-β1에 의해 유도되는 섬유아세포 증식, 콜라겐 합성, 그리고 MMP(matrix metalloproteinase) 조절을 억제하는 것으로 알려져 있으며, 이 기전을 바탕으로 일본에서 켈로이드 및 비후성 반흔 치료제로 승인되어 사용되고 있습니다.

치은종(Epulis)은 치은(잇몸) 조직의 섬유성 과증식 병변으로, 켈로이드·비후성 반흔과 마찬가지로 섬유증식성(fibroproliferative) 질환군에 속합니다. 두 질환 모두 과도한 섬유아세포 활성과 세포외기질 축적이 병리의 핵심이라는 점에서 기전상 연결점이 있습니다.

실제로 문헌근거 중 1건(PMID 15455731)은 tranilast가 사람 치은 섬유아세포에서 MMP-1 분비를 억제함을 시험관 내에서 직접 보여주어, 위 가설을 뒷받침합니다. 단, 함께 검색된 나머지 2건의 문헌(PMID 33369018, 10586135)은 "환상 탄력섬유용해성 거대세포 육아종(annular elastolytic giant cell granuloma)"을 다룬 것으로, 치은종과는 무관하며 질병명 동의어 매칭 과정에서 함께 검색된 것으로 판단됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15455731](https://pubmed.ncbi.nlm.nih.gov/15455731/) | 2004 | 체외연구 (In vitro) | Journal of Periodontology | 사람 치은 섬유아세포에서 tranilast가 MMP-1 분비를 억제함을 확인 — 치은 섬유증식 억제 기전을 직접 뒷받침 |
| [33369018](https://pubmed.ncbi.nlm.nih.gov/33369018/) | 2021 | 증례보고 (치은종과 무관) | Dermatologic Therapy | 환상 탄력섬유용해성 거대세포 육아종 치료 사례 — 질병명 동의어 매칭으로 인한 오검색 |
| [10586135](https://pubmed.ncbi.nlm.nih.gov/10586135/) | 1999 | 증례군/리뷰 (치은종과 무관) | European Journal of Dermatology | 유두상 탄력섬유용해성 거대세포 육아종 증례 — 질병명 동의어 매칭으로 인한 오검색 |

## 한국 시판 정보

Tranilast는 현재 한국에 등재된 허가증이 없어(0건) 미출시 상태입니다.

## 안전성 고려사항

현재 확보된 안전성 정보(주요 경고, 금기, 약물 상호작용)가 없습니다. 국내 미출시 약물로 국내 허가사항 자체가 존재하지 않아, 개발을 진행할 경우 원개발국(일본 등) 허가사항 및 별도의 안전성 프로파일 확보가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
현재 근거는 치은 섬유아세포를 이용한 시험관 내 연구 1건(MMP-1 억제)뿐이며, 동물실험이나 인체 대상 연구는 전무합니다. TxGNN 예측 점수(99.98%)는 매우 높으나 이는 모델 예측치일 뿐 실질적 임상 근거를 대체하지 못합니다. 또한 국내 미출시 약물로 규제·안전성 데이터가 없어 안전성 초기 평가(S1) 단계 진입 자체가 불가능한 상태입니다.

**진행하려면 필요한 것:**
- 원개발국(일본) 허가사항 및 안전성 자료(경고, 금기, DDI) 확보 — 현재 Blocking 수준의 데이터 공백
- Tranilast의 공식 작용기전(MOA) 자료 확보
- 치은 섬유증식 동물모델에서의 tranilast 효능 검증 연구
- 치은종 환자 조직 대상 TGF-β/MMP 경로 검증을 위한 파일럿 연구 설계

---

### 부록: 기타 예측 적응증 (참고용, 근거 미비)

동일한 Evidence Pack 내 나머지 9개 예측 적응증은 모두 임상시험·문헌 근거가 전무한 L5 수준으로, 현 단계에서는 참고 정보로만 제시합니다.

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 권장 |
|------|-----------|-----------|----------|------|
| 1 | 지루각화증 (Seborrheic keratosis) | 99.98% | L5 | Hold |
| 2 | 지루피부염 (Seborrheic dermatitis) | 99.98% | L5 | Hold |
| 3 | 성대 폴립 (Polyp of vocal cord) | 99.98% | L5 | Hold |
| 4 | 중이 폴립 (Polyp of middle ear) | 99.98% | L5 | Hold |
| 5 | 전두동 폴립 (Polyp of frontal sinus) | 99.98% | L5 | Hold |
| 6 | 외이도 폴립 (Polyp of external auditory canal) | 99.98% | L5 | Hold |
| 8 | 섬유상피 폴립 (Fibroepithelial polyp) | 99.98% | L5 | Hold |
| 9 | 요관 폴립 (Polyp of ureter) | 99.98% | L5 | Hold |
| 10 | 외음부 폴립 (Polyp of vulva) | 99.98% | L5 | Hold |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

