import time
from clases.error import Error
from clases.tree.bloqueInstrucciones import BloqueInstrucciones
from clases.enviroment.simbolo import Simbolo
from clases.enviroment.enviroment import Enviroment
from clases.abstract.instruccion import Instruccion
from clases.abstract.type import Return, Type

class CicloFor(Instruccion):
    def __init__(self,varControl,expre1,bloque, line, column,expre2=None):
        Instruccion.__init__(self,line, column)
        self.variable=varControl
        self.expr1 = expre1
        self.expr2 = expre2
        self.bloque:BloqueInstrucciones = bloque
    
    def ejecutar(self, enviroment):
        # rango entre 2 numeros
        gl:Enviroment = enviroment.getGlobal()
        if self.expr2 != None:
            inicio = self.expr1.ejecutar(enviroment)
            fin = self.expr2.ejecutar(enviroment)
            if inicio.tipo != Type.INT or fin.tipo!= Type.INT:
                print('error en el rango del ciclo for')
                gl.listaErrores.append(Error("error en el rango del ciclo for",self.line,self.column,time.strftime("%c")))
                return
            entornoInterno:Enviroment = Enviroment(enviroment,"ciclo for")
            entornoInterno.add_variable(self.variable,inicio.value,Type.INT,2,self.line,self.column)
            inicio = inicio.value
            fin = fin.value
            ciclo = self.valuarRango(entornoInterno.findVariable(self.variable).valor,fin)
            while ciclo:
                ret =self.bloque.ejecutar(entornoInterno)
                if ret != None:
                    if ret.tipo == Type.BREACKST:
                        break
                    elif ret.tipo != Type.CONTINUEST:
                        return ret
                inicio+=1
                entornoInterno.modificar_variable(self.variable,inicio,None)
                ciclo = self.valuarRango(inicio,fin)
        else:
            var = self.expr1.ejecutar(enviroment)
            if var.tipo==Type.STRING:
                var = str(var.value)
                listaCaracteres = []
                for car in var:
                    listaCaracteres.append(car)
                inicio = 1
                fin = len(listaCaracteres)
                entornoInterno:Enviroment = Enviroment(enviroment,"ciclo for")
                entornoInterno.add_variable(self.variable,listaCaracteres[inicio-1],Type.STRING,2,self.line,self.column)
                ciclo = self.valuarRango(inicio,fin)
                while ciclo:
                    ret =self.bloque.ejecutar(entornoInterno)
                    if ret != None:
                        if ret.tipo == Type.BREACKST:
                            break
                        elif ret.tipo != Type.CONTINUEST:
                            if ret.tipo==Type.RETURNST:
                                return
                            else:
                                if self.validarReturn(entornoInterno):
                                    return ret
                                else:
                                    print("return no valido ")
                                    gl.listaErrores.append(Error("return no valido",self.line,self.column,time.strftime("%c")))
                                    return
                    inicio+=1
                    ciclo = self.valuarRango(inicio,fin)
                    if ciclo:
                        entornoInterno.modificar_variable(self.variable,listaCaracteres[inicio-1],None)
            elif var.tipo==Type.ARRAY:
                var = var.value
                entornoInterno:Enviroment = Enviroment(enviroment,"ciclo for")
                for expreLiteral in var:
                    iterador = expreLiteral.ejecutar(enviroment)
                    if iterador.tipo==Type.UNDEFINED:
                        print("error en iterador")
                        return
                    entornoInterno.add_variable(self.variable,iterador.value,iterador.tipo,2,self.line,self.column)
                    ret =self.bloque.ejecutar(entornoInterno)
                    if ret != None:
                        if ret.tipo == Type.BREACKST:
                            break
                        elif ret.tipo != Type.CONTINUEST:
                            return ret
            else:
                print('expresion invalida para el ciclo for')
                gl.listaErrores.append(Error("expresion invalida para el ciclo for",self.line,self.column,time.strftime("%c")))

    def valuarRango(self,inicio,fin):
        if inicio <= fin:
            return True 
        else: 
            return False

    def validarReturn(self,enviroment:Enviroment):
        padre = enviroment.antecesor
        while padre != None:
            name = str(padre.nombre)
            if name.startswith("funcion"):
                return True
            padre = padre.antecesor
        return False