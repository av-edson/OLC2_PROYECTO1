from clases.enviroment.simbolo import *

class Enviroment:
    def __init__(self,antecesor):
        self.antecesor = antecesor
        self.variables = {}
        self.funciones = {}

    def getGlobal(self):
        entorno = self
        while entorno.antecesor != None:
            entorno = entorno.antecesor
        return entorno

    def findVariable(self,idVariable):
        entorno = self
        while entorno != None:
            if idVariable in entorno.variables.keys():
                return entorno.variables[idVariable]
            entorno = entorno.antecesor
        return None
        