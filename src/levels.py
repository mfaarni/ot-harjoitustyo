from time import sleep, time
import pygame
from tiles import PodiumTile, Tile, Coins
from settings import TILE_SIZE, SCREEN_WIDTH
from player import Player
from monster import Monster
from controls import Controls


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
        self.score=100000

        # voiton värihommat
        self.colour_win = 0
        self.colour_x = 0
        self.colour_y = 0

        self.start_time = time()

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
        self.score-=5000
        # kolikot ja aika alkuarvoihin
        self.coin_counter = 0
        self.start_time = time()

        # tuhotaan vanhat spritet kuollessa, jotta alustaessa taso uudelleen ei jää vanhoja elementtejä kummittelemaan
        for sprite in self.sprites:
            for i in sprite:
                i.kill()

        # Käydään asetuksissa määritelty tasokartta-taulukko läpi,
        # ja luodaan sen pohjalta elementit tasoon.
        for row_index, row in enumerate(level_map):
            for column_index, column in enumerate(row):
                # X=seinä eli tile
                if column == "X":
                    x = column_index * TILE_SIZE  # pylint: disable=invalid-name
                    y = row_index * TILE_SIZE     # pylint: disable=invalid-name
                    tile = Tile((x, y))
                    self.tiles.add(tile)
                # P=pelaaja
                if column == "P":
                    x = column_index * TILE_SIZE  # pylint: disable=invalid-name
                    y = row_index * TILE_SIZE     # pylint: disable=invalid-name
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                # M=monster eli hirviö
                if column == "M":
                    x = column_index * TILE_SIZE # pylint: disable=invalid-name
                    y = row_index * TILE_SIZE    # pylint: disable=invalid-name
                    monster_sprite = Monster((x, y-15))
                    self.monsters.add(monster_sprite)
                # W= win eli voitto
                if column == "W":
                    x = column_index * TILE_SIZE    # pylint: disable=invalid-name
                    y = row_index * TILE_SIZE       # pylint: disable=invalid-name
                    podium_sprite = PodiumTile((x, y), (TILE_SIZE/1.4))
                    self.podium.add(podium_sprite)
                # C = coin eli kolikko
                if column == "C":
                    x = column_index * TILE_SIZE    # pylint: disable=invalid-name
                    y = row_index * TILE_SIZE       # pylint: disable=invalid-name
                    coin_sprite = Coins((x+22, y+16))
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
            self.score-=1
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
        if self.level_won:
            font = pygame.font.Font("freesansbold.ttf", 125)
            if self.colour_win < 240:
                self.colour_win += 2
            self.colour_x += 8
            self.colour_y += 8
            if self.colour_x < 1500:
                pygame.draw.rect(self.display_surface, (self.colour_win, self.colour_win, 255),
                (-550+self.colour_x, -500+self.colour_x, 800+self.colour_y, 800+self.colour_y))

            win_text = font.render("YOU WON!", True, (100, 200, 14))
            self.display_surface.blit(win_text, (250, 200))
