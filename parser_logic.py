import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+(\.\d+)?'

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = ('+', p[1], p[3]) if p[2] == '+' else ('-', p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    p[0] = ('*', p[1], p[3]) if p[2] == '*' else ('/', p[1], p[3])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = float(p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Error de sintaxis en la entrada")

parser = yacc.yacc()

def evaluate_tree(tree):
    if isinstance(tree, tuple):
        op, left, right = tree
        if op == '+':
            return evaluate_tree(left) + evaluate_tree(right)
        elif op == '-':
            return evaluate_tree(left) - evaluate_tree(right)
        elif op == '*':
            return evaluate_tree(left) * evaluate_tree(right)
        elif op == '/':
            return evaluate_tree(left) / evaluate_tree(right)
    else:
        return tree