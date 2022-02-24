from .singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.driver_name = "postgresql+psycopg2"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "marina"
        self.user = "postgres"
        self.password = "postgres"