---
layout: default
title: Siltuximab
parent: 모델 예측만 (L5)
nav_order: 692
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Siltuximab: 예측 신규 적응증 골외 비만세포종 (extracutaneous mastocytoma) (근거 수준 L5). 기존 적응증: 인체면역결핍바이러스 (HIV) 음성 및 제8형 인체헤르페스바이러스 (HHV-8) 음성인 다발성 캐슬만병…"
monitor_inn: "Siltuximab"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "Kaposi's sarcoma (disease)", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "autosomal dominant familial periodic fever"]
---

# Siltuximab
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

## Siltuximab: 특발성 다중심성 캐슬만병에서 골외 비만세포종으로
{: .text-alpha }

## 한 문장 요약

Siltuximab은 IL-6를 중화하는 단클론항체로, 원래 HIV·HHV-8 음성 다중심성 캐슬만병(MCD) 치료에 사용되는 약입니다.
TxGNN 모델은 **골외 비만세포종(extracutaneous mastocytoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환에 대한 **임상시험은 0건, 문헌도 0편**이어서 모델 예측만 있는 상태입니다.
참고로 같은 약물의 다른 예측 후보인 **TAFRO 증후군**은 문헌 근거가 상대적으로 풍부합니다(아래 별도 항목 참조).

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 인체면역결핍바이러스 (HIV) 음성 및 제8형 인체헤르페스바이러스 (HHV-8) 음성인 다발성 캐슬만병 환자의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201508041/EE)) |
| 예측 신규 적응증 | 골외 비만세포종 (extracutaneous mastocytoma) |
| TxGNN 예측 점수 | 0.9964 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Siltuximab 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “실툭시맙은 인간 IL-6에 결합하여 IL-6가 가용성 및 막 결합형 IL-6 수용체 모두에 결합하는 것을 방지한다. IL-6는 면역글로불린 분비 유도와 같은 다양한 정상 생리적 과정에 관여하는 것으로 밝혀졌다.” 영어 원문: "Siltuximab binds human IL-6 and prevents the binding of IL-6 to both soluble and membrane-bound IL-6 receptors. IL-6 has been shown to be involved in diverse normal physiologic processes such as induction of immunoglobulin secretion." ([DailyMed: Sylvant (siltuximab) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d663642-f52e-49c0-a023-2da083fdfc0b), 버전 2024-08-27; 확인일 2026-11-19). 다만 Siltuximab은 IL-6를 중화하는 항체로 알려져 있고, 캐슬만병은 IL-6 과다 생성이 주된 원인인 림프증식성 질환입니다.

그러나 이 보고서에 정리된 데이터에는 IL-6 신호전달이 비만세포종의 발병 기전과 연결된다는 근거가 없습니다. 기존 적응증과 예측 적응증 사이의 연관성도 아직 평가되지 않았습니다. 따라서 이 점수는 TxGNN 모델(딥러닝)에서 나온 것으로, 모델이 관련 질환 사이에서 학습한 유사성을 반영할 수 있으며 생물학적 근거는 아닙니다. 기전적 타당성이 확인된 것은 아닙니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 201508041 | 실반트주100밀리그램(실툭시맙, 유전자재조합) | 흰색 동결건조 고체가 무색 투명한 유리바이알에 든 주사제로서, 용해 시… | (주)레코르다티코리아 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201508041/EE) | 유효 |
| 201508042 | 실반트주400밀리그램(실툭시맙, 유전자재조합) | 흰색 동결건조 고체가 무색 투명한 유리바이알에 든 주사제로서, 용해 시… | (주)레코르다티코리아 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201508042/EE) | 유효 |

<!-- licenses:end -->

제조사는 (주)레코르다티코리아이며, 두 허가 모두 유효합니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었고, 그중 일부만 상세 목록으로 확인됩니다.
  - **Major**: Deferiprone
  - **Moderate**: Warfarin, Apixaban, Rivaroxaban, Dicoumarol(항응고제), Simvastatin, Tacrolimus, Theophylline·Aminophylline·Oxtriphylline·Roflumilast(PDE/잔틴계), Lidocaine, Hydrocodone, Fentanyl, Nifedipine, 파상풍 톡소이드 백신
  - **Minor**: 아연 제제(황산아연, 아세트산아연, 글루콘산아연, 염화아연)
- 경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 참고: 같은 약물의 다른 예측 후보 중 근거가 가장 많은 TAFRO 증후군

10개 예측 후보 중 대부분은 L5(모델 예측만)입니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [25042199](https://pubmed.ncbi.nlm.nih.gov/25042199/) | 2014 | RCT | Lancet Oncol | HIV 음성 MCD에서 siltuximab의 이중맹검 위약대조 시험 (기존 적응증의 근거이며 TAFRO에는 간접 근거) |
| [30181172](https://pubmed.ncbi.nlm.nih.gov/30181172/) | 2018 | 합의 가이드라인 | Blood | 특발성 MCD 국제 근거 기반 치료 지침 |
| [36652167](https://pubmed.ncbi.nlm.nih.gov/36652167/) | 2023 | 증례 보고 | J Nephrol | TAFRO 증후군에서 siltuximab 단독요법 사례 |
| [32564425](https://pubmed.ncbi.nlm.nih.gov/32564425/) | 2020 | 증례 보고 | Eur J Haematol | TAFRO 증후군에서 siltuximab과 rituximab 병용 초기 치료 사례 |
| [38927484](https://pubmed.ncbi.nlm.nih.gov/38927484/) | 2024 | 가이드/리뷰 | Biomedicines | TAFRO 증후군 환자 관리 안내 |
| [38029058](https://pubmed.ncbi.nlm.nih.gov/38029058/) | 2023 | 리뷰 | J Med Cases | TAFRO 증후군의 단계적 치료 |
| [38087716](https://pubmed.ncbi.nlm.nih.gov/38087716/) | 2024 | 리뷰 | Blood Rev | 특발성 MCD의 진단 및 치료 최신 동향 (anti-IL-6 항체 siltuximab 포함) |

TAFRO 증후군은 특발성 MCD의 아형으로, IL-6와 VEGF가 관여하는 사이토카인 폭풍 질환입니다. TAFRO에 직접 연결되는 근거는 증례 보고 수준이며, 비-TAFRO 특발성 MCD보다 반응이 불확실합니다. TAFRO 전용 시험도 확인되지 않았습니다.

## 결론 및 다음 단계

**결정: Hold** (골외 비만세포종)

**사유:**
임상시험과 문헌이 없고 IL-6와 비만세포종을 잇는 기전적 근거도 확인되지 않아, 모델 예측만으로는 진행하기 어렵습니다.

**진행하려면 필요한 것:**
- IL-6 신호전달과 비만세포종 병태생리의 연관성을 보여주는 전임상·기전 근거
- 이 질환을 대상으로 한 임상시험 또는 문헌 근거
- 한국 허가사항 원문(적응증, 경고, 금기)의 확인과 안전성 검토
- 상세 작용 기전(MOA) 데이터 보완

**별도 권고:** 같은 약물의 TAFRO 증후군 후보는 Proceed with Guardrails 수준입니다. 이 경우 특발성 MCD 합의 지침에 맞춰 코르티코스테로이드 등과 단계적으로 병용하고, 반응을 면밀히 모니터링하는 조건으로 별도 평가를 권장합니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Sylvant (siltuximab) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d663642-f52e-49c0-a023-2da083fdfc0b) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

