from clases.expresiones.expresionLiteral import ExpresionLiteral
from clases.abstract.type import Return, Type
from clases.error import Error
import time
from clases.abstract.instruccion import Instruccion

class DeclaracionArreglo(Instruccion):
    def __init__(self,ide,lista, line, column):
        Instruccion.__init__(self,line, column)
        self.identificador = str(ide)
        self.listaExpresiones = lista
        self.size = 0
        self.lista = []
    
    def ejecutar(self, enviroment):
        gl = enviroment.getGlobal()
        if self.listaExpresiones.tipo!=Type.ARRAY:
            print("expresion no es lista")
            return
        self.lista.clear()
        try:
            for expr in self.listaExpresiones.value:
                ret = expr.ejecutar(enviroment)
                if ret == None:
                    print("expresion no admitida dentro del arreglo, None")
                    gl.listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
                    return
                if ret.tipo == Type.UNDEFINED:
                    print("Una de las expresiones dentro del arreglo tiene error en su declaracion")
                    gl.listaErrores.append(Error("Una de las expresiones dentro del arreglo tiene error en su declaracion",self.line,self.column,time.strftime("%c")))
                    return
                elif ret.tipo == Type.RETURNST or ret.tipo == Type.BREACKST or ret.tipo == Type.CONTINUEST:
                    print("expresion no admitida dentro del arreglo")
                    gl.listaErrores.append(Error("expresion no admitida dentro del arreglo",self.line,self.column,time.strftime("%c")))
                    return
                aux = ExpresionLiteral(ret.tipo,ret.value,self.line,self.column)
                self.lista.append(aux)
            if len(self.lista) != len(self.listaExpresiones.value):
                print("Error 2 expresion no admitida dentro del arreglo")
                gl.listaErrores.append(Error("Error 2 expresion no admitida dentro del arreglo",self.line,self.column,time.strftime("%c")))
                return
            enviroment.add_variable(self.identificador,self.lista,Type.ARRAY,3,self.line,self.column)
        except:
            print("Error al declarar el arreglo")
            gl.listaErrores.append(Error("Una de las expresiones el print tiene error",self.line,self.column,time.strftime("%c")))

    def getContentString(self):
        contenido="["
        for i in range(len(self.lista)):
            aux = self.lista[i]
            if i != 0:
                contenido+=","
            if not (aux.tipo == Type.ARRAY or aux.tipo == Type.STRUCT):
                contenido+=str(aux.value)
        contenido+="]"
        return contenido



