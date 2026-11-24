---
layout: default
title: Hyaluronidase
parent: 모델 예측만 (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
monitor_inn: "Hyaluronidase"
predicted_indications: ["esotropia", "amenorrhea (disease)", "severe nonproliferative diabetic retinopathy", "renal tubular acidosis", "dermatitis", "diabetic retinopathy", "acrodermatitis chronica atrophicans", "diabetic cataract", "neonatal dermatomyositis", "non-syndromic esophageal malformation"]
last_modified_at: 2026-11-24
description: "Hyaluronidase: 예측 신규 적응증 내사시 (esotropia) (근거 수준 L5). 기존 적응증: ○ 피하주사나 근육주사, 국소마취제 및 피하주입 시 침투력 증가 ○ 조직 내에 과다하게 존재하는 체액 및…"
---

# Hyaluronidase
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Hyaluronidase: 히알루론산 분해 효소 → 내사시 (esotropia)
{: .text-alpha }

## 한 문장 요약

Hyaluronidase는 히알루론산을 분해하는 효소 약물로, 한국에서 단일 성분 제제로 다수 허가되어 있습니다. TxGNN 모델은 **내사시(esotropia)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 임상시험은 없고 **1편의 문헌**(증례 보고)만 있으며, 그마저도 치료 효과가 아니라 마취 후 합병증을 다룹니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 피하주사나 근육주사, 국소마취제 및 피하주입 시 침투력 증가 ○ 조직 내에 과다하게 존재하는 체액 및 혈액의 재흡수 촉진 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201201593/EE)) |
| 예측 신규 적응증 | 내사시 (esotropia) |
| TxGNN 예측 점수 | 0.9989 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Hyaluronidase 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “히알루로니다제는 분산제로서, 결합조직의 세포간 기질 및 제대와 유리체액 등 특정 특수 조직에 존재하는 다당류인 히알루론산을 가수분해함으로써 결합조직의 투과성을 변화시킨다. 히알루론산은 A형 및 C형 용혈성 연쇄상구균의 협막에도 존재한다.” 영어 원문: "Hyaluronidase is a dispersion agent, which modifies the permeability of connective tissue through the hydrolysis of hyaluronic acid, a polysaccharide found in the intercellular ground substance of connective tissue, and of certain specialized tissues, such as the umbilical cord and vitreous humor. Hyaluronic acid is also present in the capsules of type A and C hemolytic streptococci." ([DailyMed: Hylenex Recombinant (hyaluronidase) prescribing information, Antares Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3023cc56-ed4b-4e87-b3a1-81b20943f658), 버전 2024-11-11; 확인일 2026-11-19). Hyaluronidase는 조직 내 히알루론산을 분해해 다른 약물의 확산과 흡수를 높이는 데 쓰이는 효소로 알려져 있습니다.

내사시와의 직접적인 기전적 연결고리는 확인되지 않습니다. 유일한 문헌(PMID 16934027)은 국소마취하 백내장 수술 후 지속되는 복시와 사시를 보고한 것으로, hyaluronidase가 마취 보조제로 쓰였을 가능성이 있습니다. 이는 치료 효과가 아니라 이상반응 또는 연관 신호에 가깝습니다. 따라서 높은 예측 점수는 임상 근거로 뒷받침되지 않습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [16934027](https://pubmed.ncbi.nlm.nih.gov/16934027/) | 2006 | 증례 보고/증례 시리즈 | Binocular vision & strabismus quarterly | 구후 국소마취 후 드물게 발생하는 복시·사시 합병증의 임상 특성과 치료를 보고 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201201593 | 리포더마주(히알루로니다제) | 동결건조된 흰색 분말이 든 무색투명한 바이알 주사제 | 알보젠코리아(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201201593/EE) | 유효 |
| 201307398 | 퓨리랙스주(히알루로니다제) | 맑고 투명한 액체가 충전된 무색 투명한 바이알 주사제 | 한화제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307398/EE) | 유효 |
| 200807902 | 뷰티로주(히알루로니다제) | 동결건조된 흰색 분말이 든 무색투명한 바이알 주사제 | 광동제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200807902/EE) | 유효 |
| 200704419 | 하이알라제주(히알루로니다제) | 동결건조된 흰색분말이 든 무색투명한 바이알 | (주)휴온스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200704419/EE) | 유효 |
| 200807155 | 히알로제주(히알루로니다제) | 동결건조된 흰색 분말이 든 무색투명한 바이알 주사제 | (주)중헌제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200807155/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 총 63건이 확인되었으며, 제시된 항목은 모두 경미한 수준입니다. 주요 항목은 히드로코르티손, 트리암시놀론, 아세틸살리실산, 덱사메타손, 베타메타손, 부데소니드, 프레드니솔론, 리도카인, 항히스타민제(클로르페니라민, 세티리진, 로라타딘 등), 에스트로겐 계열(에티닐에스트라디올, 에스트라디올 등)입니다.
- 문헌에는 hyaluronidase 주사에 의한 알레르기 합병증이 보고되어 있어 주의가 필요합니다(PMID 37145319).

그 밖의 경고·금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
내사시에 대한 임상시험이 없고, 유일한 문헌은 마취 후 사시·복시 합병증을 보고한 증례로 치료 효과를 뒷받침하지 않습니다. 직접 연구가 없으므로 근거 수준은 L5이며, 높은 예측 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 내사시에 대한 기전적 가설과 전임상 근거
- 작용 기전(MOA) 데이터 확보
- 허가사항(경고·금기·적응증) 원문 확인
- 마취 보조제 사용 후 사시 발생과의 연관성(안전성 신호) 평가

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Hylenex Recombinant (hyaluronidase) prescribing information, Antares Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3023cc56-ed4b-4e87-b3a1-81b20943f658) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

