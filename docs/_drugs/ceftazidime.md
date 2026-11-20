---
layout: default
title: Ceftazidime
parent: 모델 예측만 (L5)
nav_order: 196
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-15
monitor_inn: "CEFTAZIDIME"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "epiglottitis", "blood group incompatibility", "Peptostreptococcus infectious disease"]
description: "Ceftazidime: 예측 신규 적응증 고아밀라제혈증 (hyperamylasemia) (근거 수준 L5). 기존 적응증: ○ 유효균종 메치실린감수성 황색포도구균, 메치실린감수성 표피포도구균, 소구균, 스트렙토콕쿠스…"
---

# Ceftazidime
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

## Ceftazidime: 고아밀라제혈증 (hyperamylasemia)
{: .text-alpha }

## 한 문장 요약

Ceftazidime은 세균 세포벽 합성을 억제하는 세팔로스포린계 주사 항생제입니다.
TxGNN 모델은 **고아밀라제혈증(hyperamylasemia)**에 효과가 있을 수 있다고 예측하지만, 이를 뒷받침하는 임상시험과 문헌은 **각각 0건**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | ○ 유효균종 메치실린감수성 황색포도구균, 메치실린감수성 표피포도구균, 소구균, 스트렙토콕쿠스 피오게네스(그룹 A- 베타 용혈성), 스트렙토콕쿠스 아갈락티에(그룹B), 스트렙토콕쿠스 비리단스, 연쇄구균(장내구균 제외), 폐렴 연쇄구균, 슈도모나스(녹농균 등), 클레브시엘라(폐렴간균… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201202147/EE)) |
| 예측 신규 적응증 | 고아밀라제혈증 (hyperamylasemia) |
| TxGNN 예측 점수 | 0.9951 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 14건 / 전체 18건) |
| 허가증 수 | 18건 (유효 14건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Ceftazidime 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “세프타지딤은 세균 세포벽 합성을 억제함으로써 작용하는 살균제이다. 세프타지딤은 그람음성 및 그람양성 세균의 일부 베타-락타마제(페니실리나제 및 세팔로스포리나제 모두)가 존재하는 상황에서도 활성을 가진다.” 영어 원문: "Ceftazidime is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftazidime has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93), 버전 2026-08-03; 확인일 2026-11-19). 알려진 정보에 따르면 ceftazidime은 세균 세포벽 합성을 억제하는 세팔로스포린계 항생제입니다.

고아밀라제혈증은 감염 질환이 아니라 혈중 아밀라제 수치가 올라간 검사 소견입니다. 항균 작용으로 이를 치료할 수 있다는 기전적 연결고리는 확인되지 않았습니다. 높은 예측 점수는 모델 내부의 연관성에서 나온 것으로, 임상적·문헌적 뒷받침이 없습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201202147 | 딤제프주2그램(수출용) | 백색 또는 유백색의 가루가 든 주사제 | 허가 적응증 문서 링크로만 제공되어 요약 불가 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었으며, 주요 항목은 다음과 같습니다.
  - 중등도: Amphotericin B(및 콜레스테릴 설페이트·지질 복합체·리포좀 제형), Kanamycin, Neomycin, Streptomycin, Picosulfuric acid
  - 등급 미상: Calcitriol, Pantoprazole, Doxycycline, Morphine, Metformin, Omeprazole, Sucralfate, Lansoprazole, Vancomycin, Atropine, Lactulose, Triamcinolone

허가사항의 경고 및 금기 정보는 허가 문서를 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고아밀라제혈증에 대해 직접 연구한 임상시험이나 문헌이 없고, 항생제인 ceftazidime과 이 검사 소견 사이에 타당한 기전도 확인되지 않습니다. 예측 점수만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 고아밀라제혈증과 ceftazidime의 연관성을 직접 다룬 임상 또는 전임상 연구
- 상세한 작용 기전(MOA) 데이터
- 허가사항의 경고·금기 정보 확보 (한국 허가 문서 PDF 확인)

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: ceftazidime prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=112c5457-8d71-49f5-b531-9761d7d38c93) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

