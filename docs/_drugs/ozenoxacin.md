---
layout: default
title: Ozenoxacin
parent: 모델 예측만 (L5)
nav_order: 572
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Ozenoxacin: 예측 신규 적응증 말라리아 (Malaria) (근거 수준 L5). 기존 적응증: 1. 유효균종 황색포도상구균(S. aureus), 화농성연쇄상구균(S. pyogenes) 2. 적응증…"
monitor_inn: "Ozenoxacin"
predicted_indications: ["malaria"]
---

# Ozenoxacin
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

## Ozenoxacin: 국소 항균 치료에서 말라리아로
{: .text-alpha }

## 한 문장 요약

Ozenoxacin은 비불소화 퀴놀론 계열의 국소 항균제로, 원래 피부 세균 감염 치료에 사용되는 크림제입니다.
TxGNN 모델은 **말라리아(Malaria)**에 효과가 있을 수 있다고 예측하지만, 현재 이 방향을 지지하는 **임상시험과 문헌은 없습니다**. 모델 예측만 있는 단계(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 유효균종 황색포도상구균(S. aureus), 화농성연쇄상구균(S. pyogenes) 2. 적응증 농가진의 단기 국소 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202107880/EE)) |
| 예측 신규 적응증 | 말라리아 (Malaria) |
| TxGNN 예측 점수 | 0.9916 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 1건 / 전체 1건) |
| 허가증 수 | 1건 (유효 1건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

ChEMBL(EMBL-EBI)에 등록된 Ozenoxacin의 작용 기전(비공식 번역): “DNA 자이레이스 억제제; 토포이소머라제 IV 억제제; DNA 토포이소머라제 IV 억제제”. 영어 원문: "DNA gyrase inhibitor; Topoisomerase IV inhibitor; DNA topoisomerase IV inhibitor" ([ChEMBL CHEMBL3990047 (ozenoxacin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3990047), CC BY-SA 3.0; 확인일 2026-11-19). 일반적으로 ozenoxacin은 세균의 DNA gyrase와 topoisomerase IV를 억제하는 비불소화 퀴놀론 계열 국소 항균제로 알려져 있습니다.

말라리아 원충(Plasmodium)에는 아피코플라스트(apicoplast)에 위치한 DNA gyrase가 있어, 다른 퀴놀론 계열처럼 이론적인 연결고리는 존재합니다.

다만 ozenoxacin은 국소 투여용으로 전신 노출이 거의 없어 항말라리아 활성을 기대하기 어렵습니다. 0.9916이라는 높은 TxGNN 모델(딥러닝) 점수는 모델이 관련 질환 사이에서 학습한 유사성을 반영할 뿐, 생물학적 근거나 실제 효능을 뜻하지 않습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 202107880 | 오자넥스크림(오제녹사신) | 연한 노란색의 균질한 크림제 | 허가 문서 링크만 확인됨 (허가 문서 참조) |

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 기타 예측 적응증 (참고)

TxGNN이 예측한 다른 후보도 모두 L5이며 Hold 판정입니다. 이 가운데 기전적 근거가 일부라도 언급되는 것은 리슈마니아증뿐이며, 이마저도 가설 수준입니다.

| 순위 | 예측 질환 | TxGNN 점수 | 기전적 평가 |
|-----|---------|-----------|-----------|

## 결론 및 다음 단계

**결정: Hold**

**사유:**
말라리아에 대한 임상시험과 문헌이 없고, 국소 투여 제제여서 전신 노출이 미미하므로 항말라리아 효과를 기대하기 어렵습니다. 높은 TxGNN 점수만으로는 진행 근거가 되지 않습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서)의 적응증, 경고 및 금기 정보 확보
- DrugBank 기반 작용 기전(MOA) 데이터 보완
- Plasmodium에 대한 시험관 내 활성 및 약동학(전신 노출) 데이터
- 투여 경로 적합성 평가 (현재 국소 크림제만 허가)
- 리슈마니아증 등 피부 관련 질환에 대한 전임상 연구 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 (2026-11-20 수정, 이전 판은 기록에 보존) | [ChEMBL CHEMBL3990047 (ozenoxacin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3990047) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

