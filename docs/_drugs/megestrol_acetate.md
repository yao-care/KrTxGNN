---
layout: default
title: Megestrol Acetate
parent: 모델 예측만 (L5)
nav_order: 498
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Megestrol Acetate: 예측 신규 적응증 자궁체부 자궁내막암 (Uterine corpus endometrial carcinoma) (근거 수준 L5). 기존 적응증: 확인 불가 (허가 적응증 본문이 없고 허가증 문서 링크만 제공됨)"
monitor_inn: "Megestrol acetate"
predicted_indications: ["hereditary breast ovarian cancer syndrome", "borderline epithelial tumor of ovary", "uterine carcinosarcoma", "placenta cancer", "ovarian clear cell adenocarcinoma", "ovarian cancer", "malignant dysgerminomatous germ cell tumor of ovary"]
---

# Megestrol Acetate
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

## Megestrol acetate: 한국 허가 적응증에서 자궁체부 자궁내막암으로
{: .text-alpha }

## 한 문장 요약

Megestrol acetate는 합성 프로게스틴 계열 약물로, 한국에서 16건의 허가증(현탁액·정제)이 유효한 상태로 시판되고 있습니다. 다만 이번 보고서용으로 확보한 자료에는 허가 적응증 본문이 포함되지 않았습니다.
TxGNN 모델은 **자궁체부 자궁내막암(Uterine corpus endometrial carcinoma)**에 효과가 있을 수 있다고 예측합니다(예측 점수 99.94%).
이 예측을 직접 뒷받침하는 자료는 **1건의 임상시험**(Phase 2, 완료)이며, 해당 질환에 대한 문헌은 없습니다. 반면 난소암(예측 순위 8위)에는 **완료된 Phase 3 시험 1건**과 **문헌 20편**이 있어 근거가 가장 풍부합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 확인 불가 (허가 적응증 본문이 없고 허가증 문서 링크만 제공됨) |
| 예측 신규 적응증 | 자궁체부 자궁내막암 (Uterine corpus endometrial carcinoma) |
| TxGNN 예측 점수 | 99.94% |
| 근거 수준 | L2 (완료된 Phase 2 RCT 1건) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 16건 (모두 단일제, 유효) |
| 권장 결정 | Hold (추가 근거 확보 후 재평가) |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터가 없습니다. 알려진 정보에 따르면 Megestrol acetate는 프로게스테론 수용체에 작용하는 합성 프로게스틴입니다. 프로게스틴 치료는 자궁내막암, 특히 분화도가 높고 호르몬 수용체가 양성인 질환과 임신 보존 치료에서 확립된 호르몬 요법입니다.

자궁내막암은 에스트로겐이 종양 성장을 촉진할 수 있는 호르몬 의존성 암입니다. 프로게스틴은 이 자극에 대항할 수 있어 기전상 적용 가능성이 있습니다. 다만 이번 근거는 Megestrol이 비교군(호르몬 병용군)에 포함된 시험에서 나온 것이므로, 약물 자체의 재창출 효과를 검증한 것은 아닙니다.

참고로 예측 상위 10개 질환 중 근거가 비교적 많은 것은 난소암(Phase 3 시험 1건, Phase 2 연구 다수)이며, 나머지 대부분은 임상·문헌 근거가 없습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | 완료 | 73 | 진행성·지속성·재발성 자궁내막암에서 temsirolimus 단독 vs. temsirolimus + 호르몬 요법(megestrol acetate + tamoxifen) 비교. Megestrol은 병용·비교군 성분이므로 간접 근거임 |

## 안전성 고려사항

- **지식그래프 기반 금기 질환 (허가 문서가 아닌 TxGNN 지식그래프의 약물-질환 금기 연결)**: 고혈압, 신장 질환, 간 질환, 담낭 질환, 고혈당, 부신피질 기능부전(애디슨병), 당뇨병, 당뇨병성 케톤산증, 남성 성선기능저하증, 조기 폐경, 안드로겐 불감증 증후군 등
- **약물 상호작용**: 총 100건이 확인되었으며, 목록에 나온 항목은 모두 중등도(Moderate)입니다. 주로 혈당강하제(acarbose, metformin, pioglitazone, sitagliptin, semaglutide, glimepiride, 인슐린 계열, SGLT2 억제제 등)와 aprepitant, clarithromycin이 포함됩니다.
- **부신 억제**: 관련 문헌(PMID 10491532)에서 Megestrol 치료 시 이차성 부신 억제가 보고되어 있어 주의가 필요합니다.

허가사항의 경고·금기 항목은 이번 자료에 없으므로 허가사항(첨부문서)을 직접 확인하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
자궁내막암에 대한 직접 근거는 Megestrol이 비교군에 포함된 Phase 2 시험 1건뿐이며, 문헌이 없고 결과 요약도 제공되지 않았습니다. 또한 허가 적응증과 허가사항의 경고·금기가 확인되지 않아 안전성 평가를 진행할 수 없습니다.

**진행하려면 필요한 것:**
- MFDS 허가사항(첨부문서 PDF)에서 기존 적응증, 경고, 금기 확인
- DrugBank에서 작용 기전(MOA) 데이터 확보
- NCT00729586의 결과(반응률, 생존율 등)와 Megestrol 투여군 데이터 확인
- 자궁내막암 대상 Megestrol 단독요법·임신 보존 치료 관련 문헌 추가 검색
- 근거가 더 풍부한 난소암(Phase 3 시험 NCT00005975, Phase 2 연구 2건)을 대안 후보로 검토. 단, NCT00005975는 유방암 치료 후 난소 기능 저하 증상(안면홍조)을 평가한 시험이므로 난소암 치료 효과의 근거로는 부적합할 수 있어 적응증 매칭 재확인이 필요함
- 당뇨·고혈압·간·신장 질환 환자 및 혈당강하제 병용 환자에 대한 안전성 모니터링 계획 수립
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

