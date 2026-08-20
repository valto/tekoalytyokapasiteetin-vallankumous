# Julkaisuresurssi #7 — Globaali perustaso -työkirja
## Energiasta tokeneihin: tuotantokustannuskäyrät — Kotitalous, Osuustoiminnallinen, Ammattimainen, Hyperskaala

**Osa julkaisua:** "Miksi tekoälyyn investoidaan biljoonia?" — Valto Loikkanen, CC BY 4.0
**Mallin tila:** Luonnos v0.1, muokattava perustaso
**Valuuttaperustaso:** Globaali USD (ks. paikallistamishuomautus alla)
**Tässä käytettyjen syötteiden lähdeaikarajaus:** 2026-08-13
**Ei sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa.** Jokainen alla oleva skenaario on muokattava havainnollistus, rakennettu ilmoitetuille oletuksille — ei ennuste tai suositus.

---

## Näyttöluokkien selite (käytössä joka taulukossa)

| Tunniste | Merkitys |
|---|---|
| **FAKTA** | Ensisijainen dokumentaatio, virallinen tekninen tietolomake tai suoraan haettu ensisijainen lähde, tarkistettu 2026-08-12 tai välittömästi sitä ennen. |
| **LÄHDE** | Nimetyn henkilön/organisaation julkinen, tallenteella oleva lausunto. Ei itsenäisesti todistettu vain siksi, että se on sanottu. |
| **LASKELMA** | Läpinäkyvä aritmetiikka siteeratuista FAKTA-/LÄHDE-syötteistä. Kaava aina esitetty. |
| **OLETUS** | Näkyvä, muokattava skenaarioparametri — ei markkinafakta. Se, mitä se hallitsee, on ilmoitettu. |
| **TULKINTA** | Merkitty selitys siitä, miten yllä olevat voivat liittyä toisiinsa. Ei koskaan fakta. |

---

## Miten mukauttaa tätä työkirjaa omiin lukuihin

Tämä työkirja on rakennettu erotettujen taloudellisten kerrosten ketjuna, jota ei koskaan tiivistetä yhdeksi luvuksi:

```
raaka sähkökustannus → laitteiston poistettu tuotantokustannus → rahoitettu omaisuuskustannus → täysi toimintakustannus
→ kapasiteetti-/käyttöastekustannus → tokenin tuotantokustannus → työkuorman/työkapasiteetin kustannus
→ tulos ja arvo (EI yllä olevien kerrosten mekaanisesti määräämä)
```

Ajaaksesi minkä tahansa tason uudelleen omilla luvuillasi, korvaa vain merkityt **OLETUS**-solut — jokainen **FAKTA**-solu on vahvistettu tekninen tieto/hinta, ja sitä pitäisi muuttaa vain, jos sinulla on uudempi ensisijainen lähde:

1. **Pääomakustannus** — vaihda tilalle todellinen ostohintasi/tarjouksesi (vero, toimitus, tuontitulli poissuljettu, ellet lisää niitä).
2. **Rahoitusehdot** — käsiraha-%, korkokanta ja rahoitusaika (vuosina) ovat kaikki muokattavia; kaava on standardi tasaerälaina, esitetty kertaalleen alla, jotta voit käyttää sitä uudelleen missä tahansa.
3. **Sähkön hinta ($/kWh)** — korvaa matala/keski/korkea-skenaario omalla paikallisella teollisuus-, kaupallisella tai kotitaloustariffillasi. Tämä on koko mallin yksittäisenä syötteenä paikallisesti kaikkein vaihtelevin (hinnat noin 0,03 $/kWh:sta noin 0,40 $/kWh:iin ovat olemassa todellisilla globaaleilla markkinoilla).
4. **Käyttöaste (%)** — osuus vuoden 8 760 tunnista, jonka laitteisto todella tuottaa tokeneita jouten olon sijaan. Tämä on tavallisesti koko mallin yksittäisenä muuttujana suurin vipu $/miljoona-tokenia-kustannukseen — esitetty aina matala/keski/korkea-tasoina, ei koskaan yhtenä pistearviona.
5. **Läpimenoteho (tokenia/sek)** — vaihda tilalle omaa mallia/kvantisointia/kehystä koskeva oma vertailuarvosi. Älä käytä uudelleen NVIDIA:n tai muun toimittajan vertailulukua eri mallille, tarkkuudelle tai vuorovaikutteisuusasetukselle — läpimenoteho on työkuormakohtainen ja voi vaihdella 10–50-kertaisesti tavoiteltavasta viiveestä riippuen (ks. Hyperskaalatason huomautukset).
6. **Käyttömenot/hallinnolliset yleiskustannukset** — lisää omat tila-, henkilöstö-, vakuutus-, jäähdytys- ja verkkokustannuksesi; tässä esitetyt havainnollistavat kaistat ovat paikkamerkkejä, nimenomaisesti merkitty OLETUKSEKSI.
7. **Valuutta** — jokainen alla oleva luku on USD:ssä. FX-rivi näytetään vain silloin, kun se on tarpeen täsmäyttämään EUR-määräistä aiempaa lukua vasten; vaihda tilalle omaa valuuttaasi vastaava kurssi ja päivämäärä muille valuutoille.

**Kaava, jota käytetään joka "pääoma + rahoitus vuodessa" -rivillä (LASKELMA, standardi tasaerälainan kaava):**

```
down_payment = price × down_payment_%
financed_amount = price − down_payment
annual_loan_payment = financed_amount × rate / (1 − (1 + rate)^(−term_years))
capital_and_financing_per_year = annual_loan_payment + (down_payment / term_years)
```

Jälkimmäinen termi jakaa käsirahan tasaisesti rahoitusajan yli puhtaasti vuositasoisen vertailukelpoisuuden vuoksi — voit halutessasi käsitellä käsirahan sen sijaan yhden kerran vuonna 0 syntyvänä kustannuksena; molemmat ovat perusteltuja, ja ne on merkitty tässä mallinnusvalinnaksi, ei faktaksi.

**Kaava, jota käytetään joka "$/miljoona tokenia" -rivillä (LASKELMA):**

```
annual_tokens = throughput_tokens_per_sec × 3600 × 8760 × utilization_%
cost_per_million_tokens = (capital_and_financing_per_year + electricity_cost_per_year + opex_per_year)
                            / (annual_tokens / 1 000 000)
```

**Kaava, jota käytetään joka "$/tekoäly-työtunti" -rivillä (LASKELMA):**

```
cost_per_working_hour = cost_per_million_tokens × (tokens_per_working_hour_for_usage_mode / 1 000 000)
```

jossa `tokens_per_working_hour_for_usage_mode` tulee luvussa 6 määritellyistä käyttöintensiteettivyöhykkeistä.

---

## 1. Kriittinen menetelmäsääntö — tätä ei saa ohittaa

**Omistettu tuotantokustannus ja vähittäis-API-hinta ovat kaksi eri taloudellista kerrosta, ja niitä ei koskaan saa yhdistää yhdeksi luvuksi.**

- Alla olevat taulukot hinnoittelevat *tokenien tuottamisen kustannuksen laitteistolla, jonka omistat tai osaomistat*, ajaen **avoimen painotuksen malleja** (esim. Qwen, DeepSeek, Kimi-luokan mallit) — riippumatta siitä, mitä OpenAI, Anthropic tai Google veloittavat omista patentoiduista, suljetuista malleistaan.
- Vähittäis-API-hinnat (luku 7) ovat erillinen vertailukohta — "osta sähköä verkosta" -vastine "tuota omaa aurinkosähköä" -vaihtoehdolle. Ne kertovat, mitä maksaa vuokrata jonkun toisen valmis tokenintuotantokapasiteetti; ne eivät kerro, mitä maksaa rakentaa ja ajaa omaa.
- Aiempi vaihe tässä tutkimuksessa yhdisti virheellisesti laboratorion vähittäishinnoittelun omistetun laitteiston kustannuskäyrään, ja se oli itsekorjattava kesken istunnon. Tämä korjaus on säilytetty tässä tarkoituksella, työstettynä "miten tätä ei kannata mallintaa" -opetuksena, ei siloteltuna pois.

---

## 2. KOTITALOUSTASO — yksi NVIDIA DGX Spark

### 2.1 Pääoma ja rahoitus

| Syöte | Arvo | Luokka |
|---|---|---|
| DGX Spark, Founders Edition, nykyinen suositushinta | 4 699 $ | **FAKTA** — NVIDIA Developer Forumsin virallinen hinnanmuutosilmoitus, voimaan viikolla 2026-02-23 (nostettu alkuperäisestä lanseeraushinnasta 3 999 $). URL: forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713 |
| Käsiraha | 20% (939,80 $) | **OLETUS** — hallitsee, kuinka paljon rahoitetaan vs. maksetaan etukäteen |
| Rahoituskorko | 8%/vuosi | **OLETUS** — havainnollistava kuluttaja-/pienyritysluoton korko |
| Rahoitusaika | 5 vuotta | **OLETUS** — hallitsee annuiteetin kokoa; esitetty 3/4/5/7 vuoden herkkyystarkastelulla alla |

| Kaava | Tulos |
|---|---|
| `financed_amount = 4 699 $ − 939,80 $ = 3 759,20 $` | — |
| `annual_loan_payment = 3 759,20 $ × 0.08 / (1 − 1.08^−5) = 941,52 $` | — |
| `capital_and_financing_per_year = 941,52 $ + (939,80 $/5) = 941,52 $ + 187,96 $` | **1 129,48 $/yr** |

Suoraviivainen käteisostovertailu (ei rahoitusta): `4 699 $ / 5 = 939,80 $/yr` (**LASKELMA**) — esitetty, jotta voit verrata "maksa käteisellä" vs. "rahoita" -kehystä.

**Rahoitusajan herkkyys (LASKELMA, sama 8% korko, 20% käsiraha):**

| Aika | Annuiteettimaksu/vuosi | Pääoma+rahoitus/vuosi (sis. jaettu käsiraha) |
|---|---|---|
| 3 vuotta | 1 447,79 $ | 1 635,72 $ |
| 4 vuotta | 1 135,02 $ | 1 322,95 $ |
| 5 vuotta | 941,52 $ | 1 129,48 $ |
| 7 vuotta | 702,35 $ | 890,31 $ |

### 2.2 Sähkö

| Syöte | Arvo | Luokka |
|---|---|---|
| Suurin jatkuva tehonotto | 240W (virtalähteen luokitus); GB10-SoC:n TDP 140W | **FAKTA** — NVIDIA:n virallinen DGX Spark -tuotesivu |
| Sähkön hintaskenaariot | Matala 0,06 $/kWh · Keski 0,12 $/kWh · Korkea 0,25 $/kWh | **OLETUS** — korvaa omalla paikallisella kotitalous-/kaupallisella tariffillasi |

### 2.3 Läpimenoteho (tokenia/sek) — vertailuarvon perusta

| Skenaario | tok/s | Luokka |
|---|---|---|
| Matala (INT4-perustaso, vLLM+AutoRound+FlashInfer) | 28.3 | **FAKTA** — NVIDIA Developer Forumsin ketju, kirjoittaja "Albond," Qwen3.5-122B-A10B yhdellä DGX Sparkilla, suoraan näkyvä viestin sisältö |
| Keski (hybridi INT4+FP8-kvantisointi) | 30.8 | **FAKTA** — sama ketju, +8,8 % perustasoon nähden |
| Korkea (+ MTP-1-spekulatiivinen dekoodaus, "todennäköisesti muistikaistanleveyden katto" viestin kirjoittajan mukaan) | 38.4 | **FAKTA** — sama ketju, +25% perustasoon nähden |
| Otsikkotason väite (vahvistamaton) | jopa 51 | **LÄHDE** — saman ketjun omassa yhteenvetorivissä viitataan myöhempään viestiin (#71), jota ei ole itsenäisesti nähty tässä tarkistuksessa; käsittele vahvistamattomana |

**Tokenia/kWh 240W:llä (LASKELMA):**

| Läpimenoteho | Tokenia/tunti | Tokenia/kWh |
|---|---|---|
| 28.3 tok/s | 101 880 | 424 500 |
| 30.8 tok/s | 110 880 | 462 000 |
| 38.4 tok/s | 138 240 | 576 000 |
| 51 tok/s (vahvistamaton) | 183 600 | 765 000 |

`tokens_per_kWh = tok/s × 3600 / kW_draw` — esim. `30.8 × 3600 / 0.240 = 462 000`.

### 2.4 Kotitaloustaso — täysi tuotantokustannuskäyrä ($/miljoona tokenia)

Käyttöaste = osuus vuoden 8 760 tunnista, jonka kone todella tuottaa tokeneita jouten olon sijaan. **OLETUS**, esitetty matala/keski/korkea-tasoina.

| Läpimenoteho | Käyttöaste | Sähkön hinta | Vuotuiset tokenit (LASKELMA) | Sähkökustannus/vuosi (LASKELMA) | **$/miljoona tokenia (LASKELMA)** |
|---|---|---|---|---|---|
| 30.8 tok/s | Matala 10% | 0,12 $ | 97.1M | 25 $ | **11,89 $** |
| 30.8 tok/s | Keski 40% | 0,12 $ | 388.5M | 101 $ | **3,17 $** |
| 30.8 tok/s | Korkea 80% | 0,12 $ | 777.0M | 202 $ | **1,71 $** |
| 38.4 tok/s | Matala 10% | 0,12 $ | 121.1M | 25 $ | **9,53 $** |
| 38.4 tok/s | Keski 40% | 0,12 $ | 484.4M | 101 $ | **2,54 $** |
| 38.4 tok/s | Korkea 80% | 0,12 $ | 968.8M | 202 $ | **1,37 $** |
| 30.8 tok/s | Keski 40% | Matala 0,06 $ | 388.5M | 50 $ | **3,04 $** |
| 30.8 tok/s | Keski 40% | Korkea 0,25 $ | 388.5M | 210 $ | **3,45 $** |

`cost_per_million_tokens = (1 129,48 $ + electricity_cost) / (annual_tokens/1 000 000)`.

**Näin tätä luetaan:** kotitalousmittakaavassa pääoma+rahoitus hallitsee kustannuskäyrää — sähkö on pyöristysvirhe (~13–420 $/vuosi vs. ~1 130 $/vuosi rahoitusta). Käyttöaste on selvästi suurin vipu: siirtyminen 10%:sta 80%:iin käyttöasteessa samalla läpimenoteholla leikkaa $/M-tokenia-lukua noin 7-kertaisesti, koska kiinteä rahoituskustannus jakautuu paljon useammalle tokenille.

### 2.5 Kotitaloustaso — $/tekoäly-työtunti (keskiskenaario: 30.8 tok/s, 40% käyttöaste, 0,12 $/kWh → 3,17 $/M tokenia)

| Käyttöintensiteettivyöhyke (ks. luku 6) | Tokenia/tunti | **$/tekoäly-työtunti (LASKELMA)** |
|---|---|---|
| Chat/neuvonantaja | 10 000-30 000 | 0,032–0,095 $ |
| Aktiivinen tekoälytyötoveri/kopilotti | 60 000-120 000 | 0,190–0,380 $ |
| Delegoitu yksittäisagentti | 200 000-600 000 | 0,633–1,900 $ |
| Raskas moniagenttiorkestrointi | 1 000 000-12 000 000 | 3,17–38,00 $ |

Korkean käyttöasteen skenaariossa (1,71 $/M tokenia) samat kaistat ovat noin 46% matalammat; matalan käyttöasteen skenaariossa (11,89 $/M tokenia) noin 3.75x korkeammat. Ilmoita aina, mitä käyttöastesenaariota jokin $/työtunti-luku olettaa.

---

## 3. OSUUSTOIMINNALLINEN TASO — 50 jäsentä, 10 DGX Sparkia

### 3.1 Pääoma ja rahoitus (10 konetta)

Samat yksikkökohtaiset hinta-/rahoitusehdot kuin luvussa 2.1, skaalattuna ×10 (**LASKELMA**):

| Erä | Per kone | ×10 konetta |
|---|---|---|
| Pääoma+rahoitus/vuosi | 1 129,48 $ | **11 294,76 $/yr** |

### 3.2 Sähkö (10 konetta)

Yhteenlaskettu suurin jatkuva tehonotto: `0.240kW × 10 = 2.4kW` (**LASKELMA**, johdettu FAKTA-yksikkökohtaisesta spesifikaatiosta).

### 3.3 Hallinto/yleiskustannukset — osuustoiminnallisen tason omat kustannuskerros

| Skenaario | $/vuosi | Luokka |
|---|---|---|
| Matala | 1 000 $ | **OLETUS** — kevyt itsehallinnoitu koordinaatio |
| Keski | 3 000 $ | **OLETUS** — osa-aikainen hallinto, perusverkkolaitteisto |
| Korkea | 6 000 $ | **OLETUS** — omistettu koordinaattoriaika, redundantti verkko |

### 3.4 Osuustoiminnallinen taso — tuotantokustannuskäyrä ($/miljoona tokenia), yhteenlaskettu läpimenoteho 10×30.8 tok/s = 308 tok/s

| Käyttöaste | Vuotuiset tokenit (LASKELMA) | Sähkö/vuosi (0,12 $/kWh, LASKELMA) | Yhteensä/vuosi (sis. 3 000 $ hallinto) | **$/miljoona tokenia (LASKELMA)** |
|---|---|---|---|---|
| Matala 20% | 1.94B | 505 $ | 14 799 $ | **7,62 $** |
| Keski 50% | 4.86B | 1 261 $ | 15 556 $ | **3,20 $** |
| Korkea 85% | 8.26B | 2 144 $ | 16 439 $ | **1,99 $** |

### 3.5 Osuustoiminnallinen taso — $/jäsen/kk (LASKELMA)

`total_cost_per_year / 50 members / 12 months`:

| Käyttöaste | Yhteensä/vuosi | **$/jäsen/kk** | €/jäsen/kk (FX-OLETUS: 1 USD = 0.92 EUR) |
|---|---|---|---|
| Matala 20% | 14 799 $ | **24,67 $** | 22,69 € |
| Keski 50% | 15 556 $ | **25,93 $** | 23,85 € |
| Korkea 85% | 16 439 $ | **27,40 $** | 25,21 € |

### 3.6 Osuustoiminnallinen taso — $/tekoäly-työtunti (keskiskenaario, 3,20 $/M tokenia)

| Käyttöintensiteettivyöhyke | Tokenia/tunti | **$/tekoäly-työtunti** |
|---|---|---|
| Chat/neuvonantaja | 10 000-30 000 | 0,032–0,096 $ |
| Aktiivinen tekoälytyötoveri/kopilotti | 60 000-120 000 | 0,192–0,384 $ |
| Delegoitu yksittäisagentti | 200 000-600 000 | 0,641–1,922 $ |
| Raskas moniagenttiorkestrointi | 1 000 000-12 000 000 | 3,20–38,44 $ |

### 3.7 42 €/jäsen/kk-luku — ratkaistu, ks. Tokenitehtaan skenaariotyökirja §1

**Korjattu 2026-08-13:** tämän luvun aiempi versio käsitteli kirjoittajan julkaistua ~42 €/jäsen/kk-lukua ja tämän työkirjan ~23–25 €/jäsen/kk DGX Spark -uudelleenlaskelmaa ratkaisemattomana erimielisyytenä, joka vaatisi käänteismallintamista (tämän luvun aiempi sisältö yritti juuri tätä, onnistumatta). Kirjoittaja on sen jälkeen selventänyt, että 42 €/jäsen/kk ei ollut koskaan perustunut DGX Spark -hinnoitteluun — se rakennettiin hänen omalle havainnollistavalle 100 000 €-excluding-VAT -pääomaoletukselleen jaetulle työasemaluokan koneelle (esim. NVIDIA DGX Station -tyyppinen järjestelmä), jolle NVIDIA julkaisee spesifikaatiot mutta ei vähittäishintaa. Kaksi lukua kuvaavat kahta eri laitteistotasoa, ei yhtä mittausta epävarmalla lähteellä.

**Ks. Tokenitehtaan skenaariotyökirja (Julkaisuresurssi #10), §1/§1a/§1b, täydelle korjatulle selitykselle, 100 000 €-pääomaperustan aritmetiikalle ja molempien laitteistotasojen rinnakkaisvertailulle.** Tämän työkirjan oma ~23–25 €/jäsen/kk-luku (§3.5-3.6 yllä) pysyy pätevänä ja muuttumattomana DGX Spark -tason skenaariona.

---

## 4. AMMATTIMAINEN TASO — yksi NVIDIA HGX B300 (8-GPU) -solmu

**Tärkeä varaus alkuun:** NVIDIA:n virallinen HGX B300 -tuotesivu (FAKTA-spesifikaatiot alla) **ei** julkaista tehonkulutuslukua eikä hintaa tälle SKU:lle. Molemmat ovat siis **OLETUS**, ei FAKTA, tällä tasolla — huomattavasti alempi luottamustaso kuin Kotitalous- ja Hyperskaalatasoilla, joissa laitteiston hinta ja/tai teho on suoraan lähdetettyä.

### 4.1 Spesifikaatiot (FAKTA) vs. kustannussyötteet (OLETUS)

| Erä | Arvo | Luokka |
|---|---|---|
| GPU:t | 8× NVIDIA Blackwell Ultra (SXM) | **FAKTA** — nvidia.com/en-us/data-center/hgx/ |
| Kokonaismuisti | 2.1 TB | **FAKTA** |
| NVFP4-päättely | 144 PFLOPS harva / 108 PFLOPS tiivis | **FAKTA** |
| NVLink5-kaistanleveys | 1.8 TB/s per GPU-linkki, 14.4 TB/s yhteensä | **FAKTA** |
| Verkotus | 1.6 TB/s | **FAKTA** |
| Tehonkulutus | Matala 8kW · Keski 11kW · Korkea 15kW | **OLETUS** — ei ensisijaista lähdettä; skaalattu havainnollisesti GB300 NVL72:n 135kW/72-GPU-räkkisuhteesta plus isäntälaitteiston yleiskustannusmarginaali |
| Pääomakustannus | Matala 250 000 $ · Keski 350 000 $ · Korkea 500 000 $ | **OLETUS** — julkista hintaa tälle SKU:lle ei löytynyt; vain paikkamerkkivaihteluväli |

### 4.2 Läpimenoteho — johdettu lineaarisella GPU-määrän skaalauksella FAKTA-per-GPU MLPerf-luvuista

| Perusta | Per-GPU tok/s (FAKTA, MLPerf v6.0 DeepSeek-R1) | ×8 GPU:ta (LASKELMA) |
|---|---|---|
| Offline-skenaario | 9 821 | 78 568 tok/s |
| Server-skenaario (vuorovaikutteinen) | 8 064 | 64 512 tok/s |

**Varaus (kannettu lähderekisteristä):** 9 821/8 064-per-GPU-luvut mitattiin 72-GPU:n NVL72-NVLink-domainin sisällä Grace-suorittimilla ja räkkitason muistikoherenssilla — 8-GPU HGX-laatikko (ei NVL72-räkkitason kytkentää, ei Grace-suoritintasoa) tuskin toistaa tätä per-GPU-nopeutta samalla tarkkuudella/mallilla. Käsittele tätä LASKELMA-lukua optimistisena ylärajana, ei vahvistettuna HGX B300 -vertailutuloksena.

### 4.3 Ammattimainen taso — tuotantokustannuskäyrä ($/miljoona tokenia), keskipääoma 350 000 $, keskiteho 11kW, offline-johdettu läpimenoteho 78 568 tok/s, 0,10 $/kWh sähkö

**Soveltamisalan korjaus, lisätty 2026-08-13: tämän taulukon luvut ovat VAIN pääoma + rahoitus + sähkö — mitään käyttömeno-/yleiskustannuskerrosta ei ole sisällytetty.** Tämä tekee niistä rakenteellisesti vertailukelvottomia Hyperskaalatason kanonisen luvun (§5.6) kanssa, joka nimenomaisesti sisältää 200 000 $–1 000 000 $/räkki/vuosi käyttömenoja (tila, jäähdytys raaka sähkön ylittävältä osin, henkilöstö, verkko, korvausvaraus). Tämän työkirjan aiempi versio ja emo-whitepaper vertasivat Ammattimaisen tason 0,044–0,146 $/M-lukua suoraan Hyperskaalatason 0,091–0,312 $/M-lukuun ikään kuin molemmat olisivat koko kerroksen lukuja, mikä sai Ammattimaisen tason näyttämään keinotekoisesti halvemmalta. Sitä ei esitetä tässä halvempana kuin Hyperskaala — ks. havainnollistava käyttömenoherkkyys välittömästi alla.

| Käyttöaste | Vuotuiset tokenit (LASKELMA) | Sähkö/vuosi (LASKELMA) | Pääoma+rahoitus/vuosi (5v@8%, LASKELMA) | **$/miljoona tokenia, EI KÄYTTÖMENOJA (LASKELMA)** |
|---|---|---|---|---|
| Matala 25% | 619.4B | 2 409 $ | 87 660 $ | **0,146 $** |
| Keski 60% | 1 486,6B | 5 782 $ | 87 660 $ | **0,064 $** |
| Korkea 90% | 2 229,9B | 8 672 $ | 87 660 $ | **0,044 $** |

`annuity_payment(350 000 $, 8%, 5v) = 87 660 $/yr` samalla kaavalla kuin luvussa 1.

**Havainnollistava käyttömenoherkkyys (OLETUS, lisätty 2026-08-13 — ei johdettu mistään vahvistetusta yksittäisen solmun käyttömenoluvusta, koska sellaista ei ole olemassa tämän hankkeen lähderekisterissä):** yksittäinen 8-GPU-solmu tarvitsee todennäköisesti huomattavasti vähemmän tila-/henkilöstö-/verkkoyleiskustannuksia kuin täysi räkki, mutta on erittäin epätodennäköistä, että se tarvitsisi nollaa. Käyttäen havainnollistavaa 10 000 $/25 000 $/50 000 $-vuosittaista matala/keski/korkea-käyttömenokaistaa — nimenomaan skaalaamatta sitä suhteessa Hyperskaalatason räkkikohtaisiin käyttömenoihin, koska henkilöstö- ja verkkokustannukset eivät skaalaudu lineaarisesti solmumäärän mukaan — keskimmäisen käyttöasteen (60%) kustannus muuttuu seuraavasti:

| Käyttömenoskenaario | Käyttömenot/vuosi | Vuotuinen kokonaiskustannus (pääoma+rahoitus+sähkö+käyttömenot) | **$/miljoona tokenia, KÄYTTÖMENOT MUKANA** |
|---|---|---|---|
| Matala | 10 000 $ | 103 442 $ | **0,070 $** |
| Keski | 25 000 $ | 118 442 $ | **0,080 $** |
| Korkea | 50 000 $ | 143 442 $ | **0,096 $** |

Tämä pysyy **OLETUKSENA**, ei vahvistettuna lukuna — pointtina ei ole, että 0,070–0,096 $/M on "se" oikea Ammattimaisen tason kustannus, vaan että minkä tahansa uskottavan käyttömenovarauksen lisääminen kaventaa näennäistä kuilua Hyperskaalatason kanoniseen 0,133 $/M keskitapaukseen huomattavasti, ja yllä olevia käyttömenottomia lukuja ei koskaan pitäisi siteerata täydellisenä kustannuksena.

### 4.4 Ammattimainen taso — $/tekoäly-työtunti (keskiskenaario, 0,064 $/M tokenia, EI KÄYTTÖMENOJA — ks. soveltamisalan korjaus yllä)

| Käyttöintensiteettivyöhyke | Tokenia/tunti | **$/tekoäly-työtunti** |
|---|---|---|
| Chat/neuvonantaja | 10 000-30 000 | 0,0006–0,0019 $ |
| Aktiivinen tekoälytyötoveri/kopilotti | 60 000-120 000 | 0,0038–0,0076 $ |
| Delegoitu yksittäisagentti | 200 000-600 000 | 0,0127–0,0382 $ |
| Raskas moniagenttiorkestrointi | 1 000 000-12 000 000 | 0,064–0,764 $ |

**Näin tätä luetaan, korjattu 2026-08-13:** ammattimaisen tason käyttömenoton $/M-tokenia-luku on noin 25-70-kertaa matalampi kuin Kotitaloustason luku vastaavalla käyttöasteella — mutta tämä vertailu ei ole tasavertaisella pohjalla, koska Kotitalouden luku sisältää jo täyden (vaikkakin vaatimattoman) kustannusrakenteensa, kun Ammattimainen sulkee käyttömenot kokonaan pois (ks. soveltamisalan korjaus yllä). Myös havainnollistavan käyttömenoherkkyyden lisäämisen jälkeen Ammattimainen jää selvästi Kotitalouden alapuolelle, yhtenevästi GPU-sukupolven tehokkuuden (Blackwell Ultra vs. GB10) ja kiinteän kustannuksen paremman jakautumisen kanssa huomattavasti korkeamman läpimenotehon yli — mutta tarkkaa 25-70-kertaista kerrointa ei pitäisi käsitellä siistinä, vertailukelpoisena tehokkuussuhteena, eikä sitä pidä ylitulkita vahvistamattomien capex-/tehonkulutussyötteiden vuoksi. Se on suuntaa antava, ei vahvistettu markkinahintapiste.

---

## 5. HYPERSKAALA-/TEOLLISUUSTASO — GB300 NVL72 räkkimittakaava

### 5.1 Räkin spesifikaatiot (FAKTA)

| Erä | Arvo | Lähde |
|---|---|---|
| GPU:ta/räkki | 72× Blackwell Ultra | NVIDIA:n virallinen GB300 NVL72 -sivu |
| CPU:ta/räkki | 36× Grace (2 592 Arm Neoverse V2 -ydintä) | NVIDIA:n virallinen sivu |
| GPU-muisti | 20 TB HBM3e, jopa 576 TB/s | NVIDIA:n virallinen sivu |
| NVLink5-kaistanleveys | 130 TB/s | NVIDIA:n virallinen sivu |
| FP4 tiivis | 1 440 PFLOPS (10 800 PFLOPS harvuudella) | NVIDIA:n virallinen sivu |
| Räkin teho (TDP) | 135 kW | **FAKTA**, Lenovo Press LP2357 OEM-viitespesifikaatio (NVIDIA:n oma sivu ei julkaista tehonlukua) |
| Räkin teho (huippu) | jopa 155 kW | Lenovo Press LP2357 |

### 5.2 Vertailuarvon läpimenoteho — kriittinen skaalausvaraus

NVIDIA:n oma MLPerf Inference v6.0 -lähetys raportoi **2 494 310 tokenia/sek** (pyöristettynä "2,5M tok/s":ksi NVIDIA:n omassa kuvatekstissä) DeepSeek-R1:lle — mutta tämä on **aggregaatti neljän toisiinsa kytketyn GB300 NVL72 -räkin yli (288 GPU:ta)**, ei yhden räkin. Jakaen tasan (**LASKELMA**):

```
per_rack_offline_tokps = 2 494 310 / 4 racks = 623 578 tok/s (johdettu, tasajaon oletus)
```

Ristiintarkistus NVIDIA:n suoraan julkaisemia per-GPU-lukuja vasten (**FAKTA**, tarkempi ja väitetysti luotettavampi kuin yllä oleva tasajako-johdannainen):

| Skenaario | Per-GPU tok/s (FAKTA) | ×72 GPU:ta (LASKELMA, räkki yhteensä) |
|---|---|---|
| Offline | 9 821 | 707 112 |
| Server (vuorovaikutteinen) | 8 064 | 580 608 |

Nämä kolme per-räkki-arviota (623 578 / 707 112 / 580 608) rajaavat uskottavan ~580 000-710 000 tok/s per-räkki-vaihteluvälin täsmällisestä skenaariosta ja johtamismenetelmästä riippuen — tämä työkirja käyttää **623 578 tok/s**:ia (tasajako-luku) ensisijaisena työlukunaan jatkuvuuden vuoksi 4-räkin aggregaattivertailun kanssa, ja merkitsee ~14% eron per-GPU-johdettuihin lukuihin nimenomaisesti sen sijaan, että valitsisi jommankumman äänettömästi.

### 5.3 Tokenia/kWh (LASKELMA) — vain sähkökerros

| Perusta | tok/s/kW | Tokenia/kWh |
|---|---|---|
| 623 578 tok/s @ 135kW TDP | 4 619 | 16 628 733 |
| 623 578 tok/s @ 155kW huippu | 4 023 | 14 483 090 |
| 580 608 tok/s (server-skenaario, per-GPU-johdettu) @ 135kW | 4 301 | 15 482 880 |

**Vain sähkön kustannus per miljoona tokenia (LASKELMA)** — tämä on vain pohjakerros, ennen mitään laitteisto-/rahoitus-/käyttömenokerrosta:

| Sähkön hinta | $/M tokenia (16.6M tok/kWh -perustalla) |
|---|---|
| 0,06 $/kWh | 0,0036 $ |
| 0,10 $/kWh | 0,0060 $ |
| 0,25 $/kWh | 0,0150 $ |

**Tämä vahvistaa lähderekisterin löydöksen: raaka sähkö on pyöristysvirhe hyperskaalassa — pieni murto-osa sentistä miljoonaa tokenia kohti tyypillisillä sähkön hinnoilla, ja alle kaksi senttiä vielä esitetyn vaihteluvälin korkeassa päässä (0,015 $, eli 1,5 senttiä, 0,25 $/kWh:lla).** Kaikki merkittävä kustannus tällä tasolla tulee pääomasta, rahoituksesta ja toiminnan yleiskustannuksista, ei tehosta.

### 5.4 Räkin pääomakustannus — kaksi hyvin erilaista vertailukohtaa, pidetty nimenomaisesti erillään

**Vertailukohta A — Huangin/Finkin lähetyksessä esittämästä 50–60 $B/GW-luvusta johdettu implisiittinen kaikki-mukaan-lukien-infrastruktuurikustannus (LÄHDE, CNBC, 10.8.2026):**

```
rack_share_of_1GW = 135kW / 1 000 000kW = 0.000135
implied_allin_cost_per_rack = 50–60 $B × 0.000135 = 6,75 $M-8,1 $M
```

Tämä on täyden infrastruktuurin luku — maa, kuori, sähkönjakelu, jäähdytys ja laskenta yhdessä, Huangin ja Finkin omaa kehystä CNBC-lähetyksessä noudattaen — **ei** vain laitteiston hinta.

**Vertailukohta B — havainnollistava vain-laitteisto-pääomamenot (OLETUS, analyytikon arvioon ankkuroitu, nimenomaisesti EI virallinen NVIDIA-hinta):** 4 000 000 $/räkki. Mitään virallista NVIDIA-räkkihintaa ei löytynyt tässä tarkistuksessa; tämä luku sijoittuu Vertailukohta A:n alapuolelle, koska se sulkee pois maa-/kuori-/sähkönjakeluinfrastruktuurin, yhtenevästi sen kanssa, että A on "täysi rakennushanke" -luku ja B on "vain laskentalaitteisto".

**Rahoitusherkkyys 4 $M vain-laitteisto-skenaariolle (LASKELMA, 8% korko):**

| Aika | Annuiteettimaksu/vuosi | Suoraviivainen poisto/vuosi |
|---|---|---|
| 3 vuotta | 1 552 134 $ | 1 333 333 $ |
| 4 vuotta | 1 207 683 $ | 1 000 000 $ |
| 5 vuotta | 1 001 826 $ | 800 000 $ |
| 7 vuotta | 768 290 $ | 571 429 $ |

### 5.5 Käyttömeno-/yleiskustannuskerros (OLETUS — tila, jäähdytys raaka sähkön ylittävältä osin, henkilöstö, verkko, korvausvaraus)

| Skenaario | $/vuosi per räkki |
|---|---|
| Matala | 200 000 $ |
| Keski | 500 000 $ |
| Korkea | 1 000 000 $ |

### 5.6 Hyperskaalataso — täysi tuotantokustannuskäyrä ($/miljoona tokenia), 5v@8% rahoitus 4 $M laitteistopääomalle, keskikäyttömenot 500 000 $/vuosi, 0,10 $/kWh

| Käyttöaste | Vuotuiset tokenit (LASKELMA) | Raaka sähkö/M tok | Pääoma+rahoitus/M tok | Käyttömenot(keski)/M tok | **YHTEENSÄ $/miljoona tokenia (LASKELMA)** |
|---|---|---|---|---|---|
| Matala 25% | 4.92T | 0,0060 $ | 0,204 $ | 0,102 $ | **0,312 $** |
| Keski 60% | 11.80T | 0,0060 $ | 0,085 $ | 0,042 $ | **0,133 $** |
| Korkea 90% | 17.70T | 0,0060 $ | 0,057 $ | 0,028 $ | **0,091 $** |

### 5.7 Ristiintarkistus NVIDIA:n omaa julkaistua lukua vasten — nyt itsenäisesti vahvistettu, korjauksella sen soveltamisalaan

**Korjaus (2026-08-13):** tämän työkirjan aiempi versio merkitsi "0,123 $/M tokenia" TARKISTAMATTOMAKSI. Se on nyt itsenäisesti vahvistettu suoraan NVIDIA:n omalla sivustolla: NVIDIA toteaa GB300 NVL72:n toimittavan tekoälypäättelyä hintaan **0,123 $ miljoonaa tokenia kohti 116 tokenin/sek/käyttäjä-vuorovaikutteisuudella, käyttäen NVIDIA Dynamoa ja TensorRT-LLM:ää**, lähteenä SemiAnalysisin InferenceX-vertailuarvot huhtikuulta 2026 (**[FAKTA]** — nvidia.com/en-gb/solutions/ai/inference/, tarkistettu 2026-08-13).

**Korjaus, jolla on merkitystä, koskee soveltamisalaa, ei olemassaoloa.** Tämä luku kuvaa **72-GPU:n GB300 NVL72 -räkkimittakaavan järjestelmää**, joka ajaa tiettyä ohjelmistopinoa (Dynamo + TensorRT-LLM) tietyllä vuorovaikutteisuusasetuksella (116 tok/s/käyttäjä) — se on hyperskaala-/teollisuustason luku, ja se kuuluu vain tähän luvun vertailuun, ristiintarkistettuna tämän työkirjan omaa 0,091–0,312 $/M-tokenia hyperskaalavaihteluväliä vasten yllä (samaa suuruusluokkaa, yhtenevästi todellisen, vahvistetun luvun kanssa, joka osuu eri capex-/käyttömeno-oletuksille rakennetun mallinnetun vaihteluvälin sisälle). **Sitä ei koskaan saa käyttää arvioimaan yhden työaseman, DGX Sparkin tai DGX Stationin taloutta** — ne ovat täysin eri laitteistotasoja (ks. luku 2 ja Tokenitehtaan skenaariotyökirjan §1a/1b työasematason ja pöytätason luvuille). 72-GPU:n räkkimittakaavan vertailuarvon käyttäminen yhden koneen osuustoiminnallisen oston hinnoitteluun aliarvioisi kyseisen tason todellisen kustannuksen noin kaksi–kolme suuruusluokkaa, mikä on juuri sitä tasojen välistä sekoittamista, jota tämän paperin ydinmenetelmäsääntö varoittaa (luku 1 yllä).

SemiAnalysisin omalla live-InferenceX-hallintapaneelilla näkyy erikseen laajempi GB300 DeepSeek-R1-kustannusvaihteluväli, karkeasti **0,065–0,076 $/M tokenia** noin 70 tok/s/käyttäjä-vuorovaikutteisuudella aina **2,3–3,3 $/M tokenia**:iin asti noin 219 tok/s/käyttäjällä (korkeampi vuorovaikutteisuus = vähemmän tokeneita eräkäsiteltynä yhdessä = korkeampi kustannus) — nyt vahvistettu 0,123 $/M-tokenia-luku sijoittuu tämän saman vaihteluvälin sisään, tietyssä vuorovaikutteisuuspisteessä (116 tok/s/käyttäjä), joka eroaa vaihteluvälin molemmista päistä, mikä on odotettavaa, kun otetaan huomioon, että "tokenia wattia kohti" ei ole yksi kiinteä luku millekään sirulle (ks. luvun 10 keskustelu samasta vuorovaikutteisuuskompromissista).

### 5.8 Hyperskaalataso — $/tekoäly-työtunti (keskiskenaario, 0,133 $/M tokenia)

| Käyttöintensiteettivyöhyke | Tokenia/tunti | **$/tekoäly-työtunti** |
|---|---|---|
| Chat/neuvonantaja | 10 000-30 000 | 0,0013–0,0040 $ |
| Aktiivinen tekoälytyötoveri/kopilotti | 60 000-120 000 | 0,0081–0,0161 $ |
| Delegoitu yksittäisagentti | 200 000-600 000 | 0,0269–0,0807 $ |
| Raskas moniagenttiorkestrointi | 1 000 000-12 000 000 | 0,133–1,614 $ |

### 5.9 Vera Rubin NVL72 — tulevaisuuteen katsova vertailu (ei tämän työkirjan perustaso; esitetty vain kontekstiksi)

NVIDIA:n omat toimittajaväitteet (**LÄHDE**, markkinointimateriaali) seuraavan sukupolven Vera Rubin NVL72:lle (GB300:n seuraaja) väittävät "jopa 10x enemmän tokeneita per megawatti" ja "yksi kymmenesosa kustannuksesta per miljoona tokenia" verrattuna GB200 NVL72:een. SemiAnalysisin oma itsenäinen, vertailuarvoihin perustuva analyysi on maltillisempi ja työkuormariippuvainen: **~1.5-8x** kustannusetu ja läpimenoteho-per-MW-kuilu, joka alkaa noin 2x matalalla vuorovaikutteisuudella ja saavuttaa **~5.4x** korkealla vuorovaikutteisuudella, riippuen siitä, mitä GB200/GB300-perustason sukupolvea käytetään. Älä käytä toimittajan "10x"/"yksi kymmenesosa" -lukuja vahvistettuna kertoimena missään tulevaisuuteen suuntautuvassa arviossa siteeraamatta rinnalle tätä maltillisempaa itsenäistä vaihteluväliä.

---

## 6. Käyttöintensiteetti → tokenia/tunti-muunnoskaistat (käytössä joka tason $/työtunti-rivillä)

| Käyttötapa | Tokenia/tekoäly-työtunti | Luokka |
|---|---|---|
| Chat/neuvonantaja-tila | 10 000-30 000 | **OLETUS** — havainnollistava kaista, tuettu yleisillä käyttökuvioilla, ei yksittäinen vahvistettu tilasto |
| Aktiivinen tekoälytyötoveri/kopilotti | 60 000-120 000 | **OLETUS** |
| Delegoitu yksittäisagentti | 200 000-600 000 | **OLETUS** |
| Raskas moniagenttiorkestrointi | 1 000 000-12 000 000+ | **OLETUS** |

**Tukeva konteksti (LÄHDE, OpenAI:n oma itse-raportoitu sisäinen telemetria, ei itsenäisesti auditoitu):** OpenAI raportoi, että Codex saavutti 99,8 % sen viikoittaisesta sisäisestä tuotostokenimäärästä vuoden 2026 puoliväliin mennessä; toukokuuhun 2026 mennessä 70,2 % otannassa olleista Codex-käyttäjistä oli tehnyt vähintään yhden pyynnön, joka arvioitiin yli 1 ihmistyötunnin vastaavaksi työksi, ja 25,6 % oli tehnyt vähintään yhden yli 8 ihmistyötunnin pyynnön; kesäkuuhun 2026 mennessä 99. persentiilin raskaat käyttäjät tuottivat säännöllisesti 60+ tuntia Codex-agentin vuoroaikaa päivässä rinnakkaisten agenttien yli. Lähde: OpenAI, "How agents are transforming work" (openai.com/index/how-agents-are-transforming-work/, 25.6.2026), haettu Wayback Machine -arkiston kautta. Itsenäinen lehdistöuutisointi toteaa nimenomaisesti, että "jokainen luku tulee OpenAI:lta itseltään", eikä kolmannen osapuolen auditointia ole — käsittele näitä suuntaa antavana kontekstina sille, miksi raskaan orkestroinnin käyttökaistat voivat olla suuruusluokkia korkeammalla kuin chat-tilan käyttö, ei tarkkojen kaistarajojen kalibrointina.

**Väitettyä NVIDIA:n viitteellistä agenttimaista työkuormalukua "32K syöte + 8K tulostetokenia/vuoro" ei löytynyt missään** laajasta hausta huolimatta (lähderekisteri, klusteri J), eikä sitä pitäisi siteerata NVIDIA-lukuna tässä tai missään muussa julkaisuresurssissa.

---

## 7. Vähittäis-API-hinnoittelu — vain vertailukerros, ei tuotantokustannussyöte

Ei käytettäväksi omistetun laitteiston hinnoitteluun. Esitetty vain "osta verkosta" -vertailukohtana (luvun 1 menetelmäsäännön mukaan). Kaikki vahvistettu **FAKTA**- tai **LÄHDE**-tasoiseksi 2026-08-12 mennessä (ks. täysi lähderekisteri per-mallin luottamushuomautuksille):

| Tarjoaja/taso | Syöte $/M tokenia | Tuloste $/M tokenia | Luokka |
|---|---|---|---|
| Anthropic Claude Sonnet 5 | 2,00 $ | 10,00 $ | **FAKTA** — Anthropicin oma live-hintasivu; tämä on nyt pysyvä vakiohinta, ei vanheneva esittelyhinta |
| Anthropic Claude Opus 5 | 5,00 $ | 25,00 $ | **FAKTA** |
| Anthropic Claude Fable 5 | 10,00 $ | 50,00 $ | **FAKTA** |
| OpenAI GPT-5.6 Luna | 0,20 $ | 1,20 $ | **LÄHDE** — tekoälyn tiivistämän hakutuloksen kautta, ei raakaa ensisijaista tekstiä; käsittele matalamman luottamuksen lukuna |
| OpenAI GPT-5.6 Terra | 2,00 $ | 12,00 $ | **LÄHDE** |
| OpenAI GPT-5.6 Sol | 5,00 $ | 30,00 $ | **LÄHDE** |
| Google Gemini 3.1 Pro (≤200K tokenia) | 2,00 $ | 12,00 $ | **FAKTA** — Googlen oma live-hintasivu; malli on edelleen "Preview"-tilassa, ei GA |

**Tasojen luku vs. vähittäishinta, korjattu 2026-08-13 (tämän kappaleen aiempi versio esitti tukemattoman ja suunnaltaan väärän "14-25 kertaa kalliimpaa" -väitteen — todellinen vertailu on vivahteikkaampi ja riippuu voimakkaasti sekä Kotitaloustason käyttöasteesta että siitä, mitä vähittäistasoa käytetään):** käyttäen samaa 30% syöte / 70% tuloste -sekoitussopimusta, jota käytetään johdonmukaisesti muualla tässä paperissa (ks. Tekoälytyökapasiteetin muuntotyökirja §C.0), yllä olevat vähittäistasot sekoittuvat noin arvoihin 0,90 $/M (Luna), 7,60 $/M (Sonnet 5), 9,00 $/M (Terra/Gemini), 19,00 $/M (Opus 5), 22,50 $/M (Sol) ja 38,00 $/M (Fable 5) **[LASKELMA]**.

Kotitaloustason **parhaan tapauksen** $/M-tokenia-lukua vasten (~1,37 $ 38,4 tok/s:lla, 80% käyttöasteella): Kotitalous on *halvempi* kuin kaikki vähittäistasot paitsi Luna (jossa Luna on sen sijaan noin 1,5 kertaa halvempi kuin Kotitalous). Kotitaloustason **huonoimman tapauksen** $/M-tokenia-lukua vasten (~11,89 $ 10 % käyttöasteella): Kotitalous on nyt kalliimpi kuin Luna, Sonnet 5, Terra ja Gemini, karkeasti verrattavissa Opus 5:een, ja halvempi kuin Sol ja Fable 5 **[LASKELMA]**.

**Rehellinen löydös ei siis ole kiinteä kerroin kumpaankaan suuntaan — se on, että Kotitalousmittakaavan itsehostauksen kustannuskilpailukyky vähittäishintaan verrattuna riippuu täysin siitä, (a) miten tasaisesti omistaja todella käyttää konetta ja (b) mikä vähittäistaso on realistinen vaihtoehto.** Hyvin käytetty Kotitalouslaite voi alittaa useimmat keski-/premium-vähittäistasot; heikosti käytetty voi olla kalliimpi kuin kaikki paitsi kalleimmat vähittäistasot. Tämä on yhtenevä laajemman whitepaperin omistusarkkitehtuuriväitteen kanssa, jonka mukaan itsehostauksen perustelu lepää datan hallinnalla, räätälöinnillä ja riippumattomuudella tarjoajasta — mutta ei ole totta, että itsehostaus olisi kategorisesti kilpailukyvytön raa'assa $/token-kustannuksessa, eikä tämä työkirja enää väitä niin. Hyperskaalan tuotantokustannus (0,091–0,312 $/M tokenia, kanoninen keski 0,133 $/M) pysyy kaukana minkä tahansa tässä esitetyn vähittäis-API-hinnan alapuolella joka käyttöastesenaariossa — yhtenevästi lähderekisterin löydöksen kanssa, jonka mukaan eturintaman laboratorioiden päättelypalvelun katteet ovat, Huangin oman lähetyksessä esittämän kehyksen mukaan, "uskomattoman tuottoisia" (LÄHDE, vahvistamaton mitään laboratorion tosiasiallisesti julkistettuja katteita vasten).

---

## 8. Paikallistamishuomautus

Kaikki yllä olevat luvut käyttävät globaalia USD-perustasoa havainnollistavilla sähkön hintaskenaarioilla. Paikallistaaksesi:

1. Korvaa 0,06 $/0,12 $/0,25 $ (tai 0,10 $ keski, jos käytössä) per-kWh-skenaariot omalla todellisella paikallisella kaupallisella/teollisella tariffillasi — tämä on tavallisesti suurin laillinen maiden välisen vaihtelun lähde.
2. Korvaa rahoituskorko/-aika omilla paikallisesti saatavilla luottoehdoillasi (kuluttajaluotto, pk-yrityslaina tai infrastruktuurihankkeen rahoitus, tasosta riippuen).
3. Muunna USD paikalliseksi valuutaksi ilmoitetulla FX-kurssilla ja päivämäärällä — älä koskaan sekoita valuuttoja äänettömästi.
4. Aja käyttöastesenaariot uudelleen omaa realistista käyttökuviotasi vasten; tässä esitetyt havainnollistavat matala/keski/korkea-kaistat eivät ole kalibroitu millekään tietylle maalle tai organisaatiolle.

---

## 9. Yhteenvetovertailutaulukko — keskiskenaarion $/miljoona tokenia kaikkien neljän tason yli

| Taso | Pääomaperusta | Käyttömenot/yleiskustannukset mukana? | Keski $/M tokenia (LASKELMA) | Luottamus pääoma-/tehosyötteisiin |
|---|---|---|---|---|
| Kotitalous (1× DGX Spark) | 4 699 $, FAKTA-hinta | Kyllä (§2, havainnollistava tuki-/ohjelmistovaraus) | 3,17 $ | Korkea — hinta ja teho FAKTA, läpimenoteho FAKTA-yhteisövertailuarvo |
| Osuustoiminnallinen (50 jäsentä, 10× DGX Spark) | 46 990 $, FAKTA-hinta ×10 | Kyllä (§3.3, OLETUS-hallinto-/verkkokaista) | 3,20 $ | Korkea laitteistolle; hallinto/yleiskustannukset OLETUS |
| Ammattimainen (1× HGX B300 -solmu) | 350 000 $, OLETUS | **Ei — vain pääoma+rahoitus+sähkö (§4.3); havainnollistavan käyttömenoherkkyyden lisäämisen jälkeen §4.3:ssa keskitapaus nousee ~0,080 $/M:ään** | 0,064 $ (ei käyttömenoja) | Matala-keskitasoinen — capex ja teho ovat vahvistamattomia paikkamerkkejä; läpimenoteho on skaalausjohdannainen, ei suora vertailuarvo |
| Hyperskaala (1× GB300 NVL72 -räkki) | 4 000 000 $, OLETUS (vain laitteisto) | Kyllä (§5.5, OLETUS-käyttömenokaista, 200 $k-1M/vuosi) | 0,133 $ | Keskitasoinen — räkin spesifikaatiot ja teho FAKTA; capex on analyytikkoon ankkuroitu OLETUS, ei virallinen hinta |

**TULKINTA, korjattu 2026-08-13:** noin 25-50-kertainen kuilu Kotitalous-/Osuustoiminnallisen ja Ammattimaisen/Hyperskaalatason välillä on suunnaltaan yhtenevä odotettujen mittakaavaetujen kanssa tekoälyinfrastruktuurissa (uudemman sukupolven piirit, kiinteän kustannuksen parempi jakautuminen huomattavasti korkeamman läpimenotehon yli), mutta sitä ei pitäisi lukea tarkkana kertoimena yllä olevien sekoitettujen luottamustasojen vuoksi — Kotitalous-/Osuustoiminnallinen taso lepää FAKTA-hintojen ja FAKTA-yhteisövertailuarvojen varassa, kun taas Ammattimainen taso erityisesti lepää OLETUS-tason capex- ja tehosyötteiden varassa, eikä julkista hintaa tälle tietylle laitteisto-SKU:lle löytynyt. **Ammattimaisen-vs-Hyperskaalan vertailu ei erityisesti ole omenoita-omenoihin**: Ammattimaisen 0,064 $/M sulkee käyttömenot kokonaan pois, kun Hyperskaalan 0,133 $/M sisältää ne, niin osa näennäisestä 2-kertaisesta kuilusta niiden välillä on soveltamisala-artefakti, ei puhdas laitteistosukupolvien vaikutus — ks. §4.3:n havainnollistava käyttömenoherkkyys, joka kaventaa tätä kuilua, kun uskottava (vaikkakin vahvistamaton) käyttömenovaraus lisätään Ammattimaiseen tasoon.
