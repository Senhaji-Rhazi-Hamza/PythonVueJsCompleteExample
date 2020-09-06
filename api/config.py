import os

NAME_DB = os.getenv('NAME_DB', 'database.db')

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

DB_FOLDER = os.path.join(BASE_PATH, "db", "data")

URI =f'sqlite:///{os.path.join(DB_FOLDER, NAME_DB)}?check_same_thread=false'
