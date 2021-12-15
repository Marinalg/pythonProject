from Homework_14.inheritance_example.dog import Dog


class Mastif (Dog):
    def __init__(self, color: color, animal_age: int, animal_speed: str):
        super().__init__(color, animal_age)
        self.__animal_speed =speed

if __name__ == "__main__":
    mastif = Mastif("black", "4", "3", "fast")
    mastif.speak()