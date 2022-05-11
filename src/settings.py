import time
import pygame
pygame.init()
level_map = [
    "                 M                                                                                XX      XX                        ",  # pylint: disable=line-too-long
    "               XXXXXXXXX      C                                                                  X                                  ",  # pylint: disable=line-too-long
    "          XX                 XXXXXXXXXXX                                          MC C           MCCCCCCC  M                    W   ",  # pylint: disable=line-too-long
    "                                XXXXX                                           XXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXX",  # pylint: disable=line-too-long
    "                      CC                                                      XXXXXCCCCCCCCCCCCXXXXXXXXXXXXXXXX             XXXXXXXX",  # pylint: disable=line-too-long
    "              M CCC    CC                                           M C   XXXXXXXXXCCCCCCCCCCCCXXXXXXXXXXXXXXXX  C  C  C  XXXXXXXXXX",  # pylint: disable=line-too-long
    "        CCC  XXXXXXXX  M  CC XX     CCC                     C C C XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "      W XXX    XXXX    XXXXXXX      XXX C    CCXX    CCCCC XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "  P  XXXXXX      XX    XXXXX       XXXX X    XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX M       XXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "XXXXXXXXXXX    XXXXXX   XXX    XXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
]

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = len(level_map)*TILE_SIZE
tile_image=pygame.transform.scale(
            pygame.image.load("src/sprites/tileplanks.png"), (65, 65))
player_image_right=pygame.transform.scale(
            pygame.image.load("src/sprites/rogue.png"), (35, 85))
player_image_left=pygame.transform.scale(
            pygame.image.load("src/sprites/rogue_left.png"), (35, 85))
heart_image=pygame.image.load("src/sprites/heart.png")
def draw_timer(screen, start_time):
    """piirtää näytölle ajastimen

    Args:
        screen (screen): pygame-pelin näyttö
        start_time (int): pelin aloitusaika
    """
    timer_font = pygame.font.Font("freesansbold.ttf", 40)
    timer_text = "time: " + str(int(time.time() - start_time))
    screen_clock = timer_font.render(timer_text, True, (255, 255, 255))
    screen.blit(screen_clock, (400, 50))
