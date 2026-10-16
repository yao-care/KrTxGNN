---
layout: default
title: Tocilizumab
parent: 모델 예측만 (L5)
nav_order: 741
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tocilizumab: 예측 신규 적응증 강직성 척추염 (Ankylosing Spondylitis) (근거 수준 L5). 기존 적응증: 류마티스 관절염 등 (문헌 기준, 한국 허가 적응증 원문은 허가사항 링크로만 제공되어 확인 필요)"
---

# Tocilizumab
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

# Tocilizumab: 류마티스 관절염에서 강직성 척추염으로

## 한 문장 요약

Tocilizumab은 IL-6 수용체를 표적으로 하는 단클론항체로, 류마티스 관절염 등 자가면역성 관절염 치료에 주로 사용되어 왔습니다.
TxGNN 모델은 **강직성 척추염(Ankylosing Spondylitis)**에 효과가 있을 수 있다고 예측하지만, 관련 Phase 3 임상시험 2건은 조기 종료되었고 효능 결과도 일관되지 않습니다.
현재 이 방향을 다루는 임상시험은 **4건**(직접 관련 2건), 문헌은 **약 20편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 류마티스 관절염 등 (문헌 기준, 한국 허가 적응증 원문은 허가사항 링크로만 제공되어 확인 필요) |
| 예측 신규 적응증 | 강직성 척추염 (Ankylosing Spondylitis) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L3 (완료된 Phase 3 RCT 없음. 조기 종료된 RCT와 체계적 문헌고찰 존재) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 5건 (모두 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 이 약의 상세한 작용 기전 데이터는 정리되어 있지 않습니다. 문헌에 따르면 tocilizumab은 인간화 항 IL-6 수용체 단클론항체로, 막결합형과 가용성 IL-6 수용체를 모두 차단하여 IL-6 신호전달을 억제합니다.

강직성 척추염 환자의 혈청과 천장관절에서 IL-6가 상승해 있다는 보고가 있어, IL-6 차단은 기전상 시도해 볼 만합니다. 류마티스 관절염, 소아 특발성 관절염 같은 다른 염증성 관절염에서 이미 효과가 입증되었다는 점도 예측을 뒷받침합니다.

그러나 실제 임상 결과는 기전적 타당성을 충분히 뒷받침하지 못했습니다. 두 Phase 3 시험은 조기 종료되었고, 초기 RCT에서는 증상 개선 효과가 제한적이었습니다. 현재 강직성 척추염 치료에서는 TNF 억제제와 IL-17 억제제가 권고되며, tocilizumab은 권고 약제가 아닙니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | 조기 종료 | 113 | TNF 억제제에 반응이 불충분한 강직성 척추염에서 tocilizumab(8 mg/kg 또는 4 mg/kg) 대 위약 비교. 이중맹검 |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | 조기 종료 | 306 | NSAID에 실패한 TNF 억제제 미사용 강직성 척추염에서 tocilizumab 대 위약 비교. 증상 및 구조적 손상 억제 평가 |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | 해당 없음 | 모집 중 | 10,000 | 한국 류마티스학회 생물학적제제 레지스트리. 실제 진료 환경의 안전성 관찰이며 효능 검증 목적은 아님 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 모집 중 | 80 | 류마티스 환자의 어깨 관절치환술 전후 면역억제제 관리 연구. tocilizumab의 강직성 척추염 효능과는 무관 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Ann Rheum Dis | BUILDER-1/2 시험. 강직성 척추염에서 tocilizumab의 단기 증상 개선 효능과 안전성 평가 |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | 체계적 문헌고찰·네트워크 메타분석 | Medicine | 강직성 척추염 생물학적제제 간 비교 효과 분석 |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | 체계적 문헌고찰 | Expert Rev Clin Immunol | 염증성 관절염에서 비생물학적 제제와 생물학적제제의 감염 위험 비교 |
| [36260501](https://pubmed.ncbi.nlm.nih.gov/36260501/) | 2022 | 체계적 문헌고찰 | RMD Open | 면역매개 염증성 질환에서 IL-6 경로 억제제의 효능과 안전성에 대한 합의문 근거 |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | 리뷰 | Inflamm Allergy Drug Targets | 강직성 척추염에서 IL-6 길항의 가능성 |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | 리뷰 | Curr Opin Rheumatol | TNF 억제제 불응 강직성 척추염의 대안 치료 |
| [25488787](https://pubmed.ncbi.nlm.nih.gov/25488787/) | 2014 | 리뷰 | Best Pract Res Clin Rheumatol | TNF 차단을 넘어선 척추관절염 치료 |
| [29278210](https://pubmed.ncbi.nlm.nih.gov/29278210/) | 2017 | 리뷰 | Curr Pharm Biotechnol | 염증성 관절염에서 생물학적제제의 역할 |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | 리뷰 | Front Immunol | 생물학적제제 사용 자가면역 관절염 환자의 결핵 위험 관리 |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | 증례 보고 | Front Med | 강직성 척추염에 속발한 AA 아밀로이드증에서 tocilizumab 치료 성공 2례 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202500309 | 앱토즈마피하주사162밀리그램 (셀트리온) | 오토인젝터 주사제 | [허가사항 링크 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500309/EE) |
| 202500308 | 앱토즈마주80밀리그램 (셀트리온) | 바이알 액상 주사제 | [허가사항 링크 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500308/EE) |
| 202403038 | 앱토즈마주 (셀트리온) | 바이알 액상 주사제 | [허가사항 링크 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202403038/EE) |
| 201202719 | 악템라주 (제이더블유중외제약) | 바이알 액상 주사제 | [허가사항 링크 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201202719/EE) |
| 201403578 | 악템라피하주사162밀리그램 (제이더블유중외제약) | 프리필드시린지, 오토인젝터 주사제 | [허가사항 링크 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201403578/EE) |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이 보고서에 정리된 데이터에 포함되어 있지 않으므로, 허가사항을 직접 참조해야 합니다.

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 주요 항목은 다음과 같습니다.
  - **Major**: Deferiprone
  - **Moderate**: Rosuvastatin, Simvastatin(스타틴 계열), Warfarin, Apixaban, Rivaroxaban, Dicoumarol(항응고제), Chloroquine, Hydroxychloroquine, Metronidazole, Tinidazole, Disulfiram, Naltrexone, Lidocaine 등
  - **Minor**: 아연 제제(황산아연, 아세트산아연, 글루콘산아연, 염화아연)
- **감염·결핵 위험**: 관련 문헌은 생물학적제제 사용 시 감염 위험 증가와 결핵 선별 검사의 필요성을 다룹니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
강직성 척추염에 대한 Phase 3 시험 2건이 모두 조기 종료되어 완료된 RCT가 없고, 효능 신호도 제한적이었습니다. 이미 TNF 억제제와 IL-17 억제제라는 확립된 치료 옵션이 있으며, 허가사항 기반 안전성 검토도 아직 이루어지지 않았습니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고, 금기, 적응증 원문) 확보 및 안전성 검토
- BUILDER-1/2 시험의 상세 결과(1차 평가변수 및 종료 사유) 재검토
- 상세 작용 기전(MOA) 데이터 보완
- TNF 억제제 불응 환자군 등 tocilizumab이 우위를 가질 수 있는 하위집단이 있는지 확인

**참고:** 같은 약물의 다른 예측 적응증 중 다관절형 소아 특발성 관절염(pJIA)은 완료된 Phase 3 위약 대조 시험(NCT00988221)이 있어 근거가 훨씬 강합니다. 이 적응증은 이미 주요 시장에서 인정된 용도로 보이므로 한국 허가사항과 대조해 확인할 필요가 있습니다.
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

