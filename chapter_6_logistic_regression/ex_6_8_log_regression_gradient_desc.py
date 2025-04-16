# type: ignore

from sympy import *
import pandas as pd
from ptmlib.time import Stopwatch
import misc.dre_helper as dh

CSV_PATH = './chapter_6_logistic_regression/data/simple_logistic_regression.csv'

def main():
    stopwatch = Stopwatch()
    points = list(pd.read_csv(CSV_PATH).itertuples())

    b1, b0, i, n = symbols('b1 b0 i n')
    x, y = symbols('x y', cls=Function)

    joint_likelihood = Sum(log((1.0 / (1.0 + exp(-(b0 + b1 * x(i))))) ** y(i) \
	    * (1.0 - (1.0 / (1.0 + exp(-(b0 + b1 * x(i)))))) ** (1 - y(i))), (i, 0, n))
    
    dh.print_separator('Partial derivatives...')
    stopwatch.start()

    d_b1 = diff(joint_likelihood, b1) \
        .subs(n, len(points) - 1).doit() \
        .replace(x, lambda i: points[i].x) \
        .replace(y, lambda i: points[i].y)
    
    d_b0 = diff(joint_likelihood, b0) \
        .subs(n, len(points) - 1).doit() \
        .replace(x, lambda i: points[i].x) \
        .replace(y, lambda i: points[i].y)    
    
    stopwatch.stop(silent=True)
    dh.print_separator()
    
    dh.print_separator('Compile using lambdify')
    stopwatch.start()

    d_b1 = lambdify([b1, b0], d_b1)
    d_b0 = lambdify([b1, b0], d_b0)

    stopwatch.stop(silent=True)
    dh.print_separator()
    
    dh.print_separator('Performing gradient descent...')
    stopwatch.start()

    b1 = 0.01
    b0 = 0.01
    L = .01

    for _ in range(10_000):
        b1 += d_b1(b1, b0) * L
        b0 += d_b0(b1, b0) * L

    stopwatch.stop(silent=True)
    dh.print_separator()

    print(b1, b0)

if __name__ == '__main__':
    dh.print_separator()
    main_stopwatch = Stopwatch()
    main_stopwatch.start()

    main()

    main_stopwatch.stop(silent=True)
    dh.print_separator()
