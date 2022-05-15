# Tasohyppelypeli
Proketina on pygamen avulla toteutettu tasohyppelypeli.
Pelissä voi nimetä itsensä, jonka jälkeen peli alkaa ja kentällä voi liikkua keräten kolikoita ja väistellen esteitä ja vihollisia. Pelin grafiikat ovat kaikki itse luotuja. Pelin lopussa näkee omat pisteensä sekä tietokannassa olevien pelaajien huippupisteet. 

## Release
#### [Viimeisin release:](https://github.com/mfaarni/ot-harjoitustyo/releases/tag/viikko6)
## Dokumentaatio
#### [Käyttöohje]((https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/käyttöhje.md))
#### [Vaatimuusmäärittely](https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/vaatimuusmaarittely.md)
#### [Työaikakirjanpito](https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/Ty%C3%B6aikakirjanpito.md)
#### [Changelog](https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/changelog.md)
#### [Arkkitehtuuri](https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/arkkitehtuuri.md)
#### [Testausdokumentti] (https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/testausdokumentti.md)

## Asennus

1. Asenna riippuvuudet seuraavalla komennolla:
```poetry install```
2. Suorita alustustoimenpiteet komennolla: 
 ```poetry run invoke build```
HUOM! Tämä poistaa kaikki pistetulokset, joten suositellaan vain ensimmäisellä kerralla tai testauksen vaatiessa
3. Käynnistä sovellus:
```poetry run invoke start```

## Komentorivitoiminnot
**Ohjelman käynnistys:**
```bash
poetry run invoke start
```

**Ohjelman testaus:**
```bash
poetry run invoke test
```

**Testikattavuus:**
``` bash
poetry run invoke coverage-report
```

**Pylint-raportti:**
```bash
poetry run invoke lint
```

