from homework_30.sqlalchemy import create_engine
from homework_30.sqlalchemy.orm import sessionmaker, Session

from homework_30.sqlalchemy.core.singleton import Singleton

from .config import Config



class BaseRepository(Singelton):
        def__init__(self)-> None
                self.__config = Config()
                self.__engine =create_engine(
                        f"{self.__config.driver_name}://"
                        f"{self.__confing.order}:{self.__config.password}@"
                        f"{self.__config.host}:{self.__config.port}{self.__config.database}"
                )
                self.__session: Session = sessionmaker(self.__engine, autocommit=True)()

