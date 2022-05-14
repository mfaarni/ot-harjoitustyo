import time
import pygame
pygame.init()
LEVEL_MAP = [
    "                                                                                  CCCCCCCCCCCCCCCCCCC                               ",  # pylint: disable=line-too-long
    "                                                                               XXXXXXXXXXXXXXXXXXXXXXXXXX                           ",  # pylint: disable=line-too-long
    "                                    XXXXXXXXXX                                XXXXXBBBBBXXXXXBBBBBBBXXXXBXXX                    W   ",  # pylint: disable=line-too-long
    "                                    BBBBBBBXXXXXXXXX                         XXBBBBBYBYBYBYBYBYYBBBBBBBBBBBBXXX         XXXXXXXXXXXX",  # pylint: disable=line-too-long
    "                  CCCCCC            BBBBBBBBXXXXXXXXXXX                      BBBBBBYBYBYBYBYBYBYBYBBBBBBBBBBBBB        XXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "              M CCC    CC           BBBBBBBBBBBBBBBBBBBX          M   C      BBBBBYBYBYBYBYBYBYBYBYBBBBBBBBBBBBBBC  C XXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "        CCC  XXXXXXXX  M  CC       MBYBBBBYBBBBYBBBBYBBB    C C C XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "        XXX    XXXX    XXXXXXX    XXXXXYYYBYYYYBYYYYBYYBCC XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "  P  XXXXXX      XX    XXXXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXM M      XXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
    "XXXXXXXXXXX    XXXXXX   XXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # pylint: disable=line-too-long
]

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = len(LEVEL_MAP)*TILE_SIZE
BACKGROUND_IMAGE = pygame.image.load("src/sprites/background.png")
TILE_IMAGE = pygame.transform.scale(
    pygame.image.load("src/sprites/tileplanks.png"), (65, 65))
BACKTILE_IMAGE = pygame.transform.scale(
    pygame.image.load("src/sprites/backtile.png"), (65, 65))
PLAYER_IMAGE_RIGHT = pygame.transform.scale(
    pygame.image.load("src/sprites/rogue.png"), (35, 85))
PLAYER_IMAGE_LEFT = pygame.transform.scale(
    pygame.image.load("src/sprites/rogue_left.png"), (35, 85))
HEART_IMAGE = pygame.image.load("src/sprites/heart.png")


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
