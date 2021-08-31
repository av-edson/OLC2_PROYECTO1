from clases.abstract.instruccion import *
from clases.enviroment.enviroment import Enviroment
from clases.tree.bloqueInstrucciones import BloqueInstrucciones
from clases.abstract.type import *

class SentenciaELIF(Instruccion):
    def __init__(self,condicion,instrucciones, line, column):
        Instruccion.__init__(self,line, column)
        self.condicion = condicion
        self.bloque  = instrucciones
    
    def ejecutar(self, enviroment):
        exp:Return = self.condicion.ejecutar(enviroment)
        if exp.tipo != Type.BOOL:
            print('error en expresion de elif')
            return False
        if exp.value ==False:
            return False
        
        if exp.value:
            entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaIFLIF lin_"+str(self.line))
            tieneReturn=self.bloque.ejecutar(entornoInterno)
        return True
