---
layout: default
title: Denosumab
parent: 모델 예측만 (L5)
nav_order: 260
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Denosumab: 예측 신규 적응증 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) (근거 수준 L5). 기존 적응증: 1. 폐경 후 여성 골다공증 환자의 치료 2. 남성 골다공증 환자의 골밀도 증가를 위한 치료 3…"
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **2** 건
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

## Denosumab: 골다공증 등 뼈 질환에서 중증 비증식성 당뇨망막병증으로
{: .text-alpha }

## 한 문장 요약

Denosumab은 한국에서 10건의 허가증으로 시판 중인 RANKL 중화 단클론항체 주사제입니다. 다만 허가 적응증 원문은 데이터에 링크로만 제공되어 구체적인 적응증은 확인하지 못했습니다.
TxGNN 모델은 **중증 비증식성 당뇨망막병증(Severe Nonproliferative Diabetic Retinopathy)**에 효과가 있을 수 있다고 예측하지만, 이를 직접 지지하는 **임상시험은 0건, 문헌은 0편**입니다. 같은 질환군인 당뇨망막병증에서도 간접 문헌 2편만 확인되어 가설 수준의 예측입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 폐경 후 여성 골다공증 환자의 치료 2. 남성 골다공증 환자의 골밀도 증가를 위한 치료 3. 글루코코르티코이드 유발성 골다공증의 치료 4. 안드로겐 차단요법을 받고 있는 비전이성 전립선암 환자의 골 소실 치료 5. 아로마타제 저해제 보조요법을 받고 있는 여성 유방암 환자의 골… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500817/EE)) |
| 예측 신규 적응증 | 중증 비증식성 당뇨망막병증 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 예측 점수 | 0.9963 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 10건 / 전체 10건) |
| 허가증 수 | 10건 (유효 10건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Denosumab 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “데노수맙 제품은 골흡수를 담당하는 세포인 파골세포의 형성, 기능 및 생존에 필수적인 막관통 또는 가용성 단백질인 RANKL에 결합한다. 데노수맙 제품은 RANKL이 파골세포 및 그 전구세포 표면의 수용체인 RANK를 활성화하는 것을 저해한다.” 영어 원문: "Denosumab products bind to RANKL, a transmembrane or soluble protein essential for the formation, function, and survival of osteoclasts, the cells responsible for bone resorption. Denosumab products prevent RANKL from activating its receptor, RANK, on the surface of osteoclasts and their precursors." ([DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd), 버전 2026-11-04; 확인일 2026-11-19). 알려진 정보에 따르면 Denosumab은 RANKL(RANK 리간드)을 중화하는 단클론항체입니다. RANKL은 파골세포의 형성과 활성에 관여하므로, 뼈 흡수를 억제하는 약물로 사용됩니다.

신규 적응증과의 연관성은 가설 단계입니다. RANKL/RANK/OPG 신호가 당뇨병 환자의 혈관 석회화, 염증, 미세혈관 기능 이상에 영향을 줄 가능성이 제기될 수 있습니다. 그러나 RANKL 억제가 망막 신생혈관, 혈관 누출, 망막병증 진행에 영향을 준다는 직접적인 증거는 없습니다. 기존 적응증과 신규 적응증 사이의 기전적 유사성 평가도 아직 이루어지지 않았습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

중증 비증식성 당뇨망막병증에 대한 직접 문헌은 없습니다. 아래는 상위 질환군인 **당뇨망막병증**(예측 순위 2위)에서 검색된 간접 문헌입니다. 두 연구 모두 망막병증에 대한 Denosumab의 효과를 직접 검증하지 않았습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | 코호트 연구 (관찰연구) | Diabetes Obes Metab | 골다공증 환자에서 Denosumab이 비스포스포네이트 대비 제2형 당뇨병 발생, 족부 궤양 위험, 전체 사망률을 낮추는 것으로 보고됨. 제목이 잘려 있어 망막병증 결과는 확인 불가 |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | 관찰/코호트 연구 | Cureus | 제2형 당뇨병 성인의 FRAX 골절 위험 평가 도구 사용 평가. 망막병증 결과와 무관 |

## 한국 시판 정보

<!-- licenses:begin -->

| 허가번호 | 제품명 | 성상 | 업체명 | 허가사항 | 상태 |
|------|------|------|------|------|------|
| 202500817 | 오보덴스프리필드시린지(데노수맙) | 무색 내지 약간 노란색이고, 투명하며 입자를 거의 포함하지 않는 액이 무… | 삼성바이오에피스(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202500817/EE) | 유효 |
| 202600308 | 이잠비아프리필드시린지(데노수맙) | 무색 내지 연한 노란색이고, 투명하거나 유백광이 있으며, 입자를 거의 포… | 에이치케이이노엔(주) | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202600308/EE) | 유효 |
| 202402753 | 스토보클로프리필드시린지(데노수맙) | 무색 또는 연한 노란색이고, 투명에서 약간 탁한 용액이 주사침이 부착된… | (주)셀트리온 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/202402753/EE) | 유효 |
| 201404453 | 엑스지바주(데노수맙) | 무색 내지 약간 노란색이고, 투명하거나 유백광이 있으며 입자를 거의 포함… | 암젠코리아유한회사 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201404453/EE) | 유효 |
| 201404452 | 프롤리아프리필드시린지(데노수맙) | 무색 내지 약간 노란색이고 투명하거나 유백광이 있으며 입자를 거의 포함하… | 암젠코리아유한회사 | [허가사항 문서](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201404452/EE) | 유효 |

위 표는 허가 10건 중 5건입니다.

<!-- licenses:end -->

이 밖에 5건의 허가(오센벨트주, 엑스브릭주, 메디팁데노수맙프리필드시린지, 덴브레이스주, 엑스지바프리필드시린지)가 유효하며, 총 10건 모두 단일제입니다.

## 안전성 고려사항

- **약물 상호작용**: 총 100건의 상호작용이 조회되었으며, 확인된 주요 항목은 모두 중등도(Moderate) 수준입니다.
  - 코르티코스테로이드: Hydrocortisone, Prednisone, Prednisolone, Methylprednisolone, Dexamethasone, Betamethasone, Budesonide, Triamcinolone
  - 면역억제·면역조절 약물: Tacrolimus, Dupilumab, Mercaptopurine
  - 방사성의약품·기타: Ibritumomab tiuxetan, Tositumomab, Iobenguane (I-131), Levamisole, Trimetrexate
  - 부신피질자극호르몬 계열: Corticotropin, Tetracosactide

경고 및 금기 등 그 밖의 안전성 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
TxGNN 점수는 매우 높지만(0.9963), 중증 비증식성 당뇨망막병증을 직접 지지하는 임상시험과 문헌이 없어 근거 수준이 L5에 머뭅니다. 작용 기전 데이터와 허가 적응증 원문도 확보되지 않아 가설 생성 단계로 판단합니다.

**진행하려면 필요한 것:**
- 허가 적응증 및 경고·금기 확인 (허가사항 PDF 확인)
- 작용 기전(MOA) 데이터 보충 (DrugBank 조회)
- RANKL 억제와 망막 신생혈관·혈관 누출·망막병증 진행 사이의 전임상 기전 근거
- 당뇨망막병증 결과를 직접 평가하는 관찰연구 또는 임상시험
- 주사제(전신 투여)의 망막 질환 적용 타당성 및 투여 경로 검토

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Conexxence (denosumab) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39a0a789-778f-4695-b3a9-61643e6396cd) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

