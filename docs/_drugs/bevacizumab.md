---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: 항혈관신생 치료에서 낭종성 종양으로

## 한 문장 요약

Bevacizumab은 VEGF-A를 특이적으로 중화하는 항혈관신생 단클론항체로, 글로벌 시장에서 대장직장암·비소세포폐암·난소암 등 다수의 고형암에 허가되어 있으나 현재 대만 내 허가 이력이 없습니다.
TxGNN 모델은 **10개의 신규 적응증**에 대한 예측 가능성을 제시하며, 그 중 **낭종성 종양(Cystic Neoplasm)**에 대해서는 **8건의 임상시험**과 **20편의 문헌**이 효능을 지지합니다.
본 보고서는 10개 예측 적응증 전체를 종합 평가하며, 최고 수준의 근거(L1)를 보유한 낭종성 종양을 중심으로 상세 분석을 제공합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고형암 항혈관신생 치료 (대장직장암, 비소세포폐암, 난소암 등 — 글로벌 허가, 대만 미허가) |
| 주요 예측 적응증 | 낭종성 종양 (Cystic Neoplasm) — 10개 예측 중 최고 근거 |
| TxGNN 예측 점수 | 99.89% (전체 예측 순위 #2,790) |
| 근거 수준 | L1 |
| 대만 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 10개 예측 적응증 종합 현황

| 순위 | 적응증 | TxGNN 점수 | 근거 수준 | 임상시험 | 문헌 | 권장 결정 |
|------|--------|-----------|----------|---------|------|---------|
| 1 | 후두개 종양 (Epiglottis Neoplasm) | 99.90% | L5 | 0 | 0 | Hold |
| 2 | 혀 양성 종양 (Benign Neoplasm of Tongue) | 99.90% | L4 | 0 | 7 | Hold |
| 3 | 고환·부고환 종양 (Tumor of Testis and Paratestis) | 99.90% | L5 | 0 | 0 | Hold |
| 4 | 하인두 양성 종양 (Benign Neoplasm of Hypopharynx) | 99.90% | L5 | 0 | 0 | Hold |
| 5 | 구강저 양성 종양 (Benign Neoplasm of Floor of Mouth) | 99.90% | L3 | 1 | 2 | Research Question |
| 6 | 경추 신경모세포종 (Cervical Neuroblastoma) | 99.89% | L3 | 5 | 2 | Research Question |
| **7** | **낭종성 종양 (Cystic Neoplasm)** | **99.89%** | **L1** | **8** | **20** | **Proceed with Guardrails** |
| 8 | 비강 내반성 유두종 (Nasal Cavity Inverting Papilloma) | 99.89% | L4 | 4 | 0 | Hold |
| 9 | 간엽종 (Mesenchymoma) | 99.89% | L5 | 0 | 0 | Hold |
| 10 | 경정맥공 신경초종 (Schwannoma of Jugular Foramen) | 99.89% | L5 | 0 | 0 | Hold |

---

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Bevacizumab은 혈관내피성장인자(VEGF-A)를 특이적으로 중화하는 인간화 단클론항체로, 신생 혈관 형성에 필수적인 VEGF-A 신호전달을 차단하여 종양 혈액공급을 억제합니다. 이 기전은 이론적으로 혈관신생에 의존하는 모든 고형종양에 적용 가능하며, 실제로 대장직장암·난소암·비소세포폐암 등 다양한 암종에서 임상적 유효성이 확인되어 있습니다.

낭종성 종양—특히 난소 장액성·점액성 낭선암종, 복막 점액종(Pseudomyxoma Peritonei) 등—은 VEGF 의존성 혈관신생과 복강 내 삼출액 생성에 강하게 의존합니다. Bevacizumab에 의한 VEGF-A 중화는 종양 산소·영양 공급 차단과 복수 억제를 동시에 기대할 수 있으며, 이는 NCT00565851(Phase 3, n=1,052)과 같은 대규모 시험을 포함한 다수의 임상근거로 이미 검증된 기전-질환 대응 관계입니다. 저등급 장액성 난소암 및 복막 점액종에 대한 별도의 후향적 연구와 체계적 문헌고찰에서도 반응률 및 생존 이점이 보고되고 있습니다.

경추 신경모세포종(L3)의 경우에도 VEGFR 과발현 및 혈관신생 의존성이 보고되어 있으며, 후각 신경모세포종(Olfactory Neuroblastoma) 증례에서 Bevacizumab 단독 항혈관신생 요법의 지속적 완화 효과가 관찰된 바 있어 간접적 기전 지지 근거가 존재합니다. 반면, 두경부 양성 종양(후두개·혀·구강저·하인두)은 VEGF 의존성이 있어 기전적 연관성은 있으나, 양성 종양에서 천공·누공·출혈 등 Bevacizumab 특이 독성의 위험-효익 비가 불분명하여 추가 전임상·임상 데이터 확보가 선행되어야 합니다.

---

## 임상시험 근거 (낭종성 종양)

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Phase 3 | 진행 중 (모집 종료) | 1,052 | 백금 감수성 재발성 난소/복막/난관암에서 Carboplatin·Paclitaxel(또는 Gemcitabine) ± Bevacizumab 무작위 비교; 2차 종양감축술 병용 효과 동시 평가 |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Phase 2 | 진행 중 (모집 종료) | 133 | 희귀 고형종양(낭종성 아형 포함)에서 Atezolizumab + Bevacizumab 병용 면역항암 요법의 효능 및 안전성 |
| [NCT00381797](https://clinicaltrials.gov/study/NCT00381797) | Phase 2 | 완료 | 97 | 소아 재발성·불응성 악성 신경교종·상의세포종·저등급 신경교종에서 Bevacizumab + Irinotecan 병용; 낭종성 하위유형 포함 |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | 완료 | 66 | 전이성 신세포암·두경부암 등에서 Erlotinib + Cetuximab ± Bevacizumab 안전성 및 최적 용량 확립 |
| [NCT00023959](https://clinicaltrials.gov/study/NCT00023959) | Phase 1 | 완료 | 39 | 불량 예후 두경부암에서 Bevacizumab + Fluorouracil + Hydroxyurea + 동시 방사선(B-FHX); Bevacizumab 안전성 기초 데이터 제공 |
| [NCT00492089](https://clinicaltrials.gov/study/NCT00492089) | Phase 2 | 완료 | 11 | 뇌 방사선 손상 감소에 대한 Bevacizumab 무작위 비교; CNS 및 전신 안전성 참조 데이터 |
| [NCT00324987](https://clinicaltrials.gov/study/NCT00324987) | Phase 3 | 조기 종료 | 12 | 전이성 GIST에서 Imatinib ± Bevacizumab 병용 비교; 조기 종료(n=12)로 실질적 해석 한계 |
| [NCT01096381](https://clinicaltrials.gov/study/NCT01096381) | N/A | 종료 | 8 | Bevacizumab 유발 고혈압 바이오마커 탐색; 안전성 모니터링 참조 목적으로만 활용 |

---

## 문헌 근거 (낭종성 종양)

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | 임상 연구 | Future Oncology | 재발성 저등급 장액성 난소암(n=51)에서 Bevacizumab 병용 화학요법; ORR 54.1%, 중앙 PFS 15개월 |
| [37657955](https://pubmed.ncbi.nlm.nih.gov/37657955/) | 2023 | 임상 연구 | Clinical Colorectal Cancer | 수술 불가/재발성 충수돌기 기원 복막 점액종에서 Mitomycin-C + 메트로놈 Capecitabine + Bevacizumab 효능·안전성 |
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | 체계적 고찰 | Current Oncology | 저등급 장액성 난소암에서 Bevacizumab 치료 효능 및 안전성에 관한 체계적 문헌고찰 |
| [40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/) | 2025 | RCT 보조 연구 | Eur J Cancer | PAOLA-1 Phase 3 시험에서 BRCA1/RAD51C 메틸화가 Bevacizumab + Olaparib 유지 요법의 예측 바이오마커로 기능함을 확인 |
| [32494876](https://pubmed.ncbi.nlm.nih.gov/32494876/) | 2020 | 리뷰/가이드라인 | Current Oncology Reports | 진행성 고등급 장액성 난소암 1차 치료 표준 가이드라인; VEGF 억제제(Bevacizumab) 역할 및 유지 요법 근거 종합 |
| [24978709](https://pubmed.ncbi.nlm.nih.gov/24978709/) | 2014 | 임상 연구 | Int J Gynecol Cancer | 재발성 저등급 장액성 난소암/복막암에서 Bevacizumab ± 화학요법의 반응률 및 임상 활성 |
| [27154293](https://pubmed.ncbi.nlm.nih.gov/27154293/) | 2016 | 임상·중개 연구 | J Translational Medicine | 재발성 복막 점액종에서 GNAS 돌연변이가 Capecitabine + Bevacizumab 병용의 예후 예측 인자임을 확인 |
| [27141073](https://pubmed.ncbi.nlm.nih.gov/27141073/) | 2016 | 리뷰 | Annals of Oncology | 점액성 난소암(양성·경계성·악성) 병리 특성, 일차/전이성 감별 및 치료 전략 종합 고찰 |
| [27412268](https://pubmed.ncbi.nlm.nih.gov/27412268/) | 2016 | Phase 2 | Cancer | 삼중음성 전이성·국소진행성 유방암에서 Paclitaxel + Capecitabine + Bevacizumab 1차 요법; ORR 및 PFS 보고 |
| [18796376](https://pubmed.ncbi.nlm.nih.gov/18796376/) | 2008 | 증례 계열 | Clin Transl Oncol | 다회 전처치 재발성 난소암에서 저용량 경구 Cyclophosphamide + Bevacizumab 메트로놈 병용의 종양 반응 |

---

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 — 항혈관신생 단클론항체 (Anti-VEGF; Antineoplastic) |
| 골수억제 위험 | 낮음 (직접적 골수억제 없음; 병용 세포독성 화학요법의 종류에 따라 달라짐) |
| 구토 유발성 등급 | 최소 (단독 투여 시 구역·구토 발생 드묾) |
| 모니터링 항목 | 혈압 (고혈압), 소변 단백질 (단백뇨/신증후군), 상처 치유 지연, 혈전색전증 (DVT/PE), 위장관 천공·누공, CBC (병용 화학요법 시) |
| 취급 방호 | 생물학적 제제 표준 취급 절차 준수; 일반 세포독성 화학요법 수준의 방호 불필요 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails (낭종성 종양 한정) / Hold (나머지 9개 적응증)**

**사유:**
낭종성 종양(난소 낭선암종, 복막 점액종 등)에 대해서는 Phase 3 임상시험을 포함한 L1 수준의 근거가 확보되어 있으며, VEGF 억제 기전과 질환 병태생리 간 대응 관계가 명확합니다. 나머지 9개 예측 적응증은 L3–L5 수준으로, 특히 두경부 양성 종양의 경우 천공·누공·출혈 등 Bevacizumab 특이 독성의 위험이 기대 효익을 상회할 수 있어 추가 데이터 없이 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- 상세 MOA 데이터 보완 (DrugBank API 조회 — 현재 High severity Data Gap)
- 대만 TFDA 허가사항 상 경고·금기 정보 확보 (현재 Blocking Data Gap; 仿單 PDF 다운로드 및 파싱 필요)
- 낭종성 종양 세부 아형별 (난소암, 복막 점액종 등) 임상 개발 계획 및 적응증 구체화
- 경추 신경모세포종(L3, Research Question)에 대한 전향적 연구 또는 확장 증례 계열 데이터
- 두경부 양성 종양 적응증에 대한 VEGF 발현 정도 및 항혈관신생 요법 효익-위험 전임상 데이터
- Bevacizumab 특이 안전성 모니터링 프로토콜 수립 (고혈압, 단백뇨, 혈전색전증 기준)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

