from time import sleep, time
import pygame
from tiles import PodiumTile, Tile, Coins
from settings import TILE_SIZE, SCREEN_WIDTH
from player import Player
from monster import Monster
from controls import Controls
from scores import Scores


class Level:
    def __init__(self, level_map, surface):
        # Alustetaan näyttö ja suoritetaan kartalla tason luonti
        self.display_surface = surface
        self.level_map = level_map
        # aluksi kamera pysyy paikallaan
        self.world_shift = 0
        # funktio totetuttaa ikään kuin kameran liikkumisen hahmon mukana,
        # todellisuudessa liikkuu tason elementit hahmon ollessa paikallaan.
        self.level_won = False

        # lasketaan kolikot
        self.coin_counter = 0
        # Pelin Score
        self.score = 8000

        # voiton värihommat
        self.colour_win = 0
        self.colour_x = 0
        self.colour_y = 0

        self.start_time = time()
        self.highscore = Scores()
        self.controls = Controls()

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

        self.setup_level(level_map)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        # Liike tapahtuu hahmon sijainnin ja suunnan mukaan
        if player_x < (SCREEN_WIDTH/2-400) and direction_x < 0:
            self.world_shift = 6
            self.controls.speed = 0

        elif player_x > (SCREEN_WIDTH/2+200) and direction_x > 0:
            self.world_shift = -6
            self.controls.speed = 0
        else:
            self.world_shift = 0
            self.controls.speed = 6

    # Tason luonti
    def setup_level(self, level_map):
        if self.score > 1000:
            self.score -= 1000
        # kolikot ja aika alkuarvoihin
        self.coin_counter = 0
        self.start_time = time()
        # tuhotaan vanhat spritet kuollessa, jotta alustaessa taso uudelleen
        # ei jää vanhoja elementtejä kummittelemaan
        for sprite in self.sprites:
            for i in sprite:
                i.kill()
        # Käydään asetuksissa määritelty tasokartta-taulukko läpi,
        # ja luodaan sen pohjalta elementit tasoon.
        for row_index, row in enumerate(level_map):
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

    # Päivitetään pelinäkymää jatkuvasti piirtämällä näytölle muutokset
    def draw(self):
        # päivitetään hyppy-palkki
        # !!!!!!Hyppy-palkki ei toimi optimoinnin jälkeen!!!!
        if not self.level_won:
            # tason "palikat" liikkuvat liikkeen mukana
            self.tiles.update(self.world_shift)
            self.tiles.draw(self.display_surface)
            # piirretään tasoon voittopaikka
            self.podium.update(self.world_shift)
            self.podium.draw(self.display_surface)
            # piirretään tasoon hirviöt
            self.monsters.update(self.world_shift)
            self.monsters.draw(self.display_surface)
            # piirretään tasoon hyppypalkki
            # HUOM EI TOIMI ATM

            # piirretään tasoon kolikot
            self.coins.update(self.world_shift)
            self.coins.draw(self.display_surface)
            # piirretään tasoon hahmo
            self.player.update()
            self.player.draw(self.display_surface)
            # tarkistetaan osumat ja muut olennaiset
            self.horizontal_movement_collision()
            self.vertical_movement_collision()
            self.fall_to_death()
            self.scroll_x()
            self.draw_coin_counter()
            if self.score > 1:
                self.score -= 1
        
        if self.level_won:
            self.win()

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * self.controls.speed
        # kentän laatat
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
        # Podium
            if self.podium.sprite.rect.colliderect(player.rect):
                self.win()
        # hirviöt
        for sprite in self.monsters.sprites():
            if sprite.rect.colliderect(player.rect):
                self.setup_level(self.level_map)
                sleep(0.5)
        # kolikot
        for coin_sprite in self.coins.sprites():
            if coin_sprite.rect.colliderect(player.rect):
                self.coin_counter += 1
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
            self.level_won = True

    def fall_to_death(self):
        if self.player.sprite.rect.y > 1000:
            self.setup_level(self.level_map)

    def draw_coin_counter(self):
        coin_font = pygame.font.Font("freesansbold.ttf", 40)
        coin_str = "coins: "+str(self.coin_counter)
        coin_text = coin_font.render(coin_str, True, (255, 255, 255))
        self.display_surface.blit(coin_text, (150, 50))

    def win(self):
        self.highscore.save_score(self.score+self.coin_counter*200)
        font = pygame.font.Font("freesansbold.ttf", 125)
        score_font = pygame.font.Font("freesansbold.ttf", 25)

        win_text = font.render("YOU WON!", True, (100, 200, 14))
        win_text_shadow = font.render("YOU WON!", True, (80, 170, 70))
        scores = self.highscore.return_highscores()
        spacing = 0
        nmbr = 0
        self.display_surface.fill((150, 150, 150))
        pygame.draw.rect(self.display_surface,
                        (100, 20, 120), (450, 130, 300, 1000))
        self.display_surface.blit(
            (score_font.render("HIGHSCORES", True, (255, 255, 255))), (500, 180))
        self.display_surface.blit(
            (score_font.render("Your score: " + str(self.score+self.coin_counter*200+1)\
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
