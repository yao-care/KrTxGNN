---
layout: default
title: Zaltoprofen
parent: 僅模型預測 (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
---

# Zaltoprofen
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

# Zaltoprofen: 소염진통제에서 류마티스 관절염으로

## 한 문장 요약

Zaltoprofen은 비선택적 COX-1/COX-2 억제 기전을 가진 NSAID 계열 약물로, 해외에서는 만성 염증성 동통·골관절염 등에 사용되어 온 것으로 문헌에 보고되어 있습니다.
TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측하며, 현재 등록된 임상시험은 없으나 **7편의 관련 문헌**(장기 추적 코호트 연구 1건 포함)이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 정보 없음 (한국 미출시로 허가 적응증 자료 없음, 문헌상 만성 염증성 동통·골관절염 사용 보고) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 99.92% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Proceed with Guardrails |

---

## 이 예측이 타당한 이유는?

DrugBank 공식 MOA 데이터는 현재 확보되지 않았습니다(자료 공백). 다만 수집된 문헌에 따르면 Zaltoprofen은 **비선택적 COX-1/COX-2 억제제 NSAID**로, COX 선택성 비교 연구(PMID 9831331)에서 diclofenac·loxoprofen과 유사한 중등도 COX-2 선택성을 보이는 것으로 보고되어, 기존에 류마티스 관절염 치료에 쓰이는 NSAID 계열(diclofenac, loxoprofen 등)과 동일한 작용 범주에 속합니다.

기전 연구에서는 Zaltoprofen을 포함한 NSAID가 류마티스 관절염 활막세포(synovial cell)에서 PPAR-γ 활성화를 통해 세포자멸사를 유도하는 것으로 나타나(PMID 12065695), 단순 진통 효과를 넘어 활막 증식 억제 기전 가능성도 제시됩니다. 동물 실험에서는 아쥬반트 관절염 모델에서 예방적·치료적 항염 효과가 확인되었고(PMID 3566842), 최근 연구에서는 관절염 모델 마우스에서 경구 투여 시 피부 건조 등 RA 동반 증상 완화 효과도 보고되었습니다(PMID 36170456).

무엇보다 1998년 다기관 코호트 연구(PMID 9704197)에서 류마티스 관절염 환자를 대상으로 Zaltoprofen의 장기 유효성·안전성이 실제로 평가된 바 있어, 이번 TxGNN 예측은 완전히 새로운 가설이라기보다는 **기존에 보고된 임상 경험을 뒷받침하는 방향**에 가깝습니다.

---

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9831331](https://pubmed.ncbi.nlm.nih.gov/9831331/) | 1998 | 리뷰 | Inflamm Res | RA 환자의 NSAID 유발 위장관 부작용 원인인 COX 선택성 비교, Zaltoprofen은 loxoprofen·ibuprofen과 유사한 중등도 COX-2 선택성 |
| [9704197](https://pubmed.ncbi.nlm.nih.gov/9704197/) | 1998 | 코호트연구 | Curr Med Res Opin | RA 환자 대상 다기관 장기 투여 연구, 악력·적혈구침강속도·조조강직 등 지표로 유효성·내약성 평가 |
| [12065695](https://pubmed.ncbi.nlm.nih.gov/12065695/) | 2002 | 기전연구 | J Pharmacol Exp Ther | NSAID가 RA 활막세포에서 PPAR-γ 활성화를 통해 세포자멸사 유도, 항염 기전 이상의 작용 가능성 제시 |
| [36170456](https://pubmed.ncbi.nlm.nih.gov/36170456/) | 2022 | 기전연구 | Cutan Ocul Toxicol | 콜라겐유발 관절염 모델 마우스에서 Zaltoprofen 경구 투여가 RA 동반 피부 건조 증상을 완화 |
| [25903196](https://pubmed.ncbi.nlm.nih.gov/25903196/) | 2015 | 기전연구 | Chirality | Zaltoprofen이 RA·골관절염·만성 염증성 통증에 임상적으로 사용됨을 언급, UGT 효소 억제능의 광학이성질체 차이 분석 |
| [3566842](https://pubmed.ncbi.nlm.nih.gov/3566842/) | 1986 | 전임상연구 | Arzneimittelforschung | 쥐 아쥬반트 관절염 모델에서 예방적·치료적 항염 효과, indomethacin·pranoprofen 대비 우수한 억제 효과 |
| [14739775](https://pubmed.ncbi.nlm.nih.gov/14739775/) | 2003 | 증례보고 | Arerugi | 쇼그렌증후군 환자에서 Zaltoprofen 투여 후 무균성 수막염 발생 증례 (안전성 신호) |

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> 참고: 증례보고(PMID 14739775)에서 Zaltoprofen 투여와 연관된 무균성 수막염 사례가 보고된 바 있어, 자가면역질환(쇼그렌증후군 등) 병력이 있는 환자에서는 주의가 필요할 수 있습니다.

---

## 결론 및 다음 단계

**결정: Proceed with Guardrails**

**사유:**
류마티스 관절염에 대한 Zaltoprofen의 예측은 TxGNN 점수(99.92%)뿐 아니라 실제 장기 코호트 연구와 기전 연구로 일부 뒷받침되어 근거 수준 L3(S2 단계)로 평가됩니다. 다만 무작위대조시험(RCT) 부재, 한국 내 허가·시판 이력 없음, 그리고 TFDA/한국 규제 안전성 자료의 **차단급(Blocking) 결측**으로 인해 즉시 진행(Go)보다는 제한적 조건하 진행이 적절합니다.

**진행하려면 필요한 것:**
- 한국(또는 원 허가국) 공식 안전성 자료 확보 — 경고·금기 사항 PDF 다운로드 및 파싱 (DG001, Blocking)
- DrugBank API를 통한 공식 작용기전(MOA) 데이터 확보 (DG002, High)
- 류마티스 관절염 적응증에 대한 전향적 대조시험 설계 검토
- 참고: 동일 예측 세트 내 건염(tendinitis, rank 9)은 RCT 1건(PMID 30738433)으로 근거 수준 L2로 더 강하게 나타나, 병행 검토 가치가 있음
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

