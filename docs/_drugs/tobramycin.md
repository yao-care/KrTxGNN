---
layout: default
title: Tobramycin
parent: 모델 예측만 (L5)
nav_order: 740
evidence_level: L5
indication_count: 10
monitor_inn: "Tobramycin"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "epidemic keratoconjunctivitis"]
last_modified_at: 2026-11-20
description: "Tobramycin: 예측 신규 적응증 노출성 각막염 (근거 수준 L5). 기존 적응증: ○ 유효균종 포도구균(황색포도구균, 표피포도구균, 페니실린 내성균 포함), 연쇄구균(일부 그룹…"
---

# Tobramycin
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

## Tobramycin: 허가 문서상 점안제·주사제에서 노출성 각막염(예측)으로
{: .text-alpha }

## 한 문장 요약

Tobramycin은 아미노글리코사이드 계열 항생제로, 한국에서 점안액과 주사제 등 단일제 허가증이 다수 있습니다.
TxGNN 모델은 **노출성 각막염(Exposure keratitis)**에 효과가 있을 수 있다고 예측합니다(점수 0.9993).
그러나 이 질환을 직접 다룬 임상시험은 **0건**이고 직접 연구한 문헌도 없어, 근거는 모델 예측 수준(L5)입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 유효균종 포도구균(황색포도구균, 표피포도구균, 페니실린 내성균 포함), 연쇄구균(일부 그룹 A-베타용혈성 연쇄구균, 비용혈성 연쇄구균, 폐렴구균 포함), 녹농균, 대장균, 폐렴간균, 엔테로박터 에로제니스, 프로테우스 미라빌리스, 프로테우스 불가리스, 모르가넬라 모르가니… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201803990/EE)) |
| 예측 신규 적응증 | 노출성 각막염 |
| TxGNN 예측 점수 | 0.9993 |
| 근거 수준 | L5 (이 질환을 직접 연구한 시험·문헌 없음) |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 19건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Tobramycin 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “토브라마이신은 아미노글리코사이드계 항균제이다. […] 토브라마이신은 Streptomyces tenebrarius가 생산하는 아미노글리코사이드계 항균제이다. 이 약은 주로 단백질 합성을 교란하여 세포막 투과성의 변화, 세포 외피의 점진적 파괴, 그리고 궁극적인 세포 사멸을 초래함으로써 작용한다.” 영어 원문: "Tobramycin is an aminoglycoside antibacterial. […] Tobramycin is an aminoglycoside antibacterial produced by Streptomyces tenebrarius. It acts primarily by disrupting protein synthesis leading to altered cell membrane permeability, progressive disruption of the cell envelope, and eventual cell death." ([DailyMed: Tobi Podhaler (tobramycin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4b5bb1f-e158-4ac1-9c35-e98a416c743a), 버전 2026-04-15; 확인일 2026-11-19). 알려진 정보에 따르면 Tobramycin은 그람음성균과 포도상구균에 활성이 있는 아미노글리코사이드 항생제이며, 점안제 형태로 세균성 각막염 등 안구 감염에 쓰입니다. 국내에는 점안액 허가증이 많습니다.

노출성 각막염은 눈꺼풀이 제대로 닫히지 않아 각막 표면이 마르면서 손상되는 질환입니다. 감염은 이차적으로 생기는 문제입니다. 따라서 Tobramycin이 도움이 된다면 이차 세균 감염의 예방이나 치료에 한정될 것입니다. 건조 손상 자체를 치료하는 기전은 아닙니다.

또한 시험관 연구에서 Tobramycin을 포함한 아미노글리코사이드가 각막 상피세포에 독성을 보였습니다. 이미 손상된 안구 표면에는 오히려 불리할 수 있어, 예측의 타당성은 제한적입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | 시험관 연구 | Current Eye Research | 토끼 각막 상피세포에서 네오마이신, 겐타마이신, 토브라마이신, 아미카신의 세포독성 비교 |
| [42842711](https://pubmed.ncbi.nlm.nih.gov/42842711/) | 2026 | 후향적 코호트 | Cornea | 메티실린 내성/감수성 황색포도상구균 각막염의 임상 특성, 항생제 감수성, 치료 결과 비교 |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | 시험관 연구 | Nippon Ganka Gakkai Zasshi | 일본 감염성 각막염 분리균에 대한 항생제 점안액의 최소억제농도(MIC) 및 항생제 후효과 비교 |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | 증례 보고 | Oxford Medical Case Reports | 눈을 스스로 감지 못하는 환자에서 다제내성 Shewanella algae 세균성 각막염 1례 |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | 증례 보고 | Ophthalmology | 콘택트렌즈 관련 Bacillus cereus 각막염 1례 |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | 증례 보고 | Eye & Contact Lens | 굴절교정각막절제술 후 양안 MRSA 각막염 1례 |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | 증례 보고 | Yan Ke Xue Bao | 그레이브스 안병증에서 나타난 중심부 주변 각막 델렌 1례 |
| [42358321](https://pubmed.ncbi.nlm.nih.gov/42358321/) | 2026 | 시험관 연구(수의학) | Frontiers in Veterinary Science | 개 안구 병원균에서 플루오로메톨론이 항생제 감수성에 미치는 영향 |

위 문헌 중 노출성 각막염에서 Tobramycin의 효과를 직접 평가한 연구는 없습니다. 대부분 다른 원인의 각막염이나 항생제 독성·감수성을 다룹니다.

## 한국 시판 정보

허가증 목록은 일부일 수 있으며, 아래는 그중 5건입니다. 허가 적응증 본문은 데이터에 포함되어 있지 않고 허가 문서 링크만 있어, 해당 문서를 참조해야 합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201803990 | 토브점안액 | 점안액 | 허가 문서 참조 |
| 201403504 | 태극토브라마이신점안액(수출용) | 점안액 | 허가 문서 참조 |
| 200401647 | 토프라신주(바이알) | 주사제 | 허가 문서 참조 |
| 201504139 | 토브카디점안액(수출용) | 현탁성 점안액 | 허가 문서 참조 |
| 199904140 | 대한뉴팜황산토브라마이신주(수출용) | 주사제(앰플) | 허가 문서 참조 |

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건입니다. 이 중 확인된 **중대(Major)** 수준은 다음과 같습니다.
  - 황산마그네슘
  - 만니톨
- **중등도(Moderate) 수준 예시**: 암포테리신 B, 반코마이신, 카나마이신, 네오마이신, 아세틸살리실산, 메살라진, 설파살라진, 프로톤펌프억제제(오메프라졸, 판토프라졸, 란소프라졸 등)
- **눈 표면 관련 우려**: 시험관 연구에서 아미노글리코사이드의 각막 상피 독성이 보고되어, 손상된 안구 표면에는 주의가 필요합니다.

그 밖의 경고·금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 노출성 각막염을 직접 연구한 임상시험과 문헌이 없어 근거는 모델 예측뿐(L5)입니다.
- 질환의 본질이 건조 손상이어서 항생제의 기전적 연결이 약하고, 각막 상피 독성 우려가 있습니다.

**진행하려면 필요한 것:**
- 노출성 각막염에서 이차 감염 예방·치료 효과를 직접 평가한 임상 또는 관찰 연구
- 손상된 각막 상피에 대한 Tobramycin 점안제의 안전성 평가
- 국내 허가 문서(허가사항)에서 적응증, 경고, 금기 확인
- 작용 기전 데이터 보완

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Tobi Podhaler (tobramycin) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c4b5bb1f-e158-4ac1-9c35-e98a416c743a) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

