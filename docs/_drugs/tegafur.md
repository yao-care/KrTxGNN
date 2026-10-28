---
layout: default
title: Tegafur
parent: 높은 근거 (L1-L2)
nav_order: 719
evidence_level: L1
indication_count: 10
monitor_inn: "Tegafur"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "rectosigmoid junction neoplasm", "colonic lymphangioma", "cavernous hemangioma of colon"]
last_modified_at: 2026-10-28
description: "Tegafur: 예측 신규 적응증 대장 종양 (근거 수준 L5). 기존 적응증: 허가 적응증 문구 확인 불가 (허가증에 PDF 링크만 수록)"
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

## Tegafur: 기존 항종양 적응증에서 대장 종양으로
{: .text-alpha }

## 한 문장 요약

Tegafur는 5-fluorouracil(5-FU)의 경구용 전구약물로, 한국에서 단일 성분 제제로 허가되어 있습니다. 다만 허가 적응증의 구체적인 문구는 이번에 정리된 데이터에 포함되어 있지 않습니다.
TxGNN 모델은 **대장 종양(Colonic Neoplasm)**에 효과가 있을 수 있다고 예측하며, 이 질환을 직접 다룬 **임상시험 16건**과 **문헌 20편**이 검토되었습니다.
다만 이 예측은 기존 항암 용도와 같은 방향이어서 엄밀한 의미의 재창출이라기보다 기존 종양학적 사용의 연장선에 가깝습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 문구 확인 불가 (허가증에 PDF 링크만 수록) |
| 예측 신규 적응증 | 대장 종양 |
| TxGNN 예측 점수 | 0.9990 |
| 근거 수준 | L1 (완료된 Phase 3 RCT 다수) |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 5건 (모두 유효, 단일 성분) |
| 권장 결정 | Proceed with Guardrails |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Tegafur는 간 CYP2A6에 의해 5-FU로 전환되는 경구 전구약물입니다. 활성 대사체는 티미딜산 합성효소를 억제하고 RNA/DNA에 삽입되어 세포독성을 나타냅니다.

UFT 제제에서는 uracil이 디하이드로피리미딘 탈수소효소(DPD)를 경쟁적으로 억제하여 5-FU 노출을 높입니다. 이는 대장암에서 확립된 플루오로피리미딘 기전이므로, 예측과의 기전적 연결은 직접적이며 높은 TxGNN 점수와도 부합합니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | 완료 | 1608 | II/III기 결장암에서 UFT+LV vs 5-FU+LV 비교 |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | 완료 | 900 | Dukes C 대장암 수술 후 UFT vs 수술 단독 |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | 완료 | 2025 | 근치 절제 II기 결장암에서 UFT vs 관찰 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 완료 | 1535 | III기 결장암 보조요법으로 UFT+LV vs TS-1 |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | 완료 | 89 | Xeloda vs UFT+폴린산, 환자 선호도 교차 비교 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 불명 | 1191 | III기 대장암 보조요법으로 SOX vs XELOX |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Phase 3 | 불명 | 380 | IIB/III기 대장암에서 UFT+PSK vs UFT+LV |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | 불명 | 340 | III기 대장암 수술 후 UFT+LV 계열 요법 비교 |
| [NCT00004860](https://clinicaltrials.gov/study/NCT00004860) | Phase 2 | 완료 | 정보 없음 | 75세 이상 전이성 대장암에서 UFT+LV |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | 완료 | 47 | 전이성 대장암 1차 치료에서 cetuximab+irinotecan+oxaliplatin+UFT |

그 밖에 Phase 2 이하 시험, 관찰 연구, 진행 예정 시험이 추가로 있습니다. 위 표는 가장 관련성 높은 10건만 나열했습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | 고위험 III기 결장암에서 SOX vs UFT/LV 보조요법 (ACTS-CC 02) |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 5년 생존 추적: SOX는 DFS에서 UFT/LV보다 우월하지 않음 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 코호트 연구 및 메타분석 | Medicine | II/III기 결장암에서 UFT vs 5-FU 보조요법 비교 |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT (Phase 3) | Ann Oncol | II/III기 직장암 보조요법으로 S-1 vs UFT (ACTS-RC) |
| [10089948](https://pubmed.ncbi.nlm.nih.gov/10089948/) | 1999 | 메타분석 | Jpn J Clin Oncol | 경구 플루오로피리미딘 보조요법 개별 환자 자료 메타분석 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT 수술 후 보조화학요법의 임상 근거와 기전 |
| [16111469](https://pubmed.ncbi.nlm.nih.gov/16111469/) | 2005 | Review | Expert Rev Anticancer Ther | 결장암 병기별 항암화학요법 선택지 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | 합의 가이드라인 | Clin Colorectal Cancer | 아시아 전이성 대장암 치료 합의안 |
| [36676634](https://pubmed.ncbi.nlm.nih.gov/36676634/) | 2022 | 코호트 연구 | Medicina | IIA기 결장암에서 UFT 보조요법의 이점 |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | 증례 보고 | Cancer Chemother Pharmacol | 전이성 결장암 환자의 UFT 유발 용혈성 빈혈 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200300393 | 티에스원캡슐20,25 | 경질 캡슐 | 허가증에 PDF 링크만 수록 (본문 확인 필요) |
| 201706903 | 테고캡슐25 | 경질 캡슐 | 허가증에 PDF 링크만 수록 (본문 확인 필요) |
| 199700694 | 유에프티캡슐 | 경질 캡슐 | 허가증에 PDF 링크만 수록 (본문 확인 필요) |
| 201706904 | 테고캡슐20 | 경질 캡슐 | 허가증에 PDF 링크만 수록 (본문 확인 필요) |
| 200612254 | 타그린캡슐[수출용] | 경질 캡슐 | 허가증에 PDF 링크만 수록 (본문 확인 필요) |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (플루오로피리미딘 계열, 5-FU 전구약물) |
| 골수억제 위험 | 중등도로 추정 (플루오로피리미딘 계열의 일반적 특성) |
| 구토 유발성 등급 | 저~중등도 |
| 모니터링 항목 | CBC(분류 포함), 간·신기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

이 약물에 대한 구체적 독성 데이터는 이번에 정리된 자료에 없으므로, 허가사항의 경고 및 주의사항을 참조하세요.

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

참고로 문헌에는 UFT 투여 중 용혈성 빈혈 증례(PMID 11320674)와 S-1 투여 후 고중성지방혈증 증례(PMID 32936722)가 보고되어 있습니다.

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
UFT 기반 요법의 대규모 완료 Phase 3 RCT가 여러 건 있어 결장·대장암 보조요법에서 근거가 강합니다. 그러나 허가 적응증 본문, 안전성 정보, 작용 기전 데이터가 확인되지 않아 조건부로 진행하는 것이 적절합니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(첨부문서) PDF를 내려받아 허가 적응증, 경고, 금기 확인
- DrugBank 등에서 작용 기전(MOA) 데이터 보완
- 시판 현황(취소 여부) 확인
- 일부 시험(상태 불명)의 최신 진행 상태 및 결과 확인
- DPD 결핍 등 약물유전체 및 약물 상호작용 모니터링 계획 수립

**참고: 기타 예측 질환**
순위 2~10위 예측(맹장 융모선종, 맹장 신경내분비종양 G1, 대장 지방종, 맹장 질환, 대장 평활근종, 맹장 양성 신생물, 직장 S상 결장 접합부 신생물, 대장 림프관종, 대장 해면상 혈관종)은 직접 연구 근거가 없거나 대장암 사례 보고 수준입니다. 대부분 양성 병변으로 세포독성 화학요법의 근거가 없어 모두 보류(Hold) 대상입니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

