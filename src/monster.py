import pygame


class Monster(pygame.sprite.Sprite):
    """Luokka monster on pelin vihollisia varten tehty luokka, joka säilyttää niiden arvot sekä
    funktion update

    Args:
        pygame.sprite.Sprite (pygame.sprite.Sprite): Pygamen spirte, eli
        käytännössä hirviön graafinen kuva
    """
    def __init__(self, pos):
        """alustetaan hirviön ulkonäkö ja toiminta

        Args:
            pos (int): hirviön sijainti kartalla
        """
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("src/sprites/float_skel_white.png"), (38, 80))
        self.rect = self.image.get_rect(topleft=pos)
        self.facing_right = True
        self.walk_meter = 0

    def update(self, x_shift):
        """vastaa edestakaisin kävelystä

        Args:
            x_shift (int): koordinaattiarvo, jonka mukaan hirviö liikkuu kentällä
        """
        self.rect.x += x_shift
        if self.facing_right:
            self.rect.x += 1
            self.walk_meter += 0.5
        if not self.facing_right:
            self.rect.x -= 1
            self.walk_meter -= 0.5
        if self.walk_meter >= 150 and self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = False
        elif self.walk_meter <= 0 and not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
            self.facing_right = True
