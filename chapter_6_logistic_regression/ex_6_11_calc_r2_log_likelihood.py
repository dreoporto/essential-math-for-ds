# type: ignore

from math import log, exp
import pandas as pd
import misc.dre_helper as dh

CSV_PATH = './chapter_6_logistic_regression/data/simple_logistic_regression.csv'

def logistic_function(x, b0, b1) -> float:
    p = 1.0 / (1.0 + exp(-(b0 + b1 *x)))
    return p

def main():
    patient_data = list(pd.read_csv(CSV_PATH, delimiter=',').itertuples())

    # values calc'd from ex_6_8_log_regression_gradient_desc.py
    b0 = -3.17576395
    b1 = 0.69267212

    # calculate the log likelihood of the fit
    log_likelihood_fit = sum(log(logistic_function(p.x, b0, b1)) * p.y + 
                             log(1.0 - logistic_function(p.x, b0, b1)) * (1.0 - p.y) 
                             for p in patient_data)

    print(log_likelihood_fit)   # -9.946161673231583

    #calculate the log likelihood without fit
    likelihood = sum(p.y for p in patient_data) / len(patient_data)

    log_likelihood = sum(log(likelihood) * p.y + 
                         log(1.0 - likelihood) * (1.0 - p.y) 
                         for p in patient_data)
    
    print(log_likelihood)   # -14.341070198709906

    # calculate R-Squared
    r2 = (log_likelihood - log_likelihood_fit) / log_likelihood
    print(r2)   # 0.306456105756576


if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
