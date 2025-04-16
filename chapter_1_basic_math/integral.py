"""integral calculation examples"""
from sympy import symbols, integrate

def calc_integration():
    """perform integral calc"""
    x = symbols('x')

    # function to integrate
    f = x**2 + 1

    # calculate integral of function with respect to x for area between x = 0 and 1
    area = integrate(f, (x, 0, 1))

    print("area", area) # gives us exact rational number 4/3
    print("area.evalf()", area.evalf()) # gives us decimal number

def main():
    """call other functions here"""
    print('\n----\n')

    # result should be 4/3, same as integral_approx.py
    calc_integration()

    print('\n----\n')

if __name__ == '__main__':
    main()
