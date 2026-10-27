---
layout: default
title: Tegafur
parent: 높은 근거 (L1-L2)
nav_order: 719
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-15
description: "Tegafur: 예측 신규 적응증 대장 종양 (Colonic Neoplasm) (근거 수준 L1). 기존 적응증: 확인 불가 (허가 적응증 텍스트가 링크 형태로만 제공되어 내용 확인 불가)"
monitor_inn: "Tegafur"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "rectosigmoid junction neoplasm", "colonic lymphangioma"]
---

# Tegafur
{: .fs-9 }

근거 수준: **L1** | 예측 적응증: **10** 건
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

## Tegafur: 대장 종양(Colonic Neoplasm)으로의 근거 확인
{: .text-alpha }

## 한 문장 요약

Tegafur는 5-FU의 경구 전구약물로, 한국에서 단일제 캡슐 제품으로 허가·시판되고 있습니다.
TxGNN 모델은 **대장 종양(Colonic Neoplasm)**에 효과가 있을 수 있다고 예측하며, 현재 **17건의 임상시험**과 **20편의 문헌**이 이 방향을 지지합니다.
다만 대장암은 tegafur 병용제가 이미 여러 지역에서 사용되는 적응증이므로, 새로운 재창출이라기보다 기존 사용의 근거 확인에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 텍스트가 링크 형태로만 제공되어 내용 확인 불가) |
| 예측 신규 적응증 | 대장 종양 (Colonic Neoplasm) |
| TxGNN 예측 점수 | 99.90% |
| 근거 수준 | L1 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터(DrugBank 기준)는 없습니다. 다만 약리학적으로 잘 알려진 바에 따르면, tegafur는 5-fluorouracil(5-FU)의 경구 전구약물로 주로 간 CYP2A6에 의해 5-FU로 전환됩니다. 이후 티미딜레이트 합성효소(thymidylate synthase)를 억제하고 RNA/DNA에 삽입되어 항종양 효과를 나타내며, 이는 대장 선암과 직접 관련됩니다.

복합제에서는 보조 성분이 이를 보완합니다. UFT(tegafur-uracil)에서는 uracil이 DPD를 억제해 5-FU 분해를 늦추고, S-1에서는 gimeracil과 oteracil이 유사한 조절 및 소화관 보호 역할을 합니다.

위암과 대장암은 모두 소화관 선암으로 5-FU 계열 약물에 반응하는 공통 기전을 갖습니다. 대장암은 이미 많은 지역에서 tegafur 병용제의 확립된 사용 분야입니다.

## 임상시험 근거

관련성이 높은 시험 10건을 표로 정리했습니다.

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | 완료 | 1,608 | 2~3기 결장암 수술 후 UFT+LV vs 5-FU+LV 비교 |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | 완료 | 900 | Dukes C 대장암에서 수술 후 보조 UFT vs 수술 단독 비교 |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | 완료 | 2,025 | 근치 절제된 2기 결장암에서 UFT vs 관찰 비교 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 완료 | 1,535 | 3기 결장암 보조요법으로 UFT+LV vs TS-1 비교 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 상태 불명 | 1,191 | 3기 대장암 보조요법으로 SOX vs XELOX 비교 |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Phase 3 | 상태 불명 | 380 | 2B/3기 대장암에서 UFT+PSK vs UFT+LV 비교 (PSK 추가 효과 검증) |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | 상태 불명 | 340 | 3기 대장암 수술 후 UFT+LV, UFT+LV/UFT, UFT+LV+PSK/UFT+PSK 3가지 요법 비교 |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | 완료 | 89 | 진행성·전이성 대장암에서 Xeloda vs UFT 환자 선호도 교차 비교 (효능 평가 아님) |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 상태 불명 | 40 | 재발성 대장직장암에서 S-1 + 베바시주맙 |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | 완료 | 47 | 전이성 대장직장암 1차 치료로 세툭시맙, 이리노테칸, 옥살리플라틴, UFT 병용 (tegafur 기여도 분리 어려움) |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | 고위험 3기 결장암에서 SOX vs UFT/LV 보조요법 비교 (ACTS-CC 02) |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 5년 최종 생존 분석. SOX는 DFS에서 UFT/LV보다 우월하지 않음 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 코호트 연구 및 메타분석 | Medicine | 대만 전국 코호트 기반 2~3기 결장암에서 UFT vs 5-FU 보조요법 비교 (원자료의 연구 유형 분류는 RCT) |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT (Phase 3) | Ann Oncol | 2/3기 직장암 보조요법으로 S-1 vs UFT 비교 (ACTS-RC) |
| [10089948](https://pubmed.ncbi.nlm.nih.gov/10089948/) | 1999 | 메타분석 | Jpn J Clin Oncol | 대장암 근치 절제 후 경구 플루오로피리미딘 보조요법 무작위 시험의 개별 환자 자료 메타분석 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | 폐, 위, 대장, 유방암에서 UFT 보조화학요법의 임상 근거와 작용 기전 |
| [16111469](https://pubmed.ncbi.nlm.nih.gov/16111469/) | 2005 | Review | Expert Rev Anticancer Ther | 결장암의 병기별 화학요법 선택지 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | 합의 가이드라인 | Clin Colorectal Cancer | 전이성 대장암에 대한 아시아 합의 가이드라인 |
| [3933845](https://pubmed.ncbi.nlm.nih.gov/3933845/) | 1985 | 전임상 (동물) | Bull Tokyo Med Dent Univ | 쥐 대장암 모델에서 levamisole과 tegafur 병용 시 생존 연장 및 전이 감소 |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Case report | Cancer Chemother Pharmacol | 전이성 결장암에서 UFT 치료 중 용혈성 빈혈 발생 보고 (안전성 신호) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200300393 | 티에스원캡슐20,25 | 경질 캡슐 | 허가 적응증 텍스트 확인 불가 (허가사항 참조) |
| 201706903 | 테고캡슐25 | 경질 캡슐 | 허가 적응증 텍스트 확인 불가 (허가사항 참조) |
| 199700694 | 유에프티캡슐 | 경질 캡슐 | 허가 적응증 텍스트 확인 불가 (허가사항 참조) |
| 201706904 | 테고캡슐20 | 경질 캡슐 | 허가 적응증 텍스트 확인 불가 (허가사항 참조) |
| 200612254 | 타그린캡슐[수출용] | 경질 캡슐 | 허가 적응증 텍스트 확인 불가 (허가사항 참조) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (Fluoropyrimidine 계열, 5-FU 전구약물) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 (일반적으로 CBC, 간·신기능 확인) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로 수집된 문헌에는 UFT 투여 중 용혈성 빈혈 사례(PMID 11320674), S-1 투여 후 고중성지방혈증 사례(PMID 32936722)가 보고되어 있습니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
대장·결장암에서 tegafur 기반 요법(UFT, S-1)의 효능을 직접 검증한 대규모 완료 Phase 3 RCT가 여러 건 있어 근거 수준은 L1입니다. 다만 이는 이미 확립된 사용에 가까우며, 한국 허가 적응증과 안전성 정보를 아직 확인하지 못한 상태입니다.

**진행하려면 필요한 것:**
- 한국 허가사항 문서(5건)의 적응증, 경고, 금기 확인 (대장암이 이미 허가 범위에 포함되는지 포함)
- DrugBank 기반 작용 기전(MOA) 데이터 보완
- 허가사항 기반 안전성 선별 (골수억제, DPD 결핍, 약물 상호작용 등)

## 참고: 기타 예측 적응증

원 자료에는 다른 예측 적응증도 포함되어 있습니다.

| 순위 | 예측 질환 | 근거 수준 | 권장 결정 | 비고 |
|-----|---------|---------|---------|------|
| 2 | 위암 (Gastric carcinoma) | L1 | Proceed with Guardrails | S-1은 위암 보조·수술 전후·진행성 치료의 기본 요법으로 널리 쓰이며, 이 역시 확립된 사용입니다. |
| 9 | 직장 S상 결장 접합부 종양 | L4 | Research Question | 직장암 치료 중 이상반응 증례 1건만 있으며 효능 근거는 대장암 시험에 의존합니다. |
| 6, 8 | 맹장 질환, 맹장 양성 신생물 | L4 | Hold | 대장암 증례·전임상 문헌 위주의 간접 근거입니다. |
| 3, 4, 5, 7, 10 | 맹장 융모선종, 맹장 신경내분비종양 G1, 결장 지방종, 결장 평활근종, 결장 림프관종 | L5 | Hold | 대부분 양성 병변으로 세포독성 치료의 근거가 없으며, 해부학적 연관성에 의한 예측으로 보입니다. |
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

