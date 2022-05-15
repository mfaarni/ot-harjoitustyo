import time
import pygame
pygame.init()
LEVEL_MAP = [
    "                                                                                  CCCCCCCCCCCCCCCCCCC                                                                ",  # pylint: disable=line-too-long
    "                                      GGGGGGG                                 GGGGGGGGGGGGGGGGGGGGGGGGGGG                                                            ",  # pylint: disable=line-too-long
    "                                    GGXXXXXXXGGGG                            GXXXXXBBBBBXXXXXBBBBBBBXXXXBGGG                                                         ",  # pylint: disable=line-too-long
    "                                    BBBBBBBXXXXXXGGG                         XXBBBBBYBYBYBYBYBYYBBBBBBBBBBBBGGG         GGGGGG                                       ",  # pylint: disable=line-too-long
    "                  CCCCCC            BBBBBBBBXXXXXXXXGGG                      BBBBBBYBYBYBYBYBYBYBYBBBBBBBBBBBBB        GXXXXXXGG       C    CC    C    CC   C  C   W ",  # pylint: disable=line-too-long
    "              M CCC    CC           BBBBBBBBBBBBBBBBBBBG           C C   M   BBBBBYBYBYBYBYBYBYBYBYBBBBBBBBBBBBBBC  C GXXXXXXXXXGGG   GGG   GG   GGG   GG   G  G  GGG",  # pylint: disable=line-too-long
    "        CCC  GGGGGGGG  M  CC       MBYBBBBYBBBBYBBBBYBBB    C C C GGGG  GGGGGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXGGGGGXXXXXXXXXXXXX   XXX   XX   XXX   XX   X  X  XXX",  # pylint: disable=line-too-long
    "        GGG   XXXXXX   GGGGGGG    GGXXXYYYBYYYYBYYYYBYYBCC GGGGGGGXXXX  XXXXXXXXXXXXXXXXXXXXXXXXX         XXXXXXXXXXXXXXXXXXXXXXXXX   XXX   XX   XXX   XX   X  X  XXX",  # pylint: disable=line-too-long
    "  P WGGGXXX    XXXX    XXXXX    GGXXXXXXXXXXXXXXXXXXXXXGGGGXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXM M      XXXXXXXXXXXXXXXXXXXXXXXXX   XXX   XX   XXX   XX   X  X  XXX",  # pylint: disable=line-too-long
    "GGGGGXXXXXX    XXXXGG   XXX    GXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXGGGGGGGGGXXXXXXXXXXXXXXXXXXXXXXXXX   XXX   XX   XXX   XX   X  X  XXX",  # pylint: disable=line-too-long
]

TILE_SIZE = 64
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = len(LEVEL_MAP)*TILE_SIZE
GOBLIN_IMAGE = pygame.transform.scale(
    pygame.image.load("src/sprites/goblin.png"), (45, 80))
BACKGROUND_IMAGE = pygame.image.load("src/sprites/background.png")
TILE_IMAGE = pygame.transform.scale(
    pygame.image.load("src/sprites/block.png"), (65, 65))
GRASS_TILE_IMAGE = pygame.transform.scale(
    pygame.image.load("src/sprites/block_grass.png"), (65, 65))
TROPHY_IMAGE = pygame.transform.scale(
    pygame.image.load("src/sprites/trophy.png"), (65, 65))
BACKTILE_IMAGE = pygame.transform.scale(
    pygame.image.load("src/sprites/backtile.png"), (65, 65))
PLAYER_IMAGE_RIGHT = pygame.transform.scale(
    pygame.image.load("src/sprites/adventurer.png"), (25, 90))
PLAYER_IMAGE_LEFT = pygame.transform.scale(
    pygame.image.load("src/sprites/adventurer_left.png"), (25, 90))
HEART_IMAGE = pygame.image.load("src/sprites/heart.png")
COIN_IMAGE = pygame.image.load("src/sprites/coin.png")


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
