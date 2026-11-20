---
layout: default
title: Ivermectin
parent: 모델 예측만 (L5)
nav_order: 445
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-15
description: "Ivermectin: 예측 신규 적응증 외음질 칸디다증 (vulvovaginal candidiasis) (근거 수준 L5). 기존 적응증: 1. 분선충에 의한 장관계의 분선충증(즉, 비전염성)의 치료 2. 회선사상충에 의한 회선사상충증의…"
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "congenital candidiasis", "candida glabrata", "neonatal candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
---

# Ivermectin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Ivermectin: 구충·항기생충 치료에서 외음질 칸디다증으로
{: .text-alpha }

## 한 문장 요약

Ivermectin은 한국에서 경구 정제(수출용)와 1% 크림 형태로 허가된 항기생충제입니다.
TxGNN 모델은 **외음질 칸디다증(vulvovaginal candidiasis)**에 효과가 있을 수 있다고 예측하지만, 이 예측을 직접 뒷받침하는 **임상시험은 0건**, **문헌도 0건**입니다. 현재는 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 분선충에 의한 장관계의 분선충증(즉, 비전염성)의 치료 2. 회선사상충에 의한 회선사상충증의 치료(회선사상충 성충 치료에는 효과없음.) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200500039/EE)) |
| 예측 신규 적응증 | 외음질 칸디다증 (vulvovaginal candidiasis) |
| TxGNN 예측 점수 | 0.9995 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 3건 / 전체 3건) |
| 허가증 수 | 3건 (유효 3건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ivermectin 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “인간 간 마이크로솜 및 재조합 CYP450 효소를 이용한 시험관 내 연구에서 ivermectin은 주로 CYP3A4에 의해 대사되는 것으로 나타났다.” 영어 원문: "In vitro studies using human liver microsomes and recombinant CYP450 enzymes have shown that ivermectin is primarily metabolized by CYP3A4." ([DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd), 버전 2024-09-20; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면 ivermectin은 무척추동물의 글루탐산 의존성 염화물 채널에 작용하는 항기생충제입니다.

진균에는 이 채널이 없어 Candida에 대한 약리학적 연결고리가 확인되지 않습니다. 높은 예측 점수는 실제 약효보다는 항진균제와의 네트워크 근접성을 반영했을 가능성이 큽니다. 따라서 기전상 타당하다고 보기 어렵습니다.

상위 10개 예측은 대부분 칸디다증과 외음부·질 질환 계열이며, 모두 직접적인 근거가 없습니다. 그중 일부는 다음과 같이 평가됩니다.
- **항문생식기 HPV 감염**: 전임상 연구에서 광범위한 항바이러스 활성(importin α/β 매개 핵 수송 억제 등)이 보고되었으나, 효과를 내는 농도가 사람이 도달 가능한 혈장 농도를 대체로 초과하고 HPV 임상 근거도 없습니다.
- **폐경 후 위축성 질염**: 에스트로겐 결핍이 원인이므로 ivermectin과 연관된 기전이 없습니다.
- **침습성 칸디다증**: 효과적인 승인 항진균제(에키노칸딘, 아졸)가 있어 재창출 근거가 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

외음질 칸디다증과 직접 관련된 문헌은 없습니다. 하위 예측 적응증에서 검색된 문헌 2편은 모두 칸디다증에 대한 효능 근거가 아닙니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/) | 2022 | 증례 보고 | BMJ Case Reports | 장기 코르티코스테로이드 치료 후 파종성 분선충증 사례로, 식도 칸디다증과 무관 |
| [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/) | 1999 | 증례 시리즈 | Australas J Dermatol | 면역저하 소아 2명의 가피성 옴에 경구 ivermectin이 효과적이었으며, 소아 내약성 참고 정보만 제공 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200500039 | 이버튼정3밀리그램(수출용) | 정제 (흰색 원형) | 허가사항 참조 |
| 200500040 | 이버튼정6밀리그람(수출용) | 정제 (흰색 원형) | 허가사항 참조 |
| 201605345 | 수란트라크림1% | 크림 (흰색~연한 노란색) | 허가사항 참조 |

## 안전성 고려사항

- **지식그래프상 금기 질환**: loiasis(로아사상충증), filariasis(사상충증)
- **약물 상호작용**: 총 100건이 확인되었습니다. 그중 일부 주요 항목은 다음과 같습니다.
  - 중등도: aprepitant, clarithromycin, ethanol, cobicistat, deferasirox, warfarin, dicoumarol, fostamatinib, iodide I-123/I-131, abametapir(국소)
  - 등급 미확인: omeprazole, lansoprazole, prednisone, prednisolone, dexamethasone, ranitidine, famotidine, ursodeoxycholic acid, heparin

허가 문서의 경고 및 금기 정보는 확인되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
예측은 모델 점수에 한정되며 임상시험과 직접 문헌이 없습니다. 또한 ivermectin이 진균에 작용하는 기전이 확인되지 않고, 효과적인 승인 항진균제가 이미 존재합니다.

**진행하려면 필요한 것:**
- 허가사항(MFDS 첨부문서)의 적응증, 경고, 금기 확인
- ivermectin의 상세 작용 기전 데이터 확보
- Candida에 대한 in vitro 항진균 활성 및 도달 가능 농도 검증
- 외음질 칸디다증에 대한 전임상 또는 임상 근거 확보
- 상호작용 병용약(특히 warfarin, clarithromycin 등) 관련 안전성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

