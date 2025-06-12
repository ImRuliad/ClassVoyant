from sqlalchemy import create_engine
from sqlalchemy.testing.config import db_url


class Database:
    def __init__(self):
        self.db_url = "sqlite:///my_database.db"
        self.engine = create_engine(db_url, echo=True) #create db engine and allow for logging.

        


