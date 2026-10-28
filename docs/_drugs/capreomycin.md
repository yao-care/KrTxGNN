---
layout: default
title: Capreomycin
parent: 모델 예측만 (L5)
nav_order: 178
evidence_level: L5
indication_count: 9
monitor_inn: "Capreomycin"
predicted_indications: ["gout", "rheumatoid arthritis", "osteoarthritis", "sclerosing cholangitis", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "meningococcal infection", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type"]
last_modified_at: 2026-10-27
description: "Capreomycin: 예측 신규 적응증 통풍 (gout) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201104025/EE"
---

# Capreomycin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **9** 건
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

## Capreomycin: 고리형 펩타이드 항결핵 항생제 → 통풍 (gout)
{: .text-alpha }

## 한 문장 요약

Capreomycin은 다제내성 결핵 치료에 쓰이는 고리형 펩타이드 계열 주사용 항생제입니다.
TxGNN 모델은 **통풍(gout)**에 효과가 있을 수 있다고 예측했지만, 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201104025/EE |
| 예측 신규 적응증 | 통풍 (gout) |
| TxGNN 예측 점수 | 0.9991 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 1건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. Capreomycin은 세균의 단백질 합성을 억제하는 것으로 알려진 항생제이며, 다제내성 결핵 치료에 사용됩니다.

통풍은 요산 대사 이상과 이로 인한 염증성 관절염이 핵심입니다. 이번 자료에서는 capreomycin과 요산 대사 또는 통풍성 염증을 연결할 만한 기전을 찾을 수 없었습니다. 예측 점수가 높더라도 이는 모델의 계산 결과일 뿐, 생물학적 근거로 확인된 것은 아닙니다.

또한 신독성과 이독성이 알려진 주사제이므로, 만성이면서 생명을 위협하지 않는 질환인 통풍에는 위험 대비 이익이 불리할 것으로 보입니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201104025 | 카프레신주(카프레오마이신황산염)(수출용) | 백색~엷은 황백색 분말이 들어 있는 무색 바이알제 | 적응증 텍스트 미기재 |

허가증은 1건이며 단일 성분 제제로 유효 상태입니다. 수출용 제품입니다.

## 안전성 고려사항

**약물 상호작용**: 조회 결과 총 58건이 확인되었습니다. 이 중 주요 항목은 다음과 같습니다.
- **Major(중대)**: Kanamycin, Neomycin. 둘 다 아미노글리코시드 계열로, 신독성·이독성이 겹칠 수 있습니다.
- **Moderate(중등도)**: Amphotericin B 제제(일반, 지질복합체, 콜레스테릴황산염, 리포좀), 스테로이드(Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone, Beclomethasone), 프로톤펌프억제제(Omeprazole, Esomeprazole, Lansoprazole, Rabeprazole, Dexlansoprazole), 5-ASA 계열(Mesalazine, Balsalazide, Olsalazine), Exenatide

그 밖의 경고 및 금기는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
통풍에 대한 임상시험과 문헌이 전혀 없고, 기전상 연결고리도 확인되지 않아 근거는 모델 예측뿐입니다(L5). 신독성·이독성 우려가 있는 주사제라는 점도 불리합니다.

**진행하려면 필요한 것:**
- 허가사항(경고·금기) 확보 및 분석
- 작용 기전(MOA) 데이터 보완
- 통풍과의 생물학적 연관성을 보여 주는 전임상 또는 기전 연구
- 통풍 대상의 임상시험 또는 문헌 근거
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

