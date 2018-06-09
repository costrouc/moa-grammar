import ply.yacc as yacc

from .lexer import tokens
from .primitives import NDArray

def p_number(p):
    '''number : INTEGER
              | FLOAT
    '''
    p[0] = p[1]

def p_vector_begin(p):
    'partial_vector : LANGLEBRACKET'
    p[0] = list()

def p_vector_middle(p):
    'partial_vector : partial_vector number'
    p[0] = p[1].append(p[2])

def p_vector_end(p):
    'vector : partial_vector RANGLEBRACKET'
    p[0] = NDArray(shape=(len(p[1]),), data=p[1])

# Error rule for syntax errors
def p_error(p):
    raise ValueError("Syntax error in input!")

parser = yacc.yacc()
