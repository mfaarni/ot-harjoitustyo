import pygame
import sys
from player import Player
from settings import *
from levels import Level
from tiles import Tile


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock=pygame.time.Clock()
level=Level(level_map,screen)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((2,55,95))
    level.draw()

    
    pygame.display.update()
    clock.tick(60*1.5)
