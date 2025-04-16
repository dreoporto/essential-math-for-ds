from sympy import *
from math import log

def my_sympy_1():
    i, n = symbols('i, n')

    my_sum = Sum(2 * i, (i, 1, n))

    up_to_5 = my_sum.subs(n, 5)

    print(up_to_5.doit())

def my_symbols():
    x = symbols('x')
    expr = x**2 / x**5
    print(expr)

    expr2 = x**-3
    print(expr2)

def my_log():
    x = log(8, 2)
    print(x)

    y = log(100) # python uses euler's number as default
    print(y)

    z = log(100, 10)
    print(z)

def main():
    # my_sympy_1()
    my_symbols()
    my_log()

if __name__ == '__main__':
    main()
