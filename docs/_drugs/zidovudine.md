---
layout: default
title: Zidovudine
parent: 모델 예측만 (L5)
nav_order: 791
evidence_level: L5
indication_count: 3
monitor_inn: "ZIDOVUDINE"
predicted_indications: ["simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-28
description: "Zidovudine: 예측 신규 적응증 원숭이면역결핍바이러스 감염 (근거 수준 L5). 기존 적응증: 허가 적응증 본문 확인 불가 (허가증에는 문서 링크만 있음)"
---

# Zidovudine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **3** 건
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

## Zidovudine: 원숭이면역결핍바이러스 감염
{: .text-alpha }

## 한 문장 요약

Zidovudine은 뉴클레오사이드 역전사효소 억제제(NRTI)로, 한국에서 단일성분 제제로 허가를 받은 약물입니다. 다만 이번 데이터에는 허가 적응증 본문이 담겨 있지 않고 PDF 링크만 있습니다.
TxGNN 모델은 **원숭이면역결핍바이러스 감염(simian immunodeficiency virus infection)**에 효과가 있을 수 있다고 예측하며, 임상시험은 없고 **20편의 문헌**(대부분 원숭이 동물실험)이 이 방향을 뒷받침합니다.
SIV 감염은 동물 모델 질환이므로 새로운 인체 적응증이라기보다 HIV 치료를 뒷받침하는 전임상 근거로 보는 것이 적절합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문 확인 불가 (허가증에는 문서 링크만 있음) |
| 예측 신규 적응증 | 원숭이면역결핍바이러스 감염 |
| TxGNN 예측 점수 | 0.9996 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 5건 (모두 단일성분, 유효, 수출용) |
| 권장 결정 | Hold |

근거 수준 설명: 인용된 문헌은 모두 원숭이 동물실험, 시험관 연구, 총설입니다. 예측 질환인 SIV 감염을 직접 다룬 연구는 있으나 이는 인체 질환이 아닌 동물 모델 연구이고 임상시험은 없습니다. 이번 데이터에서 자동 산정된 L3(관찰 연구 또는 체계적 문헌고찰)에 해당하는 연구는 확인되지 않아 보수적으로 L5로 판정했습니다.

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 없습니다. 알려진 정보에 따르면 zidovudine은 NRTI 계열 항레트로바이러스제로, 바이러스의 역전사효소 의존적 복제 경로를 차단합니다.

SIV는 HIV와 가까운 렌티바이러스이며 같은 역전사 경로로 복제하므로, 기전상 zidovudine이 작용할 수 있습니다. 문헌에는 신생 원숭이에서 즉시 투여 시 바이러스 부하가 줄고 생존이 연장되었다는 보고가 있습니다. SIV 역전사효소의 Q151M 내성 변이 보고도 표적 작용을 뒷받침합니다.

다만 SIV 감염은 동물 모델 질환이라 인체 임상 적응증이 없습니다. 이 근거는 새로운 인체 재창출 기회가 아니라, 기존 항바이러스 용도에 대한 번역 연구(translational) 근거로 해석해야 합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | 동물실험 | AIDS | 원숭이에서 zidovudine·lamivudine·indinavir 병용 노출 후 예방(PEP)으로 질내 SIV 전파 방지 평가 |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | 동물실험 | Antimicrob Agents Chemother | 신생 원숭이에서 즉시 경구 AZT 투여 시 감염 예방 또는 바이러스 부하 감소, 항바이러스 면역 증강 |
| [7690823](https://pubmed.ncbi.nlm.nih.gov/7690823/) | 1993 | 동물실험 | J Infect Dis | 감염 후 1~72시간 시점에 시작한 zidovudine 치료의 효과 비교 |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | 동물실험 | J Infect Dis | 주산기 감염 원숭이에서 생존 연장, 혈청 및 뇌척수액 바이러스 부하 감소 (감염 자체는 예방하지 못함) |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | 내성 변이 연구 | Antimicrob Agents Chemother | Q151M 변이 SIV는 zidovudine 내성을 보이며 신생 원숭이에서 AIDS를 유발 |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | 총설 | Ann Emerg Med | 비직업적 HIV 노출 후 예방; 직접적 효능 연구는 없으나 동물 연구가 간접 근거 제공 |
| [2016686](https://pubmed.ncbi.nlm.nih.gov/2016686/) | 1991 | 동물실험 | J Acquir Immune Defic Syndr | 원숭이에서 FLT와 AZT 비교, 둘 다 감염을 막지 못했으나 FLT가 약 10배 강력 |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | 동물실험 | AIDS Res Hum Retroviruses | AZT 투여 마카크의 급성 감염기 바이러스 및 면역 동태 분석 |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | 동물실험 | J Virol | 노출 후 단기 HAART 예방이 림프구 증식 동태에 미치는 영향 예비 보고 |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | 동물실험 | J Virol | SHIV 감염 마카크에서 HAART로 바이러스혈증이 줄어도 골수 조혈 장애가 지속 |

## 한국 시판 정보

허가 적응증 본문은 이번 데이터에 포함되어 있지 않고 문서 링크만 제공되므로, 적응증 칸에는 허가사항 문서 참조로 표기합니다. 5건 모두 수출용 단일성분 제제입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199800287 | 아지도민정300밀리그람(지도부딘)(수출용) | 필름코팅정 | 허가사항 문서 참조 |
| 200308641 | 지도딘캡슐100mg(지도부딘)(수출용) | 캡슐 | 허가사항 문서 참조 |
| 199800341 | 아지도민캅셀250밀리그람(지도부딘)(수출용) | 경질캡슐 | 허가사항 문서 참조 |
| 200103740 | 대한에이젯티캡슐100mg(지도부딘)(수출용) | 캡슐 | 허가사항 문서 참조 |
| 199900540 | 유한지도부딘캅셀250mg(수출용) | 캡슐 | 허가사항 문서 참조 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 데이터에 포함되어 있지 않으므로 허가사항을 참조하세요.

- **지식그래프상 금기 관계**: 지식그래프(PrimeKG)에 기록된 관계이며 허가 라벨 내용이 아닙니다. 간부전, 신장 질환, 췌장염, 담낭 질환, 근병증·근염, 호중구감소증, 무과립구증, 빈혈(대적혈구성 포함), 고중성지방혈증, 지방간·비알코올성 지방간염, 젖산산증 등이 기록되어 있습니다.
- **약물 상호작용** (총 100건 중 일부): 다음과 같은 약물이 확인되었습니다.
  - 중등도: amphotericin B 계열, 스테로이드(betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), naltrexone, rosuvastatin, simvastatin, orlistat
  - 경미: cimetidine, clarithromycin
  - 등급 미상: pantoprazole, morphine, metformin, omeprazole

## 결론 및 다음 단계

**결정: Hold**

**사유:**
SIV 감염은 동물 모델 질환으로 인체 임상 적응증이 아니며, 관련 임상시험이 없고 근거는 원숭이 실험에 한정됩니다. 새로운 인체 재창출 기회로 보기 어렵고, 허가 적응증과 안전성 정보도 확인되지 않았습니다.

참고로 다른 예측 질환도 근거가 부족합니다.
- 신경발달장애(보행실조·언어소실·피질 백질 감소): TxGNN 점수 0.9996이나 임상시험과 문헌이 없고 기전 연결도 없습니다. 근병증·미토콘드리아 독성 위험이 우려됩니다.
- 폐지된 가족성 복합 고지혈증: 점수 0.9962이나 용어가 폐지되어 유효한 표적이 아니며, zidovudine은 지질 이상을 악화시킬 수 있어 예측이 부정확할 가능성이 높습니다.

**진행하려면 필요한 것:**
- 허가사항(경고, 금기, 적응증) 문서의 확보 및 분석
- 작용 기전(MOA) 데이터 보충 (DrugBank)
- SIV 연구를 HIV 적응증의 전임상 근거로만 활용할지에 대한 방향 결정
- 시판 상태(취소 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

