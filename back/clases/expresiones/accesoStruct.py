from clases.enviroment.simbolo import Simbolo
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
                atributos = simbolo.atributos
                for sim in atributos:
                    if sim.simbolId == self.atributo:
                        if sim.tipo == Type.STRUCT:
                            sim = sim.valor
                            return Return(Simbolo(sim.atributos,sim.simbolId,sim.tipo,sim.tipoStruct,sim.tipoStruct.mutable),Type.STRUCT)
                        return Return(sim.valor,sim.tipo)
            print("no es de tipo estruct la variable a la que quiere acceder")
            return Return()
        print("estruct no declarada")
        return Return()