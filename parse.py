import ply.yacc as yacc
import math
from lex import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS'),
)

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression"""
    if p[2] == '+': p[0] = f"({p[1]} + {p[3]})"
    elif p[2] == '-': p[0] = f"({p[1]} - {p[3]})"
    elif p[2] == '\\times': p[0] = f"({p[1]} * {p[3]})"
    elif p[2] == '\\div': p[0] = f"({p[1]} / {p[3]})"
    elif p[2] == '^': p[0] = f"({p[1]} ** {p[3]})"

def p_expression_fraction(p):
    "expression : FRACTION LBRACE expression RBRACE LBRACE expression RBRACE"
    p[0] = f"({p[3]} / {p[6]})"

def p_expression_sqrt(p):
    "expression : SQRT grouping"
    p[0] = f"({p[2]} ** 0.5)"

def p_expression_function(p):
    """expression : SIN grouping
                  | COS grouping
                  | TAN grouping
                  | LOG grouping
                  | EXP grouping"""
    p[0] = f"math.{p[1][1:]}({p[2]})"

def p_expression_pi(p):
    "expression : PI"
    p[0] = "math.pi"


def p_grouping(p):
    """grouping : LBRACE expression RBRACE
                | LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = str(p[1])

def p_expression_variable(p):
    "expression : NAME"
    p[0] = p[1]

def p_expression_parens(p):
    "expression : LPAREN expression RPAREN %prec UMINUS"
    p[0] = f"({p[2]})"

def p_error(p):
    print("Syntax error:", p)

parser = yacc.yacc(start='expression')

def parse_latex_to_python(latex_expr):
    return parser.parse(latex_expr)

if __name__ == "__main__":
    test_expr = r"\sin{\left(\frac{1}{2}\right)} + \cos{(x^3)} - \tan{\left(\sqrt{x}\right)}"
    print("LaTeX:", test_expr)
    print("Python:", parse_latex_to_python(test_expr))
