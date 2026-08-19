# Näkökulmat / kirjoitukset — merkintämuoto

Joka tiedosto tässä hakemistossa (paitsi tämä README) on yksi Näkökulmat-merkintä, YAML-muodossa, näillä kentillä:

```yaml
title: "Artikkelin tai kirjoituksen otsikko"
author: "Kirjoittajan nimi"
date: "YYYY-MM-DD"
publication: "Missä se julkaistiin (esim. LinkedIn, Substack, nimetty julkaisu)"
url: "https://..."
topic: ["Talous", "Omistus"]   # yksi tai useampi alla olevista kategorioista
description: "Yhdestä kolmeen lausetta, jotka kuvaavat, mitä kirjoitus sanoo."
relationship: "supports | interprets | applies | criticizes | extends"
type: "original | independent | critical"   # katso määritelmät alla
language: "en"
scope: "external | internal"        # internal = kirjoittajan itsensä, external = kolmas osapuoli
discovery: "manual | submitted | backlink-auto"
status: "published"                  # published | pending-review (automaattisesti löydetyille kohteille, jotka odottavat luokittelua)
```

**Tyyppimääritelmät** (tietovaraston julkaisuohjeiden mukaisesti):
- **original** — kirjoitettu suoraan tämän tutkimuksen pohjalta Valto Loikkasen toimesta.
- **independent** — kolmas osapuoli, joka viittaa työhön, tulkitsee sitä tai soveltaa sitä, ei välttämättä samaa tai eri mieltä.
- **critical** — kolmas osapuoli, joka haastaa oletuksia, laskelmia tai johtopäätöksiä. Mukana, kun relevanttia — mukanaolo ei tarkoita kannatusta, eikä poissulkemista käytetä vain siksi, että kirjoitus on eri mieltä.

**Relationship-arvot**: `supports`, `interprets`, `applies`, `criticizes`, `extends` — kirjoitus voi yhdistää useampia; listaa ensisijainen suhde.

## Merkinnän lisääminen käsin

Kopioi `_template.yaml`, täytä kentät, tallenna se nimellä `perspectives/<lyhyt-slug>.yaml`, ja aja sitten:

```bash
python3 tools/build-perspectives.py
```

Tämä uudelleengeneroi `perspectives.html`:n joka `.yaml`-tiedostosta tässä hakemistossa.

## Näkökulman lähettäminen

Katso "Lähetä näkökulma" -osio [Näkökulmat-sivulla](https://valto.github.io/tekoalytyokapasiteetin-vallankumous/perspectives.html) elävällä sivustolla.

## Automaattinen tunnistus (suunniteltu, ei vielä kytketty)

`_pending/` sisältää ehdokasmerkintöjä, joilla on `status: pending-review` — tulevasta automaattisesta takalinkkien tunnistusputkesta, tai luonnosmerkintöjä, jotka eivät ole vielä valmiita julkaistaviksi. Tämän hakemiston tiedostoja ei koskaan renderöidä julkiselle sivustolle (`tools/build-perspectives.py` julkaisee vain `status: published`-merkinnät). Katso `docs/backlink-discovery.md` täydelle putken suunnittelulle.
