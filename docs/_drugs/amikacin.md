---
layout: default
title: Amikacin
parent: 모델 예측만 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
monitor_inn: "Amikacin"
predicted_indications: ["paratyphoid fever", "diffuse scleroderma", "punctate epithelial keratoconjunctivitis", "typhoid fever", "epiglottitis", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "meningococcemia"]
last_modified_at: 2026-10-28
description: "Amikacin: 예측 신규 적응증 파라티푸스 (근거 수준 L4). 기존 적응증: 허가 적응증 본문이 문서 링크로만 제공되어 구체적인 질환명을 확인할 수 없음 (아미노글리코시드계 항균제)"
---

# Amikacin
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

## Amikacin: 아미노글리코시드계 항생제에서 파라티푸스로
{: .text-alpha }

## 한 문장 요약

Amikacin은 그람음성균 감염에 쓰이는 아미노글리코시드계 주사 항생제입니다. TxGNN 모델은 **파라티푸스(Paratyphoid Fever)**에 효과가 있을 수 있다고 예측했습니다. 다만 관련 임상시험은 **0건**이고, 문헌 **8편**은 대부분 역학·항생제 감수성 조사와 증례 보고여서 Amikacin의 임상 효능을 직접 입증하지 못합니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 허가 적응증 본문이 문서 링크로만 제공되어 구체적인 질환명을 확인할 수 없음 (아미노글리코시드계 항균제) |
| 예측 신규 적응증 | 파라티푸스 |
| TxGNN 예측 점수 | 0.9982 |
| 근거 수준 | L5 |
| 한국 시판 현황 | Unknown (source lacks cancellation status) |
| 허가증 수 | 최소 20건 (목록이 일부일 수 있음) |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 상세한 작용 기전 데이터는 확보되지 않았습니다. 알려진 정보에 따르면 Amikacin은 세균의 30S 리보솜 소단위에 결합하는 아미노글리코시드계 항생제입니다. 살모넬라를 포함한 그람음성 간균에 시험관 내 활성이 있습니다. 파라티푸스는 살모넬라(Salmonella Paratyphi)가 일으키는 감염이므로, 균에 대한 항균 활성만 보면 모델의 예측은 이해할 만합니다.

그러나 임상 적용에는 큰 한계가 있습니다. 살모넬라는 세포 내에 존재하는데 아미노글리코시드는 세포 내 침투가 약해, 시험관 내 감수성이 생체 내 효능으로 이어지지 않는 것으로 알려져 있습니다. Amikacin은 장티푸스·파라티푸스(장열)의 표준 치료제가 아니며, 이번에 수집한 문헌에도 Amikacin의 효능을 보여주는 대조 연구는 없습니다.

## 문헌 근거

파라티푸스를 직접 다룬 문헌은 있지만, Amikacin의 치료 효능을 평가한 연구는 없습니다. 임상시험 등록도 없습니다. 아래 표에는 RCT나 체계적 문헌고찰이 없어 코호트와 증례 보고를 연도순으로 정리했습니다.

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | 증례 보고 | Pediatr Hematol Oncol | 급성 전구 B세포 백혈병 소아의 Paratyphi B 무결석성 담낭염을 cefepime, amikacin, 과립구 집락자극인자로 치료해 성공 |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | 코호트 | Mikrobiyoloji Bulteni | 기존 치료에 내성인 Paratyphi B 감염 소아 48명의 항생제 치료 및 감수성 결과 보고 |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | 코호트 | New Microbiologica | 요르단의 S. typhi·S. paratyphi 발생 현황 역학 조사 |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | 코호트 | Med J Armed Forces India | 장열 45례에서 Typhi·Paratyphi A의 시험관 내 항생제 감수성 패턴 확인 (chloramphenicol 감수성 재출현) |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | 코호트 | J Indian Med Assoc | 소아 장열 145례의 임상상과 Typhi·Paratyphi 항생제 감수성 조사 |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | 코호트 | JNMA | 교육병원 혈액배양 분리균의 빈도와 항생제 감수성 조사 |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | 코호트 | Pak J Biol Sci | 파키스탄 퀘타의 장열 환자에서 S. Paratyphi 분리·동정 |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | 코호트 | J Pediatr Surg | 소아 비장 농양을 천자 배농과 항생제로 치료한 4례 보고 |

## 한국 시판 정보

한국에는 Amikacin 단일 성분 주사제 허가가 최소 20건 확인되며, 모두 단일 성분이고 유효 상태입니다. 목록은 일부일 수 있습니다. 제품명에 "수출용"이 붙은 허가가 다수 포함되어 있어, 국내 실제 유통 여부는 별도 확인이 필요합니다. 허가 적응증 본문은 첨부 문서 링크로만 제공되어 내용을 요약하지 못했습니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 201002333 | 제일제약아미카신황산염주500mg (수출용) | 앰플 주사제 | 허가 문서 링크 참조 |
| 198900080 | 신풍아미카신황산염주사액500밀리그램 | 바이알/프리필드 주사제 | 허가 문서 링크 참조 |
| 201502807 | 동광아미카신주250mg | 앰플 주사제 | 허가 문서 링크 참조 |
| 199202953 | 아디칸주사액500밀리그램 | 앰플/바이알 주사제 | 허가 문서 링크 참조 |
| 200200253 | 중외아미카신황산염프리믹스주 | 플라스틱/유리 용기 주사제 | 허가 문서 링크 참조 |

## 안전성 고려사항

- **약물 상호작용**: 상호작용 조사에서 총 100건이 확인되었고, 그중 상위 20건을 검토했습니다.
  - **주요(Major) 등급**: 황산마그네슘(Magnesium sulfate), 만니톨(Mannitol)
  - **중등도(Moderate) 등급**: 암포테리신 B 제제(일반·지질 복합체·리포좀·콜레스테릴 설페이트), 카나마이신, 네오마이신, 아스피린, 메살라진 계열(Mesalazine, Balsalazide, Olsalazine), 프로톤펌프억제제(Omeprazole, Esomeprazole, Lansoprazole, Dexlansoprazole, Pantoprazole, Rabeprazole), 엑세나타이드

경고와 금기 정보는 허가사항을 참조하세요.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
- 파라티푸스에서 Amikacin의 효능을 보여주는 임상시험이나 대조 연구가 없고, 문헌은 감수성 조사와 증례 보고에 그칩니다.
- 아미노글리코시드는 세포 내 감염에 효과가 제한적이며, 이미 확립된 표준 치료제(플루오로퀴놀론, 아지트로마이신, 3세대 세팔로스포린)가 있습니다.
- TxGNN 점수는 높지만 계산상 예측일 뿐이어서 임상 개발을 정당화하기 어렵습니다.

**진행하려면 필요한 것:**
- 작용 기전 데이터 확보 (DrugBank 등)
- 허가사항(경고·금기·적응증 본문) 확보 및 분석
- 파라티푸스 환자에서 Amikacin의 임상 효능을 평가한 연구, 또는 표준 치료제 대비 이점을 보여주는 근거
- 한국 시판 현황(취소 여부, 수출 전용 여부) 확인
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

