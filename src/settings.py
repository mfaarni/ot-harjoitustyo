import time
import pygame
pygame.init()
level_map = [
    "                 M                                 ",
    "               XXXXXX         C                    ",
    "          XX                 XX      XXX           ",
    "                                                   ",
    "                      CC                           ",
    "              M CCC    CC                          ",
    "        CCC  XXXXXXXX  M  CCXXX     CCC         W  ",
    "        XXX    XXXX    XXXXXX       XXX C    CCXX  ",
    "  P  XXXXXX      XX    XXXX        XXXX X    XXXXX ",
    "XXXXXXXXXXX    XXXXXX   XXX    XXXXXXXXXXX XXXXXXXX",
]

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = len(level_map)*TILE_SIZE


def draw_timer(screen, start_time):
    timer_font = pygame.font.Font("freesansbold.ttf", 40)
    timer_text = "time: " + str(int(time.time() - start_time))
    screen_clock = timer_font.render(timer_text, True, (255, 255, 255))
    screen.blit(screen_clock, (400, 50))
