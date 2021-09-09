from clases.expresiones.expresionLiteral import ExpresionLiteral
from clases.abstract.instruccion import Instruccion
import time
from clases.error import Error
from clases.enviroment.enviroment import Enviroment
from clases.abstract.expresion import Expresion
from clases.abstract.type import *
from math import floor
class FSimple(Expresion):
    '''
    # tipo de funcines en esta\n
    # 1 = float\n
    # 2 = string\n
    # 3 = typeof\n
    # 4 = trunc\n
    # 5 = parseInt\n
    # 6 = parseFloat\n
    '''

    def __init__(self,expr,tipo, line, column):
        self.line=line
        self.column=column
        self.tipo=tipo
        self.expresion=expr
    
    def ejecutar(self, enviroment):
        val = self.expresion.ejecutar(enviroment)
        try:
            if self.tipo==1:
                return self.f_float(val)
            elif self.tipo==2:
                return self.f_string(val)
            elif self.tipo==3:
                return self.f_typeof(val)
            elif self.tipo==4:
                return self.f_trunc(val)
            elif self.tipo==5:
                return self.f_parse(val,1)
            elif self.tipo==6:
                return self.f_parse(val,2)
            else:
                return Return()
        except:
            gl:Enviroment = enviroment.getGlobal()
            gl.listaErrores.append(Error("error en una funcion nativa",self.line,self.column,time.strftime("%c")))
            print('error en una funcion nativa '+str(self.line))
            return Return()
    
    def f_float(self,num):
        if not(num.tipo==Type.INT or num.tipo==Type.FLOAT):
            return Return()
        return Return(float(num.value),Type.FLOAT)

    def f_string(self,st):
        return Return(str(st.value),Type.STRING)
    def f_typeof(self,obj):
        return Return(obj.tipo.name,obj.tipo)
    def f_trunc(self,num):
        if num.tipo!=Type.FLOAT:
            return Return()
        return Return(floor(float(num.value)),Type.INT)
    def f_parse(self,valor,tipo):
        if valor.tipo!=Type.STRING:
            return Return()
        if tipo==1:
            num = int(valor.value)
            return Return(num,Type.INT)
        else:
            num = float(valor.value)
            return Return(num,Type.FLOAT)

class Fpush(Instruccion):
    def __init__(self,listaExpresiones, line, column):
        Instruccion.__init__(self,line, column) 
        self.identificador = ""
        self.expresiones = listaExpresiones

    def ejecutar(self, enviroment):
        try:
            gl = enviroment.getGlobal()
            ide = self.expresiones[0].ejecutar(enviroment)
            expresion = self.expresiones[1].ejecutar(enviroment)
            if len(self.expresiones)>2:
                print("Mas de 2 parametros para la funcion push")     
                gl.listaErrores.append(Error("Mas de 2 parametros para la funcion push",self.line,self.column,time.strftime("%c"))) 
                return

            if ide.tipo!=Type.ARRAY:
                print("Funcion solo admitida para arreglos")     
                gl.listaErrores.append(Error("Funcion solo admitida para arreglos",self.line,self.column,time.strftime("%c"))) 
                return

            if expresion.tipo==Type.BREACKST or expresion.tipo==Type.CONTINUEST or expresion.tipo==Type.RETURNST or expresion.tipo==Type.UNDEFINED:
                print("Expresion para pushear no admitida o tiene error")
                gl.listaErrores.append(Error("Expresion para pushear no admitida o tiene error",self.line,self.column,time.strftime("%c"))) 
                return
            nuevo = ExpresionLiteral(expresion.tipo,expresion.value,self.line,self.column)
            ide.value.append(nuevo)
        except:
            print("error inesperado en funcion push")

           
