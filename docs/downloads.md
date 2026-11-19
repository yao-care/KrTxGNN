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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## 대한민국: 현재 파일 내용

| 파일 | 현재 내용 |
|---|---|
| `/data/search-index.json` | 의약품 {{ site.data.local_facts.files.search_index }}개와 예측 적응증 |
| `/data/drugs.json` | 의약품 {{ site.data.local_facts.files.drugs_json }}개와 근거 수준·기존 적응증 |
| `/fhir/MedicationKnowledge/` | MedicationKnowledge 리소스 {{ site.data.local_facts.fhir.medication_knowledge }}개(의약품당 1개) |
| `/fhir/ClinicalUseDefinition/` | ClinicalUseDefinition 리소스 {{ site.data.local_facts.fhir.clinical_use_definition }}개(예측 적응증당 1개) |

국내 데이터셋 재사용: [의약품안전나라(nedrug) 의약품 검색](https://nedrug.mfds.go.kr/searchDrug), 식품의약품안전처이(가) 공개한 자료로, 재사용에는 공개 기관의 이용 조건이 적용되며 이 사이트가 추가 권리를 부여하지 않습니다.

{% if site.data.local_facts.top_licensed.size > 0 %}정상 의약품 허가 품목이 가장 많은 의약품: {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}검토 기록의 최근 정정: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

같은 의약품에 대해 다른 TxGNN 사이트에 없는 예측의 예: [Polmacoxib]({{ '/drugs/polmacoxib/' | relative_url }}) → acromesomelic dysplasia, Hunter-Thompson type, [Proxyphylline]({{ '/drugs/proxyphylline/' | relative_url }}) → 심장 질환.

<!-- local-facts:end -->

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

본 플랫폼은 **藥提醒科技有限公司** (yao.care)가 개발하고 운영합니다. 회사 정보, TxGNN 모델의 배경,
제품군 전체 사이트 목록은 <a href="{{ '/about/' | relative_url }}">소개</a> 페이지에서 확인할 수 있습니다.

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
