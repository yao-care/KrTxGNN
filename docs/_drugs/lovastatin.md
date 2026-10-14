---
layout: default
title: Lovastatin
parent: 모델 예측만 (L5)
nav_order: 486
evidence_level: L5
indication_count: 6
---

# Lovastatin
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **6** 건
{: .fs-6 .fw-300 }

---

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 약사 평가 보고서

</div>

# Lovastatin: 고콜레스테롤혈증에서 동형접합 가족성 고콜레스테롤혈증으로

## 한 문장 요약

Lovastatin은 HMG-CoA 환원효소를 억제하는 스타틴 계열 약물로, 원래 고콜레스테롤혈증 등 지질 이상 치료에 사용되어 왔습니다.
TxGNN 모델은 **동형접합 가족성 고콜레스테롤혈증(Homozygous Familial Hypercholesterolemia, HoFH)**에 효과가 있을 수 있다고 예측합니다.
다만 이 질환에서 lovastatin을 직접 검증한 임상시험은 없고(등록된 1건은 다른 약물인 alirocumab 시험), 소규모 임상 보고와 증례 위주의 문헌 근거만 있습니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 고콜레스테롤혈증 등 지질 이상 (허가증이 문서 링크로만 제공되어 본문 확인 불가, 약물 계열 기준으로 기재) |
| 예측 신규 적응증 | 동형접합 가족성 고콜레스테롤혈증 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 예측 점수 | 99.89% |
| 근거 수준 | L3 (소규모 임상 관찰·증례 중심, lovastatin 대상 RCT 없음) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 3건 (모두 단일제, 유효) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

Lovastatin은 HMG-CoA 환원효소를 억제해 간의 콜레스테롤 합성을 줄이고, 그 결과 간세포의 LDL 수용체 발현을 높여 혈중 LDL-C를 낮춥니다. 이 약물의 작용 기전에 관한 상세 데이터는 이번 자료에 구조화되어 있지 않아, 위 설명은 문헌과 약물 계열의 일반적 지식에 근거합니다.

HoFH는 LDL 수용체 기능이 거의 없거나 매우 낮아 LDL이 극단적으로 높아지는 질환입니다. 기존 적응증(고콜레스테롤혈증)과 같은 LDL 대사 이상이라는 점에서 예측은 기전상 일관됩니다. 그러나 lovastatin의 효과는 **잔존 LDL 수용체 활성**에 좌우됩니다. 수용체 음성 환자에서는 LDL-C가 줄지 않았다는 보고가 있고(PMID 3397806), 수용체 결함형 환자에서는 일부 반응이 보고되었습니다(PMID 3534334, 1785747).

따라서 이 예측은 새로운 기전이 아니라 이미 시판 중인 지질강하제의 사용 범위를 일부 환자군(수용체 결함형)으로 좁혀 보는 성격이 강합니다. 환자의 수용체 상태에 따라 효과 차이가 크다는 점이 핵심 한계입니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 완료 | 18 | 8~17세 HoFH 소아·청소년에서 alirocumab의 LDL-C 감소 효과 평가 (공개라벨). lovastatin 시험이 아니므로 질환 배경 정보로만 참고 |

lovastatin을 HoFH에서 직접 평가한 임상시험 등록은 확인되지 않았습니다.

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | 소규모 임상연구 | The Journal of Pediatrics | 수용체 음성 HoFH 소아 3명에서 lovastatin(2 mg/kg/일) 투여 시 LDL-C 감소 및 LDL 회전율 변화 없음 |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | 증례 보고 | JAMA | 간이식을 받은 HoFH 소아에서 lovastatin 병용 시 콜레스테롤이 정상 수준으로 감소 |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | 임상연구 | Anales Españoles de Pediatría | HoFH 환자 2명에서 lovastatin을 probucol·cholestyramine과 병용, LDL 수용체 분석과 반응 확인 |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | 증례 보고 | Anales Españoles de Pediatría | 수용체 결함형 HoFH 환자에서 cholestyramine과 lovastatin 병용요법에 대한 반응 보고 |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | 증례 보고 | European Journal of Pediatrics | HoFH 7세 소녀에서 LDL 혈장분리(HELP) 치료에 lovastatin을 병행한 경과 |
| [2912428](https://pubmed.ncbi.nlm.nih.gov/2912428/) | 1989 | 임상 관찰 | Arteriosclerosis | 소아·청소년 FH(이형 30명, 동형 3명)의 약물요법별 지질 수치 평가 |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the New York Academy of Sciences | 이상지질혈증 소아·청소년의 약물·수술 치료 개관, lovastatin 포함 여러 약제가 LDL 감소에 성공 |
| [12063772](https://pubmed.ncbi.nlm.nih.gov/12063772/) | 2001 | Review | Nutrition, Metabolism and Cardiovascular Diseases | 소아에서 스타틴을 쓰는 이유와 시기 정리, FH의 조기 치료 필요성 강조 |
| [2912429](https://pubmed.ncbi.nlm.nih.gov/2912429/) | 1989 | Review | Arteriosclerosis | HoFH에서 혈장교환·LDL 아페레시스 경험, lovastatin과 아페레시스 병용 평가 진행 중 |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clinical Therapeutics | rosuvastatin 리뷰로, HoFH가 적응증에 포함됨 (lovastatin 직접 근거는 아님) |

## 한국 시판 정보

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 199701294 | 로바콜정(로바스타틴)(수출용), 명인제약 | 담청색 원형 정제 | 허가증 문서 링크로만 제공: [허가증 보기](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199701294/EE) |
| 199904161 | 로바타딘정(로바스타틴)(수출명: Lovac Tablet), 대한뉴팜 | 담청색 원형 정제(내수용·수출용1), 녹색 원형 정제(수출용2) | 허가증 문서 링크로만 제공: [허가증 보기](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/199904161/EE) |
| 200402848 | 로바이틴정(로바스타틴), 위더스제약 | 담청색 원형 정제 | 허가증 문서 링크로만 제공: [허가증 보기](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200402848/EE) |

## 안전성 고려사항

- **허가사항 경고·금기**: 이번 데이터에는 허가사항의 경고·금기 정보가 확보되지 않았습니다. 허가사항(첨부문서)을 직접 확인해야 합니다.
- **지식그래프 기반 금기 관련 질환** (허가 문구가 아닌 TxGNN 지식그래프의 약물-질환 연결 기준): 간질환, 담낭질환, 근병증·근육질환, 횡문근융해증, 혈소판감소증, 당뇨병 및 고혈당, 통풍, 관상동맥질환·심근경색, 혈액응고질환 등
- **약물 상호작용**: 총 100건이 조회되었습니다. 주요 항목은 다음과 같습니다.
  - **Major**: Clarithromycin
  - **Moderate**: Aprepitant, Omeprazole 등 프로톤펌프억제제(Esomeprazole, Lansoprazole, Pantoprazole), Metronidazole, Cimetidine, Clotrimazole, Miconazole, Simvastatin, Rosuvastatin, Troglitazone 등
  - **Minor**: Exenatide

## 결론 및 다음 단계

**결정: Hold**

**사유:**
HoFH에서 lovastatin을 직접 평가한 임상시험이 없고, 근거는 1980~90년대의 소규모 임상 보고와 증례에 한정됩니다. 수용체 음성 환자에서는 효과가 없다는 보고도 있어 반응이 수용체 상태에 크게 좌우됩니다. 참고로 같은 모델이 예측한 일반 고지단백혈증과 이형접합 가족성 고콜레스테롤혈증은 lovastatin을 직접 평가한 근거가 더 풍부하지만, 이미 기존 지질강하 적응증 범위에 해당합니다.

**진행하려면 필요한 것:**
- HoFH 환자의 LDL 수용체 상태(잔존 활성 여부)에 따른 lovastatin 반응 데이터
- lovastatin을 직접 평가한 임상시험 또는 현대적 기준의 관찰연구 근거
- 허가사항의 경고·금기 정보 확인과 안전성 검토 (근병증, 간독성 모니터링 포함)
- CYP3A4 억제제 등 상호작용 약물 관리 계획
- HoFH 표준 치료(고강도 스타틴, PCSK9 억제제, LDL 아페레시스 등)와의 비교 및 위치 설정
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

