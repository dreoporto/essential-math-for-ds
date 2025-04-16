from math import exp
from sympy import symbols, limit, oo

def limit_zero():

    x = symbols('x')
    f = 1 / x
    result = limit(f, x, oo)

    print('limit 0:', result) # 0

def limit_e():

    n = symbols('n')
    f = (1 + (1/n))**n
    result = limit(f, n, oo)

    print('limit E:', result) # E
    print('evalf:', result.evalf())
    print('euler:', exp(1))

def limit_div_zero():
    n = symbols('n')
    f = 1 / n
    # EXAMPLE: f = (rate / n + 1)**(years*n) * principal
    # f = (1 + 0.05 / n)**(3*n) * 1000
    result = limit(f, n, oo)

    print('limit div0:', result)
    print('div0 evalf():', result.evalf())

def main():
    print('\n-------\n')
    limit_zero()
    limit_e()
    limit_div_zero()
    print('\n-------\n')

if __name__ == '__main__':
    main()
