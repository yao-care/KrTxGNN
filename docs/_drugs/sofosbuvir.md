---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 642
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sofosbuvir: C형 간염 감염에서 B형 간염 바이러스 감염으로

## 한 문장 요약

Sofosbuvir는 C형 간염바이러스(HCV)의 NS5B RNA 의존성 RNA 중합효소(RdRp)를 억제하는 항바이러스제로, 원래 만성 C형 간염 치료제로 개발되었습니다. TxGNN 모델은 **B형 간염바이러스(HBV) 감염**에도 효과가 있을 수 있다고 예측했으며(예측 점수 99.77%), HBV 단독감염 환자를 직접 평가한 소규모 Phase 2 파일럿 연구 1건과 다수의 HCV/HBV 공동감염 관련 문헌이 존재하지만, HBV에 대한 직접적이고 강력한 근거는 아직 부족합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | C형 간염(HCV) 감염 (근거팩 내 기전 분석 기준) |
| 예측 신규 적응증 | B형 간염 바이러스 감염 (Hepatitis B Virus Infection) |
| TxGNN 예측 점수 | 99.77% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 (국내 허가 없음) |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Sofosbuvir는 HCV의 NS5B RNA 의존성 RNA 중합효소(RdRp)를 억제하여 바이러스 복제를 차단하는 뉴클레오티드 유사체 항바이러스제입니다(공식 DrugBank MOA 필드는 데이터 공백이나, 근거팩 내 기전 분석에서 이 정보가 확인됩니다).

문제는 HBV가 HCV와 달리 **DNA 바이러스**이며, 복제 과정에서 역전사효소(reverse transcriptase)를 사용한다는 점입니다. Sofosbuvir의 표적 효소인 RdRp는 HBV 복제 경로에 존재하지 않아, 기전상 직접적인 연결고리는 약합니다.

그럼에도 불구하고 HCV/HBV 공동감염 환자에서 sofosbuvir 기반 HCV 치료 이후 HBsAg(B형 간염 표면항원) 감소가 관찰된 사례들이 보고되었고, 이를 근거로 HBV 단독감염 환자를 대상으로 한 소규모 Phase 2 개방표지 파일럿 연구(NCT03312023)가 진행되어 HBsAg 및 HBV DNA 감소를 1차/2차 평가지표로 삼았습니다. 다만 이는 명확한 기전적 설명 없이 경험적 관찰에 기반한 가설 검증 단계이며, 대다수 관련 문헌은 HCV 치료 도중 발생하는 **HBV 재활성화**에 대한 안전성 보고에 가깝습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | 완료 | 21 | HBV 단독감염 환자에서 Ledipasvir/Sofosbuvir 12주 투여 후 HBsAg 혈청전환 등 기능적 치유 가능성 평가 — HBV를 직접 표적으로 한 유일한 임상시험 |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | 완료 | 111 | 대만 내 HCV/HBV 공동감염 환자에서 LDV/SOF 병용요법 — 치료 표적은 HCV이며 HBV와 직접 관련 없음(관련성 등급 C) |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 완료 | 23 | HCV/HBV 공동감염 환자의 HCV 치료 중 HBV 재활성화 발생률·예후인자 조사 — 치료 표적은 HCV(관련성 등급 C) |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | 불명 | 21 | HCV 연관 무통성 B세포 림프종에서 HARVONI(LDV/SOF) 효과 평가 — 근거팩 내 관련성 등급 B로 표시되었으나 제목상 HBV 환자 대상 연구는 아님(데이터 정합성 주의 필요) |

나머지 대다수 임상시험(총 44건 중 약 40건)은 HCV 치료를 표적으로 한 연구로, sofosbuvir와의 단순 공출현(co-occurrence)으로 목록에 포함된 것이며 HBV 재창출 가설과 직접 관련이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label (Tier 1) | Journal of Medical Virology | HBV 단독감염 환자 대상 LDV/SOF 12주 파일럿 연구 프로토콜 — HBsAg·HBV DNA 감소를 평가지표로 설정 |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report (Tier 2) | Medicine | Sofosbuvir+Ribavirin으로 HCV 치료 성공 후 HBV 재활성화 발생 사례 |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | 코호트 추적 | Clinical Infectious Diseases | 대만 내 HCV/HBV 공동감염 환자의 LDV/SOF 치료 후 108주 추적 — HBV 재활성화 평가 |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | 코호트 | Journal of Clinical Gastroenterology | LDV/SOF로 HCV 치료받은 환자에서 HBV 재활성화 위험도 조사 |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | 관찰 연구 | Infection and Drug Resistance | DAA 치료 후 HBV 재활성화 환자의 관리 전략(HBeAg 혈청전환 여부에 따른 접근) |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | 전향적 관찰 | Journal of Viral Hepatitis | 암 환자에서 HCV 치료용 DAA 투여 시 HBV 재활성화 위험 평가 |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | 관찰 연구 | Trans R Soc Trop Med Hyg | 이집트 내 HCV 및 HCV/HBV 공동감염 환자에서 Sofosbuvir/Daclatasvir 치료 결과 |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | 모델링 연구 (Tier 3) | Lancet Gastroenterol Hepatol | 전 세계 HBV 유병률 및 치료 격차 추정 — 약물 특이적 근거 아님, 배경 정보 |
| [39914746](https://pubmed.ncbi.nlm.nih.gov/39914746/) | 2025 | 정책 분석 | Journal of Hepatology | HCV 치료 확산 경험이 향후 HBV/HDV 치료제 보급에 주는 시사점 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | 리뷰 (Tier 3) | Minerva Gastroenterol Dietol | HBV·HCV 항바이러스제가 신기능에 미치는 영향 개괄 |

## 한국 시판 정보

현재 국내에는 sofosbuvir 허가 제품이 없습니다(시판 현황: 미시판, 허가증 수: 0건). 국내 허가사항 정보가 없어 적응증·제형 비교가 불가능합니다.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> ⚠️ 본 근거팩에서는 허가사항 경고·금기·약물상호작용 정보가 모두 확인되지 않았습니다(Blocking 등급 데이터 공백, DG001). 이는 안전성 초기평가(S1) 진입을 가로막는 핵심 결손이며, HBV 재창출 검토 이전에 반드시 보완되어야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- HBV는 DNA 바이러스로 역전사효소에 의존하여 복제하며, sofosbuvir의 표적인 RdRp는 HBV 복제 경로에 존재하지 않아 기전상 직접적 연결고리가 약합니다.
- HBV 단독감염을 직접 평가한 임상근거는 소규모(n=21) 비대조 Phase 2 파일럿 연구 1건뿐이며, 나머지 근거는 대부분 HCV/HBV 공동감염 환자에서 HCV 치료 도중 관찰된 HBsAg 감소 또는 HBV 재활성화에 관한 부수적 관찰입니다.
- 국내 허가 정보가 전무하고(미시판) 허가사항 경고·금기 데이터가 Blocking 등급으로 결손되어 있어, 안전성 초기평가(S1) 자체가 불가능한 상태입니다.

**진행하려면 필요한 것:**
- TFDA(원 소스) 허가사항 원문 확보 및 경고·금기·상호작용 정보 파싱 (Blocking, DG001)
- DrugBank 등에서 공식 작용기전(MOA) 데이터 확보 (High, DG002)
- NCT03312023 파일럿 연구의 정식 결과 논문 발표 확인 및 반영
- HBV 단독감염 대상 무작위대조시험(RCT) 설계 필요성에 대한 전문가 검토
- NCT03261349의 관련성 등급(B) 재검토 — 근거팩 내 근거(reasoning)와 시험 제목(HCV 연관 림프종) 간 불일치 확인 필요
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

