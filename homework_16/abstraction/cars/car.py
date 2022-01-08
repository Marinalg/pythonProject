from abc import ABC
class Car(ABC):
    def mileage(self):
        raise Exception(f"Method {self.mileage.__name__} not implemented in {self.__class__.name__}")
    def fly(self):
        raise Exception(f"Method {self.fly.__name__} not implemented in {self.__class__.name__}")