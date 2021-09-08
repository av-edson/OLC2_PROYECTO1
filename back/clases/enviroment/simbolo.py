from clases.abstract.expresion import Expresion
from clases.abstract.type import *

class Simbolo:

    def __init__(self,valor,identificador,tipo=None,fila=None,columna=None,tipoStruct=None,mutable=None):
        self.valor=valor
        self.simbolId=identificador
        self.tipo:Type=tipo
        self.fila = fila
        self.columna = columna
        # structs 
        if tipoStruct!=None:
            self.tipoStruct = tipoStruct
            self.atributos = []