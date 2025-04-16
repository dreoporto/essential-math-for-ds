 # type: ignore

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import misc.dre_helper as dh

CSV_FILE = './chapter_5_linear_regression/data/linear_normal.csv'

def calc_with_sk_learn():
    df = pd.read_csv(CSV_FILE, delimiter=',')

    X = df.values[:, :-1]
    Y = df.values[:, -1]

    fit = LinearRegression().fit(X, Y)
    m = fit.coef_.flatten()
    b = fit.intercept_.flatten()
    print(f'm:\t{m}')
    print(f'b:\t{b}')

    plt.plot(X, Y, 'o') # scatter
    plt.plot(X, m * X + b) # line
    plt.show()

def calc_simple_linear_regression():
    points = list(pd.read_csv(CSV_FILE, delimiter=',').itertuples())

    n = len(points)

    m = (n*sum(p.x*p.y for p in points) - sum(p.x for p in points) *
        sum(p.y for p in points)) / (n*sum(p.x**2 for p in points) -
        sum(p.x for p in points)**2)

    b = (sum(p.y for p in points) / n) - m * sum(p.x for p in points) / n

    print(f'm:\t{m}')   # 1.7591931481052476
    print(f'b:\t{b}')   # 4.69359654825405


def main():
    dh.print_separator('SK LEARN')

    calc_with_sk_learn()

    dh.print_separator('SIMPLE')

    calc_simple_linear_regression()

    dh.print_separator()

if __name__ == '__main__':
    main()
