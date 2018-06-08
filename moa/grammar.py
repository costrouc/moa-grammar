tokens = (
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUAL'
    'PSI', 'TAKE', 'DROP', 'CAT', 'PDROP', 'PTAKE', 'OMEGA',
    'LANGLEBRACKET', 'RANGLEBRACKET',
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'CARROT',
    'INTEGER', 'FLOAT', 'IDENTIFIER'
)

# Tokens

## symbols
t_DIGIT   = r'[0-9]'
t_LETTER  = r'[a-zA-Z]'
# t_IDENTIFIER ?
t_INTEGER = r'\d+'
t_FLOAT   = r'\d+\.\d+'

## containers
t_LPAREN = r'('
t_RPAREN = r')'
t_LANGLEBRACKET = r'<'
t_RANGLEBRACKET = r'>'
t_CARROT = r'^'

## operators
t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_PSI    = r'Ψ'
t_TAKE   = r'Δ'
t_DROP   = r'∇'
t_CAT    = r'⧺'
t_OMEGA  = r'Ω'
