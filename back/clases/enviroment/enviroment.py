from clases.enviroment.simbolo import *

class Enviroment:
    def __init__(self,antecesor,nombre):
        self.antecesor = antecesor
        self.variables = {}
        self.funciones = {}
        self.nombre = nombre

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
    
    def findLocal(self,idVariable):
        entorno = self
        if idVariable in entorno.variables.keys():
            return entorno.variables[idVariable]
        return None
    
    def findGlobal(self,idVariable):
        entorno =self.getGlobal()
        if idVariable in entorno.variables.keys():
            return entorno.variables[idVariable]
        return None
    
    def add_variable(self,ide,valor,tipo,alcanse):
        '''
            alcance = 1 -> global \n
            alcance = 2 -> local \n
            alcance = 3 -> normal\n
        '''
        entorno = self
        nuevo = Simbolo(valor,ide,tipo)
        if alcanse == 3:
            if self.findVariable(ide) == None:
                self.variables[ide] = nuevo
                return
            else:
                self.modificar_variable(ide,valor)
                return
        elif alcanse==2:
            entorno.variables[ide] = nuevo
        else:
            entorno = self.getGlobal()
            entorno.variables[ide]=nuevo

    def modificar_variable(self,identificador,valor):
        env = self
        while env != None:
            if identificador in env.variables.keys():
                anterior:Simbolo = self.findVariable(identificador)
                nuevo = Simbolo(valor,anterior.simbolId,anterior.tipo)
                env.variables[identificador] = nuevo
                return
            else:
                env = env.antecesor

    def add_function(self,identificador,funcion):
        if identificador in self.funciones.keys():
            print('No se admiten funciones repetidas')
        else:
            self.funciones[identificador] = funcion 


    def get_fuction(self,identificador):
        env = self
        while env != None:
            if identificador in env.funciones.keys():
                return env.funciones[identificador]
            env = env.antecesor
        return None
