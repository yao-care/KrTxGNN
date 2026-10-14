---
layout: default
title: Mycophenolate Mofetil
parent: 모델 예측만 (L5)
nav_order: 532
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
{: .fs-9 }

근거 수준: **L5** | 예측 적응증: **10** 건
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

# 미코페놀레이트 모페틸(Mycophenolate Mofetil): 장기이식 거부반응 예방에서 HIV 감염으로

## 한 문장 요약

미코페놀레이트 모페틸은 면역억제제로, 이식 장기 거부반응 예방에 사용되어 온 약입니다(문헌 초록 기준).
TxGNN 모델은 **HIV 감염(HIV infectious disease)**에 효과가 있을 수 있다고 예측합니다.
이 방향과 관련된 자료는 **4건의 임상시험**과 **20편의 문헌**이지만, 효능이 모호하거나 근거 가치가 낮은 자료가 많아 실제 지지 강도는 제한적입니다.

## 빠른 개요

| 항목 | 내용 |
|------|------|
| 기존 적응증 | 이식 장기 거부반응 예방 (허가 적응증 원문은 허가증 링크로만 제공되어 문헌 기술을 참고함) |
| 예측 신규 적응증 | HIV 감염 (HIV infectious disease) |
| TxGNN 예측 점수 | 99.86% |
| 근거 수준 | L2 (완료된 Phase 2 무작위 임상시험 1건 및 RCT 문헌 1편, 다만 효과는 제한적) |
| 한국 시판 현황 | ✓ 시판 중 |
| 허가증 수 | 6건 |
| 권장 결정 | Hold |

## 이 예측이 타당한 이유는?

현재 데이터베이스에는 상세한 작용 기전 항목이 비어 있습니다. 다만 이번 분석 자료에 따르면 미코페놀산(미코페놀레이트의 활성 형태)은 IMPDH(이노신 일인산 탈수소효소)를 억제합니다. 이로 인해 림프구 내 구아노신 뉴클레오티드가 고갈되고 T세포 증식이 억제됩니다.

HIV는 활성화된 T세포 안에서 증식하므로, 면역 과활성화와 T세포 증식을 줄이는 접근은 이론적으로 의미가 있습니다. 또한 구아닌 뉴클레오티드(dGTP)가 감소하면 abacavir, didanosine 같은 뉴클레오시드 유사체 항레트로바이러스제의 활성이 강화될 수 있습니다. 실제로 abacavir 포함 요법에 이 약을 추가했을 때 세포 내 dGTP가 감소하고 혈장 HIV-1 RNA가 줄었다는 소규모 보고(5명)가 있습니다.

그러나 효능은 제한적이었고, 면역억제는 HIV 환자의 감염 위험을 높일 수 있습니다. 그래서 기전상 그럴듯하지만 임상적 유용성은 아직 입증되지 않았습니다.

## 임상시험 근거

| 시험 번호 | 단계 | 상태 | 참여자 수 | 주요 발견 |
|---------|------|------|----------|---------|
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | 완료 | 56 | 치료 경험이 있는 HIV 환자에서 DAPD 단독 대 DAPD+MMF를 비교한 무작위 이중맹검 위약대조 예비연구. 결과 요약은 제공되지 않았고 관련성은 낮게 평가됨 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 조기 종료 | 8 | 항-rHuEpo 연관 순수적혈구무형성증에서 cyclosporine+MMF와 cyclophosphamide+prednisolone 비교. HIV 적응증이 아니며 8명만 등록 |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | 해당 없음 | 완료 | 5 | HIV 양성 환자의 조혈모세포이식 후 혼합 키메라 유도 연구. MMF는 이식 후 면역억제 요법의 일부일 뿐임 |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | 철회 | 0 | abacavir 병용 MMF의 안전성과 항레트로바이러스 활성을 보려던 시험. 참여자 0명으로 데이터 없음 |

## 문헌 근거

| PMID | 연도 | 유형 | 저널 | 주요 발견 |
|------|-----|------|------|---------|
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | RCT | AIDS | 치료 경험이 없는 HIV-1 환자에서 HAART에 MMF를 추가했을 때 혈장 HIV-1 RNA 감소 속도와 잠복 감염 세포 저장고에 미치는 영향 평가 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | 소규모 환자군 보고 | J Acquir Immune Defic Syndr | 치료 실패 환자 5명에서 abacavir 포함 요법에 MMF 추가 시 세포 내 dGTP 고갈 및 혈장 HIV-1 RNA 감소 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | 코호트 | Clin Pharmacokinet | abacavir, efavirenz, nelfinavir 치료 HIV 환자에서 저용량 MMF의 약동학/약력학. 용량이 낮아 모니터링 권고 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | 단신(Short communication) | AIDS Res Hum Retroviruses | 치료 경험이 없는 급성·만성 HIV-1 환자에서 MMF+HAART 병용이 면역 기능에 해로운 영향을 주지 않음 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | HIV 질환에서 만성 면역 활성화를 표적으로 하는 면역억제제의 역할 고찰 |
| [16515490](https://pubmed.ncbi.nlm.nih.gov/16515490/) | 2006 | Review | Curr Pharm Des | 바이러스 증식 억제제(virostatics)를 통한 HIV 감염 표적화 접근 고찰 |
| [12003181](https://pubmed.ncbi.nlm.nih.gov/12003181/) | 2002 | Review | J Biol Regul Homeost Agents | HIV-1 장기 조절을 위한 면역 조절 접근의 잠재적 역할 |
| [20840478](https://pubmed.ncbi.nlm.nih.gov/20840478/) | 2010 | 후향 연구 | Am J Transplant | HIV 감염 신장이식 환자 27명(파리). MMF, 스테로이드, 타크로리무스 또는 cyclosporine 병용 면역억제 |
| [23622672](https://pubmed.ncbi.nlm.nih.gov/23622672/) | 2013 | 코호트/문헌고찰 | Transplant Proc | 스페인 3차 병원의 HIV 감염 신장이식 경험 및 문헌고찰 |

## 한국 시판 정보

허가 적응증 원문은 아래 허가증 링크에서만 확인할 수 있습니다. 총 6건 중 주요 5건을 나열합니다.

| 허가번호 | 제품명 | 제형 | 허가 적응증 |
|---------|------|------|-----------|
| 200606303 | 마이코놀캡슐250밀리그램 (한미약품) | 경질캡슐 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200606303/EE) |
| 200805418 | 마이렙트캡슐250밀리그램 (종근당) | 경질캡슐 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200805418/EE) |
| 200610652 | 셀셉트캡슐250밀리그램 (한국로슈) | 경질캡슐 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200610652/EE) |
| 200803703 | 이뮤셉트캡슐 (광동제약) | 경질캡슐 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/200803703/EE) |
| 201401967 | 마이렙트현탁용분말1g/5ml (종근당) | 현탁용 분말 | [허가증 원문 참조](https://nedrug.mfds.go.kr/pbp/cmn/pdfDownload/201401967/EE) |

## 안전성 고려사항

허가사항의 경고 및 금기 정보는 이번 자료에 포함되어 있지 않으므로 허가사항을 직접 참조해야 합니다.

- **지식그래프 기반 금기 질환** (허가 문구가 아닌 TxGNN 지식그래프의 약물-질환 금기 연결 정보):
  - 감염성: 단순 헤르페스, 대상포진, 거대세포바이러스 감염, 진행성 다초점 백질뇌병증
  - 혈액 관련: 호중구감소증, 무과립구증, 재생불량성 빈혈(유전성 포함), Fanconi 빈혈 및 관련 골수부전 증후군
  - 악성 종양: 림프종, 원발성 중추신경계 림프종, 피부암 등
  - 기타: 간질환, 담낭질환, 활동성 소화성 궤양
  
  감염 및 악성 종양 관련 항목은 면역 저하 상태인 HIV 환자에서 특히 주의가 필요합니다.
- **약물 상호작용** (총 92건 확인):
  - **Major**: 활성탄
  - **Moderate**:
    - 위산억제제: rabeprazole, omeprazole, esomeprazole, lansoprazole, dexlansoprazole
    - 제산제·무기질: 수산화알루미늄, 산화마그네슘, 탄산칼슘
    - 항생제: doxycycline, tetracycline, minocycline, amoxicillin, clarithromycin, vancomycin, kanamycin, paromomycin
  - **Minor**: 아연, 철분
  
  HIV 환자는 항레트로바이러스제를 병용하므로 추가적인 상호작용 평가가 필요합니다.

## 결론 및 다음 단계

**결정: Hold**

**사유:**
이론적 기전과 소규모 임상 보고는 있지만, 효능은 제한적이었고 직접 관련된 시험은 철회되었거나 결과가 없습니다. 면역억제에 따른 감염 위험도 HIV 환자에게는 큰 부담이며, 허가사항의 안전성 정보가 확인되지 않아 안전성 심사도 진행할 수 없습니다.

**진행하려면 필요한 것:**
- 한국 허가사항(경고·금기)의 확인 및 분석
- HIV 환자에서 MMF의 임상적 이득(바이러스 부하, CD4, 잠복 저장고)을 확인하는 대규모 무작위 대조시험 근거
- 항레트로바이러스제와의 약물 상호작용 평가와 기회감염 위험에 대한 모니터링 계획
- 상세한 작용 기전 데이터 보완
## 면책 조항

본 콘텐츠는 연구 목적으로만 제공되며 의학적 조언을 구성하지 않습니다.
임상 적용 전에 임상적 검증이 필요합니다.

---

