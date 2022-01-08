from abc import ABC, abstractmethod


class INoisable(ABC):
    @abstracmethod
    def noise(self):
        ...