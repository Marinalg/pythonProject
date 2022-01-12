from abc import ABC, abstractmethod

class Ivacuumable(ABC):
    @abstracmethod
    def vacuum(self):
        ...