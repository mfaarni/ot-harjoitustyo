import sys
from time import sleep
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from login_menu import Login

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
LOGIN = Login()
WHITE = (255, 255, 255)
COLOR_LIGHT = (170, 170, 170)
COLOR_DARK = (100, 100, 100)

QUIT_BUTTON_WIDTH = SCREEN_WIDTH-100
QUIT_BUTTON_HEIGHT = SCREEN_HEIGHT+300
START_BUTTON_WIDTH = SCREEN_WIDTH-100
START_BUTTON_HEIGHT = SCREEN_HEIGHT+100

NAME_FONT = pygame.font.SysFont('firacode', 120)
QUIT_FONT = pygame.font.SysFont('Corbel', 50)
START_FONT = pygame.font.SysFont('Corbel', 100)
TEXT_NAME = NAME_FONT.render("AARNI'S ADVENTURE", True, WHITE)
TEXT_NAME_2 = NAME_FONT.render("GAME", True, WHITE)
TEXT_QUIT = QUIT_FONT.render('QUIT', True, WHITE)
TEXT_START = START_FONT.render('START', True, WHITE)

while True:
    MOUSE = pygame.mouse.get_pos()

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            if QUIT_BUTTON_WIDTH/2 <= MOUSE[0] <= QUIT_BUTTON_WIDTH/2+140\
                    and QUIT_BUTTON_HEIGHT/2 <= MOUSE[1] <= QUIT_BUTTON_HEIGHT/2+40:
                pygame.quit()
                sys.exit()

            if START_BUTTON_WIDTH/2-80 <= MOUSE[0] <= START_BUTTON_WIDTH/2+220:
                if START_BUTTON_HEIGHT/2-20 <= MOUSE[1] <= START_BUTTON_HEIGHT/2+80:
                    for i in range(18):
                        SCREEN.fill((180-i*10, 180-i*10, 180-i*10))
                        pygame.display.update()
                        sleep(0.01)
                        LOGIN.run_login()

    SCREEN.fill((180, 230, 180))

    if QUIT_BUTTON_WIDTH/2 <= MOUSE[0] <= QUIT_BUTTON_WIDTH/2+140\
            and QUIT_BUTTON_HEIGHT/2 <= MOUSE[1] <= QUIT_BUTTON_HEIGHT/2+40:
        pygame.draw.rect(SCREEN, COLOR_LIGHT, [
            QUIT_BUTTON_WIDTH/2, QUIT_BUTTON_HEIGHT/2, 140, 40])

    else:
        pygame.draw.rect(SCREEN, COLOR_DARK, [
            QUIT_BUTTON_WIDTH/2, QUIT_BUTTON_HEIGHT/2, 140, 40])

    if START_BUTTON_WIDTH/2-80 <= MOUSE[0] <= START_BUTTON_WIDTH/2+220\
            and START_BUTTON_HEIGHT/2-20 <= MOUSE[1] <= START_BUTTON_HEIGHT/2+80:
        pygame.draw.rect(SCREEN, COLOR_LIGHT, [
            START_BUTTON_WIDTH/2-80, START_BUTTON_HEIGHT/2-25, 300, 100])

    else:
        pygame.draw.rect(SCREEN, COLOR_DARK, [
            START_BUTTON_WIDTH/2-80, START_BUTTON_HEIGHT/2-25, 300, 100])

    SCREEN.blit(TEXT_NAME, (200, 100))
    SCREEN.blit(TEXT_NAME_2, (500, 200))
    SCREEN.blit(TEXT_QUIT, (QUIT_BUTTON_WIDTH/2+25, QUIT_BUTTON_HEIGHT/2+5))
    SCREEN.blit(TEXT_START, (START_BUTTON_WIDTH /
                             2-40, START_BUTTON_HEIGHT/2-10))

    pygame.display.update()
