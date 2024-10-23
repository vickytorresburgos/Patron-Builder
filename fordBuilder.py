from typing import override
from auto import Auto
from autoBuilder import AutoBuilder
from motor import Motor

class FordBuilder(AutoBuilder):
    def __init__(self):
        self.__auto__ = Auto()

    @override
    def buildMarca(self):
        self.getAuto().setMarca("Ford")
        
    @override
    def buildModelo(self):
        self.getAuto().setModelo("Focus")

    @override
    def buildMotor(self):
        motor = Motor()
        motor.setNumero(212122)
        motor.setPotencia("20 HP")
        self.getAuto().setMotor(motor)

    @override
    def buildPuertas(self):
        self.getAuto().setCantPuertas(4)
