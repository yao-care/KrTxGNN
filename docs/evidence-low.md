---
layout: default
title: 모델 예측만 (L5)
nav_order: 23
permalink: /evidence-low/
description: "KrTxGNN의 L5 후보: 모델 예측만 존재하며 아직 임상 또는 문헌 근거가 없습니다."
---

# 모델 예측만 (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
모델 예측만 있고 아직 사람 대상 근거가 없는 후보
</p>

---

## 기준

| 등급 | 정의 | 임상적 의미 |
|-------|------------|------------------|
| **L5** | 모델 예측만 존재 | 가설 단계; 사람 대상 근거 없음 |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

### L5 ({{ l5_drugs.size }}건)

| 의약품 | 적응증 수 | 링크 |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [보고서 보기]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>면책 조항</strong><br>
본 보고서는 학술 연구 참고용으로만 제공되며 <strong>의료 조언을 구성하지 않습니다</strong>. 반드시 담당 의사의 지시를 따르시고, 임의로 약물을 조정하지 마십시오. 모든 약물재창출 결정은 완전한 임상 검증과 규제 당국의 심사를 거쳐야 합니다.
<br><br>
<small>검토: 藥提醒科技有限公司 (yao.care)</small>
</div>
