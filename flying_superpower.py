from abc import ABC, abstractmethod


class FlyingSuperpower(ABC):
    @abstractmethod
    def fly(self):
        pass
