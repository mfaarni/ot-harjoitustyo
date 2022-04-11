import sys
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, level_map
from levels import Level

pygame.init( ) # pylint: disable=no-member
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock=pygame.time.Clock()
level=Level(level_map,screen)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # pylint: disable=no-member
            pygame.quit() # pylint: disable=no-member
            sys.exit()
    screen.fill((2,55,95))
    level.draw()
    pygame.display.update()
    clock.tick(60)
