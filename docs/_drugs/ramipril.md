---
layout: default
title: Ramipril
parent: 모델 예측만 (L5)
nav_order: 641
evidence_level: L5
indication_count: 8
monitor_inn: "Ramipril"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "brain stem infarction", "intracerebral hemorrhage", "ABri amyloidosis", "cerebral artery occlusion"]
last_modified_at: 2026-11-24
description: "Ramipril: 예측 신규 적응증 폐질환 및/또는 저산소증에 의한 폐고혈압 (근거 수준 L5). 기존 적응증: 1. 고혈압 2. 심근경색 후 심부전 3. 심혈관 질환(심근경색,불안정형 협심증, 다혈관성…"
---

# Ramipril
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

## Ramipril: 허가 적응증 정보 미확인 상태에서 폐질환 및/또는 저산소증에 의한 폐고혈압으로
{: .text-alpha }

## 한 문장 요약

Ramipril은 ACE(안지오텐신 전환효소) 억제제로, 한국에서 라미프릴 단일제 허가와 펠로디핀 복합제(트리아핀정) 허가가 확인됩니다. 허가 건수와 상태는 빠른 개요와 「한국 시판 정보」의 표에 있습니다. 다만 허가 적응증 본문은 이번 데이터에 포함되지 않았습니다.
TxGNN 모델은 **폐질환 및/또는 저산소증에 의한 폐고혈압**에 효과가 있을 수 있다고 예측합니다.
이 질환을 직접 다룬 임상시험은 없고, 관련 문헌은 쥐 실험 1편뿐이므로 근거는 매우 제한적입니다.

<!-- review:begin kr-lic-20261112-ramipril-1 -->

> **검토 정정 (2026-11-24)**: 원래 문장: “한국에서 단일제 허가 4건이 확인됩니다.” 식품의약품안전처 의약품안전나라(nedrug) 허가 자료(2026-11-09 데이터) 기준으로 수정했습니다: 라미프릴 단일제(유효 허가와 취하·유효기간만료 허가)와 펠로디핀 복합제(트리아핀정, 유효)가 있습니다. 최신 수치는 빠른 개요에 있습니다. 근거: [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug).

<!-- review:end kr-lic-20261112-ramipril-1 -->

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 고혈압 2. 심근경색 후 심부전 3. 심혈관 질환(심근경색,불안정형 협심증, 다혈관성 관상동맥회로이식술 또는 다혈관성 경피적 관상동맥 성형술의 과거 병력), 뇌졸증 또는 말초혈관성 질환의 임상적 증거를 가지고 있는 55세 이상의 환자에서 심근경색,뇌졸증, 심혈관 질환으로 인한… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502436/EE)) |
| 예측 신규 적응증 | 폐질환 및/또는 저산소증에 의한 폐고혈압 |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 (쥐 전임상 연구 1편이 해당 질환을 직접 다룸) |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 9건) |
| 허가증 수 | 9건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ramipril 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “라미프릴 및 라미프릴라트는 사람과 동물에서 ACE를 억제한다. 안지오텐신 전환효소는 안지오텐신 I이 혈관수축 물질인 안지오텐신 II로 전환되는 반응을 촉매하는 펩티딜 디펩티다제이다. 안지오텐신 II는 또한 부신피질에서 알도스테론 분비를 자극한다.” 영어 원문: "Ramipril and ramiprilat inhibit ACE in human subjects and animals. Angiotensin converting enzyme is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II. Angiotensin II also stimulates aldosterone secretion by the adrenal cortex." ([DailyMed: ramipril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=245d3580-77c6-4c0f-b324-c8514b792c59), 버전 2026-11-11; 확인일 2026-11-19). 다만 Ramipril은 ACE 억제제로 알려져 있으며, 안지오텐신 II를 줄여 혈관 수축과 혈관 재형성을 완화할 수 있습니다. 이 점이 폐혈관에도 적용될 수 있다는 것이 예측의 기전적 배경입니다.

직접적인 뒷받침은 1996년 쥐 연구(PMID 9200213)입니다. 3주간 저산소 환경에 둔 쥐에게 Ramipril을 투여하자 폐혈관 관류압이 낮아져, ACE 억제가 만성 저산소가 폐혈관에 미치는 영향을 줄이는 것으로 보고되었습니다. 그러나 이는 동물 연구이고 사람 대상 시험은 없습니다. ACE 억제제는 저산소성 폐고혈압의 확립된 치료제도 아닙니다. 심장, 신장, 뇌 모델을 다룬 나머지 문헌은 간접 근거에 그칩니다.

## 문헌 근거

이 질환을 직접 다룬 문헌은 1편이며, 나머지는 간접 근거입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [9200213](https://pubmed.ncbi.nlm.nih.gov/9200213/) | 1996 | 전임상(동물) | Physiological Research | 저산소 노출 쥐에서 Ramipril 투여 시 폐혈관 기저 관류압 감소 |
| [12069940](https://pubmed.ncbi.nlm.nih.gov/12069940/) | 2002 | 전임상(동물) | Am J Physiol Regul Integr Comp Physiol | 레닌-안지오텐시노겐 형질전환 쥐에서 저산소-재산소화에 대한 심장 기능 감수성 감소 (간접 근거) |
| [15671045](https://pubmed.ncbi.nlm.nih.gov/15671045/) | 2005 | 전임상/인체 조직 | European Heart Journal | 심근경색 후 ACE2 발현 증가 (간접 근거) |
| [19380417](https://pubmed.ncbi.nlm.nih.gov/19380417/) | 2009 | 전임상(동물) | Cardiovascular Research | ACE 억제가 심장 압부하 시 내피 전구세포와 신생혈관 형성을 촉진 (간접 근거) |

임상시험 등록은 현재 없습니다.

## 한국 시판 정보

허가 적응증 텍스트는 문서 링크만 제공되어 내용을 확인할 수 없었습니다.

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200502436 | 알파라미프릴캡슐(라미프릴)(수출용) | 백색 또는 미백색의 분말 또는 과립이 충전된 상부 진분홍색, 하부 연부홍… | 알파제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200502436/EE) | 유효 |
| 200500140 | 하트프릴정2.5밀리그램(라미프릴) | 연한 황색의 장방형 정제 | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200500140/EE) | 유효 |
| 200600028 | 하트프릴프로텍트정(라미프릴) | 장방형의 흰색 정제 | (주)종근당 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200600028/EE) | 유효 |
| 200300699 | 트리아핀정5/5mg | 적갈색의 양쪽이 볼록한 원형의 필름코팅정 | (주)한독 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200300699/EE) | 유효 |

위 표는 허가 9건 중 4건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - **중대(Major)**: 시트르산칼륨, 탄산수소칼륨 (고칼륨혈증 위험에 유의)
  - **중등도(Moderate)**: 하이드로코르티손, 덱사메타손, 베타메타손, 부데소니드, 트리암시놀론, 아세틸살리실산, 모르핀, 메트포르민, 글리메피리드, 알로글립틴, 카나글리플로진, 다파글리플로진, 엠파글리플로진 등

허가사항의 경고 및 금기는 이번 데이터에 포함되지 않았으므로 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
저산소성 폐고혈압에 대한 근거가 1996년 쥐 실험 1편뿐이며, 사람 대상 임상시험이 없습니다. 허가 문서의 경고·금기와 작용 기전 데이터도 확보되지 않아 안전성 검토를 시작할 수 없습니다.

**진행하려면 필요한 것:**
- 식약처 허가사항(적응증, 경고, 금기) 원문 확보 및 분석
- DrugBank 등에서 작용 기전 데이터 확보
- 폐고혈압에서 ACE 억제제의 효과를 보여주는 추가 전임상 또는 사람 대상 연구
- 폐고혈압 환자에서의 저혈압, 신기능, 칼륨 수치 등 안전성 검토

<!-- review:begin log -->

## 검토 기록

이 페이지의 검토 기록입니다. 식품의약품안전처 의약품안전나라(nedrug) 허가 자료와 대조했습니다. 정정은 기본적인 사실 진술에 한정되며, 모델 예측·근거 수준·결론은 고쳐 쓰지 않았습니다. 작용 기전 자료가 없다는 문장은 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-24 | 허가 건수: “단일제 허가 4건” → 라미프릴 단일제와 펠로디핀 복합제(트리아핀정) 구분(건수는 빠른 개요와 표) | 정정 (2026-11-24 수정, 이전 판은 기록에 보존) | [식품의약품안전처 의약품안전나라(nedrug) 의약품 허가 정보](https://nedrug.mfds.go.kr/searchDrug) |
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: ramipril prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=245d3580-77c6-4c0f-b324-c8514b792c59) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

