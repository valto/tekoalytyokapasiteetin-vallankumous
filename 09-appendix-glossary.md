# MÄÄRITELMÄT JA MERKINNÄT

### Liite — täydentää julkaisua "Miksi tekoälyyn investoidaan biljoonia?" (Valto Loikkanen, CC BY 4.0)

## Miten tätä liitettä luetaan

Tämä on selkokielinen sanasto kaikista teknisistä ja taloudellisista termeistä, joita käytetään muualla tutkimusraportissa ja sen täydentävissä työkirjoissa. Termit ovat aakkosjärjestyksessä. Useimmat merkinnät ovat **määritelmiä** — kuvauksia siitä, mitä termi tarkoittaa ja miten sitä käytetään tässä raportissa — eivätkä ne itsessään ole tosiasiaväitteitä, jotka vaatisivat näyttöluokkamerkintää. Jos määritelmä sisältää tietyn luvun, teknisen tiedon tai esimerkin (hinnan, vertailutuloksen, nimetyn tuotteen), tämä luku merkitään erikseen samalla viisiluokkaisella järjestelmällä, jota käytetään muualla raportissa, jotta lukija erottaa selkeän määritelmän upotetusta tosiasiaväitteestä. Termit on ristiviitattu tutkimusraportin siihen osaan/lukuun, jossa niillä on suurin painoarvo, kun se on hyödyllistä.

**Näyttöluokkien selitteet** (määritelty kokonaisuudessaan alkutekstissä ja lähderekisterissä; toistetaan tässä, koska "näyttöluokka" on itsessään alla määritelty termi):

| Koodi | Merkitys |
|---|---|
| **HAVAITTU FAKTA** | Ensisijainen dokumentaatio, viralliset tekniset tiedot/hinnoittelu, viranomaisasiakirjat, sääntely tai suora tallenne/transkriptio, jotka on tarkistettu itsenäisesti elävää tai ensisijaista lähdettä vasten viimeistään 2026-08-13 (raportin faktojen aikarajaus; useimmat väitteet tarkistettiin alun perin viimeistään 2026-08-12, ja pieni määrä yksittäisiä korjauksia varmistettiin itsenäisesti 2026-08-13). |
| **LÄHTEESEEN KOHDISTETTU LAUSUNTO** | Se, mitä nimetty johtaja, organisaatio tai lähde sanoo julkisesti ja tallenteella — ei automaattisesti käsitellä itsenäisesti todistettuna faktana. |
| **JOHDETTU LASKELMA** | Läpinäkyvä laskutoimitus, joka perustuu mainittuihin HAVAITTU FAKTA- tai LÄHTEESEEN KOHDISTETTU LAUSUNTO -syötteisiin, kaava näkyvissä. |
| **SKENAARIO-OLETUS** | Näkyvä, muokattavissa oleva parametri, jota käytetään mahdollisen tapauksen tutkimiseen — ei nimenomaisesti markkinaluku. |
| **TULKINTA** | Selkeästi merkitty selitys siitä, miten faktat, lausunnot ja skenaariot voivat liittyä toisiinsa — ei koskaan esitetä faktana. |

---

## A

**Agentti / agenttimainen tekoäly.** Ohjelmisto, joka on rakennettu yhden tai useamman tekoälymallin päälle ja joka voi suorittaa monivaiheisia toimia tavoitteen saavuttamiseksi — käyttää työkaluja, kirjoittaa ja ajaa koodia, selaa verkkoa, muokkaa tiedostoja — vähäisellä tai olemattomalla ihmisen puuttumisella vaiheiden välillä, sen sijaan että vastaisi yhteen kehotteeseen ja pysähtyisi. OpenAI:n Codex toimii tässä raportissa esimerkkinä agenttimaisesta koodaustyökalusta. Katso *orkestrointi*.

**Tekoälytyökapasiteetti (AI working capacity).** Tämän raportin keskeinen välikäsite, erillinen raa'asta token-tuotoksesta. Työkapasiteetti on *todellinen kyky saada jotain aikaan* tekoälyn avulla — sen muodostavat yhdessä mallin suorituskyky, infrastruktuuri, mallin käytettävissä oleva tieto/konteksti, sen käytettävissä olevat työkalut, orkestrointi, luotettavuus ja ihmisen ohjaus. Malli, joka tuottaa tokeneita nopeasti, ei automaattisesti tarkoita korkeaa työkapasiteettia — työkapasiteetti on se, mitä jää jäljelle, kun kaikki näiden kertovien ja jakavien tekijöiden vaikutus on huomioitu. Erotetaan tarkoituksellisesti ja selvästi *tuloksesta* ja *arvosta* (katso näitä koskevat merkinnät) — työkapasiteetti on kyky toimia, ei takuu siitä, että toiminta tuotti mitään arvokasta. Keskeinen osa III osaa.

**Tekoäly-työtunti ($/tekoäly-työtunti).** Johdettu yksikkö, jota käytetään läpi täydentävien työkirjojen muuntamaan $/miljoona tokenia -tuotantokustannus kustannukseksi tunnissa annetulla käyttöintensiteettivyöhykkeellä (chat/neuvonantaja, aktiivinen kopilotti, delegoitu yksittäisagentti, raskas moniagenttiorkestrointi — katso *käyttöintensiteettivyöhyke*). **Kaava: $/tunti = ($/miljoona tokenia) × (kulutetut tokenit tunnissa ÷ 1 000 000).** Jokainen $/tekoäly-työtunti-luku tässä raportissa on **JOHDETTU LASKELMA**, joka perustuu ilmoitettuun $/M-token-syötteeseen ja ilmoitettuun, muokattavissa olevaan tokenia/tunti-oletukseen — se ei ole missään noteerattu markkinahinta, eikä se kerro mitään tunnin tuotoksen arvosta.

**Amortisaatio / lyhennyslaina.** Vakiomenetelmä, jota käytetään joka kustannustasolla tässä raportissa laitteistohankinnan pääomakustannuksen tasaiseen jakamiseen (maksuina) rahoitusajan yli, korko mukaan lukien. **Läpi raportin käytetty kaava: M = P × i ÷ (1 − (1+i)⁻ⁿ)**, jossa P = pääoma (rahoitettu määrä), i = jakson korkokanta, n = maksujaksojen lukumäärä. Rahoitusajan pituuden tai korkokannan muuttaminen — molemmat ovat **SKENAARIO-OLETUKSIA** jokaisessa tämän raportin työkirjassa — muuttaa vuosittaista rahoitetun pääoman lukua muuttamatta itse laitteiston kustannusta lainkaan.

**LÄHTEESEEN KOHDISTETTU LAUSUNTO.** Katso yllä oleva näyttöluokkataulukko. Kriittinen erottelu, jota tämä raportti vaatii: se, että nimetty henkilö sanoi jotain tallenteella, voi itsessään olla **HAVAITTU FAKTA** (eli itsenäisesti vahvistettu transkriptiota vasten, että hän sanoi ne sanat), kun taas hänen esittämänsä väite itsessään pysyy vain LÄHTEESEEN KOHDISTETTUNA LAUSUNTONA, ellei sitä ole erikseen ja itsenäisesti todistettu. Toistuvasti käytetty esimerkki tässä raportissa: on HAVAITTU FAKTA, että Sam Altman sanoi kysynnän kasvavan edelleen; ei ole sillä todistettu, että kysyntä todella kasvaa hänen kuvaamallaan vauhdilla.

---

## B

**Erätoteutus (batch processing).** Alennettu API-käyttötapa (noin puolet useiden tässä raportissa mainittujen laboratorioiden vakiohinnasta per token), jossa pyynnöt jonotetaan ja käsitellään ei-kiireellisesti sen sijaan, että ne palautettaisiin reaaliaikaisesti. Relevantti *vähittäis-API-hinnan* vertailuissa osissa III/VI, ei koskaan *omistettuun tuotantokustannukseen*.

**BF16 / FP16 / FP8 / FP4.** Numeeriset tarkkuusformaatit, joita käytetään esittämään tekoälymallin sisäisiä painoja ja aktivaatioita koulutuksen tai päättelyn aikana. Matalamman tarkkuuden formaatit (FP8, FP4) käyttävät vähemmän bittejä per luku, mikä lisää läpäisykykyä ja alentaa muisti-/tehokustannusta per token, jonkin verran numeerisen tarkkuuden riskillä mallista ja tehtävästä riippuen; tämän vuoksi saman sirun otsikkotason "tokenia sekunnissa" tai "tokenia wattia kohti" -luku voi vaihdella useilla kertoimilla riippuen siitä, mitä tarkkuutta lainataan (katso *harvuus*). NVIDIAn GB300 NVL72 -räkki, mainittu osassa II, ilmoittaa FP4-suorituskyvyn olevan noin 4x sen FP16/BF16-luku — tämä on formaatin todellinen ominaisuus, ei epäjohdonmukaisuus **[HAVAITTU FAKTA, NVIDIAn tuotesivu, klusteri A]**.

---

## C

**Capex (pääomamenot).** Laitteiston (sirun, räkin, robotin, datakeskuksen) etukäteinen hankintakustannus — vastakohtana *opexille* (sähkö, ylläpito, henkilöstö, rahoituskorko, jotka kaikki toistuvat). Tämän raportin kustannusmallit erottavat johdonmukaisesti capexin, rahoituskustannuksen ja käyttökustannuksen omiksi riveikseen sen sijaan, että ne yhdistettäisiin yhdeksi luvuksi, osassa II esitetyn "taloudellisten kerrosten erottelun" säännön mukaisesti, jota noudatetaan joka työkirjassa.

**Klusteri (lähderekisteri).** Ryhmittelymerkintä (A–J), jota käytetään tämän raportin lähderekisterissä / faktantarkistusluettelossa järjestämään yhdessä tarkistetut, toisiinsa liittyvät väitteet (esim. "Klusteri A: NVIDIAn laitteisto, vertailutulokset, TCO"). Ei tekninen tekoälytermi — puhtaasti tämän raportin metodologiaan sisäinen viittausten järjestelydevice.

**Laskenta (compute).** Yleinen lyhenne prosessointikyvylle — sirut, muisti, yhteenliitäntä ja sähkö ja jäähdytys, jotka pitävät niitä käynnissä — joka muuttaa sähkövirran kyvyksi ajaa tekoälymalleja. Toinen lenkki tämän raportin ydinketjussa: energia → laitteisto → **laskenta** → mallit → tokenit → tekoälytyökapasiteetti → digitaalinen työ → tulokset → arvo → toimijuus.

**Kontekstikkuna (context window).** Suurin tokenien määrä (katso *token*), jonka malli voi pitää "näkyvissä" kerralla yhden keskustelun tai pyynnön aikana — aiemmat vuorot, asiakirjat, koodi, ohjeet ja mallin oma tuotos jakavat kaikki tämän budjetin. Osassa III käsitellyt kärkimallit ilmoittavat kontekstikkunia noin 1 miljoonan tokenin tai enemmän kokoisina tämän raportin aikarajauksen mukaan **[esim. GPT-5.6-perhe ilmoitettu noin 1,05M tokenin kokoisena — LÄHTEESEEN KOHDISTETTU LAUSUNTO tekoälyn tiivistämän hakutuloksen kautta, klusteri B]**. Suurempi kontekstikkuna ei ole samaa kuin enemmän työkapasiteettia — se on yksi syöte muiden joukossa.

**Osuustoiminnallinen infrastruktuuri.** Malli, jota tarkastellaan osassa V ja täydentävässä paikallistetussa skenaariotyökirjassa, jossa joukko jäseniä rahoittaa yhdessä ja jakaa pääsyn laskentalaitteistoon (kuvattuna noin 10 laitteella / noin 50 jäsenellä) sen sijaan, että jokainen jäsen ostaisi yksin tai vuokraisi hyperskaalaajalta. Sen taloudellisuus riippuu voimakkaasti käyttöasteesta, koordinaatio-/hallintokuluista ja rahoitusehdoista — kaikki **SKENAARIO-OLETUKSIA** tämän raportin malleissa — ja tämä raportti tarkoituksellisesti säilyttää, sen sijaan että ratkaisisi, noin 2-kertaisen selittämättömän eron kahden itsenäisesti tuotetun kustannusarvion välillä samalle osuustoiminnalliselle rakenteelle (katso osa V, Tokenitehtaan skenaariotyökirjan osa 1) esimerkkinä siitä, kuinka herkkä tämäntyyppinen malli on lausumattomille oletuksille.

---

## D

**Datakeskus.** Fyysinen tila, joka sisältää laskentalaitteiston räkit sekä niiden käyttämiseen tarvittavan sähkönjakelun, jäähdytyksen ja verkottamisen. "Hyperskaala"-datakeskukset (osa VI) kuluttavat jatkuvasti useita megawatteja tai jopa gigawatteja sähköä.

**JOHDETTU LASKELMA.** Katso yllä oleva näyttöluokkataulukko. Jokainen tämän luokan esiintymä tässä raportissa näyttää kaavansa selkeästi sen sijaan, että esittäisi vain tuloksen — tämä on raportin metodologian ehdoton vaatimus, ei tyylivalinta.

**DGX Spark.** NVIDIAn prosumer-/työasemaluokan tekoälylaskentalaite, jota käytetään läpi tämän raportin viitteenä "kotitaloustason" laitteistolle. Tekniset tiedot: GB10 Grace Blackwell -superpiiri, jopa 1 petaflopin FP4-suorituskyky, 128 GB yhtenäistä muistia, 240 W virtalähde **[HAVAITTU FAKTA, NVIDIAn tuotesivu, klusteri A]**. Sen Founders Edition -hinta nousi 3 999 dollarista 4 699 dollariin helmikuussa 2026 **[HAVAITTU FAKTA, NVIDIAn kehittäjäfoorumin hinnanmuutosilmoitus, klusteri A]** — tämä raportti käyttää nykyistä 4 699 dollarin lukua, ei vanhentunutta lanseerausta hintaa, joka kustannusmallissa.

---

## E

**Sähkön hinta.** $/kWh (tai €/kWh) -hinta, joka maksetaan sähköstä. Käsitelty läpi tämän raportin **SKENAARIO-OLETUKSENA**, ei vahvistettuna markkinalukuna, joka paikallistetussa tai skenaariotyökirjassa — koska vähittäis-, kaupallinen ja teollinen sähkötariffi vaihtelee alueen, sopimuksen ja ajan mukaan, eikä yhtä vahvistettua globaalia lukua ole olemassa. Lukijoita ohjeistetaan nimenomaisesti korvaamaan tämä omalla tarkistetulla paikallisella hinnalla.

**Näyttöluokka.** Viisiosainen luokitusjärjestelmä (HAVAITTU FAKTA, LÄHTEESEEN KOHDISTETTU LAUSUNTO, JOHDETTU LASKELMA, SKENAARIO-OLETUS, TULKINTA), johon joka olennainen väite tässä tutkimusraportissa ja sen liitteissä on lajiteltava. Määritelty kokonaisuudessaan tämän liitteen alussa ja raportin alkutekstissä; ainoa metodologinen työkalu, joka erottaa tämän raportin lähestymistavan tavallisesta trendiennustekirjoittamisesta.

---

## F

**Rahoitetun omaisuuden kustannus.** Yksi kahdeksasta kustannus"kerroksesta", jotka tämä raportti vaatii eroteltavaksi (katso *kerrosten erottelu*): laitteiston vuosikustannus sen jälkeen, kun korko-/rahoitusehdot on lisätty sen raakaan hankintahintaan, vastakohtana yksinkertaiselle tasapoistolle. Katso *amortisaatio*.

**FLOP / PFLOPS.** Liukulukuoperaatio (yksittäinen aritmeettinen laskutoimitus); PFLOPS = biljoona (10^15) tällaista operaatiota sekunnissa, vakioyksikkö sirun tai räkin raa'an laskentaläpäisykyvyn kuvaamiseen. Erillinen käsite *tokenia sekunnissa* -mittarista — FLOPS mittaa raakaa aritmeettista kapasiteettia, tokenia/sek mittaa tämän kapasiteetin käytännön tuotosta ajaessa tiettyä mallia ja työkuormaa, ja näiden kahden suhde vaihtelee suuresti mallin arkkitehtuurin ja tarkkuusformaatin mukaan.

**Kärkimalli (frontier model).** Toimialan lyhenne (laboratorioiden ja median käyttämä, ei muodollisesti määritelty tekninen termi) tietyn tekoälylaboratorion sillä hetkellä tarjoamille kyvykkäimmille malleille — esim. OpenAI:n GPT-5.6-perhe, Anthropicin Claude Opus/Fable/Sonnet 5, Googlen Gemini 3.1 Pro, kaikki mainittuina osassa III. "Kärki" on suhteellinen ja liikkuu jatkuvasti eteenpäin; malli, jota kutsutaan kärkimalliksi vuoden 2026 puolivälissä, ei välttämättä ole laboratorion huipputaso vuotta myöhemmin.

---

## G

**GB300 NVL72.** NVIDIAn räkkitason tekoälyjärjestelmä, jota käytetään läpi tämän raportin viitteenä "hyperskaala-/teollisuustasolle": 72 Blackwell Ultra -GPU:ta, 36 Grace-CPU:ta, 20 TB HBM3e-muistia, 130 TB/s NVLink-yhteenliitäntäkaistanleveys ja noin 135 kW räkin sähkönkulutus (TDP) OEM-kumppanin tekniset tiedot -arkin mukaan, ei NVIDIAn omalta sivulta suoraan **[HAVAITTU FAKTA — NVIDIAn tuotesivu laskenta-/muistispekseille; Lenovon OEM-viiteasiakirja tehonkulutukselle; klusteri A]**. Tärkeä varaus, joka toistuu läpi tämän raportin: laajalti toistettu "2,5 miljoonaa tokenia sekunnissa" DeepSeek-R1-vertailutulos tälle laitteistolle on *yhteenlaskettu tulos neljän toisiinsa kytketyn GB300 NVL72 -räkin yli (yhteensä 288 GPU:ta)*, ei yksittäinen räkki — erottelu, jonka tämän raportin kustannusmallit korjaavat nimenomaisesti sen sijaan, että käyttäisivät hiljaisesti uudelleen suuremman, houkuttelevamman luvun **[HAVAITTU FAKTA, NVIDIAn kehittäjäblogi / MLPerf v6.0, klusteri A]**.

**Gigawatti (GW) -rakentaminen.** Mittakaavan yksikkö, jota osissa I ja VI lainatut rahoitusjohtajat käyttävät kuvaillessaan tekoälyinfrastruktuuri-investointeja (esim. Jensen Huangin ja Larry Finkin noin 50–60 miljardin dollarin "per gigawatti" -luku, ja Finkin ">70 gigawatin" ennustettu Yhdysvaltain kysyntä) **[LÄHTEESEEN KOHDISTETTU LAUSUNTO, CNBC-transkripti, klusteri C]**. Yksi gigawatti = 1 000 megawattia = riittää karkeasti ottaen keskikokoisen kaupungin jatkuvaan sähkönkulutukseen; tämän raportin kontekstissa se viittaa tekoälydatakeskuskampuksille varattuun jatkuvaan sähkökapasiteettiin, ei kertaluonteiseen energiamäärään.

**GPU (grafiikkasuoritin).** Sirutyyppi (alun perin suunniteltu kuvien renderöintiin), joka osoittautui hyvin soveltuvaksi tekoälymallien vaatimaan rinnakkaiseen aritmetiikkaan, ja joka nyt on käytännössä kaiken kärkitason tekoälykoulutuksen ja -päättelyn perusta. NVIDIA on tässä raportissa käsitelty hallitseva GPU-toimittaja; AMD:n MI-sarjan sirut mainitaan toissijaisena vertailukohtana joissakin vertailutulosten lähteissä (klusteri A).

---

## H

**Hashprice.** Bitcoin-louhinnan toimialan vakiotulomittari: odotettu päivittäinen dollarimääräinen tulo louhinnan laskentatehon yksikköä kohti (noteerattu $/petahash/sekunti/päivä). Käytetty osissa IV/VI puhtaasti vertailukohtana "bruttotulo kulutettua sähköyksikköä kohti" -tarkastelussa havainnollisia tekoäly-token-tuloskenaarioita vastaan — ei väitteenä siitä, että tekoälylaskenta ja Bitcoin-louhinta olisivat taloudellisesti vastaavia toimintoja. Spot-hashprice raportoitiin noin 31,73–32,05 dollariksi/PH/s/päivä noin 10.–12. elokuuta 2026 **[HAVAITTU FAKTA, Luxor Hashrate Index, klusteri F]**.

**HGX B300.** NVIDIAn 8-GPU:n Blackwell Ultra -sukupolven palvelinalusta, jota käytetään tämän raportin "ammattimaisella/pk-yritystasolla" havainnollisena keskitason vaihtoehtona. NVIDIA ei julkaise virallista vähittäishintaa tai tehonkulutuslukua tälle SKU:lle, minkä vuoksi tämä taso on nimenomaisesti merkitty matalamman luottamuksen tasoksi kuin kotitalous- ja hyperskaalatasot joka tämän raportin kustannustyökirjassa **[HAVAITTU FAKTA itse teknisille tiedoille — nvidia.com HGX-tuotesivu, klusteri F; OLETUS kaikille hinta-/tehonkulutusluvuille, joita käytetään tämän raportin malleissa]**.

**Ihmistyötunti-vastine (human-hour equivalent).** OpenAI:n omaan sisäiseen, itse raportoituun arvioon perustuva luku siitä, kuinka pitkän ajan tietty tekoälytehtävä veisi ihmiseltä suorittaa, käytetty OpenAI:n toimesta kuvaamaan Codexin käyttöä (esim. "70,2 % otetuista käyttäjistä teki vähintään yhden pyynnön, joka arvioitiin ylittävän tunnin ihmistyötä") **[LÄHTEESEEN KOHDISTETTU LAUSUNTO, OpenAI:n oma blogijulkaisu, kolmannen osapuolen tarkastamaton, klusteri J]**. Tämä raportti käyttää tätä lukua vain havainnollistamaan yhtä mahdollista muuntomenetelmää token-tuotoksen ja ihmistyö-vastine-kehyksen välillä (osat III/VI), nimenomaisesti ei validoituna kertoimena, ja listaa erikseen monet ulottuvuudet (laatu, luotettavuus, valvontakuorma, konteksti), joiden osalta tekoälytyö ja ihmistyö *eivät* ole suoraan vertailukelpoisia.

**Humanoidirobottien työkapasiteetti.** Fyysisen robotiikan vastine tekoälytyökapasiteetille, tutkittu havainnollisena laajennuksena tämän raportin täydentävissä työkirjoissa: *pääoma + energia + ylläpito + käyttöaste + orkestrointi → humanoidirobotin fyysinen työkapasiteetti.* Mallinnettu käyttäen sekä havainnollista 25 000 euron SKENAARIO-OLETUS-robottihintaa että todellista havaittua/lähteeseen kohdistettua markkinahintaväliä, joka ulottuu noin 13 500 dollarista (Unitree G1, HAVAITTU FAKTA) noin 250 000 dollariin (Agility Digit, LÄHTEESEEN KOHDISTETTU LAUSUNTO konvergentin toissijaisen lähteistyksen kautta) — katso osa V ja julkaisuresurssi #11.

**Hyperskaalaaja (hyperscaler).** Yritys, joka operoi datakeskusinfrastruktuuria massiivisessa, "hyper"-mittakaavassa — käytetään yleisesti pienestä joukosta yrityksiä (ja tämän raportin kontekstissa tekoälylaboratorioista ja rahoituskumppaneista, jotka rakentavat gigawatti-luokan tekoälykampuksia), joiden infrastruktuurijalanjälki on moninkertainen tavalliseen yritysdatakeskukseen verrattuna.

---

## I

**Päättely (inference).** Vaihe, jossa *koulutettua* tekoälymallia todella ajetaan tuotoksen tuottamiseksi — vastataan kehotteeseen, generoidaan koodia, tehdään agenttimainen toimi — vastakohtana *koulutukselle* (katso alla), joka on aikaisempi, huomattavasti laskenta-intensiivisempi prosessi mallin painojen rakentamiseksi ensimmäistä kertaa. Käytännössä joka kustannusluku, vertailutulos ja työkirja tässä raportissa (tokenia/sek, $/M-tokenia, tok/s/MW) kuvaa nimenomaisesti **päättelyn** kustannusta ja läpäisykykyä, ei koulutuskustannusta, joka on erillinen ja yleensä huomattavasti suurempi kustannus, jota ei mallinneta yksityiskohtaisesti tässä.

**TULKINTA.** Katso yllä oleva näyttöluokkataulukko. Käytetty läpi tämän raportin merkitsemään kohtia, joissa teksti nimenomaisesti yhdistää faktoja, lausuntoja ja oletuksia mahdolliseksi tulkinnaksi — ja nimenomaisesti *ei* esitä tätä tulkintaa vakiintuneena faktana. Lukijoiden tulee käsitellä joka TULKINTA-merkitty kohta yhtenä mahdollisena näkökulmana, joka on avoin erimielisyydelle.

---

## J

**Jevonsin paradoksi (tässä käytettynä).** Yleinen taloudellinen malli, jossa jonkin asian halventaminen ja tehokkaammaksi tekeminen voi kasvattaa sen kokonaiskulutusta niin paljon, että kokonaiskulutus tai resurssien käyttö kasvaa sen laskemisen sijaan (nimetty 1800-luvun havainnon mukaan hiilen tehokkuudesta ja hiilen käytöstä). Viitattu osissa I/IV implisiittisenä logiikkana Sam Altmanin väitteen takana, että laskeva token-kohtainen tekoälykustannus ajaa korkeampaa, ei matalampaa, kokonaistekoälykulutusta — hänen omansa väitteensä, että "kustannus käyttää tiettyä tekoälytasoa laskee noin 10-kertaisesti jokaisen 12 kuukauden aikana... ja alemmat hinnat johtavat paljon enemmän käyttöön" on **LÄHTEESEEN KOHDISTETTU LAUSUNTO**, ja tässä siihen sovellettu Jevonsin paradoksin kehys on tämän raportin oma **TULKINTA** tästä lausunnosta, ei väite, että Altman käytti tätä nimenomaista termiä itse.

---

## K

**Kerrosten erottelu (taloudellisten kerrosten erottelu).** Tämän raportin keskeinen metodologinen sääntö, esitetty osassa II ja noudatettu joka työkirjassa: älä koskaan yhdistä raakaa energiakustannusta, laitteiston poistoihin perustuvaa kustannusta, rahoitetun omaisuuden kustannusta, täyttä käyttöinfrastruktuurikustannusta, käyttöasteella korjattua kustannusta, token-tuotantokustannusta, työkuorma-/työkapasiteettikustannusta ja tulosta/arvoa yhdeksi yhdistetyksi luvuksi. Jokainen näytetään omana rivinään omalla kaavallaan, nimenomaan siksi, että näiden yhdistäminen on yleisin tapa, jolla otsikkotason tekoälykustannusväitteet johtavat harhaan.

---

## L

**Laitteisto (hardware).** Fyysinen tietokonelaitteisto — sirut, muisti, verkkokortit, jäähdytys, koteloinnit — jota tarvitaan laskennan suorittamiseen. Ensimmäinen konkreettinen kerros energian jälkeen tämän raportin ydinketjussa.

---

## M

**Ylläpitovaraus.** Toistuva kustannusrivi (mallinnettu tämän raportin robotiikkatyökirjassa tasaisena 10 %:na hankintahinnasta vuodessa, **SKENAARIO-OLETUS**, ei valmistajan ilmoittama luku millekään nimetylle alustalle), joka kattaa korjaukset, huollon ja osien vaihdon laitteiston käyttöiän aikana.

**MoE (asiantuntijoiden yhdistelmä, Mixture of Experts).** Mallin arkkitehtuuri, jossa vain osajoukko mallin kokonaisparametreista ("asiantuntijoista") aktivoidaan minkä tahansa syötteen kohdalla, sen sijaan että ajettaisiin koko parametrimäärä joka tokenille. Tämä yleensä alentaa laskentakustannusta per token vastaavan kokoisen "tiheän" mallin verrattuna, minkä vuoksi MoE-arkkitehtuuri mainitaan osissa II/III läpäisykyky- ja kustannus-per-token-vertailujen yhteydessä (esim. NVIDIAn oma väite, että sen Vera Rubin -alusta tarvitsee "neljäsosan GPU-määrästä" kouluttaakseen MoE-malleja samassa ajassa verrattuna GB200:aan — **LÄHTEESEEN KOHDISTETTU LAUSUNTO**, klusteri A). DeepSeek-R1, malli, jota käytetään useimmissa tämän raportin lainatuissa päättelyvertailuissa, on MoE-malli.

**MTok / miljoona tokenia.** Vakioyksikkö tekoäly-API-hinnoittelulle (dollaria miljoonaa syöte- tai tuotostokenia kohti) ja vakioyksikkö, jota käytetään läpi tämän raportin kustannus-per-token-taulukoissa. Ei pidä sekoittaa *tokenia/sek*-mittariin (läpäisykykyä kuvaava nopeus) tai *tekoäly-työtuntiin* (johdettu aikaperusteinen yksikkö).

**MW / MWh (megawatti / megawattitunti).** Tehon (MW, hetkellinen nopeus) ja energian (MWh, teho ylläpidettynä tunnin ajan) yksiköt, joita käytetään läpi osien II/VI läpäisykyky-per-teho-vertailuissa (esim. "tokenia sekunnissa per MW"). Yksi MW = 1 000 kW; yksi GW = 1 000 MW.

---

## N

**NVLink.** NVIDIAn omistusoikeudellinen, nopea siru-siru-yhteenliitäntä, jota käytetään yhdistämään GPU:t räkin sisällä (esim. 130 TB/s yhteenlaskettu kaistanleveys GB300 NVL72:n 72 GPU:n yli), jotta ne voivat toimia yhtenä suurena laskentapoolina erillisten sirujen sijaan **[HAVAITTU FAKTA, NVIDIAn tuotesivu, klusteri A]**. Yhteenliitäntäkaistanleveys on yksi teknisistä tiedoista, muistin kaistanleveyden ja tarkkuusformaatin rinnalla, joka määrittää todellisen tokenia/sek-luvun — ei raaka FLOPS yksinään.

---

## O

**HAVAITTU FAKTA.** Katso yllä oleva näyttöluokkataulukko. Tiukin luokka tässä raportin järjestelmässä: se vaatii itsenäisen vahvistuksen elävää tai ensisijaista lähdettä vasten viimeistään raportin aikarajauksena 2026-08-13, tarkalla lähdeviitteellä.

**Avoimen painotuksen malli (open-weight model).** Malli, jonka koulutetut parametrit ("painot") on julkaistu ja jonka kuka tahansa riittävällä laitteistolla voi latata ja ajaa — esim. DeepSeek-R1, Qwen, Kimi, kaikki mainittuina tämän raportin *omistetun tuotantokustannuksen* malleissa — erotuksena *omistusoikeudelliseen malliin*, joka on saatavilla vain laboratorion maksullisen API:n kautta. Tämän raportin kustannusmallit hinnoittelevat tarkoituksellisesti omistettua/osuustoiminnallista laitteistoa, joka ajaa avoimen painotuksen malleja, käyttämättä koskaan omistusoikeudellisen laboratorion vähittäis-API-hintaa sijaishintaperustana omistetulle infrastruktuurille (katso *vähittäis-API-hinnoittelu* alla, ja nimenomainen metodologiakorjaus Tokenitehtaan skenaariotyökirjan osassa 2).

**Opex (käyttömenot).** Toistuvat kustannukset — sähkö, ylläpito, henkilöstö, verkottaminen, ohjelmistot — vastakohtana laitteiston kertaluonteiselle *capex*-hankintakustannukselle. Pidetty erillisenä rivinä capexista ja rahoituskustannuksesta läpi tämän raportin malleissa.

**Orkestrointi (orchestration).** Ohjelmisto- ja prosessisuunnittelukerros, joka koordinoi useita tekoälymalleja, agentteja ja työkaluja tehtävää kohti — ajoitusta, reititystä mallien välillä, rinnakkaisten agenttien-instanssien hallintaa, uudelleenyrityksien ja virheiden käsittelyä. Nimetty nimenomaisesti yhdeksi kertovista/jakavista tekijöistä, joka erottaa raa'an token-tuotoksen todellisesta *tekoälytyökapasiteetista* (osa III), ja yhdeksi viidestä syötteestä (pääoman, energian, ylläpidon ja käyttöasteen rinnalla) humanoidirobotin työkapasiteettiketjussa (osa V).

**Tulos (outcome).** Tämän raportin ydinketjussa (energia → laitteisto → laskenta → mallit → tokenit → tekoälytyökapasiteetti → digitaalinen työ → **tulokset** → arvo → toimijuus) se todellinen seuraus, jonka digitaalinen tai fyysinen työ tuottaa maailmassa — erillinen, eikä mekaanisesti taattu, sen työkapasiteetin perusteella, jota käytettiin sen tuottamiseen. Halpa, nopea, väärä vastaus skaalattuna moniagenttitiimin yli on edelleen halpa ja väärä laajassa mittakaavassa; tämä raportti toistaa tämän rajan tarkoituksellisesti joka työkirjassa sen sijaan, että lausuisi sen kerran.

---

## P

**PUE (Power Usage Effectiveness, sähkönkäytön tehokkuus).** Vakioitu datakeskuksen tehokkuusmittari: koko toimipisteen sähkönkulutus jaettuna IT-laitteistolle (siruille, palvelimille) todella toimitetulla sähköllä. PUE-arvo 1,0 tarkoittaisi nollaa ylimääräkulutusta jäähdytyksestä, valaistuksesta ja muista toimipistekuormista; todelliset datakeskukset toimivat korkeammalla arvolla. Huomio: tämän raportin omat kustannusmallit eivät itsenäisesti vahvista tiettyä nykyistä PUE-lukua millekään nimetylle hyperskaalatoimipisteelle — kun "täysi käyttöinfrastruktuurikustannus"-kerros mallinnetaan (lisäämällä toimipistekulut raa'an laitteiston ja sähkön päälle), käytetään nimenomaista havainnollista prosenttiosuutta pääomasta -**SKENAARIO-OLETUSTA** vahvistamattoman PUE-luvun sijaan, ja tämä puute todetaan avoimesti sen peittelyn sijaan.

---

## R

**Vähittäis-API-hinnoittelu.** Se, mitä laboratorio (OpenAI, Anthropic, Google) veloittaa asiakkaalta miljoonaa tokenia kohti pääsystä sen omaan omistusoikeudelliseen, valmiiseen malliin — hinta, joka sisältää laboratorion katteen, T&K-poistot, turvallisuustyön ja luotettavuustakuut. Tämä raportti käsittelee vähittäis-API-hinnoittelua tiukasti **vertailubenchmarkina**, ei koskaan kustannusperustana omistetun tai osuustoiminnallisen infrastruktuurin mallintamiseen; joka työkirjataulukko on nimenomaisesti merkitty "OMISTETTU TUOTANTO" tai "VÄHITTÄISBENCHMARK", jotta näitä kahta ei koskaan yhdistetä yhdeksi sarakkeeksi, sen jälkeen kun aiempi sisäinen luonnosteluvirhe (dokumentoitu ja säilytetty, ei peitelty, Tokenitehtaan skenaariotyökirjan osassa 2) teki juuri tämän virheen.

---

## S

**SKENAARIO-OLETUS.** Katso yllä oleva näyttöluokkataulukko. Joka esiintymä tässä raportissa on ilmaistu selkeästi oletuksena, on muokattavissa, ja määrittää tarkalleen, mitä se säätelee (esim. "20 %:n käsiraha — säätelee, kuinka paljon pääomaa rahoitetaan verrattuna etukäteen maksettuun").

**Harvuus (sparsity, 2:4-harvuus, harva vs. tiheä läpäisykyky).** Laitteisto-/mallioptimointitekniikka, joka ohittaa jäsennellyn osajoukon nolla- tai lähes nolla-arvoja laskennan aikana lisätäkseen tehokasta läpäisykykyä. NVIDIAn otsikkotason PFLOPS-luvut ovat usein *harva*-luku (noin 2x korkeampi) *tiheän* perusluvun sijaan — tämän raportin lähderekisteri merkitsee tämän erottelun nimenomaisesti yleisenä kohtana, jossa otsikkotason laitteistomarkkinointiluvut voivat johtaa harhaan, jos tiheä/harva-perusta ei ole määritelty (klusteri A).

---

## T

**TCO (omistuksen kokonaiskustannus, Total Cost of Ownership).** Laitteiston käyttökustannus kokonaisuudessaan sen käyttöiän ajalta — pääoma/rahoitus + sähkö + ylläpito + toimipistekulut — vastakohtana pelkälle hankintahinnalle. Tämä raportti rakentaa TCO:n nimetyistä, eritellyistä kerroksista (katso *kerrosten erottelu*) sen sijaan, että esittäisi yhden yhdistetyn TCO-luvun. Usein lainattu TCO-luku — "0,123 dollaria miljoonaa tokenia kohti" GB300 NVL72:lle 116 tokenilla/sek/käyttäjä, käyttäen NVIDIA Dynamoa ja TensorRT-LLM:ää — on vahvistettu suoraan NVIDIAn omalla sivustolla (tarkistettu 2026-08-13) **[klusteri A]**, mutta kuvaa vain 72-GPU:n räkkitason järjestelmää tietyllä interaktiivisuusasetuksella; sitä ei koskaan pidä käyttää yksittäisen työaseman tai pöytätietokoneluokan laitteen hinnoitteluun, mikä aliarvioisi kyseisen tason todellisen kustannuksen noin kahdella tai kolmella suuruusluokalla.

**Token.** Perusyksikkö, jota tekoälyn kielimallit prosessoivat ja generoivat — karkeasti sananpala (joskus kokonainen lyhyt sana, joskus osa pidempää sanaa), ei kokonainen sana tai merkki. Joka $/M-token-, tokenia/sek- ja tokenia/watti-luku tässä raportissa perustuu tähän yksikköön. Token-määrät *samalle* tekstinpalalle voivat vaihdella hieman eri mallien tokenisaattoreiden välillä, mikä on todellinen pienen epäjohdonmukaisuuden lähde risti-laboratoriovertailuissa osassa III.

**Tokenia/kWh, tokenia/sek, tok/s/MW ("tokenia wattia kohti").** Läpäisykyky-tehokkuusmittarit, joita käytetään läpi osan II kuvaamaan, kuinka monta tokenia annettu laitteisto voi tuottaa aikayksikköä tai kulutettua sähköyksikköä kohti. Erittäin herkkä sille, mitä mallia, tarkkuusformaattia ja "interaktiivisuus"-asetusta (tokeneita toimitettuna sekunnissa *per aktiivinen käyttäjä*, viive/läpäisykyky-kompromissi) mitataan — tämän raportin lähderekisteri havaitsi, että yleisesti lainattua "2,8 miljoonaa tok/s/MW" GB300-lukua ei voitu vahvistaa tarkaksi julkaistuksi luvuksi, kun suoraan havaitut lähiluvut vaihtelivat noin 1,67 miljoonasta 3,89 miljoonaan tok/s/MW valitusta interaktiivisuuspisteestä riippuen **[klusteri A]** — havainnollistaen, miksi tämä raportti vaatii, että joka yksittäinen tehokkuusluku ilmoittaa interaktiivisuus-/tarkkuusperustansa.

**Koulutus (training).** (Yleensä huomattavasti laskenta- ja energiaintensiivisempi) prosessi mallin painojen rakentamiseksi datasta, erotuksena *päättelylle* (jo koulutetun mallin ajamiselle). Tämän raportin kustannus- ja läpäisykykymallit keskittyvät päättelyyn; koulutuskustannukseen viitataan vain laadullisesti (esim. NVIDIAn väite, että sen Vera Rubin -alusta tarvitsee "neljäsosan GPU-määrästä" kouluttaakseen MoE-malleja tietyssä ajassa verrattuna GB200:aan — **LÄHTEESEEN KOHDISTETTU LAUSUNTO**, klusteri A), eikä sitä mallinneta erikseen dollarimääräisesti tämän raportin työkirjoissa.

---

## U

**Käyttöintensiteettivyöhyke (usage-intensity band).** Neliportainen havainnollinen asteikko, jota käytetään läpi osan III ja Tekoälytyökapasiteetin muuntotyökirjan muuntamaan token-läpäisykyky työkapasiteettikontekstiksi: **chat/neuvonantaja** (noin 10 000–30 000 tokenia/tunti), **aktiivinen kopilotti** (noin 60 000–120 000), **delegoitu yksittäisagentti** (noin 200 000–600 000), ja **raskas moniagenttiorkestrointi** (noin 1 000 000–12 000 000+, avoin ylärajaton). Joka vyöhyke on nimenomaisesti **SKENAARIO-OLETUS** — havainnollinen haarukointi, ei mitattu toimialan standardi — löyhästi tuettuna OpenAI:n omalla itse raportoidulla, tarkastamattomalla Codex-käyttötelemetrialla (klusteri J), mutta ei suoraan kalibroituna siihen.

**Käyttöaste (utilization rate).** Osuus laitteiston enimmäiskäytettävissä olevasta toiminta-ajasta tai läpäisykyvystä, joka todella käytetään, vastakohtana joutokäynnille. Yksittäinen herkkyyttä hallitsevin muuttuja joka kustannus-per-token- ja kustannus-per-tunti-mallissa tässä raportissa: kiinteät pääoma- ja rahoituskustannukset kertyvät riippumatta siitä, käytetäänkö laitteistoa, joten matalampi käyttöaste nostaa mekaanisesti tehollista kustannusta per token tai per tunti, riippumatta mistään muutoksesta laitteiston hinnassa.

---

## V

**Arvo (value).** Viimeinen, tarkoituksellisesti erotettu vaihe tämän raportin ydinketjussa — onko tekoälytyökapasiteetin tuottama tulos todella jonkin arvoista (positiivinen), arvotonta, vai vähemmän arvoinen kuin sen tuottaminen maksoi (negatiivinen) jollekin. Tämän raportin keskeinen metodologinen kanta, toistettuna joka osassa ja joka täydentävässä työkirjassa: **arvoa ei koskaan johdeta mekaanisesti mistään edeltävästä kustannus- tai kapasiteettikerroksesta.** Mikään määrä halpaa laskentaa, korkeaa läpäisykykyä tai matalaa $/tekoäly-työtuntia ei todista, että suoritettu työ oli arvokasta.

---

## T (jatkoa)

**Työkapasiteetti (working capacity).** Katso *tekoälytyökapasiteetti* ja *humanoidirobottien työkapasiteetti* yllä — yleiskäsite, jonka kaksi tässä raportissa käsiteltyä ilmentymää ovat tekoäly-/digitaalinen ja humanoidi-/fyysinen versio.

---

*Tämä sanasto julkaistaan, kuten muukin tutkimusraportti, CC BY 4.0 -lisenssillä. Lukijoita, jotka laajentavat tämän raportin malleja uusiin tasoihin, valuuttoihin tai laitteistoihin, kannustetaan lisäämään termejä tähän samaa aakkosjärjestettyä, selkokielistä, näyttöluokkatietoista muotoa käyttäen.*

---

Tämä liite ristiviittaa Globaali perustaso -työkirjaan (julkaisuresurssi #7) ja Tekoälytyökapasiteetin muuntotyökirjaan (julkaisuresurssi #9), molemmat mukana tässä julkaisupaketissa.
