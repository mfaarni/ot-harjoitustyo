from time import sleep, time
import pygame
from tiles import PodiumTile, Tile, Backtile, Coins, Background
from settings import TILE_SIZE, HEART_IMAGE
from scores import Scores
from player import Player
from monster import Monster
from levels_2 import Level


class LevelGraphic:
    """Luokka on vastuussa tason graafisen puolen toiminnasta
    """

    def __init__(self, level_map, surface, player_name):
        """Luokan konstruktori, jossa alustetaan elementit peliruudulle

        Args:
            level_map (list): taulukko, joka kuvastaa pelin karttaa
            surface (pygame surface): ruutu, johon peli piirretään
            player_name (string): pelaajan nimi,
                joka tallennetaan pelin päätyttyä pisteiden kanssa
        """
        self.display_surface = surface
        self.level_map = level_map
        self.level_logic = Level(player_name)
        self.sprites = []
        self.sprites_append()
        self.setup_graphic()
        self.win_time = int(time())
        self.time_write = False

    def sprites_append(self):
        self.background = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        self.backtile = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monsters = pygame.sprite.Group()
        self.podium = pygame.sprite.GroupSingle()
        self.coins = pygame.sprite.Group()
        self.sprites.append(self.background)
        self.sprites.append(self.tiles)
        self.sprites.append(self.backtile)
        self.sprites.append(self.player)
        self.sprites.append(self.monsters)
        self.sprites.append(self.podium)
        self.sprites.append(self.coins)

    def setup_graphic(self):
        """Alustaa graafisen puolen elementit pelin alussa/kuoltua pelissä
        """
        for sprite in self.sprites:
            for i in sprite:
                i.kill()
        for row_index, row in enumerate(self.level_map):
            for column_index, column in enumerate(row):
                x_coordinate = column_index * TILE_SIZE
                y_coordinate = row_index * TILE_SIZE
                if column == "X":
                    self.tiles.add(Tile((x_coordinate, y_coordinate)))
                if column == "B":
                    self.backtile.add(Backtile((x_coordinate, y_coordinate)))
                if column == "P":
                    self.player.add(Player((x_coordinate, y_coordinate)))
                if column == "M":
                    self.monsters.add(Monster((x_coordinate, y_coordinate-15)))
                if column == "Y":
                    self.backtile.add(Backtile((x_coordinate, y_coordinate)))
                    self.coins.add(Coins((x_coordinate+15, y_coordinate+16)))
                if column == "W":
                    self.podium.add(PodiumTile(
                        (x_coordinate, y_coordinate), (TILE_SIZE/1.4)))
                if column == "C":
                    self.coins.add(Coins((x_coordinate+15, y_coordinate+16)))
        self.background.add(Background((-400, 0)))

    def draw_graphic(self):
        """Päivittää tason elementtien sijainnin ja piirtää ne näytölle,
        sekä tarkistaa fysiikat
        """
        if not self.level_logic.level_won:
            self.background.update(self.level_logic.world_shift)
            self.background.draw(self.display_surface)
            self.tiles.update(self.level_logic.world_shift)
            self.tiles.draw(self.display_surface)
            self.backtile.update(self.level_logic.world_shift)
            self.backtile.draw(self.display_surface)
            self.podium.update(self.level_logic.world_shift)
            self.podium.draw(self.display_surface)
            self.monsters.update(self.level_logic.world_shift)
            self.monsters.draw(self.display_surface)
            self.coins.update(self.level_logic.world_shift)
            self.coins.draw(self.display_surface)
            self.player.update()
            self.player.draw(self.display_surface)

            self.horizontal_movement_collision()
            self.vertical_movement_collision()
            self.fall_to_death_graphic()
            self.level_logic.scroll_x(self.player.sprite.rect.centerx,
                                      self.player.sprite.direction.x)
            self.draw_coin_counter()
            self.draw_health()
        else:
            self.win_graphic()
            self.click()

    def horizontal_movement_collision(self):
        """tarkistaa horisontaalisessa suunnassa tapahtuvat törmäykset
        """
        player = self.player.sprite
        player.rect.x += player.direction.x * self.level_logic.controls.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
            if self.podium.sprite.rect.colliderect(player.rect):
                self.level_logic.win()
                self.win_graphic()

        for sprite in self.monsters.sprites():
            if sprite.rect.colliderect(player.rect):
                if self.level_logic.inincibility_timer == 0:
                    self.level_logic.get_hit(-1)
                if self.level_logic.health < 1:
                    self.level_logic.setup_level()
                    self.setup_graphic()
                    sleep(0.5)

        for coin_sprite in self.coins.sprites():
            if coin_sprite.rect.colliderect(player.rect):
                self.level_logic.coin_counter += 1
                coin_sprite.kill()

    def vertical_movement_collision(self):
        """tarkistaa vertikaalisessa suunnassa tapahtuvat törmäykset
        """
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.jump_count_zero()

                elif player.direction.y < 0:

                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        if self.podium.sprite.rect.colliderect(player.rect):
            self.level_logic.level_won = True
            self.level_logic.win()
            self.win_graphic()

    def draw_coin_counter(self):
        """piirtää näytölle kolikkolaskurin
        """
        coin_font = pygame.font.Font("freesansbold.ttf", 40)
        coin_str = "coins: "+str(self.level_logic.coin_counter)
        coin_text = coin_font.render(coin_str, True, (255, 255, 255))
        self.display_surface.blit(coin_text, (150, 50))

    def draw_health(self):
        spacing = 0
        for _ in range(self.level_logic.health):
            self.display_surface.blit(HEART_IMAGE, (100+spacing, 150))
            spacing += 50

    def fall_to_death_graphic(self):
        """pelaajan pudotessa ulos kentästä alustaa sen alkuasentoon
        """
        if self.player.sprite.rect.y > 1000:
            self.level_logic.fall_to_death(self.player.sprite.rect.y)
            self.setup_graphic()

    def win_graphic(self):
        """piirtää pelin päättyessä voittonäytön, jossa näkyy tulosennätykset
        """
        font = pygame.font.Font("freesansbold.ttf", 125)
        score_font = pygame.font.Font("freesansbold.ttf", 25)
        start_again_font = pygame.font.Font("freesansbold.ttf", 35)

        win_text = font.render("YOU WON!", True, (100, 200, 14))
        win_text_shadow = font.render("YOU WON!", True, (80, 170, 70))
        start_again_text = start_again_font.render(
            "START AGAIN", True, (255, 255, 255))
        scores = self.level_logic.highscore.return_highscores()
        if not self.time_write:
            self.win_time = int(time() - self.level_logic.highscore.start_time)
            self.time_write = True
        self.display_surface.fill((150, 150, 150))
        pygame.draw.rect(self.display_surface,
                         (100, 20, 120), (450, 130, 300, 1000))
        self.display_surface.blit(
            (score_font.render("HIGHSCORES", True, (255, 255, 255))), (500, 180))
        self.display_surface.blit(
            (score_font.render("Your score: " +
                               str(self.level_logic.highscore.score
                                   -self.win_time*100+self.level_logic.coin_counter*100
                                   -1000*self.level_logic.death_counter),
                               True, (255, 255, 255))), (500, 150))
        self.draw_scores(scores, score_font)

        self.display_surface.blit(win_text_shadow, (245, 35))
        self.display_surface.blit(win_text, (250, 40))
        pygame.draw.rect(self.display_surface,
                         (100, 20, 120), (60, 470, 300, 75))
        self.display_surface.blit(start_again_text, (90, 490))

    def click(self):
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 360 and 470 <= mouse[1] <= 545:
                    self.level_logic.level_won = False
                    self.level_logic.death_counter = -1
                    self.level_logic.start_time = time()
                    self.level_logic.highscore = Scores()
                    self.setup_graphic()
                    self.level_logic.setup_level()

    def draw_scores(self, scores, score_font):
        spacing = 0
        nmbr = 0
        for score in scores:
            if int(float(score[1])) > 0:
                if nmbr < 10:
                    spacing += 40
                    nmbr += 1
                    score_text = score_font.render(
                        str(nmbr) + ". " + score[0]+" : "+str(score[1]), True, (255, 255, 255))
                    self.display_surface.blit(score_text, (465, 180+spacing))
