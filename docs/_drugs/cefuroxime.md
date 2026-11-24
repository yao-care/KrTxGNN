---
layout: default
title: Cefuroxime
parent: 모델 예측만 (L5)
nav_order: 198
evidence_level: L5
indication_count: 8
monitor_inn: "Cefuroxime"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy"]
last_modified_at: 2026-11-24
description: "Cefuroxime: 예측 신규 적응증 다클론성 과점성 증후군 (polyclonal hyperviscosity syndrome) (근거 수준 L5). 기존 적응증: ○ 유효균종 1) 호기성 그람양성균 황색포도구균(페니실린내성균포함, 메치실린 감수성 균주)…"
---

# Cefuroxime
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **8** 건
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

## Cefuroxime: 다클론성 과점성 증후군 (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## 한 문장 요약

Cefuroxime은 세균 세포벽 합성을 억제하는 2세대 세팔로스포린계 항생제입니다. TxGNN 모델은 **다클론성 과점성 증후군(polyclonal hyperviscosity syndrome)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0편**입니다. 기전상 연결 고리도 찾기 어려워 모델 예측만 있는 상태(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 유효균종 1) 호기성 그람양성균 황색포도구균(페니실린내성균포함, 메치실린 감수성 균주), 화농성연쇄구균, 베타용혈성 연쇄구균, 스트렙토 콕쿠스 아갈락티에(그룹B), 코아귤라제 음성 포도구균(Coagulase negative staphylococcus)(메치실린 감 수성 균주)… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201607370/EE)) |
| 예측 신규 적응증 | 다클론성 과점성 증후군 (polyclonal hyperviscosity syndrome) |
| TxGNN 예측 점수 | 0.9976 |
| 근거 수준 | L5 (모델 예측만 있음) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Cefuroxime 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “세푸록심은 세균 세포벽 합성을 억제하여 작용하는 살균제이다. 세푸록심은 그람음성균 및 그람양성균의 일부 베타-락타마제(페니실리나제 및 세팔로스포리나제 모두) 존재 하에서도 활성을 나타낸다.” 영어 원문: "Cefuroxime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefuroxime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c), 버전 2025-03-27; 확인일 2026-11-19). 알려진 정보로는 Cefuroxime이 세균 세포벽 합성을 억제하는 2세대 세팔로스포린이며, 효과는 세균 감염에 대한 항균 작용에 국한됩니다.

반면 과점성 증후군은 혈청 면역글로불린이 과다해 혈액 점도가 올라가는 혈액·면역학적 질환입니다. 세포벽 합성 억제제가 이 병태를 개선할 만한 기전은 확인되지 않습니다. 이 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아니며, 이를 뒷받침하는 임상 또는 문헌 근거도 없습니다.

## 임상시험 근거

현재 이 질환과 관련된 임상시험 등록이 없습니다.

## 문헌 근거

현재 이 질환과 관련된 문헌이 없습니다.

## 한국 시판 정보

허가 건수와 상태는 빠른 개요와 아래 표에 있습니다. 전체 20건 중 주요 5건만 나열하며, 전체 허가 수는 이보다 많을 수 있습니다. 허가 적응증은 본문이 아닌 허가사항 문서 링크로만 제공되어 요약할 수 없으므로, 해당 허가사항 문서를 참조해야 합니다.

<!-- review:begin kr-lic-20261124c-cefuroxime-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “목록에서 확인된 허가는 모두 단일 성분 제제입니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-23 데이터) 기준으로 수정했습니다: 이 사이트 자료의 성분란에는 일치한 성분만 기록되어 허가 품목별 단일 성분·복합 성분 여부를 확인할 수 없으므로, 단일·복합 표기를 빼고 건수는 쓰지 않고 빠른 개요와 「한국 시판 정보」의 표를 가리키도록 고쳤습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261124c-cefuroxime-1 -->

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 198801778 | 쎄록신주750밀리그램(세푸록심나트륨) | 흰색-엷은 황백색의 가루가 든 바이알제 | 경동제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/198801778/EE) | 유효 |
| 199100043 | 신세프주1.5그램(세푸록심나트륨) | 흰색-미황색의 가루가 든 무색투명한 바이알 주사제 | 신풍제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199100043/EE) | 유효 |
| 199401167 | 원푸록심주사750밀리그람(세푸록심나트륨) | 백색-엷은 황백색의 결정 또는 결정성 가루가 든 바이알 | 대원제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199401167/EE) | 유효 |
| 199700175 | 종근당세푸록심나트륨주750밀리그램(세푸록심나트륨)(수출명:푸록심주) | 백색 또는 엷은 황백색의 가루가 든 바이알. | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199700175/EE) | 유효 |
| 200500613 | 바이넥스세푸록심나트륨주 | 백색 내지 엷은 황색의 가루가 든 바이알 주사제 | (주)바이넥스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200500613/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

그 밖에 수출용 허가가 다수 포함되어 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 확인된 상호작용 100건 중 상위 20건이 모두 '중등도' 수준입니다.
  - 위산 억제제: 파모티딘, 라니티딘, 시메티딘, 니자티딘, 오메프라졸, 에소메프라졸, 란소프라졸, 덱스란소프라졸, 라베프라졸, 판토프라졸
  - 제산제: 수산화알루미늄, 탄산칼슘, 마갈드레이트, 탄산마그네슘, 수산화마그네슘, 산화마그네슘
  - 아미노글리코시드계 항생제: 카나마이신, 네오마이신
  - 기타: 발살라자이드

주요 경고와 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
다클론성 과점성 증후군에 대한 임상시험과 문헌이 없고, 항균제인 Cefuroxime과 이 질환을 잇는 기전도 확인되지 않아 모델 예측만 남아 있습니다. 이 예측만으로 연구나 개발을 진행할 근거가 부족합니다.

**진행하려면 필요한 것:**
- 이 질환에서 Cefuroxime의 작용을 뒷받침하는 기전 연구 또는 전임상 데이터
- 허가사항에 기재된 경고 및 금기 정보 확보
- 상세한 작용 기전(MOA) 데이터 확보

다만 이는 세균 감염이라는 약물의 기존 사용 범위와 가까운 질환이어서 새로운 재창출 신호로 보기 어렵습니다. 첫 번째 예측인 다클론성 과점성 증후군과는 별개로 평가해야 합니다.

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: cefuroxime sodium prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0a145288-733a-4966-b7ae-dc96eb103d8c) |
| 2026-11-24 | 단일·복합 표기: “목록에서 확인된 허가는 모두 단일 성분 제제입니다.” → 확인할 수 없는 단일·복합 표기와 건수 삭제(건수는 빠른 개요와 표) | 정정 | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

