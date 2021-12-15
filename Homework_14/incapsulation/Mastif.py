class Mastif:
    def __init__(self, name):
        self.__animal_name = name  # устанавливаем имя
        self.__age = 1      # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 15):
            self.__age = age
        else:
            print("not appropriate age")

    @property
    def name(self):
        return self.__animal_name

if __name__ == "__main__":
    mastif = Mastif()
    mastif.age(20)
    mastif.name('Lord')
