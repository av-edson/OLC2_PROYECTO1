#from clases.enviroment.simbolo import Simbolo
from clases.abstract.expresion import Expresion
#from clases.enviroment.enviroment import Enviroment
from clases.abstract.type import *
from enum import Enum

class OperacionesBinarias(Enum):
    SUMA=0
    RESTA=1
    MULTIPLICACION=2
    DIVISION=3
    POTENCIA=4
    MODULO=5

class ExpresionBinaria(Expresion):
    def __init__(self,tipo,izquierdo,derecho, line, column):
        Expresion.__init__(self,line,column)
        self.tipo = tipo
        # son clases que heredan de expresion
        self.izquierdo=izquierdo 
        self.derecho=derecho
    
    def ejecutar(self, enviroment):
        izquierdo = self.izquierdo.ejecutar(enviroment)
        derecho = self.derecho.ejecutar(enviroment)

        try:
            if self.tipo == OperacionesBinarias.SUMA:
                regreso = self.suma(izquierdo,derecho)
            elif self.tipo == OperacionesBinarias.RESTA:
                regreso = self.resta(izquierdo,derecho)
            elif self.tipo==OperacionesBinarias.MULTIPLICACION:
                regreso=self.multiplicacion(izquierdo,derecho)
            elif self.tipo==OperacionesBinarias.DIVISION:
                regreso=self.division(izquierdo,derecho)
            elif self.tipo==OperacionesBinarias.POTENCIA:
                regreso=self.potencia(izquierdo,derecho)
            elif self.tipo==OperacionesBinarias.MODULO:
                regreso=self.modulo(izquierdo,derecho)
            else:
                return Return()
        except Exception:
            print("--------Error en la operacion binaria------")
        
        return regreso

    def suma(self,iz,der):
        # si no es una cadena, entero o decimal devolvemos error
        if not(iz.tipo==Type.INT or iz.tipo==Type.STRING or iz.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        if not(der.tipo==Type.INT or der.tipo==Type.STRING or der.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        # seguimos con la ejecucion
        regreso = Return()
        if iz.tipo == Type.STRING or der.tipo == Type.STRING:
            regreso.value = str(iz.value)+str(der.value)
            regreso.tipo=Type.STRING
        elif iz.tipo == Type.FLOAT or der.tipo == Type.FLOAT:
            regreso.value = float(iz.value) + float(der.value)
            regreso.tipo=Type.FLOAT
        else:
            regreso.value = iz.value+der.value
            regreso.tipo=Type.INT
        return regreso
    def resta(self,iz,der):
        # si no es una  entero o decimal devolvemos error
        if not(iz.tipo==Type.INT or iz.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        if not(der.tipo==Type.INT or der.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        # seguimos con la ejecucion
        regreso = Return()
        if iz.tipo == Type.FLOAT or der.tipo == Type.FLOAT:
            regreso.value = float(iz.value) - float(der.value)
            regreso.tipo=Type.FLOAT
        else:
            regreso.value = iz.value-der.value
            regreso.tipo=Type.INT
        return regreso
    def multiplicacion(self,iz,der):
        if not(iz.tipo==Type.INT or iz.tipo==Type.FLOAT or iz.tipo==Type.STRING):
            return Return(0,Type.UNDEFINED)
        if not(der.tipo==Type.INT or der.tipo==Type.FLOAT or iz.tipo==Type.STRING):
            return Return(0,Type.UNDEFINED)
        regreso = Return()
        if iz.tipo == Type.FLOAT or der.tipo == Type.FLOAT:
            regreso.value = float(iz.value) * float(der.value)
            regreso.tipo=Type.FLOAT
        elif iz.tipo==Type.STRING or der.tipo==Type.STRING:
            regreso.value = str(iz.value)+str(der.value)
            regreso.tipo=Type.STRING
        else:
            regreso.value = iz.value*der.value
            regreso.tipo=Type.INT
        return regreso
    def division(self,iz,der):
        if not(iz.tipo==Type.INT or iz.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        if not(der.tipo==Type.INT or der.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        regreso = Return()
        if der.value == 0:
            print('------division por cero----')
            return regreso
        if iz.tipo == Type.FLOAT or der.tipo == Type.FLOAT:
            regreso.value = float(iz.value) / float(der.value)
            regreso.tipo=Type.FLOAT
        else:
            regreso.value = iz.value/der.value
            regreso.tipo=Type.INT
        return regreso
    def potencia(self,iz,der):
        if not(iz.tipo==Type.INT or iz.tipo==Type.FLOAT or iz.tipo==Type.STRING):
            return Return(0,Type.UNDEFINED)
        if not(der.tipo==Type.INT or der.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        regreso = Return()
        if iz.tipo==Type.STRING:
            regreso.value = str(iz.value)*int(der.value)
            regreso.tipo=Type.STRING
        elif iz.tipo == Type.FLOAT or der.tipo == Type.FLOAT:
            regreso.value = float(iz.value) ** float(der.value)
            regreso.tipo=Type.FLOAT
        else:
            regreso.value = iz.value**der.value
            regreso.tipo=Type.INT
        return regreso
    def modulo(self,iz,der):
        if not(iz.tipo==Type.INT or iz.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        if not(der.tipo==Type.INT or der.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        regreso = Return()
        if iz.tipo == Type.FLOAT or der.tipo == Type.FLOAT:
            regreso.value = float(iz.value) % float(der.value)
            regreso.tipo=Type.FLOAT
        else:
            regreso.value = iz.value%der.value
            regreso.tipo=Type.INT
        return regreso
