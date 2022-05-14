import pygame
from controls import Controls
from settings import PLAYER_IMAGE_LEFT, PLAYER_IMAGE_RIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = PLAYER_IMAGE_RIGHT
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(
            0, 0)  # pylint: disable=c-extension-no-member
        self.looking_forward = True
        self.controls = Controls()
        self.players_direction = 0

    def input(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.controls.player_x = 0

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.controls.player_x = self.controls.keypress("right")

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.controls.player_x = self.controls.keypress("left")
        else:
            self.controls.player_x = 0
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump()

    def player_direction(self):
        if int(self.direction[0]) == -1:
            self.image = PLAYER_IMAGE_LEFT
        if int(self.direction[0]) == 1:
            self.image = PLAYER_IMAGE_RIGHT

    def jump_count_zero(self):
        self.controls.jump_count = 0

    def apply_gravity(self):
        self.direction.y += self.controls.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if self.controls.jump_count == 0:
            self.direction.y = self.controls.jump_control()
            self.controls.jump_count += 1

    def update(self):
        self.input()
        self.player_direction()
        self.direction.x = self.controls.player_x
