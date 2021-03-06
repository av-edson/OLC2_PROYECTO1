import time
from clases.error import Error
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
        gl:Enviroment = enviroment.getGlobal()
        if exp.tipo != Type.BOOL:
            print('Error en la expresion del if')
            gl.listaErrores.append(Error("Error en la expresion a evaluar del if",self.line,self.column,time.strftime("%c")))
            return
        # entra si el if es VERDADERO
        if exp.value == True:
            entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaIF lin_"+str(self.line))
            tieneReturn=self.bloqueInst.ejecutar(entornoInterno)
            if tieneReturn != None:
                return tieneReturn
        # recorre la lista de ELIF 
        elif self.listaELIF != None:
            paso = False
            for instElif in self.listaELIF:
                if paso: return
                aux:SentenciaELIF = instElif
                res = aux.ejecutar(enviroment)
                if res!= None:
                    if res==True:
                        paso = True
                    elif res==False:
                        paso = False
                    else:
                        return res
            if not paso and self.elseST != None: 
                bloque:BloqueInstrucciones = self.elseST
                entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaELSE lin_"+str(self.line))
                e=bloque.ejecutar(entornoInterno)
                if e !=None:
                    return e
        # ejecuta el ELSE
        elif self.elseST != None:
            bloque:BloqueInstrucciones = self.elseST
            entornoInterno:Enviroment = Enviroment(enviroment,"SentenciaELSE lin_"+str(self.line))
            e=bloque.ejecutar(entornoInterno)
            if e !=None:
                return e
        