from typing import List
from homework_20_iterator_decorator_ect.iterator.car_class import Car

class ModificationCar:
    def __init__(self, cars: List[Car] = None) ->None:
        self.__cars = [] if not cars else cars


    def add_modifications(self, cars: Car):
        self.__monifications.append(cars)

    def add_modification(self, car: List[Car]):
        self.__modification.extend(car)

    def __iter__(self):
        return self






