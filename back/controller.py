from clases.nodo import Nodo
from clases.error import Error
from analizadores.gramatica import compilar
from analizadores.gramaticaArbol import parser2
from clases.enviroment.enviroment import Enviroment
from analizadores.lexer import errores,listaStructs

class Regreso:
    def __init__(self,comp,consola,arbol,er,table):
        self.compilacion=comp
        self.consola = consola
        self.ast = arbol
        self.errores =er
        self.tabla=table

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

def tablaToJson(obj):
    lista = []
    for var in obj:
        var = obj[var]
        dic = {}
        dic["ambito"]=var.ambito
        dic["tipo"]=var.tipo
        dic["valor"]=var.valor
        dic["nombre"]=var.nombre
        dic["fila"]=var.fila
        dic["columna"]=var.columna
        lista.append(dic)
    return lista

def analizarEntrada(contenido=None):
    try:
        arbol:Nodo= parser2.parse(contenido)
        global errores,listaStructs
        errores.clear()
        listaStructs.clear()
        listaStructs.clear()
        ast = compilar(contenido)
        gl = Enviroment(None,"Global")
        try:
            for instruccion in ast:
                if instruccion != None:
                    d=instruccion.ejecutar(gl)
            gl.addVariable_TablaSimbolos()
        except Exception as e:
            print("Error al ejecutar instrucciones")
            return Regreso(False,str(e),"","","")
        listJson = objToJson(errores)
        tablaSimbolos = tablaToJson(gl.listaSimbolos)
        abr = arbol.getGrafico()
        return Regreso(True,gl.consola,abr,listJson,tablaSimbolos)
    except Exception as e:
        return Regreso(False,str(e),"","","")
#f = open('entrada.txt',encoding="UTF-8")
#contenido = f.read()
#ast = parser.parse(contenido)
#gl = Enviroment(None,"Global")
#arbol:Nodo = parser2.parse(contenido)

#try:
#    for instruccion in ast:
#        if instruccion != None:
#            d=instruccion.ejecutar(gl)
#        x = 4
#    gl.addVariable_TablaSimbolos()
#except:
#    print("Error al ejecutar instrucciones")
#f.close()
#s=analizarEntrada(contenido)
#s=3
#s=analizarEntrada(contenido)
#s=2
#print(gl.consola)
#for var in gl.listaSimbolos:
#    var = gl.listaSimbolos[var]
#    print(var.ambito+" - "+var.nombre+" - "+var.tipo+" - "+var.valor)
#print(arbol.getGrafico())
#f = open ('pruebas\salida.txt','w')
#f.write(arbol.getGrafico())
#f.close()
#for var in gl.variables:
    #    aux:Simbolo = gl.findVariable(var)
    #    print(str(aux.simbolId)+" "+str(aux.valor)+" "+str(aux.tipo))
        #s=instruccion.ejecutar(gl)
        #print(str(s.tipo)+" --- "+str(s.value))

#print(s.errores)
