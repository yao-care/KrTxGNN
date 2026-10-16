---
layout: default
title: Nitrofurantoin
parent: 모델 예측만 (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nitrofurantoin: 예측 신규 적응증 류마티스 관절염 (Rheumatoid Arthritis) (근거 수준 L5). 기존 적응증: 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적 내용을 확인할 수 없음 (허가사항 참조)"
monitor_inn: "NITROFURANTOIN"
predicted_indications: ["rheumatoid arthritis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "sclerosing cholangitis", "methemoglobinemia, alpha type", "gout", "methemoglobinemia"]
---

# Nitrofurantoin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# Nitrofurantoin: 요로감염 치료제에서 류마티스 관절염으로 (예측)

## 한 문장 요약

Nitrofurantoin은 항균제로, 한국에서 단일제 캡슐로 허가되어 시판 중입니다. TxGNN 모델은 **류마티스 관절염(rheumatoid arthritis)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 지지하는 **임상시험은 0건**이며 수집된 **문헌 9편**은 모두 치료 효과가 아닌 이상반응(폐섬유화, 약물 상호작용 등)이나 간접적 연관을 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 텍스트가 링크 형태로만 제공되어 구체적 내용을 확인할 수 없음 (허가사항 참조) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보로는 nitrofurantoin은 항균제이며, 니트로푸란 대사체가 세균의 DNA와 리보솜 단백질을 손상시켜 작용합니다.

이 기전과 류마티스 관절염의 병태생리(자가면역성 관절 염증) 사이에는 설득력 있는 치료적 연관성이 확인되지 않습니다. 수집된 문헌도 치료 효과가 아니라 해악을 다룹니다. 약물 유발 폐섬유화, 메토트렉세이트와의 병용 시 비가역적 폐섬유화 사례, 항생제 사용과 RA 악화의 연관성 등입니다. 따라서 높은 TxGNN 점수는 임상 근거로 뒷받침되지 않으며, 지식 그래프상의 간접 연관(예: 폐섬유화)을 반영했을 가능성이 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Med J | 약물 유발 폐섬유화 개관. nitrofurantoin이 원인 약물로 언급되며 RA는 소인 질환으로 기술 |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | Rev Prat | 약물 유발 간질성 폐질환 개관. nitrofurantoin이 원인 항생제로 언급 |
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort | Sci Rep | 자기대조 환자-시리즈 분석으로 항생제 사용과 RA 악화의 연관성 조사 |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | RA 환자에서 메토트렉세이트와 nitrofurantoin 병용 후 비가역적 폐섬유화 발생 |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | 간질성 폐섬유화로 입원한 RA 환자 57명의 예후가 불량함 |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | 대상포진 유발 자가면역 간염 vs 약물 유발 간손상 감별 사례. nitrofurantoin이 감별 대상 약물 |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Ann Dermatol Venereol | 페닐부타존 유발 침샘염 사례. nitrofurantoin이 침샘염 유발 가능 약물로 언급 |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Rev Pneumol Clin | 금염 유발 폐렴과 CD4 폐포염 사례 |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Med Scand | 중년 여성 세균뇨 선별 및 단기 nitrofurantoin 치료 후 1년 추적 (RA 치료와 무관) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201801271 | 보령니트로푸란토인캡슐 | 경질캡슐 (상부 연갈색, 하부 흰색, 연한 노란색 분말 함유) | 허가사항 참조 (식약처 의약품안전나라 링크로만 제공) |

## 안전성 고려사항

- **금기 관련 지식 그래프 신호** (허가사항 문구가 아닌 TxGNN 지식 그래프의 약물-질환 금기 연결 기준): 당뇨병, 당뇨병성 케톤산증, 무뇨증, 신기능 장애, G6PD 결핍, 말초신경병증, 간질성 폐질환, 폐섬유화, 약물 유발 간손상, 간염, 폐쇄성 황달, 담도 질환, 비타민 B12 결핍, 시신경염, *Clostridium difficile* 대장염 등
- **약물 상호작용** (DDInter, 총 100건 중 일부): 
  - 중등도: metronidazole, balsalazide, picosulfuric acid, naltrexone, rosuvastatin, simvastatin
  - 경미: atropine, hyoscyamine, scopolamine, glycopyrronium, 마그네슘 제제 등
- **수집 문헌에서 확인된 이상반응 신호**: 폐섬유화·간질성 폐질환(특히 메토트렉세이트 병용 시), 약물 유발 간손상 및 자가면역 유사 간염, G6PD 결핍 환자의 용혈성 빈혈 및 메트헤모글로빈혈증

류마티스 관절염 환자는 메토트렉세이트를 흔히 사용하고 폐 질환 위험도 높아, 이 약물의 폐·간 독성 프로파일은 이 적응증에서 특히 우려됩니다. 허가사항의 경고·금기 정보는 이번 자료에서 확보되지 않았으므로 허가사항을 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험이 없고 문헌은 모두 이상반응 또는 간접 연관만 다루어 치료적 근거가 없습니다(L5). 기전상 타당성도 확인되지 않고, 폐섬유화·간독성 등 RA 환자에게 특히 부담이 되는 안전성 신호가 있습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증) 원문 확보 및 분석 (식약처 허가 PDF)
- 상세 작용 기전(MOA) 데이터 확보 (DrugBank)
- RA에 대한 항염증·면역조절 효과를 시사하는 전임상 또는 기전 연구
- 폐·간 독성 및 메토트렉세이트 병용 위험을 평가하는 안전성 분석

**참고: 다른 예측 적응증**
순위 2~10위(상염색체 우성 가족성 혈뇨-망막 세동맥 사행-구축 증후군, 뇌 소혈관질환 1형, 당뇨병성 신증, 경화성 담관염, 통풍, 메트헤모글로빈혈증 등)도 모두 L5~L4 수준이며 권장 결정은 Hold입니다. 특히 메트헤모글로빈혈증은 치료가 아니라 nitrofurantoin이 유발하는 이상반응으로 확인되어, 재창출 대상이 아닌 안전성 경고 신호로 해석해야 합니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

