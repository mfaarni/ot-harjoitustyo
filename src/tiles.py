import pygame
from settings import TILE_IMAGE, BACKTILE_IMAGE

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = TILE_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Backtile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = BACKTILE_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class PodiumTile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Coins(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load("src/sprites/coin.png"), (40, 40))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


class Background(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("src/sprites/background.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift/1.8
