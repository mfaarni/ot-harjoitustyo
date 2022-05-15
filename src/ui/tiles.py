import pygame
from services.settings import BACKGROUND_IMAGE, TILE_IMAGE, BACKTILE_IMAGE, \
                    TROPHY_IMAGE, GRASS_TILE_IMAGE, COIN_IMAGE

class Tile(pygame.sprite.Sprite):
    """Luokka joka vastaa pelin peruspalikoiden grafiikoista

    Args:
        pygame (sprite): pygame-sprite-objekti
    """
    def __init__(self, pos):
        """alustaa grafiikan
        Args:
            pos (tuple): koordinaatti kyseiselle grafiikalle, jotta saamme sen pinta-alan
        """
        super().__init__()
        self.image = TILE_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        """päivittää grafiikan sijainnin pelaajan liikkuessa

        Args:
            x_shift (int): määrä, jonka grafiikan sijainti liikkuu suunnassa x
        """
        self.rect.x += x_shift

class GrassTile(pygame.sprite.Sprite):
    """Luokka joka vastaa pelin nurmikkopalikoiden grafiikoista
    Args:
        pygame (sprite): pygame-sprite-objekti
    """
    def __init__(self, pos):
        """alustaa grafiikan
        Args:
            pos (tuple): koordinaatti kyseiselle grafiikalle, jotta saamme sen pinta-alan
        """
        super().__init__()
        self.image = GRASS_TILE_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        """päivittää grafiikan sijainnin pelaajan liikkuessa
        Args:
            x_shift (int): määrä, jonka grafiikan sijainti liikkuu suunnassa x
        """
        self.rect.x += x_shift


class Backtile(pygame.sprite.Sprite):
    """Luokka joka vastaa pelin taustaoalikoiden grafiikoista
    Args:
        pygame (sprite): pygame-sprite-objekti
    """
    def __init__(self, pos):
        """alustaa grafiikan
        Args:
            pos (tuple): koordinaatti kyseiselle grafiikalle, jotta saamme sen pinta-alan
        """
        super().__init__()
        self.image = BACKTILE_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        """päivittää grafiikan sijainnin pelaajan liikkuessa
        Args:
            x_shift (int): määrä, jonka grafiikan sijainti liikkuu suunnassa x
        """
        self.rect.x += x_shift


class PodiumTile(pygame.sprite.Sprite):
    """Luokka joka vastaa pelin pokaalin grafiikasta
    Args:
        pygame (sprite): pygame-sprite-objekti
    """
    def __init__(self, pos):
        """alustaa grafiikan
        Args:
            pos (tuple): koordinaatti kyseiselle grafiikalle, jotta saamme sen pinta-alan
        """
        super().__init__()
        self.image = TROPHY_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        """päivittää grafiikan sijainnin pelaajan liikkuessa
        Args:
            x_shift (int): määrä, jonka grafiikan sijainti liikkuu suunnassa x
        """
        self.rect.x += x_shift


class Coins(pygame.sprite.Sprite):
    """Luokka joka vastaa pelin kolilkoiden grafiikoista
    Args:
        pygame (sprite): pygame-sprite-objekti
    """
    def __init__(self, pos):
        """alustaa grafiikan
        Args:
            pos (tuple): koordinaatti kyseiselle grafiikalle, jotta saamme sen pinta-alan
        """
        super().__init__()

        self.image = COIN_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        """päivittää grafiikan sijainnin pelaajan liikkuessa
        Args:
            x_shift (int): määrä, jonka grafiikan sijainti liikkuu suunnassa x
        """
        self.rect.x += x_shift


class Background(pygame.sprite.Sprite):
    """Luokka joka vastaa pelin taustagrafiikasta
    Args:
        pygame (sprite): pygame-sprite-objekti
    """
    def __init__(self, pos):
        """alustaa grafiikan
        Args:
            pos (tuple): koordinaatti kyseiselle grafiikalle, jotta saamme sen pinta-alan
        """
        super().__init__()

        self.image = BACKGROUND_IMAGE
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        """päivittää grafiikan sijainnin pelaajan liikkuessa
        Args:
            x_shift (int): määrä, jonka grafiikan sijainti liikkuu suunnassa x
        """
        self.rect.x += x_shift/1.8
