---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 6
---

# Etanercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Etanercept: 류마토이드 관절염에서 류마토이드 혈관염으로

## 한 문장 요약

Etanercept는 TNF-α 수용체 융합 단백질(Enbrel®)로, 국제적으로 류마토이드 관절염·강직성 척추염·건선 관절염 등 자가면역질환 치료에 사용되고 있으나 현재 국내(한국) 허가 기록은 없습니다.
TxGNN 모델은 **류마토이드 혈관염(Rheumatoid Vasculitis)**에 효과가 있을 수 있다고 예측하며,
현재 **6건의 임상시험**과 **20편의 문헌**이 이 방향과 관련된 근거를 제공합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 데이터 없음 (국제적으로는 류마토이드 관절염 등 자가면역질환) |
| 예측 신규 적응증 | 류마토이드 혈관염 (Rheumatoid Vasculitis) |
| TxGNN 예측 점수 | 99.71% |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

Etanercept는 두 개의 p75 TNF 수용체(TNFR2)와 IgG1 Fc 영역으로 구성된 융합 단백질로, 가용성 및 막결합 TNF-α 모두에 결합하여 수용체 활성화를 차단합니다. TNF-α는 혈관 내피 염증 반응, 접착 분자(E-selectin, ICAM-1) 발현, 호중구 활성화에 핵심 역할을 담당하므로, TNF-α 차단이 이론적으로 류마토이드 혈관염(RV)에서의 혈관 내피 손상을 억제할 수 있다는 가설이 성립합니다.

그러나 이 예측에는 중요한 역설이 존재합니다. 문헌에는 etanercept 투여 중 오히려 피부 혈관염 및 ANCA 관련 혈관염이 역설적으로 유발된 사례가 다수 보고되어 있습니다. 이 역설성 혈관염(paradoxical vasculitis)의 기전으로는 면역 복합체 침착, B세포 비정상 활성화, 항핵항체(ANA) 및 항이중나선 DNA 항체 유도 등이 제시되고 있습니다.

특히 ANCA 관련 혈관염(Wegener 육아종증)에서 etanercept를 직접 검증한 WGET 임상시험(NCT00001901, Phase 2, N=60, 완료)은 무효성을 확인하고 감염 위험 증가를 보고한 음성 결과 연구입니다. Wegener's와 류마토이드 혈관염은 병리 기전에 차이가 있으나, 이 결과는 전신성 혈관염에서 TNF 억제제의 효능에 근본적인 의문을 제기합니다. 이처럼 치료 효과와 유발 위험이 공존하는 이중적 구조로 인해, 류마토이드 혈관염에 대한 etanercept의 기전적 타당성은 복잡하고 논쟁적입니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 2 | 완료 | 60 | Wegener 육아종증(혈관염의 일종)에서 etanercept 효능 평가; WGET 시험 결과 무효성 확인 및 감염 위험 증가 가능성 보고 — 혈관염에 대한 TNF 억제제의 음성 결과 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 불명 | 750,000 | 생물학제제·면역억제제 치료 환자에서 타 자가면역질환(IMID) 발생 위험 대규모 평가; etanercept-혈관염 사건 간 연관성 안전성 데이터 포함 가능 |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | 완료 | 808 | 중국 RA 환자에서 생물학적 DMARD 치료 패턴 및 인구통계학적 특성 관찰; 혈관염 특이 분석 없음 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | 완료 | 184 | 비생물학적 DMARD 또는 단일 생물학제제에 불충분한 반응을 보인 RA 환자에서 tocilizumab 6개월 관찰; 혈관염 특이 분석 없음 |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | 완료 | 1,754 | 중등도 RA에서 etanercept 신규 투여 코호트 대 비생물학적 DMARD 코호트의 질병 특성 및 예후 비교 관찰 연구 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 모집 예정 | 80 | 류마티스 환자의 견관절 치환술 전후 면역억제제 관리(중단 기간 비교); 혈관염 치료와 직접 연관 없음 |

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | 류마토이드 혈관염에서 생물학적 약제 치료에 관한 체계적 문헌고찰(PRISMA); 생물학제제의 RV 치료 적용 현황 및 근거 수준 종합 |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology Dialysis Transplantation | ANCA 관련 혈관염·사구체신염에서 TNF-α 차단의 역할 검토; RA에서의 효능과 비교하여 혈관염 치료 가능성 분석 |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Pharmacovigilance/Cohort | RMD Open | BSRBR-RA 등록 연구; TNFi 치료 RA 환자 대 비생물학적 DMARD 환자에서 루푸스 유사 및 혈관염 유사 사건 발생 위험 비교 |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case Series/Mechanistic | Scandinavian Journal of Immunology | Etanercept·infliximab 관련 피부 혈관염의 면역학적 기전 분석; TNF 차단제 유발 자가면역 기전 규명 |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case Report | Journal of Rheumatology | Etanercept 치료 중 증식성 루푸스 신염 및 백혈구파쇄성 혈관염 발생; TNFi의 ANA/dsDNA 항체 유도 및 혈관염 유발 기전 논의 |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Review | Journal of Rheumatology | TNF-α 차단과 혈관염 위험에 관한 검토; TNFi 투여 중 역설적 혈관염 발생 기전 및 임상 의의 논의 |
| [15624748](https://pubmed.ncbi.nlm.nih.gov/15624748/) | 2004 | Review | Journal of Drugs in Dermatology | Etanercept의 의학적 적용 범위 및 부작용 전반 검토; 피부 루푸스·피부 혈관염 등 피부과적 이상반응 포함 |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case Report | Case Reports in Medicine | Anti-TNF 치료 중인 RA 환자에서 대혈관 혈관염 발생 보고; 생물학제제 유발 자가면역 증가 경향 논의 |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case Report | Arthritis and Rheumatism | Etanercept 치료 RA 환자에서 류마토이드 결절 가속화 및 혈관염 동반 발생 사례 |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case Report | Rheumatology (Oxford) | Etanercept·infliximab 관련 피부 혈관염 복수 사례 보고; TNFi 계열 공통 이상반응으로 기술 |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
류마토이드 혈관염에 대해 etanercept의 직접적 효능을 입증하는 전향적 임상시험이 존재하지 않으며, 유사 전신성 혈관염(Wegener's)에서 음성 결과가 확인되었습니다. 더 나아가 etanercept가 오히려 혈관염을 역설적으로 유발할 수 있다는 약물감시 및 증례 보고가 다수 축적되어 있어, 현재 L3 수준의 근거로는 적극적 개발 진행이 어렵습니다.

**진행하려면 필요한 것:**
- 류마토이드 혈관염 특이적 전향적 임상 연구 (현재 전무)
- 역설성 혈관염(paradoxical vasculitis) 발생 위험 계층화 연구 — 어떤 환자에서 치료 효과 대 유발 위험이 우세한지 규명
- 작용 기전(MOA) 데이터 보완 (현재 Data Gap; DrugBank API 조회 권장)
- 국내 허가 정보 및 안전성 정보(MFDS 허가사항) 확보 (현재 미시판)
- Rituximab 등 B세포 표적 치료제와의 류마토이드 혈관염 치료 효능 비교 연구 검토
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

