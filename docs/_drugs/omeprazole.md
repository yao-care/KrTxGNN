---
layout: default
title: Omeprazole
parent: 모델 예측만 (L5)
nav_order: 564
evidence_level: L5
indication_count: 1
monitor_inn: "OMEPRAZOLE"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-20
description: "Omeprazole: 예측 신규 적응증 십이지장 폐쇄 (duodenal obstruction) (근거 수준 L5). 기존 적응증: MFDS 허가사항(PDF) 참조"
---

# Omeprazole
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Omeprazole: 양성자펌프 억제제 → 십이지장 폐쇄 (duodenal obstruction)
{: .text-alpha }

## 한 문장 요약

Omeprazole은 위산 분비를 억제하는 양성자펌프 억제제 계열 약물입니다. TxGNN 모델은 **십이지장 폐쇄(duodenal obstruction)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 연구한 임상시험이나 문헌은 확인되지 않았습니다. 현재 간접적으로 관련된 **1건의 임상시험**과 **5편의 문헌**만 있어 근거는 매우 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200301653/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199202074/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201504046/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199302187/EE); [MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201504045/EE);  |
| 예측 신규 적응증 | 십이지장 폐쇄 (duodenal obstruction) |
| TxGNN 예측 점수 | 0.9964 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 9건 / 전체 10건) |
| 허가증 수 | 10건 (유효 9건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Omeprazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “오메프라졸은 위 벽세포 분비면의 H + /K + ATPase 효소계를 특이적으로 억제하여 위산 분비를 억제하는 위산 분비 억제 화합물인 치환 벤즈이미다졸계에 속한다. 이 효소계는 위 점막 내 산(양성자) 펌프로 간주되므로, 오메프라졸은 산 생성의 최종 단계를 차단한다는 점에서 위산 펌프 억제제로 특징지어져 왔다.” 영어 원문: "Omeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H + /K + ATPase enzyme system at the secretory surface of the gastric parietal cell. Because this enzyme system is regarded as the acid (proton) pump within the gastric mucosa, omeprazole has been characterized as a gastric acid-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Prilosec (omeprazole magnesium) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b6761f84-53ac-4745-a8c8-1e5427d7e179), 버전 2024-03-19; 확인일 2026-11-19). 일반적으로 omeprazole은 위산 분비를 줄이는 약물로 알려져 있습니다.

십이지장 폐쇄는 대개 소화성 궤양의 흉터·협착, 크론병, 악성 종양 등으로 생기는 기계적 질환입니다. 궤양 치유와 염증성 부종 감소를 통해 궤양 관련 협착에는 간접적으로 도움이 될 수 있습니다. 그러나 이미 섬유화되었거나 구조적으로 굳어진 폐쇄는 해소하지 못하며, 이 경우 내시경 확장술이나 수술이 필요합니다.

높은 예측 점수는 소화성 궤양과의 네트워크상 근접성을 반영했을 가능성이 크며, 폐쇄 자체에 대한 직접적인 치료 효과를 뜻하지는 않습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00557921](https://clinicaltrials.gov/study/NCT00557921) | Phase 3 | 조기 종료 | 5000 | 아스피린 병용 환경에서 clopidogrel+omeprazole 복합제와 clopidogrel을 비교해 위장관 출혈·궤양 질환 감소를 평가한 시험. 십이지장 폐쇄를 직접 평가한 근거는 없음 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [7795284](https://pubmed.ncbi.nlm.nih.gov/7795284/) | 1995 | 임상/관찰 (증례) | Ital J Gastroenterol | 십이지장 구부 협착을 동반한 궤양 환자에서 omeprazole 4개월은 내시경 소견을 바꾸지 못했고, H. pylori 제균 치료 후 궤양과 협착이 호전됨 |
| [1475769](https://pubmed.ncbi.nlm.nih.gov/1475769/) | 1992 | Review | Ther Umsch | 소화성 궤양 진단 리뷰. 위출구 폐쇄가 의심될 때 상부 위장관 조영술이 유용할 수 있음 |
| [9005711](https://pubmed.ncbi.nlm.nih.gov/9005711/) | 1996 | Review (증례 포함) | Acta Med Port | 위십이지장 크론병 사례. prednisolone과 omeprazole이 효과가 없어 위출구 폐쇄 해소에 수술이 필요했음 |
| [9306611](https://pubmed.ncbi.nlm.nih.gov/9306611/) | 1997 | Case report | Surg Today | 십이지장 크론병으로 지속적인 위출구 폐쇄가 생겨 수술로 치료한 사례 |
| [8165479](https://pubmed.ncbi.nlm.nih.gov/8165479/) | 1994 | Case report | Surg Endosc | 위장문합술 후 거대 변연 궤양 사례. 폐쇄 등의 합병증이 보고됨 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199202074 | 라메졸캡슐20밀리그램 | 장용성 과립 충진 경질캡슐 | 허가 적응증 텍스트 미기재 |
| 199302187 | 오메드정20밀리그램 | 장용제피정제 | 허가 적응증 텍스트 미기재 |
| 199900120 | 오엠피정40밀리그램 | 장용필름코팅정제 | 허가 적응증 텍스트 미기재 |
| 199200236 | 오엠피정20밀리그램 | 장용필름코팅정제 | 허가 적응증 텍스트 미기재 |
| 199902308 | 오메드정10밀리그램 | 장용제피정제 | 허가 적응증 텍스트 미기재 |

허가 10건의 목록이며 위에는 주요 5건만 제시했습니다.

## 안전성 고려사항

- **약물 상호작용**: 조회 결과 총 100건이 확인되었으며, 주요 항목으로는 다음이 있습니다.
  - 중대(Major): Acalabrutinib, Atazanavir
  - 중등도(Moderate): Hydrochlorothiazide, Alprazolam, Amphotericin B, Amikacin, Amphetamine, Anagrelide, Fenofibrate, Apalutamide, Armodafinil, Atorvastatin 등
  - 경미(Minor): Lidocaine, Nifedipine, Ambrisentan, Acetylsalicylic acid

주요 경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
십이지장 폐쇄를 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 폐쇄는 기계적 질환이어서 omeprazole은 궤양 관련 부종을 줄이는 정도의 간접적 역할에 그칠 가능성이 높고, 사례 보고에서는 효과가 없었습니다.

**진행하려면 필요한 것:**
- 십이지장 폐쇄 환자를 직접 대상으로 한 임상 또는 관찰 연구 근거
- 궤양 관련 협착과 기타 원인(크론병, 악성 종양)을 구분한 대상군 정의
- 허가사항의 경고·금기 정보 확보 및 작용 기전 자료 보완

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Prilosec (omeprazole magnesium) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b6761f84-53ac-4745-a8c8-1e5427d7e179) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

