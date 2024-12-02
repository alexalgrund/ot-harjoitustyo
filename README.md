# Vaatimusmäärittely

## Pelin käynnistäminen Release-latauksessa

Pelin suorittaminen ei edellytä erilisiä tiedostoja. Pelin tarvitsemat erilliset kuva- ja äänitiedostot löytyvät juurihakemistosta ja ne on ladattau Free Sound Orgin kaltaisilta ilmaisjakelusivusoilta, joiden sisältö on tekijänoikeuksien näkökulmasta vapaata. Sovellus voidaan käynnistää purkamalla ladattava zip-kansio ot-harjoitustyo-viikko5.zip haluttuun sijaintiin, avaamalla puretun kansio juurihakemisto terminaalissa ja ajamalla sitten komento poetry run invoke start.

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
