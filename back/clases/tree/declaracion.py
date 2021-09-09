from clases.tree.arreglos.declaracionArreglo import DeclaracionArreglo
import time
from clases.error import Error
from clases.abstract.instruccion import Instruccion
from clases.abstract.type import *
from clases.enviroment.enviroment import Enviroment
from clases.enviroment.simbolo import Simbolo

class Asignacion(Instruccion):
    def __init__(self,identificador,expresion,tipo,alcanse, line, column):
        Instruccion.__init__(self,line, column)
        self.ide = str(identificador)
        self.valor=expresion
        self.tipo = tipo
        self.alcance=alcanse
            
    # alcance = 1 = global
    # alcance = 2 = local
    # alcance = 3 = normal
    def modificar_alcance(self,alcance):
        self.alcance = alcance
    def ejecutar(self, env:Enviroment):
        gl:Enviroment = env.getGlobal()
        try:
            # simbolo de regreso
            reg:Return = self.valor.ejecutar(env)
            if reg.tipo == Type.UNDEFINED:
                print(' expresion no valida para asignar la variable')
                gl.listaErrores.append(Error("expresion no valida para asignar la variable "+str(self.ide),self.line,self.column,time.strftime("%c")))
                return
            # validar el tipo de dato dentro de la expresion a asignar
            t = reg.tipo
            if (t==Type.RETURNST or t==Type.BREACKST or t==Type.CONTINUEST): 
                print('error en la declaracion de la variable')
                gl.listaErrores.append(Error("Error en la declaracion de la variable"+str(self.ide),self.line,self.column,time.strftime("%c")))
                return
            if t==Type.ARRAY:
                env.add_variable(self.ide,reg.value,Type.ARRAY,3,self.line,self.column)
                return
            # asignar tipo de variable si no tiene
            tipoAux = None
            if self.tipo == None:
                tipoAux=t
            else:
                if self.tipo != t:
                    print('-------expresion y tipo de dato en asignacion no coiciden-----')
                    gl.listaErrores.append(Error("Expresion y tipo de dato en asignacion no coiciden "+str(self.ide),self.line,self.column,time.strftime("%c")))
                    return
                tipoAux = self.tipo
                
            if tipoAux == Type.STRUCT:
                reg = reg.value
                atributos = reg.valor
                struct = reg.tipoStruct
                env.addVariableStruct(self.ide,struct,struct.mutable,atributos)
                return
            env.add_variable(self.ide,reg.value,tipoAux,self.alcance,self.line,self.column)
        except:
            gl.listaErrores.append(Error("Error inesperado en declaracion "+str(self.ide),self.line,self.column,time.strftime("%c")))


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
        env.add_variable(self.ide,var.valor,var.tipo,self.alcance,self.line,self.column)
