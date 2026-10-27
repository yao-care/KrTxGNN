---
layout: default
title: Mirvetuximab Soravtansine
parent: 모델 예측만 (L5)
nav_order: 520
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mirvetuximab Soravtansine: 예측 신규 적응증 항트롬빈 결핍증 2형 (antithrombin deficiency type 2) (근거 수준 L5). 기존 적응증: 허가 적응증 원문이 링크로만 제공되어 구체적 문구를 확인할 수 없음 (해외 허가 기준: 백금 저항성 난소암)"
monitor_inn: "Mirvetuximab Soravtansine"
predicted_indications: ["antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "candidiasis", "plasma cell myeloma", "indolent plasma cell myeloma", "tinea corporis", "thrombophilia", "uterine polyp", "pediatric systemic lupus erythematosus"]
---

# Mirvetuximab Soravtansine
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Mirvetuximab Soravtansine: 난소암에서 항트롬빈 결핍증 2형으로
{: .text-alpha }

## 한 문장 요약

Mirvetuximab Soravtansine은 엽산 수용체 알파(FRα)를 표적으로 하는 항체-약물 접합체(ADC)로, 원래 백금 저항성 난소암 치료에 사용되는 항종양 약물입니다.
TxGNN 모델은 **항트롬빈 결핍증 2형(antithrombin deficiency type 2)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 지지하는 **임상시험은 0건, 문헌도 0편**이며 기전상 타당한 연관성도 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문이 링크로만 제공되어 구체적 문구를 확인할 수 없음 (해외 허가 기준: 백금 저항성 난소암) |
| 예측 신규 적응증 | 항트롬빈 결핍증 2형 (antithrombin deficiency type 2) |
| TxGNN 예측 점수 | 97.95% |
| 근거 수준 | L5 |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 이 약의 상세한 작용 기전 데이터는 이번 보고서에 수집되지 않았습니다. 다만 약리학 자료에 따르면, 이 약의 항체 부분(M9346A)은 FRα(FOLR1)에 Kd 0.08 nM의 높은 친화도로 결합합니다. 이후 세포 내로 들어가 미세소관 억제 성분인 DM4(메이탄시노이드 계열)를 방출하여 FRα를 발현하는 종양세포를 사멸시키는 것으로 알려져 있습니다.

반면 항트롬빈 결핍증 2형은 SERPINC1 유전자 변이로 생기는 유전성 응고 질환으로, FRα 발현 종양세포와는 관련이 없습니다. 비악성 만성 질환에 세포독성 payload를 가진 약물을 쓰는 것도 적절하지 않습니다. 따라서 높은 예측 점수는 지식 그래프상의 인공적 결과로 보이며, 생물학적 근거는 없습니다. 같은 응고 질환 계열(헤파린 보조인자 2 결핍증, 인자 5 과잉, 혈전성향증)이 상위에 몰려 있는 것도 이러한 해석을 뒷받침합니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

항트롬빈 결핍증 2형에 대한 관련 문헌이 없습니다.

참고로 2순위 이하 예측 중 형질세포 골수종(plasma cell myeloma)에서는 아래 5편이 검색되었으나, 모두 난소암 맥락의 일반 리뷰로 골수종에 특화된 자료는 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [41151612](https://pubmed.ncbi.nlm.nih.gov/41151612/) | 2025 | Review | Dtsch Med Wochenschr | 면역종양학의 최신 치료 동향. 백금 저항성 난소암에 대한 이 약의 유럽 승인 언급 |
| [42828635](https://pubmed.ncbi.nlm.nih.gov/42828635/) | 2026 | Review | Int J Clin Oncol | 일본 PMDA의 항암제 승인 및 사용상 주의사항 개정 현황 (이 약 포함) |
| [38146364](https://pubmed.ncbi.nlm.nih.gov/38146364/) | 2023 | Review | Front Immunol | 난소암 CAR-T 면역치료 개관 |
| [34683998](https://pubmed.ncbi.nlm.nih.gov/34683998/) | 2021 | Review | Pharmaceutics | 부인과 악성종양에서 항체-항종양제 접합체의 현황과 전망 |
| [36618922](https://pubmed.ncbi.nlm.nih.gov/36618922/) | 2022 | Review | Front Pharmacol | 부인과 암에서 ADC 단독 또는 면역치료 병용 요법 리뷰 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202503327 | 엘라히어주(미르베툭시맙소라브탄신) | 주사제 (무색투명 바이알) | 허가 적응증 원문은 식약처 허가사항 링크로만 확인 가능 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (항체-약물 접합체, 미세소관 억제 payload DM4) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요 (혈구감소증 위험이 있어 감염 위험을 높일 수 있음) |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC, 안과 검진 (각막 독성 보고됨; 단기 국소 스테로이드로 호전 가능) |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

- **약물 상호작용**: 이번 조회에서 병용 약물과의 상호작용은 확인되지 않았으며, 표적(FRα) 결합 정보만 확인되었습니다.
- **기타**: 약물 유발 안구(각막) 독성이 보고되어 있습니다.

그 외 경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
항트롬빈 결핍증 2형에 대한 예측은 모델 점수만 있을 뿐 임상시험과 문헌이 전혀 없고(L5), 약물의 작용 기전과도 맞지 않습니다. 또한 세포독성 ADC를 비악성 유전성 응고 질환에 사용하는 것은 위험 대비 이익 측면에서 정당화하기 어렵습니다. 같은 이유로 다른 상위 예측(헤파린 보조인자 2 결핍증, 인자 5 과잉, 혈전성향증 등)도 모두 보류가 적절합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고, 금기, 적응증 원문) 확보 및 안전성 검토
- 상세한 약물 작용 기전(MOA) 데이터 보완
- 해당 질환에서 FRα 관련 생물학적 근거를 보여주는 전임상 연구
- 형질세포 골수종 등 종양성 질환을 검토하려면 먼저 FRα 발현 여부 검증
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

