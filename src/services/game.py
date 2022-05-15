import sys
import pygame
from services.settings import SCREEN_HEIGHT, SCREEN_WIDTH, LEVEL_MAP
from ui.levels_2_graphic import LevelGraphic

def run_game(player_name):
    """Pyörittää varsinaista peliä
    Args:
        player_name (string): pelaajan nimi, joka tallennetaan sql-databaseen
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    level_graphic = LevelGraphic(LEVEL_MAP, screen, player_name)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        level_graphic.draw_graphic()
        pygame.display.update()
        clock.tick(60)
