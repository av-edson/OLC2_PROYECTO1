from clases.abstract.instruccion import Instruccion
from clases.abstract.type import *

class Parametro(Instruccion):
    def __init__(self,ide,tipo, line, column):
        Instruccion.__init__(self,line, column)
        self.identificador = ide
        self.tipoDato = tipo

    def ejecutar(self, enviroment):
        return self
