from clases.nodo import Nodo
from clases.error import Error
from analizadores.gramatica import parser
#from analizadores.gramaticaArbol import parser2
from clases.enviroment.enviroment import Enviroment
from analizadores.lexer import errores

class Regreso:
    def __init__(self,consola,arbol,er):
        self.consola = consola
        self.ast = arbol
        self.errores =er

def objToJson(obj):
    lista = []
    for er in obj:
        dic = {}
        dic["desc"]=er.desc
        dic["lin"]=er.lin
        dic["col"]=er.col
        dic["fecha"]=er.fecha
        lista.append(dic)
    return lista

def analizarEntrada(contenido=None):
    #arbol:Nodo= parser2.parse(contenido)
    global errores
    errores.clear()
    ast = parser.parse(contenido)
    gl = Enviroment(None,"Global")
    try:
        for instruccion in ast:
            if instruccion != None:
                d=instruccion.ejecutar(gl)
    except:
        print("Error al ejecutar instrucciones")
    listJson = objToJson(errores)
    #return Regreso(gl.consola,arbol.getGrafico(),listJson)

f = open('entrada.txt',encoding="UTF-8")
contenido = f.read()
ast = parser.parse(contenido)
gl = Enviroment(None,"Global")
#arbol:Nodo = parser2.parse(contenido)
try:
    for instruccion in ast:
        if instruccion != None:
            d=instruccion.ejecutar(gl)
        x = 4
except:
    print("Error al ejecutar instrucciones")
f.close()
print(gl.consola)
#print(arbol.getGrafico())
#for var in gl.variables:
    #    aux:Simbolo = gl.findVariable(var)
    #    print(str(aux.simbolId)+" "+str(aux.valor)+" "+str(aux.tipo))
        #s=instruccion.ejecutar(gl)
        #print(str(s.tipo)+" --- "+str(s.value))

#s=analizarEntrada("~s=8;\nprint(\"hola joto\");")
#print(s.errores)

#print("---------------")
#for er in errores:
#    print(er.desc+" -> "+er.lin)