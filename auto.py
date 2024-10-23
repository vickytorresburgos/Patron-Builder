from motor import Motor

class Auto:
    def __init__ (self):
        self.__cantPuertas__ = None
        self.__modelo__ = None
        self.__marca__ = None
        self.__motor__ = None
        
    def getCantidadPuertas(self):
        return self.__cantPuertas__
    
    def setCantPuertas(self, nueva_cant_puertas):
        self.__cantPuertas__ = nueva_cant_puertas

    def getModelo(self):
        return self.__modelo__
    
    def setModelo(self, nuevo_modelo):
        self.__modelo__ = nuevo_modelo

    def getMotor(self):
        return self.__motor__
    
    def setMotor(self, nuevo_motor):
        if isinstance(nuevo_motor, Motor):
            self.__motor__ = nuevo_motor
        else:
            raise ValueError

    def getMarca(self):
        return self.__marca__

    def setMarca(self, nueva_marca):
        self.__marca__ = nueva_marca
