from time import sleep
import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from game import run_game
from database_connection import get_database_connection
from user_repository import UserRepository

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
COLOR_LIGHT = (170, 170, 170)
COLOR_DARK = (100, 100, 100)

START_BUTTON_WIDTH = SCREEN_WIDTH-100
START_BUTTON_HEIGHT = SCREEN_HEIGHT-200


class Login():

    def __init__(self):
        self.name = ""
        self.start_font = pygame.font.SysFont('Corbel', 100)
        self.error_font = pygame.font.SysFont('Corbel', 60)
        self.text_name_input = self.start_font.render('', True, WHITE)
        self.name_acceptable = False
        self.text_error = self.error_font.render(
            'TRY A LONGER NAME', True, (230, 40, 80))
        self.error_timer = 0
        self.user_repository = UserRepository(get_database_connection())

    def run_login(self):
        while True:
            if self.error_timer > 0:
                self.error_timer -= 1
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                self.handle_event(event, mouse)

            SCREEN.fill((180, 230, 180))

            if START_BUTTON_WIDTH/2-80 <= mouse[0] <= START_BUTTON_WIDTH/2+220\
                    and START_BUTTON_HEIGHT/2-20 <= mouse[1] <= START_BUTTON_HEIGHT/2+80:
                pygame.draw.rect(SCREEN, COLOR_LIGHT,
                                 [START_BUTTON_WIDTH/2-80, START_BUTTON_HEIGHT/2-25, 300, 100])

            else:
                pygame.draw.rect(SCREEN, COLOR_DARK, [
                    START_BUTTON_WIDTH/2-80, START_BUTTON_HEIGHT/2-25, 300, 100])

            if self.name_acceptable:
                pygame.draw.circle(SCREEN, (0, 200, 0), (445, 110), 20)
            SCREEN.blit(self.start_font.render('START', True, WHITE),
                        (START_BUTTON_WIDTH/2-40, START_BUTTON_HEIGHT/2-10))
            SCREEN.blit(self.start_font.render('NAME:', True, WHITE),
                        (START_BUTTON_WIDTH /2-80, START_BUTTON_HEIGHT/2-140))
            SCREEN.blit(self.text_name_input, (START_BUTTON_WIDTH /
                                               2+140, START_BUTTON_HEIGHT/2-140))
            if self.error_timer > 0:
                SCREEN.blit(self.text_error, (START_BUTTON_WIDTH /
                                              2-80, START_BUTTON_HEIGHT/2-200))
            if self.error_timer > 0:
                SCREEN.blit(self.text_error, (START_BUTTON_WIDTH /
                                              2-80, START_BUTTON_HEIGHT/2-200))

    def handle_event(self, event, mouse):
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == "backspace" and len(self.name) > 0:
                self.name = self.name[:len(self.name)-1]
                if len(self.name) < 3:
                    self.name_acceptable = False
                    self.text_error = self.error_font.render(
                        'TRY A LONGER NAME', True, (230, 40, 80))

            elif key in "abcdefghijklmnopqrstuvwxyz1234567890"\
                    and len(self.name) < 6:
                self.name = self.name+key
                if len(self.name) > 2:
                    self.name_acceptable = True
            elif key in "abcdefghijklmnopqrstuvwxyz1234567890"\
                    and len(self.name) >= 6:

                self.text_error = self.error_font.render(
                    'NAME MUST BE 6 OR LESS CHARS', True, (230, 40, 80))
                self.error_timer = 750
            else:
                self.text_error = self.error_font.render(
                    'KEY NOT ACCEPTED', True, (230, 40, 80))
                self.error_timer = 1250

        self.text_name_input = self.start_font.render(
            self.name.upper(), True, WHITE)
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_BUTTON_WIDTH/2-80 <= mouse[0] <= START_BUTTON_WIDTH/2+220:
                if START_BUTTON_HEIGHT/2-20 <= mouse[1] <= START_BUTTON_HEIGHT/2+80:
                    self.acceptable_name()
        pygame.display.update()


    def acceptable_name(self):
        if self.name_acceptable:
            if self.user_repository.find_by_username(self.name) is None:
                self.user_repository.create(self.name, 0)
            for i in range(18):
                SCREEN.fill((180-i*10, 180-i*10, 180-i*10))
                pygame.display.update()
                sleep(0.01)
                run_game(self.name)
        else:
            self.text_error = self.error_font.render(
                'NAME NOT ACCEPTED', True, (230, 40, 80))
            self.error_timer = 2500
