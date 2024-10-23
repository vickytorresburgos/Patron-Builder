from autoBuilder import AutoBuilder
from fiatBuilder import FiatBuilder
from fordBuilder import FordBuilder

class AutoDirector:
    def __init__ (self):
        self.__autoBuilder__ = None
        print("Auto builder creado")

    def construirAuto(self):
        self.__autoBuilder__.crearAuto()
        self.__autoBuilder__.buildMarca()
        self.__autoBuilder__.buildModelo()
        self.__autoBuilder__.buildMotor()
        self.__autoBuilder__.buildPuertas()
        print("Auto creado")

    def getAuto(self):
        return self.__autoBuilder__.getAuto()

    def setAutoBuilder(self, new_auto_builder):
        if isinstance(new_auto_builder, AutoBuilder):
            self.__autoBuilder__ = new_auto_builder
        else:
            raise ValueError
        
if __name__ == "__main__":
    director = AutoDirector()
    director.setAutoBuilder(FordBuilder())
    director.construirAuto()
    ford = director.getAuto()
    print("la marca del auto es: ",ford.getMarca())
    print("el modelo del auto es: ",ford.getModelo())
    
    director.setAutoBuilder(FiatBuilder())
    director.construirAuto()
    director.construirAuto()
    fiat = director.getAuto()
    print("la marca del auto es: ",fiat.getMarca())
    print("el modelo del auto es: ",fiat.getModelo())


