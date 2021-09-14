import time
from clases.error import Error
from clases.enviroment.simbolo import Simbolo
from clases.abstract.expresion import Expresion
#from clases.enviroment.enviroment import Enviroment
from clases.abstract.type import *
import copy

class AccesoStruct(Expresion):
    def __init__(self,idVar,atributo, line, column,esLista=None):
        Expresion.__init__(self,line, column)
        self.identificador = idVar
        self.atributo = atributo
        self.esLista=esLista
    
    def ejecutar(self, enviroment):
        try:
            simbolo = enviroment.findVariable(self.identificador)
            if self.esLista !=None:
                copia = list(reversed(self.atributo))
            else:
                copia = []
                copia.append(self.atributo)
            return self.getContenido(enviroment,simbolo,copia)
        except:
            print("error inesperado en acceso a struct")
        #if simbolo!=None:
        #    if simbolo.tipo == Type.STRUCT:
        #        atributos = simbolo.atributos
        #        for sim in atributos:
        #            if sim.simbolId == self.atributo:
        #                if sim.tipo == Type.STRUCT:
        #                    sim = sim.valor
        #                    st = Simbolo(sim.atributos,sim.simbolId,sim.tipo,None,None,sim.tipoStruct,sim.tipoStruct.mutable)
        #                    st.atributos = sim.atributos
        #                    return Return(st,Type.STRUCT)
        #                return Return(sim.valor,sim.tipo)
        #    print("no es de tipo estruct la variable a la que quiere acceder")
        #    gl.listaErrores.append(Error("no es de tipo estruct la variable a la que quiere acceder",self.line,self.column,time.strftime("%c")))
        #    return Return()
        #print("estruct no declarada")
        #gl.listaErrores.append(Error("estruct no declarada",self.line,self.column,time.strftime("%c")))
        #return Return()

    def getContenido(self,enviroment,ide,atributo):
        gl = enviroment.getGlobal()
        simbolo= ide
        if simbolo!=None:
            if simbolo.tipo == Type.STRUCT:
                if simbolo.valor == None:
                    atributos = simbolo.atributos
                else: atributos = simbolo.valor
                atr = atributo.pop()
                for sim in atributos:
                    if sim.simbolId == atr:
                        if sim.tipo == Type.STRUCT and len(atributo)>0:
                            return self.getContenido(enviroment,sim.valor,atributo)
                        return Return(sim.valor,sim.tipo)
                print("no se encontro atributo")
                return Return()
            print("no es de tipo estruct la variable a la que quiere acceder")
            gl.listaErrores.append(Error("no es de tipo estruct la variable a la que quiere acceder",self.line,self.column,time.strftime("%c")))
            return Return()
        print("estruct no declarada")
        gl.listaErrores.append(Error("estruct no declarada",self.line,self.column,time.strftime("%c")))
        return Return()