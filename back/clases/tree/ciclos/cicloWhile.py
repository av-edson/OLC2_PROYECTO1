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

            entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaELSE lin_"+str(self.line))
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
                    else:
                        return ret
                expr = self.condicion.ejecutar(enviroment)
                if expr.tipo != Type.BOOL:
                    print("espresion no booleana en while")
                    return
        except:
            print('Error desconocido en sentencia while')
