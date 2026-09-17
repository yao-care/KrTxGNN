---
layout: default
title: Metronidazole
parent: 모델 예측만 (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: 혐기성·원충 감염에서 뉴모시스티스증(Pneumocystosis)으로

## 한 문장 요약

Metronidazole은 구조화된 `original_indications`/`original_moa` 필드가 모두 데이터 공백 상태이며, 첨부된 문헌 초록들(PMID 7355683, 6835740, 8840708 등)을 통해서만 아메바증·트리코모나스증·혐기성 감염 등에 쓰여온 약물임이 확인됩니다. TxGNN 모델은 **뉴모시스티스증(Pneumocystosis)**에 효과가 있을 수 있다고 예측(점수 99.99%)했지만, 첨부된 임상시험 23건과 문헌 10편을 검토한 결과 실제로 이 예측을 뒷받침하는 근거는 확인되지 않았습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 등재된 공식 적응증 정보 없음 (문헌 맥락상 아메바증·트리코모나스증·혐기성 감염 관련 언급만 존재) |
| 예측 신규 적응증 | 뉴모시스티스증 (Pneumocystosis) |
| TxGNN 예측 점수 | 99.99% |
| 근거 수준 | L5 |
| 한국 시판 현황 | 미출시 |
| 허가증 수 | 0건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

작용 기전(MOA) 데이터가 제공되지 않아 공식 근거를 인용할 수 없습니다. 다만 Evidence Pack의 기전 평가(`repurposing_rationale`)에 따르면 이 예측은 기전상 성립하지 않는 것으로 판단됩니다.

Pneumocystis jirovecii는 진균이며 표준 치료는 TMP-SMX·pentamidine·atovaquone입니다. Metronidazole의 니트로이미다졸계 항혐기균/항원충 기전은 이 병원체에 대해 알려진 활성이 없습니다. 첨부된 문헌들도 대부분 "항기생충제" 또는 "HIV 기회감염" 관련 총론적 리뷰이며, metronidazole이 뉴모시스티스증을 직접 치료했다는 근거는 없습니다.

또한 첨부된 임상시험 23건 중 상당수(오피오이드 위험관리, 당뇨병 교육, 재택 진료 등)는 metronidazole이나 뉴모시스티스증과 무관한 항목으로, 데이터베이스 매칭 오류로 판단됩니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | N/A | 완료 | 65 | 두경부암 생존자 자가평가 도구 실현가능성 연구 — **무관 (Grade C)** |
| [NCT01909076](https://clinicaltrials.gov/study/NCT01909076) | N/A | 완료 | 53 | 1차 진료 내 오피오이드 위험 감소 전략 — 관련성 미평가 |
| [NCT06160947](https://clinicaltrials.gov/study/NCT06160947) | N/A | 모집 전 | 24 | 척추 만성 비암성 통증에서 카이로프랙틱 치료 병행 — 관련성 미평가 |
| [NCT06597123](https://clinicaltrials.gov/study/NCT06597123) | N/A | 모집 전 | 150 | AI 기반 동기면담 훈련 프로그램 — 관련성 미평가 |
| [NCT03466866](https://clinicaltrials.gov/study/NCT03466866) | Phase 3 | 완료 | 156 | 당뇨병 응급실 이용 감소를 위한 교육/원격의료 RCT — **무관 (Grade C)** |
| [NCT03451630](https://clinicaltrials.gov/study/NCT03451630) | N/A | 완료 | 1400 | 복합 만성질환자 통합 진료모델 연구 — 관련성 미평가 |
| [NCT05256303](https://clinicaltrials.gov/study/NCT05256303) | N/A | 완료 | 160 | 농촌 지역 재택 병원급 진료 RCT — 관련성 미평가 |
| [NCT03542084](https://clinicaltrials.gov/study/NCT03542084) | N/A | 완료 | 305 | 내분비내과 자동 이컨설트가 혈당조절에 미치는 영향 — 관련성 미평가 |
| [NCT02208947](https://clinicaltrials.gov/study/NCT02208947) | Phase 3 | 중단 | 77 | 사전의료계획 참여 유도를 위한 소비자 인센티브 — 관련성 미평가 |
| [NCT05892666](https://clinicaltrials.gov/study/NCT05892666) | N/A | 모집 중 | 4000 | 워크인 클리닉·1차진료·응급실 간 진료모델 비교 — **무관 (Grade C)** |

**참고**: 위 10건을 포함해 첨부된 23건의 임상시험 중 metronidazole 또는 뉴모시스티스증 치료를 직접 다룬 시험은 없습니다. Grade가 부여된 항목은 모두 "무관"으로 평가되었으며, 나머지는 관련성 평가가 완료되지 않았으나(`pending`) 제목·요약상 뉴모시스티스증과 무관한 주제입니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | 기생충 감염 치료제 총론, metronidazole의 뉴모시스티스증 치료 언급 없음 |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review(pending) | American Family Physician | 원충 치료제 선택 가이드 — 뉴모시스티스 폐렴은 trimethoprim-sulfamethoxazole이 표준으로 명시, metronidazole은 아메바증·트리코모나스증에만 해당 |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review(pending) | Clinical Pharmacokinetics | 항원충 치료제 약동학 총론 |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | HIV 관련 기회감염 전반 리뷰, metronidazole의 역할 언급 없음 |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review(pending) | Clinical Pharmacy | AIDS 감염 합병증 치료 총론 |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | 설사 치료로 metronidazole 복용 중이던 환자가 별개로 뉴모시스티스 폐렴 발병 — 치료 근거 아님 |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report(pending) | 감염증학잡지(일본) | 아메바성 이질에 metronidazole 투여 후 완치, 이후 별도로 뉴모시스티스 폐렴 발병 — 치료 근거 아님 |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report(pending) | J Formos Med Assoc | AIDS 환자의 CMV·아메바성 대장염 증례, 뉴모시스티스증과 무관 |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review(pending) | Reviews of Infectious Diseases | 항생제 예방요법 비평 총론 |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review(pending) | 日本臨床 | 원충 감염 치료제 총론 (초록 없음) |

**참고**: 10편 모두 metronidazole을 뉴모시스티스증 치료제로 직접 검증한 연구가 아닙니다. 다수는 같은 환자가 별개 사유(아메바증 등)로 metronidazole을 복용 중 뉴모시스티스 폐렴이 발생한 사례일 뿐입니다.

## 한국 시판 정보

현재 한국에 등록된 허가 정보가 없습니다 (미출시, 허가증 0건).

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
Pneumocystosis는 진균 감염으로 metronidazole의 항혐기균/항원충 기전과 병리학적 연관성이 없으며, 표준요법(TMP-SMX 등)과도 기전이 다릅니다. 첨부된 임상시험·문헌 근거는 대부분 무관하거나 간접적(동일 환자의 별개 질환 치료) 사례로, 이 예측을 직접 지지하는 자료가 아닙니다. Evidence Pack 자체 채점도 근거 수준 L5(모델 예측만 존재), 결정 단계 S0로 분류되어 있습니다.

**진행하려면 필요한 것:**
- 작용 기전(MOA) 데이터 확보 (DG002, High severity)
- TFDA 허가사항상 경고·금기 정보 확보 — 현재 S1 안전성 초평가 진입 불가 (DG001, Blocking)
- 뉴모시스티스증에 대한 metronidazole 직접 투여 근거(전임상 또는 임상) 확인
- 다른 예측 후보(예: rank 9 cap polyposis L3/S2, rank 3·10 L4/S1) 대비 우선순위 재검토 권장
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

