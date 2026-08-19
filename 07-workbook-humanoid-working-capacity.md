# Humanoidirobottien työkapasiteettityökirja (Julkaisuresurssi #11)

## Soveltamisalalauselma — lue tämä ensin

Tämä työkirja on **havainnollistava kehollisen kapasiteetin laajennus** whitepaperin ydinketjulle (Sähkö → laitteisto → laskenta → mallit → tokenit → tekoälytyökapasiteetti → digitaalinen työ → tulokset → arvo → toimijuus), laajennettuna: *Pääoma + energia + huolto + käyttöaste + orkestrointi → humanoidin fyysinen työkapasiteetti.*

Se **ei ole** yleinen väite robotiikan taloudesta, tuotesuositus, ennuste minkään todellisen robotin kentällä suoriutumisesta, tai sijoitus-/hankintaohjeistus. Se mallintaa yhtä kapeaa kysymystä — *mitä humanoidirobotin käyttötunnin omistaminen maksaa annetuilla oletuksilla* — käyttäen (a) yhtä selkeästi merkittyä skenaario-oletusta (kirjoittajan alkuperäinen havainnollistava 25 000 € robotti) ja (b) todellista markkinahintavaihteluväliä koottuna neljästä nimetystä, tällä hetkellä myydystä tai ilmoitetusta alustasta. Kaikki alla olevat luvut ovat joko siteerattuja ensisijaisia teknisiä tietoja/hintoja, lähteeseen kohdistettuja toissijaisia väitteitä, läpinäkyvää aritmetiikkaa tai nimenomaisesti merkittyjä skenaario-oletuksia — ei koskaan ennuste. **Tämä on koulutuksellista tutkimusta ja skenaarioanalyysiä, ei sijoitus-, hankinta-, vero- tai politiikkaneuvontaa.** Tämä raja koskee kaikkia alla olevia lukuja, ei vain tätä.

### Näyttöluokkien selitteet (käytössä läpi tekstin)

| Tunniste | Merkitys |
|---|---|
| **HAVAITTU FAKTA** | Ensisijainen/virallinen lähde, tarkistettu elävästi 2026-08-12 tai välittömästi sitä ennen |
| **LÄHTEESEEN KOHDISTETTU LAUSUNTO** | Nimetyn osapuolen julkinen väite; ei itsenäisesti todistettu tosi |
| **JOHDETTU LASKELMA** | Läpinäkyvä aritmetiikka siteeratuista syötteistä; kaava aina esitetty |
| **SKENAARIO-OLETUS** | Näkyvä, muokattava parametri, ei markkinaluku |
| **TULKINTA** | Merkitty selitys siitä, miten kohteet voivat liittyä toisiinsa — ei koskaan esitetty faktana |

---

## Osa 1 — Kaksi lähtökohtaa: havainnollistava skenaario vs. todellinen markkinavaihteluväli

| Tapaus | Hinta | Näyttöluokka | Lähde |
|---|---|---|---|
| **Havainnollistava perustapaus** | 25 000 € (≈ 27 000 $, oletetulla 1.08 EUR/USD-kurssilla) | **SKENAARIO-OLETUS** — kirjoittajan oma alkuperäinen laskettu esimerkki; ei todellinen tuotehinta | Kirjoittajan aiempi laskelma (projektin taustan mukaan); FX-kurssi on erillinen SKENAARIO-OLETUS, ei markkinakurssi |
| **Todellisen vaihteluvälin LOW** | 13 500 $ | **HAVAITTU FAKTA** — Unitree G1:n aloitushinta, "from 13,5 $K," vero/toimitus poissuljettuna | https://www.unitree.com/g1, tarkistettu 2026-08-12 |
| **Todellisen vaihteluvälin MID (kuluttaja/prosumer)** | 20 000 $ ennakkoon (tai 499 $/kk tilaus) | **LÄHTEESEEN KOHDISTETTU LAUSUNTO** — 1X NEO:n varhaisen pääsyn hinta, ilmoitettu Engadgetin toimesta (2025-10-29); ei vahvistettu 1X:n omalla hintasivulla lähderekisterin haussa | https://www.engadget.com/ai/1x-neo-is-a-20000-home-robot-that-will-learn-chores-via-teleoperation-040252200.html |
| **Todellisen vaihteluvälin HIGH (yritystaso)** | ~250 000 $ | **LÄHTEESEEN KOHDISTETTU LAUSUNTO** — Agility Robotics Digit, yhtenevä useiden toissijaisten/aggregaattorilähteiden kesken; mitään ensisijaista Agility-hintasivua ei ollut saatavilla vahvistukseen | Useita toissijaisia lähteitä (GrabARobot, RoboSelect360, Humanoza, ym.), tarkistettu 2026-08-12 |

Nimenomaisesti poissuljettu tämän työkirjan numeerisesta mallista, koska hinnoittelu on vahvistamaton tai olematon 2026-08-12 mennessä: Tesla Optimus (Musk on toistanut **20 000 $–30 000 $:n pitkän aikavälin tavoitteen**, LÄHTEESEEN KOHDISTETTU LAUSUNTO, ei kaupallisia tilauksia tai vahvistettua vähittäishintaa ole olemassa) ja Figure AI:n Figure 03 (ei virallista hinnoittelua julkaistu ollenkaan; ~20 000 $:n luku kiertää vain kolmannen osapuolen aggregaattoreiden kautta). Molemmat sijoittuisivat MID-kaistan sisään tai lähelle sitä, jos niiden tavoitehinnoista tulisi joskus todellisia hintoja — merkitty tässä TULKINTA-tulkintana, ei faktana.

**TULKINTA:** 25 000 €:n (~27 000 $:n) havainnollistava tapaus sijoittuu todellisen MID-kuluttajakaistan (20 000 $) ja olisi noin 2x havaitun LOW-hinnan ja noin 1/9 ATTRIBUTED-yritystason HIGH-hinnan välillä. Se on uskottava havainnollistava piste todellisen vaihteluvälin *sisällä*, ei poikkeama — mutta se ei silti ole vahvistettu markkinahinta millekään nimetylle tuotteelle.

---

## Osa 2 — Vaadittu talouden kerrosten erottelu

Tämän projektin mallinnussääntöjen mukaan alla olevat kerrokset pidetään erillään ja niitä ei koskaan yhdistetä yhdeksi luvuksi: **pääomakustannus → rahoituskustannus → sähkö (toiminta)kustannus → huoltovaraus → käyttöaste → kustannus per tuottava tunti**. (Pidemmät kerrokset — tokenin tuotantokustannus, työkuorman/tekoälytyökapasiteetin kustannus, tulos/arvo — jäävät tämän laitteisto-tunti-mallin soveltamisalan ulkopuolelle ja käsitellään vain Osan 6 tulkinnassa, nimenomaisesti sellaisena merkittynä.)

### 2.1 Pääomakerros (kaikki neljä hintapistettä)

| Tapaus | Hinta | Käsiraha (20 %, SKENAARIO-OLETUS) | Rahoitettu määrä |
|---|---|---|---|
| Havainnollistava (25 000 € / ~27 000 $) | 27 000 $ | 5 400 $ | 21 600 $ |
| Todellinen LOW (13 500 $) | 13 500 $ | 2 700 $ | 10 800 $ |
| Todellinen MID (20 000 $) | 20 000 $ | 4 000 $ | 16 000 $ |
| Todellinen HIGH (250 000 $) | 250 000 $ | 50 000 $ | 200 000 $ |

20 % käsiraha on **SKENAARIO-OLETUS**, joka hallitsee, kuinka paljon pääomaa rahoitetaan vs. maksetaan ennakkoon; se on muokattava (ks. Osan 3.2 herkkyystarkastelu).

---

## Osa 3 — Rahoituskerros

**JOHDETTU LASKELMA.** Standardi tasaerälainakaava:

`M = P × i / (1 − (1+i)^-n)`  jossa P = rahoitettu määrä, i = kuukausikorko (vuosikorko ÷ 12), n = kuukausierien lukumäärä (vuodet × 12).

Perustapaus: 5 vuoden laina-aika, 8 % vuosikorko (molemmat **SKENAARIO-OLETUKSET** — muokattavia; 8 % on havainnollistava, ei lainanantajan noteeraama korko). Käsiraha poistetaan tasaerinä samalle laina-ajalle ja lisätään takaisin, jotta pääoma+rahoituskustannus on vertailukelpoinen tapausten välillä.

`Vuotuinen pääoma+rahoituskustannus yhteensä = (M × 12) + (Käsiraha ÷ rahoitusajan vuodet)`

### 3.1 Perustapaus (5v @ 8 %, 20 % käsiraha)

| Tapaus | Kuukausierä | Vuotuinen rahoitus (M×12) | Käsiraha poistettuna/v | **Pääoma+rahoituskustannus/v yhteensä** |
|---|---|---|---|---|
| Havainnollistava (~27 000 $ / 25 000 €) | 437,97 $ (≈405,53 €) | 5 255,64 $ | 1 080,00 $ | **6 335,64 $** (≈5 866,33 € — täsmää alkuperäiseen EUR-laskettuun esimerkkiin) |
| Todellinen LOW (13 500 $) | 218,99 $ | 2 627,82 $ | 540,00 $ | **3 167,82 $** |
| Todellinen MID (20 000 $) | 324,42 $ | 3 893,07 $ | 800,00 $ | **4 693,07 $** |
| Todellinen HIGH (250 000 $) | 4 055,28 $ | 48 663,35 $ | 10 000,00 $ | **58 663,35 $** |

### 3.2 Rahoitusajan herkkyys (8 % korko, 20 % käsiraha pidetty vakiona) — pääoma+rahoituskustannus/v yhteensä

| Tapaus | 3 v | 4 v | 5 v | 7 v |
|---|---|---|---|---|
| Havainnollistava (~27 000 $) | 9 921,79 $ | 7 677,83 $ | 6 335,64 $ | 4 811,38 $ |
| Todellinen LOW (13 500 $) | 4 961,19 $ | 3 838,91 $ | 3 167,82 $ | 2 405,69 $ |
| Todellinen MID (20 000 $) | 7 349,92 $ | 5 687,28 $ | 4 693,07 $ | 3 563,98 $ |
| Todellinen HIGH (250 000 $) | 91 873,94 $ | 71 091,01 $ | 58 663,35 $ | 44 549,77 $ |

(Havainnollistava-sarake laskettu uudelleen 27 000 $ USD-vastinemittakaavassa sisäisen johdonmukaisuuden vuoksi; native-EUR-arvot skaalautuvat suhteessa.)

### 3.3 Käsirahan herkkyys (5v @ 8 % pidetty vakiona) — pääoma+rahoituskustannus/v yhteensä

| Tapaus | 0 % käsiraha | 20 % käsiraha | 40 % käsiraha |
|---|---|---|---|
| Havainnollistava (~27 000 $) | 6 569,55 $ | 6 335,64 $ | 6 101,73 $ |
| Todellinen LOW (13 500 $) | 3 284,78 $ | 3 167,82 $ | 3 050,87 $ |
| Todellinen MID (20 000 $) | 4 866,33 $ | 4 693,07 $ | 4 519,80 $ |
| Todellinen HIGH (250 000 $) | 60 829,18 $ | 58 663,35 $ | 56 497,51 $ |

**TULKINTA:** laina-ajan pituus vaikuttaa tässä mallissa paljon enemmän kuin käsirahan koko — venyttäminen 3:sta 7 vuoteen leikkaa vuotuisen pääoma+rahoitustaakan noin puoleen, kun käsirahan kaksinkertaistaminen vain kaventaa sitä muutaman prosentin. Molemmat ovat muokattavia vipuja, ei markkinafaktoja.

---

## Osa 4 — Sähkökerros

Kaksi rinnakkaista menetelmää, molemmat **SKENAARIO-OLETUKSET** ellei toisin mainita:

**(a) Kiinteän käyttötunnin oletus** (kuten alkuperäisessä havainnollistavassa tapauksessa): 0,11 $/käyttötunti (≈0,10 €/h oletetulla FX-kurssilla) — yksinkertainen paikkamerkki, ei sidottu mihinkään tiettyyn robotin tehonkulutukseen.

**(b) Spesifikaatioista johdettu hinta**, käyttäen 1X NEO:n HAVAITTUA akkuspesifikaatiota (842 Wh kestoaika 4 tunnin ajalta → keskimääräinen jatkuva kulutus ≈ 0,2105 kW) havainnollistavalla 0,15 $/kWh sähköhinnalla (**SKENAARIO-OLETUS** — uskottava kaupallinen/teollinen Yhdysvaltain keskihinta, ei noteerattu sähköyhtiön tariffi):

`Sähkö $/tunti = keskimääräinen tehonkulutus (kW) × sähkön hinta ($/kWh)`
`= 0,2105 kW × 0,15 $/kWh = 0,0316 $/tunti`

Lähde taustalla olevalle spesifikaatiolle: https://www.1x.tech/neo (HAVAITTU FAKTA — 842 Wh kestoaika, 4 tunnin akunkesto), tarkistettu 2026-08-12.

**TULKINTA:** spesifikaatioista johdettu luku on suuruusluokkaa alempi kuin 0,11 $/h:n kiinteä paikkamerkki — humanoidirobotit ~200W:n keskimääräisellä kulutuksella ovat sähköllisesti halpoja käyttää suhteessa lähes mihin tahansa muuhun tämän mallin pääomakustannukseen; sähkö ei ole tässä sitova kustannustekijä (toisin kuin whitepaperin muualla käsittelemässä konesalin/tokenin tuotantotaloudessa). Tämä spesifikaatio koskee erityisesti 1X NEO:ta ja sitä käytetään havainnollistavana suuruusluokka-ankkurina muille kolmelle hintapisteelle — sitä ei ole vahvistettu Unitree G1:lle, Agility Digitille tai havainnollistavalle tapaukselle.

---

## Osa 5 — Huoltokerros

**SKENAARIO-OLETUS:** huolto-/korjausvaraus = 10 % ostohinnasta vuodessa (muuttumaton alkuperäisestä havainnollistavasta tapauksesta; ei valmistajan noteeraama huoltosopimus millekään näistä neljästä alustasta — mikään näistä neljästä lähderekisterin lähteestä ei julkaise huoltokustannuslukua).

| Tapaus | Huoltovaraus/v |
|---|---|
| Havainnollistava (~27 000 $) | 2 700 $ |
| Todellinen LOW (13 500 $) | 1 350 $ |
| Todellinen MID (20 000 $) | 2 000 $ |
| Todellinen HIGH (250 000 $) | 25 000 $ |

---

## Osa 6 — Käyttöasteherkkyys ja kustannus per tunti -vaihteluvälit

**JOHDETTU LASKELMA.**

`Kustannus/tunti (rahoitus+sähkö) = (Pääoma+rahoituskustannus/v yhteensä + sähkö $/h × vuotuiset tunnit) ÷ vuotuiset tunnit`
`Kustannus/tunti (rahoitus+sähkö+huolto) = (Pääoma+rahoituskustannus/v yhteensä + sähkö $/h × vuotuiset tunnit + huolto/v) ÷ vuotuiset tunnit`

Esitetty molemmilla sähköoletuksilla (flat 0,11 $/h vs. spesifikaatiosta johdettu 0,0316 $/h) ja neljällä tuottavan käyttöasteen tasolla (2 000 / 4 000 / 6 000 / 8 000 tuntia/vuosi — nämä itsessään SKENAARIO-OLETUKSET, jotka rajaavat yhden vuoron ja lähes jatkuvan toiminnan väliä).

### 6.1 Havainnollistava perustapaus (~27 000 $ / 25 000 €) — USD, alkuperäinen EUR-ristiintarkistus suluissa

| Käyttöaste (h/v) | Rahoitus+sähkö (kiinteä) | Rahoitus+sähkö+huolto (kiinteä) | Rahoitus+sähkö (spesifikaatio) | Rahoitus+sähkö+huolto (spesifikaatio) |
|---|---|---|---|---|
| 2 000 | 3,28 $ (3,03 €) | 4,63 $ (4,28 €) | 3,20 $ | 4,55 $ |
| 4 000 | 1,69 $ (1,57 €) | 2,37 $ (2,19 €) | 1,62 $ | 2,29 $ |
| 6 000 | 1,17 $ (1,08 €) | 1,62 $ (1,49 €) | 1,09 $ | 1,54 $ |
| 8 000 | 0,90 $ (0,83 €) | 1,24 $ (1,15 €) | 0,82 $ | 1,16 $ |

(EUR-arvot ovat täsmällinen uudelleenlaskenta native EUR:ssa 0,10 €/h flat electricity -hinnalla — ne täsmäävät alkuperäiseen laskettuun esimerkkiin, vahvistaen sisäisen johdonmukaisuuden.)

### 6.2 Todellisen vaihteluvälin LOW (13 500 $, Unitree G1)

| Käyttöaste (h/v) | Rahoitus+sähkö (kiinteä) | Rahoitus+sähkö+huolto (kiinteä) | Rahoitus+sähkö (spesifikaatio) | Rahoitus+sähkö+huolto (spesifikaatio) |
|---|---|---|---|---|
| 2 000 | 1,69 $ | 2,37 $ | 1,62 $ | 2,29 $ |
| 4 000 | 0,90 $ | 1,24 $ | 0,82 $ | 1,16 $ |
| 6 000 | 0,64 $ | 0,86 $ | 0,56 $ | 0,79 $ |
| 8 000 | 0,51 $ | 0,68 $ | 0,43 $ | 0,60 $ |

### 6.3 Todellisen vaihteluvälin MID (20 000 $, 1X NEO:n varhaisen pääsyn hinta)

| Käyttöaste (h/v) | Rahoitus+sähkö (kiinteä) | Rahoitus+sähkö+huolto (kiinteä) | Rahoitus+sähkö (spesifikaatio) | Rahoitus+sähkö+huolto (spesifikaatio) |
|---|---|---|---|---|
| 2 000 | 2,46 $ | 3,46 $ | 2,38 $ | 3,38 $ |
| 4 000 | 1,28 $ | 1,78 $ | 1,21 $ | 1,71 $ |
| 6 000 | 0,89 $ | 1,23 $ | 0,81 $ | 1,15 $ |
| 8 000 | 0,70 $ | 0,95 $ | 0,62 $ | 0,87 $ |

### 6.4 Todellisen vaihteluvälin HIGH (250 000 $, Agility Digit)

| Käyttöaste (h/v) | Rahoitus+sähkö (kiinteä) | Rahoitus+sähkö+huolto (kiinteä) | Rahoitus+sähkö (spesifikaatio) | Rahoitus+sähkö+huolto (spesifikaatio) |
|---|---|---|---|---|
| 2 000 | 29,44 $ | 41,94 $ | 29,36 $ | 41,86 $ |
| 4 000 | 14,78 $ | 21,03 $ | 14,70 $ | 20,95 $ |
| 6 000 | 9,89 $ | 14,05 $ | 9,81 $ | 13,98 $ |
| 8 000 | 7,44 $ | 10,57 $ | 7,36 $ | 10,49 $ |

### 6.5 Yhteenveto — kustannus per tuottava tunti -vaihteluväli koko kirjon yli

| Käyttöaste | Täysi havaittu/lähteeseen kohdistettu vaihteluväli (sis. huolto, kiinteä sähkö) | Havainnollistava tapaus sijaitsee |
|---|---|---|
| 2 000 h/v | 2,37–41,94 $ | 4,63 $ |
| 4 000 h/v | 1,24–21,03 $ | 2,37 $ |
| 6 000 h/v | 0,86–14,05 $ | 1,62 $ |
| 8 000 h/v | 0,68–10,57 $ | 1,24 $ |

**TULKINTA:** käyttöaste hallitsee kustannus-per-tunti-tulosta enemmän kuin mikä tahansa yksittäinen muuttuja tässä mallissa — siirtyminen 2 000:sta 8 000 tuntiin/vuosi leikkaa tunnikohtaista kustannusta noin 3.5–4x kaikissa hintapisteissä, koska pääoma- ja rahoituskustannukset ovat kiinteitä, kun nimittäjä (tunnit) kasvaa. Havainnollistava 25 000 €:n/~27 000 $:n tapaus seuraa läheisesti todellista MID-kuluttajakaistaa (20 000 $, 1X NEO), kun rahoitus-/huolto-oletukset pidetään vakioina — se ei ole poikkeama suhteessa todellisiin, tällä hetkellä ostettavissa oleviin alustoihin, mutta se sijoittuu selvästi ATTRIBUTED-yritystason HIGH-tapauksen alapuolelle, jonka kustannus per tunti hallitaan ostohinnalla, joka itsessään lepää vain toissijaisen lähteen vahvistuksella, ei ensisijaisella Agility Robotics -hintataulukolla.

---

## Osa 7 — Mitä tämä malli nimenomaisesti jättää pois

Alkuperäisen soveltamisalan mukaisesti (muuttumattomana; **SKENAARIO-OLETUS**-rajaus, ei täydellisyysväite): valvonta-/ihmisvalvontatyön kustannus, robotin ohjelmisto-/tilausmaksut, vakuutus, työtilan muokkaus, kulutustarvikkeet ja käyttökatkos/suunnittelematon korjausaika kiinteän huoltovarauksen ylittävältä osin. Mikään näistä neljästä siteeratusta alustasta ei julkaise dataa, joka mahdollistaisi näiden arvioimisen ensisijaisesta lähteestä 2026-08-12 mennessä; niiden lisääminen vain nostaisi kustannusta per tunti, niin kaikki yllä olevat luvut pitäisi lukea **lattiana**, ei täydellisenä kommersiaalisena kustannuksena.

---

## Osa 8 — Missä tämä liittyy laajempaan ketjuun (vain tulkinta)

**TULKINTA:** tämä työkirja laajentaa whitepaperin ydinketjua — Pääoma + energia + huolto + käyttöaste + orkestrointi → humanoidin fyysinen työkapasiteetti — mutta pysähtyy "kapasiteettiin", tarkoituksella jatkamatta "työhön → tulokseen → arvoon". Robotti, joka maksaa 1 $/tunti omistaa, ei kerro mitään siitä, onko sen suorittama työ arvoltaan 1, 100 dollaria tai ei mitään. Whitepaperin arvokehyksen mukaan työkapasiteetti ei ole arvo, ja enemmän käyttötunteja ei automaattisesti ole parempi. Näiden kustannus-per-tunti-lukujen käyttäminen tietyn liiketoimintasuunnitelman, sijoituspäätöksen tai hankintavalinnan perusteluun menisi pidemmälle kuin mitä tämä työkirja tukee — **tämä ei ole sijoitus-, hankinta-, vero-, oikeudellista tai politiikkaneuvontaa**, ja yllä olevat luvut ovat havainnollistavaa aritmetiikkaa ilmoitetuille, muokattaville oletuksille, ei ennuste minkään todellisen käyttöönoton taloudesta.

---

### Tämän työkirjan täydellinen syöterekisteri (muokkaamista varten)

| Parametri | Käytetty arvo | Luokka | Hallitsee |
|---|---|---|---|
| Havainnollistavan robotin hinta | 25 000 € (~27 000 $) | SKENAARIO-OLETUS | Perustapauksen pääomakerros |
| EUR/USD FX-kurssi | 1,08 | SKENAARIO-OLETUS | Havainnollistavan tapauksen USD-muunnos vain |
| Unitree G1 -hinta | 13 500 $ | HAVAITTU FAKTA (unitree.com, tarkistettu 2026-08-12) | Todellinen vaihteluväli, LOW |
| 1X NEO -hinta | 20 000 $ / 499 $/kk | LÄHTEESEEN KOHDISTETTU LAUSUNTO (Engadget, 2025-10-29) | Todellinen vaihteluväli, MID |
| Agility Digit -hinta | ~250 000 $ | LÄHTEESEEN KOHDISTETTU LAUSUNTO (useita toissijaisia lähteitä) | Todellinen vaihteluväli, HIGH |
| Käsiraha | 20 % (herkkyys: 0 %/40 %) | SKENAARIO-OLETUS | Pääomakerroksen jako |
| Rahoituskorko | 8 % vuosikorko | SKENAARIO-OLETUS | Rahoituskerros |
| Rahoitusaika | 5 v (herkkyys: 3/4/7 v) | SKENAARIO-OLETUS | Rahoituskerros |
| Kiinteä sähkön hinta | 0,11 $/h (≈0,10 €/h) | SKENAARIO-OLETUS | Sähkökerros (menetelmä a) |
| Sähkön hinta spesifikaatioista johdetulle menetelmälle | 0,15 $/kWh | SKENAARIO-OLETUS | Sähkökerros (menetelmä b) |
| 1X NEO:n keskimääräinen tehonkulutus | 0,2105 kW (842 Wh / 4 h) | HAVAITTU FAKTA (1x.tech, tarkistettu 2026-08-12) | Sähkökerros (menetelmä b) |
| Ylläpitovaraus | 10 % ostohinnasta/v | SKENAARIO-OLETUS | Huoltokerros |
| Tuottava käyttöaste | 2 000 / 4 000 / 6 000 / 8 000 h/v | SKENAARIO-OLETUS | Käyttöasteherkkyys |

---

Tämä työkirja (Osa 1 real-price sourcing, Osat 2–6 aritmetiikka, Osat 7–8 soveltamisala/tulkinta) on itsenäinen numeerinen aineisto whitepaperille "Miksi tekoälyyn investoidaan biljoonia?" (CC BY 4.0, Valto Loikkanen).
