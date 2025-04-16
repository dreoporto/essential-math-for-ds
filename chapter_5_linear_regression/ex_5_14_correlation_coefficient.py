# type: ignore
from math import sqrt
import pandas as pd
import misc.dre_helper as dh

CSV_PATH = './chapter_5_linear_regression/data/single_independent_variable_linear_small.csv'

def calc_correlation_with_pandas():

    df = pd.read_csv(CSV_PATH)

    correlations = df.corr(method='pearson')
    print(correlations)

def calc_correlation():

    points = list(pd.read_csv(CSV_PATH).itertuples())
    n = len(points)

    numerator = n * sum(p.x * p.y for p in points) - \
                sum(p.x for p in points) * sum(p.y for p in points)

    denominator = sqrt(n*sum(p.x**2 for p in points) - sum(p.x for p in points)**2) \
                * sqrt(n*sum(p.y**2 for p in points) - sum(p.y for p in points)**2)

    corr = numerator / denominator

    print(f'\n   {corr:0.6f}')

def main():
    dh.print_separator('CORRELATION COEFFICIENT: PANDAS')
    calc_correlation_with_pandas()
    dh.print_separator('MANUAL')
    calc_correlation()
    dh.print_separator()

if __name__ == '__main__':
    main()
