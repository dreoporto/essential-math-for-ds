"""demonstrates the chain rule of derivatives"""

from sympy import symbols, diff

# REMEMBER THAT PYTHON IS GREAT FOR TRANSLATING MATH NOTATION TO CODE! :)
# y = x**2 + 1
# z = y**3 - 2
# z = (x**2 + 1)**3 - 2

def find_derivative_z_x():
    """find the derivative of z with respect to x"""

    x = symbols('x')

    z = (x**2 + 1)**3 - 2
    dz_dx = diff(z, x)
    print('dz_dx:\t\t', dz_dx)

def calc_derivative_chain_rule():
    """
    calculating the derivative dz/dx with and without the chain rule, 
    but still getting the same answer
    """
    x, y = symbols('x y')

    # derivative for first function
    # need to underscore y to prevent variable clash
    _y = x**2 + 1
    dy_dx = diff(_y)

    # derivative for the second function
    z = y**3 - 2
    dz_dy = diff(z)

    # calculate the derivative with and without
    # chain rule, substitute y function
    dz_dx_chain = (dy_dx * dz_dy).subs(y, _y)
    dz_dx_no_chain = diff(z.subs(y, _y))

    # both are equal! :)
    print('dz_dx_chain:\t', dz_dx_chain)
    print('dz_dx_no_chain:\t', dz_dx_no_chain)

def main():
    """calls others functions"""
    print('\n----\n')
    find_derivative_z_x()
    calc_derivative_chain_rule()
    print('\n----\n')

if __name__ == '__main__':
    main()
