import pygame
from controls import Controls


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Hahmon ulkoasu
        self.image = pygame.transform.scale(
            pygame.image.load("src/sprites/rogue.png"), (35, 85))
        self.rect = self.image.get_rect(topleft=pos)


        # Hahmon suunta
        self.direction = pygame.math.Vector2(
            0, 0)  # pylint: disable=c-extension-no-member
        self.looking_forward=True
        self.controls = Controls()

    # Hahmon ohjaus näppäimistön avulla, vastaanottaa näppäinsyötteen ja
    # kutsuu sen perusteella control-luokkaa, joka muuntaa pelaajan x-arvon suunnan
    def input(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.controls.player_x = 0

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.controls.player_x==-1 and self.looking_forward:
                self.image = pygame.transform.flip(self.image, True, False)
                self.looking_forward=True

            self.controls.player_x = self.controls.keypress("right")

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.controls.player_x==1 and not self.looking_forward:
                self.image = pygame.transform.flip(self.image, True, False)
                self.looking_forward=False

            self.controls.player_x = self.controls.keypress("left")
        else:
            self.controls.player_x = 0
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            self.jump()
    # Painovoima vaikuttaa hahmoon

    def jump_count_zero(self):
        self.controls.jump_count = 0

    def apply_gravity(self):
        self.direction.y += self.controls.gravity
        self.rect.y += self.direction.y

    # hahmon hyppy-ominaisuus, kutsuu luokkaa controls ja muuttaa sen mukaan hahmon vektorin arvoa.
    def jump(self):
        if self.controls.jump_count == 0:
            self.direction.y = self.controls.jump_control()
            self.controls.jump_count += 1

    # Päivittää näppäimistön painalluksia,  !!!!!!!!!HUOM ehkä turha!!!!!!!!!!

    def update(self):
        self.input()
        self.direction.x = self.controls.player_x
