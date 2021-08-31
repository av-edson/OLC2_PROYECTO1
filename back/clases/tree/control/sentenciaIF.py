from clases.abstract.instruccion import Instruccion
from clases.enviroment.enviroment import Enviroment
from clases.tree.control.sentenciaELIF import SentenciaELIF
from clases.tree.bloqueInstrucciones import BloqueInstrucciones
from clases.abstract.type import *

class SentenciaIF(Instruccion):
    def __init__(self,condicion,instrucciones,line,column,listaElif=None,elseSt=None):
        Instruccion.__init__(self,line, column)
        self.condicion = condicion
        self.bloqueInst = instrucciones
        self.elseST = elseSt
        self.listaELIF = listaElif
    
    def ejecutar(self, enviroment):
        exp:Return = self.condicion.ejecutar(enviroment)
        if exp.tipo != Type.BOOL:
            print('Error en la expresion del if')
            return
        if exp.value == True:
            entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaIF lin_"+str(self.line))
            tieneReturn=self.bloqueInst.ejecutar(entornoInterno)
            return
        if self.listaELIF != None:
            for instElif in self.listaELIF:
                aux:SentenciaELIF = instElif
                res = aux.ejecutar(enviroment)
                if res: return
        
        if self.elseST != None:
            bloque:BloqueInstrucciones = self.elseST
            entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaELSE lin_"+str(self.line))
            bloque.ejecutar(enviroment)
