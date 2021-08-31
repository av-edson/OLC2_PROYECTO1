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
        if self.expr2 != None:
            inicio = self.expr1.ejecutar(enviroment)
            fin = self.expr2.ejecutar(enviroment)
            if inicio.tipo != Type.INT or fin.tipo!= Type.INT:
                print(' error en el rango del ciclo for')
                return
            entornoInterno:Enviroment = Enviroment(enviroment,"ciclo for")
            entornoInterno.add_variable(self.variable,inicio.value,Type.INT,2)
            inicio = inicio.value
            fin = fin.value
            ciclo = self.valuarRango(entornoInterno.findVariable(self.variable).valor,fin)
            while ciclo:
                ret =self.bloque.ejecutar(entornoInterno)
                if ret != None:
                    if ret.tipo == Type.BREACKST:
                        break
                    elif ret.tipo == Type.CONTINUEST:
                        continue
                    else:
                        return ret
                inicio+=1
                entornoInterno.modificar_variable(self.variable,inicio)
                ciclo = self.valuarRango(inicio,fin)
            

    def valuarRango(self,inicio,fin):
        if inicio <= fin:
            return True 
        else: 
            return False
