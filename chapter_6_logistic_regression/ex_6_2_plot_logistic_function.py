from sympy import symbols, plot, exp
import misc.dre_helper as dh

COEF_B0 = -3.17581
INTERCEPT_B1 = 0.69269

'''
COEF (beta1):           0.69269
INTERCEPT (beta0):      -3.17581
'''

def main():
    
    b0, b1, x = symbols('b0 b1 x')

    p = 1.0 / (1.0 + exp(-(b0 + b1 * x))) # type: ignore

    p = p.subs(b0, COEF_B0)
    p = p.subs(b1, INTERCEPT_B1)
    print(p)

    plot(p)

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
