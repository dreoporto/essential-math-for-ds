import math
import pandas as pd
import misc.dre_helper as dh

CSV_PATH = './chapter_6_logistic_regression/data/simple_logistic_regression.csv'
b0 = -3.17576395
b1 = 0.69267212

def logistic_function(x) -> float:
    p = 1.0 / (1.0 + math.exp(-(b0 + b1 * x)))
    return p

def calc_joint_likelihood(data) -> float:
    joint_likelihood = 0.0 # use 1.0 for *=; use 0.0 for +=

    # USING IF/ELSE
    # for p in data:
    #     if p.y == 1.0:
    #         joint_likelihood *= logistic_function(p.x)
    #     else:
    #         joint_likelihood *= (1.0 - logistic_function(p.x))

    # WITHOUT IF EXPRESSION
    # for p in data:
    #     joint_likelihood *= \
    #         logistic_function(p.x) ** p.y * \
    #         (1.0 - logistic_function(p.x)) ** (1.0 - p.y)

    for p in data:
        joint_likelihood += math.log( \
            logistic_function(p.x) ** p.y * \
            (1.0 - logistic_function(p.x)) ** (1.0 - p.y))

        print(p.x, p.y, logistic_function(p.x), joint_likelihood)

    joint_likelihood = math.exp(joint_likelihood)

    return joint_likelihood

def main():
    patient_data = pd.read_csv(CSV_PATH, delimiter=',').itertuples()
    print(f'joint_likelihood: {calc_joint_likelihood(patient_data)}')

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
