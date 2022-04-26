# Tasohyppelypeli
#### Proketina on pygamen avulla toteutettu tasohyppelypeli.

## Release
#### [Viimeisin release:](https://github.com/mfaarni/ot-harjoitustyo/releases/tag/viikko5)
## Dokumentaatio
#### [Vaatimuusmäärittely](https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/vaatimuusmaarittely.md)
#### [Työaikakirjanpito](https://github.com/mfaarni/ot-harjoitustyo/blob/81b437cff5313e9c2026115d7361b8168dae3197/Dokumentaatio/Ty%C3%B6aikakirjanpito.md)
#### [Changelog](https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/changelog.md)
#### [Arkkitehtuuri](https://github.com/mfaarni/ot-harjoitustyo/blob/master/Dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet seuraavalla komennolla:
```poetry install```
2. Käynnistä sovellus:
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

