from analizadores.gramatica import parser
from clases.enviroment.enviroment import *
from clases.enviroment.simbolo import Simbolo

def analizarEntrada(contenido):
    print(contenido)

f = open('entrada.txt',encoding="UTF-8")
contenido = f.read()
ast = parser.parse(contenido)
gl = Enviroment(None,"Global")
try:
    for instruccion in ast:
        d=instruccion.ejecutar(gl)
        x = 4
    #for var in gl.variables:
    #    aux:Simbolo = gl.findVariable(var)
    #    print(str(aux.simbolId)+" "+str(aux.valor)+" "+str(aux.tipo))
        #s=instruccion.ejecutar(gl)
        #print(str(s.tipo)+" --- "+str(s.value))
except:
    print("Error al ejecutar instrucciones")

# !!!!!NO PUEDE TERMINAR CON UN COMENTARIO!!!!!!!!



f.close()