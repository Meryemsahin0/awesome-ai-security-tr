# Guardrail ve Savunma

> Modelin girdisini ve çıktısını denetleyen koruma katmanları — ve bu katmanların gerçekte ne kadar işe yaradığı.

Katkıya açık — eksik gördüğün kaynağı [PR ile ekle](../CONTRIBUTING.md).

---

## Çerçeveler

- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) — Konuşma akışını Colang adlı bir dille programlayarak sınır koyan araç seti; diyalog düzeyinde kural yazmak isteyenler için en olgun seçenek. *(tür: araç, dil: EN)*
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) — Çıktıyı şemaya ve doğrulayıcı zincirine tabi tutan çerçeve; hazır doğrulayıcı kütüphanesi (hub) sayesinde sıfırdan yazmadan kural eklenebilir. *(tür: araç, dil: EN)*
- [LLM Guard](https://github.com/protectai/llm-guard) — Girdi/çıktı için hazır tarayıcı seti: injection, PII, toksisite, gizli veri sızıntısı ve zararlı URL kontrolleri bir arada. *(tür: araç, dil: EN)*
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) — Meta'nın güvenlik araç seti; Llama Guard sınıflandırıcıları ve CyberSecEval değerlendirme paketi buradan çıkıyor. *(tür: araç, dil: EN)*
- [Prompt Guard](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M) — Doğrudan ve dolaylı injection'ı yakalamak için eğitilmiş küçük sınıflandırıcı; düşük gecikmeli ön filtre olarak konumlanır. *(tür: model, dil: EN)*

## PII ve veri koruma

- [Presidio](https://github.com/microsoft/presidio) — Metin, görsel ve yapılandırılmış veride kişisel veri tespiti ve maskeleme; NLP ve örüntü eşleştirmeyi birleştirir, kendi tanıyıcınızı eklemeye açıktır. *(tür: araç, dil: EN)*
- [turkish-pii-redactor](https://github.com/fevziegeyurtsevenler/turkish-pii-redactor) — TCKN, IBAN, VKN, plaka gibi Türkiye'ye özgü kimlik verilerini checksum doğrulamasıyla yakalayan maskeleyici; Presidio'nun kutudan çıktığı hâliyle bu alanları %0 oranında yakaladığı ölçümüyle birlikte. 🔧 AltaySec *(tür: araç, dil: TR)*
- [KVKK + AI uyum kiti](https://github.com/fevziegeyurtsevenler/kvkk-ai-compliance-kit) — LLM uygulamaları için KVKK kontrol listesi: veri minimizasyonu, maskeleme ve AB AI Act kesişimi. Hukuki tavsiye değildir. 🔧 AltaySec *(tür: rehber, dil: TR)*

## Guardrail'ler gerçekte ne kadar çalışıyor?

- [guardrail-arena](https://github.com/fevziegeyurtsevenler/guardrail-arena) — İki eksenli, çok dilli (EN+TR) guardrail ölçütü: hem saldırı kaçırma oranını hem de zararsız metni aşırı reddetme oranını ölçer. Bulgu: test edilen guard'lar güvenlikle ilgili zararsız metnin %40–70'ini reddediyor. 🔧 AltaySec *(tür: ölçüt, dil: EN)*
- [turkish-over-refusal-set](https://github.com/fevziegeyurtsevenler/turkish-over-refusal-set) — XSTest tarzı aşırı-red testi: ProtectAI guard'ı zararsız Türkçe isteklerin %59'unu reddederken aynı setin İngilizcesinde bu oran %0.8. Guardrail seçerken tek eksenli bakmanın maliyetini gösterir. 🔧 AltaySec *(tür: ölçüt, dil: TR)*
- [XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours](https://arxiv.org/abs/2308.01263) — Aşırı-red (over-refusal) problemini ölçülebilir hâle getiren çalışma; güvenlik ile kullanılabilirlik arasındaki dengeyi sayıya döker. *(tür: makale, dil: EN)*

## Mimari savunma

- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) — Modelin kendi çıktısını yazılı ilkelere göre eleştirip düzelttiği hizalama yöntemi; guardrail'in model içine gömülmüş hâli. *(tür: makale, dil: EN)*
- [StruQ: Defending Against Prompt Injection with Structured Queries](https://arxiv.org/abs/2402.06363) — Talimat ile veriyi yapısal olarak ayırmayı öneren savunma; filtre yerine mimari çözüm arayanlar için. *(tür: makale, dil: EN)*
- [CaMeL: Defeating Prompt Injections by Design](https://arxiv.org/abs/2503.18813) — Yetenek tabanlı (capability) bir kontrol katmanıyla ajanın injection sonrası ne yapabileceğini sınırlayan tasarım; "modeli düzelt" yerine "yetkiyi kıs" yaklaşımı. *(tür: makale, dil: EN)*
