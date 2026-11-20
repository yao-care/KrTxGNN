---
layout: default
title: Imatinib
parent: 모델 예측만 (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-15
description: "Imatinib: 예측 신규 적응증 심장 섬유육종 (heart fibrosarcoma) (근거 수준 L5). 기존 적응증: 1. 만성골수성백혈병(Chronic Myeloid Leukemia; CML) - 필라델피아 염색체 양성인…"
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
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

## Imatinib: 만성 골수성 백혈병 등 기존 적응증에서 심장 섬유육종으로
{: .text-alpha }

## 한 문장 요약

Imatinib은 BCR-ABL, KIT, PDGFR 티로신 키나제를 억제하는 약물로, 한국에서 20건의 허가증이 유효한 상태로 시판되고 있습니다.
TxGNN 모델은 **심장 섬유육종(heart fibrosarcoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험은 없고 **문헌 1편**(일반 논평)만 확인되었습니다.
이 질환 자체의 근거는 모델 예측과 기전적 추정에 그치며, 같은 섬유모세포 종양 계열인 **섬유모세포성 신생물(피부섬유육종, DFSP)**에서 상대적으로 근거가 많습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 만성골수성백혈병(Chronic Myeloid Leukemia; CML) - 필라델피아 염색체 양성인 만성기, 가속기, 급성기 만성 골수성백혈병 성인 및 소아 환자에서의 이 약의 효과는 만성골수성백혈병 성인 환자에서의 경우 전반적인 혈액학적, 세포유 전학적 반응, 무진행… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201307123/EE)) |
| 예측 신규 적응증 | 심장 섬유육종 (heart fibrosarcoma) |
| TxGNN 예측 점수 | 0.9994 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 최소 20건) |
| 허가증 수 | 최소 20건 |
| 권장 결정 | Hold |

> 참고: 이 보고서에 정리된 데이터에서 허가 적응증 본문은 확인되지 않았습니다. 기존 적응증은 허가사항(MFDS)에서 별도 확인이 필요합니다.

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Imatinib 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “이매티닙 메실산염은 단백질-티로신 키나아제 억제제로서, CML에서 필라델피아 염색체 이상에 의해 생성되는 구성적 비정상 티로신 키나아제인 BCR-ABL 티로신 키나아제를 억제한다. 이매티닙은 BCR-ABL 양성 세포주뿐만 아니라 필라델피아 염색체 양성 만성 골수성 백혈병 환자에게서 채취한 신선한 백혈병 세포에서도 증식을 억제하고 세포자멸사를 유도한다.” 영어 원문: "Imatinib mesylate is a protein-tyrosine kinase inhibitor that inhibits the BCR-ABL tyrosine kinase, the constitutive abnormal tyrosine kinase created by the Philadelphia chromosome abnormality in CML. Imatinib inhibits proliferation and induces apoptosis in BCR-ABL positive cell lines as well as fresh leukemic cells from Philadelphia chromosome positive chronic myeloid leukemia." ([DailyMed: Gleevec (imatinib mesylate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=211ef2da-2868-4a77-8055-1cb2cd78e24b), 버전 2026-07-13; 확인일 2026-11-19). 알려진 정보에 따르면, Imatinib은 PDGFR, KIT, ABL 키나제를 억제하는 단일제 티로신 키나제 억제제입니다. 이 기전은 해당 키나제에 의존하는 종양에서 효능을 기대하게 합니다.

섬유육종 계열 종양 중 COL1A1-PDGFB 융합을 가진 종양(DFSP 등)은 PDGFB/PDGFR 신호에 의존할 수 있어 기전상 그럴듯합니다. 다만 심장 특이적 데이터는 없으며, 확인된 문헌 1편은 imatinib의 새로운 적응증에 대한 일반 논평으로 "견고한 근거는 아니다"라는 취지입니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Imatinib의 적응증 확대를 다룬 논평. Ph+ 급성 림프모구성 백혈병 등에서 혈액학적 반응은 높았으나, 근거는 견고하지 않다고 평가 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200611516 | 글리벡필름코팅정100밀리그램 (한국노바티스) | 필름코팅정 | 허가사항 문서 참조 |
| 201307123 | 글리닙정200밀리그램 (동아에스티) | 필름코팅정 | 허가사항 문서 참조 |
| 201307122 | 글리마정400밀리그램 (보령) | 필름코팅정 | 허가사항 문서 참조 |
| 201306373 | 글리티브필름코팅정400밀리그램 (한미약품) | 필름코팅정 | 허가사항 문서 참조 |
| 202500744 | 이마벡정400밀리그램 (대웅제약) | 필름코팅정 | 허가사항 문서 참조 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 표적치료제 (티로신 키나제 억제제) |
| 골수억제 위험 | 허가사항의 경고 및 주의사항을 참조하세요. 다만 약물-질환 금기 정보에 호중구감소증, 혈소판감소증, 빈혈, 무과립구증이 포함되어 있어 혈구 감소에 유의가 필요합니다. |
| 구토 유발성 등급 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 모니터링 항목 | CBC, 간기능, 신기능, 체액 저류·심기능 (금기 관련 질환 정보 기반) |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **금기 관련 질환 (지식그래프 기반, 허가 문구 아님)**: 간부전·간질환, 신장질환, 울혈성 심부전·심부전, 관상동맥질환, 심낭삼출, 폐부종, 뇌부종, 호중구감소증, 무과립구증, 혈소판감소증, 빈혈, 당뇨병·당뇨병성 케톤산증, 고혈압, 활동성 소화성 궤양, 길버트 증후군 등.
- **약물 상호작용**: 총 100건이 조회되었으며, 대표 항목은 다음과 같습니다.
  - 중대(Major): Eliglustat, Naloxegol
  - 중등도(Moderate): Hydrocortisone, Dexamethasone, Clarithromycin, Cimetidine, Pioglitazone, Glimepiride, Morphine 등
- 다른 순위 질환(예: 피부섬유육종)의 문헌에서 imatinib 유발 DRESS(호산구증가·전신증상을 동반한 약물 반응) 증례가 보고되었으므로 중증 피부·과민반응에 주의가 필요합니다.

허가사항상 경고·금기 문구는 별도로 확인해야 합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
심장 섬유육종에 대해서는 직접적인 임상시험이 없고 문헌도 일반 논평 1편뿐이어서 모델 예측과 기전적 추정에 의존합니다. 심장 특이적 근거가 없으므로 현 단계에서 진행을 권하기 어렵습니다.

**진행하려면 필요한 것:**
- 심장 섬유육종 환자에서의 imatinib 사례 보고·코호트 등 직접 근거 확보
- 종양의 COL1A1-PDGFB 융합 여부 및 PDGFR/KIT 의존성 확인 (일반 섬유육종은 이 융합이 없어 기전이 적용되지 않을 수 있음)
- MFDS 허가사항의 적응증·경고·금기 확인 (안전성 선별 전 필수)
- 작용 기전(MOA) 데이터 보강
- 참고: 같은 모델 예측 중 **섬유모세포성 신생물(피부섬유육종 중심)**은 가이드라인과 다수 문헌이 있어 L3, "Proceed with Guardrails" 수준으로, 우선 검토 후보가 될 수 있습니다.

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Gleevec (imatinib mesylate) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=211ef2da-2868-4a77-8055-1cb2cd78e24b) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

