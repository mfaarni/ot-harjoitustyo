from time import time
from services.settings import SCREEN_WIDTH
from services.controls import Controls
from database.scores import Scores


class Level:
    """Pelin tason toimintaa hallitseva luokka
        """

    def __init__(self, player_name):
        """Luokan kostruktori, joka alustaa tason

        Args:
            player_name (string): pelaajan nimi, joka tallennetaan tietokantaan
        """
        self.world_shift = 0
        self.level_won = False
        self.coin_and_death_counter = [0, -1]
        self.health = 3
        self.start_time = time()
        self.controls = Controls()
        self.setup_level()
        self.name = player_name
        self.inincibility_timer = 0

    def scroll_x(self, player_x, direction_x):
        """vastaa pelihahmon liikkumisesta, jolloin ruudun sivuilla ollessa hahmo ei liiku,
            vaan maailma sen ympärillä, luoden vaikutelman "kamerasta", joka seuraa pelaajaa

        Args:
            player_x (int): pelaajan x-kordinaatin arvo
            direction_x (int): osoittaa pelaajan kulkemissuunnan
        """

        if player_x < (SCREEN_WIDTH/2-400) and direction_x < 0:
            self.world_shift = 6
            self.controls.speed = 0

        elif player_x > (SCREEN_WIDTH/2+200) and direction_x > 0:
            self.world_shift = -6
            self.controls.speed = 0
        else:
            self.world_shift = 0
            self.controls.speed = 6
        if self.inincibility_timer > 0:
            self.inincibility_timer -= 1

    def setup_level(self):
        """alustaa tason pelin alussa sekä kuoltaessa, asettamalla arvot oletuksiksi
        """
        self.coin_and_death_counter[1] += 1
        self.coin_and_death_counter[0] = 1
        self.get_hit(3)
        self.start_time = time()

    def get_hit(self, amount):
        if self.health>amount:
            self.health += amount
        else:
            self.health=3
        self.inincibility_timer = 50

    def fall_to_death(self, player_y):
        """vastaa tilanteesta, jossa pelaaja tippuu tason ulkopuolelle

        Args:
            player_y (int): pelaajan y-koordinaatti
        """
        if player_y > 1000:
            self.setup_level()

    def win(self):
        """pelaajan voittaessa tallennetaan tulos ja rekisteröidään voitto
        """
        self.level_won = True
        Scores().save_score(
            self.coin_and_death_counter[0], self.coin_and_death_counter[1],\
                self.start_time, self.name)
