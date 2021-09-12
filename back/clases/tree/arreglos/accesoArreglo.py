from clases.expresiones.expresionLiteral import ExpresionLiteral
from clases.enviroment.enviroment import Enviroment
import time
from clases.error import Error
from clases.abstract.type import Return, Type
from clases.abstract.expresion import Expresion

class AccesoArreglo(Expresion):
    def __init__(self,var,listaAcceso, line, column):
        Expresion.__init__(self,line, column)
        self.identificador = str(var)
        self.listaAcceso = listaAcceso
    
    def ejecutar(self, enviroment):
        try:
            listaAcceso = list.copy(self.listaAcceso)
            gl = enviroment.getGlobal()
            lista = enviroment.findVariable(self.identificador)
            if lista == None:
                print("No existe arreglo al que decea accesar")
                gl.listaErrores.append(Error("No existe arreglo al que decea accesar",self.line,self.column,time.strftime("%c")))
                return Return()
            if lista.tipo!=Type.ARRAY:
                print("id no pertenece a un arreglo")
                gl.listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
                return Return()
            lista = lista.valor
            if len(listaAcceso)==1:
                index = listaAcceso.pop()
                esRango = False
                if isinstance(index,Expresion):
                    index = index.ejecutar(enviroment)
                else:
                    esRango = True
                    inicio = index[0].ejecutar(enviroment)
                    index = index[1].ejecutar(enviroment)
                #lista = lista.value
                if index.tipo!=Type.INT:
                    print("Solo se admiten enteros para acceder a un arreglo")
                    gl.listaErrores.append(Error("Solo se admiten enteros para acceder a un arreglo",self.line,self.column,time.strftime("%c")))
                    return Return()
                index=index.value
                if index > len(lista):
                    print("Indice mayor al maximo del arreglo")
                    gl.listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
                    return Return()
                if not esRango:
                    sim = lista[index-1].ejecutar(enviroment)
                    if sim.tipo!=Type.UNDEFINED:
                        return Return(sim.value,sim.tipo)
                    return Return()
                else:
                    inicio = inicio.value
                    if inicio > len(lista):
                        print("Indice mayor al maximo del arreglo")
                        gl.listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
                        return Return()
                    return self.getRango(inicio,index,lista,enviroment)
            else:
                listaAcceso = list(reversed(self.listaAcceso))
                a=enviroment.findVariable(self.identificador)
                return self.getValor(listaAcceso,enviroment.findVariable(self.identificador),enviroment)
        except:
            print("errro inesperado en acceso a arreglo")
            return Return()

    def getValor(self,listaAcceso:list,listaValores:list,env:Enviroment):
        index = listaAcceso.pop()

        esRango = False
        if isinstance(index,ExpresionLiteral):
            index = index.ejecutar(env)
        else:
            esRango = True
            inicio = index[0].ejecutar(env)
            index = index[1].ejecutar(env)
        if index.tipo!=Type.INT:
            print("Solo se admiten enteros para acceder a un arreglo")
            return Return()
        index=index.value
        if listaValores.tipo!=Type.ARRAY:
            print("La ubicacion de los indices no concuerda con una variable tipo arreglo")
            return Return()
        if isinstance(listaValores,Return):
            listaValores = listaValores.value
        else:
            listaValores = listaValores.valor
        if index > len(listaValores):
            print("Indice mayor al maximo del arreglo")
            env.getGlobal().listaErrores.append(Error("expresion no admitida dentro del arreglo, None",self.line,self.column,time.strftime("%c")))
            return Return()
        
        if len(listaAcceso) == 0:
            if not esRango:
                sim = listaValores[index-1].ejecutar(env)
                if sim.tipo!=Type.UNDEFINED:
                    return Return(sim.value,sim.tipo)
                return Return()
            else:
                inicio = inicio.value
                if inicio > len(listaValores):
                    print("Indice mayor al maximo del arreglo")
                    return Return()
                return self.getRango(inicio,index,listaValores,env)
        #simbolo = listaValores[index-1].ejecutar(env)
        return self.getValor(listaAcceso,listaValores[index-1].ejecutar(env),env)

    def getRango(self,inicio,fin,lista,env):
        regreso = []
        for i in range(fin-1):
            i=i+inicio-1
            ret = lista[i]
            regreso.append(ret)
        
        return Return(regreso,Type.ARRAY)