---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ciprofloxacin: 세균 감염에서 미만성 피부경화증으로

## 한 문장 요약

Ciprofloxacin은 광범위 스펙트럼 플루오로퀴놀론계 항생제로, 요로감염·호흡기 감염·피부 감염 등 다양한 세균성 질환 치료에 국제적으로 사용되고 있습니다. TxGNN 모델은 **미만성 피부경화증(Diffuse Scleroderma)**에 효과가 있을 수 있다고 예측하며, 현재 **임상시험 0건**과 **2편의 문헌**이 이 방향을 지지합니다.

---

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 한국 허가 없음 (국제적으로 세균성 감염증 치료에 사용) |
| 예측 신규 적응증 | 미만성 피부경화증 (Diffuse Scleroderma) |
| TxGNN 예측 점수 | 99.87% |
| 근거 수준 | L3 |
| 한국 시판 현황 | 미시판 |
| 허가증 수 | 0건 |
| 권장 결정 | Research Question |

---

## 이 예측이 타당한 이유는?

현재 한국 허가 데이터베이스에 Ciprofloxacin의 상세 작용 기전 데이터가 없습니다. 알려진 정보에 따르면, Ciprofloxacin은 세균의 DNA 회선효소(Gyrase A/B)와 Topoisomerase IV를 억제하여 DNA 복제를 차단하는 살균성 플루오로퀴놀론계 항균제입니다.

이 재창출 예측의 핵심은 항균 효과 이외의 **이중 기전 가설**에 있습니다. 첫째, **직접 항섬유화 효과**: 체외 및 초기 임상 파일럿 연구(PMID 20507401)에서 Ciprofloxacin이 TGF-β 유도성 콜라겐 합성과 섬유아세포 증식을 억제할 수 있음이 시사되며, NF-κB 경로를 통한 작용 기전이 추정됩니다. 둘째, **간접 기전**: 미만성 피부경화증의 흔한 합병증인 소장세균과증식(SIBO)을 치료함으로써 장 점막 장벽 기능을 개선하고, 미생물 유래 면역 활성화 및 섬유화 촉진을 간접적으로 억제할 수 있습니다(PMID 7728404).

피부경화증은 미세혈관 손상, 과도한 피부 섬유화, 폐·심장·신장·위장관 침범이 특징인 자가면역 결합조직 질환으로, 현재까지 효과적인 항섬유화 약물 치료가 없습니다. 기전상 합리성은 **중등도**로 판단되며, 대규모 임상 검증이 필요합니다.

---

## 임상시험 근거

현재 미만성 피부경화증에 대한 관련 임상시험 등록이 없습니다.

---

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Clinical Observational / Pilot Study | The Journal of Dermatology | 피부경화증 환자에서 경구 Ciprofloxacin의 항섬유화 유용성을 평가한 이중맹검 무작위 대조시험; 피부경화증 섬유화 경감 여부를 직접 평가한 현존하는 핵심 임상 근거 |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Observational / Diagnostic Study | British Journal of Rheumatology | 전신성 경화증 환자 24명에서 소장세균과증식(SIBO) 검출 및 치료 결과 평가; 항생제(Ciprofloxacin 포함) 치료를 통한 흡수장애 증상 개선 사례 보고 |

---

## 한국 시판 정보

한국 내 Ciprofloxacin 허가 제품이 조회되지 않습니다 (미시판). 국제적으로는 세균성 감염증 치료제로 광범위하게 허가·사용되고 있으나, 본 데이터셋 기준 한국 규제 데이터가 없어 허가 이력을 확인할 수 없습니다.

---

## 안전성 고려사항

안전성 정보는 허가사항을 참조하세요.

> **참고**: FDA 흑박경고(Black Box Warning)에 따르면 Ciprofloxacin은 건염·건 파열, 말초 신경병증(영구적 손상 가능), QT 연장, 중증 근무력증 악화 위험이 있습니다. 피부경화증 환자는 이미 말초혈관 및 신경계 합병증 위험이 있으므로, 재창출 임상시험 설계 시 이 점을 반드시 고려해야 합니다.

---

## 결론 및 다음 단계

**결정: Research Question**

**사유:**
미만성 피부경화증에 대한 Ciprofloxacin의 항섬유화 효과를 시사하는 초기 임상 파일럿 연구 1건(이중맹검 RCT 설계)과 간접 기전 근거 문헌 1건이 존재하나, 전체 결과 공개 여부가 불명확하고 근거 규모가 매우 제한적입니다. 유망한 기전 가설이 있어 연구 주제로서의 가치는 있으나, 재창출 적응증으로 진전시키기 위해서는 추가 전임상 및 임상 근거가 선행되어야 합니다.

**진행하려면 필요한 것:**
- PMID 20507401 임상시험 전체 데이터 및 최종 결과 검토 (abstract만 공개됨)
- TGF-β/NF-κB 경로에 대한 체외(in vitro) 항섬유화 기전 연구 확보
- 피부경화증 환자에서 FDA 흑박경고 해당 이상반응(말초 신경병증, 건 손상) 위험 평가
- 한국 내 허가 경로 확인 (현재 미시판; 임상시험 IND 신청 절차 검토 필요)
- SIBO 치료를 통한 피부경화증 간접 개선 효과에 대한 전향적 파일럿 연구 설계

---

## 참고: 기타 주목할 예측

본 Evidence Pack에는 미만성 피부경화증 외 9개의 추가 예측이 포함되어 있습니다. 임상적으로 주목할 사항을 요약합니다:

| 순위 | 예측 적응증 | 근거 수준 | 권장 결정 | 비고 |
|------|------------|---------|---------|------|
| 8 | 단클론 감마글로불린병증 (Monoclonal Gammopathy) | L3 | Research Question | 다발성 골수종 환자 감염 예방 관련 RCT/코호트 다수 |
| **10** | **패혈성 페스트 (Septicemic Plague)** | **L2** | **Proceed with Guardrails** | **완료된 Phase 2 RCT(N=200) 포함; FDA 이미 승인** |
| 9 | 후천성 말초 신경병증 동반 혈액 질환 | L5 | **⛔ Hard Stop** | FDA 흑박경고: Ciprofloxacin 자체가 말초 신경병증 유발 가능—명확한 위해 |
| 2–7, 9 | 나머지 예측 | L5 | Hold | 기전적 합리성 없거나 대체 치료가 명확히 존재 |

> **특기사항**: **패혈성 페스트(Rank 10)**는 이미 FDA 승인 사용 적응증이며, 완료된 Phase 2 비열등성 RCT(NCT01243437, N=200, Madagascar)와 NEJM 2025년 발표 RCT(PMID 40768716)가 존재합니다. 본 재창출 분석에서 가장 강력한 근거를 가진 적응증으로, 별도 전체 보고서 작성을 권장합니다.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

