from __future__ import annotations
from homework_27.services.nationalities.nationalities import NationalitiesServices
from homework_27.services.gender.gender import GenderServices

class Nationalities:
    def __init__(
        self,
        nationalities: str,
        length: int,
    ) -> None:
        self.nationalities = nationalities
        self.length = length

    @classmethod
    def from_response_json(cls, data: dict) -> NationalitiesServices:
        data = data["data"][0]

        return cls(**data)

    def __eq__(self, other: NationalitiesServices) -> bool:
        pass

class Gender:
    def __init__(
        self,
        gender: str,
        length: int,
    ) -> None:
        self.nationalities = gender
        self.length = length

    @classmethod
    def from_response_json(cls, data: dict) -> GenderServices:
        data = data["data"][0]

        return cls(**data)

    def __eq__(self, other: GenderServices) -> bool:
        pass