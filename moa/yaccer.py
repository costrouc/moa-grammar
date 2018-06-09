import ply.yacc as yacc

from .lexer import tokens
from . import primitives

def p_main(p):
    '''main : vector
            | array
            | constant_array
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
    p[0] = primitives.NDArray(shape=(len(p[2]),), data=p[2])

def p_array(p):
    '''array : ARRAY IDENTIFIER CARROT INTEGER vector'''
    if len(p[5].data) != p[4]:
        raise ValueError(f'Declared dimension {p[4]} does not match {p[5]}')
    p[0] = primitives.NDArray(
        shape=tuple(p[5].data), data=None,
        constant=False, identifier=p[2])

def p_constant_array(p):
    '''constant_array : CONST ARRAY IDENTIFIER CARROT INTEGER vector'''
    if len(p[6].data) != p[5]:
        raise ValueError(f'Declared dimension {p[5]} does not match {p[6].data}')
    p[0] = primitives.NDArray(
        shape=tuple(p[6].data), data=None,
        constant=True, identifier=p[3])

# def p_binary_operation(p):
#     """binary_operation : expression PLUS   expression
#                         | expression MINUS  expression
#                         | expression TIMES  expression
#                         | expression DIVIDE expression
#                         | expression PSI    expression
#                         | expression TAKE   expression
#                         | expression DROP   expression
#                         | expression CAT    expression
#                         | expression PDROP  expression
#                         | expression PTAKE  expression
#                         | expression OMEGA  expression
#     """
#     p[0] = primitives.BinaryOperation(operation=p[1], left=p[0], right=p[2])

# def p_unary_operation(p):
#     """unary_operation : IOTA       expression
#                        | DIM        expression
#                        | TAU        expression
#                        | SHP        expression
#                        | RAV        expression
#                        | PLUSRED    expression
#                        | MINUSRED   expression
#                        | TIMESRED   expression
#                        | DIVIDERED  expression
#     """
#     p[0] = primitives.UnaryOperation(operation=p[1], right=p[2])

# Error rule for syntax errors
def p_error(p):
    raise ValueError("Syntax error in input!")

parser = yacc.yacc()
