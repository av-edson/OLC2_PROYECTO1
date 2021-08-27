from clases.expresiones.exprBinaria import *
from clases.expresiones.expresionLiteral import ExpresionLiteral
from clases.expresiones.exprNativa import *
from clases.expresiones.exprRelacional import *
from analizadores.lexer import *
from clases.tree.imprimir import *
from clases.tree.funcionesNativas import *
from clases.abstract.type import Type
from clases.expresiones import *
#------------------ SINTACTICO ---------------------------
precedence = (
    ('left','LOR'),
    ('left','LAND'),
    ('left','LNOT'),
    ('left','MAYOR','MENOR','MAYOR_IGUAL','MENOR_IGUAL','IGUAL_IGUAL','DIFERENTE'),
    ('left','SUMA','RESTA'),
    ('left','MULTI','DIV','MODULO'),
    ('left','POTENCIA'),
    #('right','UMENOS'),
    ('left','PARENTESIS_IZQ','PARENTESIS_DER'),
)
def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]
def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]
def p_instruccion(t):
    '''instruccion  :   declaracion PUNTOCOMA
                    |   asignacion  
                    |   imprimir PUNTOCOMA
                    |   expresion PUNTOCOMA'''
    t[0]=t[1]
def p_declaracion(t):
    '''declaracion :    DINT64 ID
                    |   DFLOAT64 ID
                    |   DBOOL ID
                    |   DSTRING ID
                    |   DCHAR ID'''
def p_asignacion(t):
    '''asignacion   :  ID IGUAL expresion PUNTOCOMA 
                    |   declaracion IGUAL expresion PUNTOCOMA'''
def p_expresion(t):
    '''expresion    :   expresion_bin
                    |   final_expresion'''
    t[0]=t[1]
def p_expresion_logica(t):
    '''expresion    :   LNOT expresion
                    |   expresion LOR expresion
                    |   expresion LAND expresion'''
    if t.slice[2].type=="LOR":
        t[0]=ExpresionLogica(t[1],t[3],OpeLogica.OR,t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="LAND":
        t[0]=ExpresionLogica(t[1],t[3],OpeLogica.AND,t.lineno(2),t.lexpos(2))
    elif t.slice[1].type=="LNOT":
        t[0]=ExpresionLogica(t[2],None,OpeLogica.NOT,t.lineno(1),t.lexpos(1))
def p_expresion_funcion_nativa(t):
    '''expresion    :   FLOG10 PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FLOG PARENTESIS_IZQ expresion COMA expresion PARENTESIS_DER
                    |   FSIN PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FCOS PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FTAN PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   FSQRT PARENTESIS_IZQ expresion PARENTESIS_DER'''
    if t.slice[1].type=="FLOG10":
        t[0]=ExpresionNativa(OpeNativas.LOGCOMUN,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="FLOG":
        t[0]=ExpresionNativa(OpeNativas.LOGBASE,t[3],t.lineno(1),t.lexpos(1),t[5])
    elif t.slice[1].type=="FSIN":
        t[0]=ExpresionNativa(OpeNativas.SIN,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="FCOS":
        t[0]=ExpresionNativa(OpeNativas.COS,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="FTAN":
        t[0]=ExpresionNativa(OpeNativas.TAN,t[3],t.lineno(1),t.lexpos(1))
    else:
        t[0]=ExpresionNativa(OpeNativas.RAIZ,t[3],t.lineno(1),t.lexpos(1))

def p_expresion_binaria(t):
    '''expresion_bin    :   expresion SUMA expresion
                            |   expresion RESTA expresion
                            |   expresion MULTI expresion
                            |   expresion DIV expresion
                            |   expresion POTENCIA expresion
                            |   expresion MODULO expresion'''
    if t.slice[2].type=="SUMA":
        t[0]=ExpresionBinaria(OperacionesBinarias.SUMA,t[1],t[3],t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="RESTA":
        t[0]=ExpresionBinaria(OperacionesBinarias.RESTA,t[1],t[3],t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="MULTI":
        t[0]=ExpresionBinaria(OperacionesBinarias.MULTIPLICACION,t[1],t[3],t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="DIV":
        t[0]=ExpresionBinaria(OperacionesBinarias.DIVISION,t[1],t[3],t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="POTENCIA":
        t[0]=ExpresionBinaria(OperacionesBinarias.POTENCIA,t[1],t[3],t.lineno(2),t.lexpos(2))
    else:
        t[0]=ExpresionBinaria(OperacionesBinarias.MODULO,t[1],t[3],t.lineno(2),t.lexpos(2))

def p_expresion_relacional(t):
    '''expresion    :   expresion MAYOR expresion
                    |   expresion MENOR expresion
                    |   expresion MAYOR_IGUAL expresion
                    |   expresion MENOR_IGUAL expresion
                    |   expresion IGUAL_IGUAL expresion
                    |   expresion DIFERENTE expresion'''
    if t.slice[2].type=="MAYOR":
        t[0]=ExpresionRelacional(t[1],t[3],OpRelacional.MAYORQUE,t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="MENOR":
        t[0]=ExpresionRelacional(t[1],t[3],OpRelacional.MENORQUE,t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="MAYOR_IGUAL":
        t[0]=ExpresionRelacional(t[1],t[3],OpRelacional.MAYORIGUAL,t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="MENOR_IGUAL":
        t[0]=ExpresionRelacional(t[1],t[3],OpRelacional.MENORIGUAL,t.lineno(2),t.lexpos(2))
    elif t.slice[2].type=="IGUAL_IGUAL":
        t[0]=ExpresionRelacional(t[1],t[3],OpRelacional.IGUALIGUAL,t.lineno(2),t.lexpos(2))
    else:
        t[0]=ExpresionRelacional(t[1],t[3],OpRelacional.DIFERENTE,t.lineno(2),t.lexpos(2))

def p_final_expresion(t):
    '''final_expresion  :   llamada_funcion
                        |   PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   ENTERO
                        |   DECIMAL
                        |   CADENA
                        |   CARACTER
                        |   BOOLEANO
                        |   NULO'''
    if len(t) == 2:
        if t.slice[1].type == "ENTERO":
            t[0] = ExpresionLiteral(Type.INT,int(t[1]),t.lineno(1),t.lexpos(0))
        elif t.slice[1].type == "DECIMAL":
            t[0] = ExpresionLiteral(Type.FLOAT,float(t[1]),t.lineno(1),t.lexpos(0))
        elif t.slice[1].type=="CADENA":
            t[0] = ExpresionLiteral(Type.STRING,str(t[1]),t.lineno(1),t.lexpos(0))
        elif t.slice[1].type=="CARACTER":
            t[0] = ExpresionLiteral(Type.CHAR,str(t[1]),t.lineno(1),t.lexpos(0))
        elif t.slice[1].type=="BOOLEANO":
            t[0] = ExpresionLiteral(Type.BOOL,str(t[1]),t.lineno(1),t.lexpos(0))
        elif t.slice[1].type=="NULO":
            t[0] = ExpresionLiteral(Type.NULO,str(t[1]),t.lineno(1),t.lexpos(0))
        else:
            t[0]=t[1]
    else:
        t[0] = t[2]
def p_llamada_nativas(t):
    '''llamada_funcion  :   FFLOAT PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   DSTRING PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   FTYPEOF PARENTESIS_IZQ expresion PARENTESIS_DER
                        |   FTRUNC PARENTESIS_IZQ DINT64 COMA expresion PARENTESIS_DER
                        |   FPARSE PARENTESIS_IZQ DINT64 COMA expresion PARENTESIS_DER
                        |   FPARSE PARENTESIS_IZQ DFLOAT64 COMA expresion PARENTESIS_DER'''
    if t.slice[1].type=='FFLOAT':
        t[0]=FSimple(t[3],1,t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=='DSTRING':
        t[0]=FSimple(t[3],2,t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=='FTYPEOF':
        t[0]=FSimple(t[3],3,t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=='FTRUNC':
        t[0]=FSimple(t[5],4,t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=='FPARSE' and t.slice[3].type=='DINT64':
        t[0]=FSimple(t[5],5,t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=='FPARSE' and t.slice[3].type=='DFLOAT64':
        t[0]=FSimple(t[5],6,t.lineno(1),t.lexpos(1))

def p_imprimir(t):
    '''imprimir :   IMPRIMIR PARENTESIS_IZQ lista_expresiones PARENTESIS_DER
                |   IMPRIMIR_ML PARENTESIS_IZQ lista_expresiones PARENTESIS_DER''' 
    if t.slice[1].type=="IMPRIMIR":
        t[0]=Imprimir(t[3],TipoImpresion.PRINT,t.lineno(1),t.lexpos(1))
    else:
        t[0]=Imprimir(t[3],TipoImpresion.PRINTLN,t.lineno(1),t.lexpos(1))

def p_lista_expresiones(t):
    '''lista_expresiones    :   lista_expresiones COMA expresion'''  
    t[1].append(t[3])
    t[0] = t[1]
def p_lista_expresiones_expresion(t):
    '''lista_expresiones    :   expresion'''
    t[0] = [t[1]]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    print(t)

import ply.yacc as yacc
parser = yacc.yacc()
