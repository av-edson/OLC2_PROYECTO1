from clases.abstract.instruccion import Instruccion
from clases.abstract.type import *

class ReturnFunc(Instruccion):
    def __init__(self,expresion, line, column):
        Instruccion.__init__(self,line, column)
        self.valor = expresion
    
    def ejecutar(self, enviroment):
        try:
            if self.valor != None:
                exp:Return = self.valor.ejecutar(enviroment)
                if exp.tipo != Type.UNDEFINED:
                    return exp
                else:
                    return Return()
            else:
                return Return(0,Type.RETURNST)
        except:
            print("Error en el return"+str(self.line))
            return Return()