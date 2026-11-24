---
layout: default
title: Rivaroxaban
parent: 모델 예측만 (L5)
nav_order: 661
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Rivaroxaban: 예측 신규 적응증 류마티스 관절염 (Rheumatoid Arthritis) (근거 수준 L5). 기존 적응증: 1. 비판막성 심방세동 환자에서 뇌졸중 및 전신 색전증의 위험 감소 2. 심재성 정맥혈전증 및 폐색전증의…"
monitor_inn: "RIVAROXABAN"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
---

# Rivaroxaban
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **4** 건
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

## Rivaroxaban: 혈전·색전증 치료에서 류마티스 관절염으로
{: .text-alpha }

## 한 문장 요약

Rivaroxaban은 경구용 Xa 인자 억제 항응고제로, 한국에서 20건의 단일제 허가증으로 시판 중입니다. TxGNN 모델은 **류마티스 관절염(Rheumatoid Arthritis)**에 효과가 있을 수 있다고 예측하지만(점수 0.9957), 현재 이를 직접 검증한 **임상시험은 0건**이며 문헌 4편도 치료 효과를 검증한 연구가 아닙니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 비판막성 심방세동 환자에서 뇌졸중 및 전신 색전증의 위험 감소 2. 심재성 정맥혈전증 및 폐색전증의 치료 3. 심재성 정맥혈전증 및 폐색전증의 재발 위험 감소 4. 하지의 주요 정형외과 수술(슬관절 또는 고관절 치환술)을 받은 성인 환자의 정맥혈전색전증 예방 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202103494/EE)) |
| 예측 신규 적응증 | 류마티스 관절염 (Rheumatoid Arthritis) |
| TxGNN 예측 점수 | 0.9957 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 11건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Rivaroxaban 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “XARELTO는 FXa의 선택적 억제제이다. 활성을 위해 보조인자(예: 항트롬빈 III)를 필요로 하지 않는다. 리바록사반은 유리 FXa 및 프로트롬비나제 활성을 억제한다. 리바록사반은 혈소판 응집에 직접적인 영향을 미치지 않으나, 트롬빈에 의해 유도되는 혈소판 응집을 간접적으로 억제한다.” 영어 원문: "XARELTO is a selective inhibitor of FXa. It does not require a cofactor (such as Anti-thrombin III) for activity. Rivaroxaban inhibits free FXa and prothrombinase activity. Rivaroxaban has no direct effect on platelet aggregation, but indirectly inhibits platelet aggregation induced by thrombin." ([DailyMed: Xarelto (rivaroxaban) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10db92f9-2300-4a80-836b-673e1ae91610), 버전 2026-09-10; 확인일 2026-11-19). 알려진 정보에 따르면 rivaroxaban은 Xa 인자를 억제하는 항응고제입니다. 이번 데이터에서는 허가 적응증 문구도 확인되지 않아, 기존 적응증과 신규 적응증 사이의 연관성은 제한적으로만 평가할 수 있습니다.

기전상 연결 가능성은 다음과 같습니다. 류마티스 관절염은 만성 염증과 응고계 활성화가 동반되며, 자가면역질환에서 트롬빈 생성이 증가한다는 문헌(트롬빈 생성 검사 리뷰)이 확인되었습니다. 또한 Xa 인자·트롬빈 신호가 염증 경로에 영향을 줄 수 있다는 가설이 있습니다.

다만 이는 입증되지 않은 가설입니다. 류마티스 관절염 환자는 혈栓색전증 위험이 높으므로, 실제로 사용한다면 질병 조절이 아니라 **정맥혈전색전증(VTE)의 예방·치료** 목적일 것입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | 하지 정맥혈전색전증의 진단·치료 리뷰. 하지 심부정맥혈전증 발생률은 10만 인년당 88~112건이며 나이에 따라 증가 |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | Rev Med Interne | 자가면역질환(항인지질항체증후군 등)에서 트롬빈 생성 검사를 이용한 과응고 상태 평가 |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS One | 비판막성 심방세동 환자에서 rivaroxaban과 apixaban의 순응도 비교 |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Case report | Cureus | 류마티스 관절염으로 경구 스테로이드를 복용 중인 88세 심방세동 환자의 반복 색전증 사례 |

위 문헌 중 rivaroxaban의 류마티스 관절염 치료 효과를 직접 검증한 연구는 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202103494 | 자바렐토정20밀리그램(리바록사반) | 갈색을 띤 빨간색의 원형 필름코팅정 | (주)중헌제약 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202103494/EE) | 유효 |
| 202102632 | 대한리바록사반정15mg | 빨간색의 원형 필름코팅정 | 대한약품공업(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202102632/EE) | 유효기간만료 |
| 202104228 | 자록스정15밀리그램(리바록사반) | 빨간색의 원형 필름코팅정 | (주)보령바이오파마 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202104228/EE) | 유효 |
| 202104937 | 리반틸정15밀리그램(리바록사반) | 빨간색의 원형 필름코팅정 | 경동제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202104937/EE) | 유효 |
| 201604396 | 리록스반정15밀리그램(리바록사반) | 주황색의 원형 필름코팅정 | 한미약품(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201604396/EE) | 유효 |

위 표는 허가 최소 20건 중 5건입니다.

<!-- licenses:end -->

이 외에도 총 20건의 유효한 단일제 허가증이 있습니다.

## 안전성 고려사항

- **금기(지식그래프 기반, 허가사항 아님)**: 간부전, 신장 질환, 농뇨관(pyoureter), 간 질환, 담낭 질환, 혈액응고 질환
- **약물 상호작용**: 총 100건이 확인되었으며, 주요 항목은 다음과 같습니다.
  - **Major**: Acetylsalicylic acid(아스피린), Cobicistat, Deferasirox, Ibritumomab tiuxetan, Tositumomab (I-131)
  - **Moderate**: Aprepitant, Dexamethasone, Cimetidine, Clarithromycin, Miconazole, Clotrimazole 등

허가사항의 경고·금기 정보는 이번 데이터에 포함되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만 임상시험이 없고 문헌도 치료 효과를 검증하지 않아 근거는 모델 예측뿐(L5)입니다. 항응고제인 rivaroxaban을 질병 조절 목적의 류마티스 관절염 치료제로 쓸 근거는 현재 없습니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기·적응증 원문) 확보 및 분석
- 작용 기전(MOA) 데이터 확보
- 류마티스 관절염에서 Xa 인자·트롬빈 신호와 염증의 관련성을 보는 전임상·기전 연구
- 류마티스 관절염 환자의 VTE 예방 목적 사용을 포함한 관찰 연구 또는 임상시험 설계

### 참고: 다른 예측 적응증

- **통풍(Gout)**, 점수 0.9951: 임상시험이 없고, 문헌은 CYP 상호작용 in vitro 연구와 정맥류 사례 보고뿐이어서 효능 근거가 없습니다(L5, Hold).
- **HIV 감염**, 점수 0.9917: HIV 자체에 대한 치료 근거는 없습니다. 근거는 ritonavir·cobicistat 병용 시 CYP3A4/P-gp 억제로 rivaroxaban 노출과 출혈 위험이 증가한다는 안전성·상호작용 관련 자료입니다. 재창출 효능 신호가 아니라 상호작용 안전성 연구 과제입니다(L4, Research Question).
- **합지증-단지증 증후군(Brachydactyly-syndactyly syndrome)**, 점수 0.9910: 임상시험과 문헌이 모두 없고 타당한 기전도 확인되지 않았습니다(L5, Hold).

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Xarelto (rivaroxaban) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10db92f9-2300-4a80-836b-673e1ae91610) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

