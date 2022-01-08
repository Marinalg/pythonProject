from homework_16.abstraction.vacuum_cleaner.interfaces.inoisable import INoisable
from homework_16.abstraction.vacuum_cleaner.interfaces.ivacuumable import IVacuumable

class Vacuum_cleaner(INoisable, IVacuumable):
    def __init__(self)> None;
        self.__button_on = False
        self.__button_off = False


    def noise(self):
        pass

    def vacuum(self):
        self.__button_on = True