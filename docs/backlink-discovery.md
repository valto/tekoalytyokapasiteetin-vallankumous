# Takalinkkien tunnistus → Näkökulmat-putki (suunnittelu)

**Tila: suunniteltu, ei kytketty.** Osassa 2 kuvatut käsin- ja lähetyspolut ovat käytössä tänään (`perspectives/*.yaml`, rakennettu `tools/build-perspectives.py`:llä). Osan 1 automaattinen hakuohjelma vaatii maksullisen API-tilauksen ja tunnistetiedot, joita tällä repositoriolla ei ole — se on dokumentoitu tässä, jotta se voidaan kytkeä myöhemmin uudelleensuunnittelematta datamallia sen ympärille.

## Miksi ei julkaista suoraan hakuohjelmasta automaattisesti

Takalinkkien hakuohjelmat nostavat esiin paljon kohinaa: peilejä, navigaatiolinkkejä, haravoituja/kokoajasivuja, sosiaalisia jakoja ilman todellista sisältöä, ja roskaa. Tämän syöttäminen suoraan julkiselle "kuka kirjoittaa tästä" -sivulle heikentäisi luottamusta Näkökulmat-osioon nopeammin kuin kasvattaisi sitä. Putki on siis suunniteltu kahteen selkeästi erotettuun vaiheeseen — **tunnistus** (halpa, automaattinen, liiaksi kattava) ja **luokittelu** (todellinen harkinta siitä, onko jokin todellinen kirjoitus) — mikään ei siirry ensimmäisestä vaiheesta julkiselle sivustolle kulkematta toisen läpi.

## Osa 1 — Tunnistus (ei vielä toteutettu; vaatii maksullisen API:n)

```
Ajastettu työ (päivittäin/viikoittain)
  → kysele takalinkkejä valto.github.io/tekoalytyokapasiteetin-vallankumous/
    ja tietyille syville sivuille (alkuteksti, keskeiset työkirjat)
  → vertaa tallennettuun "tunnetut takalinkit" -taulukkoon (source_url:n mukaan)
  → joka aidosti uudelle source_url:lle:
      → hae otsikko-/sivumetadata (tai käytä sitä, mitä takalinkki-API on jo palauttanut)
      → kirjoita ehdokastietue tiedostoon perspectives/_pending/<hash>.yaml
        status: pending-review
  → (valinnainen) LLM-kutsu laatii 1-2 lauseen kuvauksen + aihetunnisteet
    joka ehdokkaalle, edelleen status: pending-review -tilassa
  → pysähdy. Mikään tässä ei kosketa perspectives.html:ää tai julkaistua hakemistoa.
```

**API-vaihtoehdot, molemmat toteutettavissa, ei kumpikaan ilmainen:**

| | Ahrefs Backlinks API | Semrush Backlinks API (v4) |
|---|---|---|
| Palauttaa | Takalinkit verkkotunnukselle tai tietylle URL:lle | source_url, source_title, target_url, ankkuriteksti, ensi/viimeisin havaittu -päivämäärät |
| Uusi/menetetty-seuranta | Kyllä | Kyllä — nimenomaiset uusi/menetetty-takalinkkisuodattimet |
| Kustannus | Tilaus + API-lisäosa | Tilaus API-yksiköillä; yksiköitä kuluu per kutsu |
| Soveltuvuus tähän käyttöön | Hyvä | Hieman paremmin sopiva — v4-päätepisteen per-takalinkki-metadata (otsikko, ankkuri, päivämäärät) kartoittuu suoraan `perspectives/*.yaml`-skeemaan vähemmällä jälkikäsittelyllä |

**Ennen tämän osan rakentamista tarvittava päätös:** mikä tarjoaja (kustannus/kvoottikompromissi), kuka pitää API-avainta (tämän ei pitäisi asua git-repositoriossa — käytä GitHub Actions -repositorion salaisuutta, jos ajetaan CI:n kautta, tai vain-paikallista tunnistetiedostoa, jos ajetaan käsin), ja kuinka usein kysellä (päivittäin on vakio git-seurattua ehdokasjonoa varten; viikoittain riittää todennäköisesti tutkimusviitesivuston todelliselle liikenteelle).

## Osa 2 — Luokittelu (suunnittelu; voidaan toteuttaa ilman hakuohjelmaa)

Riippumatta siitä, tuleeko ehdokas yllä olevasta hakuohjelmasta tai käsin lähetyksestä, se käy läpi saman luokitteluvaiheen ennen kuin siitä tulee julkaistu Näkökulmat-merkintä:

```
ehdokas (pending-review)
  → luokittele: todellinen-kirjoitus | maininta | sitaatti | sosiaalinen-jako | navigaatio/peili | roska
  → jos todellinen-kirjoitus:
      → vahvista/muokkaa automaattisesti laadittua kuvausta ja aihetunnisteita
      → aseta type: independent (oletus) tai critical (jos kirjoitus on eri mieltä)
      → aseta status: published
  → muuten: poista ehdokastiedosto (ei säilytetä "hylätty"-arkistoa roskasta/peileistä —
    se ei palvele mitään tarkoitusta ja riskeeraa sen vahingossa julkaisemisen myöhemmin)
```

Tämän voi tehdä ihmisylläpitäjä lukemalla joka `_pending/*.yaml`-tiedoston ja joko muokkaamalla sitä paikallaan (poistamalla edeltävän `_pending/`-polun, asettamalla `status: published`, siirtämällä sen `perspectives/`-hakemistoon) tai poistamalla sen. Tekoälyavusteinen ensimmäinen kierros (laadi luokittelutunniste, kuvaus ja tunnisteet) on kohtuullinen tapa nopeuttaa tätä, mutta **itse julkaisupäätöksen tulisi pysyä ihmisen "hyväksy"-toimintana**, kunnes luokittelijan väärä-positiivinen-osuus on tiedossa — repositorion oman näyttödisipliinin periaatteen mukaisesti (Menetelmät §3.1) tarkistamaton automaattinen luokittelu on juuri sitä LÄHTEESEEN-KOHDISTETTU-ei-vielä-VAHVISTETTU-väitettä, jonka erillään pitämiseen vahvistetusta faktasta tämän hankkeen metodologia on rakennettu.

Nimenomainen luottamuskynnys (esim. "julkaise automaattisesti vain ehdokkaat, jotka luokitellaan todelliseksi kirjoitukseksi yli 90 %:n luottamuksella, kaikki muu jonottaa käsin tarkistukseen") on kohtuullinen myöhempi parannus, kun luokittelija on olemassa — ei lähtöoletus.

## Osa 3 — Mikä on todella käytössä tänään (ei API-riippuvuutta)

- **Käsin lisätyt merkinnät**: kuka tahansa ylläpitäjä kopioi `perspectives/_template.yaml`:n, täyttää sen, ja ajaa `tools/build-perspectives.py`:n. Näin kolme siemenmerkintää (kirjoittajan omat aiemmat LinkedIn-/Substack-kirjoitukset, jo vahvistettu `02-source-register.md`:ssä) lisättiin.
- **Lähetetyt merkinnät**: "Oletko kirjoittanut jotain, joka perustuu tähän työhön, viittaa siihen tai haastaa sen?" -toimintakehotus `perspectives.html`:ssä ohjaa lukijat avaamaan GitHub-issuen/PR:n samoilla kentillä. Ylläpitäjä tarkistaa ja lisää tiedoston samalla tavalla kuin käsin lisätyn merkinnän.

Molemmat näistä tuottavat jo täsmälleen saman tulostusmuodon (`perspectives/*.yaml` → `perspectives.html`), jota mahdollinen tuleva automaattinen putki syöttäisi — niin Osan 1 kytkeminen myöhemmin on lisäävää, ei uudelleensuunnittelua.
