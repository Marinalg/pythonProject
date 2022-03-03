from requests import get

from ...core.config.config_nationalize import Nationalities
from ...core.config.config_nationalize import Config
from ...core.singleton import Singleton



class NationalitiesServices(Singleton):
    def __init__(self, config: Config) -> None:
        self.__config = config


    def get_random_nationalities(self) -> Nationalities:
         return NationalitiesServices.from_response_json(
            get(url=f"{self.__config_nationalities.host}/nationalities".json())
         )

    def get_predict_nationalities_of_country(self) -> Nationalities:
        return NationalitiesServices.from_response_json(
            get(url=f"{self.__config_nationalities.host}/nationalities".json())
        )



