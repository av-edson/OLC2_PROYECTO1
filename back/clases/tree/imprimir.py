from clases.expresiones.expresionLiteral import ExpresionLiteral
import time
import copy
from clases.error import Error
from clases.enviroment.enviroment import Enviroment
from clases.abstract.instruccion import Instruccion
from clases.abstract.type import Return, Type
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
        gl:Enviroment = enviroment.getGlobal()
        try:
            lista = []
            # recolec
            for expre in self.listaExpre:
                res=expre.ejecutar(enviroment)
                if res.tipo==Type.UNDEFINED:
                    gl.listaErrores.append(Error("Una de las expresiones el print tiene error",self.line,self.column,time.strftime("%c")))
                    print('una de las expresiones el print tiene error')
                    return
                if res.tipo==Type.STRUCT:
                    res = res.value
                    aux=str(expre.identificador)+":"+str(res.tipoStruct.identificador)
                    aux+=self._getStruct(res.atributos)
                    res.value = aux
                if res.tipo==Type.ARRAY:
                    res = copy.copy(res.value)
                    if isinstance(expre,ExpresionLiteral):
                        aux=""
                    else:
                        aux = str(expre.identificador)
                    aux+=self._getArray(res,enviroment)[:-1]
                    lista.append(Return(aux,Type.STRING))
                    continue
                lista.append(res)
            if self.tipo==TipoImpresion.PRINT:
                self.imprimir_simple(lista,enviroment)
            else:
                self.imprimir_ml(lista,enviroment)
        except:
            gl.listaErrores.append(Error("Error inesperado en funcion print",self.line,self.column,time.strftime("%c")))
            print("error inesperado en funcion print")
    
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

    def _getStruct(self,atributos):
        if atributos == None:
            return ""
        contenido = "{"
        for atributo in atributos:
            if atributo.tipo == Type.STRUCT:
                contenido+=self._getStruct(atributo.valor.atributos)
            else:
                contenido+=str(atributo.simbolId)+":"+str(atributo.valor)+","
        contenido+="}"
        return contenido
    
    def _getArray(self,lista,enviroment):
        cont = "["
        for ex in lista:
            ex = ex.ejecutar(enviroment)
            if ex.tipo == Type.ARRAY:
                cont+=self._getArray(ex.value,enviroment)
            else:
                cont+=str(ex.value)+","
        cont+="],"
        return cont
