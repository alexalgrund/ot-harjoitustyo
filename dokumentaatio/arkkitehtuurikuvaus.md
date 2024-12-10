# The Great Cutlery Hunt of Horrible Horrors

## Kuvaus
Pienimuotoinen arcade-peli, jossa ritarihahmo väistelee haavoittavia luurankoja ja kerää samalla hopeisia aterimia. Aterimista saa pelissä pisteitä siten, että
haarukka = 1p, veitsi = 2p, lusikka = 3p. Peli päättyy kun pelaaja kohtaa luurangon. Pelin alkua edeltää 5 sekunnin lähtölaskenta, jonka aikana pelaaja ehtii valmistautumaan.
Pelin tietokantaan tallennetaan viisi parasta tulosta, joissa otetaan huomioon pisteet ja pelin ajallinen kesto. Kertyvät pisteet ja peliaika striimataan ydinpelin näytöllä reaaliajassa. 
Jos on esimerkiksi on kaksi suoritusta, joiden pistemäärä on sama, mutta peliaika eroaa, pelin tilatolistan kärkeen nousee tällöin peliajaltaan nopeampi suoritus. Pelin aloitusnäytössä pelaaja voi uuden pelin aloittamisen lisäksi tarkastella pistetilastoja kuin myös pelin päätyttyä. Pelin aloitusnäyttöön on tarkoitus päästä vain sovelluksen käynnityksessä koska se ei sisällä muulta osin keskeisiä toimintoja. Pelin voi lopettaa sekä aloitus- että loppunäytöllä.


## Hakemistorakenne

project/ ├── src/ # Lähdekoodi │ ├── main.py # Pääohjelma │ ├── utils/ # Apufunktiot ja -moduulit │ └── models/ # Tietomallit ├── tests/ # Testit ├── docs/ # Dokumentaatio └── requirements.txt # Riippuvuudet


