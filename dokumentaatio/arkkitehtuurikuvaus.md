# The Great Cutlery Hunt of Horrible Horrors

## Kuvaus
Pienimuotoinen arcade-peli, jossa ritarihahmo väistelee haavoittavia luurankoja ja kerää samalla hopeisia aterimia. Aterimista saa pelissä pisteitä siten, että
haarukka = 1p, veitsi = 2p, lusikka = 3p. Peli päättyy kun pelaaja kohtaa luurangon. Pelin alkua edeltää 5 sekunnin lähtölaskenta, jonka aikana pelaaja ehtii valmistautumaan.
Pelin tietokantaan tallennetaan viisi parasta tulosta, joissa otetaan huomioon pisteet ja pelin ajallinen kesto. Kertyvät pisteet ja peliaika striimataan ydinpelin näytöllä reaaliajassa. 
Jos on esimerkiksi on kaksi suoritusta, joiden pistemäärä on sama, mutta peliaika eroaa, pelin tilatolistan kärkeen nousee tällöin peliajaltaan nopeampi suoritus. Pelin aloitusnäytössä pelaaja voi uuden pelin aloittamisen lisäksi tarkastella pistetilastoja kuin myös pelin päätyttyä. Pelin aloitusnäyttöön on tarkoitus päästä vain sovelluksen käynnityksessä koska se ei sisällä muulta osin keskeisiä toimintoja. Pelin voi lopettaa sekä aloitus- että loppunäytöllä.


## Hakemistorakenne
- ot-harjoitustyo/
  - .coverage
  - .coveragerc
  - .pylintrc
  - .README.md
  - tasks.py
  - dokumentaatio/
    - arkkitehtuuri.md
    - changelog.md
    - tuntikirjanpito.md
    - vaatimusmaarittely.md
  - src/
    - images/
      - fork.png
      - knife.png
      - knight.png
      - skeleton.png
      - spoon.png
      - wall.png
    - sounds/
      - beep.wav
      - crush.wav
      - surpirse.wav
      - wump.wav
    - tests/
      - __init__.py
      - main_test.py
    - database.py
    - game_engine.py
    - main.py
    - resoucres.py
    - score_base.db


    
### `ot-harjoitustyo/`
**.coveragerc**: Määrittelee mm. mistä hakemistosta testikattavuusraportti kerätään.

**.pylintrc**: Määritellee mm. mitkä kaikki virheet otetaan huomioon Pylint-tarkastuksessa.

**tasks.py**: Sisältää invoke-komentojen ajamista ohjaavan koodin.

#### `dokumentaatio/`
Sisältää projektin vaiheiden kirjanpidon **changelog.md** -tiedostossa ja ohjelman rakennetta koskevat kuvaukset.

#### `src/`
**images/**: Ohjelman kuvatiedostot.

**sounds/**: Ohjelman äänitiedostot.

**tests/**: Ohjelmassa ajattevien testien kannalta keskeiset tiedot ja niitä ohjaava koodi **main_test.py** - tiedostossa.

**database.py**: Ohjelman tietokantaa hallinoiva moduuli.

**game_engine.py**: Pelimoottoria hallinoiva moduuli.

**main.py**: Pääpelin moduuli.

**resources.py**: Ohjelman kuva- ja äänitiedostoja sekä niitten toistamista hallinoiva moduuli.

**score_base.db**: Ohjelman SQL-tietokanta.

























