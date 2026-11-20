---
layout: default
title: Fluorometholone
parent: 모델 예측만 (L5)
nav_order: 358
evidence_level: L5
indication_count: 8
monitor_inn: "Fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
last_modified_at: 2026-11-20
description: "Fluorometholone: 예측 신규 적응증 감염 후 혈관염 (postinfectious vasculitis) (근거 수준 L5). 기존 적응증: 외안부 및 전안부의 염증성 질환(안검염, 결막염, 각막염, 공막염, 상공막염, 홍채염, 홍채모양체염…"
---

# Fluorometholone
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

## Fluorometholone: 글루코코르티코이드 수용체 작용제(안과용 스테로이드) → 감염 후 혈관염 (postinfectious vasculitis)
{: .text-alpha }

## 한 문장 요약

Fluorometholone은 글루코코르티코이드 수용체에 작용하는 안과용 스테로이드 점안제 성분입니다.
TxGNN 모델은 **감염 후 혈관염(postinfectious vasculitis)**에 효과가 있을 수 있다고 예측하지만, 현재 이를 직접 뒷받침하는 **임상시험은 0건, 문헌도 0편**이며 모델 예측만 존재합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 외안부 및 전안부의 염증성 질환(안검염, 결막염, 각막염, 공막염, 상공막염, 홍채염, 홍채모양체염, 포도막염, 수술후 염증 등) ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201707502/EE)) |
| 예측 신규 적응증 | 감염 후 혈관염 (postinfectious vasculitis) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Fluorometholone 처방 정보(Prescribing Information)의 “Clinical Pharmacology” 항목에 따르면(비공식 번역): “코르티코스테로이드는 다양한 유발 인자에 대한 염증 반응을 억제하며, 아마도 치유를 지연시키거나 늦출 것이다. 코르티코스테로이드는 염증과 관련된 부종, 피브린 침착, 모세혈관 확장, 백혈구 이동, 모세혈관 증식, 섬유모세포 증식, 콜라겐 침착 및 흉터 형성을 억제한다. […] 스테로이드 반응자로 확인된 환자를 대상으로 한 임상시험에서 플루오로메톨론은 덱사메타손인산염보다 안압 상승을 일으키기까지의 평균 시간이 유의하게 더 길었으나, 소수의 환자에서는 1주 이내에 유의한 안압 상승이 나타났다.” 영어 원문: "Corticosteroids inhibit the inflammatory response to a variety of inciting agents and probably delay or slow healing. They inhibit the edema, fibrin deposition, capillary dilation, leukocyte migration, capillary proliferation, fibroblast proliferation, deposition of collagen, and scar formation associated with inflammation. […] In clinical studies of documented steroid-responders, fluorometholone demonstrated a significantly longer average time to produce a rise in intraocular pressure than dexamethasone phosphate; however, in a small percentage of individuals, a significant rise in intraocular pressure occurred within one week." ([DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01), 버전 2026-08-12; 확인일 2026-11-19). 다만 약리 정보상 Fluorometholone은 글루코코르티코이드 수용체(NR3C1)에 결합하는 합성 스테로이드이며, 항염증 작용을 가집니다.

글루코코르티코이드는 면역 매개 혈관염을 억제할 수 있으나, 보통 전신 투여가 필요합니다. Fluorometholone은 전신 노출이 제한적인 국소 안과용 제제이므로 전신성 혈관염과의 기전적 연결은 약합니다. 임상 근거 없이 모델 예측만 있는 상태입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201707502 | 플루아이점안액0.1% | 현탁액(점안제) | 허가 문서 링크만 제공됨 |
| 200100630 | 풀아이론점안액0.1% | 수성 현탁 점안제 | 허가 문서 링크만 제공됨 |
| 201207413 | 후메토론플러스점안액 | 현탁 점안제 | 허가 문서 링크만 제공됨 |
| 201306498 | 플루빈점안액0.1% | 다회용·일회용 점안제 | 허가 문서 링크만 제공됨 |
| 201901070 | 휴메론플러스점안액 | 현탁액(점안제) | 허가 문서 링크만 제공됨 |

허가증 목록은 일부일 수 있으며, 위에는 주요 5건만 나열했습니다.

## 안전성 고려사항

- **약물 상호작용**: 약물 상호작용 데이터베이스에서 12건이 조회되었으나 대부분 위험 등급이 정해져 있지 않습니다. 확인된 약물은 Doxycycline, Salbutamol, Cyclosporine, Acetaminophen, Digoxin, Brimonidine, Cephalexin, Alendronic acid, Acyclovir, Diazepam, Fenofibrate 등입니다.

경고 및 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
감염 후 혈관염에 대한 임상시험과 문헌이 없고 모델 예측만 있습니다. 또한 국소 안과용 제제로는 전신성 혈관염에 필요한 전신 노출을 기대하기 어렵습니다.

**진행하려면 필요한 것:**
- 감염 후 혈관염에서 글루코코르티코이드의 효과를 직접 평가한 임상 또는 전임상 근거
- 투여 경로 적합성 평가(국소 안과용 vs 전신 투여)
- 허가사항(경고·금기) 및 상세 작용 기전 데이터 확보

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Fluorometholone Ophthalmic Suspension (fluorometholone) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e7988a3b-e432-4d42-a8d2-63ca017e6a01) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

