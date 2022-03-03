class Dog:
    def __init__(self, animal_age: int, color: str):
     self.animal_age = animal_age
     self._paws = 4
     self.color = color

     def speak(self):
         print("woff!")

if __name__ == "__main__":
    dog = Dog ("black",4)
    print(dog._paws)