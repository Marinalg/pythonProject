from abc import ABC, abstractmethod

class Ivacuumable(ABC):
    @abstractmethod
    def vacuum(self):
        ...