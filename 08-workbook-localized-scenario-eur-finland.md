# Paikallistettu skenaariotyökirja — EUR / Suomi -malli
### Julkaisuresurssi #8, kumppani *"Miksi tekoälyyn investoidaan biljoonia?"* -teokselle (Valto Loikkanen, CC BY 4.0)

---

## 0. Mikä tämä asiakirja on — ja mikä se ei ole

Tämä työkirja ottaa muualla tässä tutkimuspaketissa käytetyn globaalin USD-perustason kustannusmallirakenteen ja työstää sen **kertaalleen, kokonaan, EUR:ssa, käyttäen Suomea havainnollistavana maana**.

**Se on:**
- **Yksi laskettu malli monien mahdollisten paikallistusten joukossa.** Kuka tahansa lukija missä tahansa maassa voi kopioida menetelmän ja korvata omalla sähköhinnallaan, rahoitusehdoillaan, valuutallaan ja laitteistohankintatodellisuudellaan.
- Osoitus siitä, miten herkkä "tekoälytehtaan" talous on *paikallisille* syötteille, joita globaalit USD-otsikkoluvut eivät koskaan näytä.

**Se ei ole:**
- Väite siitä, että Suomen todellinen nykyinen sähköhinta, lainakorko tai laitteiston jälleenmyyntihinta olisi itsenäisesti vahvistettu elävää suomalaista ensisijaista lähdettä vasten. **Sitä ei ole tehty.** Tämän projektin taustalla oleva vahvistettu lähderekisteri kattaa globaaleja tekoälyteollisuuden faktoja (siruspesifikaatiot, mallien hinnoittelu, yritysilmoitukset) — se **ei sisällä vahvistettuja Suomen energiamarkkina- tai Suomen luottomarkkinalukuja**. Jokainen Suomi-kohtainen luku alla on siksi nimenomaisesti merkitty **SKENAARIO-OLETUS**-luvuksi, ei markkinafaktaksi, ja se on suunniteltu ylikirjoitettavaksi lukijan itse tarkistamalla luvulla.
- Sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa. Jokainen tämän työkirjan skenaariotaulukko on muokattava havainnollistus ilmoitetuille oletuksille rakennettuna, ei ennuste tai suositus.

### Näyttöluokkien selitteet (käytössä läpi tekstin)

| Koodi | Merkitys |
|---|---|
| **HAVAITTU FAKTA** | Tarkistettu elävää/ensisijaista lähdettä vasten 2026-08-12 tai välittömästi sitä ennen (projektin lähderekisterin mukaan). |
| **LÄHTEESEEN KOHDISTETTU LAUSUNTO** | Nimetty henkilö/organisaatio sanoi tämän; ei itsenäisesti todistettu markkinafaktaksi. |
| **JOHDETTU LASKELMA** | Läpinäkyvä aritmetiikka siteeratuista syötteistä — kaava aina esitetty. |
| **SKENAARIO-OLETUS** | Näkyvä, muokattava parametri, nimenomaisesti ei vahvistettu markkinaluku. |
| **TULKINTA** | Merkitty selitys siitä, miten faktat/lausunnot/oletukset voivat liittyä toisiinsa — ei koskaan fakta. |

---

## 1. Neljä asiaa, jotka jokaisen paikallistuksen täytyy vaihtaa

| Parametri | Globaali USD-perustaso (havainnollistava) | Tämän työkirjan Suomi/EUR-arvo | Luokka | Mitä se hallitsee |
|---|---|---|---|---|
| Valuutta | USD | EUR | SKENAARIO-OLETUS | Jokaisen kustannusluvun valuutta |
| FX-kurssi USD→EUR | n/a | **1 USD = 0,93 €** (eli 1 EUR ≈ 1,075 $) | SKENAARIO-OLETUS — **ei tarkistettu elävä kurssi**; lähderekisteri ei sisällä vahvistettua nykyistä FX-noteerausta | Muuntaa jokaisen USD:ssä noteeratun laitteisto-/API-hinnan |
| Sähkön hinta (kotitalous/prosumer-taso) | 0,20 $/kWh (havainnollinen) | **0,15 €/kWh** | SKENAARIO-OLETUS — havainnollistava paikkamerkki, ei vahvistettu nykyinen suomalainen vähittäishinta | Sähkörivi joka per-token- ja per-tunti-kustannuksessa |
| Sähkön hinta (teollisuustaso) | 0,10 $/kWh (havainnollinen) | **0,09 €/kWh** | SKENAARIO-OLETUS | Teollisen mittakaavan tokenin tuotantokustannus |
| Rahoituskorko & aika | 8 % vuosikorko, 5 vuoden poisto | **8 % vuosikorko, 5 vuoden poisto (muuttumaton)** | SKENAARIO-OLETUS — pidetty identtisenä USD-perustason kanssa vertailukelpoisuuden vuoksi; **ei vahvistettu suomalainen kuluttaja-/yrityslainakorko**. Suomessa yrityslainat noteerataan tyypillisesti Euribor-viitekorkona plus pankin marginaalina, ei kiinteänä vuosikorkona — ks. §2, miten tämä korvataan oikein. | Vuotuinen pääomakustannus joka laitteisto-/robottiskenaariolle |
| Laitteiston hintaperusta | Yhdysvaltain suora/suositushinta | **Yhdysvaltain suositushinta muunnettuna yllä olevalla FX-oletuksella, EI vahvistettu EU-jälleenmyyjän hinta** | Ks. §3 — nimenomainen ei-kanoninen merkintä | Pääomakustannussyöte joka malliin |

---

## 2. Lukijan korvausopas — tee tämä omalle maallesi

1. **Valitse valuuttasi ja hanki elävä FX-kurssi** lähteestä, jota luotat sinä hetkenä, kun rakennat omaa versiotasi. Korvaa yllä oleva 0,93 €/1 $-paikkamerkki. Joka dollariluku tässä työkirjassa kerrotaan tällä yhdellä luvulla — mitään muuta ei tarvitse muuttaa rakenteellisesti.
2. **Hanki oma sähkön hintasi**, omassa valuutassasi per kWh, todellisesta laskusta tai kansallisesta/alueellisesta vähittäistariffin sääntelyviranomaisesta, *ei* tästä asiakirjasta. Huomaa, onko kyseessä kotitalous-, kommersiaali- vai teollisuustariffi — ne eroavat tyypillisesti 2–5x, ja tämä työkirja pitää tämän erottelun (§1:n kaksi erillistä riviä) tarkoituksella.
3. **Hanki omat rahoitusehtosi.** Jos olet euroalueella, realistinen malli on: *(nykyinen Euribor-viitekorko, esim. 3- or 12-month) + (pankkisi marginaali, tyypillisesti 1–4 prosenttiyksikköä riippuen vakuudesta/luottokelpoisuudesta)*. Tämä työkirja käyttää kiinteää 8%:a vain, koska sitä (myös havainnollistava) globaali USD-perustaso käytti — korvaa se sillä korolla, jonka voit todella saada tarjottuna, ja laske sama poistokaava uudelleen §5–§7:ssä esitetyllä tavalla.
4. **Tarkista laitteistohinta paikallisesti, ei tästä asiakirjasta.** Ks. §3 välittömästi alla — tämä on yleisin tapa, jolla paikallistus menee pieleen.
5. Laske kaavat uudelleen (esitetty selkeästi, ei vain tuloksina, joka taulukossa alla) neljällä korvaamallasi luvulla. *Rakenne* — kiinteä pääoma-/rahoituskustannus vs. muuttuva sähkökustannus vs. tokenin tuotos — ei muutu; vain neljä syötettä muuttuvat.

---

## 3. Laitteistohinnan paikallistuksen varoitus (DGX Spark -tapaustutkimus) — lue tämä ennen minkään alla olevan hinnan käyttämistä

**HAVAITTU FAKTA:** NVIDIA:n virallinen DGX Spark Founders Edition -suositushinta, myyty suoraan Yhdysvalloissa, on **4 699 $** 2026-08-12 mennessä (nostettu 3 999 $:sta NVIDIA:n itse ilmoittamassa hinnanmuutoksessa 2026-02-25, viitaten muistin saatavuusrajoituksiin). Lähde: NVIDIA Developer Forumsin virallinen hinnanmuutosilmoitus, forums.developer.nvidia.com, tarkistettu 2026-08-12.

**Mitä tämä työkirja EI väitä:** mitään tietyä EU- tai Suomen jälleenmyyjähintaa DGX Sparkille. NVIDIA:n oma tuotesivu ei näytä hintaa ollenkaan, ja se ohjaa kolmannen osapuolen "Ostaa nyt" -markkinapaikkalinkkeihin; mitään EU-/Suomi-jälleenmyyjälistausta ei tarkistettu tai vahvistettu tämän projektin taustalla olevassa lähderekisterissä.

**Nimenomainen ei-kanoninen merkintä, tämän aineiston tehtävänvaatimuksen mukaisesti:** *Yhdysvaltain ulkopuolinen laitteistohinnoittelu tuotteille kuten DGX Spark on jälleenmyyjäriippuvaista — muotoutunutta tuontitullin, ALV:n, logistiikan, paikallisen kysynnän ja yksittäisen jälleenmyyjän katteen mukaan — eikä sitä koskaan pidä käsitellä universaalina faktana, joka vastaisi valmistajan kotimarkkinan suositushintaa.* Jos rakennat omaa versiotasi tästä työkirjasta, hanki todellinen tarjous todelliselta EU-jälleenmyyjältä sinä hetkenä, kun rakennat sitä, ja odota sen olevan korkeampi kuin alla näytetty valuuttakurssimuunnettu Yhdysvaltain suositushinta, ei sama kuin se.

| Vertailukohta | Arvo | Luokka |
|---|---|---|
| Yhdysvaltain suora suositushinta | 4 699 $ | HAVAITTU FAKTA |
| FX-muunnettu "lattiaviite" (EI todellinen EU-tarjous) | 4 699 $ × 0,93 = **4 370 €** | JOHDETTU LASKELMA (vain mekaaninen FX-muunnos) |
| Paikallinen ALV | *[tyhjä — lisää omasi maasi verokanta; ei vahvistettu tässä työkirjassa]* | lukijan täytettävä |
| Tuonti-/logistiikka-/jälleenmyyjämarginaali | *[tyhjä — lisää omasi paikallinen jälleenmyyjätarjous]* | lukijan täytettävä |
| **Realistinen EU-toimitushinta** | **todennäköisesti korkeampi kuin 4 370 € — hanki todellinen tarjous** | ei mallinnettu tässä |

Alla olevissa lasketuissa esimerkeissä käytämme **4 370 €:n FX-lattialukua** yksinomaan sen takia, että aritmetiikka on jäljitettävissä takaisin HAVAITTU FAKTA -lukuun Yhdysvaltain suositushinnasta. Kenen tahansa tätä lukevan pitäisi olettaa, että hänen todellinen ostohintansa Suomessa (tai muualla EU:ssa) on korkeampi, ja hänen pitäisi laskea §5:n kaavat uudelleen omalla todellisella tarjouksellaan.

---

## 4. Rahoituskäytäntöhuomautus

Tämä työkirja käyttää kahta eri (molemmat pätevää) poistokäytäntöä, ja se sanoo sen nimenomaisesti eron piilottamisen sijaan:

- **Vuosierän käytäntö** (§5, §6 — DGX Spark -tasot): `Vuosimaksu = P × r / (1 − (1+r)^-n)`, jossa r = 8 %/vuosi, n = 5 vuotta. Yksinkertaisempi silmämääräiselle vuotuiselle kokonaiskustannukselle.
- **Kuukausierän käytäntö** (§7 — humanoidirobottitaso, vastaten tyypillistä kuluttaja-/yrityslainarakennetta): `Kuukausimaksu = P × r_kk / (1 − (1+r_kk)^-n_kk)`, jossa r_kk = 8 %/12 kuukausikorko, n_kk = 60 kuukautta; vuositasoistettu ×12.

Kaksi käytäntöä tuottavat hieman erilaiset kokonaissummat samalle pääomalle ja korolle (kuukausikorko on tässä esitystavassa marginaalisesti kalliimpi maksetussa kokonaiskorossa vuodessa). Jos oma lainasi on noteerattu jommallakummalla tavalla, käytä sitä kaavaa — älä sekoita niitä yhden vertailun sisällä.

---

## 5. Laskettu malli A — Kotitalouden tekoälytehdas (yksi DGX Spark), EUR

Syötteet: Pääoma 4 370 € (§3:n lattiaviite — ei todellinen EU-tarjous) · rahoitus 8 %/5v, vuosierän käytäntö · tehonkulutus 240W jatkuva maksimi (HAVAITTU FAKTA -spesifikaatio, NVIDIA:n tuotesivu) · sähkö 0,15 €/kWh (SKENAARIO-OLETUS) · läpimenotehovaihteluväli **korjattu 2026-08-13**: 30,8–38,4 tok/s suoraan vahvistettu taustalla olevassa yhteisön foorumiketjussa (Qwen3.5-122B-A10B DGX Sparkilla), erillisen, vahvistamattoman "51 tok/s+" -otsikkoväitteen kanssa saman kirjoittajan toimesta, ei itsenäisesti uudelleenvahvistettu — **tämän osion aiempi versio käytti 83 tok/s -lukua, joka ei jäljity mihinkään tämän projektin rekisterin lähteeseen, ja se on poistettu.** Molemmat, vahvistettu 30,8–38,4 tok/s -vaihteluväli ja vahvistamaton 51 tok/s -katto, esitetään alla, selkeästi luottamuksen mukaan merkittyinä, sen sijaan, että ne yhdistettäisiin yhdeksi merkitsemättömäksi vaihteluväliksi.

**Rahoitus:** `A = 4 370 × 0,08 / (1 − 1,08⁻⁵) = 1 095 €/vuosi`
**Sähkö 100 %:n käyttöasteella:** `240W × 8 760h/vuosi × 0,15 €/kWh = 2 102,4 kWh × 0,15 € = 315 €/vuosi`

| Käyttöaste | Tokenia/vuosi @ 38,4 tok/s (vahvistettu) | Tokenia/vuosi @ 51 tok/s (vahvistamaton) | Kustannus/vuosi yhteensä (rahoitus + sähkö) | Kustannus/M tokenia @ 38,4 tok/s | Kustannus/M tokenia @ 51 tok/s |
|---|---|---|---|---|---|
| 100 % | 1 211,0M | 1 608,3M | 1 410 € | 1,16 € | 0,88 € |
| 75 % | 908,3M | 1 206,2M | 1 331 € | 1,47 € | 1,10 € |
| 50 % | 605,5M | 804,2M | 1 253 € | 2,07 € | 1,56 € |
| 25 % | 302,8M | 402,1M | 1 174 € | 3,88 € | 2,92 € |

Kaava joka solulle: `Tokenia/vuosi = tok/s × 86 400s × 365 × käyttöaste`; `Kustannus/M tokenia = (1 095 € + 315 €×käyttöaste) / (Tokenia/vuosi ÷ 1 000 000)`. **51 tok/s -sarake pitäisi käsitellä optimistisena, vahvistamattomana skenaariokattona — 38,4 tok/s -sarake on vahvistettu luku, jota kannattaa luottaa mihin tahansa todelliseen suunnittelukäyttöön.**

**Rajahuomautus:** tämä on skenaariohavainnollistus yhden koneen poistetusta + sähkökustannuksesta per token, oletetulla paikallisella sähkönhinnalla ja oletetulla laitteiston toimitushinnalla. Se jättää pois huollon, ohjelmiston, verkon, valvontaajan ja mahdollisen todellisen EU-jälleenmyyjän katteen (ks. §3). Se ei ole ennuste siitä, mitä kotitalouden tekoälytehtaan ajaminen oikeasti maksaa sinulle, eikä se ole sijoitus- tai hankintaneuvontaa.

---

## 6. Laskettu malli B — Osuustoiminnallinen tekoälytehdas (50 jäsentä, 10 DGX Sparkia), EUR

Syötteet: Pääoma 10 × 4 370 € = **43 700 €** (§3:n lattiaviite) · rahoitus 8 %/5v vuosierän käytäntö · sähkö 0,15 €/kWh · aggregaattiläpimenoteho 500–827 tok/s (10 × yhden yksikön vaihteluväli).

**Rahoitus:** `A = 43 700 × 0,08 / (1 − 1,08⁻⁵) = 10 946 €/vuosi`
**Sähkö 100 %:n käyttöasteella:** `10 × 2 102,4 kWh × 0,15 € = 3 154 €/vuosi`

**70 %:n käyttöasteella** (uskottava vakiotila-oletus, ei vahvistettu luku):
Sähkö = 3 154 € × 0,70 = 2 208 €/vuosi → **Yhteensä = 10 946 € + 2 208 € = 13 154 €/vuosi**

| Aggregaatti tok/s | Tokenia/vuosi @ 70 % käyttöaste | Kustannus/M tokenia |
|---|---|---|
| 500 | 500 × 31 536 000 × 0,70 = 11 037,6M | 13 154 € ÷ 11 037,6 = **1,19 €/M** |
| 827 | 827 × 31 536 000 × 0,70 = 18 266,2M | 13 154 € ÷ 18 266,2 = **0,72 €/M** |

**Jäsenkohtainen kustannus:** `13 154 €/vuosi ÷ 12 kuukautta ÷ 50 jäsentä = 21,92 €/jäsen/kk`.

### KORJATTU: 42 €/jäsen/kk vs. ~22 €/jäsen/kk eivät koskaan olleet kilpailevia arvioita samasta asiasta

Tämän osan aiempi versio käsitteli lukuja 42 €/jäsen/kk ja tämän työkirjan ≈22 €/jäsen/kk:n DGX Spark -rakennelmaa kahtena ristiriitaisena mittauksena, jotka tarvitsevat täsmäytystä. 2026-08-13 kirjoittaja selvensi 42 €-luvun todellisen alkuperän, mikä ratkaisee tämän sen sijaan, että se jätettäisiin avoimeksi:

**42 €/jäsen/kk rakennettiin havainnollistavalle 100 000 €:n ALV:ttömälle pääomaoletukselle yhteiskäytössä olevalle työasemaluokan koneelle (esim. NVIDIA DGX Station -tyyppinen järjestelmä) — ei koskaan DGX Spark -hinnoittelulle, eikä koskaan millekään vahvistetulle vähittäishinnalle, koska NVIDIA ei julkaise sellaista tälle koneluokalle** (**[FAKTA]** — nvidia.com/en-us/products/workstations/dgx-station/, tarkistettu 2026-08-13: DGX Station -tuotesivulla ei ole listattua hintaa, ja se ohjaa ostajat kumppanille/markkinapaikalle). Kun 50 jäsentä jakaa 2 092 €/kk:n kokonaiskustannusperustan (1 957 €/kk rahoitus 100 000 €:lle 6,5 %/5v, plus 108 €/kk sähköä havainnollistavalla 1kW:n keskikuormituksella, plus 27 €/kk jäähdytys-/tehon yleiskustannus), 42 €/jäsen/kk on yksinkertaista, täysin tarkastettavaa aritmetiikkaa — ks. Tokenitehtaan skenaariotyökirja (Julkaisuresurssi #10), §1a, täydelle lasketulle uudelleenlaskennalle.

**Tämän työkirjan ≈22 €/jäsen/kk-luku kuvaa eri, halvempaa laitteistoluokkaa** — 10× NVIDIA DGX Spark -yksikköä hintaan 4 699 $ kappale, ei 100 000 €:n työasemaluokan järjestelmää. Kaksi lukua eivät koskaan tarkoittaneet lähentyä, koska ne hinnoittelevat eri laitteistoa. Ei jää jäljelle kuilua selitettäväksi: **molemmat ovat oikein sille tietylle koneelle ja jäsenmäärälle, jotka kukin olettaa.**

**Rajahuomautus:** toistettu vaatimuksen mukaisesti — molemmat yllä olevat osuustoiminnalliset mallit ovat muokattavia skenaariohavainnollistuksia, ei ennusteita todellisista osuuskunnan käyttökustannuksista, eikä taloudellista tai hankintaneuvontaa. Lukijan, joka arvioi todellista osuuskuntaa, täytyy ensin päättää, mikä laitteistoluokka (DGX Spark -luokan pöytälaitteet vs. DGX Station -luokan jaettu työasema) sopii hänen todelliseen käyttötapaukseensa, ennen kuin kumpikaan luku muuttuu merkitykselliseksi.

---

## 7. Laskettu malli C — Humanoidirobotin työkapasiteetti, EUR

### 7a. Havainnollistava perustapaus (jo EUR-alkuperäinen — ja nimenomaisesti skenaario, ei todellinen tuotehinta)

**SKENAARIO-OLETUS, todettu selkeästi:** alla käytetty 25 000 €:n robotin hinta on havainnollistava esimerkki, ei vahvistettu markkinahinta millekään tietylle todelliselle tuotteelle (lähderekisterin klusteri G mukaan). Käsiraha 20 % (5 000 €); 20 000 € rahoitettu 5v @ 8 %, kuukausierän käytäntö.

**Rahoitus (kuukausierän käytäntö):** `Kuukausimaksu = 20 000 × 0,006667 / (1 − 1,006667⁻⁶⁰) = 405,5 €/kk → 4 866 €/vuosi`
Käsiraha jaettu 5 vuodelle: 5 000 € ÷ 5 = 1 000 €/vuosi
**Pääoma + rahoituskustannus yhteensä = 4 866 € + 1 000 € = 5 866 €/vuosi**
Sähkö: 0,10 €/käyttötunti (SKENAARIO-OLETUS, sisältää ilmoittamattoman tehonkulutusluvun — ei erikseen vahvistettu)
Huoltovaraus: 2 500 €/vuosi (10 % ostohinnasta, SKENAARIO-OLETUS)

| Vuotuiset tuottavat tunnit | Kustannus/h (rahoitus + sähkö vain) | Kustannus/h (sis. huollon) |
|---|---|---|
| 2 000 | 5 866 €/2 000 + 0,10 € = **3,03 €** | + 2 500 €/2 000 = **4,28 €** |
| 4 000 | 5 866 €/4 000 + 0,10 € = **1,57 €** | + 2 500 €/4 000 = **2,19 €** |
| 6 000 | 5 866 €/6 000 + 0,10 € = **1,08 €** | + 2 500 €/6 000 = **1,49 €** |
| 8 000 | 5 866 €/8 000 + 0,10 € = **0,83 €** | + 2 500 €/8 000 = **1,15 €** |

Kaava: `Kustannus/h = (vuotuinen rahoitus+käsirahakustannus ÷ vuotuiset tunnit) + sähkö/h [+ ylläpito/vuotuiset tunnit]`.

### 7b. Todellisen markkinahinnan ristiintarkistus (muunnettu EUR:iin §1:n FX-oletuksella)

| Alusta | USD-hinta | Luokka | EUR-vastine (× 0,93) |
|---|---|---|---|
| Unitree G1 (aloitustaso) | 13 500 $ | **HAVAITTU FAKTA** (Unitreen virallinen sivu) | 12 555 € |
| 1X NEO (varhaispääsy) | 20 000 $ (tai 499 $/kk tilaus) | LÄHTEESEEN KOHDISTETTU LAUSUNTO (Engadget, useiden muiden julkaisujen vahvistamana; ei vahvistettu 1X:n omalla hinnoittelusivulla haetussa sisällössä) | 18 600 € |
| Tesla Optimus (pitkän aikavälin tavoite, ei vielä kommersiaalista hintaa) | 20 000 $–30 000 $ | LÄHTEESEEN KOHDISTETTU LAUSUNTO (toistettu Muskin tavoite; Tesla ei ole avannut tilauksia 2026-08-12 mennessä) | 18 600 €–27 900 € |
| Figure 03 (huhuiltu tavoite, epävirallinen) | ~20 000 $ | LÄHTEESEEN KOHDISTETTU LAUSUNTO (vain kolmannen osapuolen kokoajat; Figure AI ei julkaise hintaa) | 18 600 € |
| Agility Digit (suora ostohinta) | ~250 000 $ | LÄHTEESEEN KOHDISTETTU LAUSUNTO (konvergentit toissijaiset lähteet; ei löydetty ensisijaista Agilityn hintalistaa) | 232 500 € |

**TULKINTA:** §7a:ssa käytetty 25 000 €:n havainnollistava luku sijoittuu todellisen havaitun/tavoitellun markkinavaihteluvälin *sisään*, mutta sen alempaan keskiosaan EUR:iin muunnettuna — lähelle Unitree G1:n todellista hintaa, selvästi Agility Digitin yritystason hinnan alapuolelle, ja samaan kaistaan Teslan/Figuren vahvistamattomien kuluttajatavoitteiden kanssa. Tämä ei tarkoita, että 25 000 € olisi "oikea" robotin hinta; se tarkoittaa, että havainnollistus ei ole villisti epärealistinen paikkamerkkinä.

### 7c. Uudelleenlaskenta käyttäen todellista havaittua hintaa (Unitree G1, 12 555 €) havainnollistavan 25 000 €:n sijaan

Käsiraha 20% = 2 511 €; rahoitettu 10 044 €, 5yr @ 8% kuukausierän käytäntö.
**Rahoitus:** `10 044 × 0.020275/month = 203,7 €/month → 2 444 €/yr`; käsirahan jako = 2 511 €/5 = 502 €/yr → **Yhteensä = 2 946 €/yr**
Huoltovaraus (10%): 1 255 €/yr. Sähkö: sama 0,10 €/h-paikkamerkki (G1:n todellista tehonkulutusta ei erikseen vahvistettu — lukijan pitäisi korvata, jos tiedossa).

| Vuotuiset tuottavat tunnit | Kustannus/h (rahoitus + sähkö) | Kustannus/h (sis. huollon) |
|---|---|---|
| 2 000 | 1,57 € | 2,20 € |
| 4 000 | 0,84 € | 1,15 € |
| 6 000 | 0,59 € | 0,80 € |
| 8 000 | 0,47 € | 0,63 € |

**Rajahuomautus (toistettu, vaaditun tavan mukaisesti jokaiselle mittakaava-/sijoitustyyppiskenaariolle tässä asiakirjassa):** molemmat §7a ja §7c ovat muokattavia havainnollistuksia, rakennettu ilmoitetuille oletuksille hinnasta, rahoituksesta, käyttöasteesta ja sähköstä — ei ennusteita, eikä sijoitus-, hankinta- tai toiminnallista neuvontaa. Todellinen kokonaiskustannus sisältäisi myös valvonnan, ohjelmisto-/tilausmaksut, vakuutuksen, työtilan mukauttamisen, kulutustarvikkeet ja käyttökatkokset, joita mikään näistä ei mallinneta tässä.

---

## 8. Talouden kerrosten erottelu, havainnollistettuna paikallistetun kotitalouden tekoälytehtaan (§5) luvuilla 34.6 tok/s:llä, 100%:n käyttöasteella

Projektin vaaditun menetelmän mukaisesti näitä kerroksia ei koskaan yhdistetä yhdeksi luvuksi. **Corrected 2026-08-13:** aiempi versio tästä osasta käytti tok/s = 65 "50–83:n vaihteluvälin keskikohtana" — mutta 83 tok/s ei jäljittynyt mihinkään tämän projektin rekisterin lähteeseen (ks. §5:n korjaus) ja se on poistettu. Käyttäen tok/s = 34.6 (§5:n vahvistetun 30.8–38.4 tok/s -vaihteluvälin keskikohta) yhdelle luettavalle lasketulle polulle:

`Tokens/yr @ 100% = 34.6 × 31 536 000 = 1 091,1M`

| Kerros | Mitä sisältyy | Kaava | Tulos (€/M tokenia) | Luokka |
|---|---|---|---|---|
| 1. Raaka sähkökustannus | Vain sähkö | 315 € ÷ 1 091,1M | **0,289 €/M** | JOHDETTU LASKELMA |
| 2. Laitteiston poistettu tuotantokustannus | + tasapoisto pääomasta (4 370 € ÷ 5v = 874 €/vuosi, ei korkoa) | (874 €+315 €) ÷ 1 091,1M | **1,090 €/M** | JOHDETTU LASKELMA |
| 3. Rahoitettu omaisuuskustannus | Tasapoisto korvattu 8 %/5v-rahoitetulla maksulla (1 095 €/vuosi) | (1 095 €+315 €) ÷ 1 091,1M | **1,292 €/M** | JOHDETTU LASKELMA |
| 4. Täysi toimintainfrastruktuurikustannus | + havainnollistava 5 %/vuosi pääomasta tuelle/ohjelmistolle/tilalle (218,5 €/vuosi, SKENAARIO-OLETUS) | (1 095 €+315 €+218,5 €) ÷ 1 091,1M | **1,492 €/M** | JOHDETTU LASKELMA SKENAARIO-OLETUS -syötteellä |
| 5. Kapasiteetti-/käyttöastekustannus | Sama pino, mutta 50 %:n käyttöasteella 100 %:n sijaan (kiinteät kustannukset muuttumattomia, sähkö ja tokenit puolittuvat molemmat) | (1 095 €+218,5 €+157,5 €) ÷ 545,6M | **2,696 €/M** | JOHDETTU LASKELMA — osoittaa käyttöasteherkkyyden |
| 6. Tokenin tuotantokustannus | = itse €/M-token-luku sillä kerroksella/käyttöasteella, jonka olet valinnut | — | (yksi yllä olevista) | JOHDETTU LASKELMA |
| 7. Työkuorman / tekoälytyökapasiteetin kustannus | Muunna tokenin kustannus kustannukseksi per käyttötyyppitunti, käyttäen havainnollistavia käyttöintensiteettivyöhykkeitä (chat/neuvonantaja 10k–30k tokenia/h; kopilotti 60k–120k; delegoitu agentti 200k–600k; raskas moniagentti 1M–12M+ tokenia/h — vyöhykkeet peräisin hankkeen omasta käsitteellisestä kehyksestä, ei itsenäisesti uudelleen vahvistettu per-vyöhyke tässä tarkistuksessa) | tokenia/h × (€/M-token-hinta) ÷ 1 000 000 | esim. 1,492 €/M:llä ja 60k tokenia/h: 0,090 €/h; 1M tokenia/h:lla: 1,49 €/h | JOHDETTU LASKELMA vahvistamattomalla vyöhykeoletuksella |
| 8. Tulos ja arvo | Tuottiko tuo tekoälytyökapasiteetin tunti mitään, joka on enemmän, vähemmän tai ei mitään arvokkaampaa kuin sen kustannus | **ei mekaanisesti johdettu kerroksista 1–7** | — | Vain TULKINTA — arvo voi olla positiivinen, nolla tai negatiivinen; enemmän tokeneita/tunteja ei automaattisesti ole parempi |

---

## 9. Lyhyt teollisuustason huomautus (GB300 NVL72 -mittakaava), EUR, täydellisyyden vuoksi

Tämän työkirjan pääasiallinen paikallistusfokus on yllä olevissa kotitalous-/osuustoiminnallisissa/robotti-tasoissa, koska ne ovat sitä, mitä yksilö tai PK-yrityksen lukija oikeasti hinnoittelisi paikallisesti. Täydellisyyden vuoksi kaksi teollisen mittakaavan faktaa ja niiden keskeiset varaukset, uudelleen esitettynä EUR:ssa:

- **HAVAITTU FAKTA:** NVIDIA:n oma MLPerf v6.0 -lähetys kirjasi **2 494 310 tokenia/s ("2,5M tok/s") DeepSeek-R1:llä** — mutta tämä on aggregaatti **neljän yhteenliitetyn GB300 NVL72 -järjestelmän** (yhteensä 288 GPU:ta) yli, ei yhden 72-GPU-räkin. Per-GPU-läpimenoteho yhdelle räkille Offline-skenaariossa oli 9 821 tokenia/s/GPU. (developer.nvidia.com-blogi, tarkistettu 2026-08-12.)
- **KORJATTU — nyt VAHVISTETTU, rajausvarauksella:** "0,123 $/M tokenia" -luku on vahvistettu suoraan NVIDIA:n omalla sivustolla: GB300 NVL72 toimittaa päättelyä hintaan **0,123 $ per miljoona tokenia hintaan 116 tokenia/s/käyttäjä, käyttäen NVIDIA Dynamoa ja TensorRT-LLM:ää**, SemiAnalysis InferenceX -vertailutulosten mukaan huhtikuusta 2026 (**[FAKTA]** — nvidia.com/en-gb/solutions/ai/inference/, tarkistettu 2026-08-13). Tämä koskee erityisesti **72-GPU:n räkkitason järjestelmää tällä vuorovaikutteisuusasetuksella** — sitä ei pidä käyttää hinnoittelemaan yhtä työasemaa, DGX Sparkia tai DGX Stationia; niin tehtäessä aliarvioitaisi kyseisen tason todellinen kustannus karkeasti kahdesta kolmeen suuruusluokkaa (ks. §6:n osuustoiminnallinen täsmäytys yllä, joka korjaa juuri tämänkaltaisen tasojen välisen sekoittamisen). Erikseen siteerattu "2,8M tok/s/MW" GB300-läpimenotehon luku pysyy **VAHVISTAMATTOMANA** — sitä ei löydetty sanatarkasti SemiAnalysisin InferenceX-sivustolta tämän tarkistuksen aikana; lähimmät vahvistetut vieressä olevat datapisteet siellä ovat karkeasti 1,67M–3,89M tok/s/MW riippuen valitusta vuorovaikutteisuuspisteestä.
- **Vain havainnollistava, EUR-muunnettu capex-viite (nimenomaisesti ei virallinen NVIDIA-hinnoittelu — analyytikkoarvioon perustuva):** ~4 M$/räkki (16 M$ 4-räkin/288-GPU:n asennukselle) × 0,93 FX = **≈3,72 M€/räkki (≈14,9 M€ 288 GPU:lle)**, rahoitettu 5v@8 % → ≈3,73 M€/vuosi rahoitusmaksu. 90 %:n käyttöasteella ja ~71 biljoonaa tokenia/vuosi, rahoituksen lisämaksu yksin ≈ 0,0106 €/M tokenia poiston lisäksi — suuruusluokan herkkyystarkistus, ei kokonaiskustannusväite.

**Rajahuomautus:** kuten yllä — vain havainnollistava skenaario, ei sijoitus- tai hankintaohjeistus, ja nimenomaisesti rakennettu vahvistamattomalle analyytikkotyylisen capex-per-rack-arviolle virallisen NVIDIA-hinnan sijaan.

---

## 10. Pikaviite: ainoat solut, jotka tarvitsee muuttaa tehdäksesi tästä oman maasi työkirjan

| Muutettava solu | Missä se esiintyy | Nykyinen paikkamerkki |
|---|---|---|
| FX-kurssi | §1, kaikki valuuttamuunnokset | 1 USD = 0,93 € |
| Kotitalous-/prosumer-sähkön hinta | §5, §7 | 0,15 €/kWh |
| Teollisuuden sähkön hinta | §9 | 0,09 €/kWh |
| Rahoituskorko & aika | §5, §6, §7 | 8 % / 5 vuotta |
| Paikallinen laitteiston toimitushinta (ALV+tuonti+marginaali) | §3 | *tyhjä — ei mallinnettu, hanki todellinen tarjous* |

Kaikki näiden viiden solun alavirralla on kaava, esitetty selkeästi joka yllä olevassa osassa, niin että minkä tahansa niistä muuttaminen johtaa uudelleen joka riippuvan luvun uudestaan rakentamatta mallia tyhjästä.

---

*Tämä työkirja on yksi mahdollisesti monista kansallisista/valuuttasovituksista samasta taustalla olevasta menetelmästä. Se julkaistaan samalla CC BY 4.0 -lisenssillä kuin emo-whitepaper. Se on koulutuksellista tutkimusta ja skenaarioanalyysiä vain — ei sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa.*
