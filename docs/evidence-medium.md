---
layout: default
title: 중등도 근거 (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "이 사이트(대한민국)의 근거 수준 L3–L4 의약품 63개(예: Abatacept, Beclomethasone Dipropionate, Brentuximab Vedotin). 의약품별 주요 예측 적응증, 의약품 허가 품목 수, 검토 기록을 보여 줍니다."
---

# 중등도 근거 (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
이 페이지에는 이 사이트에서 보고서를 공개한 의약품 **{{ site.data.drug_stats.total_drugs }}**개 중 **{{ site.data.evidence_tier_facts.medium.count }}**개({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}%)가 실려 있습니다: L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
30개 TxGNN 사이트의 L3–L4 비율 중앙값: {{ site.data.evidence_tier_facts.medium.cross.median_share }}%. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}이 사이트는 중앙값보다 높습니다.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}이 사이트는 중앙값보다 낮습니다.{% else %}이 사이트는 중앙값과 같습니다.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
국내 데이터(의약품 허가 품목)에서 이 중 **{{ site.data.evidence_tier_facts.medium.with_current }}**개는 정상 품목이 1건 이상 있고, **{{ site.data.evidence_tier_facts.medium.none_current }}**개는 품목은 있으나 정상 품목이 없으며, **{{ site.data.evidence_tier_facts.medium.without_data }}**개는 국내 데이터에 없습니다. **{{ site.data.evidence_tier_facts.medium.with_reviews }}**개는 검토 기록에 항목이 있습니다(의약품 페이지의 허가 정보 정정). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}**개는 같은 의약품에 대해 다른 TxGNN 사이트에 없는 예측 적응증이 있습니다.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

품목은 있으나 정상 품목이 없는 의약품: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

모든 수준의 정의: [방법론]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }}건)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| 의약품 | 수준 | 주요 예측 신규 적응증 | 의약품 허가 품목: 정상 / 전체 | 검토 기록 | 이 사이트에만 |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}예 ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }}건)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| 의약품 | 수준 | 주요 예측 신규 적응증 | 의약품 허가 품목: 정상 / 전체 | 검토 기록 | 이 사이트에만 |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}예 ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
