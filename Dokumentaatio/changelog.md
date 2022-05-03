# Changelog

## Viikko 3
###
- pelin peruslogiikka toteutettu
- pelistä löytyy kenttä jossa voi liikkua
- hahmolla on painovoima eikä se voi läpäistä seiniä
- liästty hyypyominaisuus ja sitä varten palkki
- Testattu, että liikkuminen toimii
## Viikko 4
###
- peliin lisätty eri ominaisuuksia:
  - pelissä on vihollisia, joita koskemalla alkaa alusta
  - peliin on lisätty kolikoita, ja niiden määrää näyttävä laskuri
  - peliin on lisätty ajastin
  - peliin on lisätty loppu, joka saavutetaan koskettamalla kentän lopussa olevaa palikkaa
  - pelissä mahdollisuus kuolla tippumalla alas
- grafiikoita päivitetty, nyt käytössä valmisgrafiikat, jotka päivitetään omiin myöhemmin
- Hyppypalkki poistettu turhana
## Viikko 5
###
- peliin lisätty aloitusmenu, josta peli aloitetaan
- peliin lisätty pisteytys, joka tallentuu tekstitiedostoon
- pelin loppuun päästäessä näytölle tulostuu highscores-lista, jossa näkyy pelikertojen pisteet parhausjärjestyksessä. 

## Viikko 6
###
- pelin aloitusmenuun lisätty nimikenttä, johon pelaaja voi antaa itselleen sopivan nimen
- kenttä ilmoittaa ongelmista ja hyväksyy vain sopivan nimen
- pelin pisteiden talletus tapahtuu nyt sql-tietokantaan, ja pisteet tallentuvat nimen mukaan
- korjattu muutama virhe, jossa kentässä liikkuminen on aiheuttanut ongelmia
