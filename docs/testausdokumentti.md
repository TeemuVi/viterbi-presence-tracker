# Testausdokumentti
sovellus testattu hyödyntäen pytest-työkalua

## Mitä on testattu
1. Tyhjä havainto lista.
2. Kahden huoneen välinen liike.
3. Testataan mitä tapahtuu kun annetaan mahdoton liikkuminen huoneiden välillä.

## Kattavuusraportti
Kattavuusraportti antaa täydet 100%

## Testien ajaminen
Komentoriviltä käskyllä
    poetry run pytest

html-raportti
    poetry run coverage run -m pytest
    poetry run coverage html
Tallentuu tiedostoon htmlcov/index.html.