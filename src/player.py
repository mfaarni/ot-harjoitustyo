import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        #Hahmon ulkoasu 
        self.image=pygame.Surface((20,20))
        self.image.fill((255,255,255))
        self.rect=self.image.get_rect(topleft=pos)
        
        #Hahmon suunta
        self.direction=pygame.math.Vector2(0,0)
        #Hahmon avot
        self.speed=6
        self.gravity=0.8
        self.jump_height=-18
        self.jump_meter=0
        self.jump_count=0

    #Hahmon ohjaus näppäimistön avulla
    def input(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x=1
        elif keys[pygame.K_LEFT]:
            self.direction.x=-1
        else:
            self.direction.x=0
        
        if keys[pygame.K_SPACE]:
            self.jump()
        
    #Painovoima vaikuttaa hahmoon
    def apply_gravity(self):
        self.direction.y +=self.gravity
        self.rect.y+=self.direction.y


    #hahmon hyppy-ominaisuus
    def jump(self):
        if self.jump_meter>=0:
            self.direction.y=self.jump_height
            self.jump_meter=-100
            self.jump_count+=1


    #Päivittää näppäimistön painalluksia,  !!!!!!!!!HUOM ehkä turha!!!!!!!!!!
    def update(self):
        self.input()
        