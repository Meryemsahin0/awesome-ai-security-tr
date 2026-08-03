# Jailbreak ve Red Teaming

> Modelin hizalama (alignment) sınırlarını aşmaya yönelik saldırılar ve bunları sistematik olarak arayan saldırgan-taraf metodolojisi.

Katkıya açık — eksik gördüğün kaynağı [PR ile ekle](../CONTRIBUTING.md).

---

## Metodoloji

- [Microsoft AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team/) — Üretim ölçeğinde AI red-teaming yapan bir ekibin yayınladığı planlama rehberi; kapsam belirleme ve zarar kategorileri bölümleri kurumsal işte doğrudan kullanılabilir. *(tür: rehber, dil: EN)*
- [Lessons from red teaming 100 generative AI products](https://arxiv.org/abs/2501.07238) — Microsoft'un 100 ürünlük saha deneyiminden çıkan sekiz ders; "en etkili saldırılar en karmaşık olanlar değil" bulgusu metodolojiyi sadeleştirir. *(tür: makale, dil: EN)*
- [Red Teaming Language Models to Reduce Harms](https://arxiv.org/abs/2209.07858) — Ölçekli insan red-teaming'in ilk büyük ampirik çalışması; model büyüdükçe saldırı yüzeyinin nasıl değiştiğini veriyle gösterir. *(tür: makale, dil: EN)*
- [NIST AI 100-2: Adversarial Machine Learning taksonomisi](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) — Saldırı sınıflarının resmî terminolojisi; rapor yazarken ortak dil kurmak için referans alınır. *(tür: standart, dil: EN)*
- [LLM Red Team Playbook](https://github.com/fevziegeyurtsevenler/llm-red-team-playbook) — Kapsam belirleme, tehdit modeli, OWASP LLM Top 10 test matrisi ve raporlama şablonlarını içeren pratik saha kılavuzu (EN+TR). 🔧 AltaySec *(tür: rehber, dil: TR)*

## Araçlar

- [garak](https://github.com/NVIDIA/garak) — LLM'lere karşı otomatik zafiyet taraması yapan tarayıcı; probe/detector mimarisi sayesinde kendi saldırı sınıfınızı eklemek kolay, alanın fiili `nmap`'i. *(tür: araç, dil: EN)*
- [PyRIT](https://github.com/Azure/PyRIT) — Microsoft'un red-teaming otomasyon çerçevesi; çok turlu saldırı akışları ve puanlayıcı (scorer) soyutlamasıyla tekrarlanabilir kampanyalar kurmaya uygun. *(tür: araç, dil: EN)*
- [promptfoo](https://github.com/promptfoo/promptfoo) — Prompt/ajan/RAG değerlendirmesini CI'a bağlayan bildirimsel test aracı; red-team eklentileriyle regresyon testi gibi güvenlik testi koşturulabilir. *(tür: araç, dil: EN)*
- [HarmBench](https://github.com/centerforaisafety/HarmBench) — Otomatik red-teaming yöntemlerini ve savunmaları aynı zeminde karşılaştıran standart değerlendirme çerçevesi. *(tür: ölçüt, dil: EN)*
- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) — Jailbreak saldırılarının açık, sürümlenmiş ve tekrar üretilebilir kıyaslama seti; sonuçların karşılaştırılabilir olması için artefakt arşivi tutar. *(tür: ölçüt, dil: EN)*
- [llm-attacks](https://github.com/llm-attacks/llm-attacks) — GCG saldırısının referans uygulaması; otomatik adversarial sonek üretiminin nasıl çalıştığını kodda görmek için. *(tür: araç, dil: EN)*

## Veri setleri ve saldırı koleksiyonları

- ["Do Anything Now" — jailbreak_llms](https://github.com/verazuo/jailbreak_llms) — Vahşi ortamdan toplanmış 15.000'den fazla jailbreak prompt'unun ölçülüp sınıflandırıldığı veri seti; saldırı kalıplarının evrimini görmek için birincil kaynak. *(tür: dataset, dil: EN)*
- [AdvBench / HarmBench davranış setleri](https://github.com/centerforaisafety/HarmBench/tree/main/data) — Standartlaşmış zararlı davranış istekleri; kendi guard'ınızı ölçerken karşılaştırılabilir taban sağlar. *(tür: dataset, dil: EN)*
- [turkish-prompt-injection](https://huggingface.co/datasets/fevziegeyurtsevenler/turkish-prompt-injection) — 107 Türkçe prompt injection ve jailbreak kalıbı; her satır OWASP ve MITRE ATLAS kimlikleriyle eşlenmiş ve karşı savunmasıyla birlikte veriliyor. Morfolojik bypass, çeviri bahanesi ve dil değiştirme (code-switch) teknikleri dahil. 🔧 AltaySec *(tür: dataset, dil: TR)*

## Yarışma ve arena

- [HackAPrompt](https://www.hackaprompt.com/) — Dünyanın en büyük prompt injection yarışması; toplanan veri kamuya açık makaleye dönüştüğü için hem pratik hem literatür değeri var. *(tür: yarışma, dil: EN)*
- [Gray Swan Arena](https://www.grayswan.ai/) — Sınır modellere karşı ödüllü, sürekli açık jailbreak arenası; bulduğunuz kaçış gerçek bir laboratuvara raporlanır. *(tür: yarışma, dil: EN)*
- [Kalkan Arena](https://github.com/fevziegeyurtsevenler/kalkan-arena) — Türkçe "guard'ımızı kır" challenge platformu; rızaya dayalı, KVKK uyumlu maskelemeyle denemeleri eğitim verisine çeviriyor. 🔧 AltaySec *(tür: yarışma, dil: TR)*

## Eğitim

- [Red Teaming LLM Applications](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/) — DeepLearning.AI'ın ücretsiz kısa kursu; ilk uçtan uca red-team akışını birkaç saatte kurdurur. *(tür: kurs, dil: EN)*
