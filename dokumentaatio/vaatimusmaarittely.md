# Vaatimusmäärittely

## Sovelluksen tarkoitus

Pieni Arcade-peli, jossa pelaaja saavuttaa pisteitä keräämällä kolikoita ja väistelee hirviöitä. Peli päättyy pelaajan osuessa hirviöön.
 Tämän jälkeen pelaaja voi aloittaa uuden pelin. | TOTEUTETTU -> Pelin runko on valmis.

## Käyttäjät

Pelaajat. ¦ TOTEUTETTU -> Päädytään siihen, että erilliset käyttäjäryhmät eivät ole aiheellisia.

## Käyttöliittymäluonnos

Päävalikko ¦ TOTEUTETTU -> Käyttöliitymä on tämän suunnitelman mukainen. Ei tarvtetta jatkokehityksellä. Jatkokehitys ideat koskevat enemmänkin sisältöä.

-> Aloita uusi peli -> Aloittaa uuden pelin, palaa päävalikkoon tai siirtyy tarkastelemaan tilastonäkymää.

-> Tarkastelee tilastonäkymää. -> Poistuu takaisin päävalikkoon.

-> Poistu pelistä.


## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
Päädytiin siihen, että erityistä kirjautumista ei toistaiseksi suunnitella, mutta toisaalta pelaajien olisi mahdollista tarkastella omia pistetilastojaan ja saada tietoa peliin käyttämästään ajasta,
jos tällainen ominaisuus olisi. | HYLÄTTY -> Peli on siinä määrin yksinkertainen, että oman nimimerkin lisääminen ei tuo pelaajalla suurta lisäinformaatiota. Tällainen ominaisuus soveltunee
paremmin laajempiin arca-peleihin, joissa on esimerkiksi useita erilaisia kenttiä.

### Kirjautumisen jälkeen

Ei erityisiä suunnitelmia toistaiseksi. | HYLÄTTY -> Päällekkäinen edellisen kohdan kanssa, joten ei tarvitse käsitellä erikseen. 

## Jatkokehitysideoita

- Pelin vaikeustaosojen nousu. | TOTEUTETTU -> Pelin vaikeutaso nousee aina 50 pisteen saavuttamisen jälkeen siten, että silmukan suoritusnopeus kasvaa 10 yksiköllä. Toisin sanoen peli nopeutuu vaikeustason kasvaessa.
- Grafiikan dynaamiset ominaisuudet (jos aikaa). | HYLÄTTY -> Liian vaikea toteuttaa annettuissa aikaraameissa.
- Mahdollisuus valita hahmo. | HYLÄTTY -> Ei tuo peliin lisää uusia mielekiintoisia elementtejä.
- Pelaaja saa ilmoituksen, jos saavuttaa pelissä uuden piste-ennätyksen. | TOTEUTETTU -> Pelin päättyessä pelin loppupistenäyttöön ilmestyy teksti "NEW RECORD", jos uusi ennätys saavutetaan.

