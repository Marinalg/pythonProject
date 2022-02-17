from homework_20_iterator_decorator_ect.iterator.car_class import Car
from homework_20_iterator_decorator_ect.iterator.modification import ModificationCar

if __name__ == "__main__":
    class_car = Car("S", "Retro", "Premium")
    engine = Car("Electro", "Gas")
    color = Car("Green", "Grey")
    modification = ModificationCar([class_car, engine, color])

    for car in modification:
        print(car)
