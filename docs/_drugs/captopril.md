---
layout: default
title: Captopril
parent: 모델 예측만 (L5)
nav_order: 179
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Captopril: 예측 신규 적응증 악성 신혈관성 고혈압 (Malignant Renovascular Hypertension) (근거 수준 L5). 기존 적응증: 허가 적응증 원문은 확인되지 않음 (허가 문서 링크만 확인됨). ACE 억제제로서의 항고혈압 용도로 알려져 있음"
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Captopril
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

# Captopril: 고혈압에서 악성 신혈관성 고혈압으로

## 한 문장 요약

Captopril은 ACE(안지오텐신 전환효소) 억제제로, 한국에서 고혈압 등 심혈관계 질환 치료에 사용되어 온 약물입니다.
TxGNN 모델은 **악성 신혈관성 고혈압(Malignant Renovascular Hypertension)**에 효과가 있을 수 있다고 예측하지만, 현재 **임상시험은 0건**이며 관련 **문헌 20편**은 대부분 진단용 연구, 증례 보고, 리뷰로 치료 효과를 직접 입증하지 못합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 원문은 확인되지 않음 (허가 문서 링크만 확인됨). ACE 억제제로서의 항고혈압 용도로 알려져 있음 |
| 예측 신규 적응증 | 악성 신혈관성 고혈압 (Malignant Renovascular Hypertension) |
| TxGNN 예측 점수 | 99.28% |
| 근거 수준 | L4 (치료 목적의 임상시험 없음, 기전적·진단적 문헌 위주) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 12건 |
| 권장 결정 | Hold (추가 연구 필요한 연구 질문 단계) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 DB에 등록되어 있지 않습니다. 알려진 정보에 따르면, Captopril은 ACE를 억제하여 안지오텐신 II 생성을 줄이는 약물이며, 항고혈압 효과가 확립되어 있습니다.

신혈관성 고혈압과 악성 고혈압은 레닌-안지오텐신계(RAS)의 활성화에 크게 의존합니다. 따라서 ACE 억제는 기전상 타당한 접근입니다. 검토된 문헌에서도 신혈관성 고혈압에서 Captopril 투여 후 혈장 레닌 활성이 반응적으로 상승하는 현상이 관찰되어(PMID 232024), 이 질환이 RAS 의존적임을 시사합니다.

다만 양측성 신동맥 협착이나 기능하는 단일 신장의 협착에서는 ACE 억제제가 급격한 신기능 저하를 일으킬 수 있어 안전 장치가 필수입니다. 또한 검색된 문헌은 대부분 Captopril 신장 스캔(renography) 같은 진단 용도이며, 치료 효과를 검증한 연구가 아닙니다.

같은 방식으로 예측된 다른 후보(참고)는 다음과 같으며, 모두 근거가 더 약합니다.
- 악성 고혈압성 신장질환: 문헌 1편(진단 증례), L4, Hold
- 폐 질환/저산소증에 의한 폐고혈압: 임상시험 없음, 대부분 무관하거나 전임상 문헌, L5, Hold
- 원인 불명 다인성 폐고혈압: 임상시험·문헌 모두 없음, L5, Hold

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

치료 효과를 직접 평가한 문헌은 확인되지 않았습니다. 관련성이 높은 순으로 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | 임상 보고 | Biulleten' Vsesoiuznogo kardiologicheskogo nauchnogo tsentra AMN SSSR | 안정형 및 악성 경과 동맥성 고혈압에서 Captopril 사용 (초록 없음) |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | 리뷰 | Endocrinol Metab Clin North Am | 레닌 분비 종양에서 ACE 억제제 치료 시 혈압이 하강함 |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | 임상 연구 | Clin Sci (Lond) | 신혈관성 고혈압 44명 중 43명에서 ACE 억제제/saralasin 투여 후 레닌 활성이 크게 상승, 진단 지표로 활용 가능 |
| [3326101](https://pubmed.ncbi.nlm.nih.gov/3326101/) | 1987 | 임상 보고 | J UOEH | 소아 난치성 고혈압에서 Captopril 치료 효과 검토 |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | 증례군/리뷰 | Pediatr Nephrol | 신경섬유종증 소아 27명에서 신혈관 질환과 고혈압 연관성 평가 (Captopril 검사 사용) |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | 증례/리뷰 | Clin Nephrol | 신경섬유종증 관련 신혈관성 고혈압 2예 |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | 리뷰 | Jpn J Med | 고혈압의 병태생리와 예후, 신혈관성 고혈압 진단 |
| [7955304](https://pubmed.ncbi.nlm.nih.gov/7955304/) | 1994 | 리뷰 | Cleve Clin J Med | 신혈관 질환의 비침습적 선별 검사 |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | 증례 | Clin Nucl Med | 신동맥 협착이 없는 악성 고혈압 환자에서의 Captopril 신장 스캔 이상 소견 (진단적 증례) |
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | 증례 | Clin Nucl Med | 신세포암에 의한 Captopril 신장 스캔 양성 (악성 고혈압성 신장질환 예측 관련) |

## 한국 시판 정보

허가 적응증 원문은 문서 링크로만 제공되어 본문 텍스트를 확인하지 못했습니다. 아래는 주요 허가 5건입니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 198600630 | 카프릴정12.5밀리그람 (보령) | 흰색 원형 정제 | 허가 문서 참조 |
| 199500320 | 일동캅토프릴정12.5밀리그람 (수출용, 일동제약) | 백색 원형 정제 | 허가 문서 참조 |
| 200804337 | 파마캅토프릴정25밀리그람 (수출용, 한국파마) | 백색 사각형 정제 | 허가 문서 참조 |
| 199703532 | 케토닐정 (수출용, 대한뉴팜) | 백색 원형 정제 | 허가 문서 참조 |
| 201504524 | 카모투스정 (수출용, 경진제약) | 흰색~미백색 사각형 정제 | 허가 문서 참조 |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 확인되지 않아 허가사항을 참조하세요. 다만 약물 지식 그래프에서는 다음 질환이 금기 관련 항목으로 연결되어 있습니다(허가 문구가 아닌 모델 지식 그래프 기준).

- **신장·간 질환**: 신장 질환, 간 질환, 간성 혼수/간성 뇌병증
- **혈관부종 계열**: 혈관부종, 후천성·유전성 혈관부종, RAS 차단제 유발 혈관부종
- **대사·전해질**: 당뇨병, 당뇨병성 케토산증, 칼륨 결핍, 고요산혈증, 부갑상선기능항진증
- **혈액**: 호중구감소증, 무과립구증
- **심혈관**: 대동맥 판막 협착 및 관련 질환, 저혈압성 장애
- **기타**: 전신 홍반 루푸스, 결합조직 질환, 췌장염, 담낭 질환, 뼈 질환

**약물 상호작용**: 총 100건이 조회되었으며 대부분 중등도(Moderate)입니다.
- 코르티코스테로이드: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
- 혈당강하제: metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, chlorpropamide, acetohexamide
- 기타: bupropion, morphine, acetylsalicylic acid, dronabinol
- 경미(Minor): aluminum hydroxide, calcium carbonate

특히 신동맥 협착 환자에서는 급성 신기능 저하 위험이 있어 신기능과 혈청 칼륨의 면밀한 모니터링이 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
RAS 의존성이라는 기전적 타당성은 있으나, 치료 효과를 평가한 임상시험이 없고 검색된 문헌은 대부분 진단 목적의 연구, 증례, 리뷰입니다. 신혈관 질환에서 ACE 억제제의 신기능 악화 위험도 있어 현재는 연구 질문 단계에 머뭅니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고·금기·적응증) 원문 확보 및 분석. 현재 안전성 선별을 진행할 수 없는 차단 수준의 데이터 공백입니다.
- 상세한 작용 기전(MOA) 데이터 보완
- 악성 신혈관성 고혈압에서 Captopril의 치료 효과를 평가한 문헌 및 임상 근거 확인 (기존 진료 지침 포함)
- 양측성 신동맥 협착 환자 등 고위험군에 대한 신기능 안전 모니터링 계획 수립
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

