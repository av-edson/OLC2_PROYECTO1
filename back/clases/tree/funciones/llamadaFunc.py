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
                        if not (e.tipo==Type.ARRAY or e.tipo==Type.STRUCT   ):
                            if p.tipoDato == None:
                                p.tipoDato = e.tipo
                            entornoInterno.add_variable(p.identificador,e.value,p.tipoDato,2)
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
            return Return()

    def validarFuncion(self,func:Funcion,enviroment,lista):
        listaRegreso=[]
        for expre in lista:
            val:Return = expre.ejecutar(enviroment)
            # si una expresion tiene error se sale del programa
            if val.tipo == Type.UNDEFINED:
                print('Una expresion que envio como parametro contiene error en la funcion')
                return None
            else:
                listaRegreso.append(val)
            # viendo que coincidan los datos de expresiones con los parametros
        if len(func.params) != len(listaRegreso):
            # si tienen numero diferente de parametros
            print('numero de parametros que envio no coicide con el definido')
            return None
        # validando tipo de dato
        for i in range(len(lista)):
            expr:Return = listaRegreso[i]
            param:Parametro = func.params[i]
            if expr.tipo != param.tipoDato:
                if param.tipoDato != None:
                    print('Un tipo de dato no coicide')
                    return None
        return listaRegreso
