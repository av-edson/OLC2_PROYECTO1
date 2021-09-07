from analizadores.lexer import *
from clases.nodo import Nodo
#------------------ SINTACTICO ---------------------------
precedence = (
    ('left','LOR'),
    ('left','LAND'),
    ('left','LNOT'),
    ('left','MAYOR','MENOR','MAYOR_IGUAL','MENOR_IGUAL','IGUAL_IGUAL','DIFERENTE'),
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIV','MODULO'),
    ('left','POTENCIA'),
    ('right','UMENOS'),
    ('left','PARENTESIS_IZQ','PARENTESIS_DER'),
)

def p_init(t) :
    'init            : instrucciones'
    inicial = Nodo("Inicio")
    inicial.ingresarHijo(t[1])
    t[0] = inicial

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    tem = Nodo("Instrucciones")
    tem.ingresarHijo(t[1])
    tem.ingresarHijo(t[2])
    t[0] = tem

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '  
    tem = Nodo("Instrucciones") 
    tem.ingresarHijo(t[1])
    t[0] = tem

def p_instruccion(t):
    '''instruccion  :   declaracion PUNTOCOMA
                    |   imprimir PUNTOCOMA
                    |   declaracion_funcion PUNTOCOMA
                    |   llamada_funcion PUNTOCOMA
                    |   funcion_return  PUNTOCOMA
                    |   sentencia_control
                    |   salto_control PUNTOCOMA
                    |   crear_struct PUNTOCOMA
                    |   modificar_struct PUNTOCOMA'''
    temp = Nodo("Instruccion")
    pt = Nodo(";")
    temp.ingresarHijo(t[1])
    temp.ingresarHijo(pt)
    t[0]=temp

def p_instruccion_error(t):
    '''instruccion  :   error PUNTOCOMA'''
    pass

def p_bloque_instrucciones(t):
    '''bloque_instrucciones :   instrucciones'''
    temp = Nodo("Bloque Instrucciones")
    temp.ingresarHijo(t[1])
    t[0]=temp

def p_declaracion(t):
    '''declaracion   :  ID IGUAL expresion  
                    |   ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipodato'''
    temp = Nodo("Declaracion")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo("="))
    temp.ingresarHijo(t[3])
    if len(t)==7:
        temp.ingresarHijo(Nodo("::"))
        temp.ingresarHijo(t[6])
    t[0]=temp
        
def p_modificar_declaracion(t):
    '''declaracion  :   LOCAL declaracion
                    |   VGLOBAL declaracion
                    |   VGLOBAL ID
                    |   LOCAL ID'''
    temp = Nodo("Declaracion")
    temp.ingresarHijo(Nodo(t[1]))
    if t.slice[2].type=="ID":
        temp.ingresarHijo(Nodo(t[2]))
    else:
        temp.ingresarHijo(t[2])
    t[0]=temp

def p_tipodato(t):
    '''tipodato :   DINT64 
                    |   DFLOAT64 
                    |   DBOOL 
                    |   DSTRING 
                    |   DCHAR ''' 
    temp =  Nodo(t[1])
    t[0]=temp  

def p_expresion(t):
    '''expresion    :   RESTA expresion %prec UMENOS
                    |   expresion_bin
                    |   final_expresion'''
    temp = Nodo("Expresion")
    if len(t)!=3:
        temp.ingresarHijo(t[1])
    else:
        temp.ingresarHijo(Nodo("-"))
        temp.ingresarHijo(t[2])
    t[0]=temp

def p_expresion_logica(t):
    '''expresion    :   LNOT expresion
                    |   expresion LOR expresion
                    |   expresion LAND expresion'''
    temp = Nodo("Expresion Logica")
    if len(t)==3:
        temp.ingresarHijo(Nodo("!"))
        temp.ingresarHijo(t[2])
    else:
        print("aca")
        temp.ingresarHijo(t[1])
        temp.ingresarHijo(Nodo(t[2]))
        temp.ingresarHijo(t[3])
    t[0]=temp

def p_expresion_funcion_nativa(t):
    '''expresion    :   FLOG10 PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FLOG PARENTESIS_IZQ expresion COMA expresion PARENTESIS_DER
                    |   FSIN PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FCOS PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FTAN PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FSQRT PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   UPERCASE PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   LOWERCASE PARENTESIS_IZQ expresion PARENTESIS_DER'''
    temp = Nodo("Funcion Nativa")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(t[3])
    temp.ingresarHijo(Nodo(t[4]))
    if len(t)==7:
        temp.ingresarHijo(t[5])
        temp.ingresarHijo(Nodo(t[6]))
    t[0]=temp

def p_expresion_binaria(t):
    '''expresion_bin    :   expresion SUMA expresion
                            |   expresion RESTA expresion
                            |   expresion MULTI expresion
                            |   expresion DIV expresion
                            |   expresion POTENCIA expresion
                            |   expresion MODULO expresion'''
    temp = Nodo("Expresion Binaria")
    temp.ingresarHijo(t[1])
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(t[3])
    t[0]=temp

def p_expresion_relacional(t):
    '''expresion    :   expresion MAYOR expresion
                    |   expresion MENOR expresion
                    |   expresion MAYOR_IGUAL expresion
                    |   expresion MENOR_IGUAL expresion
                    |   expresion IGUAL_IGUAL expresion
                    |   expresion DIFERENTE expresion'''
    temp = Nodo("Expresion Relacional")
    temp.ingresarHijo(t[1])
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(t[3])
    t[0]=temp

def p_final_expresion(t):
    '''final_expresion  :   llamada_funcion
                        |   PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   ENTERO
                        |   DECIMAL
                        |   CADENA
                        |   CARACTER
                        |   BOOLEANO
                        |   NULO
                        |   ID
                        |   accesoStruct'''
    if len(t) == 4:
        temp = Nodo("agrupacion")
        temp.ingresarHijo(Nodo("("))
        temp.ingresarHijo(t[2])
        temp.ingresarHijo(Nodo(")"))
        t[0]=temp
    elif t.slice[1].type == "llamada_funcion":
        t[0]=t[1]
    elif t.slice[1].type == "accesoStruct":
        t[0]=t[1]
    else:
        temp= Nodo(str(t[1]))
        t[0]=temp

def p_llamada_nativas(t):
    '''llamada_funcion  :   FFLOAT PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   FSTRING PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   FTYPEOF PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   FTRUNC PARENTESIS_IZQ DINT64 COMA expresion PARENTESIS_DER
                        |   FPARSE PARENTESIS_IZQ DINT64 COMA expresion PARENTESIS_DER
                        |   FPARSE PARENTESIS_IZQ DFLOAT64 COMA expresion PARENTESIS_DER'''
    temp=Nodo("LLamada Funcion")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    if len(t)==7:
        temp.ingresarHijo(Nodo(t[3]))
        temp.ingresarHijo(Nodo(t[4]))
        temp.ingresarHijo(t[5])
        temp.ingresarHijo(Nodo(t[6]))
    else:
        temp.ingresarHijo(t[3])
        temp.ingresarHijo(Nodo(t[4]))
    t[0]=temp

def p_imprimir(t):
    '''imprimir :   IMPRIMIR PARENTESIS_IZQ lista_expresiones PARENTESIS_DER
                |   IMPRIMIR_ML PARENTESIS_IZQ lista_expresiones PARENTESIS_DER'''
    temp=Nodo("Imprimir")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(t[3])
    temp.ingresarHijo(Nodo(t[4]))
    t[0]=temp

def p_lista_expresiones(t):
    '''lista_expresiones    :   lista_expresiones COMA expresion
                            | expresion'''  
    if len(t)==4:
        tem = Nodo("Lista Expresiones")
        tem.ingresarHijo(t[1])
        tem.ingresarHijo(Nodo(t[2]))
        tem.ingresarHijo(t[3])
        t[0] = tem
    else:
        t[0]=t[1]

def p_declaracion_funcion(t):
    '''declaracion_funcion  :   FUNCION ID PARENTESIS_IZQ params_function PARENTESIS_DER bloque_instrucciones FIN
                            |   FUNCION ID PARENTESIS_IZQ PARENTESIS_DER bloque_instrucciones FIN''' 
    temp=Nodo("Declaracion")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(Nodo(t[3]))
    if len(t)==8:
        temp.ingresarHijo(t[4])
        temp.ingresarHijo(Nodo(t[5]))
        temp.ingresarHijo(t[6])
        temp.ingresarHijo(Nodo(t[7]))
    else:
        temp.ingresarHijo(Nodo(t[3]))
        temp.ingresarHijo(t[5])
        temp.ingresarHijo(Nodo(t[6]))
    t[0]=temp

def p_params_funcion(t):
    '''params_function  :   params_function COMA ID
                        |   params_function COMA ID DOSPUNTOS DOSPUNTOS tipodato
                        |   ID
                        |   ID DOSPUNTOS DOSPUNTOS tipodato'''
    temp = Nodo("Parametros Funcion")
    if len(t)==2:
        temp.ingresarHijo(Nodo(t[1]))
    elif len(t)==4:
        temp.ingresarHijo(t[1])
        temp.ingresarHijo(Nodo(t[2]))
        temp.ingresarHijo(Nodo(t[3]))
    elif len(t)==5:
        temp.ingresarHijo(Nodo(t[1]))
        temp.ingresarHijo(Nodo("::"))
        temp.ingresarHijo(t[4])
    elif len(t)==7:
        temp.ingresarHijo(t[1])
        temp.ingresarHijo(Nodo(t[2]))
        temp.ingresarHijo(Nodo(t[3]))
        temp.ingresarHijo(Nodo("::"))
        temp.ingresarHijo(t[6])
    t[0]=temp

def p_llamada_funcion(t):
    '''llamada_funcion  :   ID PARENTESIS_IZQ PARENTESIS_DER
                        |   ID PARENTESIS_IZQ lista_expresiones PARENTESIS_DER'''
    temp = Nodo("LLamada Funcion")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    if len(t)==4:
        temp.ingresarHijo(Nodo(t[3]))
    else:
        temp.ingresarHijo(t[3])
        temp.ingresarHijo(Nodo(t[4]))
    t[0]=temp

def p_funcion_return(t):
    '''funcion_return   :   RETURNST expresion
                        |   RETURNST'''
    temp=Nodo(t[1])
    if len(t)==3:
        temp.ingresarHijo(t[2])
    t[0]=temp

def p_sentencias_control(t):
    '''sentencia_control    :   sentencia_if PUNTOCOMA
                            |   sentencia_while PUNTOCOMA
                            |   sentencia_for   PUNTOCOMA'''
    temp = Nodo("Sentencia Control")
    temp.ingresarHijo(t[1])
    temp.ingresarHijo(Nodo(t[2]))
    t[0]=temp

# sin elif, con o sin else
def p_sentencia_if(t):
    '''sentencia_if :   IFST expresion bloque_instrucciones FIN
                    |   IFST expresion bloque_instrucciones sentencia_else FIN
                    |   IFST expresion bloque_instrucciones elif_lista FIN
                    |   IFST expresion bloque_instrucciones elif_lista sentencia_else FIN'''
    temp=Nodo("Instruccion If")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(t[2])
    temp.ingresarHijo(t[3])
    if len(t)==5:
        temp.ingresarHijo(Nodo(t[4]))
    elif len(t)==7:
        temp.ingresarHijo(t[4])
        temp.ingresarHijo(t[5])
        temp.ingresarHijo(Nodo(t[6]))
    else:
        temp.ingresarHijo(t[4])
        temp.ingresarHijo(Nodo(t[5]))
    t[0]=temp

def p_sentencia_else(t):
    '''sentencia_else   :   ELSEST bloque_instrucciones'''
    temp = Nodo("Sentencia Else")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(t[2])
    t[0]=temp

def p_lista_elif(t):
    '''elif_lista   :   elif_lista elif_solo
                    |   elif_solo'''
    if len(t)==2:
        t[0]=t[1]
    else:
        temp=Nodo("Lista Elif")
        temp.ingresarHijo(t[1])
        temp.ingresarHijo(t[2])
        t[0]=temp

def p_solo_elif(t):
    '''elif_solo    :   ELIFST expresion bloque_instrucciones'''
    temp=Nodo("Elif")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(t[2])
    temp.ingresarHijo(t[3])

def p_sentencia_while(t): 
    '''sentencia_while  :   WHILEST expresion bloque_instrucciones FIN'''
    temp=Nodo("Ciclo While")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(t[2])
    temp.ingresarHijo(t[3])
    temp.ingresarHijo(Nodo(t[4]))
    t[0]=temp

def p_salto_control(t):
    '''salto_control :   CONTINUEST
                    |   BREACKST'''
    t[0]=Nodo(t[1])

def p_sentencia_for(t):
    '''sentencia_for    :   FORST ID EIN expresion DOSPUNTOS expresion bloque_instrucciones FIN
                        |   FORST ID EIN expresion bloque_instrucciones FIN'''
    temp=Nodo("Ciclo For")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(Nodo(t[3]))
    temp.ingresarHijo(t[4])
    if len(t)==9:
        temp.ingresarHijo(Nodo(t[5]))
        temp.ingresarHijo(t[6])
        temp.ingresarHijo(t[7])
        temp.ingresarHijo(Nodo(t[7]))
    else:
        temp.ingresarHijo(t[5])
        temp.ingresarHijo(Nodo(t[6]))
    t[0]=temp

def p_crear_struct(t):
    '''crear_struct  :   STRUCT ID contenido_struct FIN
                    |   MUTABLE STRUCT ID contenido_struct FIN'''
    temp = Nodo("Struct")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    if len(t)==5:
        temp.ingresarHijo(t[3])
        temp.ingresarHijo(Nodo(t[4]))
    else:
        temp.ingresarHijo(Nodo(t[3]))
        temp.ingresarHijo(t[4])
        temp.ingresarHijo(Nodo(t[5]))


def p_contenido_struct(t):
    '''contenido_struct :   contenido_struct struct_atributo
                        |   struct_atributo'''
    temp = Nodo("Atributos Struct")
    if len(t)==2:
        temp.ingresarHijo(t[1])
    else:
        temp.ingresarHijo(t[1])
        temp.ingresarHijo(t[2])
    t[0]=temp


def p_atributo_struct(t):
    '''struct_atributo  :   ID PUNTOCOMA
                        |   ID DOSPUNTOS DOSPUNTOS tipodato PUNTOCOMA'''
    temp=Nodo("Atributo Struct")
    temp.ingresarHijo(Nodo(t[1]))
    if len(t)==3:
        temp.ingresarHijo(Nodo(t[2]))
    else:
        temp.ingresarHijo(Nodo("::"))
        temp.ingresarHijo(t[1])
        temp.ingresarHijo(Nodo(t[5]))
    t[0]=temp

def p_acceso_struct(t):
    '''accesoStruct :   ID PUNTO ID'''
    temp = Nodo("Acceso a Struct")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(Nodo(t[3]))
    t[0]=temp

def p_modificar_struct(t):
    '''modificar_struct :   ID PUNTO ID IGUAL expresion'''
    temp=Nodo("Mod. Struct")
    temp.ingresarHijo(Nodo(t[1]))
    temp.ingresarHijo(Nodo(t[2]))
    temp.ingresarHijo(Nodo(t[3]))
    temp.ingresarHijo(Nodo(t[4]))
    temp.ingresarHijo(t[5])
    t[0]=temp

import ply.yacc as yacc
parser2 = yacc.yacc()
