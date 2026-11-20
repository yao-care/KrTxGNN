---
layout: default
title: Carboplatin
parent: 모델 예측만 (L5)
nav_order: 184
evidence_level: L5
indication_count: 9
monitor_inn: "Carboplatin"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "adult germ cell tumor", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "endometrial mixed adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-11-20
description: "Carboplatin: 예측 신규 적응증 직장 점액성 선암 (근거 수준 L5). 기존 적응증: 1. 진행성 상피성 난소암 1) 1차 요법 2) 다른 요법 실패 후 2차 요법 2. 소세포폐암"
---

# Carboplatin
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

## Carboplatin: 기존 허가 적응증(허가 문서 참조)에서 직장 점액성 선암으로
{: .text-alpha }

## 한 문장 요약

Carboplatin은 백금계 항암화학요법제로, 한국에서 5건의 허가증이 등록되어 있습니다. 다만 이번에 정리한 데이터에는 허가 적응증의 본문이 없고 허가 문서 링크만 있습니다.
TxGNN 모델은 **직장 점액성 선암(rectum mucinous adenocarcinoma)**에 효과가 있을 수 있다고 예측하며 점수는 0.9928로 높습니다. 그러나 이 질환을 직접 다룬 **임상시험은 0건, 문헌도 0건**이어서 모델 예측만 있는 단계입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 진행성 상피성 난소암 1) 1차 요법 2) 다른 요법 실패 후 2차 요법 2. 소세포폐암 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199201568/EE)) |
| 예측 신규 적응증 | 직장 점액성 선암 |
| TxGNN 예측 점수 | 0.9928 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 5건 / 전체 5건) |
| 허가증 수 | 5건 (유효 5건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Carboplatin 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “카보플라틴은 DNA에 결합하여 DNA 가교를 형성하는 백금 기반 약물이다. 이러한 가교는 DNA 복제 및 전사를 억제하고 세포 사멸로 이어지는 세포독성 과정을 유발한다.” 영어 원문: "Carboplatin is a platinum-based drug that binds to DNA and forms DNA cross-links. These crosslinks inhibit DNA replication and transcription and trigger cytotoxic processes that lead to cell death." ([DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b), 버전 2026-11-09; 확인일 2026-11-19). 일반적으로 알려진 바에 따르면 Carboplatin은 백금계 약물로, DNA에 결합해 가교를 형성하고 빠르게 증식하는 암세포의 분열을 억제합니다. 이론상 선암 세포에도 작용할 수 있습니다.

그러나 이 예측을 뒷받침하는 것은 TxGNN의 높은 예측 점수뿐입니다. 직장 점액성 선암에서 Carboplatin을 평가한 시험이나 문헌은 확인되지 않았습니다. 점액성 조직형은 일반적으로 항암제 감수성이 낮다고 알려져 있어, 기전만으로 효과를 단정하기 어렵습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

현재 관련 문헌이 없습니다.

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199201568 | 카보티놀주사 | 갈색 바이알(무색 투명한 용액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 200004907 | 카보틴주 (수출용) | 갈색 바이알(무색 투명한 용액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 200905067 | 칸플라틴주 (수출용) | 갈색 바이알(무색 투명한 용액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 199101108 | 네오플라틴주 | 갈색 바이알(무색 투명한 주사액) | 허가 문서 링크만 확인됨, 본문 미확보 |
| 200210228 | 화이자카보플라틴주10mg/ml | 바이알(무색 투명한 주사액) | 허가 문서 링크만 확인됨, 본문 미확보 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 기존 세포독성 약물 (백금계) |
| 골수억제 위험 | 일반적으로 높은 편이며 혈소판감소와 호중구감소가 대표적입니다. 이번 데이터에는 독성 정보가 없습니다. |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | 혈구 검사(CBC), 신장 기능, 간 기능 |
| 취급 방호 | 세포독성 약물 취급 규정 준수 필요 |

## 안전성 고려사항

허가사항의 경고와 금기 정보는 이번 데이터에 포함되어 있지 않아 허가사항을 직접 확인해야 합니다.

**약물 상호작용**: 총 100건이 조회되었으며, 이 중 확인된 20건은 다음과 같습니다.
- **중등도**
  - 프로톤펌프억제제: rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole
  - 항생제: kanamycin, neomycin, streptomycin, vancomycin, metronidazole, tinidazole
  - 스타틴: rosuvastatin, simvastatin
- **경미**: levofloxacin
- **등급 미확인**: calcitriol, glimepiride, mesalazine, doxycycline, clotrimazole

## 결론 및 다음 단계

**결정: Hold**

**사유:**
직장 점액성 선암에 대한 예측 점수는 높지만, 이를 직접 뒷받침하는 임상시험이나 문헌이 없어 근거 수준이 L5(모델 예측만 있음)입니다. 작용 기전, 허가 적응증 본문, 안전성 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가 문서(MFDS 첨부문서)에서 적응증, 경고, 금기 정보 확보
- DrugBank 등에서 작용 기전 데이터 확보
- 직장 및 대장 점액성 선암에서 Carboplatin 효능을 직접 평가한 시험이나 문헌 탐색
- 같은 데이터에서 Carboplatin의 다른 예측 적응증(성인 생식세포종양, 자궁내막 혼합 선암 등)은 임상시험이 더 많으므로 별도 평가 권장

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Kyxata (carboplatin) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f91c48da-68d1-4aa7-89b8-d84a3e8b629b) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

