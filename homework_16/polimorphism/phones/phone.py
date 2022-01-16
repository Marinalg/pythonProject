from abc import abstractmethod

class Phone(ABC):

    def __init__(self,color:str,year: int)->None:
        self._color = color
        self._year = year

    @abstractmethod
    def call(self):
        ...