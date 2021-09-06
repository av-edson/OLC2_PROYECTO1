from clases.abstract.expresion import Expresion
#from clases.enviroment.enviroment import Enviroment
from clases.abstract.type import *
from enum import Enum

class OpRelacional(Enum):
    MAYORQUE=0
    MENORQUE=1
    MAYORIGUAL=3
    MENORIGUAL=4
    IGUALIGUAL=5
    DIFERENTE=6

class ExpresionRelacional(Expresion):
    def __init__(self,izquierdo,derecho,tipo, line, column):
        Expresion.__init__(self,line, column)
        self.izquierdo=izquierdo
        self.derecho=derecho
        self.tipo:OpRelacional = tipo
    def ejecutar(self, enviroment):
        try:
            der = self.derecho.ejecutar(enviroment)
            izq = self.izquierdo.ejecutar(enviroment)
            if not(izq.tipo==Type.INT or izq.tipo==Type.FLOAT or izq.tipo==Type.STRING):
                if not (self.tipo==OpRelacional.DIFERENTE or self.tipo==OpRelacional.IGUALIGUAL):
                    return Return()
            if not(der.tipo==Type.INT or der.tipo==Type.FLOAT or der.tipo==Type.STRING):
                if not (self.tipo==OpRelacional.DIFERENTE or self.tipo==OpRelacional.IGUALIGUAL):
                    return Return()
            if self.tipo==OpRelacional.MAYORQUE:
                return self.mayor(izq,der)
            elif self.tipo==OpRelacional.MENORQUE:
                return self.menor(izq,der)
            elif self.tipo==OpRelacional.MAYORIGUAL:
                return self.mayor_igual(izq,der)
            elif self.tipo==OpRelacional.MENORIGUAL:
                return self.menor_igual(izq,der)
            elif self.tipo==OpRelacional.IGUALIGUAL:
                return self.igual_igual(izq,der)
            elif self.tipo==OpRelacional.DIFERENTE:
                return self.diferente(izq,der)
        except:
            print("-----Error en la expresion relacional "+str(self.line))
            return Return()
        
    def mayor(self,iz,der):
        regreso = Return()
        if iz.tipo==Type.STRING or der.tipo==Type.STRING:
            if iz.tipo==Type.INT or iz.tipo==Type.FLOAT or der.tipo==Type.INT or der.tipo==Type.FLOAT:
                return Return()
            if len(str(iz.value)) > len(str(der.value)):
                regreso.value=True
            else:
                regreso.value=False
        else:
            if iz.value > der.value:
                regreso.value=True
            else:
                regreso.value=False
        regreso.tipo=Type.BOOL
        return regreso
    def menor(self,iz,der):
        regreso = Return()
        if iz.tipo==Type.STRING or der.tipo==Type.STRING:
            if iz.tipo==Type.INT or iz.tipo==Type.FLOAT or der.tipo==Type.INT or der.tipo==Type.FLOAT:
                return Return()
            if len(str(iz.value)) < len(str(der.value)):
                regreso.value=True
            else:
                regreso.value=False
        else:
            if iz.value < der.value:
                regreso.value=True
            else:
                regreso.value=False
        regreso.tipo=Type.BOOL
        return regreso
    def mayor_igual(self,iz,der):
        regreso = Return()
        if iz.tipo==Type.STRING or der.tipo==Type.STRING:
            if iz.tipo==Type.INT or iz.tipo==Type.FLOAT or der.tipo==Type.INT or der.tipo==Type.FLOAT:
                return Return()
            if len(str(iz.value)) >= len(str(der.value)):
                regreso.value=True
            else:
                regreso.value=False
        else:
            if iz.value >= der.value:
                regreso.value=True
            else:
                regreso.value=False
        regreso.tipo=Type.BOOL
        return regreso
    def menor_igual(self,iz,der):
        regreso = Return()
        if iz.tipo==Type.STRING or der.tipo==Type.STRING:
            if iz.tipo==Type.INT or iz.tipo==Type.FLOAT or der.tipo==Type.INT or der.tipo==Type.FLOAT:
                return Return()
            if len(str(iz.value)) <= len(str(der.value)):
                regreso.value=True
            else:
                regreso.value=False
        else:
            if iz.value <= der.value:
                regreso.value=True
            else:
                regreso.value=False
        regreso.tipo=Type.BOOL
        return regreso
    def igual_igual(self,iz,der):
        regreso:Return = Return()
        if iz.tipo==Type.STRING or der.tipo==Type.STRING:
            if str(iz.value) == str(der.value):
                regreso.value=True
            else:
                regreso.value=False
        elif iz.tipo==Type.FLOAT or der.tipo==Type.FLOAT:
            if float(iz.value) == float(der.value):
                regreso.value=True
            else:
                regreso.value=False
        else:
            if iz.value == der.value:
                regreso.value=True
            else:
                regreso.value=False
        regreso.tipo=Type.BOOL
        return regreso
    def diferente(self,iz,der):
        regreso:Return = Return()
        if iz.tipo==Type.STRING or der.tipo==Type.STRING:
            if str(iz.value) != str(der.value):
                regreso.value=True
            else:
                regreso.value=False
        elif iz.tipo==Type.FLOAT or der.tipo==Type.FLOAT:
            if float(iz.value) != float(der.value):
                regreso.value=True
            else:
                regreso.value=False
        else:
            if iz.value != der.value:
                regreso.value=True
            else:
                regreso.value=False
        regreso.tipo=Type.BOOL
        return regreso


class OpeLogica(Enum):
    OR=0
    AND=2
    NOT=3

class ExpresionLogica(Expresion):
    def __init__(self,izquierdo,derecho,tipo, line, column):
        Expresion.__init__(self,line, column)
        self.izquierdo=izquierdo
        self.derecho=derecho
        self.tipo=tipo

    def ejecutar(self, enviroment):
        izq=self.izquierdo.ejecutar(enviroment)
        if self.tipo!=OpeLogica.NOT:
            der=self.derecho.ejecutar(enviroment)
        else:
            if not(izq.tipo==Type.BOOL):
                return Return()
            else:
                return self.operacion_not(izq)

        if not(izq.tipo==Type.BOOL) or not(der.tipo==Type.BOOL):
            return Return()
        if self.tipo==OpeLogica.OR:
            return self.operacion_or(izq,der)
        elif self.tipo==OpeLogica.AND:
            return self.operacion_and(izq,der)
            

    def operacion_or(self,izq,der):
        regreso = Return()
        if bool(izq.value)==True or bool(der.value)==True:
            regreso.value=True
        else:
            regreso.value=False
        regreso.tipo=Type.BOOL
        return regreso  
    def operacion_and(self,izq,der):
        regreso = Return()
        if bool(izq.value)==True and bool(der.value)==True:
            regreso.value=True
        else:
            regreso.value=False
        regreso.tipo=Type.BOOL  
        return regreso 
    def operacion_not(self,izq):
        regreso = Return()
        val=bool(izq.value)
        regreso.value = not(val)
        regreso.tipo=Type.BOOL
        return regreso      
