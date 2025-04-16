import pandas as pd

LEARNING_RATE = 0.001
ITERATIONS = 100_000

def main():

    points = list(pd.read_csv('./chapter_5_linear_regression/data/single_independent_variable_linear_small.csv').itertuples())
    # n = float(len(points)) UNUSED

    # model parameters to be calculated
    m = 0.0
    b = 0.0

    # perform gradient descent
    for _ in range(ITERATIONS):

        # slope with repect to m
        d_m = sum(2 * p.x * ((m * p.x + b) - p.y) for p in points) # type: ignore

        # slope with respect to b
        d_b = sum(2 * ((m * p.x + b) - p.y) for p in points) # type: ignore

        m -= LEARNING_RATE * d_m
        b -= LEARNING_RATE * d_b

    print(f'y = {m} * x + {b}')

if __name__ == '__main__':
    main()
