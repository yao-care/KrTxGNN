---
layout: default
title: 중등도 근거 (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "KrTxGNN의 L3-L4 약물재창출 후보로, 관찰 연구 또는 전임상 근거가 뒷받침합니다."
---

# 중등도 근거 (L3-L4)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
예비적 근거가 있으나 추가 검증이 필요한 후보
</p>

---

## 기준

| 등급 | 정의 | 임상적 의미 |
|-------|------------|------------------|
| **L3** | 관찰 연구 / 대규모 증례 시리즈 | 예비적 근거; 추가 검증이 필요함 |
| **L4** | 전임상 / 기전 연구 | 이론적 근거; 임상 적용과는 거리가 있음 |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }}건)

| 의약품 | 적응증 수 | 링크 |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [보고서 보기]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }}건)

| 의약품 | 적응증 수 | 링크 |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [보고서 보기]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
