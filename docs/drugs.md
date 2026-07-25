---
layout: default
title: 전체 의약품
nav_order: 20
permalink: /drugs/
description: "KrTxGNN의 전체 의약품 검증 보고서 및 근거 등급 통계."
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# 전체 의약품

{{ site.drugs.size }}건의 의약품 검증 보고서

---

## 근거 등급별 분포

| 근거 등급 | 의약품 수 | 설명 |
|---------|--------|------|
| **L1** | {{ l1_count }} | 다수의 RCT / 체계적 문헌고찰 |
| **L2** | {{ l2_count }} | 단일 RCT / 2상 시험 |
| **L3** | {{ l3_count }} | 관찰 연구 / 대규모 증례 시리즈 |
| **L4** | {{ l4_count }} | 전임상 / 기전 연구 |
| **L5** | {{ l5_count }} | 모델 예측만 존재 |

---

## 전체 의약품 목록

{% assign all_drugs = site.drugs | sort: 'title' %}

| 의약품 | 근거 등급 | 적응증 수 |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
