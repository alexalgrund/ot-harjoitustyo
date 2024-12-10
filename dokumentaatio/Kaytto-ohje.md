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

Näkymässä voi aloittaa uuden pelin hyödyntämällä kuvattuja painikkeita, katsoa tilastoja tietoja tai poistua. Jos päädyt aloittamaa uuden pelin päättymistä seuraa suurinpiirtein
tällainen loppunäyttö:![Screenshot from 2024-12-10 21-49-54](https://github.com/user-attachments/assets/512bedd3-a149-485d-9259-53502c9f6eb1)

Tässä tilassa pelin voi aloitusnäyttöä vastaavalla tavalla, joko aloittaa uudestaan, katsoa tilastotietoja tai poistua. Tästä tilasta ei ole enää tarkoituksena päästä
aloitusnäyttöön.

## Tietokanta

Ohjelma luo automaattisesti pistetilastoja ylläpitävän SQL-tietokannan, jos sellaista ei ole vielä. Ohjelman release-versio sisältää jo jonkilaisia valmiita rekisteröityjä 
pelisuorituksia.
