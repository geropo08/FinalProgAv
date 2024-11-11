import ply.lex as lex
import ply.yacc as yacc
import re  
import sqlite3

def conectar_db():
    conn = sqlite3.connect('BD.db')
    return conn

sql_mapping = {
    "TRAEME": "SELECT",
    "TODO": "*",
    "DE LA TABLA": "FROM",
    "DONDE": "WHERE",
    "AGRUPANDO POR": "GROUP BY",
    "MEZCLANDO": "JOIN",
    "EN": "ON",
    "LOS DISTINTOS": "DISTINCT",
    "CONTANDO": "COUNT",
    "METE EN": "INSERT INTO",
    "LOS VALORES": "VALUES",
    "ACTUALIZA": "UPDATE",
    "SETEA": "SET",
    "BORRA": "DELETE",
    "ORDENA POR": "ORDER BY",
    "COMO MUCHO": "LIMIT",
    "WHERE DEL GROUP BY": "HAVING",
    "EXISTE": "EXISTS",
    "EN ESTO:": "IN",
    "ENTRE": "BETWEEN",
    "PARECIDO A": "LIKE",
    "ES NULO": "IS NULL",
    "CAMBIA LA TABLA": "ALTER TABLE",
    "AGREGA LA COLUMNA": "ADD COLUMN",
    "ELIMINA LA COLUMNA": "DROP COLUMN",
    "CREA LA TABLA": "CREATE TABLE",
    "TIRA LA TABLA": "DROP TABLE",
    "POR DEFECTO": "DEFAULT",
    "UNICO": "UNIQUE",
    "CLAVE PRIMA": "PRIMARY KEY",
    "CLAVE REFERENTE": "FOREIGN KEY",
    "NO NULO": "NOT NULL",
    "TRANSFORMA A": "CAST",
    "Y": "AND",
    "O": "OR"
    
}

tokens = (
    'FRASE',
    'IDENTIFICADOR',
    'GREATER',
    'LESSER',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'COMMA',
    'DOT',
    'ALL',


)
t_GREATER = r'>'
t_LESSER = r'<'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_DOT = r'.'
t_ALL = r'\*'
   





def t_NUMBER(t):
    r'\d+'
    MAX_INT = 10**15 
    try:
        t.value = int(t.value)
        if t.value > MAX_INT:
            raise ValueError("Integer value too large")
    except ValueError:
        print("Integer value too large %d" % t.value)
        t.value = 0
    return t





t_FRASE = r'|'.join(re.escape(k) for k in sorted(sql_mapping, key=len, reverse=True))

t_IDENTIFICADOR = r'\'[^\']*\'|[a-zA-Z_][a-zA-Z0-9_]*'


t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter no reconocido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

def p_query(p):
    '''query : elementos'''
    p[0] = ' '.join(map(str, p[1]))


def p_elementos(p):
    '''elementos : elementos elemento
                 | elemento
                 '''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_elemento(p):
    '''elemento : FRASE
                | IDENTIFICADOR
                | ALL
                | NUMBER
                | dot_notation
                
     '''
    p[0] = sql_mapping.get(p[1], p[1])

def p_comparacion(p):
    '''elemento : elemento EQUALS elemento 
                | elemento GREATER elemento
                | elemento LESSER elemento
    '''
    
    p[0]= p[1] + " " + p[2] + " " + str(p[3])


def p_parentesis2(p):
    '''elemento : LPAREN lista_identificadores RPAREN'''
    p[0] = f"({p[2]})"

def p_lista_identificadores(p):
    '''lista_identificadores : lista_identificadores COMMA IDENTIFICADOR
                             | lista_identificadores COMMA NUMBER
                             | elemento'''
    if len(p) == 4:
        p[0] = f"{p[1]}, {p[3]}"
    else:
        p[0] = p[1]

def p_dot_notation(p):
    '''dot_notation : IDENTIFICADOR DOT IDENTIFICADOR'''
    
    p[0] = f"{p[1]}.{p[3]}"

parser = yacc.yacc()


            
def dar_vuelta():

    sql_mapping = {v: k for k, v in sql_mapping.items()}

