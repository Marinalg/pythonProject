class Human:
    """Super human class"""

    def __init__(self, name: str, age: int, gender: str, race: str) -> None:
        self.__name = name
        self.__age = age
        self.__gender = self.__validate_gender(gender)
        self.__race = race

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender

    def __validate_gender(self, gender: str) -> str:
        if gender not in ["male", "female"]:
            raise Exception("Not supported gender...")
        else:
            return gender

    def grow(self) -> None:
        self.__age += 1

    def change_name(self, name: str) -> None:
        if name != self.__name:
            self.__name = name
        else:
            raise Exception("Provided name is same as current...")

    def change_gender(self, gender: str):
        self.__gender = self.__validate_gender(gender)

