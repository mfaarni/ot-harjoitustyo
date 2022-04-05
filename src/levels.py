import pygame
from tiles import Tile
from jump_bar import Jump_bar, Jump_bar_bottom
from settings import tile_size, screen_width
from player import Player




class Level:
    def __init__(self, level_map,surface):
        #Alustetaan näyttö ja suoritetaan kartalla tason luonti
        self.display_surface=surface
        self.setup_level(level_map)

        #aluksi kamera pysyy paikallaan
        self.world_shift=0

    #funktio totetuttaa ikään kuin kameran liikkumisen hahmon mukana, 
    #todellisuudessa liikkuu tason elementit hahmon ollessa paikallaan.
    def scroll_x(self):
        player = self.player.sprite
        player_x=player.rect.centerx
        direction_x=player.direction.x

        #Liike tapahtuu hahmon sijainnin ja suunnan mukaan
        if player_x < (screen_width/2-400) and direction_x < 0:
            self.world_shift= 6
            player.speed=0

        elif player_x > (screen_width/2+200) and direction_x > 0:
            self.world_shift = -6
            player.speed=0
        else:
            self.world_shift=0
            player.speed=6


    #Tason luonti
    def setup_level(self,level_map):
        #Muodostetaan sprite-groupit elementeistä
        self.tiles=pygame.sprite.Group()
        self.player=pygame.sprite.GroupSingle()
        self.jump_bar=pygame.sprite.Group()


        #Käydään asetuksissa määritelty tasokartta-taulukko läpi,
        #ja luodaan sen pohjalta elementit tasoon.
        for row_index, row in enumerate(level_map):
            for column_index, column in enumerate(row):
                
                #X=seinä eli tile
                if column=="X":
                    x= column_index * tile_size
                    y= row_index * tile_size
                    tile= Tile((x,y),tile_size)
                    self.tiles.add(tile)
                #P=pelaaja
                if column=="P":
                    x= column_index * tile_size
                    y= row_index * tile_size
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

        player=self.player.sprite
        jump_bar_sprite=Jump_bar((player.jump_meter))
        jump_bar_bottom_sprite=Jump_bar_bottom()
        self.jump_bar.add(jump_bar_bottom_sprite)
        self.jump_bar.add(jump_bar_sprite)

    #Päivitetään pelinäkymää jatkuvasti piirtämällä näytölle muutokset
    def draw(self):
        player = self.player.sprite
        #tason "palikat" liikkuvat liikkeen mukana
        self.tiles.update(self.world_shift)
        #päivitetään hyppy-palkki

        # !!!!!!Hyppy-palkki ei toimi optimoinnin jälkeen!!!!
        self.jump_timer(player)


        self.tiles.draw(self.display_surface)
        self.jump_bar.update(player.jump_meter)
        #print(player.jump_meter)
        self.jump_bar.draw(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)
    


        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.scroll_x()





    
    def horizontal_movement_collision(self):
        player=self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player=self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):

                player.jump_meter=0
                player.jump_count=0


                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y=0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y=0


    
    def jump_timer(self,player):
        if player.jump_meter<0:
            if player.jump_count==1:
                player.jump_meter+=5
            elif player.jump_count==2:
                player.jump_meter+=2.5
            elif player.jump_count>2:
                player.jump_meter+=1.5