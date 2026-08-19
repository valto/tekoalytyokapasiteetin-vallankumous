# Sijoitusteesin skenaariomuistiinpanot — Julkaisuresurssi #12
### Kumppani "Miksi tekoälyyn investoidaan biljoonia?" -teokselle (Valto Loikkanen, CC BY 4.0)

**Tämän muistiinpanon tila:** Nämä ovat koulutuksellisia skenaariomuistiinpanoja, ei sijoitus-, hankinta-, vero- tai politiikkaneuvontaa. Jokainen alla oleva luku on joko HAVAITTU FAKTA (lähdeviitattu ensisijaiseen lähteeseen), LÄHTEESEEN KOHDISTETTU LAUSUNTO (nimetyn henkilön/organisaation väite, ei itsenäisesti todistettu), JOHDETTU LASKELMA (esitetty kaavalla), SKENAARIO-OLETUS (muokattava havainnollistava syöte, ei markkinaluku) tai TULKINTA (merkitty mahdollinen tulkinta yllä olevasta). Tämä raja koskee erikseen **kutakin alla olevaa tasokappaletta** — mikään neljästä alla olevasta tasosta ei ole suositus ostaa, rakentaa tai sijoittaa mihinkään.

**Kanonisen lähteen huomautus (2026-08-13):** jokainen alla oleva kustannusluku on siteerattu suoraan Globaali perustaso -työkirjasta (Julkaisuresurssi #7) ja Tekoälytyökapasiteetin muuntotyökirjasta (Julkaisuresurssi #9) — kahdesta työkirjasta, jotka kantavat tämän paperin auktoritatiiviset tuotantokustannuskäyrät — sen sijaan, että ne johdettaisiin uudelleen tässä. Missä tämän muistiinpanon aiempi luonnos käytti väliaikaisia tai eri lähteistä peräisin olevia lukuja, ne on korvattu kanonisilla luvuilla.

### Näyttöluokkien selitteet
| Koodi | Merkitys |
|---|---|
| HAVAITTU FAKTA | Tarkistettu suoraa/ensisijaista lähdettä vasten |
| LÄHTEESEEN KOHDISTETTU LAUSUNTO | Nimetyn henkilön/organisaation julkinen väite; ei itsenäisesti todistettu |
| JOHDETTU LASKELMA | Läpinäkyvä aritmetiikka siteeratuista syötteistä; kaava esitetty |
| SKENAARIO-OLETUS | Muokattava havainnollistava parametri, ei markkinaluku |
| TULKINTA | Merkitty mahdollinen tulkinta, joka yhdistää faktoja/lausuntoja/skenaarioita |

---

## Taso 1 — Kotitalous (yhden laitteen laskenta)

Kotitaloustason "tehdas" on yksi prosumer-tekoälytyöasema (havainnollistava viitelaite: NVIDIA DGX Spark), jota yksilö tai kotitalous käyttää henkilökohtaiseen tai pienen projektin käyttöön. Talous toimii vain, jos omistajan omakäyttö — tai pieni jälleenmyyty/jaettu osuus siitä — on riittävän korkea ja riittävän vakaa kattamaan kiinteän rahoituskustannuksen; alla on lyhyt skenaariotaulukko, ei suositus.

| Kohta | Arvo | Luokka |
|---|---|---|
| Viitelaite | NVIDIA DGX Spark, GB10 Superchip, 128GB yhtenäistä muistia | HAVAITTU FAKTA — nvidia.com/en-us/products/workstations/dgx-spark/ |
| Vaadittu pääoma (nykyinen suositushinta) | 4 699 $ (Founders Edition; nostettu 3 999 $:sta helmikuussa 2026) | HAVAITTU FAKTA — NVIDIA Developer Forumsin hinnanmuutosilmoitus |
| Havainnollistava rahoitettu pääoma+sähkökustannus | ~1 129 $/yr (5v @ 8% rahoitus) + 25–210 $/yr sähköä käyttöasteesta/hintaskenaariosta riippuen | JOHDETTU LASKELMA — ks. Globaali perustaso -työkirja §2.1–2.2 täydelle johdannolle |
| Kustannus per M tokenia, koko käyttöastevälillä (matala/keski/korkea skenaario) | **1,37–11,89 $/M tokenia** (paras tapaus: 38,4 tok/s, 80 % käyttöaste; huonoin tapaus: 30,8 tok/s, 10 % käyttöaste) | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §2.4 mukaan |
| $/tekoäly-työtunti, keskiskenaario (3,17 $/M tokenia, 30,8 tok/s, 40 % käyttöaste) | Chat/neuvonantaja 0,032–0,095 $/h; aktiivinen kopilotti 0,190–0,380 $/h; delegoitu agentti 0,633–1,900 $/h; raskas orkestrointi 3,17–38,00 $/h | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §2.5 mukaan |

**Verrattuna vähittäis-API-hintaan (korjattu 2026-08-13):** parhaimmalla käyttöasteella Kotitaloustaso on halvempi kuin kaikki vähittäistasot paitsi OpenAI:n halvin (Luna); huonoimmalla käyttöasteella Kotitaloustaso on kalliimpi kuin useimmat vähittäistasot paitsi kaikkein kalleimmat (Sol, Fable 5). Tämä on aito vaihteluväli, ei kiinteä kerroin suuntaan tai toiseen — ks. Globaali perustaso -työkirja §7 täydelle korjatulle vertailutaulukolle.

**Kysyntäpuolen tekijät, jotka oikeuttaisivat sen:** jatkuva henkilökohtainen tai pienen tiimin käyttö selvästi satunnaisen chat-tason yläpuolella (siis säännöllinen työtoveri-/kopilottitason käyttö, ei sattumanvaraisia kyselyitä); tietosuoja-, viive- tai offline-saatavuusvaatimus, jota API-pääsy ei täytä; halukkuus ajaa avoimen painotuksen malleja sen sijaan, että maksettaisiin eturintaman laboratorion vähittäis-API-hintoja samasta työkuormasta.

**Keskeiset riskit:** laitteisto menettää arvoaan nopeasti liikkuvaa eturintamaa vastaan (tänään ostettu laite voi olla kykyvanhentunut ennen kuin se on taloudellisesti poistettu); yhteisön ilmoittama läpimenoteho (DGX Sparkin Qwen3.5-122B-A10B-foorumibenchmark, LÄHTEESEEN KOHDISTETTU LAUSUNTO, ~38,4 tok/s vahvistettu / ~51 tok/s väitetty mutta vahvistamaton) on selvästi alle sen, mitä yritystason räkit saavuttavat, joten per-tokenin kustannus on rakenteellisesti korkeampi kuin suuremmilla tasoilla; jouten oleva aika on puhdasta uponnutta kustannusta, koska rahoitus kertyy käytettiinpä laitetta tai ei; käyttöaste on yksittäisenä muuttujana suurin kustannusvipu (~7-kertainen heilahdus 10 % ja 80 % käyttöasteen välillä samalla läpimenoteholla, Globaali perustaso -työkirjan §2.4 mukaan).

**Mitä pitäisi olla totta, jotta tämä taso olisi järkevä:** omistajan todellisen käytön täytyy sijoittua lähelle "aktiivinen kopilotti" -kaistan huippua tai sen yläpuolelle, johdonmukaisesti, useiden vuosien ajan, käyttöasteella, joka pitää $/M-tokenia selvästi alle 11,89 $ huonoimman tapauksen luvun — satunnainen tai kokeileva käyttö tekee eturintaman laboratorion vähittäis-API-hinnoittelusta halvemman kuin laitteiston omistamisesta useimmissa skenaarioissa. Tämä on havainnollistus tasapainopisteen logiikasta, ei väite, että kotitalousomistus voittaisi vuokrauksen jollekin tietylle ostajalle.

*Ei-neuvontaa koskeva vastuuvapauslauseke: tämän tason luvut ovat muokattava havainnollistus tasapainopisterakenteesta, ei suositus ostaa DGX Spark tai mikä tahansa muu laite.*

---

## Taso 2 — Osuustoiminnallinen (jaettu monilaite- tai jaettu työasemaluokan kone)

Osuustoiminnallinen tehdas kokoaa pääomaa jäsenten kesken päästäkseen yksittäistä yksikkökustannusta alemmas jaetun käyttöasteen avulla, hintana koordinaatioyleiskustannus ja hallinto-/pääsynjakoongelma. Tälle skenaariolle on olemassa kaksi laitteistotasoa, jotka kuvaavat kahta eri laitetta, ei kahta kilpailevaa arviota yhdestä asiasta.

| Kohta | Arvo | Luokka |
|---|---|---|
| **DGX Spark -pooli** — 10 yksikköä, 50 jäsentä | Pääoma ~46 990 $; rahoitus+sähkö ~14 000–15 770 $/vuosi ennen hallintoa/verkkoa | JOHDETTU LASKELMA — 10 × 4 699 $ (HAVAITTU FAKTA yksikköhinta); ks. Globaali perustaso -työkirja §3.1–3.4 |
| Kustannus per M tokenia (DGX Spark -pooli, 20–85 % käyttöaste) | **1,99–7,62 $/M tokenia** | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §3.4 mukaan |
| $/jäsen/kk (DGX Spark -pooli, 50 jäsentä) | **24,67–27,40 $/jäsen/kk** | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §3.5 mukaan |
| $/tekoäly-työtunti, keskiskenaario (3,20 $/M tokenia) | Chat/neuvonantaja 0,032–0,096 $/h; aktiivinen kopilotti 0,192–0,384 $/h; delegoitu agentti 0,641–1,922 $/h; raskas orkestrointi 3,20–38,44 $/h | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §3.6 mukaan |
| **Jaettu DGX Station -luokan kone** — 1 yksikkö, 50 tai 100 jäsentä | Pääoma, havainnollistava 100 000 € ilman ALV:a (tälle koneluokalle ei ole olemassa virallista NVIDIA-hintaa); rahoitettu 5v @ 6,5 % | SKENAARIO-OLETUS — ks. Tokenitehtaan skenaariotyökirja §1a täydelle rakenteelle |
| $/jäsen/kk (jaettu työasemaluokan kone) | **42 €/jäsen/kk 50 jäsenellä; 21 €/jäsen/kk 100 jäsenellä** | JOHDETTU LASKELMA 100 000 €:n havainnollisesta pääomaperustasta, Tokenitehtaan skenaariotyökirjan §1a mukaan |

**Molemmat luvut ovat oikein sille laitteistolle, jota ne kuvaavat, eivät kilpailevia arvioita yhdestä osuuskunnasta.** DGX Spark pool hinnoittelee kymmenen pienempää, itsenäistä pöytäluokan laitetta; jaettu työasemaluokan kone hinnoittelee yhden suuremman järjestelmän, jossa on huomattavasti enemmän muistia ja laskentaa per yksikkö. Ks. Tokenitehtaan skenaariotyökirja (Julkaisuresurssi #10) §1/§1a/§1b täydelle korjatulle selitykselle siitä, miksi näitä ei koskaan ollut ristiriidassa.

**Kysyntäpuolen tekijät, jotka oikeuttaisivat kumman tahansa tason:** riittävästi jäseniä, joilla on aidosti toisiaan täydentävät käyttöaikataulut (tasoittavat toistensa huippuja) pitämään kokonaiskäyttöaste korkeana; jaettu luottamus-/hallintorakenne, joka voi jakaa niukkaa huippukapasiteettia oikeudenmukaisesti; osuuskunnan käyttöprofiili, joka painottuu kopilotti-/delegoitu agentti -kaistoihin sen sijaan, että olisi satunnaista chattia (per-capita vain-chat-käyttö ei poista jaettua laitteistoa hyvin).

**Keskeiset riskit:** ilmaisin ratsastaja- ja jakoon liittyvät oikeudenmukaisuusongelmat (raskaat käyttäjät vs. kevyet maksajat); koordinaatio-/hallintoyleiskustannus, jota ei täysin mallinneta kummassakaan yllä olevassa otsikkoluvussa; jäsenkato, joka horjuttaa käyttöasteoletusta, jota molemmat tasot riippuvat; väärän laitteistotason valinta todelliselle jäsenkysynnälle (DGX Spark pool voi palvella riittämättömästi jäseniä, jotka tarvitsevat suurikontekstista tai biljoonan parametrin luokan paikallista päättelyä, kun taas yksi DGX-Station-class machine voi olla vajaakäytöllä osuuskunnalle, jonka jäsenet tarvitsevat enimmäkseen kevyitä, rinnakkaisia, matalakontekstisia työkuormia).

**Mitä pitäisi olla totta, jotta tämä taso olisi järkevä:** valittiinpa mikä taso tahansa (DGX Spark -pooli hintaan 24,67–27,40 $/jäsen/kk, tai jaettu DGX Station -luokan kone hintaan 42 €/jäsen/kk 50 jäsenellä / 21 € 100 jäsenellä), sen täytyy voittaa jäsenen realistinen vaihtoehto — joko yksilöllinen kotitalousomistus (Taso 1) tai mitattu API-/pilvipääsy — kyseisen jäsenen todellisella käyttötasolla ja todellisilla kykyvaatimuksilla (muisti/kontekstikoko, mallin mittakaava, rinnakkaisuus), ei oletetulla keskiarvolla.

*Ei-neuvontaa koskeva vastuuvapauslauseke: yllä olevat osuustoiminnalliset luvut ovat havainnollistavia skenaariolaskelmia kahdelle eri laitteistotasolle, ei validoitu osuuskunnan perustamisen liiketoimintasuunnitelma.*

---

## Taso 3 — Ammattimainen / PK-yritys (varattu yritysmittakaavan kapasiteetti)

Tämä taso sijoittuu osuustoiminnallisen ja hyperskaalatason väliin, ja se on nykyisen lähdeaineiston vähiten täsmällisesti rajattu — käsittele sitä skenaarioluonnoksena, ei johdettuna mallina. Se kattaa yrityksen, toimiston tai keskisuuren yrityksen, joka tarvitsee varattua, korkeamman vuorovaikutteisuuden päättelykapasiteettia enemmän kuin osuustoiminnallinen allas tyypillisesti tarjoaa, joko omistamalla yritysluokan laitteistoa tai, yleisemmin, sopimalla varatusta pilvi-/co-location-kapasiteetista.

| Kohta | Arvo | Luokka |
|---|---|---|
| Pääomapolku A — omistettu yritysluokan laitteisto | Yksittäinen NVIDIA HGX B300 (8× Blackwell Ultra GPU) -solmu; havainnollistava capex 250 000–500 000 $ (keski 350 000 $) ja tehonkulutus 8–15kW (keski 11kW) — **NVIDIA ei julkaise hintaa tai tehospesifikaatiota tälle SKU:lle**, niin molemmat luvut ovat nimenomaisesti paikkamerkkejä | SKENAARIO-OLETUS — nimenomaisesti ei virallista hinnoittelua, Globaali perustaso -työkirjan §4.1 mukaan |
| Pääomapolku B — sopimuksellinen varattu kapasiteetti | Esimerkki mittakaavasta: IBM Cloud + Together AI:n monivuotinen 240 M$ -sopimus varatulle NVIDIA HGX B300 -päättelyklusterille, saatavilla Q1 2027 | HAVAITTU FAKTA — IBM Newsroomin lehdistötiedote, 11.8.2026 (tämä on jaettu/monen asiakkaan sopimus, joka havainnollistaa ammattimaisen tason markkinan mittakaavaa, ei yhden ostajan omaa kulutusta) |
| Kustannus per M tokenia, HGX B300 -solmu (25–90 % käyttöaste) | **0,044–0,146 $/M tokenia** — rakennettu JOHDETUN lineaarisen GPU-määrän skaalauksen pohjalta HAVAITUISTA per-GPU MLPerf-luvuista, jotka lähdetyökirja merkitsee optimistiseksi ylärajaksi, koska se olettaa, että 8-GPU-kotelo toistaa NVL72-räkkitason per-GPU-läpimenotehon | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §4.3 mukaan; matala luottamus pohjana olevien capex/tehosyötteiden osalta |
| $/tekoäly-työtunti, keskiskenaario (0,064 $/M tokenia) | Chat/neuvonantaja 0,0006–0,0019 $/h; aktiivinen kopilotti 0,0038–0,0076 $/h; delegoitu agentti 0,0127–0,0382 $/h; raskas orkestrointi 0,064–0,764 $/h | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §4.4 mukaan |

**Tärkeä rajaushuomautus:** yllä oleva 0,044–0,146 $/M-tokenia-vaihteluväli on erityisesti Ammattimaisen tason pienemmälle HGX B300 (8-GPU) -solmulle. Sitä ei pidä sekoittaa Hyperskaalatason 0,123 $/M-tokenia-lukuun (vahvistettu suoraan NVIDIAn omalla sivustolla, 2026-08-13) tai laajempaan 0,065–3,3 $/M-tokenia GB300-vuorovaikutteisuuskäyrään — ne kuvaavat 72-GPU:n GB300 NVL72 -räkkiä, eri, suurempaa laitteistotasoa (Taso 4 alla).

**Kysyntäpuolen tekijät, jotka oikeuttaisivat sen:** yritys, jonka tuote aidosti vaatii korkean vuorovaikutteisuuden, matalan viiveen päättelyä volyymissä (ei vain satunnaista käyttöä); työkuormaprofiili, joka vastaa delegoidun agentin tai varhaisen moniagentin kaistaa kevyen chatin sijaan; vaatimustenmukaisuus-, tietosuoja- tai räätälöintitarve, jota valmiit eturintaman laboratorioiden API:t eivät täytä yhtä halvasti tällä volyymilla.

**Keskeiset riskit:** tämän tason pohjana olevat capex- ja tehonkulutussyötteet ovat vahvistamattomia paikkamerkkejä (mitään julkista NVIDIA-/jälleenmyyjähintaa HGX B300 node -laitteelle ei ole olemassa), niin tämän tason koko kustannuskäyrä kantaa oleellisesti matalampaa luottamusta kuin Tasot 1, 2 tai 4; monivuotisen varatun kapasiteetin sopimukseen sitoutuminen (Pääomapolku B) lukitsee nykyisen laitteistosukupolven nopeasti arvoaan menettävää suorituskykykäyrää vastaan (Vera Rubin-class-laitteiston väitetään NVIDIA:n omassa markkinoinnissa — LÄHTEESEEN KOHDISTETTU LAUSUNTO, ei itsenäisesti todistettu — leikkaavan tokenin kustannuksen jopa 10x versus GB200, kun SemiAnalysisin itsenäinen analyysi on maltillisempi, roughly 2–5.4x).

**Mitä pitäisi olla totta, jotta tämä taso olisi järkevä:** yrityksen todellinen, jatkuva tokenivolyymi ja vaadittu vuorovaikutteisuustaso täytyy olla tiedossa (ei arvattu) ennen kuin verrataan omistettua/varattua kapasiteettia eturintaman laboratorion API-vuokraukseen tai osuustoiminnalliseen tasoon; vahvistettu HGX B300 -hinta-/tehotarjous pitäisi korvata yllä olevat paikkamerkkisyötteet ennen kuin tätä tasoa käytetään mihinkään todelliseen mitoitusharjoitukseen.

*Ei-neuvontaa koskeva vastuuvapauslauseke: tämä taso on näiden neljän luonnoksen vähiten vahvistettu, eikä sitä pitäisi käyttää mitoittamaan mitään todellista pääomasitoumusta; se havainnollistaa kustannus- ja riskimuotoa, ei liiketoimintasuunnitelmaa.*

---

## Taso 4 — Hyperskaala (usean gigawatin tekoälyinfrastruktuuri)

Tämä on taso, jota nimetyt rahoitus- ja teollisuusjohtajat (Jensen Huang, Larry Fink, and five other CEOs on CNBC, Aug 10 2026) käsittelevät nimenomaisesti uusien sadan-miljardin-dollarin-luokan rahoitusrakenteiden kohteena. Kaikki mittakaavasta, käyttöönottotarkoituksesta ja kokonaisesta tulevasta pääomasta tässä tulee nimetyistä, julkisista mutta eteenpäin katsovista lausunnoista — ei tarkastetusta markkinakokonaisuudesta.

| Kohta | Arvo | Luokka |
|---|---|---|
| Vasta ilmoitettu rahoitusrakenne | Six MOUs (Apollo, Blackstone, BlackRock, Brookfield, Goldman Sachs, KKR) aiming to mobilize >500 $B kolmannen osapuolen pääomaa hyperskaalaajille, eturintaman laboratorioille ja yrityksille | HAVAITTU FAKTA — CNBC transcript & article, Aug 10 2026, corroborated by Fortune |
| Kustannus per gigawatti | "jotain 50, 60 miljardin dollarin luokkaa" per gigawatti (energia, maa, teho/kuori, laskenta) | LÄHTEESEEN KOHDISTETTU LAUSUNTO — Jensen Huang, CNBC-lähetys, 10.8.2026; itsenäiset analyytikkoarviot (Morgan Stanley ~49 miljardia dollaria/GW, Bernstein ~35 miljardia dollaria/GW, Foxconn ~47 miljardia dollaria/GW, Epoch.ai ~38 miljardia dollaria/GW) sulkevat tämän sisäänsä uskottavana korkeintaan, ei vahvistettuna |
| Pidemmän aikavälin pääomamittakaava | "trillions of dollars over the coming years"; >70GW:n uusi Yhdysvaltain sähkönkysyntä implisiittisesti | LÄHTEESEEN KOHDISTETTU LAUSUNTO — Larry Fink, same broadcast; suunnaltaan yhtenevä, mutta ei identtinen, itsenäisten BCG (50–80GW US shortfall by 2030) ja S&P Global (64.4GW hyperscale draw in 2025) -lukujen kanssa |
| Kustannus per M tokens — täysi tuotantokustannuskäyrä, 25–90% käyttöaste | **0,091–0,312 $/M tokens (canonical mid: 0,133 $/M)** — pääoma + rahoitus + sähkö + käyttömenot, kaikki kerrokset mukana | JOHDETTU LASKELMA, kanoninen luku Globaali perustaso -työkirjan §5.6 mukaan |
| Ristiintarkistus: NVIDIA:n omat vahvistetut luvut | 0,123 $/M tokens at 116 tokens/sec/user, using NVIDIA Dynamo and TensorRT-LLM, attributed to SemiAnalysis InferenceX (April 2026) | HAVAITTU FAKTA — vahvistettu suoraan nvidia.com/en-gb/solutions/ai/inference/, tarkistettu 2026-08-13; sijoittuu yllä olevaan kanoniseen vaihteluväliin, tiettyyn vuorovaikutteisuuspisteeseen |
| $/AI-working-hour (raskas moniagenttikaista, 1M–12M+ tokens/hr, koko vaihteluväli) | **0,091–3,74 $/hr** across the low-to-high käyttöastevälin | JOHDETTU LASKELMA — kaava: $/hr = ($/M tokens) × (tokens/hour ÷ 1 000 000); alapää 0.091×1=0,091 $, yläpää 0.312×12=3,74 $ |

**Kysyntäpuolen tekijät, jotka oikeuttaisivat sen (nimettyjen johtajien esittämällä tavalla, ei itsenäisesti vahvistettu):** Huangin väite, että "AI tokens are... incredibly profitable" eturintaman laboratorioille (LÄHTEESEEN KOHDISTETTU LAUSUNTO); OpenAI:n omat sisäiset telemetriatiedot, joiden mukaan Codex now accounts for 99,8 % sen viikoittaisesta sisäisestä tulostetokenimäärästä (LÄHTEESEEN KOHDISTETTU LAUSUNTO, OpenAI:n itse-ilmoittama, ei tarkastettu data); Altmanin blogikirjoituksen väite, että tekoälyn kustannus laskee ~10x every 12 months, jonka hän yhdistää Jevonsin paradoksin tapaiseen kysyntäreaktioon (LÄHTEESEEN KOHDISTETTU LAUSUNTO, ei kysynnän kasvunopeuden luku, vaikka sitä toisinaan parafraseerataan sellaisena).

**Keskeiset riskit:** koko rahoitusteesi lepää eteenpäin katsovilla, julkisilla mutta tarkastamattomilla lausunnoilla osapuolilta, jotka hyötyvät kerättävästä pääomasta (Huang myy siruja; Finkin yhtiö auttaisi sijoittamaan pääoman); 50–60 $B/GW-luku on Huangin oma ilmoittama arvio, itsenäisten analyytikkovaihteluvälien yläpäässä, ei tarkastettu kustannus; laitteiston arvonalenemisriski on rakenteellinen myös tässä mittakaavassa — tänään sitoutunut pääoma GB300-era economics -mukaisesti on lukittu laitteistoa vastaan, jonka oman valmistajan mukaan tulee olemaan olennaisesti halvempaa per token samalla monivuotisella rahoitusaikahorisontilla; >70GW US power-demand-luku vaatii todellisen sähköverkon rakentamista, joka on itsessään kiistanalaista ja hidasliikkeistä infrastruktuuria, riippumatta pääoman saatavuudesta.

**Mitä pitäisi olla totta, jotta tämä taso olisi järkevä:** tokenkysynnän kasvun ja per-tokenin kannattavuuden eturintaman laboratorioille pitäisi jatkua jonkinlaisella nopeudella, joka muistuttaa Altmanin ja Huangin kuvaamia, useiden vuosien ajan, useiden laitteistosukupolvien poikki, ilman kestävää per-tokenin hinnan romahdusta, joka ohittaisi vastaavan kysynnän kasvun — mitään näistä ei ole tänä päivänä itsenäisesti todistettavissa; se on veto sille, että yllä olevat LÄHTEESEEN KOHDISTETUT LAUSUNNOT ovat suunnaltaan oikeita, ei ratkaistu fakta.

*Ei-neuvontaa koskeva vastuuvapauslauseke: mikään tämän tason taulukossa tai keskustelussa ei ole signaali sijoittaa, lainata tai sopia mihinkään nimettyihin yhtiöihin, johtajiin tai rahoitusvälineisiin; se tiivistää, mitä nimetyt osapuolet ovat julkisesti väittäneet ja mitä itsenäiset vertailuarvot osoittavat, vain koulutustarkoituksessa.*

---

**Tasojenvälinen huomautus (TULKINTA):** siirtyminen kotitaloudesta hyperskaalaan vaihtaa laskevan $/M-token-kustannuksen nousevaan pääoman keskittymiseen, nousevaan riippuvuuteen nimetyn osapuolen eteenpäin katsovista lausunnoista itsenäisesti tarkastettujen lukujen sijaan, ja siirtymän yksilön/pienen ryhmän hallinnasta (Tasot 1–2) kohti rahoitusrakenteita, joita hallitsee pieni joukko infrastruktuuri- ja varainhoitoyhtiöitä (Taso 4) — tämä keskittymä-vs-kustannus-kompromissi on sama omistusrakennekysymys, joka nostetaan esiin muualla tässä paperissa, ei erillinen löydös.

---

Tämä toimitus on Julkaisuresurssi #12, osa "Miksi tekoälyyn investoidaan biljoonia?" -tutkimuspakettia (CC BY 4.0, Valto Loikkanen).
