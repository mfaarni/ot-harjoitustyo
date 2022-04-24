import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
import sys
from game import run_game
from time import sleep
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

white = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)

QUIT_BUTTON_WIDTH = SCREEN_WIDTH-100
QUIT_BUTTON_HEIGHT = SCREEN_HEIGHT+100
START_BUTTON_WIDTH = SCREEN_WIDTH-100
START_BUTTON_HEIGHT = SCREEN_HEIGHT-200

# defining a font
quit_font = pygame.font.SysFont('Corbel', 50)
start_font = pygame.font.SysFont('Corbel', 100)

# rendering a text written in
# this font
text_quit = quit_font.render('QUIT', True, white)
text_start = start_font.render('START', True, white)

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if QUIT_BUTTON_WIDTH/2 <= mouse[0] <= QUIT_BUTTON_WIDTH/2+140 and QUIT_BUTTON_HEIGHT/2 <= mouse[1] <= QUIT_BUTTON_HEIGHT/2+40:
                pygame.quit()
                sys.exit()

            if START_BUTTON_WIDTH/2-80 <= mouse[0] <= START_BUTTON_WIDTH/2+220 and START_BUTTON_HEIGHT/2-20 <= mouse[1] <= START_BUTTON_HEIGHT/2+80:
                for i in range(18):
                    screen.fill((180-i*10, 180-i*10, 180-i*10))
                    pygame.display.update()
                    sleep(0.01)
                run_game()
    # fills the screen with a color
    screen.fill((180, 230, 180))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if QUIT_BUTTON_WIDTH/2 <= mouse[0] <= QUIT_BUTTON_WIDTH/2+140 and QUIT_BUTTON_HEIGHT/2 <= mouse[1] <= QUIT_BUTTON_HEIGHT/2+40:
        pygame.draw.rect(screen, color_light, [
                         QUIT_BUTTON_WIDTH/2, QUIT_BUTTON_HEIGHT/2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [
                         QUIT_BUTTON_WIDTH/2, QUIT_BUTTON_HEIGHT/2, 140, 40])

    # if mouse is hovered on a button it
    # changes to lighter shade
    if START_BUTTON_WIDTH/2-80 <= mouse[0] <= START_BUTTON_WIDTH/2+220 and START_BUTTON_HEIGHT/2-20 <= mouse[1] <= START_BUTTON_HEIGHT/2+80:
        pygame.draw.rect(screen, color_light, [
                         START_BUTTON_WIDTH/2-80, START_BUTTON_HEIGHT/2-25, 300, 100])

    else:
        pygame.draw.rect(screen, color_dark, [
                         START_BUTTON_WIDTH/2-80, START_BUTTON_HEIGHT/2-25, 300, 100])

    # superimposing the text onto our button
    screen.blit(text_quit, (QUIT_BUTTON_WIDTH/2+25, QUIT_BUTTON_HEIGHT/2+5))
    screen.blit(text_start, (START_BUTTON_WIDTH /
                2-40, START_BUTTON_HEIGHT/2-10))

    # updates the frames of the game
    pygame.display.update()
