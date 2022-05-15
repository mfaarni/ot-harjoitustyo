from database.database_connection import get_database_connection


def drop_tables(connection):
    """Deletes existing datatables

    Args:
        connection (sqlite3 connect): connection to sqlite3 database
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()


def create_tables(connection):
    """_summary_

    Args:
        connection (sqlite3 connect): connection to sqlite3 database
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            score int
        );
    ''')

    connection.commit()


def initialize_database():
    """Refreshes the databases for a empty start
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
