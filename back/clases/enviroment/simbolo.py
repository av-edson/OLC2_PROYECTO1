from clases.abstract.expresion import Expresion
from clases.abstract.type import *

class Simbolo:

    def __init__(self,valor,identificador,tipo=None):
        self.valor=valor
        self.simbolId=identificador
        self.tipo:Type=tipo