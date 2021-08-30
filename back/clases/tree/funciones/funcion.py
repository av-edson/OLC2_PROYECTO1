from clases.enviroment.enviroment import Enviroment
from clases.abstract.instruccion import Instruccion
from clases.abstract.expresion import Expresion

class Funcion(Instruccion):
    def __init__(self,identificador,instrucciones,parametros, line, column):
        Instruccion.__init__(self,line, column)
        self.ide = identificador
        self.instrucciones = instrucciones
        self.params = parametros
    
    def ejecutar(self, enviroment:Enviroment):
        enviroment.add_function(self.ide,self)