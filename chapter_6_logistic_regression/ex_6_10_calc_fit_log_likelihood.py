from math import log, exp
import pandas as pd
import misc.dre_helper as dh

CSV_PATH = './chapter_6_logistic_regression/data/simple_logistic_regression.csv'

def logistic_function(x, b0, b1) -> float:
    p = 1.0 / (1.0 + exp(-(b0 + b1 *x)))
    return p

def main():
    patient_data = pd.read_csv(CSV_PATH, delimiter=',').itertuples()

    # values calc'd from ex_6_8_log_regression_gradient_desc.py
    b0 = -3.17576395
    b1 = 0.69267212

    # sum the log-likelihoods
    log_likelihood_fit = 0.0

    for p in patient_data:
        if p.y == 1.0:
            log_likelihood_fit += log(logistic_function(p.x, b0, b1))
        elif p.y == 0.0:
            log_likelihood_fit += log(1 - logistic_function(p.x, b0, b1))

    print(log_likelihood_fit)   # -9.946161673231583

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
