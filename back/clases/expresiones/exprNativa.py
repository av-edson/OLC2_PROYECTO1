from clases.abstract.expresion import Expresion
#from clases.enviroment.enviroment import Enviroment
from clases.abstract.type import *
from enum import Enum
import math

class OpeNativas(Enum):
    LOGCOMUN=0
    LOGBASE=1
    SIN=2
    COS=3
    TAN=4
    RAIZ=5
    UPER=6
    LOWER=7

class ExpresionNativa(Expresion):
    def __init__(self,tipo,content, line, column,base=None):
        Expresion.__init__(self,line, column)
        self.tipo=tipo
        self.content=content
        self.base=base
    
    def ejecutar(self,enviroment):
        expre = self.content.ejecutar(enviroment)
        if self.base != None:
            base = self.base.ejecutar(enviroment)
        try:
            if self.tipo==OpeNativas.LOGCOMUN:
                return  self.log_comun(expre)
            elif self.tipo==OpeNativas.LOGBASE:
                return self.log_base(expre,base)
            elif self.tipo==OpeNativas.SIN:
                return self.seno(expre)
            elif self.tipo==OpeNativas.COS:
                return self.coseno(expre)
            elif self.tipo==OpeNativas.TAN:
                return self.tangente(expre)
            elif self.tipo==OpeNativas.RAIZ:
                return self.raiz(expre)
            elif self.tipo==OpeNativas.UPER:
                return self.uper(expre)
            else:
                return self.lower(expre)
        except:
            print('----Error al ejecutar funcion nativa')
            return Return()
    
    def log_comun(self,expre):
        if not(expre.tipo==Type.INT or expre.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        valorExpre = expre.value
        regreso = Return()
        try:
            regreso.value = math.log10(float(valorExpre))
            regreso.tipo=Type.FLOAT
        except:
            return regreso
        return regreso
    def log_base(self,expre,base):
        if not(expre.tipo==Type.INT or expre.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        if not(base.tipo==Type.INT or base.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        valorExpre = expre.value
        regreso = Return()
        try:
            regreso.value = math.log(float(valorExpre),base.value)
        except:
            return regreso
        regreso.tipo=Type.FLOAT
        return regreso
    def seno(self,expre):
        if not(expre.tipo==Type.INT or expre.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        valorExpre = expre.value
        regreso = Return()
        try:
            regreso.value = math.sin(float(valorExpre))
        except:
            return regreso
        regreso.tipo=Type.FLOAT
        return regreso
    def coseno(self,expre):
        if not(expre.tipo==Type.INT or expre.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        valorExpre = expre.value
        regreso = Return()
        try:
            regreso.value = math.cos(float(valorExpre))
        except:
            return regreso
        regreso.tipo=Type.FLOAT
        return regreso
    def tangente(self,expre):
        if not(expre.tipo==Type.INT or expre.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        valorExpre = expre.value
        regreso = Return()
        try:
            regreso.value = math.tan(float(valorExpre))
        except:
            return regreso
        regreso.tipo=Type.FLOAT
        return regreso
    def raiz(self,expre):
        if not(expre.tipo==Type.INT or expre.tipo==Type.FLOAT):
            return Return(0,Type.UNDEFINED)
        valorExpre = expre.value
        regreso = Return()
        try:
            regreso.value = math.sqrt(float(valorExpre))
        except:
            return regreso
        regreso.tipo=Type.FLOAT
        return regreso
    def uper(self,expre:Return):
        if not(expre.tipo==Type.STRING or expre.tipo==Type.CHAR):
            print('upper solo de cadenas o caracteres')
            return Return()
        nuevoValor = str(expre.value).upper()
        return Return(nuevoValor,Type.STRING)
    def lower(self,expre):
        if not(expre.tipo==Type.STRING or expre.tipo==Type.CHAR):
            print('lower solo de cadenas o caracteres')
            return Return()
        nuevoValor = str(expre.value).lower()
        return Return(nuevoValor,Type.STRING)