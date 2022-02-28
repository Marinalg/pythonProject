from requests import get


from ...core.config.config_gender import Gender
from ...core.config.config_gender import Config
from ...core.singleton import Singleton



class GenderServices(Singleton):
    def __init__(self, config: Config) -> None:
        self.__config = config


    def get_random_gender(self):
        return GenderServices.from_response_json(
            get(url=f"{self.__config_gender.host}/gender".json())
        )
    def get_gender_by_name(self):
        return GenderServices.from_response_json(
            get(url=f"{self.__config_gender.host}/gender".json())
        )