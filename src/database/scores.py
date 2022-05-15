import time
from database.user_repository import UserRepository
from database.database_connection import get_database_connection


class Scores:
    """Luokka Scores vastaa pelin pisteytyksestä
    """

    def __init__(self):
        """alustetaan pisteet alkuun, sekä luodaan yhteys tietokantaan
        """
        self.score = 8000
        self.user_repository = UserRepository(get_database_connection())
        self.final_score = 0

    def save_score(self, coin_count, death_count, start_time, name):
        """tallentaa tietokantaan pelaajan pisteet

        Args:
            coin_count (int): kolikoiden määrä
            death_count (int): kuolemien määrä
            name (string): pelaajan nimi, jonka kohdalle pisteet tallennetaan
        """
        save_score = (self.score-int(
            time.time() - start_time)*100+coin_count*100-1000*death_count)
        self.user_repository.update_score(name, save_score)

    def return_highscores(self):
        """palauttaa listan pelaajien ennätyspisteistä suuruusjärjestyksessä,
        tämä näytetään pelin lopussa

        Returns:
            _type_: _description_
        """
        all_scores = self.user_repository.find_all()
        all_scores = sorted(all_scores, key=lambda x: int(x[1]))
        all_scores.reverse()
        all_scores = all_scores[0:11]
        return all_scores
