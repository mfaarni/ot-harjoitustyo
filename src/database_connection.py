import os
import sqlite3

DIRNAME = os.path.dirname(__file__)
CONNECTION = sqlite3.connect(os.path.join(DIRNAME, "data", "database.db"))
CONNECTION.row_factory = sqlite3.Row


def get_database_connection():
    return CONNECTION
