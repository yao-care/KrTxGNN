---
layout: default
title: 다운로드
nav_order: 94
permalink: /downloads/
description: "KrTxGNN 공개 데이터 다운로드: FHIR 리소스, 예측 결과, 검색 인덱스."
---

# 다운로드

<div class="key-takeaway">
예측 결과는 FHIR R4 형식으로 공개되어 EHR 시스템과 바로 연동할 수 있습니다.
</div>

---

## FHIR 리소스

본 사이트는 예측 결과를 FHIR R4 리소스로 공개하며, SMART on FHIR 앱에서 직접 사용할 수 있습니다:

| 리소스 | 경로 | 설명 |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | FHIR 서버 기능 명세 |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | 의약품 리소스 |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | 예측된 적응증 |
| Bundle | `/fhir/Bundle/all-predictions.json` | 전체 예측 번들 |

---

## 검색 인덱스

`/data/search-index.json`은 의약품과 적응증의 검색 인덱스를 제공하므로, 이를 이용해 자체
조회 인터페이스를 구축할 수 있습니다.

---

## 이용 약관

<ol class="actionable-steps">
<li>본 사이트의 데이터는 <strong>연구 참고용으로만</strong> 제공되며 의료적 판단의 근거로 사용해서는 안 됩니다.</li>
<li>인용 시 KrTxGNN (藥提醒科技有限公司)을 밝히고 TxGNN 원논문을 함께 인용하십시오.</li>
<li>2차 활용 데이터에도 각 원출처의 라이선스 조건이 그대로 적용됩니다(<a href="{{ '/sources/' | relative_url }}">데이터 출처</a> 참조).</li>
</ol>

---

## 개발사 소개

본 플랫폼은 **藥提醒科技有限公司** (yao.care, 사업자등록번호 83620786, 12F, No. 220, Sec. 2,
Taiwan Blvd., West Dist., Taichung City, Taiwan)가 개발하고 운영합니다.

KrTxGNN은 이 회사의 "TxGNN 약물재창출" 제품군 중 대한민국 사이트입니다.
동일한 시스템이 30개 국가 및 지역에 배포되어 있으며, 각각 `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN 등)으로 명명되어 `{cc}txgnn.yao.care`에서 운영됩니다.
제품 개요: <https://www.yao.care/medical/txgnn/>.

TxGNN 모델 자체는 Harvard Medical School의 Zitnik Lab이 개발하여 *Nature Medicine*에
발표했습니다. 본 플랫폼은 藥提醒科技有限公司가 해당 모델을 기반으로 구축한 운영 시스템으로,
국가별 의약품 허가 데이터 통합, 지식 그래프와 딥러닝의 이중 예측, PubMed / ClinicalTrials
근거 등급화, SMART on FHIR 전자의무기록 연동을 포함합니다.

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
