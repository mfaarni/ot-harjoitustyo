#### Käyttöohje
Lataa viimeisin [release](https://github.com/mfaarni/ot-harjoitustyo/releases) koneellesi.

## Ohjelman käynnistäminen

Asenna riippuvuudet seuraavalla komennolla:
```poetry install```
Suorita alustustoimenpiteet komennolla: 
 ```poetry run invoke build```
Käynnistä sovellus:
```poetry run invoke start```

## Kirjautuminen
Seuraavalla aloitussivulla voi painaa start
![kirj](https://user-images.githubusercontent.com/102048170/168482840-748168ce-d278-40e6-a3b0-bfa7292ae3c4.png)
Tähän tarvitse syöttää sopiva käyttäjänimi, pituus 3-6 merkkiä ja hyävksyttäviä merkkejä ovat aakkoset a-z sekä numerot 0-9. 
![kirj_2](https://user-images.githubusercontent.com/102048170/168482841-b3b9e082-c1b2-46d9-9fab-bd617199f730.png)
Virheellisillä syötteillä tulee ilmoitus.

Itse peli toimii siten, että hahmo liikkuu joko nuolinäppäimillä tai wasd-ohjauksella. Välilyönnistä hahmo hyppää.
![pelinäkymä](https://user-images.githubusercontent.com/102048170/168482843-d42de47c-759f-4b75-a92c-0970fc4f78f4.png)

Lopussa näkyy lista pelin parhaista tuloksista, sekä nappi "start again". Valitettavasti nappi jäi hieman keskeneräiseksi ja sen toimiminen saattaa vaatia useamman peräkkäisen klikkauksen.!
![win_screen](https://user-images.githubusercontent.com/102048170/168483088-fef7149d-b877-499a-a1c5-7bb2742b7caa.png)
