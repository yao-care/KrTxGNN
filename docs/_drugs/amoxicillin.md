---
layout: default
title: Amoxicillin
parent: 모델 예측만 (L5)
nav_order: 68
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Amoxicillin: 예측 신규 적응증 고아밀라아제혈증 (Hyperamylasemia) (근거 수준 L5). 기존 적응증: 1. 유효균종 황색포도구균, 표피포도구균, 부생포도구균, 화농성연쇄구균, 폐렴연쇄구균, 헤모필루스…"
monitor_inn: "AMOXICILLIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
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

## Amoxicillin: 세균 감염에서 고아밀라아제혈증으로
{: .text-alpha }

## 한 문장 요약

Amoxicillin은 베타락탐계 항생제로, 세균의 세포벽 합성을 억제하여 감염 치료에 사용되어 왔습니다.
TxGNN 모델은 **고아밀라아제혈증(Hyperamylasemia)**에 효과가 있을 수 있다고 예측하지만, 이를 지지하는 **임상시험은 0건, 문헌도 0편**으로 모델 예측만 존재하는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 유효균종 황색포도구균, 표피포도구균, 부생포도구균, 화농성연쇄구균, 폐렴연쇄구균, 헤모필루스 인플루엔자, 대장균 *, 클레브시엘라속*, 프로테우스 미라빌리스*, 임균*, 박테로이드속(박테로이디즈 프라질리스 포함), 모락 셀라 카타라리스 (암피실린 및 아목시실린에 내성이 있는 :… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200801301/EE)) |
| 예측 신규 적응증 | 고아밀라아제혈증 (Hyperamylasemia) |
| TxGNN 예측 점수 | 0.9963 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Amoxicillin 처방 정보(Prescribing Information)의 “Mechanism of Action” 및 “Microbiology” 항목에 따르면(비공식 번역): “아목시실린은 항균제이다. […] 아목시실린은 활발한 증식 단계에 있는 감수성 세균에 대한 살균 작용이 페니실린과 유사하다. 아목시실린은 세포벽 생합성을 저해하여 세균을 사멸시킨다.” 영어 원문: "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), 버전 2026-11-13; 확인일 2026-11-19). 알려진 정보에 따르면, Amoxicillin은 세균 세포벽 합성을 억제하는 베타락탐계 항생제이며, 단독제 외에 클라불란산 또는 설박탐과의 복합 제형으로도 허가되어 있습니다.

그러나 고아밀라제혈증은 아밀라제 수치가 상승하는 상태로, 항균 작용과 직접적인 연관이 확인되지 않습니다. Amoxicillin이 아밀라제 조절에 작용한다는 알려진 기전은 없으며, 이 예측은 TxGNN 모델(딥러닝)의 점수로서 관련 질환 사이에서 모델이 학습한 유사성을 반영할 수 있을 뿐, 생물학적 근거는 아닙니다.

참고로 같은 모델이 제시한 상위 예측들(다클론성 과점도 증후군, 선천성 무알부민혈증, 혈액형 부적합, 전악성 혈액계 질환, 단클론 감마병증, 후천성 말초신경병증 동반 혈액질환, 패혈성 페스트)도 대부분 타당한 기전이나 임상 근거가 없습니다. 패혈성 페스트만 항균제 관점에서 생물학적으로 그럴듯하지만, 베타락탐은 세포 내 페스트균에 활성이 낮고 1차 치료제도 아닙니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 200801301 | 아시박탐주1.5그램 | 무색투명한 바이알에 흰색~황백색 가루가 든 주사제 | (주)펜믹스 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200801301/EE) | 유효 |
| 201109013 | 아목신캡슐250밀리그램(아목시실린)(수출용) | 백색의 가루가 들어있는 상부 청색, 하부 백색의 경질캡슐제 | 한국코러스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201109013/EE) | 유효 |
| 201109014 | 아목신캡슐500밀리그램(아목시실린)(수출용) | 백색의 가루가 들어있는 상부 적색, 하부 노랑색의 경질캡슐제 | 한국코러스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201109014/EE) | 유효 |
| 199200517 | 아모크라주1.2그램(아목시실린나트륨-클라불란산칼륨5:1) | 무색투명한 바이알에 흰색 또는 미백색의 가루가 든 주사제 | 건일제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199200517/EE) | 유효 |
| 200607737 | 유한아목시실린정250밀리그람(수출용) | 백색의 원형 제피정 | (주)유한양행 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200607737/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

이 외에도 총 12건의 유효 허가가 있으며, 모두 단일 성분 허가로 분류되어 있습니다.

## 안전성 고려사항

- **약물 상호작용**: 수집된 데이터에서 100건의 상호작용이 확인되었습니다. 주요 항목은 다음과 같습니다.
  - **주의 필요(Major)**: Methotrexate, 콜레라 생백신(Vibrio cholerae CVD 103-HgR)
  - **중등도(Moderate)**: Doxycycline, Minocycline, Demeclocycline, Ethinylestradiol, Estradiol, Mycophenolate mofetil, Entecavir, Dicoumarol, Anisindione, Balsalazide 등
  - **경미(Minor)**: Allopurinol, Amiloride, Azithromycin, Clarithromycin, Erythromycin
- **지식 그래프상 금기 관련 질환**(허가 문서가 아닌 모델 지식 그래프 기준): 간부전·간질환, 신장질환, 담즙정체, 포르피린증, 긴 QT 증후군, 심실빈맥, 중증근무력증, *Clostridium difficile* 대장염, 골다공증, 골절, 전염성 단핵구증 등

허가사항의 경고 및 금기 항목은 허가 문서를 직접 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
고아밀라아제혈증에 대한 임상시험과 문헌이 없고, 기전적 연결고리도 확인되지 않아 모델 점수(0.9963)만으로는 진행 근거가 부족합니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 정보 확보 (허가사항 PDF 확인)
- 상세 작용 기전(MOA) 데이터 보완
- 고아밀라아제혈증과 Amoxicillin의 연관성을 뒷받침하는 전임상 또는 임상 근거
- 다른 후보(예: 패혈성 페스트)는 항균제로서의 타당성이 있어 별도 연구 질문으로 검토할 수 있으나, 베타락탐의 한계로 우선순위는 낮음

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

