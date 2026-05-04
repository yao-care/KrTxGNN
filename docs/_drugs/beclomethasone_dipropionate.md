---
layout: default
title: Beclomethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 1
---

# Beclomethasone Dipropionate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Beclomethasone Dipropionate: 알레르기 질환(천식/비염)에서 아토피 습진으로

## 한 문장 요약

Beclomethasone Dipropionate(BDP)는 합성 당질코르티코이드로, 전 세계적으로 천식 및 알레르기성 비염 치료에 널리 사용되어 온 스테로이드제이며, 한국 내 허가 이력은 현재 확인되지 않습니다.
TxGNN 모델은 **아토피 습진(Atopic Eczema)**에 효과가 있을 수 있다고 예측하며,
현재 **0건의 임상시험**과 **18편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 데이터 없음 (한국 미허가) |
| 예측 신규 적응증 | 아토피 습진 (Atopic Eczema) |
| TxGNN 예측 점수 | 99.41% |
| 근거 수준 | L2 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

Beclomethasone Dipropionate(BDP)는 합성 당질코르티코이드로, 세포 내 당질코르티코이드 수용체(GR)에 결합하여 NF-κB 전사인자 활성을 억제합니다. 이를 통해 아토피 습진(AD)의 핵심 병인인 Th2 면역 과활성화를 매개하는 IL-4, IL-13, IL-31, TNF-α 등 염증성 사이토카인 발현을 하향 조절합니다. 아울러 IgE 합성 억제, 비만세포 탈과립 억제, 호산구 침윤 감소 등 AD의 주요 병리 기전에 직접 작용합니다.

아토피 습진은 Th2 경로 과활성을 특징으로 하는 만성 염증성 피부 질환이며, 코르티코스테로이드는 이미 아토피 피부염의 국소 치료 표준 요법으로 확립되어 있습니다. BDP는 그 중에서도 강력한 국소 효능을 지닌 화합물로, 기전적 합리성은 높습니다. 실제로 1984년 RCT를 포함한 여러 임상 연구에서 경구 및 비강 내 투여 경로를 통한 치료 가능성이 확인된 바 있습니다.

다만 주요 문헌에서 연구된 투여 경로는 경구 또는 비강 내 투여로, 피부과 표준 투여 경로인 국소(외용) 도포와 상이합니다. 경구 투여 시 성장 저해, 부신 억제 등 전신 부작용 위험이 보고되어 있으므로, 적절한 제형 선택 및 투여 경로 최적화에 대한 신중한 평가가 필요합니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|------|------|------|---------|
| [6434024](https://pubmed.ncbi.nlm.nih.gov/6434024/) | 1984 | RCT | British Medical Journal | 중증 아토피 습진 소아 26명 이중맹검 교차 시험에서 경구+비강 BDP 병용군이 위약군 대비 유의한 증상 개선 확인 |
| [1476023](https://pubmed.ncbi.nlm.nih.gov/1476023/) | 1992 | 임상 연구 | Acta Derm Venereol Suppl | 소아 중증 아토피 피부염 14명에게 경구 BDP 투여 시 10명에서 안정적 질병 조절 달성, 선형 성장 감소 부작용 관찰 |
| [30911861](https://pubmed.ncbi.nlm.nih.gov/30911861/) | 2019 | 제형 연구 | AAPS PharmSciTech | 아토피 피부염 동물 모델에서 BDP 혼합 미셀 하이드로겔 제형의 최적화 및 피부 전달 효능 평가 |
| [14522624](https://pubmed.ncbi.nlm.nih.gov/14522624/) | 2003 | 임상 안전성 연구 | J Dermatol Treat | 아토피 습진 소아에서 습식 랩 스테로이드 요법이 단기 성장 속도 및 골 대사에 미치는 영향 평가 |
| [8765824](https://pubmed.ncbi.nlm.nih.gov/8765824/) | 1996 | 임상 연구 | J Allergy Clin Immunol | 아토피 피부염 환자에서 국소 스테로이드 사용이 시험관 내 자발적 IgE 생성을 증가시킬 수 있음을 보고, 크로모글리케이트의 대안 가능성 제시 |
| [374799](https://pubmed.ncbi.nlm.nih.gov/374799/) | 1979 | 임상 연구 | Jpn J Dermatol | 베타메타손 17-발레레이트 및 플루오시노나이드 대비 국소 BDP 도포의 전신 흡수 및 부신 억제 효과 비교 |
| [19874229](https://pubmed.ncbi.nlm.nih.gov/19874229/) | 2009 | 전임상 연구 | Immunopharmacol Immunotoxicol | 마우스 모델에서 BDP 대비 모메타손의 국소 항염 효과와 전신 부작용 해리(dissociation) 비교; 모메타손이 BDP보다 국소/전신 효과 비율 유리 |
| [9463794](https://pubmed.ncbi.nlm.nih.gov/9463794/) | 1998 | 리뷰 | Drugs | BDP의 16α-메틸 유사체인 모메타손의 아토피 피부염 등 피부 염증 질환 치료 효능 및 약리학적 특성 종합 검토 |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | 리뷰 | Neuroimmunomodulation | 비강 내 코르티코스테로이드 사용과 시상하부-뇌하수체-부신(HPA) 축 억제 관계 고찰; 천식·아토피 피부염 동반 시 BDP 중복 노출 위험 경고 |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | 리뷰 | Allergy | 천식 환자에서 흡입 코르티코스테로이드 사용에 따른 지연형 접촉 알레르기 및 즉시형 알레르기 발생률 조사 |

---

## 한국 시판 정보

현재 한국 내 Beclomethasone Dipropionate 단일 성분 제제의 허가 내역이 확인되지 않습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
1984년 이중맹검 위약 대조 RCT(PMID 6434024)를 포함한 여러 임상 연구에서 BDP의 아토피 습진 치료 가능성이 확인되었으며, 당질코르티코이드로서의 기전이 AD의 Th2 주도 병태생리와 직접적으로 부합합니다. 다만 한국 내 허가 이력이 없고 안전성 공식 데이터 확보가 선행되어야 합니다.

**진행하려면 필요한 것:**
- 한국 식약처(MFDS) 허가사항 및 안전성 정보(경고·금기·부작용) 확보
- DrugBank MOA 상세 데이터 검토 및 기전 문서화
- 현대적 아토피 습진 임상시험 계획 수립 (특히 외용 제형 또는 경구 저용량 접근법)
- 최적 투여 경로(국소 외용 vs. 경구 vs. 비강 내) 및 소아 대상 안전성 모니터링 계획 마련
- 전신 부작용(부신 억제, 성장 저해) 모니터링 프로토콜 사전 설계
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

