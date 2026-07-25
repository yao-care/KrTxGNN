---
layout: default
title: 높은 근거 (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "KrTxGNN의 L1-L2 약물재창출 후보로, 임상시험 또는 체계적 문헌고찰이 뒷받침합니다."
---

# 높은 근거 (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
임상 평가를 우선적으로 고려할 수 있는 후보
</p>

---

## 기준

| 등급 | 정의 | 임상적 의미 |
|-------|------------|------------------|
| **L1** | 다수의 3상 RCT / 체계적 문헌고찰 | 강력한 근거; 임상 적용을 고려할 수 있음 |
| **L2** | 단일 RCT 또는 다수의 2상 시험 | 중등도 근거; 검증 시험을 설계할 수 있음 |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }}건)

| 의약품 | 적응증 수 | 링크 |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [보고서 보기]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }}건)

| 의약품 | 적응증 수 | 링크 |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [보고서 보기]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
