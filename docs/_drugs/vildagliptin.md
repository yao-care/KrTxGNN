---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: 제2형 당뇨병에서 제1형 당뇨병(베타세포 보존)으로

## 한 문장 요약

Vildagliptin(빌다글립틴)은 DPP-4 억제제로, 문헌 근거상 원래 **제2형 당뇨병** 치료에 사용됩니다(한국 허가 자료 없음, 현재 미상매). TxGNN은 이 약물에 대해 총 10개 적응증을 예측했지만, 그중 8개(순위 1~8)는 기전적 연관성이 전혀 없고 실제 임상시험·문헌 근거가 하나도 없는 저신뢰 예측(L5, Hold)입니다. 유일하게 실질적 근거를 갖춘 예측은 **제1형 당뇨병(Type 1 Diabetes Mellitus)**으로, 이중맹검 RCT 1건을 포함한 다수 문헌이 베타세포 기능 보존 가설을 뒷받침합니다(L3).

> ⚠️ **투명성 안내**: TxGNN 점수 자체는 순위 1(강직인간증후군)이 가장 높지만, 해당 예측은 근거 패키지 내 기전 분석에서 "無合理機轉... 純屬圖譜嵌入相似度預測"(합리적 기전 없음, 순수 그래프 임베딩 유사도 예측)이라고 명시되어 있습니다. 따라서 이 보고서는 임상적 의미가 있는 근거를 실제로 보유한 후보(제1형 당뇨병)를 중심으로 작성합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 제2형 당뇨병 (문헌 근거 기반; 한국 허가 자료 없음) |
| 예측 신규 적응증 | 제1형 당뇨병 (Type 1 Diabetes Mellitus) |
| TxGNN 예측 점수 | 99.37% (전체 랭킹 10,056위) |
| 근거 수준 | L3 |
| 한국 시판 현황 | ✗ 미상매 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## TxGNN 전체 예측 목록 (참고)

| 순위 | 적응증 | 점수 | 근거 수준 | 권장 |
|------|--------|------|-----------|------|
| 1 | 강직인간증후군 (Classic Stiff Person Syndrome) | 99.88% | L5 | Hold |
| 2 | 국소 강직사지증후군 | 99.88% | L5 | Hold |
| 3 | 티아민반응성 대사이상증후군 | 99.87% | L5 | Hold |
| 4 | Opsismodysplasia | 99.86% | L5 | Hold |
| 5 | 약물유발 국소지방위축증 | 99.79% | L5 | Hold |
| 6 | 원심성 지방위축증 | 99.78% | L5 | Hold |
| 7 | 압박유발 국소지방위축증 | 99.78% | L5 | Hold |
| 8 | 특발성 국소지방위축증 | 99.76% | L5 | Hold |
| 9 | 췌장무형성증 (Pancreatic Agenesis) | 99.75% | L4 | Hold (기전 모순) |
| **10** | **제1형 당뇨병** | **99.37%** | **L3** | **Research Question** |

순위 1~8은 근거 패키지 자체가 "기전 관련성 없음"을 명시하고 있어 검토 대상에서 제외합니다. 순위 9는 오히려 **기전상 모순**됩니다 — Vildagliptin은 기능하는 췌장 β세포가 있어야 효과를 내는데, 췌장무형성증은 췌장 자체가 선천적으로 없거나 미형성된 질환입니다.

## 이 예측이 타당한 이유는?

구조화된 MOA 필드는 데이터 갭이지만, 근거 패키지에 포함된 문헌(PMID 18827867)에 따르면 Vildagliptin은 **DPP-4(dipeptidyl peptidase-IV)를 선택적으로 억제**하여 GLP-1과 GIP(인크레틴 호르몬)의 분해를 막고, 이를 통해 췌장 α/β 세포 기능을 개선해 제2형 당뇨병에서 혈당을 조절하는 약물입니다.

제1형 당뇨병은 자가면역에 의한 β세포 파괴가 핵심 병태생리이므로, 기존 승인 기전("이미 존재하는 β세포의 인슐린 분비 증강")과는 다른 방향의 가설이 필요합니다. 근거 패키지에 포함된 전임상 연구(PMID 25395211, 23523961)는 DPP-4 억제가 산화스트레스로 인한 β세포 파괴를 완화하고 **β세포 신생(neogenesis)**을 유도할 가능성을 시사하며, 임상 연구(PMID 22855332, 18597213)는 저혈당 시 글루카곤 역조절 반응에 미치는 영향을 확인했습니다. 즉, "잔존 β세포 기능 보존" 가설이지 "자가면역 파괴를 되돌리는" 기전은 아니므로 승인 적응증과는 명확히 구분되는 독립적 검증이 필요합니다.

## 임상시험 근거

제공된 임상시험 목록 대부분(50건 이상)은 실제로는 **제2형 당뇨병 환자 대상**이며, 평가자가 이미 "grade C / 족군 불일치" 로 표시해 두었습니다. 제1형 당뇨병을 명시적으로 다룬 시험은 다음 3건뿐입니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01147276](https://clinicaltrials.gov/study/NCT01147276) | Phase 4 | 완료 | 28 | 제1형 당뇨병 환자에서 vildagliptin이 저혈당 시 글루카곤 역조절 반응에 미치는 영향 조사 |
| [NCT06021119](https://clinicaltrials.gov/study/NCT06021119) | Phase 3 | 완료 | 50 | MiniMed 780G AHCL 시스템 사용 중인 제1형 당뇨병 청소년/청년 대상, 라마단 이프타르 식후 혈당 변동에 대한 vildagliptin 병용 효과 |
| [NCT06348706](https://clinicaltrials.gov/study/NCT06348706) | Phase 3 | 완료 | 60 | 제1형 당뇨병 청소년의 비알코올성 지방간염(NASH)에 대한 DPP-4 억제제 보충 효과 |

나머지 시험들은 대부분 제2형 당뇨병 인구를 대상으로 하며(예: NCT00099853, NCT00728351 등), 이 적응증(T1DM)과 직접 관련이 없어 제외했습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/) | 2021 | RCT (이중맹검) | J Clin Endocrinol Metab | Rapamycin+Vildagliptin 병용이 장기 이환 제1형 당뇨병 환자의 β세포 기능 회복에 미치는 영향 평가 |
| [39318059](https://pubmed.ncbi.nlm.nih.gov/39318059/) | 2024 | RCT | Diabetes Obes Metab | 제1형 당뇨병+NASH 청소년에서 vildagliptin 추가요법이 MMP-14, 간 경직도, 무증상 죽상경화증에 미치는 영향 |
| [38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/) | 2023 | RCT | Diabetol Metab Syndr | MiniMed 780G 사용 제1형 당뇨병 청소년/청년의 라마단 이프타르 관련 혈당 변동 완화 |
| [22855332](https://pubmed.ncbi.nlm.nih.gov/22855332/) | 2012 | 임상 기전 연구 | J Clin Endocrinol Metab | Vildagliptin이 고혈당 시 글루카곤 분비를 감소시키고, 제1형 당뇨병에서 저혈당 시 글루카곤 역조절을 유지 |
| [31781045](https://pubmed.ncbi.nlm.nih.gov/31781045/) | 2019 | 기전/PK 연구 | Front Endocrinol | Vildagliptin이 GLP-1·GIP 불활성화를 차단하여 24시간 동안 인크레틴 농도를 유지시키는 기전 규명 |
| [18597213](https://pubmed.ncbi.nlm.nih.gov/18597213/) | 2008 | 임상 기전 연구 | Horm Metab Res | 제1형 당뇨병 환자의 식사 중 글루카곤 농도에 대한 vildagliptin 효과 |
| [30848158](https://pubmed.ncbi.nlm.nih.gov/30848158/) | 2019 | Review | Expert Opin Investig Drugs | DPP-4 억제제가 제1형 당뇨병에서 자가면역에 의한 β세포 파괴에 보호 효과를 가질 가능성 논의 |
| [16629719](https://pubmed.ncbi.nlm.nih.gov/16629719/) | 2006 | Review | Pediatr Diabetes | 소아 당뇨병 치료에서 인크레틴 기반 약제(DPP-4 억제제 포함)의 이론적·실용적 고려사항 |
| [25395211](https://pubmed.ncbi.nlm.nih.gov/25395211/) | 2015 | 전임상 (동물) | Curr Pharm Biotechnol | 제1형 당뇨병 후기 단계 랫드 모델에서 vildagliptin이 β세포 신생을 유도하고 지질 프로파일 개선 |
| [23523961](https://pubmed.ncbi.nlm.nih.gov/23523961/) | 2013 | 전임상 (동물) | Arch Med Res | 제1형 당뇨병 랫드 모델에서 vildagliptin이 산화스트레스와 β세포 파괴를 완화 |

## 한국 시판 정보

한국에는 현재 Vildagliptin의 허가된 제품이 없습니다(미상매, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 상위 8개 예측(강직인간증후군, 지방위축증군 등)은 기전적 연관성이 전무하고 임상시험·문헌 근거가 전혀 없습니다(L5). 순위 9(췌장무형성증)는 오히려 기전상 모순됩니다. 근거를 실제로 갖춘 유일한 후보인 제1형 당뇨병(순위 10)도 확증적 RCT 없이 가설 검증 단계(L3, Research Question)에 머물러 있어, 이번 단계에서 재창출을 진행할 근거 수준에 미달합니다.

**진행하려면 필요한 것:**
- **[Blocking]** 한국(또는 원 허가국) 공식 허가사항의 경고·금기 정보 확보 — 현재 안전성 초기평가(S1) 진입이 불가능한 상태
- 상세 MOA 데이터 확보 (DrugBank API 조회)
- 제1형 당뇨병 가설에 대한 전향적 대조군 임상시험(특히 신규 진단/밀월기 환자 대상 β세포 기능 보존 종점) 확보
- 순위 1~9 예측은 추가 문헌·전임상 근거가 발견되지 않는 한 재평가 대상에서 제외 권장
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

