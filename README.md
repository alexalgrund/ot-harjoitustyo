# Vaatimusmäärittely

## Pelin käynnistäminen Release-latauksessa

Pelin suorittaminen ei edellytä erilisiä tiedostoja. Pelin tarvitsemat erilliset kuva- ja äänitiedostot löytyvät juurihakemistosta ja ne on ladattau Free Sound Orgin kaltaisilta ilmaisjakelusivusoilta, joiden sisältö on tekijänoikeuksien näkökulmasta vapaata. eli voidaan käynnistää purkamalla ladattava zip-kansio **ot-harjoitustyo-viikko6.zip** haluttuun sijaintiin, ja avaamalla puretun kansio juurihakemisto terminaalissa. Mene sitten terminaalinäkymässä **src**-hakemistoon ja asenna tarvittavat riippuvuudet ajamalla komento **poetry install** ennen invoke-komentojen ajamista. Myös invoke-komennot tulee ajaa **src**-hakemistossa. Taskien tiedostopolut on siis muodostettu juuri niin, että ne eivät ota huomioon juurihakemistoissa tai muissa hakemistoissa annettuja komentoja. Asennusohjeet ovat samat, jos päädyt terminaalin sijaan avaamaan juurihakemiston **Visual Studio Codessa**.

Invoke-komennot

Ohjelman suoritus: **poetry run invoke start**

Ohjelman testaus: **poetry run invoke test**

Testikattavuusraportti: **poetry run invoke coverage-report**

Pylint-tarkastu: **poetry run invoke pylint**

## Kuvaus

Pieni videopeli, jossa pelaaja kerää pisteitä keräämällä erilaisia esineitä samalla, kun välttelee hirviöitä. Peli päättyy, kun hirviö saavuttaa pelaajan.

## Käyttöliittymän kuvaus

Aluksi pelaajalle näytetään infosivu, joka kertoo pelin idean. Pelaaja voi valita aloittavansa pelin tai tarkastella parhaita tuloksia.  
Jos pelaaja valitsee pelin aloittamisen, ennen varsinaisen pelialueen käynnistymistä näkyy muutaman sekunnin lähtölaskenta, joka antaa pelaajalle aikaa valmistautua.

Pelin päättyessä näytetään "Game over" -näkymä. Pelaaja voi tämän jälkeen joko poistua pelistä tai aloittaa uuden pelin.

Ennen pelialueelle siirtymistä pelaaja voi valita käyttäjänimen. Käyttäjänimet näkyvät parhaiden tulosten listassa.

## Tulevaisuuden kehitysideat

- Pelin ideaa voisi laajentaa useisiin osioihin: esimerkiksi eri vaikeustasot ja niin edelleen.
- Moninpelimahdollisuus.
- Pelin visuaalinen ilme: staattiset vai dynaamiset grafiikat?

[Työaikakirjanpito](/dokumentaatio/tuntikirjanpito.md)

[Vaatimusäärittely](/dokumentaatio/vaatimusmaarittely.md)

[Pakkauskaavio](/dokumentaatio/arkkitehtuuri.md)

[Release-julkaisu](https://github.com/alexalgrund/ot-harjoitustyo/releases/tag/viikko5)

