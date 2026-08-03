# Ajan, Araç ve MCP Güvenliği

> Model artık sadece cevap üretmiyor; araç çağırıyor, dosya okuyor, istek atıyor. Zafiyetin sonucu "kötü cevap" olmaktan çıkıp "yetkisiz eylem"e dönüşüyor.

**Bölüm sahibi:** _(atanacak)_ · [Katkı kuralları](../CONTRIBUTING.md)

---

## Temel kavramlar

- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — Özel veri erişimi + güvenilmeyen içerik + dışarı iletişim bir aradaysa sızıntının kaçınılmaz olduğunu anlatan çerçeve; ajan tasarımında ilk kontrol edilecek şey. *(tür: makale, dil: EN)*
- [AI Agent Security Nedir?](https://github.com/fevziegeyurtsevenler/AI-Agent-Security-Nedir) — Otonom ajan ve MCP güvenliğinin Türkçe girişi: yetki sınırları, araç zehirlenmesi ve izolasyon yaklaşımları. 🔧 AltaySec *(tür: rehber, dil: TR)*
- [Model Context Protocol — belirtim](https://modelcontextprotocol.io/) — Ajanların araçlara bağlandığı protokolün resmî tanımı; güvenlik tartışmasının üzerine kurulduğu zemin. *(tür: doküman, dil: EN)*
- [MCP güvenlik en iyi uygulamaları](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) — Protokolün kendi güvenlik rehberi: yetkilendirme, kullanıcı onayı ve karışık-vekil (confused deputy) riskleri. *(tür: doküman, dil: EN)*

## Saldırılar

- [MCP tool poisoning saldırıları](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) — Araç açıklamasına gizlenen talimatın modeli ele geçirdiğini gösteren bulgu; MCP ekosistemindeki ilk büyük güvenlik uyarısı. *(tür: araştırma, dil: EN)*
- [AgentDojo](https://github.com/ethz-spylab/agentdojo) — Ajanların prompt injection altında hem güvenli hem işlevsel kalıp kalamadığını ölçen dinamik değerlendirme ortamı. *(tür: ölçüt, dil: EN)*
- [Damn Vulnerable LLM Agent](https://github.com/WithSecureLabs/damn-vulnerable-llm-agent) — Kasıtlı olarak zafiyetli bir ReAct ajanı; araç zincirinin nasıl kaçırıldığını elle deneyerek öğrenmek için. *(tür: lab, dil: EN)*
- [OWASP Agentic AI — tehditler ve azaltımlar](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) — Ajan mimarilerine özgü tehdit taksonomisi ve karşı önlem kataloğu. *(tür: standart, dil: EN)*

## Araçlar

- [uncloak](https://github.com/fevziegeyurtsevenler/uncloak) — Ajan eklentilerindeki (Skills, MCP sunucuları, kural dosyaları) görünmez Unicode talimat kaçakçılığını, araç zehirlenmesini ve ölümcül üçlüyü tarar; terminal, JSON ve SARIF çıktısı verir. 🔧 AltaySec *(tür: araç, dil: EN)*
- [lethal-trifecta-lint](https://github.com/fevziegeyurtsevenler/lethal-trifecta-lint) — Bir ajanın araç manifestosunda ölümcül üçlünün oluşup oluşmadığını denetleyen sıfır bağımlılıklı linter; MCP, OpenAI ve LangChain manifestolarını okur, CI kapısı olarak çalışır. 🔧 AltaySec *(tür: araç, dil: EN)*
- [agent-security-ci](https://github.com/fevziegeyurtsevenler/agent-security-ci) — Ajan eklentilerini CI'da taramak için hazır GitHub Actions tarifleri; SARIF çıktısı ve önem derecesine göre başarısız olma desteğiyle. 🔧 AltaySec *(tür: araç, dil: EN)*
- [ToolHive](https://github.com/stacklok/toolhive) — MCP sunucularını izole ve yönetilebilir biçimde çalıştıran platform; her sunucuyu konteynerleyerek yetki sınırını işletim sistemi düzeyine taşır. *(tür: araç, dil: EN)*
- [ai-honeypot](https://github.com/fevziegeyurtsevenler/ai-honeypot) — Zafiyetli bir AI ajanı gibi görünüp injection ve ajan suistimali denemelerini yakalayan, bunları açık veri setine çeviren bal küpü. 🔧 AltaySec *(tür: araç, dil: EN)*
