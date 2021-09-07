import time
from clases.error import Error
from clases.tree.bloqueInstrucciones import BloqueInstrucciones
from clases.tree.funciones.funcion import Funcion
from clases.tree.funciones.parametro import Parametro
from clases.abstract.type import Return, Type
from clases.enviroment.enviroment import Enviroment
from clases.abstract.instruccion import Instruccion
from clases.abstract.expresion import Expresion

class LLamadaFuncion(Expresion):
    def __init__(self,identificador,listaExpr, line, column):
        Expresion.__init__(self,line, column)
        self.lista = listaExpr
        self.ide = identificador
    
    def ejecutar(self, enviroment):
        gl:Enviroment = enviroment.getGlobal()
        try:
            func:Funcion = enviroment.get_fuction(self.ide)
            if func != None:
                entornoInterno =  Enviroment(enviroment,"funcion_"+str(self.ide))
                listaRegreso = self.validarFuncion(func,enviroment,self.lista)
                if listaRegreso != None:
                    # declarando las variables en el entorno
                    if self.lista != None:
                        for i in range(len(self.lista)):
                            p:Parametro = func.params[i]
                            e:Return = listaRegreso[i] 
                            # referencia de listas y structs
                            if p.tipoDato == None:
                                p.tipoDato = e.tipo
                            if not (e.tipo==Type.ARRAY or e.tipo==Type.STRUCT   ):
                                entornoInterno.add_variable(p.identificador,e.value,p.tipoDato,2)
                            else:
                                # agregando variable local struct
                                e = e.value
                                entornoInterno.addVariableStruct(p.identificador,e.tipoStruct,e.tipoStruct.mutable,e.atributos)

                    # ejecutando las instrucciones de la funcion
                    bloque:BloqueInstrucciones = func.instrucciones
                    tieneReturn=bloque.ejecutar(entornoInterno)
                    if tieneReturn !=None:
                        return tieneReturn
                    #print('espero todo haya salido bien xd')
                else:
                    return Return()
            else:
                print('Funcion no definida o no se encontro')
                gl.listaErrores.append(Error("Funcion no definida o no se encontro",self.line,self.column,time.strftime("%c")))
                return Return()
        except:
            print("Error desconocido dentro de la funcion"+str(self.ide))
            gl.listaErrores.append(Error("Error desconocido dentro de la funcion",self.line,self.column,time.strftime("%c")))

    def validarFuncion(self,func:Funcion,enviroment,lista):
        listaRegreso=[]
        gl:Enviroment = enviroment.getGlobal()
        for expre in lista:
            val:Return = expre.ejecutar(enviroment)
            # si una expresion tiene error se sale del programa
            if val.tipo == Type.UNDEFINED:
                print('Una expresion que envio como parametro contiene error en la funcion')
                gl.listaErrores.append(Error("Una expresion que envio como parametro contiene error en la funcion",self.line,self.column,time.strftime("%c")))
                return None
            else:
                listaRegreso.append(val)
            # viendo que coincidan los datos de expresiones con los parametros
        if len(func.params) != len(listaRegreso):
            # si tienen numero diferente de parametros
            print('numero de parametros que envio no coicide con el definido')
            gl.listaErrores.append(Error("Numero de parametros que envio no coicide con el definido",self.line,self.column,time.strftime("%c")))
            return None
        # validando tipo de dato
        for i in range(len(lista)):
            expr:Return = listaRegreso[i]
            param:Parametro = func.params[i]
            if expr.tipo != param.tipoDato:
                if param.tipoDato != None:
                    print('Un tipo de dato no coicide')
                    gl.listaErrores.append(Error("Un tipo de dato no coicide",self.line,self.column,time.strftime("%c")))
                    return None
        return listaRegreso
