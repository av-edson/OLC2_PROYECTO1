from clases.enviroment.simbolo import Simbolo
from clases.expresiones.expresionLiteral import ExpresionLiteral
from os import times
from clases.error import Error
from clases.abstract.instruccion import Instruccion
from clases.abstract.type import Return, Type

class ModificarArreglo(Instruccion):
    def __init__(self,var,listaAcceso,expre, line, column):
        Instruccion.__init__(self,line, column)
        self.accesoArreglo = listaAcceso
        self.identificador = var
        self.valor = expre

    def ejecutar(self, enviroment):
        try:
            nuevoDato:Return = self.valor.ejecutar(enviroment)
            if nuevoDato.tipo == Type.UNDEFINED or nuevoDato.tipo == Type.BREACKST or nuevoDato.tipo==Type.BREACKST or nuevoDato.tipo==Type.CONTINUEST:
                print("Tipo de dato no admitido para valor del arreglo")
                return
            lista:Simbolo = enviroment.findVariable(self.identificador)
            if lista.tipo != Type.ARRAY:
                print("variable no pertenece a un arreglo")
                return
            listaAcceso = list(reversed(self.accesoArreglo))
            anterior = self.getValor(listaAcceso,lista,enviroment,nuevoDato)
        except:
            print("error inesperado al modificar arreglo")
            return
        

    def getValor(self,listaAcceso:list,listaValores:list,env,nuevo):
        index = listaAcceso.pop()
        index = index.ejecutar(env)
        if index.tipo!=Type.INT:
            print("Solo se admiten enteros para acceder a un arreglo")
            return 
        index=index.value
        if listaValores.tipo!=Type.ARRAY:
            print("La ubicacion de los indices no concuerda con una variable tipo arreglo")
            return
        if isinstance(listaValores,Return):
            listaValores = listaValores.value
        else:
            listaValores = listaValores.valor
        if index > len(listaValores):
            print("Indice mayor al maximo del arreglo")
            env.getGlobal().listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,times.strftime("%c")))
            return 
        if len(listaAcceso) == 0:
            sim = listaValores[index-1]
            if sim.tipo!=Type.UNDEFINED:
                sim.valor = nuevo.value
                sim.tipo = nuevo.tipo
            return 
        return self.getValor(listaAcceso,listaValores[index-1].ejecutar(env),env,nuevo)
