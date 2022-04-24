import sys
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, level_map, draw_timer
from levels import Level
def run_game():
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    level = Level(level_map, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
        if not level.level_won:
            screen.fill((2, 55, 95))
            draw_timer(screen, level.start_time)
        level.draw()
        pygame.display.update()
        clock.tick(60)
        print(level.score)