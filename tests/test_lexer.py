import pytest

from moa.lexer import lexer


@pytest.mark.parametrize("expresion,result", [
    ("psi", ['PSI']), ('take', ['TAKE']), ('drop', ['DROP']),
    ('cat', ['CAT']), ('pdrop', ['PDROP']), ('ptake', ['PTAKE']),
    ('omega', ['OMEGA']), ('iota', ['IOTA']), ('dim', ['DIM']),
    ('tau', ['TAU']), ('shp', ['SHP']), ('rav', ['RAV']),
    ('(', ['LPAREN']), (')', ['RPAREN']),
    ('{', ['LBRACKET']), ('}', ['RBRACKET']),
    ('<', ['LANGLEBRACKET']), ('>', ['RANGLEBRACKET']),
    ('^', ['CARROT']), (';', ['ENDSTATEMENT']),
    ('+', ['PLUS']), ('-', ['MINUS']), ('*', ['TIMES']), ('/', ['DIVIDE']),
    ('=', ['EQUAL']),
    ('+red', ['PLUSRED']), ('-red', ['MINUSRED']),
    ('*red', ['TIMESRED']), ('/red', ['DIVIDERED']),
    ('asdf_asAVA', ['IDENTIFIER']),
    ("1234", ['INTEGER']), ('01234', ['INTEGER']), ('-12398', ['INTEGER']),
    ("1234.1234", ['FLOAT']), ('-12.123', ['FLOAT']),
])
def test_valid_single_token(expresion, result):
    lexer.input(expresion)
    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token.type)
    assert tokens == result


@pytest.mark.parametrize("expresion,error", [
    ('_asdf', "'_' no valid token can be formed from '_asdf'"),
])
def test_invalid_single_token(expresion, error):
    lexer.input(expresion)
    with pytest.raises(ValueError) as excinfo:
        tokens = []
        while True:
            token = lexer.token()
            if not token:
                break
            tokens.append(token.type)
    assert error in str(excinfo.value)
