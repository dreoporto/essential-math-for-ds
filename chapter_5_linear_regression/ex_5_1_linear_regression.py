import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():

    # import points
    df = pd.read_csv('./chapter_5_linear_regression/data/single_independent_variable_linear_small.csv', delimiter=',')

    # extract input values (all rows, all columns but last column)
    X = df.values[:, :-1]

    # extract output column (all rows, last column)
    Y = df.values[:, -1]

    fit = LinearRegression().fit(X, Y)

    m = fit.coef_.flatten()
    b = fit.intercept_.flatten() # type: ignore
    print(f'm:\t{m}')
    print(f'b:\t{b}')

    plt.plot(X, Y, 'o') # scatter
    plt.plot(X, m * X + b) # line
    plt.show()

if __name__ == '__main__':
    main()
