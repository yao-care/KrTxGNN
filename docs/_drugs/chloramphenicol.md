---
layout: default
title: Chloramphenicol
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 9
---

# Chloramphenicol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Chloramphenicol: 전신 세균 감염 치료에서 결막염으로

## 한 문장 요약

Chloramphenicol은 광범위 항생제로, 문헌상 수막염·페스트·콜레라·장티푸스 등 전신 감염과 더불어 결막염에도 이미 사용되어 온 이력이 확인됩니다. TxGNN 모델은 **결막염(Conjunctivitis)**을 신규 예측 적응증으로 제시했으나, 등록된 임상시험은 없고 **19편의 문헌**(다수의 무작위 대조 비교연구 포함)이 이 연관성을 뒷받침합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 자료 없음 (한국 허가 이력 없음, 원 적응증 구조화 데이터 미확보) |
| 예측 신규 적응증 | 결막염 (Conjunctivitis) |
| TxGNN 예측 점수 | 99.66% |
| 근거 수준 | L3 (임상시험 등록 없음, 다수 RCT·Cochrane 체계적 문헌고찰 존재) |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전(MOA) 데이터는 확보되지 않았습니다. 다만 문헌(PMID 35369683)에 따르면 Chloramphenicol은 수막염, 페스트, 콜레라, 장티푸스 등 전신 세균 감염과 함께 결막염 치료에도 이미 사용되어 온 광범위 항생제로 기록되어 있으며, 이러한 기존 사용 이력이 결막염 예측의 기전적 타당성을 뒷받침합니다.

실제로 안과용 Chloramphenicol 점안액은 영국 등에서 세균성 결막염의 표준 치료제로 수십 년간 사용되어 왔고, 본 근거자료의 다수 비교임상연구(1983~2007년)가 이를 뒷받침합니다. 즉 이번 예측은 완전히 새로운 적응증 발굴이라기보다, 기존에 이미 확립된 용도가 지식그래프상에서 재확인된 사례로 해석하는 것이 타당합니다.

한편 문헌(PMID 8800624)은 국소(점안) Chloramphenicol 사용과 재생불량성빈혈 간의 연관성 논란을 다루고 있어, 결막염 적응증을 검토할 때 이 안전성 이슈를 반드시 함께 평가해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT (이중맹검, 다기관) | J Antimicrob Chemother | 230명 대상 다기관 이중맹검 시험, trimethoprim-polymyxin B 등과 비교 시 chloramphenicol 점안액 유효하며 심각한 이상반응 적음 |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | RCT (단일맹검) | Acta Ophthalmologica | 급성 화농성 결막염에서 fusidic acid(84%) vs chloramphenicol(81%) 임상 성공률 유사, chloramphenicol군에서 자극감 등 경미한 부작용 다소 많음(14% vs 5%) |
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | RCT (개방, 무작위) | Acta Ophthalmologica | 탄자니아 세균성 결막염에서 fusidic acid(93%)가 chloramphenicol(48%), framycetin(74%)보다 우수, chloramphenicol의 낮은 효과는 내성률(17%)과 연관 |
| [17947266](https://pubmed.ncbi.nlm.nih.gov/17947266/) | 2007 | RCT (동등성 시험) | Br J Ophthalmol | 멕시코 트라코마 유행지역 신생아안염 예방에서 2.5% povidone-iodine과 chloramphenicol 점안액의 효과 비교 |
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Cochrane 체계적 문헌고찰 | Cochrane Database Syst Rev | 신생아안염(ophthalmia neonatorum) 예방을 위한 항생제/소독제 중재 전반 검토 |
| [16378567](https://pubmed.ncbi.nlm.nih.gov/16378567/) | 2005 | Cochrane 체계적 문헌고찰 | Br J Gen Pract | 급성 세균성 결막염에 대한 국소 항생제(chloramphenicol 포함)의 위약 대비 효과 메타분석 갱신 |
| [8333258](https://pubmed.ncbi.nlm.nih.gov/8333258/) | 1993 | 비교임상연구 | Acta Ophthalmologica | 노르웨이 일반의 대상, fusidic acid vs chloramphenicol 세균학적 결과 및 치료반응 차이 없음 |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | 안전성 리뷰 | Drug Safety | 국소(점안) chloramphenicol과 재생불량성빈혈 간 연관성 논쟁을 다룸 (영국은 결막염에 흔히 사용, 미국은 거의 사용 안 함) |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | 비교연구 | Curr Ther Res Clin Exp | 세균성 안 감염 치료에서 moxifloxacin과 chloramphenicol 비교, chloramphenicol은 독성으로 인해 주로 국소제제로 사용됨을 언급 |
| [19680306](https://pubmed.ncbi.nlm.nih.gov/19680306/) | 2009 | 근거 리뷰 | N Z Med J | 급성 감염성 결막염 진단·치료 가이드라인, 국소 항생제 선택 및 치료 지연 전략 논의 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
허가사항 경고/금기/DDI 데이터가 전무하여 S1 안전성 초기평가 자체가 불가능한 Blocking 데이터 갭이 존재하며, 해당 약물은 한국 내 허가·시판 이력이 없습니다(허가증 0건). 결막염에 대한 문헌 근거는 다수의 RCT와 Cochrane 체계적 문헌고찰로 뒷받침되지만, 대부분 1980~2000년대 자료로 이는 새로운 적응증 발굴이라기보다 기존에 이미 알려진 용도의 재확인에 가깝고, 국소 사용에도 불구하고 재생불량성빈혈 연관성 논란(PMID 8800624)이 존재해 별도의 위해성 재평가가 필요합니다.

**진행하려면 필요한 것:**
- 허가사항(경고/금기/DDI) 원문 자료 확보 (Blocking 항목, DG001)
- 상세 작용기전(MOA) 자료 확보 (DG002)
- 재생불량성빈혈 등 전신 흡수 관련 위해성 자료 재검토
- 한국 내 허가·도입 전략 여부 검토 (현재 미시판 상태)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

