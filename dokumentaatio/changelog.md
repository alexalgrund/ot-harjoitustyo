## Viikko3
- Luotiin pelin runko src-tiedostoon ja rakennettiin kokeilumielessä muutama alustava testi.

Ongelmia:
- Testit eivät jostain syystä löydä kuvia oikeasta hakemistosta.
- Pelissä ilmenee suorituksen aikana "main not respond" -viiveitä, jotka eivät ole kriittisiä pelin suorituksella.

## Viikko 4
- Yritettiin jakaa ohjelma luokkiin, mutta havaittiin että tämä lähinnä vaikeuttaa ohjelman toimintaan, joten pitäydytään proseduraalisessa ohjelmointityylissä.
Ongelma saatiin korjattua vasta refaktoroimmalla konstruktorin ja funktion initialize_game() sisällöt.
- Koska edellisellä viikolla toteutettiin toiminnallisuuksia verraten paljon tällä viikolla keskityttin yksityiskohtiin. Muutettiin hieman käyttöliittymän
kuvausta ja pelaajalle tarkoitettuja opastetekstejä.
- Kehitysideoista tulee lopulta mieleen lähinnä asteittain tapahtuva pelin vaikeustason nousu. Oman hahmon luonti ei tuo peliin mukaan kovin mielekiintoisia
ominaisuuksia, joten luovutaan siitä.

- Tehtiin Pylintin ohjeiden mukaan korjausehdotuksia.
 1. Pylint ei josain syystä pysty tunnistamaan Pygame-moduulia täysin, josta aihetuu että se herjaa näppäintapahtumista.
Tästä ei kuitenkaan aiheudu pelin suorituksen kannalta ongelmaa, joten suljetaan tapaus W0201 Pylint-ilmoitusten ulkopuolella.
2. Peliin kuuluu mahdollisuus aloittaa uusi peli GAME OVERIN jälkeen, joten keskeisiä muuttujia ei kannata alustaa konstruktorissa, vaan
niitä varten tarvitaan oma funktionsa, jota voidaan toisintaa. Pylint on tästä eri mieltä, joten suljetaan myös tapaukset E1101 ja E0606
Pylint-testauksen ulkopuolelle.

## Viikko5
- Lisättiin ohjelmaan ominaisuudet: vaikeustason nousu ja ilmoitus, kun pelaaja saavuttaa uuden piste-ennätyksen. Pelin vaikeustaso nousee 50 pisteen välein siten,
että pääsilmukan suoritusnopeus kasvaa aina tällöin 10 yksiköllä.
- Sijoitettiin pelin kuvat ja äänet omiin alihakemistoihinsa src-päähakemiston alle ja korjattiin koodia tämän muutoksen mukaiseksi.
- Päädytään siihen, että pelin toiminnallisuus on nyt riittävä, eikä peliin enää lisätä sisällöllisesti uusia asioita. Seuraavat kaksi viikkoa
käytetään järjestämällä nyt proseduraalisessa muodossa oleva koodi luokkiin, tekemällä tältä kannalta tarpeellinen refaktorointi ja kirjoittamalla pelille
riittävän kattava testitiedosto.
- Lisättiin myös sekvensikaavio kuvaamaan pelin pääluokkaa eli funktiota maingame().

## Viikko6
- Korjattiin viimesimmä Pylint-virheet ja jaettiin ohjelma mielekkäisiin luokkiin ja useampaan tiedostoon.
- Laadittiin ohjelman rakennetta kuvaava arkkitehtuurikuvaus, käyttöohje sekä suoritettiin docstring-dokumentaatio.
- Tarkistettiin SQL-tietokannan toimivuus Release-versiota varten.
- Ohjelma on rakenteellisesti lopullisessa muodossaan, eikä sitä aleta enää kehittämään enempää muute kuin bugien ilmetessä.
Projektin viimeisimmät viikot käytetään ohjelman testien kirjoittamiseen.

## Viikko7
- Peli on valmis arviointia varten.
- Päädytään siihen, että pelin automatisoitu testaus on vaikeasti saavutettavissa sillä peli ei sisällä niin selkeitä in- ja outputteja. Mielekkäiden testien laatiminen vaatisi myös paljon sellaista osaamista, jota tällä kurssilla ei käsitellä. Testausdokumenttia ei tästä syystä liitetä tällä kertaa mukaan. Loppullisesta vaatimusmäärittellystä käyvät ilmi pelin luomisen eri vaiheet siltä varalta, että esitettyihin ideoihin on mielekiintoa palata vielä myöhemmin.
- Projektissa on käytetty kielimalleja ChatGPT ja Google Gemini soveltuvin osin koodin debuggaukseen, generointiin ja rakenteen parantamiseen.

