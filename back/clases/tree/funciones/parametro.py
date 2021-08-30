from clases.abstract.instruccion import Instruccion
from clases.abstract.type import *

class Parametro(Instruccion):
    def __init__(self,ide,tipo, line, column):
        Instruccion.__init__(self,line, column)
        self.identificador = ide
        self.tipoDato = tipo

    def ejecutar(self, enviroment):
        return self

class ReturnFunc(Instruccion):
    def __init__(self,expresion, line, column):
        Instruccion.__init__(self,line, column)
        self.valor = expresion
    
    def ejecutar(self, enviroment):
        try:
            exp:Return = self.valor.ejecutar(enviroment)
            return Return(exp.value,Type.RETURNST)
        except:
            print("Error en el return"+str(self.line))
            return Return()