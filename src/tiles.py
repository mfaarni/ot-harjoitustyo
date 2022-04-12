import pygame

#Laattojen spirte
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()

        
        self.image=pygame.transform.scale(pygame.image.load("sprites/tile.png"), (65,65))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Podium_tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift



class Coins(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        
        self.image=pygame.transform.scale(pygame.image.load("sprites/white_monster.png"), (26,45))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift