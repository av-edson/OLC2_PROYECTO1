from clases.abstract.expresion import Expresion
#from clases.enviroment.enviroment import Enviroment
from clases.abstract.type import *

class AccesoStruct(Expresion):
    def __init__(self,idVar,atributo, line, column):
        Expresion.__init__(self,line, column)
        self.identificador = idVar
        self.atributo = atributo
    
    def ejecutar(self, enviroment):
        simbolo = enviroment.findVariable(self.identificador)
        if simbolo!=None:
            if simbolo.tipo == Type.STRUCT:
                atributos = simbolo.valor.atributos
                for sim in atributos:
                    if sim.simbolId == self.atributo:
                        return Return(sim.valor,sim.tipo)

        return Return()
