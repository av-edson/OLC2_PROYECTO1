import time
from clases.error import Error
from clases.abstract.instruccion import Instruccion

class CrearStruct(Instruccion):
    def __init__(self,ide,atributos,mutable, line, column):
        '''ide: identificador \n atributos: lista de simbolos para los atributos \n mutable: booleano para saber'''
        Instruccion.__init__(self,line, column)
        self.identificador = str(ide)
        self.atributos = atributos
        self.mutable = bool(mutable)

    def ejecutar(self, enviroment):
        result=enviroment.addStruct(self.identificador,self)
        if not result:
            env = enviroment.getGlobal()
            env.listaErrores.append(Error("Identificador del struct repetido",self.line,self.column,str(time.strftime("%c"))))
