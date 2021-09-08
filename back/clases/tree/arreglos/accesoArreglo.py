from clases.enviroment.enviroment import Enviroment
import time
from clases.error import Error
from clases.abstract.type import Return, Type
from clases.abstract.expresion import Expresion

class AccesoArreglo(Expresion):
    def __init__(self,var,listaAcceso, line, column):
        Expresion.__init__(self,line, column)
        self.variable = str(var)
        self.listaAcceso = listaAcceso
    
    def ejecutar(self, enviroment):
        try:
            gl = enviroment.getGlobal()
            lista = enviroment.findVariable(self.variable)
            if lista.tipo!=Type.ARRAY:
                print("id no pertenece a un arreglo")
                gl.listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
                return Return()
            lista = lista.valor
            if len(self.listaAcceso)==1:
                index = self.listaAcceso.pop()
                index = index.ejecutar(enviroment)
                lista = lista.value
                if index.tipo!=Type.INT:
                    print("Solo se admiten enteros para acceder a un arreglo")
                    gl.listaErrores.append(Error("Solo se admiten enteros para acceder a un arreglo",self.line,self.column,time.strftime("%c")))
                    return Return()
                index=index.value
                if index > len(lista):
                    print("Indice mayor al maximo del arreglo")
                    gl.listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
                    return Return()
                sim = lista[index-1].ejecutar(enviroment)
                if sim.tipo!=Type.UNDEFINED:
                    return Return(sim.value,sim.tipo)
            else:
                self.listaAcceso = list(reversed(self.listaAcceso))
                return self.getValor(self.listaAcceso,lista,enviroment)
        except:
            print("errro inesperado en acceso a arreglo")

    def getValor(self,listaAcceso:list,listaValores:list,env:Enviroment):
        expre = listaAcceso.pop()
        index = expre.ejecutar(env)
        if index.tipo!=Type.INT:
            print("Solo se admiten enteros para acceder a un arreglo")
            return Return()
        index=index.value
        if listaValores.tipo!=Type.ARRAY:
            print("La ubicacion de los indices no concuerda con una variable tipo arreglo")
            return Return()
        listaValores = listaValores.value
        if index > len(listaValores):
            print("Indice mayor al maximo del arreglo")
            env.getGlobal().listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
            return Return()
        if len(listaAcceso) == 0:
            sim = listaValores[index-1].ejecutar(env)
            if sim.tipo!=Type.UNDEFINED:
                return Return(sim.value,sim.tipo)
            return Return()
        simbolo = listaValores[index-1].ejecutar(env)
        return self.getValor(listaAcceso,listaValores[index-1].ejecutar(env),env)
