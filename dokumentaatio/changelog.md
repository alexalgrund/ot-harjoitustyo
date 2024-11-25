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
