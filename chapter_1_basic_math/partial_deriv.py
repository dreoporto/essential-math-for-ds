
"""demonstrate partial derivatives"""
from sympy import diff, symbols
from sympy.plotting import plot3d

def calc_partial():
    """calculate partial derivative"""
    x, y = symbols('x y')

    f = 2*x**3 + 3*y**3

    dx_f = diff(f, x)
    dy_f = diff(f, y)

    print('dx_f:', dx_f)
    print('dy_f:', dy_f)

    plot3d(f)

def main():
    """call other functions here"""
    print('\n----\n')
    calc_partial()
    print('\n----\n')

if __name__ == '__main__':
    main()
