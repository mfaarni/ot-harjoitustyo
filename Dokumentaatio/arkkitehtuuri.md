# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenteessa on itse pelin varsinainen koodi, sekä data ja spirtes-luokat. data-luokassa on tallennettuna pelin tulokset sql-tietokantaan, ja sprites-kansiossa ladattavat grafiikat

## Käyttöliittymä

Pelin käyttöliittymässä on neljä eri näkymää:
- Pelin aloitusruutu
- Nimen valitseminen
- itse peli
- voitto- ja tulosruutu

Kaikki näkymistä paitsi voittoruutu ovat omia luokkiaan, ja kaikki ovat toteutettuja pygamen avulla. Näkymät näkyvät ruudulla yksi kerrallaan ja niistä siirrytään toiseen osittain nappien kautta. Käyttöliittymää on pyritty eristämään sovelluslogiikasta.
Näkymistä toinen eli nimen valinta päivittyy jatkuvasti syötteen perusteella, ja antaa käyttäjälle neuvoja.
Itse pelinäkymä päivittyy jatkuvasti pelin edetessä.
Käyttöliittymä sisältää luokkia, kuten menu, login_menu sekä levels_2_graphic

## Sovelluslogiikka
Sovelluslogiikka sisältää useita luokkia, joista tärkeimmät ovat levels_2 sekä game. levels_2 vastaa itse pelikentän toiminnasta, ja game pyörittää koko peliä. 

## Tietojen pysyväistallennus
Pelissä pelaajan nimet sekä saavutetut tulokset tallennetaan SQLite-tietokantaan. Voittaessa tästä tietokannasta haetaan tulokset. tärkeitä ovat tiedostot database_connection, initialize_database sekä scores, jotka käsittelevät tietokantaa niin kirjoittamiseen kuin lukemiseen.
## Tiedostot
SQLite-tietokanta Users tallennetaan kansion data tiedostoon database.db. Sinne tallenetaan pelaajan nimi sekä kunkin nimen paras saavutettu tulos. 


```mermaid
classDiagram
  Login--|>Game
  Login--|>Settings
  Login--|>UserRepository
  Game--|>Level
  Game--|>Level_graphic
  Game--|>Settings
  Level_graphic--|>Level
  Level_graphic--|>Tile
  Level_graphic--|>Settings
  Level_graphic--|>Player
  Level_graphic--|>Monster
  Level--|>Monster
  Level--|>Player
  Level--|>Tile
  Level--|>PodiumTile
  Level--|>Coins
  Level--|>Controls
  Player--|>Controls
  
  
  class UserRepository{
    find_all()
    find_by_username()
    create()
    update_score()
    delete_all()
  }
  
  
  class Login{
    run_login()
    handle_event()
    acceptable_name()
  }


  class Level_graphic{
    setup_graphic()
    draw_graphic()
    horizontal_movement_collision()
    vertical_movement_collision()
    draw_coin_counter()
    fall_to_death_graphic()
    win_graphic()
    
  
  }
  
  
  class Level{
    scroll_x()
    setup_level()
    print_stuff()
    fall_to_death()
    win()

    

  }

  class Player{
    input()
    jump_count_zero()
    apply_gravity()
    jump()
    update()

  }

  class Monster{
    update()

  }

  class Tile{
    update()

  }

  class PodiumTile{
    update()

  }
  

  class Coins{
    update()

  }
  

  class Controls{
    keypress()
    jump_control()

  }
  

  class Settings{
    draw_timer()

  }
  class Game{
  run_game()
  }
```
