from Homework_14.colors.colors import Color


class Dog:
    def __init__(self, animal_age: int, color: Color):
     self.__animal_age = animal_age
     self.__paws = 4
     self.__color = color


    def speak (self):
     print ("woff!")
