
class Hydrogen:
    def __init__(self, name: str, number_of_group: int, atomyweight: float):
        self.__name = "CH4"
        self.__number_of_group = 1
        self.__atomyweight = 1.00784

    def __str__(self):
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"

        return result

    @property
    def name(self):
        return self.__name