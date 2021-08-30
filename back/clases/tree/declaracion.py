from clases.abstract.instruccion import Instruccion
from clases.abstract.type import *
from clases.enviroment.enviroment import Enviroment
from clases.enviroment.simbolo import Simbolo

class Asignacion(Instruccion):
    def __init__(self,identificador,expresion,tipo,alcanse, line, column):
        Instruccion.__init__(self,line, column)
        self.ide = identificador
        self.valor=expresion
        self.tipo = tipo
        self.alcance=alcanse
            
    # alcance = 1 = global
    # alcance = 2 = local
    # alcance = 3 = normal
    def modificar_alcance(self,alcance):
        self.alcance = alcance
    def ejecutar(self, env:Enviroment):
        # simbolo de regreso
        reg:Return = self.valor.ejecutar(env)
        if reg.tipo == Type.UNDEFINED:
            print(' expresion no valida para asignar la variable')
        # validar el tipo de dato dentro de la expresion a asignar
        t = reg.tipo
        if (t==Type.ARRAY or t==Type.UNDEFINED or t==Type.RETURNST or t==Type.BREACKST or t==Type.CONTINUEST): 
            print('error en la declaracion de la variable')
            return
        # asignar tipo de variable si no tiene
        if self.tipo == None:
            self.tipo=t
        else:
            if self.tipo != t:
                print('-------expresion y tipo de dato en asignacion no coiciden-----')
                return
        env.add_variable(self.ide,reg.value,self.tipo,self.alcance)


class DeclaracionGloLoc(Instruccion):
    '''
    Esta clase solo se utiliza para modificar\n el alcanze de una variable a local o global
    \n 1 es global \n 2 es local \n 3 es normal
    '''
    def __init__(self,identificador,alcance, line, column):
        Instruccion.__init__(self,line, column)
        self.ide=identificador
        self.alcance = alcance
    
    def ejecutar(self, enviroment):
        env:Enviroment = enviroment
        var:Simbolo = env.findVariable(self.ide)
        env.add_variable(self.ide,var.valor,var.tipo,self.alcance)
