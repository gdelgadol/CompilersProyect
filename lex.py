import ply.lex as lex

# List of token names
tokens = [
    'NAME', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'EQUALS', 'FRACTION', 
    'SQRT', 'SIN', 'COS', 'TAN', 'LOG', 'EXP', 'SEP'
]

# Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\\times'
t_DIVIDE = r'\\div'
t_POWER = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EQUALS = r'='
t_FRACTION = r'\\frac'
t_SQRT = r'\\sqrt'
t_SIN = r'\\sin'
t_COS = r'\\cos'
t_TAN = r'\\tan'
t_LOG = r'\\log'
t_EXP = r'\\exp'
t_SEP = r','
t_ignore = ' \t'

# Ignore \left and \right (they don't affect parsing)
def t_LEFT(t):
    r'\\left'
    pass  # Ignore

def t_RIGHT(t):
    r'\\right'
    pass  # Ignore

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_]\w*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    data = r"\sin{\left(\frac{1}{2}\right)} + \cos{(x^3)} - \tan{\left(\sqrt{x}\right)}"
    lexer.input(data)
    print("Tokens:")
    for tok in lexer:
        print(tok)
