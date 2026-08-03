# Prompt Injection

> Bir dil modeline verilen talimatla, ona ulaşan veriyi ayırt edememesinden doğan zafiyet sınıfı. LLM güvenliğinin en temel ve en çözümsüz problemi.

**Bölüm sahibi:** _(atanacak)_ · [Katkı kuralları](../CONTRIBUTING.md)

---

## Temel okumalar

- [Prompt injection: what's the worst that can happen?](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) — Alanın adını koyan kişinin risk çerçevesi; "sadece chatbot kötü söz söyler" sanısını kıran, saldırının neden veri sızdırma ve eylem ele geçirme olduğunu anlatan giriş metni. *(tür: makale, dil: EN)*
- [Simon Willison — prompt injection etiketi](https://simonwillison.net/tags/prompt-injection/) — Konunun 2022'den beri kesintisiz takip edildiği tek arşiv; yeni bir saldırı çıktığında ilk buraya bakılır. *(tür: arşiv, dil: EN)*
- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — Özel veri + güvenilmeyen girdi + dışarı iletişim üçlüsü bir arada olduğunda sömürünün kaçınılmaz olduğunu gösteren zihinsel model; ajan mimarisi tasarlarken kontrol listesi olarak kullanılır. *(tür: makale, dil: EN)*
- [OWASP LLM01: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) — Riskin standart tanımı, örnek senaryolar ve önerilen azaltımlar; kurumsal raporlarda atıf verilebilecek referans. *(tür: standart, dil: EN)*
- [Prompt Injection Nedir?](https://github.com/fevziegeyurtsevenler/Prompt-Injection-Nedir) — Konunun Türkçe kapsamlı girişi: doğrudan/dolaylı ayrımı, saldırı örnekleri ve savunma yaklaşımları. 🔧 AltaySec *(tür: rehber, dil: TR)*

## Akademik kaynaklar

- [Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173) — Dolaylı prompt injection kavramını literatüre sokan çalışma; saldırganın modele hiç dokunmadan, modelin okuduğu içerik üzerinden kontrol ele geçirmesini gösterir. *(tür: makale, dil: EN)*
- [Ignore Previous Prompt: Attack Techniques For Language Models](https://arxiv.org/abs/2211.09527) — Talimat kaçırma ve hedef saptırma tekniklerinin ilk sistematik incelemesi; "ignore previous instructions" kalıbının kökeni. *(tür: makale, dil: EN)*
- [Tensor Trust: Interpretable Prompt Injection Attacks from an Online Game](https://arxiv.org/abs/2311.01011) — Binlerce gerçek insanın ürettiği saldırı/savunma verisinden çıkarılan taksonomi; oyunlaştırılmış veri toplamanın red-team değeri için de iyi bir emsal. *(tür: makale, dil: EN)*
- [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) — Otomatik üretilen sonek (suffix) saldırılarının modeller arası taşınabildiğini gösteren GCG çalışması; "kapalı model güvenlidir" varsayımını kırar. *(tür: makale, dil: EN)*
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) — Savunma tarafına geçen ender çalışmalardan biri; ajan mimarisinde injection'ı yapısal olarak sınırlayan altı tasarım kalıbı önerir. *(tür: makale, dil: EN)*

## Araçlar

- [promptmap](https://github.com/utkusen/promptmap) — Kendi sistem prompt'unuza karşı otomatik injection testi koşan tarayıcı; Türkiye'den Utku Şen tarafından geliştirildi, kural setini kendi uygulamanıza göre genişletebilirsiniz. *(tür: araç, dil: EN)*
- [Rebuff](https://github.com/protectai/rebuff) — Çok katmanlı injection tespiti: sezgisel filtre, LLM tabanlı sınıflandırma, vektör benzerliği ve canary token sızıntı kontrolü bir arada. *(tür: araç, dil: EN)*
- [Vigil](https://github.com/deadbits/vigil-llm) — Prompt ve yanıtları YARA kuralları, vektör veritabanı ve transformer sınıflandırıcıyla tarayan savunma katmanı. *(tür: araç, dil: EN)*
- [uncloak](https://github.com/fevziegeyurtsevenler/uncloak) — Görünmez Unicode ile gizlenmiş talimat kaçakçılığını ve tool poisoning'i yakalayan tarayıcı; sıfır bağımlılık, SARIF çıktısı ve tarayıcıda çalışan demosu var. 🔧 AltaySec *(tür: araç, dil: EN)*

## Türkçeye özgü bulgular

- [turkish-casefold-evasion](https://github.com/fevziegeyurtsevenler/turkish-casefold-evasion) — `"İGNORE".lower() != "ignore"` — Türkçe noktalı İ'nin Unicode katlaması, naif kelime filtrelerini ölçülen %94.6 oranında atlatıyor; veri seti ve tek satırlık NFKC düzeltmesiyle birlikte. 🔧 AltaySec *(tür: araştırma, dil: EN)*
- [guard-blindspots-tr](https://github.com/fevziegeyurtsevenler/guard-blindspots-tr) — 248 etiketli Türkçe injection yükü popüler açık guard modellerinden geçirildi; İngilizcede iyi olan bir guard'ın Türkçede otomatik olarak iyi olmadığını ölçüyor. 🔧 AltaySec *(tür: araştırma, dil: EN)*

## Pratik

- [PortSwigger — Web LLM attacks](https://portswigger.net/web-security/llm-attacks) — Ücretsiz, çözülebilir laboratuvarlarla LLM entegrasyonlarındaki injection ve aşırı yetki zafiyetlerini öğreten modül; web güvenliği geçmişi olan için en hızlı giriş. *(tür: lab, dil: EN)*
- [Gandalf](https://gandalf.lakera.ai/) — Seviye seviye zorlaşan sistem prompt sızdırma oyunu; alana ilk temas için standart başlangıç noktası. *(tür: lab, dil: EN)*
