import time
import pygame
pygame.init()
level_map = [
    "                 M                                                                                                                  ",  # pylint: disable=line-too-long
    "               XXXXXX         C                                                                                                     ",  # pylint: disable=line-too-long
    "          XX                 XX      XXX                                          M              M         M                    W   ",  # pylint: disable=line-too-long
    "                                                                                XXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXX",  # pylint: disable=line-too-long
    "                      CC                                                      XXXXX            XXXXXXXXXXXXXXXX             XXXXXXXX",  # pylint: disable=line-too-long
    "              M CCC    CC                                           M     XXXXXXXXXXXX      XXXXXXXXXXXXXXXXXXX           XXXXXXXXXX",  # pylint: disable=line-too-long
    "        CCC  XXXXXXXX  M  CC XX     CCC                           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "        XXX    XXXX    XXXXXXX      XXX C    CCXX          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "  P  XXXXXX      XX    XXXXX       XXXX X    XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX M       XXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "XXXXXXXXXXX    XXXXXX   XXX    XXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
]

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = len(level_map)*TILE_SIZE


def draw_timer(screen, start_time):
    timer_font = pygame.font.Font("freesansbold.ttf", 40)
    timer_text = "time: " + str(int(time.time() - start_time))
    screen_clock = timer_font.render(timer_text, True, (255, 255, 255))
    screen.blit(screen_clock, (400, 50))
