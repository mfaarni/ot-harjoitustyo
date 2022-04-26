from time import time
from settings import SCREEN_WIDTH
from controls import Controls
from scores import Scores


class Level:
    def __init__(self):
        # aluksi kamera pysyy paikallaan
        self.world_shift = 0
        # funktio totetuttaa ikään kuin kameran liikkumisen hahmon mukana,
        # todellisuudessa liikkuu tason elementit hahmon ollessa paikallaan.
        self.level_won = False

        # lasketaan kolikot
        self.coin_counter = 0
        self.death_counter = -1


        self.start_time = time()
        self.highscore = Scores()
        self.controls = Controls()
        self.setup_level()

    def scroll_x(self, player_x, direction_x):

        # Liike tapahtuu hahmon sijainnin ja suunnan mukaan
        if player_x < (SCREEN_WIDTH/2-400) and direction_x < 0:
            self.world_shift = 6
            self.controls.speed = 0

        elif player_x > (SCREEN_WIDTH/2+200) and direction_x > 0:
            self.world_shift = -6
            self.controls.speed = 0
        else:
            self.world_shift = 0
            self.controls.speed = 6

    # Tason luonti
    def setup_level(self):
        self.death_counter += 1
        # kolikot ja aika alkuarvoihin
        self.coin_counter = 0
        self.start_time = time()

    def print_stuff(self):
        print("!!!!")

    def fall_to_death(self, player_y):
        if player_y > 1000:
            self.setup_level()

    def win(self):
        self.level_won = True
        self.highscore.save_score(self.coin_counter, self.death_counter)
