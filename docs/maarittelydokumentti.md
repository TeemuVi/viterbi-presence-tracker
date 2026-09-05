Määrittelydokumentti:
Läsnäolon päättely Viterbi-algoritmilla

Opinto-ohjelma: Tietojenkäsittelytieteen kandiohjelma (TKT)
Aihealue: Koneoppiminen
Ohjelmointikieli: Python
Dokumentaation kieli: Suomi (koodi ja kommentit englanniksi)
Vertaisarvioitavat kielet: Python
Ratkaistava ongelma: Ihmisten liikkeiden tunnistaminen rakennuksen eri tiloissa erilaisten anturien avulla on epätarkkaa, sillä data ei anturien epätarkkuudesta johtuen ole aina täysin luotettavaa.

Tavoitteena on selvittää todennäköisin reitti huoneiden välillä, jotta nähdään, missä seurattu kohde on todennäköisimmin liikkunut.

Harjoitustyön ydin: Ytimenä on Viterbi-algoritmin toteutus alusta saakka ja sen soveltaminen tilassa liikkumisjärjestyksen selvittämiseksi.

Algoritmit ja tietorakenteet:
Viterbi-algoritmi: Algoritmi jolla on tarkoitus löytää todennäköisin piilotettujen tilanteiden jono jolla voidaan perustella havaitut  tapahtumat. 
Tietorakenteet: Taulukot joissa määritellään kuinka todennäköistä on siirtyä huoneesta toiseen sekä kuinka usein anturit ilmaisevat havaintoja. 
Laskenta- ja muistitaulukko: Kuinka todennäköistä on huoneessa olo ja mistä ollaan tultu. 

Syötteet ja niiden käyttö:
Ohjelmalle annetaan yksinkertaistettu CSV-tiedosto peräkkäisistä havainnoista sekä tiedosto joka määrittelee siirtymä- ja emissiotodennäköisyydet .
Ohjelma palauttaa todennäköisimmän huonesijaintien järjestyksen.


Tavoitteena olevat aika- ja tilavaativuudet:
N = huoneet, T = aika-askeleet
Aikavaativuus: O(T*N^2) 
Aikajanassa on T askelta, jokaisella askeleella tutkitaan kaikki N huonetta.
Mihinkä vaan näistä N huoneista voidaan tulla mistä tahansa edelliseen aika-askeleen N huoneesta.
T*N*N
Tilavaativuus: O(T*N)
Tarvitaan kokoa T*N oleva taulukko todennäköisyyksille ja pisteille.
Myös taulukko pitämään kirjaa tulosuunnasta T*N

Lähteet:
https://en.wikipedia.org/wiki/Viterbi_algorithm
https://en.wikipedia.org/wiki/Hidden_Markov_model
