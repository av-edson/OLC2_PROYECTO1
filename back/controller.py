from analizadores.gramatica import parser
from clases.enviroment.enviroment import *

def analizarEntrada(contenido):
    print(contenido)

f = open('entrada.txt')
contenido = f.read()
ast = parser.parse(contenido)
gl = Enviroment(None)
try:
    for instruccion in ast:
        #instruccion.ejecutar(gl)
        s=instruccion.ejecutar(gl)
        print(str(s.tipo)+" --- "+str(s.value))
except:
    print("Error al ejecutar instrucciones")




f.close()