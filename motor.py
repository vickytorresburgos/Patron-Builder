class Motor:
    def __init__ (self):
        self.__numero__ = None
        self.__potencia__ = None
        print("Motor creado")

    def getNumero(self):
        return self.__numero__ 
    
    def setNumero(self, nuevo_numero):
        self.__numero__ = nuevo_numero

    def getPotencia(self):
        return self.__potencia__

    def setPotencia(self, nueva_potencia):
        self.__potencia__ = nueva_potencia
