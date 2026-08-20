# Julkaisuresurssi #9 — Tekoälytyökapasiteetin muuntotyökirja
## Käyttöintensiteettitikapuu: Tokenia/tunti → $/tekoäly-työtunti, tuotantotasojen yli — plus ihmistyön vertailu

**Osa julkaisua:** *Miksi tekoälyyn investoidaan biljoonia?* — Valto Loikkanen, CC BY 4.0
**Työkirjan tila:** v1.0-luonnos, rakennettu vahvistetusta lähderekisteristä (aikarajaus 2026-08-13)
**Valuuttaperustaso:** Globaali USD
**Riippuu:** Julkaisuresurssi #7 (Globaali perustaso -työkirja — tuotantokustannuskäyrät per taso). Tämä työkirja ei johda laitteisto-/sähkö-/rahoituskustannuksia uudelleen; se ottaa Julkaisuresurssi #7:n jo johdetut $/miljoona-tokenia-luvut syötteinä ja muuntaa ne $/tekoäly-työtunniksi käyttöintensiteettitikapuun yli.
**Ei sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa.** Jokainen alla oleva skenaario on muokattava havainnollistus, rakennettu ilmoitetuille oletuksille — ei ennuste tai suositus.

---

## Näyttöluokkien selite (käytössä joka taulukossa)

| Tunniste | Merkitys |
|---|---|
| **FAKTA** | Ensisijainen dokumentaatio, virallinen tekninen tieto-/hintasivu, viranomaisasiakirja, sääntely tai suora tallenne/transkriptio, itsenäisesti tarkistettu 2026-08-12 tai välittömästi sitä ennen. |
| **LÄHDE** | Nimetyn henkilön/organisaation julkinen, tallenteella oleva lausunto. Ei itsenäisesti todistettu vain siksi, että se on sanottu — myös silloin, kun lausunto itsessään on hyvin dokumentoitu. |
| **LASKELMA** | Läpinäkyvä aritmetiikka siteeratuista FAKTA-/LÄHDE-syötteistä. Kaava aina esitetty, ei koskaan vain tulos. |
| **OLETUS** | Näkyvä, muokattava skenaarioparametri — ei markkinafakta. Se, mitä se hallitsee, on aina ilmoitettu. |
| **TULKINTA** | Merkitty selitys siitä, miten yllä olevat voivat liittyä toisiinsa. Ei koskaan esitetä faktana. |

---

## Osa A — Mikä "token" ja "tekoäly-työtunti" ovat, ja mitä ne eivät ole

**TULKINTA.** Token on mallin prosessoinnin/tuotoksen mitattava yksikkö — se mittaa tekoälyn *työkapasiteettia*, jokseenkin samalla tavalla kuin kWh mittaa energiakapasiteettia. Token **ei** ole yhtä kuin arvo, laatu, oikeellisuus tai "yhden tunnin työ". "Tekoäly-työtunti", sellaisena kuin sitä käytetään tässä työkirjassa, on *käyttöintensiteettivyöhyke* (tokeninkulutuksen nopeus yhden kelloajan tunnin yli), ei yksikkö, joka takaa ihmisvastaavan tuotoksen. Kaksi agenttia voivat molemmat kuluttaa identtisen määrän tokeneita tunnissa ja tuottaa hurjasti erilaista arvoa — yksi hyödyllistä, yksi hukattua, yksi aktiivisesti haitallista. Tämä työkirja hinnoittelee token-läpimenon; se ei hinnoittele, eikä voi hinnoitella, tuloksia. Ks. Osa D tulosten/arvon rajanvedolle nimenomaisesti esitettynä, ja Julkaisuresurssi #11 (tai whitepaperin ydinarvokehyksen osa) täydellisemmälle käsittelylle siitä, miksi työkapasiteetti ≠ arvo.

**Vaadittu talouden kerrosten erottelu (ei koskaan tiivistetä yhdeksi tässä työkirjassa):**

```
raaka sähkökustannus → laitteiston poistettu tuotantokustannus → rahoitettu omaisuuskustannus → täysi toimintainfrastruktuurikustannus
→ kapasiteetti-/käyttöastekustannus → tokenin tuotantokustannus → työkuorman/tekoälytyökapasiteetin kustannus
→ tulos ja arvo (EI mekaanisesti määräytynyt millään yllä olevalla riviltä)
```

Kaikki alla Osissa B ja C elää "tokenin tuotantokustannus"- ja "työkuorman/tekoälytyökapasiteetin kustannus" -kerroksissa. Osa D toistaa nimenomaisesti, että askel "tulokseen ja arvoon" ei koskaan ole automaattinen.

---

## Osa B — Käyttöintensiteettitikapuu (tokenia/tekoäly-työtunti)

Neljä vyöhykettä, matala/keski/korkea, kukin **OLETUS** (havainnollistava vaihteluväli, ei yksittäinen vahvistettu tilasto), mutta tuettuna, missä huomautettu, OpenAI:n itse-raportoidusta Codex-telemetriasta (**LÄHDE**, itse-raportoitu, ei itsenäisesti auditoitu).

| # | Käyttöintensiteettivyöhyke | Mitä se kuvaa | Tokenia/tekoäly-työtunti: Matala | Keski | Korkea | Luokka |
|---|---|---|---|---|---|---|
| 1 | **Chat/neuvonantaja** | Ihminen kysyy, tekoäly vastaa; ihminen lukee/päättää/toteuttaa. Tekoäly ei koskaan kosketa maailmaa suoraan. | 10 000 | 20 000 | 30 000 | **OLETUS** |
| 2 | **Aktiivinen tekoälytyötoveri** | Ihminen ja tekoäly työstävät samaa tehtävää yhdessä reaaliajassa (yhteismuokkaus, yhteiskirjoitus, parityöskentelytyylinen); jatkuva edestakainen vuorovaikutus tunnin sisällä. | 60 000 | 90 000 | 120 000 | **OLETUS** |
| 3 | **Delegoitu yksittäisagentti** | Ihminen määrittelee tuloksen/tavoitteen; yksi agentti suorittaa autonomisesti jakson ajan, ihminen valvoo/tarkistaa yhteiskirjoittamisen sijaan. | 200 000 | 400 000 | 600 000 | **OLETUS** |
| 4 | **Raskas moniagenttiorkestrointi** | Ihminen ohjaa laivastoa — useita rinnakkaisia agentteja käynnissä samanaikaisesti yhtä ihmisen kelloaikatuntia vastaan, ei yhtä agenttia nopeasti käynnissä. | 1 000 000 | 5 000 000 | 12 000 000+ | **OLETUS** |

**Mitä jokaisen vyöhykkeen rajapiste hallitsee:** vyöhykkeen matala/keski/korkea-luvun siirtäminen ylös- tai alaspäin skaalaa suoraan uudelleen joka $/tekoäly-työtunti-luvun Osassa C sille riville — nämä ovat tämän työkirjan yksittäisenä tärkeimpänä muokattavana syötteenä. Korvaa ne omalla organisaatiosi havaituilla token-lokeilla, jos sinulla on niitä; yllä olevat luvut ovat havainnollistavia kaistoja, ei mitattuja mediaaneja millekään tietylle tuotteelle tai yritykselle.

### B.1 Miksi vyöhyke 4 on ilmoitettu "1 000 000-12 000 000+"-muodossa, ei tiukempana vaihteluvälinä

**LÄHDE, OpenAI:n oma itse-raportoitu sisäinen telemetria (lähderekisteri klusteri J — käsittele yrityksen omana itseraportointina, ei itsenäisesti auditoituna):**

- Codex saavutti **99,8 %** OpenAI:n omasta viikoittaisesta sisäisestä tuotostokenimäärästä (verrattuna muuhun kuin Codex-chat-käyttöön) vuoden 2026 puoliväliin mennessä.
- Toukokuuhun 2026 mennessä **70,2 %** otannassa olleista yksittäisistä Codex-käyttäjistä oli tehnyt vähintään yhden pyynnön, jonka OpenAI itse arvioi yli **1 ihmistyötunnin** vastaavaksi työksi; **25,6 %** oli tehnyt vähintään yhden yli **8 ihmistyötunnin** arvioidun pyynnön.
- Kesäkuuhun 2026 mennessä käyttäjät **99. persentiilissä** tuottivat säännöllisesti **yli 60 tuntia Codex-agentin vuoroaikaa yhtä kalenteripäivää kohti**, jaettuna useiden rinnakkaisten agenttien yli.

**Korjattu 2026-08-13 — alla oleva päättely oli virheellinen ja on poistettu.** Tämän kappaleen aiempi versio väitti, että ">60 agentti-vuorotuntia per kalenteripäivä" on todiste siitä, että käyttäjä tuottaa 60 agenttituntia *yhden ihmisen kelloaikatunnin sisällä*. Tämä ei seuraa: kalenteripäivä sisältää 24 kelloaikatuntia, niin 60 agentti-vuorotuntia levitettynä koko päivän yli voitaisiin tuottaa yhtä hyvin vain ~2,5 agentilla, jotka toimivat jatkuvasti koko päivän — se ei itsessään kerro mitään siitä, kuinka monta agenttia toimii *samanaikaisesti minkä tahansa yksittäisen tunnin sisällä*. OpenAI:n tilasto säilytetään alla vain sen todellisen sisällön osalta, ei virheellisen ekstrapolaation:

**Mitä tämä tilasto todella tukee [LÄHDE, OpenAI:n itseraportti]:** se on vahvaa todistetta jatkuvasta, raskaasta *rinnakkaisesta* käytöstä 99. persentiilin käyttäjien keskuudessa, koko päivän yli aggregoituna, ja pitkästä, nopeasti kasvavasta pyyntökeston hännästä (8h+ osuus pyynnöistä raportoidusti kasvoi "+1131%" noin kuuden kuukauden aikana saman raportin mukaan). Se **ei** itsessään määritä tiettyä tokenia-per-ihmisen-kelloaikatunti-lukua vyöhykkeelle 4.

**Miksi vyöhyke 4 pysyy ankkuroituna avoimeksi "1 000 000–12 000 000+"-arvoksi [SKENAARIO-OLETUS, ei LASKELMA yllä olevasta tilastosta]:** yläraja on havainnollistava, valittuna riittävän leveäksi mahtumaan todella raskaisiin rinnakkaisorkestroinnin skenaarioihin implikoimatta väärää tarkkuutta — sitä ei ole laskettu 60-tuntia/päivä-luvusta. Lukijan, jolla on todellisia token-kulutuslokeja tai rinnakkaisuustietoja tietylle raskaan orkestroinnin työnkululle, pitäisi korvata tämä vyöhyke suoraan mitatulla luvulla tämän havainnollistavan ylärajan sijaan (ks. Osan G suositus käyttää omia mitattuja token-lokeja).

**Tärkeät soveltamisalavaraukset, todettuna suoraan:**
- Nämä luvut kuvaavat OpenAI:n omaa sisäistä työntekijäkäyttöä sen omalle koodausagenttituotteelle (Codex). Ne ovat todistetta siitä, että raskaan moniagenttiorkestroinnin käyttö on olemassa ja voi olla äärimmäistä — ne **eivät** ole yleinen populaatiotilasto, eivät itsenäisesti auditoituja kolmannen osapuolen toimesta, eivätkä välttämättä edustavia käytöstä muissa organisaatioissa, muissa työkaluissa tai muussa kuin koodaustyössä.
- Erikseen väitettyä "NVIDIA:n viitteellistä agenttimaista työkuormaa 32 000 syöte + 8 000 tuloste tokenia per vuoro" **ei löytynyt missään** (lähderekisteri klusteri J), ja sitä nimenomaisesti **ei käytetä** syötteenä tämän työkirjan vyöhykkeille.

### B.2 Orkestrointi ei luo eri tyyppistä tuntia — se luo useita työtunteja rinnakkain

Vyöhykkeen 4 korkea tokenimäärä tulee kokonaan siitä, *kuinka monta agenttia on käynnissä kerralla*, ei siitä, että yksittäinen agentti prosessoisi tokeneita eri nopeudella kuin vyöhykkeet 1–3. Tämä kannattaa esittää omana tiiviinä taulukkonaan, koska se on helppo hukata yhden "tokenia/tunti"-luvun sisään:

| Työkapasiteetti | Tekoäly | Ihminen |
|---|---|---|
| 1 työtunti | 1 tekoälyagentti × 1 tunti = 1 agenttitunti | 1 henkilö × 1 tunti = 1 ihmistunti |
| 10-agentin/hengen tiimin tunti | 10 tekoälyagenttia × 1 tunti = 10 agenttituntia | 10 henkilöä × 1 tunti = 10 ihmistuntia |
| 1 työpäivä | 1 agentti × 8 tuntia = 8 agenttituntia | 1 henkilö × 8 tuntia = 8 ihmistuntia |
| 10-agentin/hengen tiimin päivä | 10 agenttia × 8 tuntia = 80 agenttituntia | 10 henkilöä × 8 tuntia = 80 ihmistuntia |

**Tiimin työkapasiteetti on tekijät × tunnit, molemmilla puolilla vertailua, poikkeuksetta.** 10-agentin orkestrointitunti ei ole "yksi agentti työskentelemässä kymmenen kertaa nopeammin" enempää kuin 10-hengen tiimin tunti on "yksi henkilö työskentelemässä kymmenen kertaa nopeammin" — molemmat ovat kymmenen itsenäistä työkapasiteettiyksikköä sovellettuna samaan yhteen kelloaikatuntiin. Vyöhykkeen 4:n 1 000 000–12 000 000+ tokenia/tunti -vaihteluväli yllä olevassa taulukossa on tämä sama aritmetiikka tiivistettynä yhdeksi per-kelloaikatunti-luvuksi kustannusmallinnuksen käytännöllisyyden vuoksi (Osa C tarvitsee yhden luvun per vyöhyke kertoakseen sen $/M-tokenia-luvun kanssa) — se on mallinnuksen käytännöllisyys infrastruktuurikysynnän arvioimiseksi, ei väite, että raskas orkestrointi olisi laadullisesti eri tyyppinen tunti kuin vyöhykkeet 1–3. Vyöhyke-4-luvun lukeminen "yhtenä erittäin nopeana tuntina" sen sijaan, että se luettaisiin "monena rinnakkaisena tavallisena tuntina", on helpoin tapa lukea tätä taulukkoa väärin.

---

## Osa C — $/tekoäly-työtunti tuotantotasojen yli

Tämä on ydintuotos: Osan B käyttöintensiteettitikapuun risteyttäminen Julkaisuresurssi #7:n jo johdettujen tuotantokustannustasojen kanssa, matala/keski/korkea-skenaarioilla molemmilla akseleilla.

**Kaava (LASKELMA, käytetty jokaisessa alla olevassa solussa):**

```
$/AI-working-hour = (tokens_per_working_hour / 1 000 000) × ($/million_tokens_at_that_production_tier)
```

Lattia = parhaan tapauksen käyttövyöhykkeen tokenia/tunti (Matala) × parhaan tapauksen (halvin) tuotantotason $/M tokenia.
Keski = keskitapauksen tokenia/tunti (Keski) × keskitapauksen tuotantotason $/M tokenia.
Katto = huonoimman tapauksen käyttövyöhykkeen tokenia/tunti (Korkea) × huonoimman tapauksen (kalleimman) tuotantotason $/M tokenia.
Tämä yhdistää tarkoituksella "paras-parhaan-kanssa" ja "huonoin-huonoimman-kanssa" rajaamaan uskottavan vaihteluvälin — se ei väitä, että paras käyttö aina osuisi yhteen parhaan tuotantotalouden kanssa todellisuudessa; käsittele lattia/katto havainnollistavana haarukointina, ei yhteistodennäköisyysennusteena.

### C.0 Tuotantotason $/miljoona-tokenia-syötteet (siirretty suoraan Julkaisuresurssi #7:stä — ei johdettu uudelleen tässä)

| Tuotantotaso | Matala (paras tapaus) $/M tok | Keski $/M tok | Korkea (huonoin tapaus) $/M tok | Käyttömenot mukana? | Luottamusluokka (Julkaisuresurssi #7:n mukaan) |
|---|---|---|---|---|---|
| **Kotitalous** — 1× DGX Spark, omistettu tuotanto | 1,71 $ | 3,17 $ | 11,89 $ | Kyllä (havainnollistava varaus) | Korkea laitteiston hinnalle/tehölle (FAKTA); läpimenoteho on FAKTA-yhteisövertailuarvo; käyttöaste on OLETUS |
| **Osuustoiminnallinen** — 10× DGX Spark, 50 jäsentä, omistettu tuotanto | 1,99 $ | 3,20 $ | 7,62 $ | Kyllä (OLETUS-hallinto-/verkkokaista) | Korkea laitteistolle; hallinto-/yleiskustannusrivi on OLETUS |
| **Ammattimainen** — 1× HGX B300 (8-GPU) -solmu, omistettu tuotanto | 0,044 $ | 0,064 $ | 0,146 $ | **Ei — vain pääoma+rahoitus+sähkö; ks. Julkaisuresurssi #7 §4.3:n havainnollistava käyttömenoherkkyys, keskitapaus nousee ~0,080 $/M:ään käyttömenojen lisäämisen jälkeen** | Matala-keskitasoinen — capex ja teho ovat OLETUS-paikkamerkkejä (ei julkista hintaa/tehoa löytynyt tälle SKU:lle); läpimenoteho on LASKELMA-skaalausarvio, ei suora vertailuarvo |
| **Hyperskaala/Teollisuus** — 1× GB300 NVL72 -räkki, omistettu tuotanto | 0,091 $ | 0,133 $ | 0,312 $ | Kyllä (OLETUS-käyttömenokaista, 200 $k-1M/vuosi) | Keskitasoinen — räkin spesifikaatiot/teho FAKTA; capex on analyytikkoon ankkuroitu OLETUS, ei virallinen NVIDIA-hinta |
| **Vähittäis-API** — osta markkinoilta, EI omistettua tuotantoa (vain vertailukerros) | 0,90 $ | 9,00 $ | 38,00 $ | ei sovellettavissa (vähittäishinta, ei tuotantokustannuserittely) | FAKTA (Anthropic, Google) / LÄHDE (OpenAI, tekoälyn tiivistämän hakutuloksen kautta — ks. Julkaisuresurssi #7 §7 luottamushuomautukset) |

**Korjattu 2026-08-13:** Ammattimaisen tason yllä olevat luvut sulkevat käyttömenot pois, kun Kotitalous, Osuustoiminnallinen ja Hyperskaala sisällyttävät ne — tämä ei ole omenoita-omenoihin-vertailu. Älä lue Ammattimaista yksinkertaisesti "halvimpana omistetun tuotannon tasona" — osa sen näennäisestä edusta Hyperskaalaan verrattuna on soveltamisala-artefakti, ei puhdas laitteistosukupolvien vaikutus. Ks. Julkaisuresurssi #7 §4.3/§9 täydelle korjaukselle.

**Vähittäis-API-sekoitusmenetelmä (LASKELMA):** joka nimetyn mallin "sekoitettu $/M tokenia" = `0.3 × input_price + 0.7 × output_price` (**OLETUS**: 30% syöte / 70% tuloste tokenisekoitus, havainnollistaen agenttimaista/generointipainotteista työkuormaa lyhyen kysymyksen chat-työkuorman sijaan — chat-painotteinen työkuorma, jossa on enemmän syöte- kuin tulostetokeneita, siirtäisi tämän sekoituksen matalammaksi). Lattia = OpenAI GPT-5.6 Luna sekoitettuna (0,90 $); Keski ≈ OpenAI GPT-5.6 Terra / Google Gemini 3.1 Pro sekoitettuna (molemmat 9,00 $); Katto = Anthropic Claude Fable 5 sekoitettuna (38,00 $). **Kriittinen menetelmämuistutus (kannettu Julkaisuresurssi #7 §1:stä): vähittäis-API-hinnat ovat "osta sähköä verkosta" -vertailukohta jonkun toisen valmiin tokenintuotantokapasiteetin vuokraamiselle — niitä ei koskaan saa käyttää kelvollisena syötteenä omistetun laitteiston hinnoittelulle, ja ne esitetään tässä vain, jotta lukija voi nähdä, miten itseisännöity tuotantokustannus vertautuu eturintaman laboratorion päättelyn vuokraamiseen samalla käyttöintensiteetillä.**

### C.1 Täysi matriisi — $/tekoäly-työtunti (lattia | keski | katto)

| Käyttöintensiteettivyöhyke | Kotitalous | Osuustoiminnallinen | Ammattimainen | Hyperskaala | Vähittäis-API (vain vertailu) |
|---|---|---|---|---|---|
| **1. Chat/neuvonantaja** | 0,0171 $ \| 0,063 $ \| 0,36 $ | 0,0199 $ \| 0,064 $ \| 0,23 $ | 0,00044 $ \| 0,0013 $ \| 0,004 $ | 0,00091 $ \| 0,0027 $ \| 0,009 $ | 0,009 $ \| 0,18 $ \| 1,14 $ |
| **2. Aktiivinen tekoälytyötoveri** | 0,103 $ \| 0,285 $ \| 1,43 $ | 0,119 $ \| 0,288 $ \| 0,91 $ | 0,0026 $ \| 0,0058 $ \| 0,018 $ | 0,0055 $ \| 0,012 $ \| 0,037 $ | 0,054 $ \| 0,81 $ \| 4,56 $ |
| **3. Delegoitu yksittäisagentti** | 0,342 $ \| 1,268 $ \| 7,13 $ | 0,398 $ \| 1,280 $ \| 4,57 $ | 0,0088 $ \| 0,0256 $ \| 0,088 $ | 0,018 $ \| 0,053 $ \| 0,19 $ | 0,18 $ \| 3,60 $ \| 22,80 $ |
| **4. Raskas moniagenttiorkestrointi** | 1,71 $ \| 15,85 $ \| 142,68 $ | 1,99 $ \| 16,00 $ \| 91,44 $ | 0,044 $ \| 0,32 $ \| 1,75 $ | 0,091 $ \| 0,665 $ \| 3,74 $ | 0,90 $ \| 45,00 $ \| 456,00 $ |

`$/tekoäly-työtunti = (tokens/hr ÷ 1 000 000) × ($/M tokenia)` — esim. Hyperskaala, vyöhyke 3, keski: `(400 000 ÷ 1 000 000) × 0,133 $ = 0,0532 $`, pyöristettynä 0,053 $:ksi yllä.

### C.2 Matriisin lukeminen — mitä vaihteluväli tarkoittaa

**TULKINTA.**

1. **Eri tuotantotasoilla samalla käyttövyöhykkeellä** vaihteluväli on valtava — "delegoidun yksittäisagentin" (keskitapaus) kohdalla Hyperskaala (0,053 $/hr) on karkeasti **24 kertaa halvempi** kuin Kotitalous (1,268 $/hr) ja karkeasti **68 kertaa halvempi** kuin Vähittäis-API-vertailu (3,60 $/hr). Tämä on sama johtopäätös kuin Julkaisuresurssi #7:n tasovertailu, ilmaistuna nyt per työtunti sen sijaan, että se olisi per miljoona tokenia — mittakaavaedut omistetussa tuotantoinfrastruktuurissa kääntyvät suoraan mittakaavaeduiksi tekoäly-työtunnin kustannuksessa.
2. **Eri käyttövyöhykkeillä samalla tuotantotasolla** vaihteluväli on myös suuri rakenteellisesti — siirtyminen "chat/neuvonantajasta" "raskaaseen moniagenttiorkestrointiin" kertoo $/tekoäly-työtunnin karkeasti 100-250-kertaiseksi joka tasolla, koska käyttövyöhykkeet itsessään kattavat kaksi-plus suuruusluokkaa tokenia/tunti (Osa B). Tämä ei ole väite, että raskas orkestrointi olisi "huonompi arvo" — se yksinkertaisesti kuluttaa paljon enemmän raakaa työkapasiteettia per kelloaikatunti, määritelmän mukaan.
3. **Kotitalous- ja Osuustoiminnallinen taso ovat, joka käyttövyöhykkeellä, kalliimpia per tekoäly-työtunti kuin Vähittäis-API sen lattiassa (Luna), mutta halvempia kuin Vähittäis-API sen katossa (Fable 5).** Tämä on merkityksellistä paperin omistusväitteelle: itsehostaus kuluttajaluokan laitteistolla (DGX Spark) ei ole automaattisesti halvin per-token-vaihtoehto — sen olemassaolon perustelu lepää datan hallinnalla, räätälöinnillä ja riippumattomuudella tarjoajasta (paperin muualla esittämän omistusarkkitehtuuriväitteen mukaan), ei sillä, että se olisi matalin $/token-polku. Ammattimainen ja Hyperskaalataso sen sijaan alittavat jopa halvimman vähittäis-API-lattian 1-2 suuruusluokkaa — mutta näiden tasojen vaatima pääoma ja mittakaava ylittävät yksilön tai pienen osuuskunnan mahdollisuudet kaukana, niiden capex-/tehosyötteet kantavat huomattavasti matalampaa luottamusta (ks. C.0-taulukko) kuin Kotitalous-/Osuustoiminnallinen- tai Vähittäis-rivit, ja **Ammattimaisen oma luku erityisesti sulkee käyttömenot pois, kun Hyperskaalan luku sisällyttää ne (ks. C.0-huomautus, korjattu 2026-08-13) — näitä kahta ei pitäisi verrata suoraan toisiinsa huomioimatta tätä soveltamisalaeroa.**
4. **Mikään tässä matriisissa ei kerro mitään siitä, oliko suoritettu työ tekemisen arvoista.** Ks. Osa D.

---

## Osa D — Tulosten/arvon rajanveto (toistettu nimenomaisesti, ei kertaalleen etukäteistekstissä)

**TULKINTA, toistettu paperin vaaditun kehyksen mukaisesti.** Työkapasiteetti → työ → tulos → arvo on ketju, ja viimeinen askel ei koskaan ole mekaanisesti aiempien askelten määräämä. $/tekoäly-työtunti-luku Osassa C kertoo, mitä maksaa *tuottaa annettu tekoälytuotoksen nopeus* annetulla tuotantotasolla — se ei kerro mitään siitä, oliko tuotos oikea, hyödyllinen, hyvin kohdistettu tai nettopositiivinen. Arvo voi olla positiivinen, nolla tai negatiivinen riippumatta siitä, miten halvasti tai kalliisti taustalla olevat tokenit tuotettiin. Raskas moniagenttiorkestrointitunti hintaan 0,665 $ (Hyperskaala, keskitapaus), joka tuottaa varmuudella-väärää koodia, huonosti kohdistettua asiakastavoitusta tai uskottavan kuuloista mutta virheellistä analyysiä, ei ole "halpaa hyvää työtä" — se on halpaa työtä, jonka arvo on määrittämätön tai negatiivinen, ja runsas halpa työkapasiteetti lisää, ei vähennä, ihmisen harkinnan merkitystä siitä, *mihin* tätä kapasiteettia ohjataan. Tämä rajanveto koskee joka lukua Osassa C ja joka lukua Osassa E; se ei ole etukäteistekstiin rajattu varauslauseke.

Tämä työkirja, ja paperi, jonka osa se on, **ei ole sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa.** Joka skenaario on muokattava havainnollistus, rakennettu ilmoitetuille, näkyville oletuksille — ei ennuste tai suositus siitä, mikä taso, tarjoaja tai käyttökuvio pitäisi valita.

---

## Osa E — Ihmistyön vertailutaulukko

**Tarkoitus ja soveltamisala.** Tämä taulukko on olemassa tehdäkseen näkyväksi *mikä on ja mikä ei ole merkityksellisesti vertailukelpoista* ihmisen työtuntien ja tekoäly-työtuntien välillä, käyttäen samaa näkyvän oletuksen kurinalaisuutta kuin muualla tässä työkirjassa. Se tarkoituksella **ei** tuota yhtä "tekoäly on X ihmistyötunnin arvoinen" -muunnoskerrointa faktana — mikä tahansa tällainen kerroin alla esitetään SKENAARIO-OLETUKSENA tai LASKELMANA nimetystä, muokattavasta oletuksesta, ei koskaan vakiintuneena yhtäläisyytenä. Ulottuvuudet, jotka on merkitty nimenomaisesti "ei vertailukelpoiseksi", eivät ole täytettä — ne ovat paperin omia vaadittuja varauksia työkuormasta, laadusta, luotettavuudesta, valvonnasta ja kontekstista, pidettynä näkyvinä sen sijaan, että ne hiljaisesti taipuisivat yhdeksi luvuksi.

### E.1 Ulottuvuudet, jotka OVAT kohtuullisesti vertailukelpoisia (ilmoitetulla menetelmällä)

| Ulottuvuus | Miten tekoälypuoli mitataan | Miten ihmispuoli mitataan | Vertailukelpoisuuden perusta | Luokka |
|---|---|---|---|---|
| **Määritellyn, mekaanisen alitehtävän raaka läpimenoteho** (esim. kiinteän pituisen tallenteen litteroiminen, kiinteän asiakirjan ensimmäisen luonnoksen laatiminen, kiinteän samankaltaisten luokitusten erän ajaminen) | Tokeneita prosessoitu/tuotettu kelloaikatuntia kohti, Osasta B/C | Tehtäväaikatutkimukset tai pyytäjän oma arvio siitä, "kuinka kauan tämä veisi pätevältä henkilöltä", joka itsessään on OpenAI:n oma sisäinen menetelmä sen "ihmistyötunti-vastaavuus" -telemetrialle (**LÄHDE**, lähderekisteri klusteri J) — ei itsenäisesti validoitu työtaloustieteen standardi | Molemmat puolet voidaan ajastaa samaa kiinteää, kapea-alaisesti rajattua toimitusta vasten | **LASKELMA** (kun molemmat puolet todella mitataan samaa tehtävää vasten) |
| **Yhden lisäläpimenoyksikön marginaalikustannus, tehtävätyyppi vakiona** | $/tekoäly-työtunti annetulla tuotantotasolla (Osa C) — omistettu tuotantokustannus pariutuu ihmisen työntekijän kokonaiskustannuksen kanssa; vähittäis-API-hinta pariutuu ihmisen laskutettavan tuntihinnan kanssa (**OLETUS** — ks. E.2) | Työntekijän kokonaiskustannus työnantajalle (täysin katettu — palkka/edut/yleiskustannus) sisäiselle palkkaukselle, tai laskutettava tuntihinta ulkoa ostetulle työntekijälle (**OLETUS** — ks. E.2) | Molemmat ovat kustannuslukuja samassa valuutassa, samalle nimelliselle tehtäväluokalle, pidettynä täsmäävinä sisäinen/sisäinen- tai ulkoinen/ulkoinen-pareina | **LASKELMA** |
| **Kapasiteetin saatavuus/joustavuus** | Lisää tekoäly-työtunteja voidaan tyypillisesti lisätä maksamalla enemmästä laskennasta tai enemmästä API-kutsusta, todellisten laitteisto-/tarjoajakapasiteettirajojen alaisena (ks. Osan C tuotantotason katot) | Lisää ihmistyötunteja vaatii rekrytointia, koulutusta tai ylitöitä, todellisten työmarkkina- ja kalenteriaikarajojen alaisena | Molemmat ovat todellisia, havaittavia kapasiteetin laajentamisen rajoitteita, vaikka niiden muodot eroavat jyrkästi | **TULKINTA** |

### E.2 Havainnollistava $/tunti-vertailu — ihmistyön kaistat vs. tekoäly-työtunnin kaistat (SKENAARIO-OLETUS ihmispuolella; ei luettava markkinapalkkakyselynä)

**Työnantaja-/laskutuseroittelu, todettuna nimenomaisesti.** Ihmistyön kustannus ei ole yksi luku — se riippuu siitä, tehdäänkö työ jonkun organisaation suoraan palkkaaman henkilön toimesta (täysin katettu sisäinen kustannus: palkka + edut + yleiskustannus) tai ostetaanko se ulkoiselta osapuolelta (toimisto, alihankkija, konsultointiyritys tai freelance-markkinapaikka, jonka laskutushinta sisältää *sen omat* katteensa, yleiskustannuksensa, ei-laskutettavan ajan ja liiketoimintariskin sen oman työntekijän maksamisen päälle). Tämä on täsmälleen sama rakenteellinen ero, jonka Osa C piirtää tekoälypuolella **omistetun tuotantokustannuksen** ja **vähittäis-API-hinnan** välille — ja kaksi paria linjautuvat:

| | Sisäinen/omistettu | Ulkoinen/ostettu |
|---|---|---|
| **Tekoäly** | Omistettu tuotantokustannus (Kotitalous/Osuustoiminnallinen/Ammattimainen/Hyperskaala, Osa C) | Vähittäis-API-hinta (osta markkinoilta, Osa C) |
| **Ihminen** | Työntekijän kokonaiskustannus työnantajalle, täysin katettu (tämä osa) | Laskutettava tuntihinta (tämä osa) |

Omistetun tekoälyn kustannuksen vertaaminen ihmisen *laskutettavaan* hintaan — tai vähittäis-API-hinnan vertaaminen ihmisen työnantajakustannukseen — sekoittaa kaksi sisäinen/ulkoinen-kerrosta täsmälleen samalla tavalla kuin paperi varoittaa omistetun tuotantokustannuksen sekoittamisesta vähittäis-API-hintaan pelkästään tekoälypuolella (Osa C.0, "kriittinen menetelmämuistutus"). Alla oleva vertailu pitää siis molemmat parit erillään läpi taulukon, ei koskaan sekoitettuna yhdeksi "tekoäly vs. ihminen" -luvuksi.

**Ihmispuolen OLETUS, nimenomaisesti muokattava, EI lähdetetty mistään tietystä työmarkkinadatajoukosta tässä työkirjassa:**

| Ihmistyön taso | Työntekijän kokonaiskustannus työnantajalle (täysin katettu — palkka + edut + yleiskustannus, sisäinen palkkaus) | Ihmisen laskutettava/ulkoa ostettu työkapasiteetti (toimisto, alihankkija, konsultointiyritys tai freelance-markkinapaikan hinta) | Luokka |
|---|---|---|---|
| Aloitustason/rutiinitehtävätyö | 15–35 $/hr | 40–90 $/hr | **OLETUS** — korvaa omilla paikallisilla, roolikohtaisilla luvuillasi; nämä eivät ole palkka-/hintakyselylukuja |
| Ammattitaitoinen ammattilainen (esim. keskitason analyytikko, kehittäjä, erikoisasiantuntija) | 50–150 $/hr | 100–350 $/hr | **OLETUS** |
| Vanhempi erikoisasiantuntija/asiantuntijakonsultti | 150–500 $+/h | 300–1 000 $+/h | **OLETUS** |

**Miksi laskutettava sarake on korkeampi, ilmaistuna oletuksena, ei todistettuna suhteena:** ulkoisen tarjoajan laskutettavan hinnan täytyy kattaa sama palkka-/etu-/yleiskustannus, jonka sen oma työntekijä maksaa sille, plus sen oma kate, myynti-/asiakashallintayleiskustannus, penkkiaika toimeksiantojen välillä ja vaihtelevan kysynnän riskipreemio — sama logiikka, jota Osa C.0 käyttää selittämään, miksi vähittäis-API-hinta sijoittuu omistetun tuotantokustannuksen yläpuolelle. Tässä esitetty havainnollistava ~2-3-kertainen kerroin on **SKENAARIO-OLETUS** vain suuntaa antavaksi — todelliset laskutushinnat vaihtelevat valtavasti markkinan, erikoistumisen ja sopimusrakenteen mukaan, ja ne pitäisi korvata omilla tarjouksillasi ennen tämän taulukon käyttämistä mihinkään todelliseen päätökseen.

| Käyttöintensiteettivyöhyke | Omistettu tekoäly, keskitapaus (Hyperskaala, halvin omistetun tuotannon taso Osasta C) | Vähittäistekoäly, keskitapaus (osta markkinoilta, Osa C) | vs. Työntekijän kokonaiskustannus työnantajalle — aloitustaso (15–35 $/hr) | vs. Työntekijän kokonaiskustannus työnantajalle — ammattitaitoinen ammattilainen (50–150 $/hr) | vs. Ihmisen laskutettava hinta — aloitustaso (40–90 $/hr) | vs. Ihmisen laskutettava hinta — ammattitaitoinen ammattilainen (100–350 $/hr) |
|---|---|---|---|---|---|---|
| 1. Chat/neuvonantaja | 0,0027 $ | 0,18 $ | Kaukana alapuolella | Kaukana alapuolella | Kaukana alapuolella | Kaukana alapuolella |
| 2. Aktiivinen tekoälytyötoveri | 0,012 $ | 0,81 $ | Alapuolella | Alapuolella | Alapuolella | Alapuolella |
| 3. Delegoitu yksittäisagentti | 0,053 $ | 3,60 $ | Alapuolella | Alapuolella | Alapuolella | Alapuolella |
| 4. Raskas moniagenttiorkestrointi | 0,665 $ | 45,00 $ | Omistettu tekoäly edelleen alapuolella; Vähittäistekoäly nyt sisällä/yläpuolella ihmisen työnantajakustannuksen ammattitaitoisen ammattilaisen kaistalla | Omistettu tekoäly edelleen alapuolella; Vähittäistekoäly nyt sisällä/yläpuolella | Omistettu tekoäly edelleen alapuolella; Vähittäistekoäly nyt laskutettavan ammattitaitoisen ammattilaisen kaistan sisällä | Omistettu tekoäly edelleen alapuolella; Vähittäistekoälyn katto (456 $/hr, Osasta C) ylittää jopa laskutettavan vanhemman erikoisasiantuntijan kaistan |

**TULKINTA, esitettynä huolellisesti:** siistein omenoita-omenoihin-pariutus on **omistettu tekoäly vs. ihmisen työnantajakustannus** (molemmat ovat sisäisiä, täysin katettuja tuotantokustannuksia) ja **vähittäistekoäly vs. ihmisen laskutettava kustannus** (molemmat ovat sitä, mitä maksat ulkoiselle osapuolelle valmiista, käyttövalmiista kapasiteetista, sisältäen sen katteen). Lue diagonaalisesti — omistettua tekoälyä laskutettavia hintoja vasten, tai vähittäistekoälyä työnantajakustannusta vasten — ja vertailu ylittää sisäinen/ulkoinen-rajan hiljaa sitä sanomatta. Halvimmilla omistetun tuotannon tasoilla $/tekoäly-työtunti on dramaattisesti minkä tahansa tässä esitetyn ihmisen työnantajakustannuskaistan alapuolella, joka käyttöintensiteetillä — tämä on todellinen, todennettava aritmeettinen vertailu *tokenintuotannon kustannuksesta* vs. *ihmisen ajan kustannuksesta*, pidettynä oikeassa sisäinen/sisäinen- tai ulkoinen/ulkoinen-pariutuksessa. Se ei nimenomaisesti ole väite, että tekoäly-työtunti ja saman keston ihmistyötunti tuottaisivat vastaavaa, korvattavaa tai yhtä luotettavaa tuotosta — se yhtäläisyys on juuri se, mitä Osa E.3 alla sanoo, ettei sitä voida olettaa. Tämän taulukon vertailu pitäisi lukea "raakan kapasiteetin kustannuksena", ei "vastaavan valmiin tuloksen kustannuksena".

### E.3 Ulottuvuudet, jotka EIVÄT OLE vertailukelpoisia ilman nimenomaista, näkyvää sillanrakennusoletusta — paperin vaaditut varaukset, pidettynä näkyvinä sen sijaan, että ne piilotettaisiin

| Ulottuvuus | Miksi suora tekoälytunti ↔ ihmistunti-vertailu murtuu tässä | Mitä tarvittaisiin sen vertailukelpoiseksi tekemiseksi (ja miksi tämä työkirja ei toimita sitä) | Luokka |
|---|---|---|---|
| **Työkuorman määrittely** | "Yksi tekoäly-työtunti" 5 000 000 tokenia/tunti (vyöhyke 4, keski) ei tee "samanlaista työtä" kuin yksi ihmistunti — se voi edustaa kymmeniä rinnakkaisia, kapea-alaisia, mekaanisia alitehtäviä sen sijaan, että se olisi yksi jatkuva, integroitu, harkintaa vaativa työ. Tokenimäärä mittaa prosessointivolyymia, ei tehtävän kompleksisuutta tai tehtävien määrää. | Tehtäväkohtainen kartoitus (esim. "tämä tietty 500 000-tokenin agenttiajo = tämä tietty 3-tuntinen ihmistehtävä, itsenäisesti ajastettuna") *tietylle* kysymyksessä olevalle työkuormalle — tämä työkirja ei toimita tällaista kartoitusta; OpenAI:n oma "arvioitu ihmistuntien" telemetria (klusteri J) on lähin saatavilla oleva vastine, ja OpenAI itsekään ei julkista arviointimenetelmäänsä todennettavassa yksityiskohdassa. | **VARAUS (pidetty näkyvänä, ei ratkaistu)** |
| **Tuotoksen laatu/oikeellisuus** | Mikään Osassa B tai C ei mittaa, olivatko tuotetut tokenit tarkkoja, sopivasti rajattuja tai käyttötarkoitukseen sopivia. Ihmistyöntekijän tuotos ja tekoälyagentin tuotos "samassa" nimellisessä tehtävässä voivat erota virhesuhteessa, hallusinaatioriskissä ja soveltuvuudessa tavoilla, joita mikään tokenimäärä ei tallenna. | Itsenäisesti auditoitu, tehtäväkohtainen laatu-/virhesuhdevertailuarvo molemmille — tekoälyjärjestelmälle ja vertailtavalle ihmistyövoimalle — identtistä tehtäväjakaumaa vasten — soveltamisalan ulkopuolella tälle työkirjalle; paperin ei pitäisi implikoida, että sellainen olisi olemassa. | **VARAUS (pidetty näkyvänä, ei ratkaistu)** |
| **Luotettavuus/johdonmukaisuus toistetuissa ajoissa** | Ihmisen suoritus ja tekoälyagentin suoritus vaihtelevat molemmat ajosta ajoon, mutta eri syistä (väsymys/taitovaihtelu vs. mallin stokastisuus/kehotesensitiivisyys/vikatilat), eikä tämä työkirja eikä laajempi lähderekisteri sisällä hallittua toistokoetutkimusta, joka vertaisi näitä kahta. | Toistokoetutkimus (esim. tuotoksen laadun vaihtelu N ajon yli samalle tehtävälle, samalle kehotteelle, samalle ihmiselle vs. samalle agenttikonfiguraatiolle) — ei saatavilla lähderekisterissä; älä oleta tekoälyn olevan luotettavampaa tai epäluotettavampaa kuin ihmistyö millään perusteella tästä työkirjasta. | **VARAUS (pidetty näkyvänä, ei ratkaistu)** |
| **Valvonta- ja tarkistustaakka** | Delegoidut ja orkestroidut tekoälyn käyttövyöhykkeet (3-4) olettavat nimenomaisesti "ihminen valvoo yhteiskirjoittamisen sijaan" (Osa B) — mutta valvontaaika itsessään on todellinen kustannus, jota ei lasketa missään Osan C $/tekoäly-työtunti-luvuissa. Ihmistyöntekijän tuntikustannus tyypillisesti sisältää jo jonkin perustason itsetarkistusta; tekoälyagentin valvontakustannus on erillinen, laskematon ihmistuntikerros päälle lisättynä. | Mitattu valvontaaika-per-agenttitunti-suhde, joka vaihtelisi valtavasti tehtäväriskin ja organisaation kypsyyden mukaan (ks. paperin Tekoälyn kypsyyskehys, Neuvo→Yhteistyö→Delegoi→Johda-etenemä) — ei mallinnettu tässä; mikä tahansa kokonaiskustannusvertailu, joka jättää tämän pois, aliarvioi systemaattisesti tekoälyn tuottaman työn todellista kustannusta vyöhykkeillä 3-4. | **VARAUS (pidetty näkyvänä, ei ratkaistu)** |
| **Konteksti ja organisaation tieto** | Paperin "informaatio on tekoälyn käyttöjärjestelmä" -kehyksen mukaan sama malli samalla tokenikustannuksella voi tuottaa hyvin erilaista tehokasta työkapasiteettia riippuen siitä, mitä kontekstia/informaatiota sillä on käytettävissä — ulottuvuus, jolla ei ole vastinetta yksinkertaisessa ihmisen tuntipalkkaluvussa, jossa kertynyt hiljainen tieto hinnoitellaan implisiittisesti senioriteettiin/kokemukseen, mutta ei mitata erikseen. | Kontekstintäydellisyys- tai informaationsaatavuuspisteytysmenetelmä, sovellettuna johdonmukaisesti molemmille — tekoälyjärjestelmälle ja ihmisvertailulle — ei saatavilla; tämä työkirja hinnoittelee vain raakaa token-läpimenoa, nimenomaisesti ei "tekoälyn työkapasiteettia kontekstin vahvistamana tai rajoittamana", jota käsitellään laadullisesti muualla paperissa, ei määrällisesti tässä. | **VARAUS (pidetty näkyvänä, ei ratkaistu)** |

**Vaadittu uudelleentoteamus (paperin ydinperiaatteen mukaan, ei valinnainen tässä):** työkapasiteetti on kyky suorittaa työtä, ei työ itse, eikä sen tulos tai arvo. Joka rivi yllä on muistutus siitä, että $/tunti-vertailu tekoälyn ja ihmistyön välillä on vertailu *raa'an kapasiteetin kustannuksesta*, rajattuna nimetyillä ja näkyvillä varauksilla — ei koskaan vertailu *taatusta vastaavasta tuotetusta arvosta*. Missä paperi tai kuka tahansa lukija haluaa esittää vahvemman väitteen kuin "kapasiteetti maksaa vähemmän", tietty sillanrakennusoletus (tehtäväkartoitus, laatuvertailuarvo, luotettavuustutkimus, valvontasuhde tai kontekstintäydellisyysmittaus) täytyy todeta avoimesti, täsmälleen niin kuin tämä taulukko tekee, sen sijaan, että se taipuisi hiljaa yhdeksi kertoimeksi.

---

## Osa F — Työstetty esimerkki: väitetyn tuottavuusanekdootin muuntaminen tämän työkirjan yksiköiksi (vain menetelmädemonstraatio)

**Tarkoitus:** näyttää, miten todellinen, lähderekisterissä dokumentoitu väite *muunnettaisiin* tämän työkirjan yksiköiksi, ollessaan avoin siitä, mikä on ja mikä ei ole vahvistettu prosessissa — ei väittääkseen tiettyä tuottavuuskerrointa todistettuna.

Sam Altmanin, Y Combinatorin Startup School -päätössessiossa (Chase Center, San Francisco, 26. heinäkuuta 2026), on itsenäisesti vahvistettu (CC BY 4.0 -osallistujamuistiinpanovaraston kautta, ei sanatarkka virallinen transkriptio — lähderekisteri klusteri D) käyttäneen kieltä, joka vastaa "voit nyt tehdä kolmen kuukauden työn seitsemässätoista minuutissa". Tämä on **LÄHTEESEEN KOHDISTETTU LAUSUNTO** — todellinen väite, nimetyn henkilön toimesta, todellisessa tallennetussa tilanteessa — ei itsenäisesti todistettu tuottavuussuhde.

**LASKELMA, vain menetelmä, nimenomaisesti ei hyväksyen taustalla olevaa "kolme kuukautta = 17 minuuttia" -väitettä todeksi:**

```
Jos "kolmen kuukauden työ" ≈ 3 kuukautta × ~160 työtuntia/kuukausi (OLETUS, vakiokokoinen kokoaikainen kuukausi) ≈ 480 ihmistyötuntia,
ja tämä puristettaisiin 17 minuuttiin = 0,283 tuntia tekoäly-työaikaa,
implikoitu suhde = 480 / 0,283 ≈ 1 696-kertainen
```

**Mitä tämä NÄYTTÄÄ ja EI NÄYTÄ:**
- Se **näyttää**, miten vilkas retorinen väite voitaisiin periaatteessa kääntää "ihmistuntien-tiivistetty-per-tekoäly-työtunti"-kertoimeksi, joka on henkeltään verrattavissa Osan E taulukoihin.
- Se **ei näytä**, että tämä kerroin olisi tarkka, että se pätisi mihinkään tiettyyn tehtävätyyppiin, millään tietyllä käyttöintensiteettivyöhykkeellä tai tuotantotasolla Osasta C, tai että "17 minuuttia tekoälyaikaa" vastaisi mitään mitattavaa tokenimäärää tässä työkirjassa — Altmanin lausunto, lähderekisterin mukaan, esiintyy kontekstissa, jossa perusteltiin perustajille *olla ambitiöösimpiä* tekoälyvetoisen tuottavuuden kasvun vuoksi, ei kalibroituna vertailuarvona, ja mitään tokenimäärää tai tehtävän määrittelyä ei liity alkuperäiseen väitteeseen.
- Osan E.3 varausten (työkuorman määrittely, laatu, luotettavuus, valvonta, konteksti) mukaan 1 696-kertaisen tyylistä suhdetta ei pitäisi esittää missään paperin kohdassa validoituna tuottavuuskertoimena — se on sisällytetty tähän ehdottomasti demonstraationa siitä, *miten* retorinen väite muunnetaan tämän työkirjan kehykseksi läpinäkyvästi, merkitsemällä joka käytetty oletus, ei lukuna, jota siteerataan sellaisenaan.

---

## Osa G — Miten ajaa tämä työkirja uudelleen omilla luvuillasi

1. **Muuta Osan B käyttöintensiteettivyöhykkeitä** vastaamaan oman organisaatiosi mitattuja token-lokeja (jos saatavilla) tässä esitettyjen havainnollistavien vyöhykkeiden sijaan.
2. **Vaihda tilalle päivitetyt tuotantotason $/M-tokenia-luvut** Julkaisuresurssi #7:n päivitetystä versiosta, kun laitteistohinnat, sähkön hinnat tai käyttöasteoletukset muuttuvat — tämän työkirjan Osa C -taulukko on kokonaan alavirrassa Julkaisuresurssi #7:stä, ja se pitäisi tuottaa uudelleen aina, kun tuon työkirjan tasoluvut muuttuvat.
3. **Korvaa Osan E.2 ihmisen tuntikustannuskaistat** omilla paikallisilla, roolikohtaisilla luvuillasi molemmille sarakkeille — työnantajakustannuksella (palkka + edut + yleiskustannus + hallintorasite) sisäiselle palkkaukselle, ja laskutettavalla/ulkoa ostetulla hinnalla ostetulle kapasiteetille — tässä esitetyt kaistat ovat havainnollistavia paikkamerkkejä, ei palkka- tai hintakyselyä. Pidä kaksi saraketta erillään; älä keskiarvoista niitä yhdeksi "ihmiskustannus"-luvuksi, samasta syystä kuin Osa C.0 ei koskaan keskiarvoista omistettua tuotantokustannusta vähittäis-API-hinnan kanssa.
4. **Älä poista tai lievennä Osan E.3 varauksia** mukauttaessasi tätä taulukkoa tiettyä väitettä varten — jos haluat esittää tietyn ihmis-tekoäly-vastaavuuden tietylle tehtävälle, lisää uusi rivi omalla, nimetyllä ja lähdetetyllä sillanrakennusoletuksellasi sen sijaan, että poistaisit varauksen siitä, ettei yleistä sellaista ole olemassa.
5. **Säilytä Osan D tulosten/arvon rajanvetokieli** missä tahansa tästä taulukosta johdetussa tai lainatussa versiossa — paperin näyttöstandardin mukaan joka sijoitusteesi- tai skaalausskenaarioluvun täytyy sisältää tämä rajanveto nimenomaisesti, ei vain kertaalleen etukäteistekstissä.

---

## Yhteenvetotaulukko — pikaviite $/tekoäly-työtunti, vain keskitapaus

| Käyttöintensiteettivyöhyke | Kotitalous | Osuustoiminnallinen | Ammattimainen | Hyperskaala | Vähittäis-API |
|---|---|---|---|---|---|
| Chat/neuvonantaja | 0,063 $ | 0,064 $ | 0,0013 $ | 0,0027 $ | 0,18 $ |
| Aktiivinen tekoälytyötoveri | 0,285 $ | 0,288 $ | 0,0058 $ | 0,012 $ | 0,81 $ |
| Delegoitu yksittäisagentti | 1,268 $ | 1,280 $ | 0,0256 $ | 0,053 $ | 3,60 $ |
| Raskas moniagenttiorkestrointi | 15,85 $ | 16,00 $ | 0,320 $ | 0,665 $ | 45,00 $ |

Kaikki keskitapauksen luvut per `$/tekoäly-työtunti = (keski tokens/hr ÷ 1 000 000) × (keski $/M tokenia sillä tasolla)`, tasosyötteet C.0:sta, käyttövyöhykkeet Osasta B. Ks. Osa C.1 täydelle lattia/keski/katto-vaihteluvälille ja Osa D/E tulos-arvo- ja ihmisvertailurajanvedoille, jotka koskevat joka lukua tässä taulukossa poikkeuksetta.
