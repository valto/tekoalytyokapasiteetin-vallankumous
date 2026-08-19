# Miksi tekoälyyn investoidaan biljoonia?

*Luvut ja talous tekoälytyökapasiteetin vallankumouksen takana — sähköstä ja infrastruktuurista tokeneihin, robotteihin, arvoon, omistukseen ja toimijuuteen.*

**Kirjoittaja:** Valto Loikkanen
**Tila:** **v1.0.1** tutkimuspaketti, julkaistu 2026-08-14. Katso `CHANGELOG.md` mitä on muuttunut v1.0.0:sta lähtien, ja tietovaraston [Julkaisut-sivu](https://github.com/valto/tekoalytyokapasiteetin-vallankumous/releases) viitattavia, tarkistussummalla vahvistettuja tilannekuvia joka julkaisusta varten.
**Tämä on suomenkielinen käännös** alkuperäisestä englanninkielisestä julkaisusta: [github.com/valto/ai-working-capacity-revolution](https://github.com/valto/ai-working-capacity-revolution). Käännös on kirjaimellinen — luvut, päivämäärät, URL-osoitteet, lainaukset, henkilö-/yritysnimet ja osioiden numerointi pysyvät muuttumattomina; vain teksti on käännetty. Katso `TERMINOLOGY.md` käytetylle terminologialle.
**Tutkimus aloitettu:** 12. elokuuta 2026
**Faktojen aikarajaus:** 2026-08-13
**Lisenssi:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) alkuperäiselle tekstille, kaavioille ja mallirakenteelle — katso `LICENSE` täydelle soveltamisalahuomautukselle (kolmannen osapuolen lainaukset, tavaramerkit ja ulkoinen data on suljettu pois ja pysyvät omien ehtojensa alaisina).
**Ehdotettu viittaustapa:** "Tutkimussynteesi ja mallinnus: Valto Loikkanen, tekoälyn avustuksella."
**Viittaus:** katso `CITATION.cff`. **Tarkistussummat:** katso `CHECKSUMS.sha256`. **Muutosloki:** katso `CHANGELOG.md`.

## Mikä tämä on

Neutraalin ulkopuolisen tarkkailijan tutkimussynteesi, joka rekonstruoi yhdistetyn taloudellisen mallin — energia → laitteisto → laskenta → mallit → tokenit → tekoälytyökapasiteetti → digitaalinen työ → tulokset → arvo → toimijuus — Jensen Huangin (ja NVIDIA/Wall Street -rahoituspaneelin), Sam Altmanin ja Mark Zuckerbergin julkisista lausunnoista, yhdistettynä itsenäisesti tarkistettuihin laitteistospesifikaatioihin, hinnoitteluun ja vertailutuloksiin, sekä kirjoittajan omaan aiemmin julkaistuun työhön tekoälyinfrastruktuurin omistuksesta ja osuustoiminnallisista malleista.

Se ei ole toimittajaraportti, poliittinen ohjelma tai sijoitussuositus. Kuudelle lukijalinssille — Yksityishenkilö, PK-yritys/yrittäjä, Rahoitus-/infrastruktuurisijoittaja, Valtio/alue/yhteisö, Tekoälyrakentaja/-operaattori ja Kouluttaja/tutkija/toimittaja — annetaan **yhtäläinen paino ja ei priorisointijärjestystä**, tarkoituksellisella toimituksellisella päätöksellä.

Joka olennainen väite on merkitty yhdellä viidestä näyttöluokasta (Havaittu fakta / Lähteeseen kohdistettu lausunto / Johdettu laskelma / Skenaario-oletus / Tulkinta), jotta lukija näkee yhdellä silmäyksellä, mikä on itsenäisesti vahvistettu, mikä on jonkun tallenteella oleva väite, mikä on laskutoimitus ja mikä on muokattavissa oleva havainnollistus.

**Avaus:** kirjoittajalla on kommersiaalisia ja edunajointiin liittyviä intresseja henkilökohtaiseen tekoälyinfrastruktuuriin ja osuustoiminnallisiin/omistusperustaisiin tekoälymalleihin Prifinan, Digiolen, ValtoAI:n ja PIOS- ja EIOS-viitekehyksien kautta. Katso alkutekstin (`01-whitepaper.md`) Menetelmät §3.4 täydelle avaukselle ja ei-neuvonta-rajalle.

## Lukupolut — aloita tästä, ei koko paketista kerralla

Tämä paketti on rakennettu niin, että eri lukijat voivat saada yhteisen faktapohjan eri syvyyksillä, joutumatta kaikki läpikäymään samaa 89-sivuista asiakirjaa ensin:

- **Ensikertalainen lukija, mikä tahansa linssi:** aloita tiedostosta `00-how-to-use-this-research.md` (yksi sivu — mikä tämä on/ei ole, mitä se voi/ei voi vahvistaa), sitten `12-executive-brief.md`.
- **Auktoritatiivinen kartta** — `01-whitepaper.md` (+ `01-whitepaper.pdf`). Täysi malli, kaikki näyttöluokkamerkinnät, kaikki varaukset. Tämä on totuuden lähde, jota joka muu resurssi tulisi jäljittää. **PDF on itsenäinen**: se upottaa neljä argumentin kannalta kantavinta kaaviota (päästä päähän -ketju, omistusrakenne, mittakaavaspektri ja uuden arvon silta) suoraan käyttökohtaansa, jotta lukija, jolla on vain ladattu PDF, näkee ne tarvitsematta tietovarastoa. Jäljelle jäävät kaaviot (2–5, 7, 9–10) sijaitsevat vain `assets/diagrams/`-kansiossa ja itsenäisessä diaesityksessä/briiffeissä — PDF on kertova raportti keskeisimmillä visuaaleillaan upotettuna, ei täysi visuaalinen toisinto koko 11-kaavioisesta joukosta.
- **Aloituspiste** — `12-executive-brief.md`. Nopea, itsenäinen tiivistelmä lukijoille, jotka haluavat argumentin muodon syventymättä koko syvyyteen.
- **Tarkistus- ja tutkimuskerros** — täydentävät työkirjat (`03`–`08`) ja `18-companion-data-model.xlsx`. Joka kaava on näkyvissä; joka oletus on muokattava solu. Tässä tarkistat raportin laskutoimitukset tai ajat sen uudelleen omilla luvuillasi.
- **Keskustelunavaaja** — `19-slide-deck.pptx` / `13-slide-deck-outline.md` ja lyhytmuotoiset kappaleet (`14`–`16`). Argumentin esittämiseen tai jakamiseen, ei sen tarkistamiseen.
- **Ennen mihinkään tiettyyn lukuun luottamista:** tarkista `20-appendix-known-limitations.md` — koottu lista siitä, mitä tämän mallin näyttö voi ja ei voi tällä hetkellä vahvistaa (mallin suorituskyky, käyttöaste, rahoitus, sähkön hinnoittelu, käyttöönoton ajoitus, ja Ammattimaisen tason näyttökuilu).

## Paketin sisältö

| Tiedosto | Mikä se on | Kenelle |
|---|---|---|
| `00-how-to-use-this-research.md` | Yhden sivun orientaatio: neutraalin mallin kehystys, mitä tämä voi/ei voi vahvistaa, miten sitä haastetaan tai laajennetaan | Kaikille; lue tämä ensin |
| `01-whitepaper.md` | Täysi alkuteksti — alkusanat, osat I–VII, loppusanat (45 osiota) | Kaikille; auktoritatiivinen kartta |
| `02-source-register.md` | Raaka faktantarkistusloki tarkistuskierrokselta — joka väite tarkistettuna, sen näyttöluokka, ja miten se tarkistettiin | Kaikille, joka tarkistaa tietyn luvun tai lainauksen |
| `03-workbook-global-baseline.md` | Julkaisuresurssi #7 — täydet energiasta-tokeneihin-kustannuskäyrät Kotitalous-/Osuustoiminnallinen-/Ammattimainen-/Hyperskaalatasolle, globaali USD-perustaso | Kaikille, joka mallintaa omaa tekoälytehdastaloutta |
| `04-workbook-ai-working-capacity-conversion.md` | Julkaisuresurssi #9 — käyttöintensiteettitikapuu (chat → kopilotti → delegoitu agentti → raskas orkestrointi) ja ihmistyön vertailutaulukot | Kaikille, joka muuntaa $/tokenin $/tekoäly-työtunniksi |
| `05-workbook-token-factory-scenarios.md` | Julkaisuresurssi #10 — token-/tekoälytehdasskenaariot, korjattu 42 € vs. 19,50–25 €/jäsen/kuukausi -osuustoiminnallinen kustannuserittely (kaksi eri laitteistotasoa, ei ristiriita), ja Bitcoin-louhinnan energian rahaksimuunto -vertailu | Osuustoiminnalliset/yhteisöinfrastruktuurisuunnittelijat |
| `06-investment-thesis-notes.md` | Julkaisuresurssi #12 — opetuksellisia, ei-neuvonnallisia sijoitusskenaariomuistiinpanoja mittakaavatasoittain | Sijoittajat ja pääoman allokoijat (lue ei-neuvonta-raja ensin) |
| `07-workbook-humanoid-working-capacity.md` | Julkaisuresurssi #11 — humanoidirobotin ruumiillistuneen työkapasiteetin laajennus, havainnollinen 25 000 €:n esimerkki plus todellinen markkinahintavaihteluväli | Kaikille, joka laajentaa mallin fyysiseen työhön |
| `08-workbook-localized-scenario-eur-finland.md` | Julkaisuresurssi #8 — laskettu EUR/Suomi-paikallistusmalli | Kaikille, joka mukauttaa globaalin perustason omaan maahansa |
| `09-appendix-glossary.md` | Määritelmät ja merkinnät — joka tekninen/taloudellinen termi käytettynä raportissa, selkokielisesti | Uudet lukijat |
| `10-appendix-source-register-formatted.md` | Julkaisumuotoiltu versio lähderekisteristä, järjestettynä lähteen mukaan tarkistusmenetelmineen | Faktantarkistajat, toimittajat, tutkijat |
| `11-appendix-assumption-register.md` | Joka muokattava skenaario-oletus kaikkien työkirjojen yli, koottuna yhteen taulukkoon ristikkäistyökirjajohdonmukaisuushuomautuksilla | Kaikille, joka ajaa mallit uudelleen omilla luvuillaan |
| `12-executive-brief.md` | Itsenäinen, itseriittävä koko raportin tiivistelmä | Lukijat, jotka eivät lue koko raporttia |
| `13-slide-deck-outline.md` | Dia diaan-esityskäsikirjoitus, joka kattaa koko raportin | Kaikille, joka esittää tätä materiaalia |
| `14-shortform-general.md` | ~300 sanan yleisyleisölle suunnattu selittäjä | Sosiaalinen/lyhytmuotoinen jakaminen |
| `15-shortform-ownership.md` | ~300-400 sanan kappale omistuskysymyksestä (osa V) | Sosiaalinen/lyhytmuotoinen jakaminen |
| `16-shortform-value.md` | ~300-400 sanan kappale siitä, miksi halvat tokenit ≠ halpa arvo (osa IV) | Sosiaalinen/lyhytmuotoinen jakaminen |
| `17-visual-asset-briefs.md` | Kaaviospesifikaatiot Kaavioille 1–11 (kaikki 11 nyt rakennettu — katso `assets/diagrams/`) | Kuka tahansa, joka rakentaa/muokkaa lopulliset grafiikat |
| `18-companion-data-model.xlsx` | Reaaliaikaisilla kaavoilla toimiva Excel-työkirja (10 välilehteä: README, Kotitalous-/Osuustoiminnallinen-/Ammattimainen-/Hyperskaalatasot, Työkapasiteettimatriisi, Bitcoin-vertailu, Humanoidirobotti, EUR-Suomi-paikallistus, Oletusten hallinta) — rakennettu `03-04-05-07-08`:n taulukoista, muokkaa mitä tahansa keltaista oletussolua laskettaaksesi uudelleen kaiken sen alapuolella | Kaikille, joka haluaa ajaa omat lukunsa kirjoittamatta kaavoja uudelleen |
| `19-slide-deck.pptx` | 26-dian esitys rakennettu `13-slide-deck-outline.md`:stä, puhujan muistiinpanoineen | Kaikille, joka esittää tätä materiaalia |
| `20-appendix-known-limitations.md` | Koottu lista avoimista epävarmuustekijöistä (mallin suorituskyky, käyttöaste, rahoitus, sähkön hinnoittelu, käyttöönoton ajoitus, Ammattimaisen tason näyttökuilu) | Kaikille, joka päättää, kuinka paljon painoarvoa antaa tietylle luvulle |
| `assets/diagrams/diagram-01…11-*.png` | 11 valmista kaaviokuvaa, jotka on määritelty `17-visual-asset-briefs.md`:ssä — Kaavio 11 on kirjoittajan oma ennalta olemassa oleva kehyskaavio, provenienssikehystetty (näyttöluokkatunniste, viittaus, foottei) vastaamaan muuta joukkoa; muokkaamaton alkuperäinen säilytetään sen vierellä tiedostona `diagram-11-*.jpg` | Raportti-/diaesitys-/verkkokäyttö |
| `data/canonical-cost-model.csv` | Yksittäinen kanoninen lähde joka tason $/M-token- ja $/tekoäly-työtunti-luvuille | Kaikille, joka tarkistaa tai laajentaa mallia |
| `tools/check-canonical-consistency.py` | Automaattinen tarkistus, ettei alkuteksti, PDF, työkirjat, diaesitys ja xlsx ole ajautuneet pois `data/canonical-cost-model.csv`:stä | Ylläpitäjät, ennen mitä tahansa julkaisua — katso asennus alla |
| `tools/requirements.txt` | Kiinnitetyt Python-riippuvuudet johdonmukaisuustarkistajalle | Ylläpitäjät, jotka ajavat tarkistajaa |
| `CITATION.cff` | Koneluettava viittausmetadata (GitHub renderöi tämän "Cite this repository" -kehotteeksi) | Kaikille, joka viittaa tähän työhön |
| `LICENSE` | Täysi CC BY 4.0 laillinen teksti, plus soveltamisalahuomautus siitä, mikä on (ja ei ole) tämän lisenssin kattamaa | Kaikille, joka käyttää tätä materiaalia uudelleen |
| `CHECKSUMS.sha256` | SHA-256-manifesti joka tiedostolle tässä julkaisussa (vain datarivit, ei kommentteja — tavallinen `sha256sum`/`shasum`-tuotos alustojen väliselle yhteensopivuudelle), niin että julkinen kopio voidaan vahvistaa tätä täsmällistä committia vasten | Kaikille, joka vahvistaa paketin eheyden |
| `CHANGELOG.md` | Versiohistoria — mikä on muuttunut julkaisujen välillä, ja miksi | Kaikille, joka seuraa revisioita |
| `index.html`, `*.html` | GitHub Pages -sivusto — joka yllä olevalla markdown-asiakirjalla on vastaava natiivi HTML-sivu (rakennettu siitä, ei kopio), niin että koko paketti voidaan lukea sivuston sisällä siirtymättä GitHubin markdown-katseluohjelmaan | Kaikille, joka lukee elävää sivustoa osoitteessa [valto.github.io/tekoalytyokapasiteetin-vallankumous](https://valto.github.io/tekoalytyokapasiteetin-vallankumous/) |
| `diagrams.html` | Galleriasivu kaikille 11 kaaviolle, kuvateksteillä ja vaihtoehtoisella tekstillä, linkittyen `17-visual-asset-briefs.html`:ään täydelle spesifikaatiolle | Lukijat, jotka selaavat visuaalista joukkoa poistumatta sivustolta |
| `perspectives.html`, `perspectives/*.yaml` | Näkökulmat/kirjoitukset-hakemisto — alkuperäiset, itsenäiset ja kriittiset julkaisut, jotka johdettu tästä tutkimuksesta tai haastavat sen, suodatettavissa tyypin/aiheen mukaan. Katso `perspectives/README.md` merkintäskeemalle | Kaikille, joka seuraa laajempaa keskustelua tämän työn ympärillä, tai lähettää oman kirjoituksensa |
| `docs/backlink-discovery.md` | Suunnittelu (ei vielä toteutettu) automaattiselle takalinkkien tunnistus → luokittelu → Näkökulmat-putkelle | Ylläpitäjät, jotka harkitsevat Ahrefs/Semrush-API-integraatiota |
| `tools/build-pages.py`, `tools/page-template.html` | Generoi joka markdown-lähteisen `*.html`-sivun `.md`-lähteestään, ristiviitteillä uudelleenkirjoitettuina pysymään sivuston sisällä | Ylläpitäjät, minkä tahansa markdown-sisältömuutoksen jälkeen — katso alla |
| `tools/build-perspectives.py`, `tools/perspectives-template.html` | Generoi `perspectives.html`:n joka `perspectives/*.yaml`-merkinnästä | Ylläpitäjät, näkökulman lisäämisen/muokkaamisen jälkeen |

## Pages-sivuston uudelleenrakentaminen sisältömuutoksen jälkeen

Joka `*.html`-tiedosto tietovaraston juuressa paitsi `index.html` ja `diagrams.html` (käsin kirjoitetut) ja `perspectives.html` (generoitu erillisellä skriptillä, alla) generoidaan vastaavasta `.md`-tiedostostaan — **ei käsin muokata generoitua `.html`-tiedostoa**; muokkaa markdown-lähdettä ja rakenna uudelleen:

```bash
python3 tools/build-pages.py
```

Tämä uudelleengeneroi kaikki sivut ja kirjoittaa uudelleen ristiviitteet niiden välillä (linkki toiseen seurattuun `.md`-tiedostoon muuttuu linkiksi kyseisen tiedoston `.html`-sivulle), niin että lukeminen pysyy Pages-sivuston sisällä sen sijaan, että siirryttäisiin GitHubin markdown-katseluohjelmaan. Vaatii `pandoc`:n `PATH`:issa.

`perspectives/*.yaml`-merkinnän lisäämisen tai muokkaamisen jälkeen, rakenna Näkökulmat-hakemisto uudelleen:

```bash
python3 tools/build-perspectives.py
```

Vaatii `pyyaml`:n (katso `tools/requirements.txt`).

## Johdonmukaisuustarkistajan ajaminen

`tools/check-canonical-consistency.py` vahvistaa, että alkuteksti, rakennettu PDF, täydentävä Excel-työkirja ja diaesitys ovat kaikki yhtenäisiä `data/canonical-cost-model.csv`:n kanssa — yksittäinen totuuden lähde tasojen kustannusluvuille. Se epäonnistuu suljettuna: puuttuva riippuvuus, puuttuva tiedosto tai rikkinäinen Python-ympäristö raportoidaan epäonnistumisena, ei hiljaisesti ohitettuna, niin että `PASS`-tulokseen voi luottaa tarkoittavan, että joka tarkistus todella ajettiin.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tools/requirements.txt
python3 tools/check-canonical-consistency.py
```

**Tunnettu ympäristöongelma joissakin macOS/Homebrew-asennuksissa:** jos järjestelmäsi oletus `python3` raportoi `ImportError: ... pyexpat ...` tai `No module named expat`, kyseisen Python-käännöksen XML-tuki on rikki (Homebrew `libexpat`-versioristiriita), ja joka tarkistus, joka koskettaa xlsx:ää tai pptx:ää, epäonnistuu — tämä on todellinen ympäristöongelma, jota tarkistaja oikein kieltäytyy peittämästä, ei virhe tässä skriptissä. Käytä eri Python-asennusta (esim. `pyenv`-hallittua käännöstä, tai `python3.11` uudesta Homebrew `python@3.11`-asennuksesta) luodaksesi yllä olevan virtuaaliympäristön sen sijaan.

## Tarkistussummien vahvistaminen

```bash
shasum -a 256 -c CHECKSUMS.sha256      # macOS
sha256sum -c CHECKSUMS.sha256          # Linux/GNU coreutils
```

`CHECKSUMS.sha256` sisältää vain tavallisia tiiviste/tiedostonimirivejä — ei kommentteja tai otsikkotekstiä — niin että molemmat yllä olevat työkalut hyväksyvät sen ilman varoituksia.

## Tila ja tunnetut avoimet kohteet

Tämä on täydellinen v1.0-luonnos, tuotettu tekoälyavusteisella tutkimus- ja mallinnustyönkululla, itsenäisellä vahvistuskierroksella, osiokohtaisilla faktajohdonmukaisuustarkastuksilla, ja deterministisellä (ei tekoälyn uudelleengeneroimalla) lopullisella koontivaiheella, jotta voidaan varmistaa, ettei mitään sisältöä pudotettu tai katkaistu kokoamisen aikana.

Tunnetut kohteet, merkitty läpinäkyvästi itse paketin sisällä:

- **Ratkaistu (2026-08-13):** aiempi "42 € vs. 19,50–25 €/jäsen/kuukausi" -osuustoiminnallinen kustannuskohta ei ollutkaan ristiriita — kaksi lukua kuvaavat kahta eri laitteistotasoa (havainnollinen 100 000 €:n jaettu työasemaluokan kone vs. 4 699 dollarin NVIDIA DGX Spark -yksiköiden pooli), ei kilpailevia arvioita samasta osuuskunnasta. Katso `05-workbook-token-factory-scenarios.md` §1a/§1b ja `11-appendix-assumption-register.md` rivi 6a korjatulle, täysin tarkistettavalle erittelylle.
- **Ratkaistu (2026-08-13):** "0,123 dollaria/M tokenia" GB300-luokan päättelyluku on nyt vahvistettu suoraan NVIDIAn omalla sivustolla (aiemmin merkitty VAHVISTAMATTOMAKSI). Se koskee erityisesti 72-GPU:n GB300 NVL72 -räkkiä 116 tokenilla/sek/käyttäjä käyttäen NVIDIA Dynamoa ja TensorRT-LLM:ää — sitä ei saa käyttää minkään työaseman tai pöytätietokoneluokan laitteen hinnoitteluun. Katso `03-workbook-global-baseline.md` §5.7.
- Useat laitteisto-/hintasyötteet (Ammattimaisen tason HGX B300 -solmun hinnoittelu/teho, hyperskaalaräkin capex, havainnolliset 100 000 €:n DGX-Station-luokan ja 25 000 €:n humanoidirobotin hinnat) ei ole julkista lähdettä ja on merkitty ⚠ läpi paikkamerkeiksi, ei vahvistetuiksi luvuiksi — NVIDIA ei julkaise vähittäishintoja DGX Stationille tai HGX B300:lle.
- **Ratkaistu (2026-08-13):** diaesitys, kaaviot ja täydentävä työkirja ovat nyt valmiita binääritiedostoja (`19-slide-deck.pptx`, `assets/diagrams/*.png`, `18-companion-data-model.xlsx`) markdown-spesifikaatioiden sijaan — työkirjan kaavat ja kaaviot vahvistettiin itsenäisesti lähdemarkdownia vasten rakennuksen aikana (yksi hyperskaala-käyttöastekaavavirhe ja kaksi kaaviosuunnitteluvirhettä havaittiin ja korjattiin tällä tavalla).
- **Ratkaistu (2026-08-13):** lopullinen yhteensovituskierros löysi ja korjasi klusterin vanhentuneita Kotitalous-/Osuustoiminnallisen tason lukuja, joita ei ollut päivitetty, kun tämän raportin kanoniset vaihteluvälit vahvistettiin — alkuteksti, `05-workbook-token-factory-scenarios.md`, `13-slide-deck-outline.md`, `19-slide-deck.pptx` ja `assets/diagrams/diagram-08-scale-spectrum.png` lainaavat nyt kaikki yksittäistä kanonista Kotitalous (1,37–11,89 dollaria/M tokenia) ja Osuustoiminnallinen (1,99–7,62 dollaria/M tokenia) -vaihteluväliä ja niiden oikein johdettuja $/tekoäly-työtunti-lukuja. Samalla kierroksella korjattiin 1000-kertainen yksikkövirhe Bitcoin-louhinnan energian rahaksimuunto -vertailussa (raportin §14, Tokenitehtaan skenaariotyökirjan §5) — korjattu laskutoimitus kääntää tämän kohdan alkuperäisen havainnollisen johtopäätöksen: kanonisella Kotitaloustason tuotantokustannuksella arvotettuna, tekoälytokenien bruttotulo per MWh-vastine ylittää jopa tehokkaat Bitcoin-louhintakalustot, ei jää niiden alle kuten aiempi luonnos väitti. Kaksi tekstimerkintää `18-companion-data-model.xlsx`:ssä, jotka oli tallennettu rikkinäisinä kaavoina (olisivat näyttäneet `#NAME?`:n), muunnettiin myös tavalliseksi tekstiksi.
- **Ratkaistu (2026-08-14):** tämä paketti on nyt julkaistu GitHub Pages -sivustona osoitteessa [valto.github.io/ai-working-capacity-revolution](https://valto.github.io/ai-working-capacity-revolution/) (englanninkielinen alkuperäinen), seuraten `main`:ia — katso yllä oleva Tila-rivi siitä, miten elävä sivusto liittyy viimeksi tagattuun julkaisuun. Tämän suomenkielisen käännöksen omaa Pages-sivustoa koskeva tila päivitetään erikseen.

Ennen mitä tahansa julkista julkaisua, ihmisen suorittama tarkistuskierros koko alkutekstistä ja työkirjoista suositellaan, erityisesti yllä oleville yhteensovitus- ja paikkamerkkikohteille.
