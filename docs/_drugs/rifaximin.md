---
layout: default
title: Rifaximin
parent: 모델 예측만 (L5)
nav_order: 654
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-15
description: "Rifaximin: 예측 신규 적응증 구강 칸디다증 (Oral candidiasis) (근거 수준 L5). 기존 적응증: 1. 그람양성균 및 그람음성균에 의한 급성장내감염에 의한 설사 증후군 2. 장내세균총의 이상으로 인한…"
monitor_inn: "RIFAXIMIN"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "oral leukoedema", "burning mouth syndrome", "candidiasis"]
---

# Rifaximin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
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

## Rifaximin: 간성뇌증 등 장관 질환에서 구강 칸디다증으로
{: .text-alpha }

## 한 문장 요약

Rifaximin은 장에서 거의 흡수되지 않는 경구 항생제로, 한국에서 4건의 허가를 받아 시판되고 있습니다.
TxGNN 모델은 **구강 칸디다증(oral candidiasis)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건**이며 관련 문헌 1편은 오히려 **위험 신호**를 시사합니다.
따라서 이 예측은 모델 점수에 의존한 가설 수준에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 그람양성균 및 그람음성균에 의한 급성장내감염에 의한 설사 증후군 2. 장내세균총의 이상으로 인한 설사(여름철 설사, 여행자 설사, 소장결장염) 3. 위장관 수술전후 장내 감염의 예방 4. 고암모니아혈증 치료의 보조요법 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201706207/EE)) |
| 예측 신규 적응증 | 구강 칸디다증 (Oral candidiasis) |
| TxGNN 예측 점수 | 0.9975 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Rifaximin 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “리팍시민은 항균제이다. […] 리팍시민은 리팜핀의 반합성 유도체로, 세균의 DNA 의존성 RNA 중합효소의 베타 소단위에 결합하여 전사 단계 중 하나를 차단함으로써 작용한다. 이로 인해 세균의 단백질 합성이 억제되고, 결과적으로 세균의 증식이 억제된다.” 영어 원문: "Rifaximin is an antibacterial drug. […] Rifaximin is a semi-synthetic derivative of rifampin and acts by binding to the beta-subunit of bacterial DNA-dependent RNA polymerase blocking one of the steps in transcription. This results in inhibition of bacterial protein synthesis and consequently inhibits the growth of bacteria." ([DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b), 버전 2025-08-27; 확인일 2026-11-19). 알려진 정보에 따르면 Rifaximin은 장에서 거의 흡수되지 않는 항균제이며, 항진균 활성은 알려져 있지 않습니다.

기존 적응증(장관 관련 감염 및 관련 질환)과 구강 칸디다증 사이에는 직접적인 기전 연관성이 확인되지 않습니다. 오히려 유일한 문헌(PMID 34180023)은 Rifaximin 사용이 동종 조혈모세포이식 환자에서 미카펀진 내성 Candida 감염을 **조장**했다고 보고합니다. 장내 미생물총 교란이 진균 과증식을 촉진했을 가능성이 있습니다.

따라서 높은 TxGNN 점수(0.9975)는 임상 근거로 뒷받침되지 않습니다. 이 점수는 TxGNN 모델(딥러닝)이 산출한 값이며, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있을 뿐 생물학적 근거는 아닙니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | 코호트 | Annals of Hematology | 동종 조혈모세포이식 환자에서 Rifaximin 사용이 미카펀진 내성 Candida 감염과 연관됨 (치료 효과가 아닌 위험 신호) |

관련 임상시험 등록은 현재 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201706207 | 리팍신정(리팍시민)(수출용) | 분홍색 원형 필름코팅정 | 허가사항 참조 |
| 201800492 | 리팍신정550mg(리팍시민)(수출용) | 분홍색 원형 필름코팅정 | 허가사항 참조 |
| 202302343 | 틱스타정(리팍시민) | 분홍색 타원형 필름코팅정 | 허가사항 참조 |
| 200209900 | 노르믹스정(리팍시민) | 분홍색 원형 필름코팅정 | 허가사항 참조 |

## 안전성 고려사항

- **지식그래프상 금기 질환**: *Clostridium difficile* 대장염, 신생아 괴사성 장염 (라벨 문구가 아닌 지식그래프 기반 정보)
- **약물 상호작용**: 총 69건이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **Major**: Vibrio cholerae CVD 103-HgR 생백신
  - **Moderate**: Cyclosporine, Warfarin, Tolvaptan, Alpelisib, Apalutamide, Cabozantinib, Daclatasvir, Ledipasvir 등
- 이 밖의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
구강 칸디다증에 대한 임상시험이 없고, 유일한 문헌은 치료 이점이 아닌 진균 감염 위험 증가를 시사합니다. Rifaximin에는 항진균 활성이 없어 높은 모델 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 분석
- 상세한 작용 기전(MOA) 데이터
- 구강 칸디다증에 대한 전임상 또는 임상 근거
- Rifaximin 사용과 진균 감염 위험의 연관성에 대한 추가 안전성 검토

**참고:** 같이 예측된 다른 질환(연결 순위 2~6위: 구순 연결부 누공, 하악 방사선골괴사, 작열구 증후군, 구강 백색부종, 칸디다증)도 모두 Hold입니다. 이들 중 임상 근거가 있는 것은 없으며, 칸디다증 관련 문헌 2편은 이점이 아닌 위험 연관성만 시사합니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Xifaxan (rifaximin) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7afafa63-3236-4212-9589-045db6b01c0b) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

