import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load("sprites/sonic.png"), (65,65))
        self.image=pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect(topleft=pos)
        self.facing_right=True
        self.walk_meter=0

    def update(self, x_shift):
        self.rect.x += x_shift
        if self.facing_right:
            self.rect.x+=1
            self.walk_meter+=0.5
        if not self.facing_right:
            self.rect.x-=1
            self.walk_meter-=0.5
        if self.walk_meter>=150 and self.facing_right:
            self.image=pygame.transform.flip(self.image,True,False)
            self.facing_right=False
        elif self.walk_meter<=0 and not self.facing_right:
            self.image=pygame.transform.flip(self.image,True,False)
            self.facing_right=True
