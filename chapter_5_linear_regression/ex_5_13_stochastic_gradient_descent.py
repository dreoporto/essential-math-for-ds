import pandas as pd
import numpy as np

SAMPLE_SIZE = 1
LEARNING_RATE = 0.0001
EPOCHS = 1_000_000  # number of iterations to perform gradeint descent

def main():
    data = pd.read_csv('./chapter_5_linear_regression/data/single_independent_variable_linear_small.csv', header=0)

    X = data.iloc[:, 0].values
    Y = data.iloc[:, 1].values

    n = data.shape[0]   # rows

    # build the model
    m = 0.0
    b = 0.0

    for i in range(EPOCHS):
        index = np.random.choice(n, SAMPLE_SIZE, replace=False)
        x_sample = X[index]
        y_sample = Y[index]

        y_pred = m * x_sample + b

        # calc derivatives
        d_m = (-2 / SAMPLE_SIZE) * sum(x_sample * (y_sample - y_pred))
        d_b = (-2 / SAMPLE_SIZE) * sum(y_sample - y_pred)

        m -= LEARNING_RATE * d_m
        b -= LEARNING_RATE * d_b

        if i % 10000 == 0:
            print(i, m, b)

    print(f'y = {m}x + {b}')

if __name__ == '__main__':
    main()
