

class Methane:
    def __init__(self, name: str, number_of_group: int, atomyweight: float):
        self.__name = name
        self.__atomyweight = atomyweight

    def __str__(self):
        result = ""

        for key, value in self.__dict__.items():
            result += f"{key} => {value}\n"
        return result



