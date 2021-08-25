from abc import abstractmethod
from abstract.instruccion import Instruccion
from enviroment.enviroment import Enviroment

class BloqueInstrucciones(Instruccion):
    def __init__(self,instrucciones,line,column):
        self.listaInstrucciones = instrucciones
        self.line=line
        self.column=column
    def ejecutar(self, enviroment):
        entorno = Enviroment(enviroment)
        for instruccion in self.listaInstrucciones:
            regreso = instruccion.ejecutar(entorno)