from abc import ABC, abstractmethod
from auto import Auto

class AutoBuilder(ABC):
    def getAuto(self):
        return self.__auto__
    
    def crearAuto(self):
        self.__auto__ = Auto()

    @abstractmethod
    def buildMotor():
        pass

    @abstractmethod
    def buildModelo():
        pass

    @abstractmethod
    def buildMarca():
        pass

    @abstractmethod
    def buildPuertas():
        pass
