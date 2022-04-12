```mermaid
classDiagram
  Game--|>Level
  Game--|>Settings
  Level--|>Monster
  Level--|>Player
  Level--|>Tile
  Level--|>PodiumTile
  Level--|>Coins
  Level--|>Controls
  Player--|>Controls

  class Level{
    scroll_x()
    setup_level()
    draw()
    horizontal_movement_collision()
    vertical_movement_collision()
    fall_to_death()
    draw_coin_counter()
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
```
