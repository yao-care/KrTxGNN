---
layout: default
title: Letrozole
parent: 모델 예측만 (L5)
nav_order: 470
evidence_level: L5
indication_count: 4
monitor_inn: "LETROZOLE"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
last_modified_at: 2026-11-20
description: "Letrozole: 예측 신규 적응증 유두암 (nipple carcinoma) (근거 수준 L5). 기존 적응증: 1. 에스트로겐 또는 프로게스테론 수용체 양성이거나 또는 수용체 상태가 알려지지 않은 폐경후 여성의…"
---

# Letrozole
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

## Letrozole: 방향족화효소 억제제 → 유두암 (nipple carcinoma)
{: .text-alpha }

## 한 문장 요약

Letrozole은 방향족화효소(아로마타제) 억제제 계열의 약물로, 한국에서 단일 성분 제제로 허가되어 있습니다.
TxGNN 모델은 **유두암(nipple carcinoma)**에 효과가 있을 수 있다고 예측하지만, 이 질환을 직접 다룬 임상시험은 없고 **8편의 문헌**(대부분 증례 보고)만 확인됩니다.
따라서 현재 근거는 모델 예측 수준(L5)에 머물러 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 1. 에스트로겐 또는 프로게스테론 수용체 양성이거나 또는 수용체 상태가 알려지지 않은 폐경후 여성의 국소적으로 진전된 또는 전이성 유방암에서 1차 치료 2. 항에스트로겐 요법후 재발된 자연적 또는 인공적으로 폐경이 된 여성의 진전된 유방암 3. 에스트로겐 또는 프로게스테론 수용체… ([MFDS 허가사항 PDF](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201500168/EE)) |
| 예측 신규 적응증 | 유두암 (nipple carcinoma) |
| TxGNN 예측 점수 | 0.9976 |
| 근거 수준 | L5 |
| 한국 시판 현황 | 시판 중 (유효 허가 6건 / 전체 6건) |
| 허가증 수 | 6건 (유효 6건) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

미국 FDA가 승인한 Letrozole 처방 정보(Prescribing Information)의 “Mechanism of Action” 항목에 따르면(비공식 번역): “일부 유방암의 성장은 에스트로겐에 의해 촉진되거나 유지된다. 호르몬 반응성으로 생각되는(즉, 에스트로겐 수용체 및/또는 프로게스테론 수용체 양성이거나 수용체 상태가 알려지지 않은) 유방암의 치료에는 에스트로겐 수치를 감소시키거나(난소절제술, 부신절제술, 뇌하수체절제술) 에스트로겐 효과를 억제하기 위한(항에스트로겐제 및 프로게스틴제) 다양한 시도가 포함되어 왔다. […] 레트로졸은 아로마타제 효소계의 비스테로이드성 경쟁적 억제제로, 안드로겐이 에스트로겐으로 전환되는 것을 억제한다.” 영어 원문: "The growth of some cancers of the breast is stimulated or maintained by estrogens. Treatment of breast cancer thought to be hormonally responsive (i.e., estrogen and/or progesterone receptor positive or receptor unknown) has included a variety of efforts to decrease estrogen levels (ovariectomy, adrenalectomy, hypophysectomy) or inhibit estrogen effects (antiestrogens and progestational agents). […] Letrozole is a nonsteroidal competitive inhibitor of the aromatase enzyme system; it inhibits the conversion of androgens to estrogens." ([DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406), 버전 2026-06-11; 확인일 2026-11-19). 다만 letrozole은 방향족화효소 억제제 계열로 알려져 있으며, 이 계열은 에스트로겐 의존성 유방 질환에서 사용됩니다.

유두암은 유방암의 하위 유형이므로, 종양이 호르몬 수용체 양성이라면 방향족화효소 억제가 기전상 적용 가능할 수 있습니다. 그러나 이를 뒷받침하는 질환 특이적 근거는 아직 없으며, 수용체 상태에 따라 적합성이 달라질 수 있습니다.

## 임상시험 근거

현재 관련 임상시험 등록이 없습니다.

## 문헌 근거

모두 증례 보고 또는 소규모 보고이며, letrozole의 유두암 치료 효과를 직접 평가한 연구는 없습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [33120755](https://pubmed.ncbi.nlm.nih.gov/33120755/) | 2020 | 코호트/증례 | Medicine | 저분화 신경내분비 유방암에서 선행 내분비요법의 효과를 보고 |
| [41607681](https://pubmed.ncbi.nlm.nih.gov/41607681/) | 2026 | 증례 보고 | Clinical Case Reports | 유두에서 기원한 고형 유두상 상피내암 증례 및 문헌 고찰 |
| [34495428](https://pubmed.ncbi.nlm.nih.gov/34495428/) | 2021 | 증례 보고 | Surgical Case Reports | 유방 아래 부위 副유방암 증례 |
| [40395253](https://pubmed.ncbi.nlm.nih.gov/40395253/) | 2025 | 증례 보고 | Cureus | 혈성 유두 분비를 보인 유방암의 비정형 액와 재발 |
| [39682607](https://pubmed.ncbi.nlm.nih.gov/39682607/) | 2024 | 증례 보고 | Diagnostics | 전이성 副유방암과 동측 유방암의 동시 발생 |
| [42040393](https://pubmed.ncbi.nlm.nih.gov/42040393/) | 2026 | 증례 보고 | Clinical Case Reports | 역극성 유방 Tall cell 암종의 IDH1 변이 |
| [42305961](https://pubmed.ncbi.nlm.nih.gov/42305961/) | 2026 | 증례 보고 | Frontiers in Medicine | 副유방암, 갑상선 유두암, 비강 유두종의 동시 발생 |
| [42416948](https://pubmed.ncbi.nlm.nih.gov/42416948/) | 2026 | 증례 보고 | Cureus | florid 소엽상피내암의 초음파 소견 |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201500168 | 파누엘정2.5밀리그램 | 필름코팅정 | 허가 문서 링크만 제공됨 |
| 202402459 | 레트로보정2.5밀리그램 | 필름코팅정 | 허가 문서 링크만 제공됨 |
| 200108765 | 페마라정 | 필름코팅정 | 허가 문서 링크만 제공됨 |
| 202403042 | 페트라정 | 필름코팅정 | 허가 문서 링크만 제공됨 |
| 201500998 | 테바레트로졸정2.5밀리그램 | 필름코팅정 | 허가 문서 링크만 제공됨 |

## 세포독성

| 항목 | 내용 |
|------|------|
| 세포독성 분류 | 호르몬 요법(방향족화효소 억제제), 전통적 세포독성 약물 아님 |
| 골수억제 위험 | 낮음 |
| 구토 유발성 등급 | 낮음 |
| 모니터링 항목 | 허가사항의 경고 및 주의사항을 참조하세요 |
| 취급 방호 | 허가사항의 경고 및 주의사항을 참조하세요 |

## 안전성 고려사항

- **약물 상호작용**: 총 100건이 조회되었습니다. 이 중 등급이 확인된 항목은 Aprepitant(중등도)이며, 나머지 주요 항목(Calcitriol, Glimepiride, Lansoprazole, Dolasetron, Granisetron, Famotidine, Acetylsalicylic acid, Pantoprazole, Morphine, Metformin 등)은 등급이 미상입니다.
- 간부전, 간경변, 골다공증, 고빌리루빈혈증, 길버트 증후군, 뇌혈관 질환 등은 주의가 필요한 질환으로 참고됩니다. 다만 이는 허가 문서 기반 정보가 아니므로 허가사항 확인이 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
유두암을 직접 다룬 임상시험이 없고 문헌도 증례 보고 위주여서, 근거는 모델 예측 수준(L5)입니다. 허가사항 기반의 경고·금기 정보도 확보되지 않았습니다.

**진행하려면 필요한 것:**
- 허가사항(첨부문서) 확보 및 경고·금기 확인
- 상세한 작용 기전(MOA) 데이터
- 호르몬 수용체 양성 유두암에서 letrozole의 효과를 평가한 임상 또는 관찰 연구
- 한국 시판 및 허가 취소 현황 확인

<!-- review:begin log -->

## 검토 기록

아래는 이 페이지의 검토 기록입니다. 작용 기전 자료가 없다는 문장을 인용한 공식 처방 정보의 발췌문(비공식 번역 포함)으로 교체했습니다. 모델 예측, 근거 수준, 결론은 다시 쓰지 않았습니다.

| 검토일 | 항목 | 처리 | 근거 |
|------|------|------|------|
| 2026-11-19 | “작용 기전 데이터가 없습니다” 문장을 미국 처방 정보 발췌문으로 교체 | 작용 기전 자료가 없다는 문장을 출처가 있는 발췌문으로 교체 | [DailyMed: Femara (letrozole) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=82b77d74-085f-45ac-a7dd-1f5c038bf406) |

<!-- review:end log -->

## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

