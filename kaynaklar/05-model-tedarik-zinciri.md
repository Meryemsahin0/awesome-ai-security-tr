# Model ve Tedarik Zinciri Güvenliği

> İndirdiğiniz model dosyası, kullandığınız veri seti ve kurduğunuz bağımlılık — üçü de saldırı yüzeyi.

**Bölüm sahibi:** _(atanacak)_ · [Katkı kuralları](../CONTRIBUTING.md)

---

## Model dosyası riskleri

- [Hugging Face Hub güvenlik dokümanı](https://huggingface.co/docs/hub/security) — Model deposu güvenliğinin resmî referansı: pickle taraması, gizli anahtar tespiti, imzalama ve kötü amaçlı dosya politikaları. *(tür: doküman, dil: EN)*
- [safetensors](https://github.com/huggingface/safetensors) — Model ağırlıklarını kod çalıştırmadan yükleyen dosya biçimi; pickle deserialization sınıfını kökten kapattığı için varsayılan tercih olmalı. *(tür: araç, dil: EN)*
- [picklescan](https://github.com/mmaitre314/picklescan) — Pickle dosyalarını yüklemeden önce zararlı çağrı kalıpları için tarayan araç; model indirme borusuna kapı olarak konur. *(tür: araç, dil: EN)*
- [modelscan](https://github.com/protectai/modelscan) — Birden çok serileştirme biçimini (pickle, H5, SavedModel) yüklemeden tarayan güvenlik aracı. *(tür: araç, dil: EN)*
- [Pickle serileştirme dokümanı — güvenlik uyarısı](https://docs.python.org/3/library/pickle.html) — Riskin birincil kaynağı: Python'un kendi dokümantasyonu pickle'ın güvenilmeyen veriyle asla kullanılmaması gerektiğini açıkça yazar. *(tür: doküman, dil: EN)*

## Veri zehirlenmesi

- [Poisoning Web-Scale Training Datasets is Practical](https://arxiv.org/abs/2302.10149) — Devasa veri setlerini gerçekten ve ucuza zehirlemenin mümkün olduğunu gösteren çalışma; tedarik zinciri tehdidini teoriden pratiğe taşır. *(tür: makale, dil: EN)*
- [Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://arxiv.org/abs/2401.05566) — Arka kapının güvenlik eğitiminden sağ çıkabildiğini gösteren çalışma; "sonradan hizalarız" varsayımını çürütür. *(tür: makale, dil: EN)*
- [hf-dataset-scan](https://github.com/fevziegeyurtsevenler/hf-dataset-scan) — Veri setlerine gizlenmiş prompt injection'ı (görünmez Unicode, injection kalıpları, sızdırma URL'leri) tarayan sıfır bağımlılıklı araç; CI kapısı olarak kurulabilir, 17 bin satırlık açık bir çalışmayla birlikte gelir. 🔧 AltaySec *(tür: araç, dil: EN)*

## Tedarik zinciri bütünlüğü

- [SLSA](https://slsa.dev/) — Yazılım artefaktlarının üretim zincirini doğrulanabilir kılan çerçeve; model üretim hattına da uygulanabilir olgunluk seviyeleri tanımlar. *(tür: standart, dil: EN)*
- [CycloneDX ML-BOM](https://cyclonedx.org/capabilities/mlbom/) — Model, veri seti ve bağımlılıkları makine-okunur bir malzeme listesine döken standart; AI için SBOM karşılığı. *(tür: standart, dil: EN)*
- [Sigstore](https://www.sigstore.dev/) — Artefakt imzalama ve şeffaflık günlüğü altyapısı; yayımladığınız modelin sizden geldiğini kanıtlamanın pratik yolu. *(tür: araç, dil: EN)*
- [OWASP LLM03: Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) — Riskin standart tanımı: üçüncü parti model, adaptör ve veri kaynaklarının getirdiği tehditler. *(tür: standart, dil: EN)*

## Denetim çalışmaları

- [skills-in-the-wild](https://github.com/fevziegeyurtsevenler/skills-in-the-wild) — 3.168 gerçek AI ajan eklentisinin (skill, MCP yapılandırması, kural dosyası) açık ve tekrar üretilebilir güvenlik denetimi; yöntem ve veri seti dahil. 🔧 AltaySec *(tür: araştırma, dil: EN)*
