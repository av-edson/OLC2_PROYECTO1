from clases.abstract.type import Type
from clases.expresiones.accesoStruct import AccesoStruct
from clases.abstract.instruccion import Instruccion

class ModificarStruct(Instruccion):
    def __init__(self,idVar,atributo,expresion, line, column):
        Instruccion.__init__(self,line, column)
        self.identificador = idVar
        self.atributo = atributo
        self.expresion = expresion
    
    def ejecutar(self, enviroment):
        valor = self.expresion.ejecutar(enviroment)
        if valor.tipo == Type.UNDEFINED:
            print("expresion con error en la asignacion del atributo struct")
        else:
            simbolo = enviroment.findVariable(self.identificador)
            if simbolo!=None:
                if simbolo.tipo == Type.STRUCT:
                    if not simbolo.tipoStruct.mutable:
                        print("la estruct no es mutable")
                        return
                    atributos = simbolo.atributos
                    for sim in atributos:
                        if sim.simbolId == self.atributo:
                            if sim.tipo != valor.tipo:
                                if sim.tipo != Type.NULO:
                                    print("No se puede cambiar el tipo de dato del atributo en struct")
                                    return
                                else: sim.tipo = valor.tipo
                            sim.valor = valor.value
                            return
                    print("error, no se encontro atributo del struct")  
                    return
                else:
                    print("identificador no es struct")   
            else:
                print("No se encontro struct")         