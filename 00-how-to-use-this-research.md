# Miten tätä tutkimusta käytetään

*Yhden sivun orientaatiomuistio. Lue tämä ennen mitään muuta paketissa.*

---

## Mikä tämä on

Neutraalin ulkopuolisen tarkkailijan tutkimussynteesi, joka rekonstruoi tekoälylaskennan taloutta — energiaa, laitteistoa, tokeneita, työkapasiteettia, omistusta — nimettyjen johtajien julkisten lausuntojen, itsenäisesti tarkistettujen laitteistospesifikaatioiden ja hinnoittelun, sekä kirjoittajan omien aiemmin julkaistujen töiden pohjalta. Joka olennainen väite on merkitty yhdellä viidestä näyttöluokasta (Havaittu fakta, Lähteeseen kohdistettu lausunto, Johdettu laskelma, Skenaario-oletus, Tulkinta), jotta lukija näkee yhdellä silmäyksellä, mikä on itsenäisesti vahvistettu, mikä on jonkun tallenteella oleva väite, mikä on laskutoimitus ja mikä on muokattavissa oleva havainnollistus.

## Mitä tämä ei ole

- **Ei sijoitus-, oikeudellista, vero-, hankinta- tai politiikkaneuvontaa.** Joka skenaariomalli tässä on muokattavissa oleva havainnollistus, joka rakentuu ilmoitetuille, näkyville oletuksille — ei ennuste tai suositus. Tämä rajaus toistetaan joka mittakaava-/investointipainotteisessa alkutekstin osassa, ei vain tässä.
- **Ei tuomio "kupla vai ei."** Raportti ei väitä, että nykyinen tekoälyinfrastruktuurikulutus olisi joko selvästi perusteltua tai selvästi kupla. Se erittelee, mitä pitäisi olla totta, jotta kulutus olisi taloudellisesti järkevää, ja erottaa itsenäisesti tarkistettavissa olevat faktat väitteistä, joita ei voida tarkistaa — jättäen lukijan itse punnitsemaan niitä.
- **Ei yksittäisen kirjoittajan mielipidekirjoitus neutraalina tutkimuksena esitettynä.** Kirjoittajalla on avattu kommersiaalinen ja edunajointiin liittyvä intressi osuustoiminnallisiin/omistusperustaisiin tekoälyinfrastruktuurimalleihin (Menetelmät §3.4). Tätä mallia sivuavat osat on merkitty käyttökohdassaan, ei vain alkusanojen vastuuvapauslausekkeessa.
- **Ei valmis, kiistämätön malli.** Se on lähtökohta, joka on rakennettu haarautettavaksi, ajettavaksi uudelleen omilla luvuilla ja väiteltäväksi.

## Mitä tämä tutkimus voi vahvistaa

- Mitä todella sanottiin, kenen sanomana, minä päivänä, ja on tämä lausunto itsenäisesti vahvistettu (Havaittu fakta / Lähteeseen kohdistettu lausunto -jako).
- Mitä annettu kustannus- tai kapasiteettiluku *mekaanisesti seuraa*, annetuilla oletuksilla — joka johdettu laskelma tässä paketissa näyttää kaavansa, ei vain tulostaan.
- Missä näyttö on ohutta, kiistanalaista tai aidosti vahvistamattomissa, nimetty selkeästi sen tasoittamisen sijaan (katso `20-appendix-known-limitations.md` koottu lista).

## Mitä tämä tutkimus ei voi vahvistaa

- Osoittautuuko nykyinen tekoälyinfrastruktuuri-investointi perustelluksi tulevan kysynnän tai tuoton valossa. Se riippuu käyttöönotosta, kilpailusta, sääntelystä ja teknologiakäyristä, jotka eivät ole vielä tapahtuneet.
- Onko mikään nimetyn johtajan tulevaisuuteen suuntautuva väite (kustannus per gigawatti, kysynnän kasvuvauhti, tuleva pääomatarve) *totta* — vain se, sanottiinko se todella, ja miten se vertautuu itsenäisiin arvioihin niiltä osin kuin niitä on olemassa.
- Yhtä "oikeaa" kustannuslukua tekoälylaskennan omistamiselle millä tahansa tasolla. Joka dollariluku tässä paketissa on skenaario, rakennettu ilmoitetuille syötteille (käyttöaste, rahoitusehdot, sähkön hinta) — muuta syötteitä, ja tuotos muuttuu. Tämä on tarkoituksellista, ei heikkous, joka pitäisi ratkaista yhdeksi luvuksi.
- Muuttuuko halpa tekoälytyökapasiteetti positiiviseksi arvoksi millekään tietylle lukijalle. Työkapasiteetti ja arvo pidetään rakenteellisesti erillään läpi raportin (osa IV) — kustannustaulukot eivät koskaan implikoi tulosta.

## Miten tätä tutkimusta haastetaan tai laajennetaan

1. **Tarkista lähderekisteri** (`02-source-register.md`, `10-appendix-source-register-formatted.md`) — joka havaittu fakta ja lähteeseen kohdistettu lausunto jäljittyy päivättyyn ensisijaiseen tai toissijaiseen lähteeseen. Jos lähde on siirtynyt, päivittynyt tai luettu väärin, se on legitiimi havainto — kirjaa se sellaisena.
2. **Aja työkirjat uudelleen omilla luvuillasi.** Täydentävät työkirjat (`03`–`08`) ja reaaliaikaisilla kaavoilla toimiva Excel-malli (`18-companion-data-model.xlsx`) paljastavat joka skenaario-oletuksen muokattavana solunä. Eri sähkön hinta, rahoituskorko tai käyttöasteoletus ei ole mallin kumoamista — se on malli toimimassa tarkoitetulla tavalla.
3. **Erota erimielisyys oletuksesta faktakorjauksesta.** "Mielestäni 60 %:n käyttöaste on epärealistinen omassa kontekstissani" on skenaarioerimielisyys (muuta solua). "Tämä vertailutulosluku on 4 räkin yhteenlaskettu tulos, ei yksittäisen räkin luku" on faktakorjaus (kirjaa se lähderekisteriä vasten). Tämä paketti käsittelee näitä kahta eri tavoin, ja niin tulisi tehdä myös sen kritiikin.
4. **Varo mittakaavan vuotamista tuotantotasojen välillä.** Kustannus-per-token-lukua yhdelle laitteistotasolle (esim. hyperskaalaräkille) ei koskaan pidä soveltaa eri tasoon (esim. pöytätietokoneeseen) — raportti merkitsee tämän selkeästi joka kohdassa, jossa se on todellinen riski (osa II, osa VI). Minkä tahansa tämän työn laajennuksen tulisi säilyttää tämä kuri.
5. **Raportoi ajautumista, ei vain erimielisyyttä.** Jos löydät luvun yhdestä resurssista (alkuteksti, diaesitys, työkirja, kaavio), joka on ristiriidassa toisen kanonisen luvun kanssa, se on virhe tämän paketin omassa sisäisessä johdonmukaisuudessa, ei mallinnusvalinta — katso `data/canonical-cost-model.csv` yksittäinen totuuden lähde, jota näiden lukujen tulisi seurata, `tools/check-canonical-consistency.py` automaattinen tarkistus, joka valvoo tätä, ja `README.md`:n tunnettujen ongelmien loki siitä, miten tällaisia havaintoja on käsitelty aiemmissa versioissa.

## Mistä aloittaa, riippuen siitä mitä haluat

Katso "Lukupolut" tiedostossa `README.md` linssikohtaiset ja syvyyskohtaiset aloituspisteet — alkuteksti, johdon tiivistelmä, työkirjat ja diaesitys on rakennettu palvelemaan eri yleisöjä eri syvyyksillä samasta jaetusta faktapohjasta, ei luettavaksi alusta loppuun kaikkien toimesta.

---

*Julkaistu CC BY 4.0 -lisenssillä alkuperäisen tekstin ja rakenteen osalta. Tutkimussynteesi ja mallinnus: Valto Loikkanen, tekoälyn avustuksella. Faktojen aikarajaus: 2026-08-13.*
