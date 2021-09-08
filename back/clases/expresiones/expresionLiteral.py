#from clases.enviroment.simbolo import Simbolo
from clases.abstract.expresion import Expresion
#from clases.enviroment.enviroment import Enviroment
from clases.abstract.type import *

class ExpresionLiteral(Expresion):
    def __init__(self,tipoDato,valorDato, line, column):
        Expresion.__init__(self,line,column)
        self.tipo=tipoDato # regresa el tipo de dato de la expresion
        self.valor=valorDato
    
    def ejecutar(self, enviroment):
        if self.tipo==Type.STRING:
            self.valor = str(self.valor).replace("\\n","\n")
        return Return(self.valor,self.tipo)


class Identificador(Expresion):
    def __init__(self,ide, line, column):
        Expresion.__init__(self,line,column)
        self.identificador=ide 
    
    def ejecutar(self, enviroment):
        simbolo = enviroment.findVariable(self.identificador)
        if simbolo != None:
            if simbolo.tipo==Type.STRUCT:
                return Return(simbolo,Type.STRUCT)
            else:
                return Return(simbolo.valor,simbolo.tipo)
        return Return()

