import time
from user_repository import UserRepository
from database_connection import get_database_connection


class Scores:
    """Luokka Scores vastaa pelin pisteytyksestä
    """
    def __init__(self):
        """alustetaan pisteet alkuun, sekä luodaan yhteys tietokantaan
        """
        self.first_write = True
        self.score = 8000
        self.start_time = time.time()
        self.user_repository = UserRepository(get_database_connection())
        self.final_score=0


    def save_score(self, coin_count, death_count, name):
        """tallentaa tietokantaan pelaajan pisteet

        Args:
            coin_count (int): kolikoiden määrä
            death_count (int): kuolemien määrä
            name (string): pelaajan nimi, jonka kohdalle pisteet tallennetaan
        """
        save_score=(self.score-int(
                    time.time() - self.start_time)*100+coin_count*100-1000*death_count)
        self.user_repository.update_score(name,save_score)

        with open("src/highscores.txt", "a", encoding="utf8") as text_file:
            if self.first_write:
                text_file.write("\n Player score:" + str(self.score-int(
                    time.time() - self.start_time)*100+coin_count*100-1000*death_count))
                text_file.write("\n Player score: 0")
                self.first_write = False

    def return_highscores(self):
        """palauttaa listan pelaajien ennätyspisteistä suuruusjärjestyksessä,
        tämä näytetään pelin lopussa

        Returns:
            _type_: _description_
        """
        all_scores=self.user_repository.find_all()
        all_scores=sorted(all_scores, key=lambda x: int(x[1]))
        all_scores.reverse()
        all_scores=all_scores[0:11]
        return all_scores

    def update_start_time(self):
        """päivittää pisteisiin vaikuttavan aloitusajan tarvittaessa
        """
        self.start_time = time.time()
