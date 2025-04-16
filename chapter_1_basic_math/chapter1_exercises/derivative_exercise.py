from sympy import symbols, diff

def calc_derivative():
    x = symbols('x')
    f = 3*x**2 + 1

    # calc derivative of function
    dx_f = diff(f)
    print('dx_f:', dx_f)

    # calc slope at x=2
    print('slope x=3:', dx_f.subs(x, 3))

def main():
    print('\n----\n')

    calc_derivative()

    print('\n----\n')

if __name__ == '__main__':
    main()
