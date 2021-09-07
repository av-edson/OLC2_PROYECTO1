import time
from clases.error import Error
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
        gl = enviroment.getGlobal()
        try:
            valor = self.expresion.ejecutar(enviroment)
            if valor.tipo == Type.UNDEFINED:
                print("expresion con error en la asignacion del atributo struct")
            else:
                simbolo = enviroment.findVariable(self.identificador)
                if simbolo!=None:
                    if simbolo.tipo == Type.STRUCT:
                        if not simbolo.tipoStruct.mutable:
                            print("la estruct no es mutable")
                            gl.listaErrores.append(Error("la estruct no es mutable "+str(self.identificador),self.line,self.column,time.strftime("%c")))
                            return
                        atributos = simbolo.atributos
                        for sim in atributos:
                            if sim.simbolId == self.atributo:
                                if sim.tipo != valor.tipo:
                                    if sim.tipo != Type.NULO:
                                        print("No se puede cambiar el tipo de dato del atributo en struct")
                                        gl.listaErrores.append(Error("No se puede cambiar el tipo de dato del atributo en struct "+str(self.identificador),self.line,self.column,time.strftime("%c")))
                                        return
                                    else: sim.tipo = valor.tipo
                                sim.valor = valor.value
                                return
                        print("error, no se encontro atributo del struct")  
                        gl.listaErrores.append(Error("Error, no se encontro atributo del struct "+str(self.identificador),self.line,self.column,time.strftime("%c")))
                        return
                    else:
                        print("identificador no es struct")   
                        gl.listaErrores.append(Error("Iidentificador no es struct"+str(self.identificador),self.line,self.column,time.strftime("%c")))
                else:
                    print("No se encontro struct")  
                    gl.listaErrores.append(Error("No se encontro struct"+str(self.identificador),self.line,self.column,time.strftime("%c")))       
        except:
            gl.listaErrores.append(Error("Error inesperado al modificar la struct "+str(self.identificador),self.line,self.column,time.strftime("%c")))