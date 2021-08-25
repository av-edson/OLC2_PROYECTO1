reservadas = {
    'log10' : 'FLOG10',
    'log' : 'FLOG',
    'sin':'FSIN',
    'cos':'FCOS',
    'tan':'FTAN',
    'sqrt':'FSQRT',
    'int64':'DINT64',
    'float64':'DFLOAT64',
    'bool':'DBOOL',
    'char':'DCHAR',
    'string':'DSTRING',
    'nulo':'NULO',
    'true':'BOOLEANO',
    'false':'BOOLEANO',
}

tokens = [
    'COMENTARIOSIMPLE',
    'COMENTARIOMULTIPLE',
    # AGRUPACION
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'CORCHETE_IZQ',
    'CORCHETE_DER',
    'LLAVE_ABRE',
    'LLAVE_CIERRA',
    # ARITMETICAS
    'SUMA',
    'RESTA',
    'MULTI',
    'DIV',
    'POTENCIA',
    'MODULO',
    # RELACIONALES 
    'MAYOR',
    'MENOR',
    'MAYOR_IGUAL',
    'MENOR_IGUAL',
    'IGUAL_IGUAL',
    'DIFERENTE',
    # LOGICAS
    'LOR' ,
    'LAND',
    'LNOT',
    # DATOS
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'ID',
    'CARACTER',
    # otros
    'IGUAL',
    'PUNTOCOMA'
] + list(reservadas.values())

# Tokens

t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_LLAVE_ABRE = r'\{'
t_LLAVE_CIERRA = r'\}'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIV = r'\/'
t_POTENCIA = r'\^'
t_MODULO = r'\%'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_IGUAL_IGUAL = r'=='
t_DIFERENTE = r'!='
t_LOR = r'\|\|' 
t_LAND = r'&&'
t_LNOT = r'!'
t_IGUAL = r'\='
t_PUNTOCOMA = r'\;'


#decimal
def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t
# entero
def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t
# booleano
# cadena
def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] 
    return t 
    # CARACTER
def t_CARACTER(t):
    r'\'.*?\''
    t.value = t.value[1:-1] 
    return t 
#identificador
def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'ID') 
     return t
# comentario multi linea
def t_COMENTARIOMULTIPLE(t):
    r'\#\=((.|\n)*)?\=\#'
    t.lexer.lineno += t.value.count("\n")
# comentario simple
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1
# ignorados
t_ignore = " \t"
#salto de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
# fin de documento
def t_eof(t):
    return None
# manejador de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()
