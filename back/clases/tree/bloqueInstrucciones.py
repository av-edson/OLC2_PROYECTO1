import time
from clases.error import Error
from clases.abstract.instruccion import Instruccion
from clases.enviroment.enviroment import Enviroment

class BloqueInstrucciones(Instruccion):
    def __init__(self,instrucciones,line,column):
        self.listaInstrucciones = instrucciones
        self.line=line
        self.column=column
    def ejecutar(self, enviroment):
        try:
            for instruccion in self.listaInstrucciones:
                regreso = instruccion.ejecutar(enviroment)
            if regreso != None:
                return regreso
        except:
            gl = enviroment.getGlobal()
            gl.listaErrores.append(Error("Error inesperado en instruccion"+str(self.ide),self.line,self.column,time.strftime("%c")))