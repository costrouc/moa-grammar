import ply.yacc as yacc

from .lexer import tokens
from . import primitives

# binary operators need precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'PSI', 'TAKE', 'DROP', 'CAT', 'PDROP', 'PTAKE', 'OMEGA'),
    ('right', 'IOTA', 'DIM', 'TAU', 'SHP', 'RAV', 'PLUSRED', 'MINUSRED', 'TIMESRED', 'DIVIDERED'),
    ('right', 'EQUAL'),
)


def p_main(p):
    '''main : function'''
    p[0] = p[1]


def p_number_list(p):
    '''number_list : number_list INTEGER
                   | number_list FLOAT
                   | empty
    '''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = list()


def p_vector(p):
    '''vector : LANGLEBRACKET number_list RANGLEBRACKET'''
    p[0] = primitives.NDArray(shape=(len(p[2]),), data=p[2])


def p_array(p):
    '''array : ARRAY IDENTIFIER CARROT INTEGER vector'''
    if len(p[5].data) != p[4]:
        raise ValueError(f'Declared dimension {p[4]} does not match {p[5]}')
    p[0] = primitives.NDArray(
        shape=tuple(p[5].data), data=None,
        constant=False, identifier=p[2])


def p_array_list(p):
    '''array_list : array_list COMMA array
                  | LPAREN array
                  | LPAREN
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    elif len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = []


def p_constant_array(p):
    '''constant_array : CONST ARRAY IDENTIFIER CARROT INTEGER vector'''
    if len(p[6].data) != p[5]:
        raise ValueError(f'Declared dimension {p[5]} does not match {p[6].data}')
    p[0] = primitives.NDArray(
        shape=tuple(p[6].data), data=None,
        constant=True, identifier=p[3])


def p_undefined_array(p):
    '''reference_array : IDENTIFIER'''
    p[0] = primitives.NDArray(
        shape=None, data=None,
        constant=False, identifier=p[1])


def p_unary_operation(p):
    """unary_operation : IOTA       term
                       | DIM        term
                       | TAU        term
                       | SHP        term
                       | RAV        term
                       | PLUSRED    term
                       | MINUSRED   term
                       | TIMESRED   term
                       | DIVIDERED  term
    """
    p[0] = primitives.UnaryOperation(operator=p[1].upper(), right=p[2])


def p_binary_operation(p):
    """binary_operation : term PLUS   term
                        | term MINUS  term
                        | term TIMES  term
                        | term DIVIDE term
                        | term PSI    term
                        | term TAKE   term
                        | term DROP   term
                        | term CAT    term
                        | term PDROP  term
                        | term PTAKE  term
                        | term OMEGA  term
    """
    p[0] = primitives.BinaryOperation(operator=p[2].upper(), left=p[1], right=p[3])


def p_term(p):
    """term : LPAREN binary_operation RPAREN
            | LPAREN unary_operation  RPAREN
            | LPAREN reference_array  RPAREN
            | binary_operation
            | unary_operation
            | reference_array
            | vector
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_function(p):
    """function : IDENTIFIER array_list RPAREN LBRACKET statement_list RBRACKET

    """
    p[0] = primitives.Function(arguments=p[2], statements=p[5], identifier=p[1])


def p_statement_list_identifier(p):
    """statement_list : statement_list IDENTIFIER EQUAL term ENDSTATEMENT"""
    p[0] = p[1] + [primitives.BinaryOperation(
        operator='EQUAL',
        left=primitives.NDArray(
            shape=None, data=None,
            constant=False, identifier=p[2]),
        right=p[4])]


def p_statement_list_constant_array(p):
    """statement_list : statement_list constant_array EQUAL vector ENDSTATEMENT"""
    p[0] = p[1] + [primitives.NDArray(
            shape=p[2].shape, data=p[4].data,
            constant=True, identifier=p[2].identifier)]


def p_statement_list_array(p):
    """statement_list : statement_list array ENDSTATEMENT"""
    p[0] = p[1] + [p[2]]


def p_statement_list_emptry(p):
    """statement_list : empty"""
    p[0] = []


def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    raise ValueError("Syntax error in input!")


def build_parser(start=None):
    return yacc.yacc(start=start)
