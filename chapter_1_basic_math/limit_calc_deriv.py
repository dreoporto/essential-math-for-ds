
"""demonstrate calculating derivative using limit"""
from sympy import symbols, limit

def calc_derivative():
    """calc using limit"""
    x, s = symbols('x s')

    f = x**2

    # slope over two points with gap "s"
    # substitute into rise-over-run formula
    slope_f = (f.subs(x, x + s) - f) / ((x+s - x))

    slope_2 = slope_f.subs(x, 2)

    result = limit(slope_2, s, 0)
    print(result)

    result = limit(slope_f, s, 0)
    print(result)

def main():
    """call other functions here"""
    print('\n----\n')
    calc_derivative()
    print('\n----\n')

if __name__ == '__main__':
    main()
