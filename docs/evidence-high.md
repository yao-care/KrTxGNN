---
layout: default
title: 높은 근거 (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "KrTxGNN의 L1-L2 약물재창출 후보로, 임상시험 또는 체계적 문헌고찰이 뒷받침합니다."
---

# 높은 근거 (L1-L2)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L1 | plus: site.data.drug_stats.level_counts.L2 %}
이 페이지에는 이 사이트에서 보고서를 공개한 의약품 **{{ site.data.drug_stats.total_drugs }}**개 중 **{{ pd_m }}**개({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%)가 실려 있습니다. 수준 정의: [방법론]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
임상 평가를 우선적으로 고려할 수 있는 후보
</p>

이 의약품 중 예측 신규 적응증에 시험 근거가 있는 것은 무엇이며, 등록 임상시험은 몇 건이 인용되었을까요? [새 적응증에 임상시험 근거가 있는 국내 의약품]({{ '/clinical-trial-evidence/' | relative_url }})을 참조하십시오.

---

## 기준

| 등급 | 정의 | 임상적 의미 |
|-------|------------|------------------|
| **L1** | 다수의 3상 RCT / 체계적 문헌고찰 | 강력한 근거; 임상 적용을 고려할 수 있음 |
| **L2** | 단일 RCT 또는 다수의 2상 시험 | 중등도 근거; 검증 시험을 설계할 수 있음 |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

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
