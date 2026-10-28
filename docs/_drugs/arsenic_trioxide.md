---
layout: default
title: Arsenic Trioxide
parent: 모델 예측만 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Arsenic Trioxide: 예측 신규 적응증 분류되지 않은 골수이형성증후군 (Unclassified Myelodysplastic Syndrome) (근거 수준 L5). 기존 적응증: 허가증 원문 링크만 제공되어 확인 불가"
monitor_inn: "ARSENIC TRIOXIDE"
predicted_indications: ["unclassified myelodysplastic syndrome", "refractory cytopenia of childhood", "severe congenital hypochromic anemia with ringed sideroblasts", "aregenerative anemia", "partial deletion of the long arm of chromosome 5", "myelodysplastic syndrome", "Ewing sarcoma", "dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
---

# Arsenic Trioxide
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 약사 평가 보고서

</div>

## Arsenic Trioxide: 급성 전골수성백혈병에서 미분류 골수이형성증후군으로
{: .text-alpha }

## 한 문장 요약

Arsenic trioxide(삼산화비소)는 국내에서 주사제로 허가된 항종양제입니다. TxGNN 모델은 **분류되지 않은 골수이형성증후군(unclassified myelodysplastic syndrome)**을 최상위 신규 적응증으로 예측했지만, 이 질환 자체에 대한 임상시험과 문헌은 없습니다. 같은 골수이형성증후군(MDS) 계열에서 가장 근거가 많은 **골수이형성증후군(Myelodysplastic Syndrome)**에는 **19건의 임상시험**과 **20편의 문헌**이 있어, 이를 중심으로 평가했습니다.

> 참고: 국내 허가 적응증은 허가증 링크 형태로만 제공되어 구체적인 문구를 확인할 수 없었습니다. 제목의 "급성 전골수성백혈병"은 이 약의 일반적으로 알려진 적응증이며, 이번에 정리된 데이터로 확인된 내용은 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증 원문 링크만 제공되어 확인 불가 |
| 예측 신규 적응증 | 분류되지 않은 골수이형성증후군 (Unclassified Myelodysplastic Syndrome) |
| TxGNN 예측 점수 | 0.9993 (전체 순위 1,863위) |
| 근거 수준 | L5 (분류되지 않은 MDS). 참고: 골수이형성증후군 전체는 L2 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 4건 |
| 권장 결정 | Hold (분류되지 않은 MDS). 참고: 골수이형성증후군 전체는 Proceed with Guardrails |

### 상위 10개 예측 후보 요약

| 순위 | 예측 질환 | 점수 | 근거 수준 | 권장 |
|-----|---------|------|---------|------|
| 1 | 분류되지 않은 골수이형성증후군 | 0.9993 | L5 | Hold |
| 2 | 소아 불응성 혈구감소증 | 0.9993 | L5 | Hold |
| 3 | 중증 선천성 저색소성 빈혈(고리철적아구 동반) | 0.9993 | L5 | Hold |
| 4 | 재생불량성 빈혈(Aregenerative anemia) | 0.9992 | L5 | Research Question |
| 5 | 5번 염색체 장완 부분 결실 | 0.9992 | L5 | Hold |
| 6 | 골수이형성증후군 | 0.9991 | L2 | Proceed with Guardrails |
| 7 | 유잉 육종 | 0.9989 | L3 | Research Question |
| 8 | 융기성 피부섬유육종 | 0.9977 | L5 | Hold |
| 9 | 지방육종 | 0.9975 | L5 | Hold |
| 10 | 난소 점액성 지방육종 | 0.9970 | L5 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 다만 수집된 문헌에 따르면 삼산화비소는 세포자멸사(apoptosis) 유도, 세포 분화 유도, 항증식 및 항혈관신생 작용을 나타내며, 급성 전골수성백혈병(APL)에서 PML-RARA 융합 단백질 분해를 통해 효과를 보이는 약물로 알려져 있습니다.

MDS 세포에서는 NF-κB/FLIP 조절, BCL2 계열 유전자 조절, 산화 스트레스를 통한 세포자멸사가 보고되었습니다. 또한 TP53 재활성화 가능성이 제기되어 현재 임상시험이 계획되어 있습니다. 같은 골수성 혈액암 계열이라는 점에서 기전상 MDS에 적용될 수 있는 근거가 있습니다.

다만 1순위로 예측된 "분류되지 않은 MDS"는 이 아형에 특화된 자료가 없어, MDS 전체 범주에서 추정한 간접적 타당성에 그칩니다. 높은 점수는 네트워크 기반 예측일 뿐입니다.

## 임상시험 근거

아래는 가장 근거가 풍부한 **골수이형성증후군(순위 6)**의 임상시험 중 관련성이 높은 10건입니다. 1순위 질환(분류되지 않은 MDS)에는 등록된 임상시험이 없습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00621023](https://clinicaltrials.gov/study/NCT00621023) | Phase 2 | 완료 | 7 | MDS에서 decitabine + 삼산화비소 + 아스코르브산 병용의 안전성 평가 (소규모 파일럿) |
| [NCT00251511](https://clinicaltrials.gov/study/NCT00251511) | Phase 2 | 조기 종료 | 60 | 저위험~고위험 MDS에서 삼산화비소 + thalidomide 병용 |
| [NCT00671697](https://clinicaltrials.gov/study/NCT00671697) | Phase 1 | 완료 | 13 | MDS/AML에서 decitabine + 삼산화비소 + 아스코르브산의 안전성 |
| [NCT00093366](https://clinicaltrials.gov/study/NCT00093366) | Phase 1/2 | 완료 | 32 | 진행성 MDS에서 삼산화비소 + etanercept 병용 |
| [NCT00195104](https://clinicaltrials.gov/study/NCT00195104) | Phase 1/2 | 완료 | 87 | 고위험 MDS 및 예후 불량 AML에서 삼산화비소 + 저용량 cytarabine |
| [NCT02190695](https://clinicaltrials.gov/study/NCT02190695) | Phase 2 | 완료 | 92 | 재발·불응성·고령 AML/MDS에서 decitabine 단독 vs 병용(carboplatin 또는 삼산화비소) 무작위 비교 |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | 완료 | 2000 | 고령 AML 및 고위험 MDS 치료 개발 프로그램 (삼산화비소는 구성 요소 중 하나) |
| [NCT00104806](https://clinicaltrials.gov/study/NCT00104806) | Phase 2 | 조기 종료 | 5 | 삼산화비소 + cholecalciferol, 자료 극히 제한적 |
| [NCT06670222](https://clinicaltrials.gov/study/NCT06670222) | Phase 1 | 모집 중 | 24 | ESA 및 luspatercept 실패 저위험 MDS에서 경구 삼산화비소 |
| [NCT06778187](https://clinicaltrials.gov/study/NCT06778187) | Phase 2 | 모집 중 | 30 | TP53 변이 골수성 종양에서 경구 삼산화비소 기반 저강도 치료 |

이 외에도 MDS 대상 삼산화비소 단독 Phase 2 시험(NCT00020969, NCT00225992)이 조기 종료되었고, MDS 대상 Phase 3 시험(NCT03377725)은 시작 전에 철회되었습니다. 삼산화비소만을 MDS에서 검증한 Phase 3 시험은 없습니다.

## 문헌 근거

아래는 **골수이형성증후군(순위 6)**의 문헌 중 우선순위가 높은 10편입니다. 1순위 질환에는 연결된 문헌이 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37908176](https://pubmed.ncbi.nlm.nih.gov/37908176/) | 2023 | 체계적 문헌고찰/네트워크 메타분석 | Hematology | MDS에서 삼산화비소 포함 요법의 효능과 이상반응 평가. 소규모 표본과 상충하는 결과로 널리 권고되지 않음 |
| [20956016](https://pubmed.ncbi.nlm.nih.gov/20956016/) | 2011 | Phase 1/2 임상 | Leuk Res | 중간-2/고위험 MDS 49명에서 삼산화비소 + 저용량 cytarabine, 완전관해 17% |
| [17920679](https://pubmed.ncbi.nlm.nih.gov/17920679/) | 2008 | 임상 연구 | Leuk Res | 고위험 MDS에서 삼산화비소 + thalidomide + 레티노산 병용 |
| [18282365](https://pubmed.ncbi.nlm.nih.gov/18282365/) | 2007 | Review | Clin Lymphoma Myeloma | 백혈병 및 MDS에서 삼산화비소의 새로운 데이터 |
| [20425329](https://pubmed.ncbi.nlm.nih.gov/20425329/) | 2006 | Review | Curr Hematol Malig Rep | 항세포자멸사·항증식·항혈관신생 기전으로 MDS에서 활성 |
| [15610661](https://pubmed.ncbi.nlm.nih.gov/15610661/) | 2005 | Review | Curr Hematol Rep | MDS에서 삼산화비소의 단독 및 병용 치료 개관 |
| [38816179](https://pubmed.ncbi.nlm.nih.gov/38816179/) | 2024 | 전임상 | Immunopharmacol Immunotoxicol | MDS 마우스 모델에서 realgar와 삼산화비소의 면역학적 변화 비교 |
| [41398777](https://pubmed.ncbi.nlm.nih.gov/41398777/) | 2025 | 전임상 | Medicine | Triptolide + 삼산화비소가 NF-κB 억제를 통해 MDS 세포자멸사 유도 |
| [27665715](https://pubmed.ncbi.nlm.nih.gov/27665715/) | 2016 | 전임상 | Mol Med Rep | SKM-1 MDS 세포주에서 삼산화비소 + triptolide 상승적 세포자멸사 |
| [12886236](https://pubmed.ncbi.nlm.nih.gov/12886236/) | 2003 | Review | Leukemia | MDS에서 삼산화비소의 기회와 생물학적 표적 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202203561 | 아사딘주(삼산화비소) | 주사제 (바이알) | 허가증 원문 참조 |
| 201507055 | 아시트리주(삼산화비소) | 주사제 (바이알) | 허가증 원문 참조 |
| 202302004 | 트리세녹스주2mg/mL(삼산화비소)(바이알) | 주사제 (바이알) | 허가증 원문 참조 |
| 201004242 | 트리세녹스주(삼산화비소) | 주사제 (앰플) | 허가증 원문 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 항종양 비소 화합물 (세포자멸사 및 분화 유도 작용) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 심전도(QT 간격), 전해질(칼륨·마그네슘), 간·신기능, 분화증후군 감시 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에서 확인되지 않았습니다. 아래는 지식그래프와 약물상호작용 조회에서 확인된 내용입니다.

- **지식그래프 기반 금기 관련 질환** (허가 문구가 아님): 긴QT증후군(가족성 포함), 심실빈맥(torsades de pointes), 신장 질환, 간 질환, 담낭 질환, 칼륨 결핍, 방실차단, 요관농증
- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Hydrocortisone, Amphotericin B(일반·지질복합체·콜레스테릴황산염·리포솜 제형), Cisapride, Clarithromycin, Dolasetron, Granisetron, Levofloxacin (QT 연장 및 전해질 이상 위험과 관련된 약물 다수)
  - **Moderate**: Famotidine, Loperamide, Bisacodyl, Castor oil, Glycerin, Lactitol, Lactulose, Magnesium citrate, Magnesium hydroxide (설사·전해질 이상 유발 가능 약물 포함)
  - **Minor**: Metronidazole
- **MDS 대상 시 가드레일**: QT 모니터링 및 전해질 교정, 분화증후군 감시, 간·신기능 모니터링이 필요합니다. 소아에서는 QT 연장과 분화증후군 우려가 더 크다고 평가되었습니다.

## 결론 및 다음 단계

**결정: Hold** (1순위 "분류되지 않은 MDS")
참고: 골수이형성증후군 전체는 **Proceed with Guardrails**

**사유:**
1순위 질환은 임상시험과 문헌이 전혀 없어 모델 예측에 불과합니다(L5). 반면 상위 MDS 범주에는 다수의 Phase 1/2 시험과 2023년 체계적 문헌고찰이 있어 활성 가능성은 지지됩니다. 그러나 반응률이 낮고 다수 시험이 조기 종료되었으며, MDS 대상 Phase 3 시험은 없습니다.

**진행하려면 필요한 것:**
- 분류되지 않은 MDS 환자군에 대한 직접 근거 확보, 또는 MDS 일반 범주에서 하위 아형으로 외삽 가능한지에 대한 임상적 판단
- 허가사항 원문(경고, 금기, 적응증, 골수억제 및 구토 유발성 정보) 확보
- 작용 기전(MOA) 데이터 보완
- QT 간격, 전해질, 분화증후군, 간·신기능 모니터링 계획 수립
- 진행 중인 시험(NCT06670222, NCT06778187, NCT07737769) 결과 추적
- 재생불량성 빈혈과 유잉 육종은 별도의 연구 질문으로 후속 검토. 다만 재생불량성 빈혈 소규모 연구에서 반응이 일관되지 않았고(PMID 29075064는 전원 무반응으로 조기 종료, PMID 23044093은 5명 전원 반응), 유잉 육종은 전임상 근거가 중심입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

