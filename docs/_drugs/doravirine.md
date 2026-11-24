---
layout: default
title: Doravirine
parent: 모델 예측만 (L5)
nav_order: 288
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Doravirine: 예측 신규 적응증 원숭이 면역결핍 바이러스 감염 (Simian Immunodeficiency Virus Infection) (근거 수준 L5). 기존 적응증: 이전 항레트로바이러스 치료 경험이 없거나, 기존 항레트로바이러스 치료 요법에 치료 실패 없이 적어도 6개월…"
monitor_inn: "DORAVIRINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Doravirine
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

## Doravirine: HIV-1 감염에서 원숭이면역결핍바이러스 감염으로
{: .text-alpha }

## 한 문장 요약

Doravirine은 비뉴클레오시드 역전사효소 억제제(NNRTI)로, 원래 HIV-1 감염 치료에 사용되었습니다.
TxGNN 모델은 **원숭이 면역결핍 바이러스 감염(Simian Immunodeficiency Virus Infection)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 지지하는 **임상시험은 0건**이며 간접적으로 관련된 **문헌은 1편**(HIV-1 치료제에 관한 리뷰)뿐입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이전 항레트로바이러스 치료 경험이 없거나, 기존 항레트로바이러스 치료 요법에 치료 실패 없이 적어도 6개월 이상 안정된 바이러스 수치 억제 효과를 보이며(HIV-1 RNA < 50 copies/mL) 도라비린에 대한 알려진 내성 관련 치환이 없는 성인 환자들의 HIV-1 감염 치료를… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201908060/EE)) |
| 예측 신규 적응증 | 원숭이 면역결핍 바이러스 감염 (Simian Immunodeficiency Virus Infection) |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 (직접적인 연구 없이 기전적 추정만 존재) |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Doravirine 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “도라비린은 항레트로바이러스 약물이다. […] 도라비린은 HIV-1의 피리디논계 비뉴클레오시드 역전사효소 억제제로서, HIV-1 역전사효소(RT)를 비경쟁적으로 억제하여 HIV-1 복제를 억제한다. 생화학적 분석에서 재조합 야생형 HIV-1 RT의 RNA 의존성 DNA 중합에 대한 도라비린의 50% 억제 농도(IC 50 )는 12.2±2.0 nM(n=3)이었다.” 영어 원문: "Doravirine is an antiretroviral drug. […] Doravirine is a pyridinone non-nucleoside reverse transcriptase inhibitor of HIV-1 and inhibits HIV-1 replication by non-competitive inhibition of HIV-1 reverse transcriptase (RT). The inhibitory concentration at 50% (IC 50 ) of doravirine for RNA-dependent DNA polymerization of recombinant wild-type HIV-1 RT in a biochemical assay was 12.2±2.0 nM (n=3)." ([DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25), 버전 2026-07-09; 확인일 2026-11-19). 알려진 정보에 따르면 Doravirine은 HIV-1에 대해 허가된 NNRTI 계열 약물로, 바이러스 역전사효소의 비경쟁적 결합 부위에 작용하여 바이러스 복제를 억제합니다.

SIV는 HIV와 가까운 렌티바이러스 계열이어서 기전상 연관성은 있습니다. 그러나 NNRTI는 일반적으로 HIV-1에는 활성이 있지만 HIV-2에는 효과가 없습니다. 많은 SIV 균주도 역전사효소의 NNRTI 결합 부위 구조 차이 때문에 본래 내성을 보입니다. 따라서 SIV에 대한 활성은 불확실하며 균주에 따라 달라질 수 있습니다.

높은 TxGNN 점수는 직접적인 증거라기보다 HIV와의 네트워크 근접성을 반영한 것으로 보입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | 새로운 역전사효소 전위 억제제 islatravir의 HIV-1 감염 치료·예방 역할 논의 (doravirine이나 SIV를 직접 다루지 않음) |

관련 임상시험 등록은 현재 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201908060 | 피펠트로정(도라비린) | 한 면에 ‘MSD 로고’와 ‘700’이 새겨져 있는 흰색의 타원형 정제 | 한국엠에스디(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201908060/EE) | 유효 |
| 202000448 | 델스트리고정 | 한 면에 ‘MSD 로고’와 ‘776’이 새겨져 있는 노란색의 타원형 정제 | 한국엠에스디(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202000448/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 59건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Dexamethasone, Lumacaftor
  - **Moderate**: Glycerol phenylbutyrate, Metreleptin, Troglitazone, Deferasirox, Praziquantel, Griseofulvin
  - 그 외 Aprepitant, Cimetidine, Clarithromycin, Fluconazole 등은 Minor 수준입니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
SIV 감염에 대한 임상시험이 없고 문헌도 직접적인 관련성이 낮습니다. NNRTI 계열이 SIV에 본래 내성을 보일 수 있다는 점에서 기전상 근거도 약합니다. 높은 예측 점수는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영한 결과일 수 있으며, 생물학적 근거는 아닙니다. SIV는 주로 비인간 영장류의 질환이므로 인체 대상 약물 재창출의 범위와도 맞지 않습니다.

**진행하려면 필요한 것:**
- Doravirine의 SIV 역전사효소에 대한 시험관 내 활성 및 균주별 감수성 데이터
- 상세한 작용 기전(MOA) 데이터
- 허가사항(경고·금기) 확인
- 인체 대상 적응증으로서의 타당성 검토

*참고: 이 보고서는 예측 1순위 적응증을 기준으로 작성했습니다. 2순위(고양이 후천성 면역결핍 증후군)는 수의학 적응증이며 NNRTI의 활성이 낮아 근거가 없고, 3순위(희귀 신경발달장애)는 기전적 연관성이 확인되지 않아 두 가지 모두 Hold가 적절합니다.*

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

