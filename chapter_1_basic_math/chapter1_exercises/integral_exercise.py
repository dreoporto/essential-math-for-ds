from sympy import symbols, integrate

def calc_integral():
    x = symbols('x')

    f = 3*x**2 + 1
    
    area = integrate(f, (x, 0, 2))
    
    print('area:', area)

def main():
    print('\n----\n')

    calc_integral()

    print('\n----\n')

if __name__ == '__main__':
    main()
