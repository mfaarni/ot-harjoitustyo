from time import sleep, time
import pygame
from tiles import PodiumTile, Tile, Coins
from settings import TILE_SIZE
from player import Player
from monster import Monster
from levels_2 import Level

class Level_graphic:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        self.level_map=level_map
        self.level_logic=Level()


        # Muodostetaan sprite-groupit elementeistä
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monsters = pygame.sprite.Group()
        self.podium = pygame.sprite.GroupSingle()
        self.coins = pygame.sprite.Group()
        # lisätään sprites-taulukkoon
        self.sprites = []
        self.sprites.append(self.tiles)
        self.sprites.append(self.player)
        self.sprites.append(self.monsters)
        self.sprites.append(self.podium)
        self.sprites.append(self.coins)

        self.setup_graphic()
        self.win_time=int(time())
        self.time_write=False


    
    def setup_graphic(self):
        # tuhotaan vanhat spritet kuollessa, jotta alustaessa taso uudelleen
        # ei jää vanhoja elementtejä kummittelemaan
        for sprite in self.sprites:
            for i in sprite:
                i.kill()
        # Käydään asetuksissa määritelty tasokartta-taulukko läpi,
        # ja luodaan sen pohjalta elementit tasoon.
        for row_index, row in enumerate(self.level_map):
            for column_index, column in enumerate(row):
                # X=seinä eli tile
                if column == "X":
                    x_coordinate = column_index * TILE_SIZE
                    y_coordinate = row_index * TILE_SIZE
                    tile = Tile((x_coordinate, y_coordinate))
                    self.tiles.add(tile)
                # P=pelaaja
                if column == "P":
                    x_coordinate = column_index * TILE_SIZE
                    y_coordinate = row_index * TILE_SIZE
                    player_sprite = Player((x_coordinate, y_coordinate))
                    self.player.add(player_sprite)
                # M=monster eli hirviö
                if column == "M":
                    x_coordinate = column_index * TILE_SIZE
                    y_coordinate = row_index * TILE_SIZE
                    monster_sprite = Monster((x_coordinate, y_coordinate-15))
                    self.monsters.add(monster_sprite)
                # W= win eli voitto
                if column == "W":
                    x_coordinate = column_index * TILE_SIZE
                    y_coordinate = row_index * TILE_SIZE
                    podium_sprite = PodiumTile(
                        (x_coordinate, y_coordinate), (TILE_SIZE/1.4))
                    self.podium.add(podium_sprite)
                # C = coin eli kolikko
                if column == "C":
                    x_coordinate = column_index * TILE_SIZE
                    y_coordinate = row_index * TILE_SIZE
                    coin_sprite = Coins((x_coordinate+15, y_coordinate+16))
                    self.coins.add(coin_sprite)
    
    def draw_graphic(self):
        
        if not self.level_logic.level_won:
            # tason "palikat" liikkuvat liikkeen mukana
            self.tiles.update(self.level_logic.world_shift)
            self.tiles.draw(self.display_surface)
            # piirretään tasoon voittopaikka
            self.podium.update(self.level_logic.world_shift)
            self.podium.draw(self.display_surface)
            # piirretään tasoon hirviöt
            self.monsters.update(self.level_logic.world_shift)
            self.monsters.draw(self.display_surface)
            # piirretään tasoon hyppypalkki
            # HUOM EI TOIMI ATM

            # piirretään tasoon kolikot
            self.coins.update(self.level_logic.world_shift)
            self.coins.draw(self.display_surface)
            # piirretään tasoon hahmo
            self.player.update()
            self.player.draw(self.display_surface)
        
            # tarkistetaan osumat ja muut olennaiset
            self.horizontal_movement_collision()
            self.vertical_movement_collision()
            self.fall_to_death_graphic()
            self.level_logic.scroll_x(self.player.sprite.rect.centerx,\
                self.player.sprite.direction.x)
            self.draw_coin_counter()
        else:
            self.win_graphic()


    def horizontal_movement_collision(self):
        player=self.player.sprite
        player.rect.x += player.direction.x * self.level_logic.controls.speed
        # kentän laatat
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        # Podium
            if self.podium.sprite.rect.colliderect(player.rect):
                self.level_logic.win()
                self.win_graphic()
        # hirviöt
        for sprite in self.monsters.sprites():
            if sprite.rect.colliderect(player.rect):
                self.level_logic.setup_level()
                self.setup_graphic()
                sleep(0.5)
        # kolikot
        for coin_sprite in self.coins.sprites():
            if coin_sprite.rect.colliderect(player.rect):
                self.level_logic.coin_counter += 1
                coin_sprite.kill()

    def vertical_movement_collision(self):
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
        # Podium
        if self.podium.sprite.rect.colliderect(player.rect):
            self.level_logic.level_won = True
            self.level_logic.win()
            self.win_graphic()


    def draw_coin_counter(self):
        coin_font = pygame.font.Font("freesansbold.ttf", 40)
        coin_str = "coins: "+str(self.level_logic.coin_counter)
        coin_text = coin_font.render(coin_str, True, (255, 255, 255))
        self.display_surface.blit(coin_text, (150, 50))
    
    def fall_to_death_graphic(self):
        if self.player.sprite.rect.y>1000:
            self.level_logic.fall_to_death(self.player.sprite.rect.y)
            self.setup_graphic()


    def win_graphic(self):
        font = pygame.font.Font("freesansbold.ttf", 125)
        score_font = pygame.font.Font("freesansbold.ttf", 25)

        win_text = font.render("YOU WON!", True, (100, 200, 14))
        win_text_shadow = font.render("YOU WON!", True, (80, 170, 70))
        scores = self.level_logic.highscore.return_highscores()
        if not self.time_write:
            self.win_time=int(time() - self.level_logic.highscore.start_time)
            self.time_write=True
        spacing = 0
        nmbr = 0
        self.display_surface.fill((150, 150, 150))
        pygame.draw.rect(self.display_surface,
                        (100, 20, 120), (450, 130, 300, 1000))
        self.display_surface.blit(
            (score_font.render("HIGHSCORES", True, (255, 255, 255))), (500, 180))
        self.display_surface.blit(
            (score_font.render("Your score: " + str(self.level_logic.highscore.score-self.win_time*100+self.level_logic.coin_counter*100-1000*self.level_logic.death_counter)\
                , True, (255, 255, 255))), (500, 150))
        for score in scores:
            if int(float(score[1])) > 0:
                if nmbr<10:
                    spacing += 40
                    nmbr += 1
                    score_text = score_font.render(
                        str(nmbr) + ". " + score[0]+" : "+score[1], True, (255, 255, 255))
                    self.display_surface.blit(score_text, (465, 180+spacing))
        self.display_surface.blit(win_text_shadow, (245, 35))
        self.display_surface.blit(win_text, (250, 40))