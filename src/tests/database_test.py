import unittest
from database_connection import get_database_connection
from initialize_database import drop_tables, create_tables, initialize_database
from user_repository import UserRepository


class Test_levels(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        self.userRepo = UserRepository(self.connection)
        initialize_database()

    def test_empty_connection(self):
        all_names = self.userRepo.find_all()
        self.assertEqual(all_names, [])

    def test_save_name(self):
        self.userRepo.create("testi", 123)
        all_names = self.userRepo.find_all()
        self.assertEqual(all_names, [("testi", 123)])

    def test_save_and_purge_name(self):
        self.userRepo.create("testi", 123)
        self.userRepo.delete_all()
        all_names = self.userRepo.find_all()
        self.assertEqual(all_names, [])
