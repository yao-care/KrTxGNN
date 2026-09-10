---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: 장기이식 거부반응 예방에서 HIV 감염증으로

## 한 문장 요약

Mycophenolate Mofetil(MMF)은 원래 장기이식 후 거부반응 예방 및 GVHD 예방을 위한 면역억제제로 사용되어 왔습니다 (한국 내 시판 허가 정보는 현재 확인되지 않음). TxGNN 모델은 **HIV 감염증(HIV infectious disease)**에 효과가 있을 수 있다고 예측하며(예측 점수 **99.86%**), 현재 **10건의 임상시험**과 다수의 문헌이 이 방향을 탐색해왔으나, 대부분 소규모 파일럿 연구이거나 상태 불명·중단된 시험이어서 근거 수준은 **L3**입니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 장기이식 거부반응 예방 / GVHD 예방 (면역억제제) — 한국 허가 정보 없음 |
| 예측 신규 적응증 | HIV 감염증 (HIV infectious disease) |
| TxGNN 예측 점수 | 99.86% (rank 3438) |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

---

## 이 예측이 타당한 이유는?

현재 DrugBank의 상세 작용 기전(MOA) 데이터는 확보되지 않았습니다(Data Gap). 다만 본 Evidence Pack에 포함된 근거 자료들을 종합하면, MMF는 IMPDH(inosine monophosphate dehydrogenase)를 억제하여 세포 내 dGTP(deoxyguanosine triphosphate) pool을 감소시키는 기전을 가지고 있습니다. 이는 체외 실험에서 HIV의 역전사(reverse transcription) 효율을 저하시키고, 동시에 T세포의 활성화·증식을 억제하여 바이러스 복제에 필요한 활성화된 CD4+ 표적 세포를 줄이는 것으로 보고됩니다.

즉 MMF는 직접적인 항레트로바이러스제라기보다, 기존 HAART(고강도 항레트로바이러스 요법)의 **보조제(면역 활성화 억제 및 바이러스 저장고 감소 목적)**로 위치합니다. 여러 임상시험에서 MMF가 abacavir 등 NRTI와 병용 시 세포 내 dGTP 고갈을 통해 항바이러스 활성을 증강시킨다는 보고가 있으나, 이는 FDA 승인 HIV 표준 치료 경로는 아닙니다. 또한 MMF는 신장이식 등에서 HIV 감염 환자의 표준 면역억제제로 이미 광범위하게 사용되고 있어(NCT00009009, NCT02793544 등), 임상적 사용 경험 자체는 상당히 축적되어 있습니다.

---

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | 상태 불명 | 90 | MAN2 연구 — ART 미투여 만성 HIV-1 감염자에서 MMF의 면역 과활성화 억제 및 CD4+ 감소 예방 효과 평가 |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | 상태 불명 | 90 | MAN2 하위연구 — MMF가 HIV-1 감염자의 심혈관 대리 지표에 미치는 영향 평가 |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | 조기 종료(Withdrawn) | 0 | Abacavir 병용 MMF의 안전성·내약성 및 바이러스량 감소 효과 평가 목적이었으나 등록 없이 철회 |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | 완료 | 27 | HIV 감염 신장이식 환자의 급성 거부반응 발생률 평가(MMF는 표준 면역억제 요법의 일부) |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | 완료 | 56 | DAPD 단독 대비 DAPD+MMF 병용 요법의 안전성·유효성 비교(치료 경험자 대상) |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | 완료 | 5 | HIV 감염자 대상 이식편 유도 위한 비골수제거 조혈모세포이식, MMF는 이식 후 면역억제 목적 병용 |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | 완료 | 10 | 말기신부전 HIV 감염 환자의 신장이식 안전성·유효성 평가, MMF는 표준 항거부반응제 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 중단(Terminated) | 8 | Anti-r-HuEpo 관련 순수적혈구재생불량증 치료 비교(HIV 무관, MMF+cyclosporine 병용군) |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | 모집 중 | 56 | 고령 고위험 AML 환자의 반일치 조혈모세포이식 전처치 요법(HIV 무관) |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | 완료 | 80 | HLA 불일치 골수이식 후 GVHD 예방을 위한 MMF 병용(HIV 무관, 표준 이식 프로토콜) |

**주의:** 상위 3건(MAN2 연구 및 하위연구, abacavir 병용 연구)만이 MMF의 HIV 치료 효과를 직접 평가하는 시험이며, 나머지는 HIV 감염자의 장기이식 시 표준 면역억제 요법으로 MMF가 사용된 사례이거나 HIV와 무관한 연구입니다. 직접 평가 시험들도 상태 불명 또는 철회되어 확정적 결과가 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | 무작위 파일럿 연구 | J Acquir Immune Defic Syndr | HAART 중단 기간 중 MMF 병용이 면역반응 및 혈장/림프조직 바이러스량에 미치는 영향 평가 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | 임상시험 | J Acquir Immune Defic Syndr | Abacavir 포함 요법에 MMF 추가 시 세포 내 dGTP 고갈 및 혈장 HIV-1 RNA 감소 관찰 |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | 임상 연구 | AIDS | 치료 미경험 HIV-1 환자에서 MMF 병용 유무에 따른 HAART 효과(바이러스 감소 속도, 잠복 저장고) 비교 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | 임상 연구 | AIDS Res Hum Retroviruses | 치료 미경험 급·만성 HIV-1 환자에서 MMF+HAART 병용이 면역학적으로 유해하지 않음을 확인 |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | 파일럿 연구 | J Acquir Immune Defic Syndr | 다제내성 HIV-1 감염(AIDS) 환자 7명 대상 MMF+ABC+ddI 등 병용 개방표지 시험 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | 임상 PK/PD 연구 | Clin Pharmacokinet | Abacavir·efavirenz·nelfinavir 병용 HIV 환자에서 저용량 MMF의 약동/약력학 분석 |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | 임상 PK 연구 | Clin Pharmacokinet | MMF가 항레트로바이러스제 약동학 및 세포 내 뉴클레오시드 삼인산 풀에 미치는 영향 평가 |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | 임상 연구 | AIDS | 약제내성 HIV 감염에서 DAPD 단독 대비 DAPD+MMF 병용의 안전성·항바이러스 활성 평가 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | HIV 질환에서 면역억제제(MMF 포함)의 역할 및 면역 과활성화 표적치료 개념 고찰 |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | 중개/전임상 | J Clin Invest | 항증식 약물을 이용한 HIV 감염 클론 표적화 전략 탐색(항암화학요법 병용 사례 기반) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요. (본 Evidence Pack에서는 주요 경고, 금기, 약물상호작용 데이터가 확보되지 않았으며, TFDA 수준 등재 정보 부재로 안전성 초기 평가(S1) 자체가 제한됩니다.)

---

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- MMF의 HIV 치료 효과를 직접 평가한 임상시험(MAN2 연구 등)은 모두 **상태 불명(UNKNOWN)** 이거나 **철회(WITHDRAWN)** 되어 확정적 유효성 근거가 없습니다.
- 나머지 임상시험 다수는 HIV 감염 환자의 **장기이식 시 표준 면역억제** 목적으로 MMF가 사용된 사례로, "HIV 치료"라는 예측 적응증과는 결이 다릅니다.
- 허가사항(경고/금기/DDI) 데이터가 전혀 확보되지 않아(Blocking Data Gap, DG001) 안전성 초기 평가(S1) 진입이 불가능한 상태입니다.
- 한국 내 시판 허가 정보가 없어(미출시, 0건) 현 시점에서 실제 처방 전환 경로가 존재하지 않습니다.

**진행하려면 필요한 것:**
- TFDA(관련 규제기관) 수준의 최신 첨부문서(경고/금기/DDI) 확보
- DrugBank API를 통한 정식 작용 기전(MOA) 데이터 보완
- MAN2 연구(NCT00120419/NCT00247494) 결과 보고 여부 재확인 — 완료 후 미보고 상태일 가능성 확인 필요
- HIV 치료 효과만을 직접 평가하는 완료된 RCT 확보 (현재는 파일럿·PK 연구 수준)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

