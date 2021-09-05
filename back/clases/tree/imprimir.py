import time
from clases.error import Error
from clases.enviroment.enviroment import Enviroment
from clases.abstract.instruccion import Instruccion
from clases.abstract.type import Type
from enum import Enum

class TipoImpresion(Enum):
    PRINT=0
    PRINTLN=1

class Imprimir(Instruccion):
    def __init__(self,listaExpresiones,tipo:TipoImpresion, line, column):
        Instruccion.__init__(self,line, column)
        self.listaExpre = listaExpresiones
        self.tipo=tipo
    def ejecutar(self, enviroment):
        lista = []
        # recolec
        for expre in self.listaExpre:
            res=expre.ejecutar(enviroment)
            if res.tipo==Type.UNDEFINED:
                gl:Enviroment = enviroment.getGlobal()
                gl.listaErrores.append(Error("Una de las expresiones el print tiene error",self.line,self.column,time.strftime("%c")))
                print('una de las expresiones el print tiene error')
                return
            lista.append(res)
        if self.tipo==TipoImpresion.PRINT:
            self.imprimir_simple(lista,enviroment)
        else:
            self.imprimir_ml(lista,enviroment)
    
    def imprimir_simple(self,lista,enviroment):
        res=""
        for ex in lista:
            res+=str(ex.value)
        env = enviroment.getGlobal()
        env.consola += res 
        #print(consola, end="")

    def imprimir_ml(self,lista,enviroment):
        res = ""
        for ex in lista:
            res+=str(ex.value)
        env = enviroment.getGlobal()
        env.consola += res + "\n"
        #print(aux)