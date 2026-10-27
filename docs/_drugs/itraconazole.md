---
layout: default
title: Itraconazole
parent: 모델 예측만 (L5)
nav_order: 444
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Itraconazole: 예측 신규 적응증 폐포자충증 (Pneumocystosis) (근거 수준 L5). 기존 적응증: 허가증에 적응증 원문이 아닌 링크만 수록되어 있어 확인 불가 (아졸계 항진균제)"
monitor_inn: "ITRACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
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

## Itraconazole: 진균 감염에서 폐포자충증(Pneumocystosis)으로
{: .text-alpha }

## 한 문장 요약

Itraconazole은 아졸계 항진균제로, 한국에서 진균 감염 치료에 사용되고 있습니다.
TxGNN 모델은 **폐포자충증(Pneumocystosis)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이며 **문헌 18편**은 대부분 일반 리뷰나 증례 보고로 직접적인 근거로 보기 어렵습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가증에 적응증 원문이 아닌 링크만 수록되어 있어 확인 불가 (아졸계 항진균제) |
| 예측 신규 적응증 | 폐포자충증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.34% |
| 근거 수준 | L5 (모델 예측 중심, 직접적인 임상 연구 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 데이터베이스에 없습니다. 일반적으로 itraconazole은 진균의 lanosterol 14-alpha-demethylase(CYP51)를 억제하여 에르고스테롤 합성을 차단하는 아졸계 항진균제로 알려져 있습니다.

그러나 이 기전은 폐포자충증에는 잘 맞지 않습니다. *Pneumocystis jirovecii*는 세포막의 주요 스테롤이 에르고스테롤이 아닌 콜레스테롤이어서 아졸계 약물의 활성이 제한적일 것으로 예상됩니다. 높은 TxGNN 점수는 히스토플라스마증, 아스페르길루스증 등 다른 항진균 적응증과의 네트워크 근접성을 반영했을 가능성이 크며, 폐포자충증에 대한 검증된 기전을 뜻하지는 않습니다.

표준 치료는 trimethoprim-sulfamethoxazole이며, 대체 약물로 pentamidine, atovaquone, primaquine-clindamycin이 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

제공된 문헌은 대부분 HIV, 이식, 호중구감소증 환자의 기회감염에 관한 일반 리뷰이며, itraconazole은 주로 다른 진균(히스토플라스마 등)과 관련해 언급됩니다. 폐포자충증에 itraconazole이 효과가 있음을 직접 보여주는 연구는 확인되지 않았습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | 무작위 대조 임상시험(제3상, 분류 미확정) | HIV Medicine | HIV 감염 환자에서 itraconazole 캡슐의 심부 진균 감염 예방 효과를 평가한 이중맹검 위약대조 시험 |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | 항진균제 등 항감염제의 폐 상피 내층액 침투에 관한 고찰 |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | HIV 환자의 기회감염 1차·2차 예방 |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clinical Infectious Diseases | 호중구감소성 발열의 항균 예방요법. TMP-SMX가 폐포자충 폐렴 예방에 매우 효과적임 |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | *Pneumocystis carinii*를 포함한 전신 원충 감염의 치료 및 예방 |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | 폐이식 후 감염의 예방, 식별 및 치료 |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | 골수이식 수혜자의 감염 예방 및 치료 |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | 신장이식 후 침습성 진균 감염의 단일 기관 경험 |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Case series | Medicine | AIDS에서의 파종성 히스토플라스마증 임상 소견, 진단 및 치료 |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Frontiers in Immunology | STAT1 변이 소아의 *T. marneffei*와 *P. jirovecii* 동시 감염 |

## 한국 시판 정보

허가증에는 적응증 원문이 아닌 허가사항 PDF 링크만 수록되어 있어 적응증 요약은 제공할 수 없습니다. 주요 허가 5건은 다음과 같습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202105228 | 스포라녹스캡슐 (한국얀센) | 캡슐 | 허가사항 참조 |
| 201402364 | 이트릭스정 (한국휴텍스제약) | 필름코팅정 | 허가사항 참조 |
| 201405281 | 씨코나졸정 (씨엠지제약) | 필름코팅정 | 허가사항 참조 |
| 200003111 | 이트라정100밀리그램 (한미약품) | 필름코팅정 | 허가사항 참조 |
| 200301285 | 스파졸캡슐 (한국유나이티드제약) | 캡슐 | 허가사항 참조 |

전체 20건 모두 유효한 단일제 허가이며, 이 중 일부는 수출용입니다.

## 안전성 고려사항

허가사항 기반의 경고 및 금기 정보는 확보되지 않았으므로 허가사항을 참조하세요.

- **지식 그래프 기반 금기 관련 질환(허가사항 문구 아님)**: QT 연장 증후군, torsades de pointes, 울혈성 심부전, 심근병증, 간질환 및 약물 유발 간손상, 신장 질환, 만성 폐쇄성 폐질환, 말초신경병증, 관상동맥질환, 청력 소실 등
- **약물 상호작용**(총 100건 조회, 일부 표시):
  - 주요(Major): Loperamide, Triamcinolone, Budesonide
  - 중등도(Moderate): Famotidine, Ranitidine, Omeprazole, Rabeprazole, Cimetidine, Dexamethasone, Hydrocortisone, Betamethasone, Aprepitant, Alosetron
  - 경미(Minor): Metformin, Pioglitazone, Chlorpropamide, Amphotericin B

위산억제제(H2 차단제, PPI)와는 흡수 저하 가능성이 있어 투여 시 주의가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
폐포자충증에 대한 임상시험이 없고 문헌도 직접적인 근거가 없으며, *Pneumocystis*의 세포막 구성상 아졸계 기전이 잘 맞지 않습니다. 높은 TxGNN 점수만으로는 진행하기 어려우며, 이미 확립된 표준 치료(TMP-SMX 등)가 있습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기 포함) 확보 및 분석 (현재 안전성 선별 진행을 막는 항목)
- 작용 기전(MOA) 데이터 보완
- *Pneumocystis*에 대한 itraconazole의 전임상(in vitro/in vivo) 활성 근거
- 표준 치료 불응·불내성 환자 등 특정 집단에 대한 타당성 검토
- 이후 소규모 탐색적 임상 연구 설계 여부 판단
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

