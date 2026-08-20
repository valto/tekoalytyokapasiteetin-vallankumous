# Visuaalisten resurssien briiffit — Kaaviospesifikaatiot julkaisulle "Miksi tekoälyyn investoidaan biljoonia?"

**Tila:** Kaaviot 1–10 on rakennettu valmiiksi PNG-kuviksi (katso `assets/diagrams/`); alla olevat briiffit pysyvät spesifikaationa, jonka pohjalta kukin rakennettiin, säilytettynä kaikkia varten, jotka muokkaavat tai johtavat niitä uudelleen. **Kaavio 11** ("Kasvun luominen uuden arvon pohjalta", lisätty 2026-08-14, uuden "Tekoälytyökapasiteetista uuteen arvoon" -käsitteellisen sillan mukana) on kirjoittajan oma ennalta olemassa oleva kaavio, toimitettu suoraan ja käytetty sellaisenaan — katso `assets/diagrams/diagram-11-creating-growth-from-new-value.png` (provenienssikehystetty tätä pakettia varten — näyttöluokkatunniste, viittaus, lähdehuomautus ja vakioalatunniste lisätty alkuperäisen kuvan ympärille; kirjoittajan toimittama muokkaamaton alkuperäinen säilytetään sen vierellä tiedostona `diagram-11-creating-growth-from-new-value.jpg`). Sen alla oleva briiffi kuvaa tämän kuvan todellista rakennetta sen sijaan, että se olisi suunnittelijan spesifikaatio rakennettavaksi tyhjästä, koska kuva on jo olemassa.

**Kaikkia kaavioita koskevat säännöt (koskevat kaikkia 11 alla olevaa briiffiä, ei toisteta per briiffi paitsi kun tietty poikkeus on tärkeä):**
- Joka luku, tunniste tai datapiste, joka nostetaan kaavioon, on kannettava samaa näyttöluokkatunnistetta, jota käytetään lähdetekstissä — HAVAITTU FAKTA, LÄHTEESEEN KOHDISTETTU LAUSUNTO, JOHDETTU LASKELMA, SKENAARIO-OLETUS tai TULKINTA. Käytä pientä selitettä (värikoodattua tai ikonikoodattua) tekstialaviitteiden sijaan, missä kaaviossa on tilaa; missä ei ole, numeroitu alaviite, joka viittaa selitelohkoon, on hyväksyttävä.
- Mikään kaavio ei saa asettaa järjestykseen, mitoittaa tai visuaalisesti suosia yhtä kuudesta lukijalinssistä (Yksityishenkilö, PK-yritys/yrittäjä, Rahoitus-/infrastruktuurisijoittaja, Valtio/alue/yhteisö, Tekoälyrakentaja/-operaattori, Kouluttaja/tutkija/toimittaja) toisen yli. Missä linssi esiintyy (Kaaviot 1, 6, 8, 10), käytä neutraalia, järjestämätöntä asettelua (esim. rengasta, ruudukkoa tai aakkosellista/tasalevyistä sarakejakoa) — ei koskaan numeroitua priorisointia, kokogradienttia tai "prioriteetti"-nuolta.
- Mikään kaavio ei saa visuaalisesti kannattaa tai järjestää Huangin, Altmanin ja Zuckerbergin kantoja suhteessa toisiinsa (Kaaviot 1, 6, 10). Missä heidän lausuntonsa esiintyvät yhdessä, käytä yhtäläistä visuaalista painoarvoa (sama laatikon koko, sama typografinen käsittely, neutraali sijoittelu — esim. kolme rinnakkaista sarakettä, ei hierarkiaa).
- Joka kaavio, joka koskettaa kustannus-, hinta-, rahoitus- tai skenaariolukua (Kaaviot 2, 3, 8, 9), on kannettava näkyvä "SKENAARIO-OLETUS — muokattava havainnollistus, ei ennuste; ei sijoitus-/oikeudellista/vero-/hankinta-/politiikkaneuvontaa" -rajatunniste, raportin vaatimuksen mukaisesti, että tämä raja esiintyy joka mittakaava-/investointipainotteisessa osassa, ei vain kerran alkusanoissa.
- Mikään kaavio ei saa esittää avoimen painotuksen/osuustoiminnallista/hajautettua omistusta ylivertaisena keskitettyyn/omistusoikeudelliseen omistukseen verrattuna, tai päinvastoin (Kaaviot 6, 7, 8). Kompromissikaaviot on näytettävä hyödyt ja kustannukset molemmilla puolilla.
- Missä luku on merkitty VAHVISTAMATTOMAKSI lähdetekstissä (esim. "2,8M tokenia/sek/MW," NVIDIAn "32K/8K-viitetyökuorma"), sitä EI SAA näyttää missään kaaviossa vahvistettuna — se on joko jätettävä kokonaan pois tai näytettävä yliviivattuna/harmaana "VAHVISTAMATON — ei käytetty" -tunnisteella, jos sen poissulkeminen itsessään tarvitsee selityksen. Huomaa: "0,123 dollaria/M tokenia" korjattiin VAHVISTETUKSI 2026-08-13 (suoraan NVIDIAn omalla sivustolla) ja voi nyt esiintyä kaavioissa, mutta vain kun se on nimenomaisesti rajattu 72-GPU:n GB300 NVL72 -räkkitasolle — ei koskaan sovellettuna työasemaan tai pöytätietokoneluokan laitteeseen.
- Vakioalatunniste joka kaaviossa: "Julkaistu CC BY 4.0 -lisenssillä. Ehdotettu viittaustapa: Tutkimussynteesi ja mallinnus: Valto Loikkanen, tekoälyn avustuksella." plus raportin faktojen aikarajauksen päivämäärä, 2026-08-13.

---

## Kaavio 1 — Päästä päähän -työkapasiteettiketju

**Ehdotettu tyyppi:** Horisontaalinen virtaus-/prosessikaavio ("muuntoketju"), 10 yhdistettyä solmua, alla toinen rinnakkainen haara fyysiselle/humanoidivariantille.

**Mitä se näyttää:** Raportin ydin analyyttinen ketju, ilmoitettu johdon tiivistelmässä ja toistettuna joka osarajassa: **energia → laitteisto → laskenta → mallit → tokenit → tekoälytyökapasiteetti → digitaalinen työ → tulokset → arvo → toimijuus.** Sen alla, siirrettynä ja visuaalisesti erotettuna (katkoviivayhteys, ei jatkoa samalle nuolelle), rinnakkainen fyysisen työn ketju osista V/VI: **pääoma + energia + ylläpito + käyttöaste + orkestrointi → humanoidin fyysinen työkapasiteetti.**

**Visualisoitu data/osat:** Johdon tiivistelmä (ketjuväite); Osio 15:n 8-kerroksinen taulukko (energia→tulos-läpikäynti, osa II); Osio 25 (arvoa ei määritetä mekaanisesti); Osio 36 (humanoidiketju, osa VI).

**Rakenteelliset vaatimukset:**
- Joka solmu päketjussa on merkitty laatikko; solmujen väliset nuolet on merkitty *muuntokustannuksella/epävarmuudella*, jonka raportti liittää tähän linkkiin (esim. energia→laitteisto-nuoli viittaa Osio 10:n teho/PUE-varaukseen; tokenit→tekoälytyökapasiteetti-nuoli viittaa Osio 16:n käyttöintensiteettivyöhykkeisiin; työkapasiteetti→tulokset-nuoli ja tulokset→arvo-nuoli on erotettava visuaalisesti — esim. eri nuolityyli (pisteviiva, ohuempi tai "?"-glyfi) kuin joka muu nuoli ketjussa — kantaakseen raportin yksittäisen useimmin toistetun varoituksen: **"arvo voi olla positiivinen, nolla tai negatiivinen; sitä ei määritä mekaanisesti mikään sitä edeltävä."** Tämä on se yksi visuaalinen painotuspiste, jonka EI PITÄISI olla neutraali — se on raportin oma ilmoitettu teesi, ei arvottava tuomio, jonka tämä kaavio lisää.
- Pieni sisäkkäinen laatikko tai huomautus "tokenit"-solmussa tulisi todeta: "Token mittaa tekoälytyökapasiteettia, ei arvoa — katso Osio 14."
- Fyysisen kapasiteetin haaran on kannettava omaa rajahuomautustaan: "Kapeampi, aikaisemmassa vaiheessa, epävarmempi kuin digitaalinen ketju — Osio 36 soveltamisalailmoitus."
- Ei lisätä "arvo"-lukua, dollarimerkkiä tai valmistumistilaa ketjun loppuun — ketju päättyy "toimijuuteen", kuvattuna osissa I/VII avoimena, ei ratkaistuna.

**Näyttöluokkamerkinnät:** Itse ketju on [TULKINTA] — kirjoittajan oma jäsentävä kehys, ilmoitettu sellaiseksi Menetelmät-osiossa ja johdon tiivistelmässä. Merkitse koko kaavio vastaavasti kulmatunnisteella: "Jäsentävä kehys — TULKINTA, Menetelmät §3.1 mukaisesti."

---

## Kaavio 2 — Energiasta tokeniin -pino ja kustannusvesiputous

**Ehdotettu tyyppi:** Vesiputous-/pinottu palkkikaavio (pystysuora), 8 palkkia vasemmalta oikealle, kukin palkki näyttää kumulatiivisen kustannuksen, jonka tämä kerros lisää, ja rinnakkainen pieni monikertaversio näyttää saman vesiputouksen 3 rahoitusajalla.

**Mitä se näyttää:** Osa II:n vaadittu taloudellisten kerrosten erottelu, konkreettisimmin taulukoituna Osio 15:n lasketussa EUR-esimerkissä (Tokenitehtaan skenaariotyökirja) ja toistettuna yleisenä sääntönä Osio 12:ssa: raaka energiakustannus → laitteiston poistoihin perustuva tuotantokustannus → rahoitetun omaisuuden kustannus → täysi käyttöinfrastruktuurikustannus → kapasiteetti-/käyttöastekustannus → token-tuotantokustannus → työkuorma-/tekoälytyökapasiteettikustannus → tulos ja arvo (tämä viimeinen palkki tarkoituksellisesti tyhjä/täyttämättömissä — katso alla).

**Visualisoitu data/osat:** Osio 15:n 8-rivinen taulukko (0,154 €/M → 0,580 €/M → 0,688 €/M → 0,794 €/M → 1,435 €/M 50 %:n käyttöasteella → lopullinen €/M-luku → €/h-muunnos → tulos/arvo); Osio 12:n rahoitusajan herkkyystaulukko (3/4/5/7-vuoden ajat, 0,094/0,074/0,063/0,050 dollaria per M tokenia); Osio 10:n räkin teho- ja MLPerf-läpäisykykyluvut fyysisenä perustana ensimmäisille palkeille.

**Rakenteelliset vaatimukset:**
- Palkit 1–7 pinoutuvat kumulatiivisesti (jokaisen palkin yläosa = kertyvä €/M-token- tai $/M-token-summa); palkki 8 ("tulos ja arvo") on renderöitävä **tyhjänä/viivoitettuna/kysymysmerkillä varustettuna** segmenttinä, ei korkeutta omaavana palkkina — kuvatekstillä: "Ei mekaanisesti johdettu kerroksista 1–7 — Osio 15, rivi 8."
- Toinen pieni monikertakaista pääputouksen alla näyttää samat kerrokset 2–3 uudelleenlaskettuna 3-vuoden / 5-vuoden / 7-vuoden rahoitusajoilla (Osio 12:n taulukko), osoittaen että pidemmät ajat alentavat kustannusta per token, mutta kantaen parillisen merkinnän: "vaihtaa alemman kustannuksen per token pidempään lukitukseen nykyisen laitteistosukupolven kanssa — Osio 11/12."
- Joka palkki on merkitty yksitellen [LASKELMA]-tunnisteella paitsi palkki 1 (joka lepää [OLETUS]-sähkön hinnalla) ja palkki 8 (merkitsemätön/[TULKINTA] vain, koska sitä ei nimenomaisesti lasketa).
- Sisällytä huomautuslaatikko, joka erottaa **omistetun tuotantokustannuksen** (koko tämä vesiputous) **vähittäis-API-hinnasta** (yksittäinen viiteviiva tai merkki päällekkäisenä ylhäällä, esim. "2–50 dollaria/M tokenia vähittäisvertailuarvo, Osio 14 taulukko" — renderöitynä horisontaalisena viiteviivana, joka kulkee koko vesiputouksen yli, EI toisena pinottuna segmenttinä, visuaalisesti vahvistaakseen Osio 3.2:n säännön, että näitä kahta ei koskaan yhdistetä yhdeksi sarakkeeksi).

**Näyttöluokkamerkinnät:** Täysi selite vaaditaan (5 luokkaa); tämä kaavio käyttää vähintään 4:ää 5:stä (FAKTA laitteisto-/vertailuspesifikaatioille, jotka syöttävät palkkeja 1–2, OLETUS sähkö-/rahoitussyötteille, LASKELMA joka palkin korkeudelle, TULKINTA palkki-8-huomautukselle).

---

## Kaavio 3 — Tokenista työkapasiteetti-intensiteettitikapuuhun

**Ehdotettu tyyppi:** Logaritminen horisontaalinen tikapuu-/hakasulkukaavio (tokenia/tunti logaritmisella x-akselilla), 4 käyttöintensiteettivyöhykettä horisontaalisina hakasulkupalkkeina, ristiviitattuna pieneen matriisitaulukkoon alla, joka näyttää $/tekoäly-työtunti tuotantotasoittain.

**Mitä se näyttää:** Osio 16:n 4-vyöhykkeinen käyttöintensiteettitikapuu (chat/neuvonantaja, aktiivinen kollega, delegoitu yksittäisagentti, raskas moniagenttiorkestrointi) ja Osio 17:n ristiintaulukointi näistä vyöhykkeistä osien II/III tuotantotasoja vastaan tuottaakseen $/tekoäly-työtunti.

**Visualisoitu data/osat:** Osio 16:n taulukko (tokenia/tunti Matala–Keski–Korkea per vyöhyke, kaikki merkitty OLETUS); Osio 17:n täysi matriisitaulukko (Kotitalous/Osuustoiminnallinen/Hyperskaala/Vähittäis-API-Luna-lattia/Vähittäis-API-keski/Vähittäis-API-Fable-katto × 4 vyöhykettä); OpenAI Codex -telemetriahuomautus (99,8 % viikoittaisista tuotostokeneista, 70,2 %/25,6 % tuntivastaavuustilastot, 60+ tuntia/päivä p99:llä) tukevana merkintänä, joka perustelee vyöhyke 4:n avoimen katon.

**Rakenteelliset vaatimukset:**
- X-akseli: tokenia/tunti, logaritminen asteikko, ulottuen karkeasti 10 000:sta 12 000 000+:aan. Neljä horisontaalista hakasulkupalkkia (yksi per vyöhyke), kukin ulottuen Matala–Korkea-vaihteluväliinsä, Keski-arvo merkittynä. Vyöhyke 4:n palkin on visuaalisesti osoitettava avoimuutta (nuoli tai häivytys oikeassa reunassa, ei kova pysähdys), kuvatekstillä "avoin kattoluku — Osio 16."
- Tikapuun alla pieni lämpökartta-tyylinen matriisi (rivit = tuotantotaso, sarakkeet = vyöhyke) näyttää $/tekoäly-työtunti, käyttäen värin intensiteettiä tai yksinkertaista numeeriruudukkoa — EI yksittäistä "halvin voittaa" -väriasteikkoa, joka implikoi arvoarviota; käytä neutraalia sekventiaalista palettia, joka on avainnettu vain suuruusluokkaan, huomautuksella siitä, että matalampi kustannus ≠ paremp tulos (ristiviite Kaavioon 4/Osioon 25).
- Erillinen, päärakenteesta visuaalisesti erotettu huomautuslaatikko kantaa OpenAI Codex -telemetrialuvut täysin varauksin: "OpenAI:n oma sisäinen, itse raportoitu, tarkastamaton telemetria omista työntekijöistään käyttäen omaa tuotettaan — ei yleistä populaatiotilastoa. LÄHTEESEEN KOHDISTETTU LAUSUNTO."
- Ammattimaisen tason rivi on näytettävä tyhjänä/harmaana huomautuksella "— epävirallinen/ei vahvistettua spesifikaatiota, Osio 17 taulukkohuomautus" sen sijaan, että täytettäisiin millä tahansa luvulla, vastaten alkutekstin omaa nimenomaista tämän sarakkeen poistoa.

**Näyttöluokkamerkinnät:** Vyöhykkeet = [OLETUS]; matriisisolut = [LASKELMA] (kaava: tokenia/h ÷ 1 000 000 × $/M-tokenia); Codex-huomautus = [LÄHDE] nimenomaisella itse-raportoidulla/tarkastamattomalla varaustekstillä näkyvissä itse kaaviossa, ei vain linkitetyssä alaviitteessä.

---

## Kaavio 4 — Ihmisen ja tekoälyn työn arvokertoimet

**Ehdotettu tyyppi:** Kaksiosainen kaavio: (a) säteittäinen pyörä-/radiaalikaavio Osio 18:n 8 vuorovaikuttavasta laatutekijästä, "luotettavuus" ja "tieto" visuaalisesti merkittynä kertovina, ei lisäävinä; (b) kolme rinnakkaista parivertailukorttia (professori/yrittäjä; uusi toimitusjohtaja/veteraanityöntekijä; sijoittaja/myyjä) havainnollistaen Osio 25:n ihmisvertausperustelua, laajennettuna tekoäly-/orkestrointipaneeliin.

**Mitä se näyttää:** Osio 18:n 8-tekijäkehys (kyvykkyys, luotettavuus, aloitteellisuus, harkinta, luovuus, konteksti, työkalut/käyttöliittymä, tieto) ja Osio 25:n ydinväite, että työkapasiteetti ≠ arvo, että orkestrointi moninkertaistaa kapasiteetin, ei arvon, ja että raaka kyvykkyys/älykkyys ei ennusta, kuka tuottaa käyttökelpoista arvoa annetussa tilanteessa.

**Visualisoitu data/osat:** Osio 18 (8 tekijää, luotettavuus/tieto kertoimina); Osio 25 (3 ihmisvertausparia + tekoäly-orkestrointirinnastus); Osio 17 kohta 2 (kustannus-per-vyöhyke-vaihtelu) tukevana huomautuksena, että hinta ja arvo ovat erilliset akselit.

**Rakenteelliset vaatimukset:**
- Osa (a): radiaalinen/pyörä-kaavio 8 merkityllä puolalla (yhtäläinen visuaalinen painoarvo — ei mitoiteta puolia "tärkeyden" mukaan, koska raportti ei aseta 8 tekijää järjestykseen toisiinsa nähden sen lisäksi, että se merkitsee luotettavuuden ja tiedon rakenteellisesti eri lajiksi). Käytä erottuvaa visuaalista käsittelyä (esim. kaksinkertainen rengas tai lihavoitu ääriviiva) vain luotettavuudelle ja tiedolle, kuvatekstillä: "nämä kaksi toimivat kertoimina muille kuudelle — ei lisäetuina, Osio 18."
- Osa (b): kolme yhtä suurta vertailukorttia, kukin näyttää kaksi ihmisroolia rinnakkain yksinkertaisella 2×2- tai Venn-käsittelyllä "kyvykkyys korkea / tehtäväsopivuus vaihteleva," kukin kuvatekstillä raportin omalla lauseella: "raaka kyvykkyys ja tehtäväsopivuus ovat eri asioita." Neljäs kortti, visuaalisesti yhtä suuri kuin muut kolme, laajentaa samaa logiikkaa tekoälyyn: "orkestrointi moninkertaistaa kapasiteetin, ei arvon — halpa, nopea, väärä vastaus, skaalattuna moniagenttitiimin yli, on edelleen halpa ja väärä laajassa mittakaavassa (Julkaisuresurssi #10 §6 / Julkaisuresurssi #11 osa 8)."
- Ei ratkaista mitään neljästä vertailukortista "voittajalla" — kunkin kortin on visuaalisesti päätyttävä avoimeen kysymysmerkkiin tai tasapainoiseen vaakakuvakkeeseen, ei valintamerkkiin kummalla puolella.

**Näyttöluokkamerkinnät:** Koko kaavio on [TULKINTA] (Osio 18 nimenomaisesti tunnistaa itsensä kirjoittajan omaksi käsitteelliseksi synteesiksi, ei vertailtavaksi). Merkitse selkeästi: "Kehys: kirjoittajan oma käsitteellinen synteesi, ei itsenäisesti vertailtu — TULKINTA."

---

## Kaavio 5 — Tekoälyn kypsyyden ja tiedon kehityksen kehys

**Ehdotettu tyyppi:** Kaksiakselinen etenemismatriisi/porraskaavio — X-akseli: "miten työ tehdään" (Neuvo → Työskentele yhdessä → Delegoi → Johda); Y-akseli: "orkestroinnin mittakaava" (Yksittäinen tekoälytyöntekijä → Tekoälytiimi → Tekoälytyövoima) — diagonaalisella "tietoarkkitehtuurin kypsyys" -vyöhykepäällysteellä.

**Mitä se näyttää:** Osio 23:n kaksiakselinen kypsyyskehys ja Osioiden 21–22 väite, että tieto/konteksti on erillinen akseli mallin kyvykkyydestä ("tieto tekoälyn käyttöjärjestelmänä"), plus nimenomainen, ilmoitettu epävarmuus tämän kehyksen julkisesta muodosta (Osio 23:n havainto, että tarkkaa alun perin odotettua kolmivaiheista/kolmiulotteista rakennetta ei vahvistettu LinkedInissä, eikä CC BY 4.0 -lisenssiä löytynyt julkisista julkaisuista).

**Visualisoitu data/osat:** Osio 23 (2-akselinen kehys, neuvo/yhteistyö/delegointi/johtaminen × yksilö/tiimi/työvoima); Osiot 21–22 (tieto kertoimena/käyttöjärjestelmänä, Zuckerbergin henkilökohtaisen agentin yksityisyyssitoumus ja Altmanin 1 000 000-kertaisen käyttökasvun anekdootti tukevina, eri lähteistä tulevina datapisteinä, EI kehyksen itsensä validointina); Osio 24 ("miten saamme sen tehtyä" → "mitä meidän pitäisi tehdä" -siirtymä työn siirtyessä oikealle/ylös matriisissa).

**Rakenteelliset vaatimukset:**
- 4×3-ruudukko (Neuvo/Yhteistyö/Delegointi/Johtaminen × Yksilö/Tiimi/Työvoima), kukin ruutu tavanomainen merkitty laatikko — mitään ruutua ei tulisi sävyttää implikoimaan "parempaa" tai että "kypsempi on arvokkaampaa"; käytä yksinkertaista suuntanuolta (vasemmasta alakulmasta oikeaan yläkulmaan) merkittynä "kasvava delegointi ja orkestroinnin mittakaava" neutraalilla kuvatekstillä, ei "paranemis"-nuolella.
- Peitä diagonaalinen vyöhyke tai gradientinauha merkittynä "tietoarkkitehtuuri ja tiedonhallinta — Osio 21/22, TULKINTA" kulkien ruudukon yli, näyttääkseen tiedon kypsyyden erillisenä, poikkileikkaavana akselina kolmannen ruudukkoulottuvuuden sijaan (vältetään väärä 3D-ruudukko, jonka olemassaoloa alkuperäisessä julkisessa kehyksessä lähdeteksti itse ei voinut vahvistaa).
- Selkeästi erotetun huomautuslaatikon on kannettava havaintoehe­yshuomautus sanatarkasti henkeltään: "Tämän kehyksen julkinen versio (2 LinkedIn-videota, päivätty 2026-06-20) ei täsmälleen vastaa tässä tiivistettyä rakennetta; CC BY 4.0 -lisenssiä ei löytynyt julkisista julkaisuista. Tämä kaavio mukauttaa kehyksen tämän raportin omaan käyttöön — katso Osio 23."
- Toinen pieni merkintärata alareunassa: "kun tämä matriisi siirtyy oikealle/ylös, ihmiskysymys siirtyy 'miten saamme sen tehtyä' -kysymyksestä 'mitä meidän pitäisi tehdä' -kysymykseen — Osio 24, TULKINTA."

**Näyttöluokkamerkinnät:** Ruudukon akselit/rakenne = [TULKINTA], nimenomaisesti kirjoittajan oma mukautettu kehys; mikä tahansa Codex-telemetria tai Altman/Zuckerberg-datapiste, jota käytetään havainnollisena merkkinä ruudukossa, on säilytettävä oma [LÄHDE]-tunnisteensa yksitellen — ruudukon TULKINTA-tunniste ei saa niellä niitä.

---

## Kaavio 6 — Omistusrakenne ja vaihtoehtoiset arkkitehtuurit

**Ehdotettu tyyppi:** Pystysuora kerroksellinen pinokaavio (8 kerrosta) yhdistettynä horisontaaliseen vertailunauhaan 6 pääsy-/omistusmallista — käytännössä kaksi yhdistettyä kaaviota, jotka jakavat yhden selitteen.

**Mitä se näyttää:** Osio 26:n 8-kerroksinen omistusrakenne (energia, laitteisto, laskenta/pääsy, mallit, tieto, agentit, identiteetti, hallinta) kunkin kerroksen havaitulla keskittymiskuviolla, ja Osio 27:n 6 rinnakkain elävää pääsymallia (keskitetty julkinen alusta, yrityskohtainen omistautunut järjestelmä, avoimet mallit omalla/vuokratulla laitteistolla, yksityinen/henkilökohtainen omistus, osuuskunta, paikallinen/alueellinen kapasiteetti), esitettynä nimenomaisesti rinnakkain elävinä kilpailevien sijaan.

**Visualisoitu data/osat:** Osio 26 taulukko (8 kerrosta × keskittymiskuvio × näyttöluokka); Osio 27 (6 mallia, kullakin oma kustannus-/hallintaprofiili); Osio 30:n kompromissitaulukko (mittakaava/suorituskyky/kustannus/yksityisyys/sietokyky/kätevyys/pääsy/hallinta per malli — syötä tämä toiseen pieneen tutka-/hämähäkkikaavioon per malli, jos tilaa riittää, käyttäen identtistä akseliskaalausta kaikissa 6:ssa, jotta yhdenkään mallin tutka ei näytä visuaalisesti "suuremmalta").

**Rakenteelliset vaatimukset:**
- 8-kerroksinen pino: kukin kerros on horisontaalinen kaista, lyhyellä keskittymiskuvio-tunnisteella ja näyttöluokkatunnisteella sisäisesti (useimmat ovat [FAKTA]/[LÄHDE]/[TULKINTA] Osio 26:n taulukon mukaisesti — säilytä täsmälleen, ei nosteta mitään [TULKINTA]-riviä, esim. "Tieto" ja "Identiteetti," [FAKTA]-tasolle).
- 6-mallinauha: kuusi yhtälevyistä sarakettä, nimenomaisesti kuvatekstillä "rinnakkain eläviä pääsykuvioita — ei yleisesti ylivertaista, Osio 27/30," kukin näyttää: kustannusvaihteluväli (osuuskuntasarake näyttää kaksi laitteistotasolukua rinnakkain — 19,50–23 euroa/jäsen/kuukausi DGX Spark -poolille, 42 euroa/jäsen/kuukausi jaetulle työasemaluokan koneelle, Osio 27/32 — selkeästi merkittynä kahdeksi eri tasoksi, ei ratkaisemattomana vaihteluvälinä), hallinta-/siirrettävyys-/poistumis-/hallintotapa-/jatkuvuusikonit Osio 29:n 5-kysymyskehyksestä.
- Jos tutka-/hämähäkkikaaviota käytetään Osio 30:n kompromisseille, kaikkien 6 mallin on käytettävä identtisiä akseliskaaloja (Matala/Keski/Korkea kartoitettuna samaan säteittäiseen etäisyyteen) ja yhtäläistä värivahvuutta — yhdenkään mallin muoto ei saa olla suurempi tai lihavoitunut oletustyylityksellä.
- Nimenomainen avaushuomautus, visuaalisesti näkyvissä (ei haudattuna alaviitteeseen): "Tässä käsitelty osuustoiminnallinen/omistusarkkitehtuuri on yksi ehdokasmalli useiden joukossa, perusteltu omilla luvuillaan kirjoittajan toimesta, jolla on ilmoitettu kommersiaalinen ja edunajointiin liittyvä intressi siihen — Menetelmät §3.4-avaus."

**Näyttöluokkamerkinnät:** Sekoitettu per kerros/per malli kuten Osioissa 26/27/30 määritelty — ei sovelleta yhtä yleistunnistetta koko kaavioon; säilytä lähdetaulukon per-solu-tunnisteet täsmälleen.

---

## Kaavio 7 — Sähköverkko-/aurinko-/osuustoiminta-analogia

**Ehdotettu tyyppi:** Rinnakkainen viisitasoinen analogiakaavio (kaksi rinnakkaista sarakettä: "Sähköennakkotapaus" vs. "Tekoälylaskennan vastine"), erottuvalla visuaalisella "heikko lenkki" -merkillä viidennellä tasolla.

**Mitä se näyttää:** Osio 28:n 5-tasoinen sähköverkkoanalogia (kotitalouden aurinko → energiaosuuskunta → kaupallinen sähköntuottaja → teollisen mittakaavan voimalaitos → sähköverkko/pörssi, kartoitettuna kotitalouden tekoälytehdas → tekoälyinfrastruktuuriosuuskunta → kaupallinen päättelypalveluntarjoaja → hyperskaala-tekoälytehdas → hajautettu päättelymarkkinapaikka), mukaan lukien raportin oma nimenomainen merkintä siitä, että tätä analogiaa ei voitu vahvistaa yksittäistä päivättyä ensisijaista lähdettä vasten ja että sen viidennen tason kartoitus (kitkaton tekoälylaskennan spot-markkina) ei vielä ole olemassa.

**Visualisoitu data/osat:** Osio 28 taulukko (5 tasoa); Bitcoin-hashprice-vs-tekoäly-token-arvo-vertailu (Osio 14/28, Luxor spot-hashprice ~31,73–32,05 dollaria/PH/s/päivä vs. token-arvon vaihtelu vähittäishinnoitellun ja tuotantokustannushinnoitellun tokenin välillä) tukevana sisäkkäisenä havainnollistuksena siitä, miksi taso 5 on heikoin lenkki; OpenRouterin itse raportoimat yli 200T kuukausittaista tokenia / yli 10M käyttäjää "lähimpänä nykyisin olemassa olevana osittaisena vastineena" tasolle 5.

**Rakenteelliset vaatimukset:**
- Viisi parillista riviä, vasen sarake = sähköennakkotapaus (tavanomaiset, arkiset ikonit: aurinkopaneeli, osuuskuntarakennus, voimalaitosikoni, verkkopylväsikoni), oikea sarake = tekoälylaskennan vastine (DGX Spark -ikoni, osuustoiminnallinen palvelinräkki, sopimusklusteri-ikoni, hyperskaalaräkki-ikoni, katkoviiva-/keskeneräinen verkkoikoni tasolle 5).
- Taso 5 -rivin on oltava visuaalisesti erottuva — esim. katkoviivareunus tai viivoitettu täyttö — kuvatekstillä: "Heikoin lenkki analogiassa: kitkatonta, protokollatasoista tekoälylaskennan spot-markkinaa ei tällä hetkellä ole olemassa — Osio 28. OpenRouter on vain osittainen, tarjoajareitittävä vastine, ei laskennan spot-markkina."
- Pieni sisäkkäinen kaavio (palkki- tai dumbbell-tyyppinen), joka vertaa Bitcoinin hashpricea (~31,73–32,05 dollaria/PH/s/päivä, HAVAITTU FAKTA) havainnolliseen tekoäly-token-arvon vaihteluväliin (~0,45–1,50 dollaria/MWh-vastine tuotantokustannuksella vs. ~4 500 dollaria/MWh vähittäishinnalla) — nimenomaisella kuvatekstillä, että tämä EI ole kannattavuusväite kummastakaan toiminnasta, vaan havainnollistus siitä, miksi tokenin *hinta* ja tokenin *arvo* ovat erilliset kysymykset (Osio 14).
- Nimenomainen rajatunniste koko kaaviolla: "Rakenteellinen vertailu tehdäkseen tuntemattoman omaisuusluokan ymmärrettäväksi tutun kautta — ei väite, että tekoälylaskennan markkinat kehittyvät identtisesti sähkömarkkinoiden kanssa. Ei sijoitus- tai infrastruktuurisuunnitteluneuvontaa — Osio 28."

**Näyttöluokkamerkinnät:** Koko analogia = [TULKINTA] (nimenomaisesti merkitty lähteessä analogiaksi, jota kirjoittaja on käyttänyt kommentaareissaan, ei itsenäisesti vahvistettu yksittäistä päivättyä julkaisua vasten). Bitcoinin hashprice-luku = [FAKTA]; tekoäly-token-arvovaihteluväli = [LASKELMA] [OLETUS]-syötteillä; OpenRouter-luvut = [FAKTA, itse raportoitu].

---

## Kaavio 8 — Mittakaavaspektri (Kotitalous → Osuustoiminnallinen → Ammattimainen → Hyperskaala)

**Ehdotettu tyyppi:** Horisontaalinen mittakaavaspektri / porrastettu palkkikaavio neljällä tasolla, kaksoisakseli (pääomakustannus yhdellä akselilla, $/M-token tai $/tekoäly-työtunti toisella käänteisellä akselilla), plus pieni monikertakäyttöasteherkkyysnauha.

**Mitä se näyttää:** Osa VI:n 4-tasoinen skenaariovertailu (Osio 35:n yhteenvetotaulukko): Kotitalous (1× DGX Spark), Osuustoiminnallinen (10×, 50 jäsentä), Ammattimainen (HGX B300/GB300-räkki, heikoimmin todennettu), Hyperskaala (4-räkki/288-GPU-klusteri) — näyttäen pääomakustannuksen, omistetun tuotannon $/M-tokenia, $/tekoäly-työtunti asiaankuuluvalla käyttövyöhykkeellä, ja hallitsevan vivun kullekin tasolle (käyttöaste / käyttöaste+ylikuorma / interaktiivisuusasetus / rahoitusaika).

**Visualisoitu data/osat:** Osio 35 yhteenvetotaulukko (kaikki 4 tasoa); Osio 31 (Kotitaloustason yksityiskohta + käyttöastekäyrä); Osio 32 (Osuustoiminnallinen taso + kahden laitteistotason taulukko: 19,50–23 dollaria DGX Spark -poolille vs. 42 dollaria jaetulle työasemaluokan koneelle, näytettynä rinnakkain); Osio 33 (Ammattimainen taso, nimenomaisesti merkitty heikoimmin todennetuksi/OLETUS-painotteiseksi); Osio 34 (Hyperskaalataso + rahoitusaika-herkkyystaulukko); Osio 12:n käyttöastevipupointti (2 000→8 000 h/vuosi leikkaa kustannuksen 3,5–4-kertaisesti, samaa kuviota käytetty uudelleen Kaaviossa 9).

**Rakenteelliset vaatimukset:**
- Neljä yhtälevyistä pystypaneelia, vasemmalta oikealle, tiukasti järjestettynä mittakaavan mukaan (Kotitalous→Osuustoiminnallinen→Ammattimainen→Hyperskaala) — tämä vasemmalta-oikealle-järjestys on faktuaalinen mittakaavajärjestys, ei arvoranking, ja tulisi merkitä sellaiseksi ("järjestetty pääomamittakaavan mukaan, ei suositellun valinnan mukaan").
- Jokainen paneeli näyttää: pääomakustannuksen (FAKTA/OLETUS soveltuvin osin — Kotitalouden 4 699 dollaria on FAKTA; Ammattimaisen tason capex on nimenomaisesti OLETUS/epävirallinen, ja on renderöitävä visuaalisesti erottuvana, esim. katkoviivalaatikkona, muiden kolmen paneelin pääomaluvuista), omistetun tuotannon $/M-tokenia-vaihteluvälin (LASKELMA), ja $/tekoäly-työtunti-vaihteluvälin kyseisen tason "asiaankuuluvalla vyöhykkeellä" (LASKELMA) — toista Osio 35:n taulukkoarvot täsmälleen, mukaan lukien vaihteluvälit (ei yksittäiset pisteet), säilyttääkseen raportin oman käyttöaste-/interaktiivisuus-/rahoitusherkkyyden.
- Neljän paneelin alla jaettu pieni monikertanauha näyttää "kustannus-per-tunti vs. käyttöaste" -käyrät ainakin Kotitalous- ja Osuustoiminnalliselle tasolle (Osio 31:n kanoninen 0,014–1,427 dollaria/h chat/kopilotti-vyöhykeluku ja Osio 32:n osuustoiminnallinen yhteensovitus), vahvistaen "käyttöaste on yksittäinen suurin vipu joka mittakaavassa — Osio 35 kohta 1."
- Ammattimaisen paneelin on kannettava näkyvä merkki: "Heikoimmin todennettu taso — NVIDIA ei julkaise virallista hinta-/tehospesifikaatiota tälle SKU:lle. Luvut ovat havainnollisia paikkamerkkejä — Osio 33/17 taulukkohuomautus."
- Osuustoiminnallisen paneelin on näytettävä molemmat laitteistotasoluvut nimenomaisesti, ei keskiarvoistettuina, lyhyellä huomautuksella: "kaksi laitteistotasoa — DGX Spark -pooli (19,50–23 €) vs. jaettu työasemaluokan kone (42 €) — Osio 27/32."
- Joka paneeli kantaa näkyvän rajatunnisteen: "SKENAARIO-OLETUS — muokattava havainnollistus, ei ennuste; ei sijoitus-/oikeudellista/vero-/hankinta-/politiikkaneuvontaa."

**Näyttöluokkamerkinnät:** Sekoitettu ja nimenomainen per paneeli yllä olevan mukaisesti — tämä kaavio tarvitsee suoraan täyden 5-luokkaisen selitteen näkyviin koko ajan, koska se sekoittaa FAKTAA (laitteistospesifikaatiot), OLETUSTA (Ammattimaisen tason capex, rahoitus-/sähkösyötteet) ja LASKELMAA (kaikki johdetut $/M-token- ja $/h-luvut) yhdessä visuaalisessa kehyksessä.

---

## Kaavio 9 — Humanoidin fyysisen kapasiteetin laajennus

**Ehdotettu tyyppi:** Rinnakkaisrakennekaavio, jäljittelee Kaavio 2:n vesiputouslogiikkaa, mukautettuna Osio 36:n pääoma+energia+ylläpito+käyttöaste+orkestrointi-ketjuun, plus pieni monikertakäyttöasteherkkyystaulukko (identtinen visuaalinen kielioppi kuin Kaavio 8:n digitaalitason käyttöastekäyrissä, tehdäksesi eri toimialojen rinnastuksen ymmärrettäväksi).

**Mitä se näyttää:** Osio 36:n humanoidin työkapasiteettimalli: todellinen markkinahintavaihteluväli 4 nimetyn alustan yli (Unitree G1, 1X NEO, Agility Digit, kirjoittajan oma havainnollinen 25 000 €/27 000 dollarin peruslaskenta), kustannus-per-tuottava-tunti-taulukko 4 käyttöastetasolla (2 000/4 000/6 000/8 000 h/vuosi), havainto, että sähkö EI ole sitova kustannustekijä tässä (toisin kuin digitaalisilla tasoilla), ja nimenomainen lista poissuljetuista kustannuskategorioista (valvonta, ohjelmisto/tilaus, vakuutus, työtilan muutos, kulutustarvikkeet, käyttökatkot tasaisen varauksen ulkopuolella).

**Visualisoitu data/osat:** Osio 36 (alustahintataulukko: Unitree 13,5K dollaria FAKTA, 1X NEO 20K dollaria/499 dollaria/kk LÄHDE-vahvistamaton, Agility Digit ~250K dollaria LÄHDE-toissijainen, Tesla Optimus 20–30K dollaria LÄHDE-vahvistamaton-tavoite, Figure 03 ei dataa, kirjoittajan oma 25 000 €/27 000 dollarin havainnollinen peruslaskenta TULKINTA); 4×4-kustannus-per-tunti-matriisi; 1X NEO:n akusta johdettu sähköarvio (~0,03 dollaria/h) verrattuna rahoitukseen/ylläpitoon hallitsevana kustannuksena.

**Rakenteelliset vaatimukset:**
- Horisontaalinen hintavaihteluvälipalkki näyttää kaikki 5 nimettyä viitepistettä (Unitree matala pää, kirjoittajan havainnollinen piste, 1X NEO, Optimus-tavoite, Agility Digit korkea pää, nousevassa hintajärjestyksessä) — kukin piste merkitty yksitellen näyttöluokallaan (ei annettu havainnollisen 25 000 €:n luvun näyttää visuaalisesti "todellisemmalta" kuin FAKTA-merkitty Unitree-luku; käytä identtistä merkintätyyliä, erotettuna vain luokkaselitteen värillä/ikonilla).
- Kustannus-per-tunti-taulukko (4 käyttöasteriviä × 5 hintasaraketta Osio 36:sta) toistettuna pienenä lämpöruudukkona, käyttäen samaa käyttöastevipukehystystä kuin Kaavio 8:n nauhassa, nimenomaisella ristiviitekuvatekstillä: "sama 3,5–4-kertainen käyttöastevaikutus havaittu joka digitaalisella tuotantotasolla Osiossa 35 — Osio 36."
- Erillinen, visuaalisesti erotettu huomautus sähkö-vs-rahoitus/ylläpito-havainnolle: pieni piirakka- tai pinottupalkkierittely yhdellä viitekäyttöastetasolla (esim. 4 000 h/vuosi) näyttää rahoituksen + ylläpitovarauksen hallitsevan ~0,03 dollarin/h sähköarviota, kuvatekstillä "toisin kuin token-tuotannossa (Kaavio 2), sähkö ei ole sitova kustannus tässä — Osio 36."
- Selkeästi laatikoitu "pois tästä mallista" -lista (valvontatyö, ohjelmistomaksut, vakuutus, työtilan muutos, kulutustarvikkeet, ylimääräiset käyttökatkot) kuvatekstillä: "joka yllä oleva luku on lattia, ei täysi kommersiaalinen kustannus — Osio 36."
- Pakollinen soveltamisalabanneri koko kaavion yli: "Kapea omistuskustannusmalli vain. EI yleinen väite robotiikkataloudesta, tuotesuositus tai ennuste. Teolliset varret/AMR:t ja muut kategoriat ovat soveltamisalan ulkopuolella — Osio 36 soveltamisalailmoitus."
- Lyhyt loppuhuomautus/ikoni, joka toistaa Osio 36:n arvorajapointin: "kapasiteetti ≠ arvo — laivue, jonka omistus maksaa 1 dollarin/tunti, ei kerro mitään siitä, onko sen työ 1, 100 dollarin tai ei mitään arvoinen (ristiviite Kaavio 4)."

**Näyttöluokkamerkinnät:** Sekoitettu per datapiste kuten määritelty — tämä kaavio on korkein LÄHDE/vahvistamaton- ja TULKINTA/havainnollinen-tunnisteiden pitoisuus mistä tahansa briiffistä tässä joukossa, ja sitä ei saa visuaalisesti tasoittaa; selitteen on oltava näkyvä, ei koristeellinen.

---

## Kaavio 10 — Viimeinen siirtymä: Runsas työkapasiteetti → "Mitä meidän pitäisi tehdä?"

**Ehdotettu tyyppi:** Yksittäinen suuri loppukoostetta — lähentyvä suppilo-/nuolikaavio, joka syöttää avoimeen kysymysmerkkiin, kuuden paneelin järjestämättömällä renkaalla tai ruudukolla alla, edustaen kuutta lukijalinssiä, kukin kohtaamassa samaa avointa kysymystä.

**Mitä se näyttää:** Raportin loppuväite (Osiot 43–45): että biljoonien sitoutettu pääoma ja laskevat kustannuskäyrät (osat II–IV) edustavat mahdollisuutta, ei kohtaloa; että orkestrointi moninkertaistaa kapasiteetin, ei harkinnan; ja että keskeinen ratkaisematon ihmiskysymys, kun työkapasiteetti tulee runsaaksi, siirtyy "miten saamme sen tehtyä" (yhä enemmän tekoälyn vastaamana) -kysymyksestä "mitä meidän pitäisi tehdä" -kysymykseen (kysymys, jota raportti nimenomaisesti ei vastaa lukijan puolesta).

**Visualisoitu data/osat:** Osio 43 (kuusi-linssinen mahdollisuudet-ei-väistämättömyyttä-lista, nimenomaisesti järjestämätön); Osio 44 (käyttöönotto/organisatorinen muutos/aika ratkaisemattomina muuttujina — Codex-telemetria, Tekoälyn kypsyyskehyksen "oppiminen→sisäistäminen→tekoälynatiivi"-etenemä, ja Altmanin kustannuslasku-vs-kysyntäkasvu-erottelu, kaikki käytetty tässä tiukasti aiemmin vahvistettuna näyttönä, ei uusina väitteinä); Osio 45 (loppusanojen "miten" vs. "mitä" -kehystys, nimenomaisesti merkitty TULKINNAKSI ja ei kohdistettu millekään nimetylle johtajalle).

**Rakenteelliset vaatimukset:**
- Ylä osa: lähentyvä suppilo, joka tuo yhteen pieniä merkittyjä sivujokia edustaen raportin suuria eteenpäin katsovia säikeitä (Huangin/Finkin rahoitus- ja per-GW-väitteet, Altmanin kustannuslasku- ja kysyntäväitteet, Zuckerbergin henkilökohtaisen agentin väitteet, laskevat $/M-token-käyrät) — kukin sivujoki säilyttää oman näyttöluokkatunnisteensa ja EI SAA sulautua yhdeksi merkitsemättömäksi "tekoälykehitys"-nuoleksi; suppilo lähentyy kohti yksittäistä solmua merkittynä "Runsas, halpa tekoälytyökapasiteetti (jos trendi jatkuu — ei todistettu, Osio 44)."
- Tämä lähentymissolmu syöttää yhden nuolen alaspäin suureen, tarkoituksellisesti avoimeen/täyttämättömään kysymysmerkkimuotoon merkittynä "Mitä meidän pitäisi tehdä?" — tämän muodon on oltava visuaalisesti keskeneräinen/avoin (vain ääriviiva, tai pirstaloitunut/katkoviivaglyfi), jotta ei implikoida, että raportti tarjoaa vastauksen.
- Alla, kuusi yhtä suurta paneelia järjestettynä renkaaksi tai 2×3/3×2-ruudukoksi (ei linssiä ensimmäisenä, ei linssiä suurimpana, ei numeroitua järjestystä muuta kuin mitä tarvitaan aakkosellisen tai asettelullisen neutraliteetin vuoksi) — kukin paneeli nimeää yhden lukijalinssin ja yhden avoimen, ratkaisemattoman mahdollisuuden/kysymyksen Osio 43:sta, muotoiltuna kysymykseksi, ei suositukseksi (esim. Yksityishenkilö: "yksityinen oletuksena -henkilökohtainen agentti, vai syvempi riippuvuus?"; PK-yritys: "toimitusinnovaationousu — ehdollinen käyttöönottokyvylle"; Rahoitus: "todellista infrastruktuuria ja väärin hinnoiteltua riskiä, samoista faktoista"; Valtio: "mahdollisuus jakautuneena, vai keskittyneenä, oletuksena?"; Rakentaja/Operaattori: "halvat tokenit laajentavat sitä, mitä on rakennettavissa — ja mitä on rakennettavissa väärin laajassa mittakaavassa"; Kouluttaja/Tutkija/Toimittaja: "halvat tokenit laajentavat pääsyä selitykseen ja itsevarmaan virheeseen yhtä lailla").
- Pieni sivumerkintä, joka toistaa Osio 45:n loppu-TULKINTA-lauseen sanatarkasti, selkeästi laatikoituna ja merkittynä: "[TULKINTA — kirjoittajan oma loppusynteesi, ei kohdistettu millekään nimetylle johtajalle]: kun työkapasiteetista tulee runsasta, 'miten saamme sen tehtyä' saa yhä enemmän vastauksen tekoälystä, kun taas 'mitä meidän pitäisi tehdä' tulee yksittäiseksi tärkeimmäksi ihmiskysymykseksi."
- Nimenomainen loppuraja itse kaaviossa: "Tämä raportti ei vastaa tähän kysymykseen kenenkään lukijan puolesta. Yhtäkään linssin versiota kysymyksestä ei priorisoida toisen yli."

**Näyttöluokkamerkinnät:** Sekoitettu per sivujoki (LÄHDE joka nimetyn johtajan väitteelle, LASKELMA kustannuskäyräsivujoille, TULKINTA suppilon lähentymiskehystykselle ja loppu-"miten/mitä"-lauseelle) — itse avoin kysymysmerkkisolmu ei kanna näyttötunnistetta, koska se edustaa ratkaisematonta kysymystä, ei väitettä.

---

## Kaavio 11 — Kasvun luominen uuden arvon pohjalta

**Tila:** Lisätty 2026-08-14, uuden "Tekoälytyökapasiteetista uuteen arvoon" -käsitteellisen sillan mukana (sijoitettu alkutekstin osien IV ja V väliin). Toisin kuin Kaaviot 1–10, tämä on kirjoittajan oma **ennalta olemassa oleva kaavio, toimitettu suoraan ja käytetty sellaisenaan** — katso `assets/diagrams/diagram-11-creating-growth-from-new-value.png` (provenienssikehystetty tätä pakettia varten — näyttöluokkatunniste, viittaus, lähdehuomautus ja vakioalatunniste lisätty alkuperäisen kuvan ympärille; kirjoittajan toimittama muokkaamaton alkuperäinen säilytetään sen vierellä tiedostona `diagram-11-creating-growth-from-new-value.jpg`). Tämä kohta kuvaa tämän kuvan todellista rakennetta (toimittajille, vaihtoehtoiselle tekstille ja johdonmukaisuuden tarkistamiseen varten), ei tyhjästä laadittua suunnittelijabriiffiä.

**Todellinen tyyppi:** Kaksisarakkeinen, alapohjainen muuntokaavio — ei horisontaalinen ketju kuten Kaavio 1. Kaksi yhtälevyistä pystysarakea ("Uuden arvon luominen" vasemmalla, "Kasvu uuden arvon pohjalta" oikealla), kumpikin ajaa kolme laatikkoa, molemmat sarakkeet lähentyvät yhteen jaettuun horisontaaliseen vyöhykkeeseen, "Uusi arvo," alareunassa. Harmaat alaspäin osoittavat nuolet vasemmassa sarakkeessa ja harmaat ylöspäin osoittavat nuolet oikeassa sarakkeessa osoittavat molemmat kohti tätä jaettua vyöhykettä — visuaalisesti toteaen, että uusi arvo luodaan laskeutumalla vasenta saraketta, ja kasvu luodaan nousemalla oikeaa saraketta, samasta taustalla olevasta arvosta.

**Mitä se näyttää:** Sama ydinerottelu kuin alkutekstin "Tekoälytyökapasiteetista uuteen arvoon" -osiossa — että uuden arvon luominen ja kasvun luominen tästä arvosta ovat kaksi erillistä, peräkkäistä prosessia, joista kumpikaan ei ole toisen takaama, eikä kumpaakaan tämän raportin kustannus-/kapasiteettimalli (osat I–IV) suorita itsestään.

**Tarkka sisältö, laatikko laatikolta (ylhäältä alas, vasen sarake ensin, sitten oikea):**
- **Idea / Keksintö** — "Näkemys jostakin uudesta tai olemassa olevan ratkaisun kohdistaminen uudelle yleisölle uutena tarjoamana."
- **Innovaatio** — "Kehitys- ja toteutusprosessi."
- **Uuden arvon vahvistaminen** — "Uusi arvo on olemassa vain, kun joku (tyypillisesti asiakas) on halukas maksamaan siitä, käyttämään sitä tai sitoutumaan siihen."
- **Uusi arvo** (jaettu alavyöhyke, korostettuna sinisellä, ulottuu molempien sarakkeiden yli) — "Mitä, kenelle, miten, ja miten vahvistettu."
- **Arvolupaus ja viestintä** — "(Markkinointi = Skaalattu myynti) — uuden arvon tekeminen näkyväksi ja sen viestiminen houkuttelevasti kohderyhmälle."
- **Tulomalli** — "Miten uusi arvo vaihdetaan tuloksiin/tuloon."
- **Tuottavuus (Tuotos / Syötteet)** — "Kuinka tehokkaasti arvoa tuotetaan käytettyihin syötteisiin nähden."

**Miten tämä kartoittuu alkutekstin omaan ketjuun:** vasen sarake ("Uuden arvon luominen") vastaa alkutekstin osion idea/keksintö → innovaatio → vahvistettu uusi arvo -segmenttiä; oikea sarake ("Kasvu uuden arvon pohjalta") vastaa sen arvolupaus ja viestintä → tulomalli → tuottavuus -segmenttiä. Alkutekstin aikaisemmat vaiheet — sähkö → laskentainfrastruktuuri → tekoälytyökapasiteetti → hyödylliset työtulokset → ihmisen ja organisaation integraatio — sijaitsevat kokonaan tämän kaavion yläpuolella; tämä kaavio alkaa "idea/keksinnöstä," eli kohdasta, jossa käyttö tälle kapasiteetille on jo tunnistettu. Se tulisi kuvatekstittää tämän mukaisesti kaikkialla, missä se sijoitetaan, jotta lukija ei odota tekoälykustannusketjun esiintyvän tämän kuvan sisällä.

**Sijoitteluhuomautus:** tämä kaavio on kirjoittajan oma yleinen liiketoiminta-/innovaatiokehys, sovellettavissa kauas tekoälyn ulkopuolelle, ja edeltää tätä alkutekstiä. Se on **[TULKINTA]** samassa mielessä kuin muu tämä osio — käsitteellinen linssi, ei numeerinen havainto — ja sen tulisi kantaa tätä tunnistetta plus lyhyt huomautus siitä, että se on yleinen kehys, sovellettu tässä tekoälytyökapasiteettikysymykseen, ei johdettu tämän raportin kustannusdatasta.

**Näyttöluokkamerkinnät:** Koko kaavio on **[TULKINTA]** — kirjoittajan oma yleinen käsitteellinen kehys, sovellettu tämän raportin aiheeseen, ei johdettu miltään nimetyn johtajan lausunnolta tai tämän raportin kustannustyökirjoilta.

---

**Kaavioiden välinen johdonmukaisuushuomautukset suunnittelijalle (koskevat kaikkia 11 briiffiä):**
- Käytä yhtä johdonmukaista 5-luokkaista selitettä (ikoni + väri) koko resurssijoukossa (#15), jotta lukija, joka siirtyy kaaviosta toiseen, ei joudu opettelemaan koodia uudelleen joka kerta.
- Käytä yhtä johdonmukaista typografista/värikäsittelyä "SKENAARIO-OLETUS — ei ennuste, ei neuvontaa" -rajatunnisteille kaavioissa 2, 3, 8, 9 (ja 1:n ja 6:n rahoitus-/skenaarioosuuksissa).
- Ei tuoda värikoodausta, joka implikoi suosittua omistusmallia, johtajaa tai lukijalinssiä missään joukossa — palettivalintojen tulisi olla funktionaalisia (näyttöluokka, taso tai akseli), ei arvottavia.
- Kaikkien 11 kaavion tulisi kantaa sama alatunniste-lohko: faktojen aikarajaus (2026-08-13) ja CC BY 4.0 -viittausrivi.

---

Julkaistu CC BY 4.0 -lisenssillä. Ehdotettu viittaustapa: Tutkimussynteesi ja mallinnus: Valto Loikkanen, tekoälyn avustuksella.
