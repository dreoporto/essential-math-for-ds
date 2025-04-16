# using gradient descent to find the minimum of a parabola

import random
from sympy import diff, symbols

def f(x: float) -> float:
    return (x - 3) ** 2 + 4

def dx_f(x: float) -> float:
    # return 2 * (x - 3) # BOOK VERSION
    return 2 * x - 6 # CALCULATED VERSION; SAME RESULT :)

def calc_derivative():
    x = symbols('x')
    my_f = (x - 3) ** 2 + 4
    calculated_dx_f = diff(my_f)
    print(f'calculated_dx_f:\t{calculated_dx_f}')

LEARNING_RATE = 0.001
ITERATIONS = 100_000

def main():
    x = random.randint(-15, 15)

    for i in range(ITERATIONS):
        # get slope
        d_x = dx_f(x)

        # update x by subtracting: learning rate * slope
        x -= LEARNING_RATE * d_x

        if i % 100 == 0:
            print(f'step({i}):\t{x}')

    print('\n')

    calc_derivative()
    print(f'x:\t{x}')
    print(f'f(x):\t{f(x)}')

if __name__ == '__main__':
    print('\n----\n')
    main()
    print('\n----\n')
