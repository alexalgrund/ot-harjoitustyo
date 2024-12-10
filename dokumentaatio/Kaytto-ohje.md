# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/alexalgrund/ot-harjoitustyo/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Ohjelman käynnistäminen

Peli voidaan käynnistää purkamalla ladattava zip-kansio ot-harjoitustyo-viikko6.zip haluttuun sijaintiin, ja avaamalla puretun kansio juurihakemisto terminaalissa. Mene sitten terminaalinäkymässä `src`-hakemistoon ja asenna tarvittavat riippuvuudet ajamalla komento `poetry install` ennen invoke-komentojen ajamista. Myös invoke-komennot tulee ajaa `src`-hakemistossa. Taskien tiedostopolut on siis muodostettu juuri niin, että ne eivät ota huomioon juurihakemistoissa tai muissa hakemistoissa annettuja komentoja. Asennusohjeet ovat samat, jos päädyt terminaalin sijaan avaamaan juurihakemiston Visual Studio Codessa.

### Invoke-komennot ###

Ohjelman suoritus: `poetry run invoke start`

Ohjelman testaus: `poetry run invoke test`

Testikattavuusraportti: `poetry run invoke coverage-report`

Pylint-tarkastu: `poetry run invoke lint`

## Kirjautuminen

Sovellus avautuu aloitusnäyttö-näkymään:
![Screenshot from 2024-12-10 21-47-07](https://github.com/user-attachments/assets/26832227-4ef6-4708-8812-44728e00a872)

Näkymässä voi aloittaa uuden pelin hyödyntämällä kuvattuja painikkeita, katsoa tilastoja tietoja tai poistua. Jos päädyn aloittamaa uuden pelin päättymistä seuraa suurinpiirtein
tällainen loppunäyttö:![Screenshot from 2024-12-10 21-49-54](https://github.com/user-attachments/assets/512bedd3-a149-485d-9259-53502c9f6eb1)

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkymään panikkeella "Create user".

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Create"-painiketta:

![](./kuvat/kayttoohje-uusi-kayttaja.png)

Jos käyttäjän luominen onnistuu, siirrytään siirrytään käyttäjän tekemättömät työt listaavaan näkymään.

## Todojen luominen ja tehdyksi merkkaaminen

Onnistuneen kirjautumisen myötä siirrytään käyttäjän tekemättömät työt listaavaan näkymään:

![](./kuvat/kayttoohje-tehdyksi-merkkaaminen.png)

Näkymä mahdollistaa olemassaolevien todojen merkkaamisen tehdyksi painikkeella "Done" sekä uusien todojen luomisen kirjoittamalla syötekenttään tehtävän kuvauksen ja painamalla "Create"-painiketta.

Klikkaamalla näkymän oikean ylänurkan painiketta "Logout" painamalla käyttäjä kirjautuu ulos sovelluksesta ja sovellus palaa takaisin kirjaantumisnäkymään.
