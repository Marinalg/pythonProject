from homework_19_magic_method import Hydrogen
from homework_19_magic_method import Methane


class Carbone:
    def __init__(self, name: str, number_of_group: int, atomyweight: float):
        self.__name = "C"
        self.__number_of_group = 14
        self.__atomyweight = 12.0107

    def __str__(self):
        result = ""
        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"
        return result

def __add__(self, other: Hydrogen):
    return Methane(self._atomyweight, other.name)
def __radd__(self, other: Hydrogen):
    return Methane(self.__atomyweight, other.name)

    @property
    def atomyweight(self):
        return self.__atomyweight

