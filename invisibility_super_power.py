from abc import ABC, ABCMeta, abstractmethod


class InvisibilitySuperPower(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def turn_invisible(self):
        raise NotImplementedError

    @abstractmethod
    def turn_visible(self):
        raise NotImplementedError