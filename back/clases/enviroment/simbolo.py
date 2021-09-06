from clases.abstract.expresion import Expresion
from clases.abstract.type import *

class Simbolo:

    def __init__(self,valor,identificador,tipo=None,tipoStruct=None,mutable=None):
        self.valor=valor
        self.simbolId=identificador
        self.tipo:Type=tipo
        # structs 
        if tipoStruct!=None:
            self.tipoStruct = tipoStruct
            self.atributos = []