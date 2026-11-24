---
layout: default
title: Dexlansoprazole
parent: 모델 예측만 (L5)
nav_order: 272
evidence_level: L5
indication_count: 4
monitor_inn: "DEXLANSOPRAZOLE"
predicted_indications: ["gastroduodenitis", "duodenal obstruction", "achlorhydria", "leather-bottle stomach"]
last_modified_at: 2026-11-24
description: "Dexlansoprazole: 예측 신규 적응증 위십이지장염 (gastroduodenitis) (근거 수준 L5). 기존 적응증: 1. 미란성 식도염의 치료 2. 미란성 식도염의 치료 후 유지 3. 증후성 비미란성 위식도…"
---

# Dexlansoprazole
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

## Dexlansoprazole: 프로톤 펌프 억제제 → 위십이지장염 (gastroduodenitis)
{: .text-alpha }

## 한 문장 요약

Dexlansoprazole은 프로톤 펌프 억제제(PPI) 계열의 약물로, 한국에서 단일 성분 제제로 허가되어 있습니다.
TxGNN 모델은 **위십이지장염(gastroduodenitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이 예측을 지지하는 **임상시험과 문헌은 없습니다**.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 미란성 식도염의 치료 2. 미란성 식도염의 치료 후 유지 3. 증후성 비미란성 위식도 역류질환(Non-Erosive Gastroesophageal Reflux Disease)과 관련된 속쓰림의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802449/EE)) |
| 예측 신규 적응증 | 위십이지장염 (gastroduodenitis) |
| TxGNN 예측 점수 | 0.9998 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 4건 / 전체 4건) |
| 허가증 수 | 4건 (유효 4건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Dexlansoprazole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “덱스란소프라졸은 위 벽세포의 분비 표면에서 (H +, K + )-ATPase를 특이적으로 억제함으로써 위산 분비를 억제하는 항분비 화합물 계열인 치환 벤즈이미다졸에 속한다. 이 효소는 벽세포 내의 산(양성자) 펌프로 간주되므로, 덱스란소프라졸은 산 생성의 최종 단계를 차단한다는 점에서 위 양성자 펌프 억제제로 특징지어졌다.” 영어 원문: "Dexlansoprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the (H +, K + )-ATPase at the secretory surface of the gastric parietal cell. Because this enzyme is regarded as the acid (proton) pump within the parietal cell, dexlansoprazole has been characterized as a gastric proton-pump inhibitor, in that it blocks the final step of acid production." ([DailyMed: Dexlansoprazole Delayed Release (dexlansoprazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55c550b4-eb8b-4e69-9c09-fa5125a52e65), 버전 2026-11-04; 확인일 2026-11-19). 다만 Dexlansoprazole은 PPI 계열 약물로, 위산 분비를 억제하는 것이 일반적인 약리 특성입니다.

위와 십이지장의 염증은 위산과 관련될 수 있으므로, 위산 억제가 증상 완화에 도움이 될 가능성은 기전상 있습니다. 그러나 이 예측을 뒷받침하는 임상시험이나 문헌이 연결되어 있지 않으며, 현재 근거는 TxGNN 모델 점수뿐입니다. 약물과 질환 간 유사성 분석도 아직 완료되지 않았습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201802449 | 덱시라졸캡슐60밀리그램(덱스란소프라졸) | 흰색 내지 연한 노란색의 과립이 충전된 상부청색, 하부청색의 경질캡슐 | (주)유한양행 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802449/EE) | 유효 |
| 201207344 | 덱실란트디알캡슐60밀리그램(덱스란소프라졸) | 백색 또는 연한 갈색의 과립이 충전된 상부청색, 하부청색의 경질캡슐 | 한국다케다제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207344/EE) | 유효 |
| 201207343 | 덱실란트디알캡슐30밀리그램(덱스란소프라졸) | 백색 또는 연한 갈색의 과립이 충전된 상부청색, 하부회색의 경질캡슐 | 한국다케다제약(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201207343/EE) | 유효 |
| 201802450 | 덱시라졸캡슐30밀리그램(덱스란소프라졸) | 흰색 내지 연한 노란색의 구형 과립이 충전된 상부청색, 하부 회색의 경질… | (주)유한양행 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201802450/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

- **약물 상호작용**: 조회된 상호작용은 총 100건이며, 그중 일부는 다음과 같습니다.
  - 주요(Major): Acalabrutinib, Atazanavir
  - 중등도(Moderate): Fosamprenavir, Foscarnet, Fostamatinib, Furosemide, Gefitinib, Hydrochlorothiazide, Amphotericin B, Amikacin, Amphetamine, Ampicillin, Bosutinib, Bumetanide 등
  - 경미(Minor): Acetylsalicylic acid, Axitinib, Brivaracetam, Cyanocobalamin 등

허가사항의 경고 및 금기 정보는 허가 문서를 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
위십이지장염에 대한 예측은 모델 점수에만 의존하며, 직접 연구한 임상시험이나 문헌이 없어 근거 수준은 L5입니다. 또한 작용 기전 데이터와 허가사항의 경고·금기 정보가 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가 문서에서 적응증, 경고 및 금기 정보 확보
- 상세한 약물 작용 기전(MOA) 데이터 확보
- 위십이지장염에 대한 임상시험 또는 문헌 근거 탐색
- 기존 적응증과 예측 질환 간 유사성 분석 및 투여 경로 적합성 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Dexlansoprazole Delayed Release (dexlansoprazole) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=55c550b4-eb8b-4e69-9c09-fa5125a52e65) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

