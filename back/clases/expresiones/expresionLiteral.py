from clases.enviroment.simbolo import Simbolo
from clases.abstract.expresion import Expresion
from clases.enviroment.enviroment import Enviroment
from clases.abstract.type import *

class ExpresionLiteral(Expresion):
    def __init__(self,tipoDato,valorDato, line, column):
        Expresion.__init__(self,line,column)
        self.tipo=tipoDato # segresa el tipo de dato de la expresion
        self.valor=valorDato
    
    def ejecutar(self, enviroment):
        # falta verificar si es variable y recuperarla
        return Return(self.valor,self.tipo)