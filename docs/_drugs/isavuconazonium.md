---
layout: default
title: Isavuconazonium
parent: 모델 예측만 (L5)
nav_order: 437
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-15
description: "Isavuconazonium: 예측 신규 적응증 폐포자충증 (Pneumocystosis) (근거 수준 L5). 기존 적응증: 1. 만 18세 이상 성인에서의 침습성 아스페르길루스증 치료 2. 만 18세 이상 성인에서의 암포테리신 B…"
monitor_inn: "isavuconazonium"
predicted_indications: ["pneumocystosis", "mycetoma"]
---

# Isavuconazonium
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Isavuconazonium: 침습성 진균 감염에서 폐포자충증으로
{: .text-alpha }

## 한 문장 요약

Isavuconazonium은 한국에서 크레셈바(캡슐·주사제)로 시판 중인 항진균제입니다. TxGNN 모델은 **폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 임상시험과 문헌은 **0건**입니다. 2순위 예측인 **균종(Mycetoma)**은 간접 문헌 1편만 있어, 두 예측 모두 근거가 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 만 18세 이상 성인에서의 침습성 아스페르길루스증 치료 2. 만 18세 이상 성인에서의 암포테리신 B 투여가 적합하지 않은 침습성 털곰팡이증 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202000447/EE)) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 0.9956 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Isavuconazonium 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “이사부코나조늄 황산염은 아졸계 항진균제인 이사부코나졸의 전구약물이다. […] 이사부코나조늄 황산염은 아졸계 항진균 약물인 이사부코나졸의 전구약물이다. 이사부코나졸은 사이토크롬 P-450 의존성 효소인 라노스테롤 14-알파-탈메틸화효소를 억제함으로써 진균 세포막의 핵심 구성성분인 에르고스테롤의 합성을 억제한다.” 영어 원문: "Isavuconazonium sulfate is the prodrug of isavuconazole, an azole antifungal. […] Isavuconazonium sulfate is the prodrug of isavuconazole, an azole antifungal drug. Isavuconazole inhibits the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14-alpha-demethylase." ([DailyMed: Cresemba (isavuconazonium sulfate) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7f73b8-586a-4df0-935f-fecd4696c16c), 버전 2025-04-25; 확인일 2026-11-19). 알려진 정보에 따르면 Isavuconazonium은 isavuconazole의 전구약물인 광범위 트리아졸계 항진균제로, 진균의 lanosterol 14-alpha-demethylase(CYP51)를 억제하여 ergosterol 합성을 차단합니다.

다만 이 기전은 폐포자충증에는 잘 맞지 않습니다. *Pneumocystis jirovecii*는 세포막에 ergosterol이 거의 없고 콜레스테롤 등 다른 스테롤을 사용하므로, 아졸계 약물이 효과적이라고 보기 어렵습니다. 0.9956라는 높은 점수는 TxGNN 모델(딥러닝)이 산출한 값으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영했을 수 있으며 생물학적 근거는 아닙니다. 1차 치료제인 trimethoprim-sulfamethoxazole이 이미 확립되어 있다는 점도 고려해야 합니다.

참고로 2순위 예측인 균종(Mycetoma)은 기전상 더 설득력이 있습니다. 진균성 균종(eumycetoma)의 원인균은 아졸계 약물에 감수성이 있고, itraconazole이 현재 표준 치료입니다. 반면 방선균성 균종(actinomycetoma)은 세균 감염이어서 항진균제에 반응하지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

폐포자충증에 대한 문헌은 없습니다. 2순위 예측인 균종에 대해서는 다음 1편이 있으며, 직접적인 임상 연구가 아닌 간접 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Review | Parasites & Vectors | 방치된 열대질환(NTD) 관리를 위한 경구 항감염제의 적응증 외 사용 파이프라인 검토 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202000447 | 크레셈바캡슐100mg (이사부코나조늄황산염) | 경질캡슐 (상부 흰색, 하부 적갈색) | 허가사항 PDF 참조 |
| 202000446 | 크레셈바주200mg (이사부코나조늄황산염) | 주사제 (바이알) | 허가사항 PDF 참조 |

두 제품 모두 한국화이자제약(주)이 제조·판매합니다.

## 안전성 고려사항

- **약물 상호작용**: 데이터에 177건의 상호작용이 확인되었습니다. 이 중 주요(Major) 등급은 다음과 같습니다.
  - Clarithromycin
  - Eliglustat
  - Cisapride
- 중등도(Moderate) 등급에는 코르티코스테로이드 계열(Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Budesonide), 당뇨병 치료제(Metformin, Pioglitazone, Saxagliptin, Linagliptin, Empagliflozin), Bupropion, Aprepitant, Loperamide, Cimetidine, Clotrimazole 등이 포함됩니다.
- 경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐포자충증 예측은 임상시험과 문헌이 전혀 없는 모델 예측(L5)뿐입니다. 또한 *Pneumocystis*에 ergosterol이 없다는 점 때문에 아졸계 기전이 생물학적으로 맞지 않아 보류를 권장합니다. 균종은 기전상 더 타당하지만 근거가 간접 문헌 1편(L4 수준)에 그쳐, 현 단계에서는 추가 연구가 필요한 연구 과제로 보는 것이 적절합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고·금기·적응증)의 확보 및 분석
- 폐포자충증: *Pneumocystis*에 대한 in vitro 활성 등 기전 검증 자료. 이것이 없다면 추가 개발의 타당성이 낮음
- 균종: *Madurella mycetomatis* 등 원인균에 대한 in vitro 감수성 자료와 초기 임상 자료
- 균종 연구 시 진균성과 방선균성 균종을 구분하는 대상 선정 전략
- 주요 상호작용 약물(Clarithromycin, Eliglustat, Cisapride) 병용에 대한 관리 계획

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Cresemba (isavuconazonium sulfate) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7f73b8-586a-4df0-935f-fecd4696c16c) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

