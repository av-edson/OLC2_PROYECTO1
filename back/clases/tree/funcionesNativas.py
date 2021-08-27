from clases.enviroment.enviroment import Enviroment
from clases.abstract.expresion import Expresion
from clases.abstract.type import *
from math import floor
class FSimple(Expresion):
    # tipo de funcines en esta
    # 1 = float
    # 2 = string
    # 3 = typeof
    # 4 = trunc
    # 5 = parseInt
    # 6 = parseFloat

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
            print('error en una funcion '+str(self.line))
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

        
