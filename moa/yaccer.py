import ply.yacc as yacc

from .lexer import tokens
from .primitives import NDArray

def p_main(p):
    '''main : vector
    '''
    p[0] = p[1]

def p_number_list(p):
    '''number_list : number_list INTEGER
                   | number_list FLOAT
                   |
    '''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = list()

def p_vector(p):
    'vector : LANGLEBRACKET number_list RANGLEBRACKET'
    p[0] = NDArray(shape=(len(p[2]),), data=p[2])

# def p_binary_opperation(p):
#     """binary_opperation : expression PLUS expression

#     """

# Error rule for syntax errors
def p_error(p):
    raise ValueError("Syntax error in input!")

parser = yacc.yacc()
