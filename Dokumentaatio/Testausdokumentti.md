# Testausdokumentti
Peliä on luonnollisesti testattu paljon kehitysprosessin aikana, ja sen lisäksi eri osia varten on kehitetty unittestilla toimivia testejä.

## Pelin toimivuus
Koska pygame-pelin toimivuutta on osittain vaikea testata automatisoiduilla testeillä (esim grafiikat ja eri kappaleiden hitboxit), on tätä testaamista tehty paljon manuaalisesti
Kuitenkin joitain testejä pelissä liikkumista varten on tehty testiluokassa TestMoving.

## Kentän toimivuus
Lisäksi testiluokassa TestLevels luodaan Level-luokan olio, ja testataan "kameran" liikkumista, kun pelaajan sijaintiarvo muuttuu.

## Tietokanta
Pelin tulosten tallentumista tietokantaan testataan luokassa TestDatabase, jossa luodaan uusi taulu testitietokantaan database_test.db, joka on toiminnaltaan identtinen aitoon tietokantaan nähden,
ja sille voidaan suorittaa samoja toimintoja funktioiden avulla. 
Myös luokan Scores tallennustoimintoa testataan, se tapahtuu oikeassa tietokannassa, jonne luodaan alkio ja poistetaan se testin jälkeen.

## Testikattavuus
Sovelluksen testikattavuus on 87%
![coverage](https://user-images.githubusercontent.com/102048170/168482468-2608a61f-6112-40de-9d17-54b41ecd2e8a.png)
Testaamatta jäivät initialize_database, koska se tyhjentää tyhjentää tietokannan ja sen toiminta perustuu tällä hetkellä vain pelin oikeaan tietokantaan, joten sen testaaminen ei ole kovin mielekästä.
Lisäksi pelin ohjaamisesta, tasosta sekä asetuksen kellosta puuttuu osa testeistä, mutta olennaisimmat asiat ovat testattuna.

## Asennus ja konfigurointi 
Peli on asennettu käyttöohjeen mukaan useammalle Linux-käyttöjärjestelmälle sekä yhdelle Windows-järjestelmälle. Peliä on testannut usea ihminen, eikä virheitä ole lopussa tullut esille.

# Toiminnallisuudet
Pelissä on ainoastaan alussa mahdollisuus syöttää käyttäjänimi, ja se hyväksyy vain oikean malliset nimet, tätä on testattu, ja virheellisiä syötteitä ei näytä saatavan läpi.

