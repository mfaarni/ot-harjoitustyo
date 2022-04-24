import time
import pygame
pygame.init()
level_map = [
    "                 M                                                                                                                  ",
    "               XXXXXX         C                                                                                                     ",
    "          XX                 XX      XXX                                                                                        W   ",
    "                                                                                XXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXX",
    "                      CC                                                      XXXXX            XXXXXXXXXXXXXXXX             XXXXXXXX",
    "              M CCC    CC                                                 XXXXXXXXXXXX      XXXXXXXXXXXXXXXXXXX           XXXXXXXXXX",
    "        CCC  XXXXXXXX  M  CCXXX     CCC                           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "        XXX    XXXX    XXXXXX       XXX C    CCXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXX",
    "  P WXXXXXX      XX    XXXX        XXXX X    XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX M       XXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXX    XXXXXX   XXX    XXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = len(level_map)*TILE_SIZE


def draw_timer(screen, start_time):
    timer_font = pygame.font.Font("freesansbold.ttf", 40)
    timer_text = "time: " + str(int(time.time() - start_time))
    screen_clock = timer_font.render(timer_text, True, (255, 255, 255))
    screen.blit(screen_clock, (400, 50))
