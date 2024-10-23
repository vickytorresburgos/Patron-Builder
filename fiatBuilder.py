from typing import override
from autoBuilder import AutoBuilder
from motor import Motor
from auto import Auto

class FiatBuilder(AutoBuilder):
    def __init__(self):
        self.__auto__ = Auto()

    @override
    def buildMarca(self):
        self.getAuto().setMarca("Fiat")
        
    @override
    def buildModelo(self):
        self.getAuto().setModelo("Palio")

    @override
    def buildMotor(self):
        motor = Motor()
        motor.setNumero(232323)
        motor.setPotencia("23 HP")
        self.getAuto().setMotor(motor)

    @override
    def buildPuertas(self):
        self.getAuto().setCantPuertas(2)
