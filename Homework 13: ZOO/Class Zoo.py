class Zoo:
    def __init__(self, animal: str, animal_type: str, habitat: str, count: int):
        self.animal = animal
        self.animal_type = animal_type
        self.habitat = habitat
        self.count = count

    def show(self):
        return self.animal,self.animal_type,self.habitat,self.count

    def total_of_count(self, count):
        result = 0
        for animal in self.count.values():
            if animal == count:
                result += 1
        return result
        print(total_of_count())

    if __name__ == "__main__":
      giraffe = Zoo ("giraffe","herbivore","outside", 1)
      tiger = Zoo ("tiger","meaty","cage",2)
      bear = Zoo ("bear","omnivore","cage", 3)
    print(bear.show())
    print(tiger.show())
    print(giraffe.show())

