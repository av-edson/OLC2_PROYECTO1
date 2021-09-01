from clases.tree.funciones.funcion import Funcion
from clases.expresiones.exprBinaria import *
from clases.expresiones.expresionLiteral import ExpresionLiteral, Identificador
from clases.expresiones.exprNativa import *
from clases.expresiones.exprRelacional import *
from analizadores.lexer import *
from clases.tree.imprimir import *
from clases.tree.funcionesNativas import *
from clases.tree.declaracion import *
from clases.tree.bloqueInstrucciones import BloqueInstrucciones
from clases.tree.funciones.parametro import *
from clases.tree.funciones.returnST import ReturnFunc
from clases.abstract.type import Type
from clases.tree.funciones.llamadaFunc import LLamadaFuncion
from clases.tree.control.sentenciaELIF import SentenciaELIF
from clases.tree.control.sentenciaIF import SentenciaIF
from clases.tree.ciclos.cicloWhile import CicloWhile
from clases.tree.ciclos.cicloFor import CicloFor
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
    ('right','UMENOS'),
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
                    |   imprimir PUNTOCOMA
                    |   declaracion_funcion PUNTOCOMA
                    |   llamada_funcion PUNTOCOMA
                    |   funcion_return  PUNTOCOMA
                    |   sentencia_control
                    |   salto_control PUNTOCOMA'''
    t[0]=t[1]

def p_bloque_instrucciones(t):
    '''bloque_instrucciones :   instrucciones'''
    t[0] = BloqueInstrucciones(t[1],t.lineno(1),t.lexpos(0))
def p_declaracion(t):
    '''declaracion   :  ID IGUAL expresion  
                    |   ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipodato'''
    if len(t)==7:
        t[0]=Asignacion(t[1],t[3],t[6],3,t.lineno(1),t.lexpos(1))
    else:
        t[0]=Asignacion(t[1],t[3],None,3,t.lineno(1),t.lexpos(1))
def p_modificar_declaracion(t):
    '''declaracion  :   LOCAL declaracion
                    |   VGLOBAL declaracion
                    |   VGLOBAL ID
                    |   LOCAL ID'''
    if t.slice[1].type=="LOCAL":
        if t.slice[2].type=="ID":
            t[0] = DeclaracionGloLoc(t[2],2,t.lineno(1),t.lexpos(1))
        else:
            t[2].modificar_alcance(2)
            t[0]=t[2]
    else:
        if t.slice[2].type=="ID":
            t[0] = DeclaracionGloLoc(t[2],1,t.lineno(1),t.lexpos(1))
        else:
            t[2].modificar_alcance(1)
            t[0]=t[2]

def p_tipodato(t):
    '''tipodato :   DINT64 
                    |   DFLOAT64 
                    |   DBOOL 
                    |   DSTRING 
                    |   DCHAR '''    
    if t.slice[1].type=='DINT64':
        t[0]=Type.INT
    elif t.slice[1].type=='DFLOAT64':
        t[0]=Type.FLOAT
    elif t.slice[1].type=='DBOOL':
        t[0]=Type.BOOL
    elif t.slice[1].type=='DSTRING':
        t[0]=Type.STRING
    elif t.slice[1].type=='DCHAR':
        t[0]=Type.CHAR
def p_expresion(t):
    '''expresion    :   RESTA expresion %prec UMENOS
                    |   expresion_bin
                    |   final_expresion'''
    if t.slice[1].type=="RESTA":
        t[0]=ExpresionBinaria(OperacionesBinarias.MULTIPLICACION,ExpresionLiteral(Type.INT,-1,t.lineno(1), t.lexpos(0)),t[2],t.lineno(1), t.lexpos(0))
    else:
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
                    |   FSQRT PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   UPERCASE PARENTESIS_IZQ expresion PARENTESIS_DER
                    |   LOWERCASE PARENTESIS_IZQ expresion PARENTESIS_DER'''
    if t.slice[1].type=="FLOG10":
        t[0]=ExpresionNativa(OpeNativas.LOGCOMUN,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="FLOG":
        t[0]=ExpresionNativa(OpeNativas.LOGBASE,t[5],t.lineno(1),t.lexpos(1),t[3])
    elif t.slice[1].type=="FSIN":
        t[0]=ExpresionNativa(OpeNativas.SIN,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="FCOS":
        t[0]=ExpresionNativa(OpeNativas.COS,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="FTAN":
        t[0]=ExpresionNativa(OpeNativas.TAN,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="FSQRT":
        t[0]=ExpresionNativa(OpeNativas.RAIZ,t[3],t.lineno(1),t.lexpos(1))
    elif t.slice[1].type=="UPERCASE":
        t[0]=ExpresionNativa(OpeNativas.UPER,t[3],t.lineno(1),t.lexpos(1))
    else:
        t[0]=ExpresionNativa(OpeNativas.LOWER,t[3],t.lineno(1),t.lexpos(1))

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
                        |   NULO
                        |   ID'''
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
            if str(t[1])=="true":
                t[0] = ExpresionLiteral(Type.BOOL,True,t.lineno(1),t.lexpos(0))
            else:
                t[0] = ExpresionLiteral(Type.BOOL,False,t.lineno(1),t.lexpos(0))
        elif t.slice[1].type=="NULO":
            t[0] = ExpresionLiteral(Type.NULO,str(t[1]),t.lineno(1),t.lexpos(0))
        elif t.slice[1].type=="ID":
            t[0] = Identificador(str(t[1]),t.lineno(1),t.lexpos(0))
        else: # para la llamada de funcion
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
    else:
        print('wache la 208 de gramar')

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

def p_declaracion_funcion(t):
    '''declaracion_funcion  :   FUNCION ID PARENTESIS_IZQ params_function PARENTESIS_DER bloque_instrucciones FIN
                            |   FUNCION ID PARENTESIS_IZQ PARENTESIS_DER bloque_instrucciones FIN''' 
    if len(t)==7:
        t[0] = Funcion(t[2],t[5],[],t.lineno(1), t.lexpos(1))
    else:
        t[0] = Funcion(t[2],t[6],t[4],t.lineno(1), t.lexpos(1))

def p_params_funcion(t):
    '''params_function  :   params_function COMA ID
                        |   params_function COMA ID DOSPUNTOS DOSPUNTOS tipodato
                        |   ID
                        |   ID DOSPUNTOS DOSPUNTOS tipodato'''
    if len(t)==2:
        t[0] = [Parametro(t[1],None, t.lineno(1), t.lexpos(1))]
    elif len(t)==4:
        t[1].append(Parametro(t[3],None, t.lineno(3), t.lexpos(3)))
        t[0] = t[1]
    elif len(t)==5:
        t[0] = [Parametro(t[1],t[4], t.lineno(1), t.lexpos(1))]
    else:
        t[1].append(Parametro(t[3],t[6], t.lineno(3), t.lexpos(3)))
        t[0] = t[1]

def p_llamada_funcion(t):
    '''llamada_funcion  :   ID PARENTESIS_IZQ PARENTESIS_DER
                        |   ID PARENTESIS_IZQ lista_expresiones PARENTESIS_DER'''
    if len(t)==4:
        t[0] = LLamadaFuncion(t[1],[],t.lineno(1), t.lexpos(1))
    else:
        t[0] = LLamadaFuncion(t[1],t[3],t.lineno(1), t.lexpos(1)) 
def p_funcion_return(t):
    '''funcion_return   :   RETURNST expresion
                        |   RETURNST'''
    if len(t)==2:
        t[0]=ReturnFunc(None,t.lineno(1), t.lexpos(1))
    else:
        t[0]=ReturnFunc(t[2],t.lineno(1), t.lexpos(1))

def p_sentencias_control(t):
    '''sentencia_control    :   sentencia_if PUNTOCOMA
                            |   sentencia_while PUNTOCOMA
                            |   sentencia_for   PUNTOCOMA'''
    t[0]=t[1]

# sin elif, con o sin else
def p_sentencia_if(t):
    '''sentencia_if :   IFST expresion bloque_instrucciones FIN
                    |   IFST expresion bloque_instrucciones sentencia_else FIN
                    |   IFST expresion bloque_instrucciones elif_lista FIN
                    |   IFST expresion bloque_instrucciones elif_lista sentencia_else FIN'''
    if len(t)==5:
        t[0]=SentenciaIF(t[2],t[3],t.lineno(1), t.lexpos(1))
    elif len(t)==6:
        t[0]=SentenciaIF(t[2],t[3],t.lineno(1), t.lexpos(1),None,t[4])
    elif len(t)==7:
        t[0]=SentenciaIF(t[2],t[3],t.lineno(1), t.lexpos(1),t[4],t[5])

def p_sentencia_else(t):
    '''sentencia_else   :   ELSEST bloque_instrucciones'''
    t[0]=t[2]

def p_lista_elif(t):
    '''elif_lista   :   elif_lista elif_solo
                    |   elif_solo'''
    if len(t)==3:
        t[1].append(t[2])
        t[0]=t[1]
    else:
        t[0]=[t[1]]
def p_solo_elif(t):
    '''elif_solo    :   ELIFST expresion bloque_instrucciones'''
    t[0]=SentenciaELIF(t[2],t[3],t.lineno(1), t.lexpos(1))

def p_sentencia_while(t):
    '''sentencia_while  :   WHILEST expresion bloque_instrucciones FIN'''
    t[0] = CicloWhile(t[2],t[3],t.lineno(1), t.lexpos(1))

def p_salto_control(t):
    '''salto_control :   CONTINUEST
                    |   BREACKST'''
    if t.slice[1].type=="CONTINUEST":
            t[0] = ExpresionLiteral(Type.CONTINUEST,str(t[1]),t.lineno(1),t.lexpos(0))
    elif t.slice[1].type=="BREACKST":
        t[0] = ExpresionLiteral(Type.BREACKST,str(t[1]),t.lineno(1),t.lexpos(0))

def p_sentencia_for(t):
    '''sentencia_for    :   FORST ID EIN expresion DOSPUNTOS expresion bloque_instrucciones FIN
                        |   FORST ID EIN expresion bloque_instrucciones FIN'''
    if len(t)==9:
        t[0]=CicloFor(t[2],t[4],t[7],t.lineno(1), t.lexpos(1),t[6])
    else:
        t[0]=CicloFor(t[2],t[4],t[5],t.lineno(1), t.lexpos(1))

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)
    print(t)

import ply.yacc as yacc
parser = yacc.yacc()
