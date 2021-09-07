from clases.enviroment.simbolo import Simbolo
from clases.tree.structs.CrearStruct import CrearStruct
from clases.abstract.type import Return, Type
import time
from clases.error import Error
from clases.abstract.instruccion import Instruccion

class DeclararStruct(Instruccion):
    def __init__(self,tipoStruct,listaExpresiones, line, column):
        '''Atributos es una lista con los simbolos del struct'''
        Instruccion.__init__(self,line, column)
        self._lista = listaExpresiones
        self.tipoStruct = tipoStruct

    def ejecutar(self, enviroment):
        struct = enviroment.getStruct(self.tipoStruct)
        gl = enviroment.getGlobal()
        if struct == None:
            print("No se encontro struct definida")
            gl.listaErrores.append(Error("No se encontro una struct definida",self.line,self.column,time.strftime("%c")))
            return Return()
        listaExpresiones = self.evaluarExpresiones(self._lista,enviroment)
        # evaluando las expresiones con el tipo expresion del struct
        if len(listaExpresiones) != len(struct.atributos):
            print("en numero de parametros no coicide con la struct definida")
            gl.listaErrores.append(Error("Numero de parametros no coicide con la struct definida",self.line,self.column,time.strftime("%c")))
            return
        aux=[]
        for i in range(len(listaExpresiones)):
            if listaExpresiones[i].tipo != struct.atributos[i].tipo:
                if struct.atributos[i].tipo != None and struct.atributos[i].tipo != Type.NULO:
                    print("uno de los tipos de datos del struct no coincide con el declarado")
                    gl.listaErrores.append(Error("Uno de los tipos de datos del struct no coicide con el declarado",self.line,self.column,time.strftime("%c")))
                    return Return()
                elif listaExpresiones[i].tipo == Type.UNDEFINED:
                    print("Error en uno de los parametros para declarar la struct")
                    gl.listaErrores.append(Error("Error en uno de los parametro spara declarar la struct",self.line,self.column,time.strftime("%c")))
                    return Return()
            simboloAux = Simbolo(listaExpresiones[i].value,struct.atributos[i].simbolId,listaExpresiones[i].tipo)
            aux.append(simboloAux)
        mutable = struct.mutable
        simboloStruct = Simbolo(aux,None,Type.STRUCT,struct,mutable)
        return Return(simboloStruct,Type.STRUCT)

    def evaluarExpresiones(self,lista,enviroment):
        resutado = []
        for expre in lista:
            reg:Return = expre.ejecutar(enviroment)
            resutado.append(reg)
        return resutado