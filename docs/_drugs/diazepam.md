---
layout: default
title: Diazepam
parent: 모델 예측만 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Diazepam: 예측 신규 적응증 불면증 (Insomnia) (근거 수준 L5). 기존 적응증: 허가 적응증 본문은 허가사항 문서 링크로만 제공되어 이 보고서에서 요약하지 못했습니다"
monitor_inn: "Diazepam"
predicted_indications: ["insomnia (disease)", "cauda equina syndrome", "sleep disorder, initiating and maintaining sleep", "attention deficit hyperactivity disorder, inattentive type", "hallucinogen abuse", "antidepressant type abuse", "barbiturate abuse", "specific developmental disorder"]
---

# Diazepam
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

# Diazepam: 기존 허가 적응증에서 불면증으로

## 한 문장 요약

Diazepam은 한국에서 8건의 단일제 허가를 보유한 벤조디아제핀계 약물입니다. TxGNN 모델은 **불면증(Insomnia)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건**입니다. 문헌 18편은 대부분 총설, 한약·침 연구, 동물 연구이고, 불면증에서 diazepam 자체를 검증한 근거는 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문은 허가사항 문서 링크로만 제공되어 이 보고서에서 요약하지 못했습니다. |
| 예측 신규 적응증 | 불면증 (Insomnia) |
| TxGNN 예측 점수 | 99.9997% |
| 근거 수준 | L4 (기전 및 전임상 수준, 불면증 대상 임상시험 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 8건 (모두 유효, 단일제) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Diazepam은 GABA-A 수용체의 양성 알로스테릭 조절제(PAM)입니다. 억제성 신경전달을 강화하여 진정·수면 유도 효과를 냅니다. 약물 작용 기전 데이터베이스의 상세 정보는 이번 자료에 포함되지 않았고, 위 기전은 예측 근거 분석에서 가져온 내용입니다.

벤조디아제핀계 약물은 이미 단기 불면증 치료에 쓰여 왔으므로, TxGNN의 예측은 기전상 일관됩니다. 같은 기전을 가진 다른 수면제와 비교한 오래된 이중맹검 연구도 있습니다. 1981년 연구에서는 lormetazepam 1 mg이 diazepam 5 mg보다 입면 시간 단축 등에서 우수했습니다.

다만 이 예측은 새로운 발견이라기보다 기존 임상 지식에 가깝습니다. 불면증에서 diazepam의 효능을 직접 검증한 최신 임상시험은 이번 자료에 없습니다. 장기 사용 시 수면 구조 변화, 의존성, 인지 저하 등 위험을 다룬 문헌이 더 많이 확인됩니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

불면증과 직접 관련된 무작위 대조시험(RCT)은 확인되지 않았습니다. 아래는 관련성이 높은 순으로 정리한 목록입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | 이중맹검 비교연구 | J Int Med Res | 불면 외래환자 100명에서 lormetazepam 1 mg과 diazepam 5 mg을 7일간 비교했고, lormetazepam이 입면 시간 단축 등에서 유의하게 우수했습니다. |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorg Chem | 불면증을 포함한 신경계 질환에서 GABA-A 수용체 조절제의 임상 적용을 고찰했습니다. Diazepam은 대표적 PAM이며 진정 등 부작용이 따릅니다. |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | 메타분석 | Acta Pharm | 만성 비전염성 질환이 있는 고령 환자에서 신경안정제의 용량, 결과, 이상반응을 평가했습니다. |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | 코호트 | Cell Mol Biol Lett | 벤조디아제핀과 Z-drug의 장기 사용이 유방암 위험을 높일 수 있다는 임상 근거와 분자 기전을 보고했습니다. |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | 항불안제의 약동학을 고찰했습니다. |
| [31770357](https://pubmed.ncbi.nlm.nih.gov/31770357/) | 2019 | Review | Med Lett Drugs Ther | 대마·카나비노이드에 관한 총설로, 불면증과의 연관성은 간접적입니다. |
| [35196378](https://pubmed.ncbi.nlm.nih.gov/35196378/) | 2022 | 비무작위 중재연구 | Fam Pract | 일차의료 현장에서 만성 벤조디아제핀 사용 중단을 지원하는 중재를 평가했습니다. |
| [16671957](https://pubmed.ncbi.nlm.nih.gov/16671957/) | 2006 | 처방 행태 조사 | Fundam Clin Pharmacol | 다카르 의사들의 벤조디아제핀 처방 습관과 지식을 조사했고, 명확한 적응증 없이 사용되는 경향을 지적했습니다. |
| [32623439](https://pubmed.ncbi.nlm.nih.gov/32623439/) | 2020 | 동물 연구 | Med Sci Monit | 불면 쥐 모델에서 berberine의 효과를 평가했고, diazepam은 대조약으로 쓰였습니다. |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | 동물 연구 | J Pharm Biomed Anal | 불면 쥐 모델에서 Naoling Pian의 대사체 변화를 평가했고, diazepam은 양성 대조약이었습니다. |

## 한국 시판 정보

허가 적응증 본문은 허가사항 문서 링크로만 제공되어, 아래 표에는 링크로 표시했습니다. 허가증 8건 중 5건을 나열합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198501812 | 명인디아제팜정5밀리그램 | 미황색 원형 정제 | [허가사항 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198501812/EE) |
| 198501813 | 명인디아제팜정10밀리그램 | 청색 원형 정제 | [허가사항 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198501813/EE) |
| 197900546 | 삼진디아제팜주 | 앰플 주사제 | [허가사항 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197900546/EE) |
| 197700525 | 대원디아제팜정2밀리그램 | 백색 원형 정제 | [허가사항 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/197700525/EE) |
| 200700501 | 바리움정5밀리그람(디아제팜) | 미황색 원형 정제 | [허가사항 문서 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200700501/EE) |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 20건을 확인했습니다.
  - **Major**: Morphine (호흡억제·과진정 위험 등 병용 시 주의 필요)
  - **Moderate**: Bupropion, Aprepitant, Omeprazole, Esomeprazole, Cimetidine, Clarithromycin, Cisapride, Clotrimazole, Miconazole, Dronabinol, Metoclopramide
  - **Minor**: Dexamethasone, Betamethasone, 제산제류 (수산화마그네슘, 산화마그네슘, 탄산마그네슘, 수산화알루미늄, 탄산칼슘, magaldrate)
- **문헌에서 확인된 신호**: 장기 사용과 관련해 수면 구조 변화, 의존성, 인지 저하, 고령자의 낙상 위험이 보고되었습니다. 유방암 위험 증가 가능성을 다룬 코호트 연구도 있습니다.

경고 및 금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
GABA-A 기전상 불면증에 대한 예측은 타당하지만, 불면증에서 diazepam을 직접 검증한 임상시험이 없고 문헌도 간접 근거 중심입니다. 장기 사용의 위해 신호도 반복해서 확인되어 현 시점에서는 진행을 보류합니다.

**진행하려면 필요한 것:**
- 한국 허가사항(적응증, 경고, 금기) 원문을 확인하여 불면증이 이미 허가 범위에 포함되는지 검토
- 불면증에서 diazepam의 용량, 투여 기간, 효능을 비교하는 임상시험 또는 체계적 문헌고찰 확보
- 약물 작용 기전 데이터베이스 정보 보강
- 고령자, 간 기능 저하 환자, 병용 약물(특히 opioid) 대상 안전성 관리 계획 수립
- 같은 예측 목록의 알코올 금단 섬망과 불안은 근거 수준이 L2로 더 높지만, 이미 확립된 임상 용도일 가능성이 있어 허가 상태를 먼저 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

