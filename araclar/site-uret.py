#!/usr/bin/env python3
"""kaynaklar/*.md dosyalarından indekslenebilir statik site üretir.

Her bölüm ayrı bir HTML sayfası olur; böylece her bölüm kendi arama
terimi için sıralanabilir. Çıktı site/ dizinine yazılır.

Kullanım:  python3 araclar/site-uret.py
"""

import html
import json
import pathlib
import re
import sys

import markdown

KOK = pathlib.Path(__file__).resolve().parent.parent
KAYNAK_DIZIN = KOK / "kaynaklar"
CIKTI = KOK / "site"

TABAN_URL = "https://fevziegeyurtsevenler.github.io/awesome-ai-security-tr"
REPO_URL = "https://github.com/fevziegeyurtsevenler/awesome-ai-security-tr"
YAZAR = "Fevzi Ege Yurtsevenler"
SON_GUNCELLEME = "2026-08-03"

SITE_ADI = "Yapay Zeka Güvenliği Kaynakları"
SITE_ACIKLAMA = (
    "Türkçe açıklamalı, küratörlü ve CI ile doğrulanan yapay zeka güvenliği "
    "kaynak listesi: prompt injection, jailbreak, red teaming, guardrail, "
    "ajan/MCP güvenliği, RAG güvenliği ve model tedarik zinciri."
)

# Bölüm dosyası -> (kısa ad, arama odaklı meta açıklama)
META = {
    "01-prompt-injection": (
        "Prompt Injection",
        "Prompt injection nedir, nasıl çalışır ve nasıl savunulur — Türkçe "
        "açıklamalı kaynaklar: temel okumalar, akademik makaleler, tespit "
        "araçları ve Türkçeye özgü bypass bulguları.",
    ),
    "02-jailbreak-red-teaming": (
        "Jailbreak ve Red Teaming",
        "LLM jailbreak ve yapay zeka red teaming kaynakları: metodoloji "
        "rehberleri, garak ve PyRIT gibi otomasyon araçları, saldırı veri "
        "setleri ve açık arenalar.",
    ),
    "03-guardrail-savunma": (
        "Guardrail ve Savunma",
        "LLM guardrail ve savunma kaynakları: NeMo Guardrails, Llama Guard, "
        "PII maskeleme ve guardrail'lerin gerçekte ne kadar çalıştığını "
        "gösteren ölçümler.",
    ),
    "04-degerlendirme-standartlar": (
        "Değerlendirme ve Standartlar",
        "Yapay zeka güvenliği standartları ve değerlendirme çerçeveleri: "
        "OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, AISVS ve ölçüt araçları.",
    ),
    "05-model-tedarik-zinciri": (
        "Model ve Tedarik Zinciri Güvenliği",
        "Model dosyası ve yapay zeka tedarik zinciri güvenliği: pickle "
        "riskleri, safetensors, veri zehirlenmesi, model imzalama ve ML-BOM.",
    ),
    "06-agent-mcp-guvenligi": (
        "Ajan, Araç ve MCP Güvenliği",
        "Yapay zeka ajanı ve MCP güvenliği kaynakları: tool poisoning, "
        "ölümcül üçlü, yetki sınırlama, ajan eklentisi denetim araçları.",
    ),
    "07-rag-uygulama-guvenligi": (
        "RAG ve Uygulama Güvenliği",
        "RAG güvenliği ve LLM uygulama güvenliği: bilgi tabanı zehirlenmesi, "
        "vektör veritabanı riskleri, eğitim verisi sızıntısı ve API katmanı.",
    ),
    "08-turkce-kaynaklar-veri-setleri": (
        "Türkçe Kaynaklar ve Veri Setleri",
        "Türkçe yapay zeka güvenliği kaynakları ve veri setleri: Türkçeye "
        "özgü ölçülmüş guardrail kör noktaları, KVKK, USOM ve Türkçe rehber "
        "serisi.",
    ),
    "09-egitim-lab-ctf": (
        "Eğitim, Lab ve CTF",
        "Yapay zeka güvenliği eğitimi, laboratuvarları ve CTF'leri: Gandalf, "
        "PortSwigger LLM lab'ları, HackAPrompt, ücretsiz kurslar ve bug "
        "bounty platformları.",
    ),
}

CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --bg:#ffffff; --bg-alt:#f8fafc; --metin:#0f172a; --soluk:#475569;
  --kenar:#e2e8f0; --vurgu:#6d28d9; --vurgu-2:#0e7490; --kod-bg:#f1f5f9;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#0b0f19; --bg-alt:#111827; --metin:#e6edf6; --soluk:#94a3b8;
    --kenar:#1f2a3a; --vurgu:#a78bfa; --vurgu-2:#22d3ee; --kod-bg:#131c2b;
  }
}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--metin);
  font-family:ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:17px; line-height:1.7;
}
.kabuk{max-width:860px;margin:0 auto;padding:0 20px}
header.ust{border-bottom:1px solid var(--kenar);background:var(--bg-alt)}
header.ust .kabuk{display:flex;align-items:center;gap:14px;padding:16px 20px;flex-wrap:wrap}
header.ust a.marka{
  font-weight:700;color:var(--metin);text-decoration:none;letter-spacing:-.3px;
}
header.ust nav{margin-inline-start:auto;display:flex;gap:16px;flex-wrap:wrap}
header.ust nav a{color:var(--soluk);text-decoration:none;font-size:14px}
header.ust nav a:hover{color:var(--vurgu)}
main{padding:40px 0 64px}
h1{font-size:clamp(28px,5vw,40px);line-height:1.2;letter-spacing:-1px;margin:0 0 8px}
h2{font-size:clamp(21px,3.4vw,26px);letter-spacing:-.4px;margin:44px 0 14px;
   padding-top:14px;border-top:1px solid var(--kenar)}
h3{font-size:19px;margin:28px 0 10px}
p{margin:0 0 16px}
a{color:var(--vurgu);text-underline-offset:2px}
a:hover{color:var(--vurgu-2)}
ul{padding-inline-start:22px}
li{margin:0 0 14px}
li em{color:var(--soluk);font-style:normal;font-size:14px}
blockquote{
  margin:0 0 24px;padding:14px 18px;border-inline-start:3px solid var(--vurgu);
  background:var(--bg-alt);border-radius:0 8px 8px 0;color:var(--soluk);
}
blockquote p{margin:0}
code{background:var(--kod-bg);padding:2px 6px;border-radius:5px;font-size:.88em;
     font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
pre{background:var(--kod-bg);padding:16px;border-radius:10px;overflow-x:auto}
pre code{background:none;padding:0}
.tablo-sar{overflow-x:auto;margin:0 0 24px}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{border:1px solid var(--kenar);padding:9px 12px;text-align:start;vertical-align:top}
th{background:var(--bg-alt);font-weight:600}
hr{border:0;border-top:1px solid var(--kenar);margin:32px 0}
.altbilgi{border-top:1px solid var(--kenar);background:var(--bg-alt);
          padding:26px 0;color:var(--soluk);font-size:14px}
.altbilgi .kabuk{display:flex;gap:12px;justify-content:space-between;flex-wrap:wrap}
.kartlar{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));
         padding:0;margin:0 0 28px;list-style:none}
.kart{border:1px solid var(--kenar);border-radius:12px;padding:16px 18px;background:var(--bg-alt);margin:0}
.kart a{font-weight:650;text-decoration:none;font-size:17px}
.kart p{margin:6px 0 0;font-size:14px;color:var(--soluk);line-height:1.55}
.kart .sayi{font-size:12px;color:var(--soluk);font-family:ui-monospace,Menlo,monospace}
.rozetler{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 26px;padding:0;list-style:none}
.rozet{font-size:13px;border:1px solid var(--kenar);border-radius:999px;
       padding:4px 12px;color:var(--soluk);background:var(--bg-alt)}
.giris{font-size:19px;color:var(--soluk);margin:0 0 26px}
img{max-width:100%;height:auto}
@media (max-width:520px){body{font-size:16px}main{padding:28px 0 48px}}
"""


def md_to_html(metin: str) -> str:
    return markdown.markdown(
        metin,
        extensions=["tables", "fenced_code", "attr_list", "toc"],
        output_format="html5",
    )


def sar_tablolari(icerik: str) -> str:
    """Geniş tabloların sayfayı yatay kaydırmasını engelle."""
    return icerik.replace("<table>", '<div class="tablo-sar"><table>').replace(
        "</table>", "</table></div>"
    )


def sayfa(*, baslik, aciklama, govde, yol, jsonld, nav_aktif=""):
    kanonik = f"{TABAN_URL}/{yol}" if yol else f"{TABAN_URL}/"
    tam_baslik = baslik if baslik == SITE_ADI else f"{baslik} — {SITE_ADI}"
    kok = "../" if "/" in yol else ""
    bolumler_nav = f"{kok}bolumler.html" if kok else "bolumler.html"
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(tam_baslik)}</title>
<meta name="description" content="{html.escape(aciklama)}">
<link rel="canonical" href="{kanonik}">
<meta name="author" content="{YAZAR}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{html.escape(SITE_ADI)}">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{html.escape(tam_baslik)}">
<meta property="og:description" content="{html.escape(aciklama)}">
<meta property="og:url" content="{kanonik}">
<meta property="og:image" content="{TABAN_URL}/afis.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(tam_baslik)}">
<meta name="twitter:description" content="{html.escape(aciklama)}">
<meta name="twitter:image" content="{TABAN_URL}/afis.svg">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🛡️</text></svg>">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False, indent=1)}</script>
</head>
<body>
<header class="ust"><div class="kabuk">
  <a class="marka" href="{kok if kok else ''}index.html">🛡️ {html.escape(SITE_ADI)}</a>
  <nav>
    <a href="{bolumler_nav}">Bölümler</a>
    <a href="{REPO_URL}">GitHub</a>
    <a href="{REPO_URL}/blob/main/CONTRIBUTING.md">Katkı</a>
    <a href="https://altaysec.com.tr">AltaySec</a>
  </nav>
</div></header>
<main><div class="kabuk">
{govde}
</div></main>
<footer class="altbilgi"><div class="kabuk">
  <span>CC BY 4.0 · Küratör: <a href="https://github.com/fevziegeyurtsevenler">{YAZAR}</a></span>
  <span>Son güncelleme: {SON_GUNCELLEME} · <a href="{REPO_URL}">Kaynak repo</a></span>
</div></footer>
</body>
</html>
"""


def bolum_verisi():
    veriler = []
    for yol in sorted(KAYNAK_DIZIN.glob("*.md")):
        anahtar = yol.stem
        if anahtar not in META:
            print(f"uyarı: {anahtar} için meta tanımı yok, atlanıyor", file=sys.stderr)
            continue
        ham = yol.read_text(encoding="utf-8")
        kisa_ad, meta_aciklama = META[anahtar]
        sayi = len(re.findall(r"^- \[", ham, flags=re.M))
        ozet = ""
        m = re.search(r"^> (.+)$", ham, flags=re.M)
        if m:
            ozet = m.group(1).strip()
        veriler.append(
            {
                "anahtar": anahtar,
                "ad": kisa_ad,
                "meta": meta_aciklama,
                "ozet": ozet,
                "sayi": sayi,
                "ham": ham,
                "cikti": f"bolum/{anahtar}.html",
            }
        )
    return veriler


def uret():
    bolumler = bolum_verisi()
    if not bolumler:
        print("hata: hiç bölüm bulunamadı", file=sys.stderr)
        return 1

    toplam = sum(b["sayi"] for b in bolumler)
    CIKTI.mkdir(parents=True, exist_ok=True)
    (CIKTI / "bolum").mkdir(exist_ok=True)

    # afiş (OG görseli olarak da kullanılıyor)
    (CIKTI / "afis.svg").write_text(
        (KOK / "varlik" / "afis-koyu.svg").read_text(encoding="utf-8"), encoding="utf-8"
    )

    # --- ana sayfa ---
    kartlar = "\n".join(
        f'  <li class="kart"><a href="{b["cikti"]}">{html.escape(b["ad"])}</a>'
        f'<p>{html.escape(b["ozet"])}</p>'
        f'<p class="sayi">{b["sayi"]} kaynak</p></li>'
        for b in bolumler
    )
    ana_govde = f"""<h1>{html.escape(SITE_ADI)}</h1>
<p class="giris">Türkçe açıklamalı, küratörlü ve CI ile doğrulanan yapay zeka güvenliği kaynak dizini.</p>
<ul class="rozetler">
  <li class="rozet">{toplam} kaynak</li>
  <li class="rozet">{len(bolumler)} bölüm</li>
  <li class="rozet">CC BY 4.0</li>
  <li class="rozet">ölü link taraması: haftalık</li>
</ul>
<p>İngilizce awesome-list'ler var; her kaynağın yanında <strong>neden orada olduğunu Türkçe anlatan</strong>
ve ölü linkleri otomatik tarayan bir liste yoktu. Buradaki her girdi bir insan tarafından açılıp okundu.</p>
<h2>Bölümler</h2>
<ul class="kartlar">
{kartlar}
</ul>
<h2>Neden Türkçe için ayrı bir liste?</h2>
<p>Bir guardrail'in İngilizcede iyi olması Türkçede iyi olduğu anlamına gelmiyor. Aşağıdakiler tahmin değil,
açık veri setleriyle birlikte yayımlanmış ölçümler:</p>
<div class="tablo-sar"><table>
<tr><th>Bulgu</th><th>Ölçüm</th></tr>
<tr><td>Türkçe harf katlaması (<code>"İGNORE".lower() != "ignore"</code>) naif filtreleri atlatıyor</td><td>%94.6 bypass</td></tr>
<tr><td>Bir guard modeli zararsız Türkçe istekleri reddediyor (İngilizcesinde %0.8)</td><td>%59 aşırı-red</td></tr>
<tr><td>Popüler bir jailbreak sınıflandırıcısı Türkçe saldırıları kaçırıyor</td><td>%83 kaçırma</td></tr>
</table></div>
<h2>Katkı</h2>
<p>Bölüm sahibi veya atama yok; istediğin bölüme PR atabilirsin. Tek kural: çıplak link kabul edilmiyor —
her girdinin yanında 1-2 cümle Türkçe açıklama olmalı, ve eklediğin kaynağı okumuş olmalısın.
Ayrıntı için <a href="{REPO_URL}/blob/main/CONTRIBUTING.md">katkı rehberi</a>.</p>
"""
    ana_jsonld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{TABAN_URL}/#website",
                "name": SITE_ADI,
                "url": f"{TABAN_URL}/",
                "description": SITE_ACIKLAMA,
                "inLanguage": "tr-TR",
                "author": {"@type": "Person", "name": YAZAR},
            },
            {
                "@type": "CollectionPage",
                "@id": f"{TABAN_URL}/#collection",
                "name": SITE_ADI,
                "url": f"{TABAN_URL}/",
                "description": SITE_ACIKLAMA,
                "inLanguage": "tr-TR",
                "dateModified": SON_GUNCELLEME,
                "isPartOf": {"@id": f"{TABAN_URL}/#website"},
                "hasPart": [
                    {
                        "@type": "WebPage",
                        "name": b["ad"],
                        "url": f"{TABAN_URL}/{b['cikti']}",
                        "description": b["meta"],
                    }
                    for b in bolumler
                ],
            },
        ],
    }
    (CIKTI / "index.html").write_text(
        sayfa(
            baslik=SITE_ADI,
            aciklama=SITE_ACIKLAMA,
            govde=ana_govde,
            yol="",
            jsonld=ana_jsonld,
        ),
        encoding="utf-8",
    )

    # --- bölüm listesi sayfası ---
    liste_govde = (
        "<h1>Bölümler</h1>\n"
        f'<p class="giris">{len(bolumler)} bölüm, toplam {toplam} küratörlü kaynak.</p>\n'
        f'<ul class="kartlar">\n{kartlar}\n</ul>'
    )
    (CIKTI / "bolumler.html").write_text(
        sayfa(
            baslik="Bölümler",
            aciklama=f"Yapay zeka güvenliği kaynak listesinin {len(bolumler)} bölümü: "
            + ", ".join(b["ad"] for b in bolumler)
            + ".",
            govde=liste_govde,
            yol="bolumler.html",
            jsonld={
                "@context": "https://schema.org",
                "@type": "ItemList",
                "name": "Bölümler",
                "numberOfItems": len(bolumler),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": i,
                        "name": b["ad"],
                        "url": f"{TABAN_URL}/{b['cikti']}",
                    }
                    for i, b in enumerate(bolumler, 1)
                ],
            },
        ),
        encoding="utf-8",
    )

    # --- bölüm sayfaları ---
    for b in bolumler:
        ham = b["ham"]
        # repo içi göreli linkleri sitede çalışır hâle getir
        ham = ham.replace("../CONTRIBUTING.md", f"{REPO_URL}/blob/main/CONTRIBUTING.md")
        govde = sar_tablolari(md_to_html(ham))
        jsonld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": f"{b['ad']} — Türkçe kaynaklar",
            "description": b["meta"],
            "inLanguage": "tr-TR",
            "url": f"{TABAN_URL}/{b['cikti']}",
            "dateModified": SON_GUNCELLEME,
            "author": {"@type": "Person", "name": YAZAR},
            "isPartOf": {"@id": f"{TABAN_URL}/#website"},
            "breadcrumb": {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": SITE_ADI,
                        "item": f"{TABAN_URL}/",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": b["ad"],
                        "item": f"{TABAN_URL}/{b['cikti']}",
                    },
                ],
            },
        }
        (CIKTI / b["cikti"]).write_text(
            sayfa(
                baslik=b["ad"],
                aciklama=b["meta"],
                govde=govde,
                yol=b["cikti"],
                jsonld=jsonld,
            ),
            encoding="utf-8",
        )

    # --- sitemap + robots ---
    yollar = ["", "bolumler.html"] + [b["cikti"] for b in bolumler]
    girisler = "\n".join(
        f"  <url><loc>{TABAN_URL}/{y}</loc><lastmod>{SON_GUNCELLEME}</lastmod>"
        f"<changefreq>weekly</changefreq><priority>{'1.0' if y == '' else '0.8'}</priority></url>"
        for y in yollar
    )
    (CIKTI / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{girisler}\n</urlset>\n",
        encoding="utf-8",
    )
    (CIKTI / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {TABAN_URL}/sitemap.xml\n", encoding="utf-8"
    )
    # Jekyll işlemesini kapat
    (CIKTI / ".nojekyll").write_text("", encoding="utf-8")

    print(f"site üretildi: {len(bolumler)} bölüm, {toplam} kaynak, {len(yollar) } sayfa")
    return 0


if __name__ == "__main__":
    sys.exit(uret())
