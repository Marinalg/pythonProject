from abc import ABC, abstractmethod


class INoisable(ABC):
    @abstractmethod
    def noise(self):
        ...