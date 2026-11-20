---
layout: default
title: Adapalene
parent: 모델 예측만 (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Adapalene: 예측 신규 적응증 혈장 아연 상승 (zinc, elevated plasma) (근거 수준 L5). 기존 적응증: 12세 이상의 면포, 구진, 농포가 나타나는 여드름의 국소치료"
monitor_inn: "ADAPALENE"
predicted_indications: ["zinc, elevated plasma"]
---

# Adapalene
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **1** 건
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

## Adapalene: 여드름에서 혈장 아연 상승으로
{: .text-alpha }

## 한 문장 요약

Adapalene은 국소 도포용 3세대 레티노이드로, 원래 여드름(심상성 좌창) 치료에 사용되었습니다. TxGNN 모델은 **혈장 아연 상승(zinc, elevated plasma)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건**, **문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 12세 이상의 면포, 구진, 농포가 나타나는 여드름의 국소치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200706875/EE)) |
| 예측 신규 적응증 | 혈장 아연 상승 (zinc, elevated plasma) |
| TxGNN 예측 점수 | 0.9951 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 12건 / 전체 12건) |
| 허가증 수 | 12건 (유효 12건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Adapalene 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “아다팔렌은 특정 레티노산 핵수용체에 결합하지만 세포질 수용체 단백질에는 결합하지 않는다. 생화학적 및 약리학적 프로파일 연구에서 아다팔렌은 세포 분화, 각질화 및 염증 과정의 조절제인 것으로 입증되었다.” 영어 원문: "Adapalene binds to specific retinoic acid nuclear receptors but does not bind to cytosolic receptor protein. Biochemical and pharmacological profile studies have demonstrated that adapalene is a modulator of cellular differentiation, keratinization, and inflammatory processes." ([DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec), 버전 2023-12-27; 확인일 2026-11-19). 알려진 정보에 따르면 Adapalene은 RAR-beta/gamma에 선택적으로 결합하는 국소용 레티노이드이며, 여드름 치료에 쓰입니다.

레티노이드와 아연 항상성 사이에는 비타민 A-아연 상호작용, 아연 의존성 금속단백분해효소 및 레티놀 결합 단백질에 대한 영향 등 느슨한 생물학적 연관만 있습니다. Adapalene이 혈장 아연을 낮추는 직접적인 경로는 확립된 바 없습니다.

또한 혈장 아연 상승은 치료 표적 질환이라기보다 검사실 소견에 가깝고, 전신 흡수가 적은 국소제로 전신 아연 수치를 바꾸기는 어렵습니다. 따라서 이 예측 점수(0.9951)는 TxGNN 모델(딥러닝)이 관련 질환 간에 학습한 유사성을 반영한 것일 수 있으며, 생물학적 근거가 아니므로 실행 가능한 근거로 보기 어렵습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200706875 | 엘리아겔(아다팔렌) | 반투명의 흰색 겔 | 허가 문서 링크만 제공됨 |
| 200907303 | 에피듀오겔0.1%/2.5%(아다팔렌/과산화벤조일) | 흰색~미황색의 불투명한 겔 | 허가 문서 링크만 제공됨 |
| 200708882 | 동구아다팔렌겔 | 반투명한 흰색 겔 | 허가 문서 링크만 제공됨 |
| 200210174 | 디페린크림0.1%(아다팔렌) | 흰색의 크림 | 허가 문서 링크만 제공됨 |
| 201800996 | 에피듀오포르테겔0.3%/2.5%(아다팔렌/과산화벤조일) | 흰색 또는 연한 노란색의 불투명한 겔 | 허가 문서 링크만 제공됨 |

위 5건 외에도 겔 제형 허가가 7건 더 있어 총 12건이 유효합니다.

## 안전성 고려사항

- **지식 그래프상 금기 질환**: 광발작 반응(photoparoxysmal response), 광과민성 질환(photosensitivity disease), 박탈성 피부염(exfoliative dermatitis), 피부염(dermatitis). 이는 라벨 문구가 아니라 지식 그래프의 약물-질환 금기 연결에서 나온 정보입니다.
- **약물 상호작용**: 총 58건이 확인되었으며, 상호작용 수준은 모두 "미상"으로 분류됩니다. 일부 예: Doxycycline, Tetracycline, Minocycline, Metronidazole, Prednisone, Triamcinolone, Budesonide, Ibuprofen, Fluconazole, Clopidogrel, Bupropion.

허가사항의 경고 및 금기는 확인되지 않았으므로 허가사항을 직접 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
높은 TxGNN 점수(0.9951) 외에는 임상시험, 문헌, 기전상 근거가 모두 없습니다. 혈장 아연 상승은 치료 표적으로 부적절하고, 국소제의 낮은 전신 흡수를 고려하면 생물학적 타당성도 낮아 현 단계에서는 보류가 적절합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 원문 확보 및 분석
- DrugBank 등에서 상세 작용 기전 데이터 확보
- 레티노이드와 아연 대사의 연결을 보여주는 전임상 또는 관찰 연구 근거
- 국소 도포 시 전신 노출 수준과 투여 경로 적합성 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

