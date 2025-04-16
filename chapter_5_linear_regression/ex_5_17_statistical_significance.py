from math import sqrt
from scipy.stats import t
import misc.dre_helper as dh

def main():
    sample_size = 10

    lower_cv = t(sample_size - 1).ppf(0.025)
    upper_cv = t(sample_size - 1).ppf(0.975)

    corr_coeff = 0.957586 # value calculated in ex 5.14

    test_value = corr_coeff / sqrt((1 - corr_coeff**2) / (sample_size - 2))

    print(f'TEST VALUE: {test_value}')
    print(f'CRITICAL RANGE: {lower_cv}, {upper_cv}')

    if test_value < lower_cv or test_value > upper_cv:
        print('CORRELATION PROVEN, REJECT H0')
    else:
        print('CORRELATION NOT PROVEN, FAILED TO REJECT H0')

    if test_value > 0:
        p_value = 1.0 - t(sample_size - 1).cdf(test_value)
    else:
        p_value = t(sample_size - 1).cdf(test_value)

    p_value *= 2
    print(f'P-VALUE: {p_value}')

if __name__ == '__main__':
    dh.print_separator('STATISTICAL SIGNIFICANCE')
    main()
    dh.print_separator()
