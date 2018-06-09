import pytest

from moa import lexer


@pytest.mark.parametrize("expression,result", [
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
def test_valid_single_token(expression, result):
    lexer.input(expression)
    tokens = [token.type for token in lexer]
    assert tokens == result


@pytest.mark.parametrize("expression,error", [
    ('_asdf', "'_' no valid token can be formed from '_asdf'"),
])
def test_invalid_single_token(expression, error):
    lexer.input(expression)
    with pytest.raises(ValueError) as excinfo:
        tokens = [token.type for token in lexer]
    assert error in str(excinfo.value)


@pytest.mark.parametrize("expression,result", [
    ("< 1 2 3>", ['LANGLEBRACKET', 'INTEGER', 'INTEGER', 'INTEGER', 'RANGLEBRACKET']),
    ("<2> drop Xi", ['LANGLEBRACKET', 'INTEGER', 'RANGLEBRACKET', 'DROP', 'IDENTIFIER']),
    ("main()", ['IDENTIFIER', 'LPAREN', 'RPAREN']),
    ("AMY^3", ['IDENTIFIER', 'CARROT', 'INTEGER']),
    ('AMts =<2  >   ', ['IDENTIFIER', 'EQUAL', 'LANGLEBRACKET', 'INTEGER', 'RANGLEBRACKET']),
    ('  <    1 8 >;', ['LANGLEBRACKET', 'INTEGER', 'INTEGER', 'RANGLEBRACKET', 'ENDSTATEMENT']),
    ('Y cat   omega < 1 1>', ['IDENTIFIER', 'CAT', 'OMEGA', 'LANGLEBRACKET', 'INTEGER', 'INTEGER', 'RANGLEBRACKET'])
])
def test_valid_multiple_token(expression, result):
    lexer.input(expression)
    tokens = [token.type for token in lexer]
    assert tokens == result
