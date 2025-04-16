from math import sqrt
import pandas as pd
from scipy.stats import t
import misc.dre_helper as dh

CSV_FILE = './chapter_5_linear_regression/data/linear_normal.csv'
SAMPLE_SIZE = 99

def calc_correlation_with_pandas():

    df = pd.read_csv(CSV_FILE)
    corr = df.corr(method='pearson')
    print('CORRELATION COEFFICIENT:', corr.x.y) # 0.92421
    return corr.x.y

def calc_statistical_significance():
    lower_cv = t(SAMPLE_SIZE - 1).ppf(0.025)
    upper_cv = t(SAMPLE_SIZE - 1).ppf(0.975)

    corr_coeff = calc_correlation_with_pandas()

    test_value = corr_coeff / sqrt((1 - corr_coeff**2) / (SAMPLE_SIZE - 2))

    print(f'TEST VALUE: {test_value}')
    print(f'CRITICAL RANGE: {lower_cv}, {upper_cv}')

    if test_value < lower_cv or test_value > upper_cv:
        print('CORRELATION PROVEN, REJECT H0')  # CORRELATION PROVEN, REJECT H0'
    else:
        print('CORRELATION NOT PROVEN, FAILED TO REJECT H0')

    if test_value > 0:
        p_value = 1.0 - t(SAMPLE_SIZE - 1).cdf(test_value)
    else:
        p_value = t(SAMPLE_SIZE - 1).cdf(test_value)

    p_value *= 2
    print(f'P-VALUE: {p_value}')    # 0.0; below 0.05 threshold: NO COINCIDENCE!

def main():
    dh.print_separator()
    calc_statistical_significance()
    dh.print_separator()

if __name__ == '__main__':
    main()
