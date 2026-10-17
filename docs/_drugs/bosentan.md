---
layout: default
title: Bosentan
parent: 모델 예측만 (L5)
nav_order: 153
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Bosentan: 예측 신규 적응증 류마티스 관절염 (Rheumatoid Arthritis) (근거 수준 L5). 기존 적응증: 허가 적응증 본문이 확인되지 않음 (허가증에 PDF 링크만 있음). 문헌상 폐동맥 고혈압(PAH)에 사용되는 약물임"
monitor_inn: "bosentan"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "pseudoxanthoma elasticum, forme fruste", "kyphoscoliotic heart disease", "elastoma", "gout", "hypertrichosis (disease)"]
---

# Bosentan
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

# Bosentan: 폐동맥 고혈압에서 류마티스 관절염으로

## 한 문장 요약

Bosentan은 이중 엔도텔린 수용체 길항제로, 한국에서 허가·시판 중인 약물입니다.
TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측하지만, 현재 등록된 **임상시험은 0건**이며 **문헌 15편**은 대부분 간접 근거(결합조직질환 연관 폐동맥 고혈압 리뷰, 동물 실험)입니다.
참고로 예측 순위 3위인 **limited systemic sclerosis(국한형 전신 경화증)**는 문헌 근거가 더 풍부하여 별도로 정리했습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 확인되지 않음 (허가증에 PDF 링크만 있음). 문헌상 폐동맥 고혈압(PAH)에 사용되는 약물임 |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.80% |
| 근거 수준 | L4 (전임상 연구 중심) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 4건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 수집되지 않았습니다. 다만 문헌에 따르면 bosentan은 ETA/ETB 수용체를 모두 차단하는 이중 엔도텔린 수용체 길항제입니다.

엔도텔린-1은 활막 염증, 혈관병증, 사이토카인(TNF-α, LTB4) 분비에 관여합니다. 마우스 콜라겐 유발 관절염 모델에서 bosentan이 TNF-α와 연관된 기전을 통해 관절염을 완화했다는 전임상 결과가 있어 기전상 가능성은 있습니다.

그러나 사람 대상 류마티스 관절염 임상시험은 확인되지 않았습니다. 임상 문헌의 상당수는 결합조직질환 연관 폐동맥 고혈압에 관한 것으로, 관절 질환 자체에 대한 근거가 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | 전임상(동물) | Inflamm Res | Bosentan이 마우스 콜라겐 유발 관절염을 완화, TNF-α와 엔도텔린 시스템 유전자 연관 |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | 전임상(동물) | J Leukoc Biol | 자이모산 유발 관절염에서 엔도텔린이 호중구 축적과 부종에 관여 |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheum Dis Clin North Am | 결합조직질환 연관 PAH의 진단과 치료 |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | 결합조직질환 연관 PAH(류마티스 관절염은 드문 원인) |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | 루푸스 및 쇼그렌 증후군 연관 혈관병증과 PAH |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case report | Kardiol Pol | 아이젠멩거 증후군 환아가 bosentan 치료 중 소아 류마티스 관절염을 추가 진단받은 증례 |

위 문헌 중 bosentan이 류마티스 관절염 환자에서 효능을 보였다고 직접 입증한 연구는 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202003657 | 카나보센정62.5밀리그램 | 연한 살구색의 원형 필름코팅정 | 허가사항 문서 참조 |
| 202004778 | 카나보센정125밀리그램 | 연한 살구색의 타원형 필름코팅정 | 허가사항 문서 참조 |
| 200706894 | 트라클리어정62.5밀리그램 | 연한 살구색의 원형 필름코팅정 | 허가사항 문서 참조 |
| 201800684 | 제이더블유보센탄정62.5밀리그램 (수출용) | 흰색 원형 정제 | 허가사항 문서 참조 |

## 안전성 고려사항

- **지식그래프 기반 금기 관련 질환** (허가 문구가 아닌 TxGNN 지식그래프 정보): 간부전, 간질환, 담낭질환, 혈소판감소증, 울혈성 심부전, 빈혈, 고빌리루빈혈증, 길버트 증후군, 약물유발 간손상, 폐부종, 폐정맥폐쇄질환
- **약물 상호작용**: 총 244건이 확인되었으며, 이 중 일부는 중등도(Moderate) 수준입니다. 예: hydrocortisone, dexamethasone, betamethasone, triamcinolone, pioglitazone, aprepitant, metronidazole, clarithromycin, cimetidine, cisapride

허가사항의 경고·금기 문구는 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
류마티스 관절염에 대해서는 동물 실험 수준의 근거만 있고 사람 대상 임상시험이 없어 근거 수준이 L4에 그칩니다. 또한 간독성 등 안전성 우려가 있는 약물이므로 현 단계에서 진행하기는 어렵습니다.

**진행하려면 필요한 것:**
- 류마티스 관절염 환자 대상 탐색적 임상시험 설계 또는 기존 시험 확인
- 허가사항(경고·금기·적응증) 원문 확보 및 분석
- 상세한 작용 기전(MOA) 데이터 보완
- 간기능 모니터링을 포함한 안전성 계획 수립

## 참고: 다른 예측 적응증

| 순위 | 예측 적응증 | TxGNN 점수 | 근거 수준 | 비고 |
|-----|-----------|-----------|----------|------|
| 3 | 국한형 전신 경화증 (Limited Systemic Sclerosis) | 99.65% | L3 | 수부 궤양 체계적 문헌고찰·메타분석(2023, PMID [36974107](https://pubmed.ncbi.nlm.nih.gov/36974107/)), 시험관 내 EndoMT 억제 연구, 2024년 포르투갈 권고안 등. 이 데이터에는 등록 임상시험이 없어 근거 등급은 보수적으로 산정되었으며, 기반 RCT가 확인되면 상향될 수 있음. 권장: 연구 과제(Research Question) |
| 8 | 통풍 | 99.21% | L5 | 효능 근거 없음 (안전성 신호 분석 1건뿐) |
| 2, 4, 5, 6, 7, 9 | 갈래손가락-합지증 증후군, 결손성 소안구증-근위부 단축 이형성 증후군, 탄성섬유성 가성황색종(경미형), 척추후만측만성 심장질환, 탄력종, 다모증 | 99.04~99.74% | L5 | 모델 예측만 있고 임상시험·문헌 없음, 기전적 연결 불명확. 권장: Hold |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

