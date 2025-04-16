 # type: ignore

from math import sqrt
import pandas as pd
from scipy.stats import t
import misc.dre_helper as dh

CSV_FILE = './chapter_5_linear_regression/data/linear_normal.csv'
X_VALUE = 50
CI = 0.95
CI_RIGHT = CI + ((1 - CI) / 2)

def main():

    points = list(pd.read_csv(CSV_FILE, delimiter=',').itertuples())

    n = len(points)

    m = 1.7591931481052476
    b = 4.69359654825405

    # calculate prediction interval for X_VALUE at CI
    x_mean = sum(p.x for p in points) / n
    t_value = t(n - 2).ppf(CI_RIGHT)

    standard_error = sqrt(sum((p.y - (m * p.x + b)) ** 2 for p in points) / (n - 2))

    margin_of_error = t_value * standard_error * \
                    sqrt(1 + (1 / n) + (n * (X_VALUE - x_mean) ** 2) / \
                        (n * sum(p.x ** 2 for p in points) - \
                                sum(p.x for p in points) ** 2))

    predicted_y = m * X_VALUE + b

    # Calculate prediction interval
    print(predicted_y - margin_of_error, predicted_y + margin_of_error) # 50.79208640247933 134.51442150455352
    print(f'(predicted_y = {predicted_y} +/- {margin_of_error})') # 92.65325395351643 +/- 41.8611675510371

if __name__ == '__main__':
    dh.print_separator(f'{CI:0.0%} PREDICTION INTERVAL (X={X_VALUE}; right: {CI_RIGHT})')
    main()
    dh.print_separator()
