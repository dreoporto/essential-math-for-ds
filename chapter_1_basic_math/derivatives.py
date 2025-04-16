from sympy import *

def derivative2x():

    # declare 'x' to SymPy
    x = symbols('x')

    # declare function
    f = x**2

    # calculate the derivative of the function
    dx_f = diff(f)
    print('diff 2x:', dx_f)

    # calculate the slope at x = 2
    print('subs(x=2):', dx_f.subs(x, 2))

# translated from diff(f) results above
def slope2():

    # AEO NOTE: this is never used!
    # def f(x):
    #     return x**2

    def dx_f(x):
        return 2*x
    
    slope_at_2 = dx_f(2)
    print('slope@2:', slope_at_2)

def main():
    print('\n----\n')
    derivative2x()
    slope2()
    print('\n----\n')

if __name__ == '__main__':
    main()
