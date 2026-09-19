# Viterbi Presence Tracker

Kurssin "TKT20010 Harjoitustyö: Algoritmit ja tekoäly" harjoitustyö

Ohjelman idea on päätellä asukkaan todennäköisin sijainti asunnossa käyttäen "Hidden Markov Model" epätarkkojen sensoreiden avulla hyödyntäen Viterbi-algoritmia 

# Asennus ohjeet
Käytössä on Poetry riippuvuuksien hallintaan [https://python-poetry.org/](https://python-poetry.org/)

Asenna komentorivillä komennolla:
    poetry install

# Ohjelman suoritus
Komennolla:
    poetry run python src/main.py
Pystyt ajamaan 10 huoneen kodin simulaation joka vertaa Viterbi-algoritmin tulosta siihen että luotettaisiin sensoreiden tuloksiin suoraan sen mukaan missä huoneessa ne ovat.


# Testaus
Komennolla:
    poetry run pytest
Visuaalinen raportti:
    poetry run coverage run -m pytest
    poetry run coverage html
Raportti tallennetaan tiedostoon:
    htmlcov/index.html

Laatu vaatimukset voi tarkistaa komennolla:
    poetry run pylint src