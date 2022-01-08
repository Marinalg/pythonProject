from abc import ABC, abstractmethod

class IVacuumable(ABC):
    @abstracmethod
    def vacuum(self):
        ...