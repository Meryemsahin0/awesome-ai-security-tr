<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="varlik/afis-koyu.svg">
    <source media="(prefers-color-scheme: light)" srcset="varlik/afis-acik.svg">
    <img src="varlik/afis-koyu.svg" alt="Yapay Zeka Güvenliği Kaynakları — Türkçe açıklamalı, küratörlü, CI ile doğrulanan liste" width="100%">
  </picture>
</p>

<h1 align="center">Yapay Zeka Güvenliği Kaynakları</h1>

<p align="center">
  <strong>Türkçe açıklamalı, küratörlü ve CI ile doğrulanan yapay zeka güvenliği kaynak listesi.</strong><br>
  Prompt injection, jailbreak, red teaming, guardrail, ajan/MCP güvenliği, RAG güvenliği ve tedarik zinciri.
</p>

<p align="center">
  <a href="https://github.com/fevziegeyurtsevenler/awesome-ai-security-tr/actions/workflows/dogrulama.yml"><img alt="doğrulama" src="https://github.com/fevziegeyurtsevenler/awesome-ai-security-tr/actions/workflows/dogrulama.yml/badge.svg"></a>
  <img alt="kaynak sayısı" src="https://img.shields.io/badge/kaynak-137-8b5cf6">
  <img alt="bölüm" src="https://img.shields.io/badge/b%C3%B6l%C3%BCm-9-6366f1">
  <a href="LICENSE"><img alt="lisans" src="https://img.shields.io/badge/lisans-CC%20BY%204.0-22d3ee"></a>
  <a href="https://altaysec.com.tr"><img alt="AltaySec" src="https://img.shields.io/badge/AltaySec-altaysec.com.tr-0f172a"></a>
</p>

---

Türkçe yapay zeka güvenliği için **kaynak dizini**. İngilizce awesome-list'ler var; her kaynağın yanında **neden orada olduğunu Türkçe anlatan**, ölü linkleri otomatik tarayan ve birden çok küratörün sahiplendiği bir liste yoktu.

**Buradaki her girdi bir insan tarafından açılıp okundu.** Çıplak link kabul edilmiyor, CI bunu zorunlu kılıyor.

## Nereden başlamalı?

| Durumun | Git |
|---|---|
| **Alana yeni giriyorum** | [Prompt Injection](kaynaklar/01-prompt-injection.md) → [Eğitim ve Lab](kaynaklar/09-egitim-lab-ctf.md) → [Gandalf](https://gandalf.lakera.ai/) ile ilk kırma denemeni yap |
| **Uygulamamı güvene almam lazım** | [Değerlendirme ve Standartlar](kaynaklar/04-degerlendirme-standartlar.md) → [Guardrail ve Savunma](kaynaklar/03-guardrail-savunma.md) → [RAG ve Uygulama Güvenliği](kaynaklar/07-rag-uygulama-guvenligi.md) |
| **Ajan/MCP sistemi kuruyorum** | [Ajan, Araç ve MCP Güvenliği](kaynaklar/06-agent-mcp-guvenligi.md) → ölümcül üçlü kontrolü |
| **Türkçe özelinde ne değişiyor?** | [Türkçe Kaynaklar ve Veri Setleri](kaynaklar/08-turkce-kaynaklar-veri-setleri.md) — ölçülmüş bulgular aşağıda |
| **Sıralı bir öğrenme planı istiyorum** | Bu liste "ne var" der; sıra için [LLM Security Roadmap](https://github.com/fevziegeyurtsevenler/LLM-Security-Roadmap) |

## Bölümler

| # | Bölüm | Kapsam | Kaynak |
|---|---|---|---|
| 01 | [Prompt Injection](kaynaklar/01-prompt-injection.md) | Doğrudan/dolaylı injection, ölümcül üçlü, tespit araçları | 18 |
| 02 | [Jailbreak ve Red Teaming](kaynaklar/02-jailbreak-red-teaming.md) | Saldırgan-taraf metodoloji, otomasyon çerçeveleri, arenalar | 18 |
| 03 | [Guardrail ve Savunma](kaynaklar/03-guardrail-savunma.md) | Koruma katmanları, PII maskeleme, aşırı-red problemi | 14 |
| 04 | [Değerlendirme ve Standartlar](kaynaklar/04-degerlendirme-standartlar.md) | OWASP, ATLAS, NIST, ölçüt çerçeveleri | 14 |
| 05 | [Model ve Tedarik Zinciri](kaynaklar/05-model-tedarik-zinciri.md) | Model dosyası riskleri, veri zehirlenmesi, imzalama | 13 |
| 06 | [Ajan, Araç ve MCP Güvenliği](kaynaklar/06-agent-mcp-guvenligi.md) | Tool poisoning, yetki sınırlama, ajan denetimi | 13 |
| 07 | [RAG ve Uygulama Güvenliği](kaynaklar/07-rag-uygulama-guvenligi.md) | Bilgi tabanı zehirlenmesi, veri sızıntısı, API katmanı | 11 |
| 08 | [Türkçe Kaynaklar ve Veri Setleri](kaynaklar/08-turkce-kaynaklar-veri-setleri.md) | Türkçeye özgü ölçümler, veri setleri, yerel kurumlar | 18 |
| 09 | [Eğitim, Lab ve CTF](kaynaklar/09-egitim-lab-ctf.md) | Oynanabilir laboratuvarlar, yarışmalar, bug bounty | 18 |

## Neden Türkçe için ayrı bir liste?

Bir guardrail'in İngilizcede iyi olması Türkçede iyi olduğu anlamına gelmiyor. Bunlar tahmin değil, açık veri setleriyle birlikte yayımlanmış ölçümler:

| Bulgu | Ölçüm | Kaynak |
|---|---|---|
| Türkçe harf katlaması (`"İGNORE".lower() != "ignore"`) naif filtreleri atlatıyor | **%94.6** bypass | [turkish-casefold-evasion](https://github.com/fevziegeyurtsevenler/turkish-casefold-evasion) |
| Bir guard modeli zararsız Türkçe istekleri reddediyor (aynı setin İngilizcesinde %0.8) | **%59** aşırı-red | [turkish-over-refusal-set](https://github.com/fevziegeyurtsevenler/turkish-over-refusal-set) |
| Popüler bir jailbreak sınıflandırıcısı Türkçe saldırıları kaçırıyor | **%83** kaçırma | [guardrail-arena](https://github.com/fevziegeyurtsevenler/guardrail-arena) |

Bu yüzden 08. bölüm ayrı duruyor: İngilizce için ölçülmüş hiçbir sonuç buraya doğrudan taşınmıyor.

## Nasıl okunur

```
- [Kaynak Adı](url) — Ne olduğu ve neden değerli olduğu. *(tür: makale|araç|lab|dataset, dil: TR|EN)*
```

| İşaret | Anlamı |
|---|---|
| 🔧 AltaySec | Bu listeyi yürüten ekibin kendi ürettiği kaynak — gizlenmez, işaretlenir |
| ⚠️ bakımsız | 12+ aydır güncellenmemiş; tarihsel değeri var, üretimde kullanma |

## Katkı

Bu liste tek kişilik değil. Her bölümün ayrı bir sahibi var ve katkı PR ile geliyor.

**[CONTRIBUTING.md](CONTRIBUTING.md)'yi oku.** Özet:

- Her linkin yanında **1-2 cümle Türkçe açıklama** olacak — çıplak link CI'da reddedilir
- Eklediğin kaynağı **açıp okumuş olacaksın** (listeyi bir dil modeline doldurtmak yasak)
- Hangi bölüme istersen katkı ver; küçük ve odaklı PR'lar daha hızlı incelenir
- Bölüm başına 15-40 kaynak; şişme awesome-list'leri öldürür

### Bölüm sahipleri

| Bölüm | Sahibi |
|---|---|
| 01 · Prompt Injection | _boşta_ |
| 02 · Jailbreak ve Red Teaming | _boşta_ |
| 03 · Guardrail ve Savunma | _boşta_ |
| 04 · Değerlendirme ve Standartlar | _boşta_ |
| 05 · Model ve Tedarik Zinciri | _boşta_ |
| 06 · Ajan, Araç ve MCP Güvenliği | _boşta_ |
| 07 · RAG ve Uygulama Güvenliği | _boşta_ |
| 08 · Türkçe Kaynaklar ve Veri Setleri | _boşta_ |
| 09 · Eğitim, Lab ve CTF | _boşta_ |
| Editörlük ve CI | [@fevziegeyurtsevenler](https://github.com/fevziegeyurtsevenler) |

Bir bölümü sahiplenmek istiyorsan [issue aç](https://github.com/fevziegeyurtsevenler/awesome-ai-security-tr/issues/new) — sahiplik adınla birlikte burada kalıcı olarak durur.

## İlgili Türkçe kaynaklar

Bu liste bir dizin. Konuları sırayla ve derinlemesine anlatan Türkçe rehberler ayrı repolarda:

- [LLM Security Türkiye](https://github.com/fevziegeyurtsevenler/LLM-Security-Turkiye) — Türkçe yapay zeka güvenliği ekosisteminin giriş noktası
- [LLM Security Nedir?](https://github.com/fevziegeyurtsevenler/LLM-Security-Nedir) — alanın Türkçe tanımı ve temelleri
- [Prompt Injection Nedir?](https://github.com/fevziegeyurtsevenler/Prompt-Injection-Nedir) — en kritik zafiyetin Türkçe işlenişi
- [OWASP LLM Top 10 Türkçe](https://github.com/fevziegeyurtsevenler/OWASP-LLM-TOP-10-TURKCE) — standardın Türkçe kapsamlı rehberi
- [LLM Security Roadmap](https://github.com/fevziegeyurtsevenler/LLM-Security-Roadmap) — sıfırdan uzmanlığa 7 aşamalı öğrenme planı
- [LLM Security Akademi](https://ai.altaysec.com.tr) — 5 öğrenme yolu, 14 modül, 35 uygulamalı lab

## Lisans

[CC BY 4.0](LICENSE) — kullan, çoğalt, uyarla. Tek şart: atıf ver.

<p align="center">
  <sub>
    <a href="https://altaysec.com.tr">AltaySec</a> tarafından yürütülüyor ·
    Küratör: <a href="https://github.com/fevziegeyurtsevenler">Fevzi Ege Yurtsevenler</a> ·
    Katkıya açık
  </sub>
</p>
