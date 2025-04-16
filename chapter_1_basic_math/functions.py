"""
testing linear and related functions
"""
from sympy import symbols, plot
from sympy.plotting import plot3d

def linear_function():
    """
    plot a linear function
    """
    x = symbols('x')
    f = 2 * x + 1
    plot(f)

def exponential_function():
    """
    plot an exponential function
    """
    x = symbols('x')
    f = x**2 + 1
    plot(f)

def plot3d_function():
    """
    plot function with two independent variables    
    """
    x, y = symbols('x y')
    f = 2 * x + 3 * y
    plot3d(f)

def summation():
    my_sum = sum(2 * i for i in range(1, 6))
    print(my_sum)

def summation2():
    x = [1, 4, 6, 2]
    n = len(x)
    # my_sum = sum(10 * x[i] for i in range(0, n))
    # my_sum = sum(10 * x[i] for i in range(n))
    # my_sum = sum(10 * i for i in x)
    my_sum = sum(10 * i for i in x if i > 2)
    print(my_sum)

if __name__ == '__main__':
    # linear_function()
    # exponential_function()
    # plot3d_function()
    summation2()
