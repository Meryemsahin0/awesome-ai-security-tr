# RAG ve Uygulama Güvenliği

> Modeli bir uygulamaya bağladığınız anda klasik uygulama güvenliği geri geliyor — üstüne vektör veritabanı, belge alma ve aşırı yetki katmanlarıyla.

**Bölüm sahibi:** _(atanacak)_ · [Katkı kuralları](../CONTRIBUTING.md)

---

## RAG'a özgü riskler

- [RAG Security Nedir?](https://github.com/fevziegeyurtsevenler/RAG-Security-Nedir) — Belge alma mimarilerindeki güvenlik sorunlarının Türkçe girişi: bilgi tabanı zehirlenmesi, yetki sızıntısı ve alıntı manipülasyonu. 🔧 AltaySec *(tür: rehber, dil: TR)*
- [OWASP LLM08: Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) — Vektör veritabanı ve gömme katmanına özgü risklerin standart tanımı; çok kiracılı RAG kurulumlarındaki yetki karışmasını da kapsar. *(tür: standart, dil: EN)*
- [PoisonedRAG: Knowledge Corruption Attacks to RAG](https://arxiv.org/abs/2402.07867) — Bilgi tabanına birkaç zehirli belge eklemenin cevabı hedeflenen şekilde değiştirmeye yettiğini gösteren çalışma. *(tür: makale, dil: EN)*
- [Follow My Instruction and Spill the Beans](https://arxiv.org/abs/2402.17840) — Alınan bağlamın içine gömülü talimatların modeli ele geçirdiğini ve bağlam sızıntısına yol açtığını inceleyen çalışma. *(tür: makale, dil: EN)*

## Uygulama katmanı

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — Uygulama düzeyindeki risklerin (aşırı yetki, güvensiz çıktı işleme, sınırsız tüketim) ortak referansı. *(tür: standart, dil: EN)*
- [OWASP API Security Top 10](https://owasp.org/API-Security/) — LLM'i bir API'nin arkasına koyduğunuz anda geçerli olan klasik liste; yetkilendirme hatalarının çoğu hâlâ buradan geliyor. *(tür: standart, dil: EN)*
- [PortSwigger — Web LLM attacks](https://portswigger.net/web-security/llm-attacks) — LLM'e verilen aşırı yetkinin klasik web zafiyetlerine (SSRF, komut çalıştırma) nasıl döndüğünü laboratuvarla gösteren modül. *(tür: lab, dil: EN)*
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) — Çıktı kodlama, yetkilendirme ve girdi doğrulama gibi temel konularda uygulanabilir kısa rehberler; LLM çıktısını HTML'e basmadan önce bakılacak yer. *(tür: rehber, dil: EN)*

## Gizlilik ve veri sızıntısı

- [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805) — Modelin eğitim verisini ezberleyip geri verebildiğini gösteren temel çalışma; veri gizliliği tartışmasının başlangıç noktası. *(tür: makale, dil: EN)*
- [Scalable Extraction of Training Data from (Production) Language Models](https://arxiv.org/abs/2311.17035) — Üretimdeki kapalı modellerden bile eğitim verisi çıkarılabildiğini gösteren devam çalışması. *(tür: makale, dil: EN)*
- [Presidio](https://github.com/microsoft/presidio) — Uygulama sınırında kişisel veriyi tespit edip maskeleyen çerçeve; loglara ve model isteklerine PII kaçmasını engellemek için. *(tür: araç, dil: EN)*
