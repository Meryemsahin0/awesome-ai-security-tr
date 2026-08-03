# Değerlendirme, Ölçüt ve Standartlar

> "Bu sistem güvenli mi?" sorusunu ölçülebilir hâle getiren çerçeveler, ölçütler ve resmî standartlar.

**Bölüm sahibi:** _(atanacak)_ · [Katkı kuralları](../CONTRIBUTING.md)

---

## Standartlar ve çerçeveler

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — LLM uygulamalarındaki en kritik on risk; alanın ortak sözlüğü hâline geldiği için rapor ve teklif yazarken çıpa olarak kullanılır. *(tür: standart, dil: EN)*
- [OWASP LLM Top 10 — Türkçe kapsamlı rehber](https://github.com/fevziegeyurtsevenler/OWASP-LLM-TOP-10-TURKCE) — Aynı listenin Türkçe işlenmiş hâli: her risk için saldırı senaryosu ve savunma stratejisiyle. 🔧 AltaySec *(tür: rehber, dil: TR)*
- [MITRE ATLAS](https://atlas.mitre.org/) — Yapay zeka sistemlerine yönelik gerçek dünya saldırı taktik ve tekniklerinin ATT&CK tarzı matrisi; tehdit modellemesini somut tekniklere bağlar. *(tür: standart, dil: EN)*
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — Risk yönetimini yönetişim/haritalama/ölçme/yönetme döngüsüne oturtan çerçeve; kurumsal uyum tarafının referansı. *(tür: standart, dil: EN)*
- [OWASP AI Security Verification Standard (AISVS)](https://github.com/OWASP/AISVS) — AI sistemleri için maddeleştirilmiş doğrulama gereksinimleri; ASVS'in yapay zeka karşılığı, denetim listesi olarak kullanılabilir. *(tür: standart, dil: EN)*
- [OWASP Agentic AI — tehditler ve azaltımlar](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — Otonom ajanlara özgü tehdit taksonomisi; klasik LLM Top 10'un kapsamadığı çok adımlı saldırıları ele alır. *(tür: standart, dil: EN)*
- [EU AI Act teknik uyum kontrol listesi](https://github.com/fevziegeyurtsevenler/eu-ai-act-technical-checklist) — Mevzuatı mühendislik görevlerine çeviren kontrol listesi: red-teaming, loglama, adversarial test yükümlülükleri (EN+TR). 🔧 AltaySec *(tür: rehber, dil: TR)*

## Değerlendirme çerçeveleri

- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) — UK AI Security Institute'un değerlendirme çerçevesi; ajan davranışı ve güvenlik değerlendirmelerini tekrarlanabilir biçimde koşmak için tasarlandı. *(tür: araç, dil: EN)*
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) — Dil modeli değerlendirmesinin fiili standardı; güvenlik ölçütlerini de aynı altyapıya bağlamak için taban olarak kullanılır. *(tür: araç, dil: EN)*
- [HELM](https://crfm.stanford.edu/helm/) — Modelleri tek skorla değil çok boyutlu (doğruluk, sağlamlık, önyargı, toksisite) değerlendiren bütünsel çerçeve. *(tür: ölçüt, dil: EN)*
- [CyberSecEval](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks) — Modellerin güvensiz kod üretme eğilimini ve siber saldırıya yardım etme davranışını ölçen kıyaslama paketi. *(tür: ölçüt, dil: EN)*
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) — Ajanların prompt injection altında görevini sürdürüp sürdüremediğini ölçen dinamik ortam; savunma ile fayda arasındaki dengeyi aynı anda raporlar. *(tür: ölçüt, dil: EN)*

## Ölçüm metodolojisi

- [guardrail-arena](https://github.com/fevziegeyurtsevenler/guardrail-arena) — Guardrail'i tek eksenli ("kaç saldırı yakaladı") değil iki eksenli değerlendiren yaklaşım; herhangi bir guard'ı çağrılabilir bir fonksiyon olarak takar. 🔧 AltaySec *(tür: ölçüt, dil: EN)*
- [Evaluating the Robustness of LLM Guardrails](https://arxiv.org/abs/2504.11168) — Guardrail'lerin sistematik zayıflıklarını inceleyen çalışma; kendi değerlendirme setinizi kurarken hangi tuzaklara düşmemeniz gerektiğini gösterir. *(tür: makale, dil: EN)*
