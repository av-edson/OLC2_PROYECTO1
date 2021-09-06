from clases.enviroment.enviroment import Enviroment
from clases.abstract.instruccion import Instruccion
from clases.abstract.type import Return, Type

class CicloWhile(Instruccion):
    def __init__(self,condicion,bloque, line, column):
        Instruccion.__init__(self,line, column)
        self.condicion = condicion
        self.bloque=bloque
    
    def ejecutar(self, enviroment):
        try:
            expr:Return = self.condicion.ejecutar(enviroment)
            if expr.tipo != Type.BOOL:
                print("espresion no booleana en while")

            entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaWHILE lin_"+str(self.line))
            while expr.value:
                ret=self.bloque.ejecutar(entornoInterno)
                if ret != None:
                    if ret.tipo == Type.BREACKST:
                        break
                    elif ret.tipo == Type.CONTINUEST:
                        expr = self.condicion.ejecutar(enviroment)
                        if expr.tipo != Type.BOOL:
                            print("espresion no booleana en while")
                            return
                        continue
                    elif ret.tipo==Type.RETURNST:
                        return
                    else:
                        if self.validarReturn(entornoInterno):
                            return ret
                        else:
                            print("return no valido ")
                            return
                expr = self.condicion.ejecutar(enviroment)
                if expr.tipo != Type.BOOL:
                    print("espresion no booleana en while")
                    return
        except Exception as e:
            print('Error desconocido en sentencia while')
            print(str(e))

    def validarReturn(self,enviroment:Enviroment):
        padre = enviroment.antecesor
        while padre != None:
            name = str(padre.nombre)
            if name.startswith("funcion"):
                return True
            padre = padre.antecesor
        return False