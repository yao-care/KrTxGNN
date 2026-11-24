---
layout: default
title: Brolucizumab
parent: 모델 예측만 (L5)
nav_order: 158
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices without bleeding", "esophageal varices with bleeding", "exocrine pancreatic insufficiency"]
description: "Brolucizumab: 예측 신규 적응증 핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) (근거 수준 L5). 기존 적응증: https://nedrug.mfds.go.kr/pbp/cmn/pdfDownloa…"
---

# Brolucizumab
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

## Brolucizumab: 핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies)
{: .text-alpha }

## 한 문장 요약

Brolucizumab은 VEGF-A를 억제하는 단쇄 항체 절편(scFv) 제제로, 안구 내(유리체 내) 주사용으로 허가되어 한국에서 시판 중입니다.
TxGNN 모델은 **핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애**에 효과가 있을 수 있다고 예측하지만, 현재 이를 뒷받침하는 **임상시험은 0건, 문헌도 0편**입니다.
즉, 이 예측은 모델 예측 단계(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 신생혈관성 (습성) 연령관련 황반변성의 치료 당뇨병성 황반부종의 치료 ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202004402/EE)) |
| 예측 신규 적응증 | 핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애 (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| TxGNN 예측 점수 | 0.9967 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 2건 / 전체 2건) |
| 허가증 수 | 2건 (유효 2건) |
| 권장 결정 | Hold |

> 참고: 같은 약물에 대해 다음 예측도 있었으나 모두 근거가 없습니다: 식도 정맥류(출혈 없음/출혈 동반, 각 0.9912), 외분비 췌장 기능부전(0.9907).

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Brolucizumab 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “브롤루시주맙은 인간 VEGF 억제제이다. 브롤루시주맙은 VEGF-A의 세 가지 주요 동형(예: VEGF 110, VEGF 121 및 VEGF 165)에 결합하여 수용체 VEGFR-1 및 VEGFR-2와의 상호작용을 차단한다. VEGF-A를 억제함으로써 브롤루시주맙은 내피세포 증식, 신생혈관 형성 및 혈관 투과성을 억제한다.” 영어 원문: "Brolucizumab is a human VEGF inhibitor. Brolucizumab binds to the three major isoforms of VEGF-A (e.g., VEGF 110, VEGF 121, and VEGF 165 ), thereby preventing interaction with receptors VEGFR-1 and VEGFR-2. By inhibiting VEGF-A, brolucizumab suppresses endothelial cell proliferation, neovascularization, and vascular permeability." ([DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d), 버전 2026-10-26; 확인일 2026-11-19). 알려진 정보에 따르면 brolucizumab은 VEGF-A를 표적으로 하는 항체 절편이며, 안구 내 투여용으로 허가된 단일 성분 제제입니다.

핵 DNA 이상에 의한 미토콘드리아 산화적 인산화 장애는 호흡사슬의 조립 또는 기능 결손이 원인이며, VEGF 신호와는 직접적인 관련이 없습니다. 따라서 **현재까지 확립된 기전적 연결고리는 없습니다.** 0.9967이라는 높은 점수는 TxGNN 모델(딥러닝)에서 나온 값으로, 모델이 관련 질환 간에 학습한 유사성을 반영할 수 있으며 생물학적 근거가 아닙니다.

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202004402 | 비오뷰주(브롤루시주맙) | 투명하거나 옅은 유백광이 있는 무색 또는 엷은 황갈색의 액이 무색 투명한… | 한국노바티스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202004402/EE) | 유효 |
| 202005466 | 비오뷰프리필드시린지(브롤루시주맙) | 투명하거나 옅은 유백광이 있는 무색 또는 엷은 황갈색의 액이 무색투명한… | 한국노바티스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202005466/EE) | 유효 |

<!-- licenses:end -->

## 안전성 고려사항

- **지식 그래프 기반 금기 질환**(허가 문서가 아닌 TxGNN 지식 그래프 기준): 포도막염, 홍채 질환, 섬모체 질환, 범포도막염, 안구 감염성 질환, 결막염
- **참고 위험(예측 적응증 관련)**: 항 VEGF 제제는 출혈 및 혈전색전 위험이 우려되므로, 특히 출혈이 동반된 식도 정맥류에서는 안전성 방향이 불리할 수 있습니다.

그 외 경고·금기 사항은 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
임상시험과 문헌이 전혀 없고 기전적 연결고리도 확인되지 않아, 높은 TxGNN 점수만으로는 재창출을 추진하기 어렵습니다. 또한 안구 내 투여용 제제라 전신 노출 및 출혈 관련 안전성 문제가 있습니다.

**진행하려면 필요한 것:**
- 허가 적응증 본문 및 허가사항의 경고·금기 정보 확보
- 작용 기전(MOA) 데이터 보완
- 미토콘드리아 질환과 VEGF 경로의 연관성을 보여주는 전임상 또는 기전 연구
- 투여 경로 적합성 평가(안구 내 투여 제제의 전신 적용 가능성)
- 관련 임상시험 및 문헌 근거 재검색

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

