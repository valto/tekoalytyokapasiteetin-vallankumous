# Tokenitehtaan skenaariotyökirja
**Julkaisuresurssi #10 — "Miksi tekoälyyn investoidaan biljoonia?" (Valto Loikkanen, CC BY 4.0)**
**Tila: koulutuksellinen / ei neuvontaa.** Kaikki alla olevat luvut ovat joko lähdeviitattuja faktoja, lähteeseen kohdistettuja lausuntoja, näistä läpinäkyvästi johdettuja laskelmia tai selkeästi merkittyjä skenaario-oletuksia. Mikään tässä ei ole sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa, eikä yksikään skenaariomalli ole ennuste tai suositus — kaikki syöttöarvot ovat muokattavia, ja tulos on aina yhtä hyvä kuin valitsemasi syöttöarvot.

**Näyttöluokkien lyhenteet** (käytössä läpi tekstin): **[FAKTA]** = Havaittu fakta · **[LÄHDE]** = Lähteeseen kohdistettu lausunto · **[LASKELMA]** = Johdettu laskelma (kaava aina esitetty) · **[OLETUS]** = Skenaario-oletus (muokattava, ei markkinaluku) · **[TULKINTA]** = Tulkinta.

**Valuuttahuomautus:** tämä työkirja käyttää **globaalia USD-perustasoa**, paitsi luvussa 1, jossa täsmäytetään kaksi **EUR-määräistä** lukua kirjoittajan omasta julkaistusta osuustoiminnallisesta mallista — EUR on säilytetty siellä, koska se on täsmäytettävien alkuperäislähteiden valuutta.

---

## 1. KORJATTU: 42 € vs. 19,50–23 € per-jäsen/kk-luvut eivät olleet koskaan vertailukelpoisia — ratkaistu, ei vain täsmäytetty

Tämän työkirjan aiempi luonnos käsitteli lukuja 42 €/jäsen/kk ja 19,50–23 €/jäsen/kk kahtena kilpailevana arviona *samasta* osuustoiminnallisesta skenaariosta, joiden välillä oli selittämätön ~2x kuilu. 2026-08-13 kirjoittaja tarkisti omat alkuperäiset oletuksensa ja selvensi todellisen tilanteen, mikä ratkaisee kuilun sen sijaan, että se vaatisi lisää arvailua:

1. **42 €/jäsen/kk ei ollut koskaan laitteistotarjoukseen perustuva luku.** Se rakennettiin kirjoittajan omalle **havainnollistavalle 100 000 € ALV:ttä-pääomaoletukselle** yhteiskäytössä olevalle työasemaluokan koneelle — nimenomaisesti skenaario-oletus, ei todennettu ostohinta millekään tietylle tuotteelle. Alkuperäinen julkaistu artikkeli ei paljastanut tätä perustaa, minkä takia tämän työkirjan aiempi luonnos virheellisesti käsitteli 42 €:ta läpinäkymättömänä, ei-tarkastettavana "julkaistuna faktana", joka piti käänteismallintaa. Se ei ole läpinäkymätön, kun 100 000 €:n perusta on ilmoitettu; se on normaali **[OLETUS]**-vetoinen skenaariotulos, täysin tarkastettavissa kunhan perusta annetaan (ks. laskettu uudelleenlaskenta alla).
2. **19,50–23 €/jäsen/kk on eri laitteistoluokka, ei kilpaileva arvio samasta.** Tämä luku rakennettiin 10× NVIDIA **DGX Spark** -yksikön varaan vahvistetulla nykyhinnalla 4 699 $ kappale (**[FAKTA]**) — huomattavasti pienempi, halvempi, yhden GPU:n luokan pöytälaite, ei työasemaluokan tai räkkimittakaavan kone. Kaksi lukua kuvasivat eri laitteistoa alusta alkaen.

**Ei siis ole olemassa kuilua täsmäytettäväksi kahden yhden asian mittauksen välillä — on olemassa kaksi eri laitteistotason skenaariota, jotka ovat molemmat sisäisesti johdonmukaisia, mutta jotka virheellisesti esitettiin ikään kuin niiden pitäisi täsmätä.** Alla oleva korjattu käsittely pitää ne selkeästi erillään.

### 1a. DGX Station -luokan skenaario, korjattu (havainnollistava 100 000 € pääomaperusta)

NVIDIA:n nykyinen DGX Station (GB300-pohjainen) on todellinen, nimetty vertailukohta sen *tyyppiselle* koneelle, jota osuuskunta voisi käytännössä jakaa: **748 GB koherenttia muistia ja jopa 20 petaFLOPS:ia FP4-tekoälylaskentaa** (**[FAKTA]** — nvidia.com/en-us/products/workstations/dgx-station/, tarkistettu 2026-08-13), NVIDIA:n asemoimana ajamaan malleja aina 1 biljoonan parametrin kokoon asti ja pitkäkestoisia paikallisia tekoälyagentteja. **NVIDIA ei julkaise vähittäis- tai listahintaa tälle järjestelmälle** (**[FAKTA]** — sama lähde; sivu ohjaa ostajat "ottamaan yhteyttä kumppaniin" ja markkinapaikkalistaukseen hinnan näyttämisen sijaan) — joten mikä tahansa tässä käytetty ostohinta on **tarjoustason havainnollistava oletus**, ei virallinen hinta, eikä sitä saa siteerata sellaisena.

Vain havainnollistamistarkoituksessa oletetaan, että osuuskunta hankkii sopivan järjestelmän **100 000 € excluding VAT:lla** (**[OLETUS]** — nimenomaisesti ei DGX Stationin listahinta, koska sellaista ei ole olemassa), rahoitettuna 5 vuoden ajalle 6,5 %:lla (**[OLETUS]**):

| Kustannuserä | Kaava | Tulos | Luokka |
|---|---|---|---|
| Laitteiston rahoitus | Standardi tasaerälaina 100 000 €:lle, 5v, 6,5 % APR, muunnettuna kuukausiluvuksi | **≈1 957 €/month** | **[LASKELMA]** **[OLETUS]**-pääomaperustalla |
| Sähkö | 1 kW havainnollistava keskimääräinen jatkuva kuormitus × 24h × ~30.4 päivää/kk × 0,15 €/kWh | **≈108 €/month** | **[LASKELMA]** **[OLETUS]**-keskikuormitusluvulla |
| Jäähdytys/tehon yleiskustannus | 25% allowance sähkörivistä | **≈27 €/month** | **[OLETUS]** |
| **Peruslaskentainfrastruktuuri yhteensä** | Yllä olevien kolmen rivin summa | **≈2 092 €/month** | **[LASKELMA]** |

**1 kW:n keskikuormitusoletuksesta:** NVIDIA:n omassa dokumentaatiossa todetaan **kiinteä maksimijärjestelmätehobudjetti 1 600 W (1.6 kW)** DGX Station GB300:lle, jaettuna GB110-laskentamoduulin ja valinnaisen RTX-lisäkortin kesken (**[FAKTA]** — docs.nvidia.com/dgx/dgx-station-development-guide/dynamic-power-sloshing.html, tarkistettu 2026-08-13). Yllä käytetty 1 kW:n luku on siis **havainnollistava keskimääräisen käyttökuorman oletus, selvästi dokumentoidun 1.6 kW:n katon sisäpuolella** — se ei ole mitattu kulutusluku mistään todellisesta käyttöönotosta, ja käyttöastesidonnainen kuormitus voisi todennäköisesti vaihdella missä tahansa kohdassa aina tähän 1.6 kW:n maksimiin asti.

**Jaettuna jäsenten kesken (**[LASKELMA]**, samalla 2 092 €/month-perustalla läpi taulukon):**

| Jäsenet, jotka jakavat tämän yhden koneen | €/member/month |
|---|---|
| 20 | 105 € |
| **50** | **42 €** |
| 100 | **21 €** |

Tämä on täsmällinen laskutoimitus, joka on kirjoittajan alun perin julkaisemien lukujen 42 € (50 jäsentä) ja 21 € (100 jäsentä) taustalla — molemmat nyt esitettyinä **[LASKELMA]**-tuloksina eksplisiittisestä, muokattavasta 2 092 €/month-perustasta, ei tarkastamattomina "julkaistuina faktoina". Tämän työkirjan aiempi luonnos oli väärässä kuvatessaan 42 €-lukua mahdottomana tarkastaa; se on täysin tarkastettavissa, kunhan 100 000 €:n havainnollistava pääomaperusta (jota alkuperäinen artikkeli ei ilmoittanut) paljastetaan.

Tämä laskelma jättää tarkoituksella pois ihmiset, datan tallennuksen, ohjelmistokehityksen, sovellukset, tuen ja mallien koulutuksen — se hinnoittelee vain jaetun laitteiston rahoituksen ja tehon avoimien tekoälymallien ajamiseksi, täsmälleen alkuperäisen rajauksen mukaisesti. Käytännössä yhtä konetta jaettaisiin päättelypalvelun kautta sen sijaan, että jokaiselle jäsenelle varattaisiin erillinen malli tai kone, lisäkoneita rahoitettaisiin kysynnän kasvaessa.

### 1b. DGX Spark -skenaario (muuttumaton, pidetty selkeästi erillään)

**~19,50–23 €/jäsen/kk**-luku pysyy pätevänä **kuvauksena eri, pienemmästä laitteistoluokasta**: 10× NVIDIA DGX Spark -yksikköä vahvistetulla nykyhinnalla 4 699 $ kappale (**[FAKTA]**) — 10 units × 4 699 $ ≈ 46 990 $ pääomaa; 5v@8% rahoitus ≈ 11 770 $/yr; sähkö ≈ 2 000 $–4 000/yr; yhteensä ≈ 14 000 $–15 770/yr **ennen hallintoa/verkkoa**, ÷ 50 jäsentä ÷ 12 kuukautta. Ks. Globaali perustaso -työkirjan (Julkaisuresurssi #7) luku 2 täydelle rakenteelle. Tämä on **[LASKELMA]**, muuttumaton aiempaan luonnokseen verrattuna.

**Yhteenveto, korjattu:** 42 €/jäsen/kk (50 jäsentä, havainnollistava 100 000 € DGX-Station-luokan kone) ja 19,50–23 €/jäsen/kk (50 jäsentä, vahvistetut 4 699 $ DGX Spark -koneet) eivät ole kaksi ristiriitaista arviota yhdestä osuuskunnasta. Ne ovat kaksi sisäisesti johdonmukaista, nimenomaisesti eri laitteistotason skenaariota — yksi suurempi jaettu työasemaluokan järjestelmä versus kymmenen pienemmän pöytäluokan laitteen ryhmä. **Molemmat ovat oikein siitä, mitä ne kuvaavat; kumpaakaan ei pitäisi siteerata "sen" tekoälylaskennan yhteistyön kustannuksena mainitsematta myös, mitä laitteistoluokkaa ja jäsenmäärää se olettaa.** Osuuskunnan todellinen kaikki-mukaan-lukien-kustannus riippuu siitä, minkä laitteistoluokan se valitsee, sen todellisista rahoitusehdoista ja käyttöasteesta, ja — ratkaisevasti — sisältyvätkö ihmiset, tallennus, ohjelmisto, tuki ja mallien koulutus, joita kumpikaan yllä oleva luku ei kata.

---

## 2. Menetelmähuomautus: "miten tätä ei kannata mallintaa" — pidä omistettu tuotanto ja vähittäishinnoittelu erillään

**Tämä on tarkoituksella säilytetty itsekorjaus, ei siloteltu pois.** Aiempi vaihe tämän projektin omassa tutkimusketjussa hinnoitteli virheellisesti itse omistetun laskentatilan käyttäen vähittäistason eturintaman laboratorioiden API-hintoja (OpenAI/Anthropic/Google $/M-token-hintoja) ikään kuin ne olisivat kustannusperusta — eivät ole. Vähittäis-API-hinnat ovat **valmis, katteellinen, patentoitu mallituotteen hinta**; ne sisältävät laboratorion oman katteen, T&K-poistot ja liiketoimintamallivalinnat, eivätkä kerro mitään siitä, mitä avoimen mallin päättelyn ajaminen omistetulla tai vuokratulla laitteistolla maksaa.

Korjattu kehys, käytetty johdonmukaisesti läpi tämän työkirjan:

- **Omistettu tuotantokustannus** = sähkö + laitteisto (poistettu tai rahoitettu) + tila/toiminta, ajaen **avoimen painotuksen malleja** (esim. Qwen, DeepSeek, Kimi) omistetulla tai osuustoiminnallisella laitteistolla. Tämä on "tuota oma sähkösi" -puoli.
- **Vähittäis-API-hinnoittelu** = mitä OpenAI, Anthropic ja Google veloittavat pääsystä omiin patentoituihin malleihinsa. Tämä on "ostaa verkosta" -puoli — **vain vertailukohta**, ei koskaan korvike omistettun tuotantokustannuksen laskelmalle.

Kaksi lukua voivat laillisesti erota 1–2 suuruusluokkaa suuntaan tai toiseen käyttöasteesta, mallivalinnasta ja siitä, mitä "kustannukseen" sisältyy riippuen — se kuilu on juuri se syy pitää ne erillään, ei virhe täsmäytettäväksi pois. Jokainen alla oleva taulukko on merkitty **OMISTETTU TUOTANTO** tai **VÄHITTÄISVERTAILU**, jotta niitä ei koskaan yhdistetä yhdeksi sarakkeeksi.

**Rajahuomautus:** mikään alla olevista luvuista ei ole suositus rakentaa, ostaa tai välttää mitään tiettyä laskentakokoonpanoa — ne ovat muokattavia havainnollistuksia kustannusrakenteen ymmärtämiseksi.

---

## 3. Vaadittu talouden kerrosten erottelu (vain viite — vahvistettu aiemmissa julkaisuresurssityökirjoissa, ei johdettu uudelleen tässä)

| Kerros | Mitä se kattaa | Missä se käsitellään tässä työkirjassa |
|---|---|---|
| Raaka sähkökustannus | $/kWh mittarilla | Luvut 4, 5 |
| Laitteiston poistettu tuotantokustannus | pääomakulut ÷ odotettu käyttöikä, ei rahoitusta | Luku 4 (viite) |
| Rahoitettu omaisuuskustannus | pääomakulut + korko, rahoitusajan mukaan | Luku 4 (rahoitusajan herkkyys) |
| Täysi toimintainfrastruktuurikustannus | + tilan sähkö, jäähdytys, verkko | Luku 4 (viite) |
| Kapasiteetti-/käyttöastekustannus | yllä oleva kustannus ÷ todellinen (ei maksimi) käyttöaste | Luku 4 |
| Tokenin tuotantokustannus | $/M tokens omistetussa laitoksessa | Luku 4 |
| Työkuorman/tekoälytyökapasiteetin kustannus | $/M tokens muunnettuna $/agenttitunniksi | Luku 6 |
| Tulos ja arvo | EI mekaanisesti määräytynyt yllä olevasta | Ei mallinnettu numeerisesti — ks. rajahuomautus, luku 7 |

---

## 4. Omistetun tuotannon kustannustasot (viittaus, ei uudelleenjohdettu aiemmista työkirjaluvuista)

**Rajahuomautus tälle luvulle:** nämä ovat havainnollistavia skenaariorakenteita, ei suositus ostaa mitään tiettyä laitteistoluokkaa, eikä markkinaennuste.

| Taso | Pääoma (OLETUS/FAKTA-sekoitus) | Rahoitus (5v@8%) | Sähkö | Omistettu tuotantokustannus | Näyttöluokka |
|---|---|---|---|---|---|
| Kotitaloustehdas (1× DGX Spark) | 4 699 $ **[FAKTA — nykyinen NVIDIA-hinta, klusteri A]** | ~1 177 $/vuosi | ~25–202 $/vuosi (240W, 0,12 $/kWh OLETUS, 10–80 % käyttöaste) | **1,37–11,89 $/M tokenia** (10–80 % käyttöaste) — kanoninen luku, Globaali perustaso -työkirja §2.4 | LASKELMA (viitattu) |
| Osuustoiminnallinen tehdas (10× DGX Spark, 50 jäsentä) | ~46 990 $ | ~11 294,76 $/vuosi | ~505–2 144 $/vuosi + hallinto | **1,99–7,62 $/M tokenia** (20–85 % käyttöaste) — kanoninen luku, Globaali perustaso -työkirja §3.4 | LASKELMA (viitattu) |
| Teollisuustehdas (GB300 NVL72, 4-räkin/288-GPU:n klusteri) | ~16 M$ **[OLETUS — analyytikkoarvioon perustuva, nimenomaisesti ei virallinen NVIDIA-hinta]** | ks. herkkyystaulukko luvussa 4.1 | ~568kW max, 0,10 $/kWh OLETUS | ~0,091–0,312 $/M tokenia, koko kerros (pääoma + rahoitus + käyttömenot), KANONINEN luku Globaali perustaso -työkirjan §5.6 mukaan | LASKELMA (viitattu) |

Nämä siirtävät aiemman työkirjan luvut muuttumattomina eteenpäin; ks. luku 1 osuustoiminnallisen tason selitykselle. **Tässä paperissa johdonmukaisesti käytetty kanoninen, koko kerroksen Hyperskaala-luku on Globaali perustaso -työkirjan §5.6:n vaihteluväli (0,091–0,312 $/M tokens, mid 0,133 $/M) — tämä luku sisältää pääoman, rahoituksen, sähkön JA käyttömenot/yleiskustannukset. Alla luvussa 4.1 oleva osittaisen kerroksen herkkyystaulukko (pääoma + rahoitus + sähkö vain, ei käyttömenoja) on kapeampi, tarkoituksella epätäydellinen ristiintarkistus nimenomaan rahoitusaika-vivulle; sen matalampia otsikkolukuja (as low as 0,050 $/M) ei saa lukea vaihtoehtoisena tai halvempana "todellisena" Hyperskaalakustannuksena — ne yksinkertaisesti jättävät pois käyttömenokerroksen, joka sisältyy kanoniseen lukuun.**

### 4.1 Rahoitusajan herkkyys — vain teollinen taso, VAIN PÄÄOMA+RAHOITUS+SÄHKÖ (käyttömenot pois luettuna; ei kanoninen koko kerroksen luku)

**Tämän taulukon soveltamisala, nimenomaisesti todettu:** tämä herkkyystaulukko eristää vain *rahoitusaika*-vivun, pitäen pääoman, sähkön ja käyttöasteen kiinteinä samalla, kun lainaaikaa vaihdellaan. Se **jättää tarkoituksella pois käyttömeno-/yleiskustannuskerroksen** (tila, jäähdytys raaka sähkön ylittävältä osin, henkilöstö, verkko, korvausvaraus — ks. Globaali perustaso -työkirja §5.5, 200 000 $–1 000 000 $/räkki/vuosi) jonka yllä oleva kanoninen Hyperskaala-luku sisältää. **Alla olevia 0,050–0,094 $/M-tokenia-lukuja ei pidä siteerata "sen" Hyperskaalakustannuksena — ne ovat vain osittaisen kerroksen havainnollistus rahoitusajan herkkyydestä.**

**Kaava:** Vuotuinen rahoitettu pääomakustannus = Pääoma ÷ AF(n,8%), jossa AF(n,8%) = (1 − 1,08⁻ⁿ) ÷ 0,08. Vuotuinen tilan sähkökustannus = 568kW × 90 % käyttöaste × 8 760 h/vuosi × 0,10 $/kWh **[OLETUS]** ≈ 447 800 $/vuosi. Kustannus per miljoona tokenia = (rahoitettu pääoma + tilan sähkö) ÷ (vuotuiset maksimitokenit × 90 % käyttöaste ÷ 1 000 000), jossa vuotuiset maksimitokenit = 2,5M tok/s × 31 536 000 s/vuosi ≈ 78,84 biljoonaa tok/vuosi **[2,5M tok/s -luku on itsessään HAVAITTU FAKTA 4-räkin/288-GPU:n MLPerf v6.0 -aggregaatille, ei yhdelle räkille — ks. lähderekisteri klusteri A]**.

| Rahoitusaika | Annuiteettikerroin AF(n,8%) | Vuotuinen rahoitettu pääoma (16 M$) | + Tilan sähkö/vuosi | Vuotuinen kokonaiskustannus (vain pääoma+rahoitus+sähkö) | Kustannus per M tokenia (osittainen kerros) |
|---|---|---|---|---|---|
| 3 vuotta | 2,577 | 6 206 900 $ | 447 800 $ | 6 654 700 $ | ~0,094 $/M tokenia |
| 4 vuotta | 3,312 | 4 832 600 $ | 447 800 $ | 5 280 400 $ | ~0,074 $/M tokenia |
| 5 vuotta | 3,993 | 4 007 300 $ | 447 800 $ | 4 455 100 $ | ~0,063 $/M tokenia |
| 7 vuotta | 5,206 | 3 073 000 $ | 447 800 $ | 3 520 800 $ | ~0,050 $/M tokenia |

Ristiintarkistus: 5 vuoden kohdalla pelkkä tasapoisto (16 M$÷5 = 3,2 M$/vuosi) tarkoittaa ~0,045 $/M tokenia; rahoituksen lisämaksu poiston yli on ~0,0114 $/M tokenia — yhtenevä aiemman työkirjan ilmoittaman luvun kanssa. **Pidemmät rahoitusajat mekaanisesti alentavat per-tokenin rahoitettua pääomakustannusta, mutta lisäävät maksettua kokonaiskorkoa ja lukitsevat nykyisen laitteiston pidemmäksi ajaksi nopeasti arvoaan menettävää laiteluokkaa vastaan — tämä taulukko näyttää aritmeettisen kompromissin, se ei suosittele mitään aikaa.** Lisäämällä kanoninen keskimääräinen käyttömenoluku (500 000 $/vuosi, Globaali perustaso -työkirjan §5.5 mukaan) mihin tahansa yllä olevaan riviin ja laskemalla uudelleen palauttaisi sen takaisin kanonisessa taulukossa esitettyyn 0,091–0,312 $/M-vaihteluväliin — nämä eivät ole kaksi eri mittausta Hyperskaalakustannuksesta, ne ovat sama malli esitettynä kahdessa eri täydellisyyskerroksessa.

### 4.2 Vähittäisvertailu (vain vertailukohta — ei koskaan omistettu tuotantokustannus)

| Malli | Syöte $/M tokenia | Tuloste $/M tokenia | Näyttöluokka |
|---|---|---|---|
| Claude Sonnet 5 (Anthropic) | 2,00 $ | 10,00 $ | FAKTA |
| Claude Opus 5 (Anthropic) | 5,00 $ | 25,00 $ | FAKTA |
| Claude Fable 5 (Anthropic) | 10,00 $ | 50,00 $ | FAKTA |
| GPT-5.6 Terra (OpenAI) | 2,00 $ | 12,00 $ | LÄHDE (tekoälyn tiivistämän hakukyselyn kautta, ei raakaa alkuperäistekstiä) |
| GPT-5.6 Sol (OpenAI) | 5,00 $ | 30,00 $ | LÄHDE (sama varaus) |
| Gemini 3.1 Pro Preview (Google), ≤200K tokenia | 2,00 $ | 12,00 $ | FAKTA (edelleen "Preview", ei yleisesti saatavilla) |

**Tämän taulukon oikea lukutapa:** yllä olevat omistetun tuotannon kustannukset vaihtelevat Hyperskaalatason 0,091–0,312 $/M:stä (yksi–kaksi suuruusluokkaa alle näiden vähittäishintojen) aina Kotitaloustason 1,37–11,89 $/M:ään (lähempänä, ja matalalla käyttöasteella jopa halvimman vähittäistason lattian sisällä). Kuilu on todellinen ja suuri Hyperskaalatasolla, mutta kapeampi ja käyttöastesidonnainen Kotitalous-/Osuustoiminnallisella tasolla — se ei ole todiste siitä, että vähittäistason laboratorioiden hinnoittelu olisi epärationaalista, koska vähittäishinnat sisältävät patentoidun mallin T&K:n, turvallisuustyön, katteen ja luotettavuustakuut, joita itseisännöity avoimen painotuksen pino ei sisällä; se on todiste siitä, että "tuota oma sähkösi vs. ostaa verkosta" -kuilun (luku 2) suuruus itsessään riippuu voimakkaasti mittakaavasta ja käyttöasteesta, ei vain itseisännöinnin valinnasta.

---

## 5. Bitcoin-louhinnan bruttoenergiamonetisaation vertailu

**Tämä ei ole nimenomaisesti voittoväite.** Se vertailee vain *bruttotuloa kulutettua sähkömegawattituntia kohti* kahden energiamonetisaatiomekanismin välillä — Bitcoin-louhinta (kitkaton, protokollatason "liitä ja saat maksun" -markkina) ja hypoteettinen tekoäly-tokenien myynti vähittäisvertailuhinnoin (jolla ei ole vastaavaa kitkatonta markkinaa — OpenRouter ja vastaavat reitittimet ovat vain varhainen, osittainen vastine). Kumpikaan puoli ei vähennä pääomakuluja, rahoitusta, jäähdytystä, henkilöstöä tai (tekoälyn osalta) sitä, ostaisiko kukaan oikeasti niin montaa tokenia siihen hintaan.

**Bitcoin-puoli — kaava:** Tulo/MWh = (hashprice $/PH·s⁻¹/päivä ÷ 1000 muuntaakseen $/TH·s⁻¹/päivä) ÷ 24 (→ $/TH·s⁻¹/h) ÷ (tehokkuus J/TH ÷ 1000 → kWh per TH·s⁻¹·h) × 1000 (kWh→MWh), joka yksinkertaistuu muotoon **Tulo/MWh = 1 333 ÷ tehokkuus(J/TH)**, ankkuroituna Luxorin ilmoittamaan spot-hashpriceen **31,73–32,05 $/PH/s/päivä noin 10.–12.8.2026 [FAKTA, klusteri F]**. ASIC-tehokkuuskaistat (25–38 J/TH vanhemmille laitekannoille, alle 14 J/TH tehokkaimmille nykyisille laitekannoille) ovat **[OLETUS]** — havainnollistavia sukupolvikaistoja, ei tässä istunnossa tarkastettua tiettyä spesifikaatiota.

**Tekoäly-token-puoli — kaava:** 240W jatkuvalla kuormituksella ja 50 tok/s:n tulosteella **[OLETUS, DGX Sparkin havaitun teho-/läpäisykykyvaihteluvälin sisällä, klusteri A]**, 1 MWh sähköä ostaa 1 000kWh ÷ 0,24kW = 4 166,7 tuntia käyttöaikaa → 4 166,7 h × 3 600 s/h × 50 tok/s ≈ 750 miljoonaa tuloste-tokenia per MWh. Tulo = 750 × hinta miljoonaa tokenia kohti.

| Skenaario | Perusta | Bruttotulo per MWh | Näyttöluokka |
|---|---|---|---|
| Bitcoin-louhinta — vanhempi kalusto (25–38 J/TH) | 1 333 ÷ 25 – 1 333 ÷ 38 | **~35–53 $** | LASKELMA FAKTA-ankkurilla + OLETUS-tehokkuudella |
| Bitcoin-louhinta — tehokas kalusto (<14 J/TH) | 1 333 ÷ 14 | **~95 $+** (nousee edelleen alle 14 J/TH:n) | LASKELMA FAKTA-ankkurilla + OLETUS-tehokkuudella |
| Tekoälytokenit myyty 1 $/M | 750M tokenia × 1 $/M | **750 $** | LASKELMA OLETUS-laitteisto-/hintasyötteillä |
| Tekoälytokenit myyty 5 $/M | 750M tokenia × 5 $/M | **3 750 $** | LASKELMA |
| Tekoälytokenit myyty 10 $/M | 750M tokenia × 10 $/M | **7 500 $** | LASKELMA |
| Tekoälytokenit myyty 25 $/M | 750M tokenia × 25 $/M | **18 750 $** | LASKELMA |

**Miksi tekoäly-tokenien luvut näyttävät niin paljon suuremmilta:** ne olettavat, että joka tuotettu token myydään *vähittäis*-eturintaman mallin hintaan (luku 4.2), joka on "ostaa verkosta" -hinta, ei kustannus. **Korjattu 2026-08-13:** aiempi versio tästä kappaleesta arvotti samat 750M tokenia sittemmin korvattuun, matalampaan Kotitaloustason kustannuslukuun (~0,6–2 $/M) ja sisälsi lisäksi 1 000-kertaisen yksikkövirheen, aliarvioiden syntynyttä tulo-per-MWh:ta noin tuhatkertaisesti (se ilmoitti 0,45–1,50 $/MWh; oikea aritmetiikka jopa tällä vanhalla, matalammalla kustannusluvulla olisi ollut 450–1 500 $/MWh). Käyttäen tämän paperin kanonista Kotitaloustason lukua (1,37–11,89 $/M tokenia, luku 4), samat 750M tokenia, arvotettuna omistetulla tuotantokustannuksella, ovat arvoltaan **1 028–8 918 $ per MWh-ekvivalentti** — *yli* jopa tehokkaan Bitcoin-kaluston, ei sen alapuolella. Vain kanonisen Hyperskaalatason 0,091–0,312 $/M:llä tuotantokustannusarvo laskee **68–234 $:aan per MWh-ekvivalentti**, joka sijoittuu tehokkaan kaluston Bitcoin-vaihteluvälin sisään (~95 $+/MWh) sen selkeästi alapuolelle jäämisen sijaan. **Koko vertailu on herkkä sille, mikä hintapiste ja mikä tuotantotaso syötetään, minkä juuri takia tämä on skenaariotaulukko muokattavilla syötteillä, ei kummankaan toiminnan kannattavuusväite, ja sitä ei saa lukea sellaisena.**

---

## 6. Tokenkustannuksen yhdistäminen työkapasiteettikustannukseen (viite, lyhyt)

$/M tokenia -yhdistämiseksi $/tekoäly-työtunti-yksikköön ("työkuorman/tekoälytyökapasiteetin kustannus" -kerros) sovelletaan havainnollistavia käyttöintensiteettivyöhykkeitä **[OLETUS, tuettuna OpenAI:n itse-raportoimalla Codex-telemetrialla — LÄHDE, klusteri J, ei itsenäisesti auditoitu]**:

| Käyttötapa | Tokenia/tunti (havainnollinen) | Vähittäis-Sonnet 5 -hinnoittelulla (~6 $/M sekoitettuna) | Omistetulla tuotantokustannuksella (~1 $/M sekoitettuna) |
|---|---|---|---|
| Chat/neuvonantaja | 10 000–30 000 | 0,06–0,18 $/h | 0,01–0,03 $/h |
| Aktiivinen kopilotti | 60 000–120 000 | 0,36–0,72 $/h | 0,06–0,12 $/h |
| Delegoitu yksittäinen agentti | 200 000–600 000 | 1,20–3,60 $/h | 0,20–0,60 $/h |
| Raskas moniagenttiorkestrointi | 1 000 000–12 000 000+ | 6–72 $+/h | 1–12 $+/h |

**Kaava:** $/tunti = (tokenia/tunti ÷ 1 000 000) × $/M-token-hinta. **Tulkitseva huomautus [TULKINTA]:** tämä osoittaa, miksi raskas orkestrointi voi tehdä tekoälytyökapasiteetista halpaa $/tunti-mielessä jopa vähittäishinnoilla — mutta kapasiteettitunnin kustannus ei kerro mitään sen *arvosta*, mitä tuo kapasiteetti tuottaa. Halpa, nopea, väärä vastaus laajennettuna moniagenttitiimin yli on edelleen halpa ja väärä laajassa mittakaavassa.

---

## 7. Pysyvä rajahuomautus (toistettu tarkoituksella, ei todettu vain kerran)

Jokainen tämän työkirjan taulukko on skenaario rakennettuna näkyville, muokattaville oletuksille — käyttöasteille, sähköhinnoille, rahoitusehdoille, ASIC-tehokkuuskaistoille ja vähittäishintapisteille voidaan kaikki muuttaa, ja niin tehdessä muuttuu joka alavirran luku. Mikään tässä työkirjassa ei ole sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa, eikä yksikään tässä oleva luku pitäisi lukea ennusteena siitä, mitä mikä tahansa tietty laitos, osuuskunta tai louhinta-/päättelytoiminta oikeasti ansaitsee tai maksaa. Analyyttisen ketjun viimeinen vaihe — tulos ja arvo — **ei ole mekaanisesti määräytynyt** mistään yllä olevista kustannus- tai tuloluvuista; tämä vaihe riippuu ihmisen harkinnasta, ohjauksesta ja kontekstista, jota tämä työkirja ei mallinna eikä voi mallintaa.
