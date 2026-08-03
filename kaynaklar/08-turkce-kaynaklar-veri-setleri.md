# Türkçe Kaynaklar ve Veri Setleri

> Türkçe konuşan bir saldırı yüzeyi var ve İngilizce için ölçülmüş hiçbir sonuç buraya doğrudan taşınmıyor. Bu bölüm o boşluğu belgeliyor.

Katkıya açık — eksik gördüğün kaynağı [PR ile ekle](../CONTRIBUTING.md).

---

## Neden ayrı bir bölüm?

Türkçe, güvenlik filtreleri açısından üç ayrı zorluk çıkarıyor: Unicode büyük/küçük harf katlaması (`İ`/`ı`), İngilizce ağırlıklı eğitilmiş guard modellerinin düşük kapsamı, ve KVKK'ya özgü kişisel veri biçimleri (TCKN, VKN, IBAN, plaka). Aşağıdaki ölçümler bu üç eksenin de gerçek ve ölçülebilir olduğunu gösteriyor.

## Ölçülmüş bulgular

- [turkish-casefold-evasion](https://github.com/fevziegeyurtsevenler/turkish-casefold-evasion) — Türkçe harf katlamasının naif kelime filtrelerini %94.6 oranında atlattığı ölçümü; veri seti ve NFKC düzeltmesiyle. 🔧 AltaySec *(tür: araştırma, dil: EN)*
- [turkish-over-refusal-set](https://github.com/fevziegeyurtsevenler/turkish-over-refusal-set) — 120 zararsız-ama-ürkütücü çift üzerinden aşırı-red ölçümü: ProtectAI guard'ı Türkçede %59, İngilizcede %0.8 reddediyor (71 kat fark). 🔧 AltaySec *(tür: araştırma, dil: TR)*
- [guard-blindspots-tr](https://github.com/fevziegeyurtsevenler/guard-blindspots-tr) — 248 etiketli Türkçe injection yükü ve obfuskasyon stres testi; popüler bir açık guard Türkçe saldırıların %85'ini kaçırıyor, başkaları sağlam kalıyor. 🔧 AltaySec *(tür: araştırma, dil: EN)*
- [guardrail-arena](https://github.com/fevziegeyurtsevenler/guardrail-arena) — EN+TR iki eksenli guardrail ölçütü; `jailbreak-classifier` bu sette Türkçe saldırıların %83'ünü kaçırdı. 🔧 AltaySec *(tür: ölçüt, dil: EN)*

## Veri setleri (Hugging Face)

- [Hugging Face — AltaySec veri setleri](https://huggingface.co/fevziegeyurtsevenler) — Türkçe injection, aşırı-red, casefold kaçışı ve ajan eklenti denetimi veri setlerinin toplandığı profil. 🔧 AltaySec *(tür: dataset, dil: TR)*
- [turkish-prompt-injection](https://huggingface.co/datasets/fevziegeyurtsevenler/turkish-prompt-injection) — 107 Türkçe injection/jailbreak kalıbı, OWASP ve MITRE ATLAS eşlemeli, her biri savunmasıyla birlikte. 🔧 AltaySec *(tür: dataset, dil: TR)*
- [multilingual-jailbreak](https://huggingface.co/datasets/fevziegeyurtsevenler/multilingual-jailbreak) — Aynı jailbreak niyetinin farklı dillerdeki karşılıklarını içeren set; guard'ların dil bazlı kör noktalarını ölçmek için. 🔧 AltaySec *(tür: dataset, dil: TR)*
- [turkish-pii-corpus](https://huggingface.co/datasets/fevziegeyurtsevenler/turkish-pii-corpus) — Türkçe kişisel veri örüntülerinin (TCKN, IBAN, VKN, plaka) etiketli derlemi; maskeleme aracı geliştirirken taban set olarak kullanılır. 🔧 AltaySec *(tür: dataset, dil: TR)*
- [ai-security-glossary](https://huggingface.co/datasets/fevziegeyurtsevenler/ai-security-glossary) — Yapay zeka güvenliği terimlerinin Türkçe karşılıklarını sabitleyen sözlük; çeviri tutarlılığı için başvuru kaynağı. 🔧 AltaySec *(tür: dataset, dil: TR)*
- [turkish-pii-redactor](https://github.com/fevziegeyurtsevenler/turkish-pii-redactor) — TCKN/IBAN/VKN/plaka için checksum doğrulamalı tespit ve maskeleme; kutudan çıkan Presidio'nun bu alanları %0 yakaladığı ölçümüyle. 🔧 AltaySec *(tür: araç, dil: TR)*

## Türkçe rehber serisi

- [LLM Security Türkiye](https://github.com/fevziegeyurtsevenler/LLM-Security-Turkiye) — Türkçe yapay zeka güvenliği ekosisteminin giriş noktası: rehber serisi, akademi, araştırmalar, araçlar ve veri setleri. 🔧 AltaySec *(tür: hub, dil: TR)*
- [LLM Security Nedir?](https://github.com/fevziegeyurtsevenler/LLM-Security-Nedir) — Alanın Türkçe tanımı ve klasik siber güvenlikten farkları; seriye buradan başlanır. 🔧 AltaySec *(tür: rehber, dil: TR)*
- [LLM Security Roadmap](https://github.com/fevziegeyurtsevenler/LLM-Security-Roadmap) — Sıfırdan uzmanlığa 7 aşamalı Türkçe öğrenme yol haritası; bu liste "ne var" sorusunu, roadmap "hangi sırayla" sorusunu cevaplar. 🔧 AltaySec *(tür: rehber, dil: TR)*
- [OWASP LLM Top 10 Türkçe](https://github.com/fevziegeyurtsevenler/OWASP-LLM-TOP-10-TURKCE) — Standardın Türkçe kapsamlı işlenişi, saldırı senaryoları ve savunmalarla. 🔧 AltaySec *(tür: rehber, dil: TR)*

## Türkiye'den genel siber güvenlik kaynakları

- [Siber Güvenlik SSS](https://github.com/LuNiZz/siber-guvenlik-sss) — Türkiye'nin en çok başvurulan Türkçe siber güvenlik soru-cevap arşivi; kariyer ve temel konularda referans, yapay zeka güvenliğini ayrı bir disiplin olarak kapsamıyor. *(tür: rehber, dil: TR)*
- [USOM — Ulusal Siber Olaylara Müdahale Merkezi](https://www.usom.gov.tr/) — Resmî zafiyet duyuruları ve zararlı bağlantı listeleri; Türkiye'ye özgü tehdit istihbaratının birincil kamu kaynağı. *(tür: kurum, dil: TR)*
- [KVKK — Kişisel Verileri Koruma Kurumu](https://www.kvkk.gov.tr/) — Kişisel veri işlemenin yasal çerçevesi; LLM uygulamalarında veri minimizasyonu ve maskeleme kararlarının dayanağı. *(tür: kurum, dil: TR)*
- [Türkçe Yapay Zeka Kaynakları](https://github.com/deeplearningturkiye/turkce-yapay-zeka-kaynaklari) — Türkçe yapay zeka kaynaklarının en bilinen derlemesi; güvenlik kapsamı yok ve 2021'den beri güncellenmiyor. ⚠️ bakımsız *(tür: liste, dil: TR)*
