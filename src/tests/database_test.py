import unittest
from initialize_database import drop_tables, create_tables, initialize_database
from database.user_repository import UserRepository
from database.scores import Scores
from database.database_connection import get_database_connection

class TestDatabase(unittest.TestCase):
    def setUp(self):
        import os
        import sqlite3
        DIRNAME = os.path.dirname(__file__)
        self.connection = sqlite3.connect(os.path.join(DIRNAME, "..", "data", "database_test.db"))
        self.connection.row_factory = sqlite3.Row
        drop_tables(self.connection)
        create_tables(self.connection)
        self.userRepo = UserRepository(self.connection)
        self.userRepoReal=UserRepository(get_database_connection())
        self.test_scores=Scores()

    def test_empty_connection(self):
        all_names = self.userRepo.find_all()
        self.assertEqual(all_names, [])
        
    def test_save_and_purge_name(self):
        self.userRepo.create("testi", 123)
        self.userRepo.delete_all()
        all_names = self.userRepo.find_all()
        self.assertEqual(all_names, [])

    def test_save_name(self):
        self.userRepo.create("testi", 123)
        all_names = self.userRepo.find_all()
        self.assertEqual(all_names, [("testi", 123)])

    def test_find_by_username(self):
        self.userRepo.create("testi", 123)
        ret=self.userRepo.find_by_username("testi")
        self.assertEqual(ret,("testi", 123))
        
    def test_update_score(self):
        self.userRepo.create("testi", 123)
        self.userRepo.update_score("testi",124)
        ret=self.userRepo.find_by_username("testi")
        self.assertEqual(ret,("testi", 124))
        
    def test_update_lower_score(self):
        self.userRepo.create("testi", 123)
        self.userRepo.update_score("testi",122)
        ret=self.userRepo.find_by_username("testi")
        self.assertEqual(ret,("testi", 123))
        
    def test_save_score(self):
        self.userRepoReal.delete_by_username("testi_save")
        self.userRepoReal.create("testi_save",123)
        self.test_scores.save_score(1000,0,1000000000000,"testi_save")
        self.assertEqual("testi_save",self.test_scores.return_highscores()[0][0])
        self.userRepoReal.delete_by_username("testi_save")
        
        
