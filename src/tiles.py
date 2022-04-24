import pygame

# Laattojen sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load("src/sprites/tileplanks.png"), (65, 65))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

    # voitto-kohdan sprite


class PodiumTile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

    # kolikon sprite


class Coins(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.transform.scale(
            pygame.image.load("src/sprites/coin.png"), (40, 40))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
