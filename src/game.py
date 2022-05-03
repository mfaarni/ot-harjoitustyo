import sys
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, level_map, draw_timer
from levels_2 import Level
from levels_2_graphic import LevelGraphic


def run_game(player_name):
    """Pyörittää varsinaista peliä

    Args:
        player_name (string): pelaajan nimi, joka tallennetaan sql-databaseen
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    level = Level(player_name)
    level_graphic = LevelGraphic(level_map, screen, player_name)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not level.level_won:
            screen.fill((2, 55, 95))
            draw_timer(screen, level.start_time)
        level_graphic.draw_graphic()
        pygame.display.update()
        clock.tick(60)
