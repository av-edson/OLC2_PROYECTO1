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
        self.listaDatosExpresiones = []
    
    def ejecutar(self, enviroment):
        env:Enviroment = enviroment
        func:Funcion = env.get_fuction(self.ide)
        if func != None:
            entornoInterno =  Enviroment(env,"funcion_"+str(self.ide))
            if self.validarFuncion(func,enviroment):
                # declarando las variables en el entorno
                if self.lista != None:
                    for i in range(len(self.lista)):
                        p:Parametro = func.params[i]
                        e:Return = self.listaDatosExpresiones[i]
                        # referencia de listas y structs
                        if not (e.tipo==Type.ARRAY or e.tipo==Type.STRUCT   ):
                            entornoInterno.add_variable(p.identificador,e.value,p.tipoDato,3)
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

    def validarFuncion(self,func:Funcion,enviroment):
        for expre in self.lista:
            val:Return = expre.ejecutar(enviroment)
            # si una expresion tiene error se sale del programa
            if val.tipo == Type.UNDEFINED:
                print('Una expresion que envio como parametro contiene error en la funcion')
                return False
            self.listaDatosExpresiones.append(val)
            # viendo que coincidan los datos de expresiones con los parametros
        if len(func.params) != len(self.listaDatosExpresiones):
            # si tienen numero diferente de parametros
            print('numero de parametros que envio no coicide con el definido')
            return False
        # validando tipo de dato
        for i in range(len(self.listaDatosExpresiones)):
            expr:Return = self.listaDatosExpresiones[i]
            param:Parametro = func.params[i]
            if expr.tipo != param.tipoDato:
                if param.tipoDato != None:
                    print('Un tipo de dato no coicide')
                    return False
        return True
