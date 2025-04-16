import pandas as pd
from sklearn.linear_model import LogisticRegression
import misc.dre_helper as dh

CSV_PATH = './chapter_6_logistic_regression/data/simple_logistic_regression.csv'

def main():
    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = df.values[:,:-1]
    Y = df.values[:, -1]

    model = LogisticRegression(penalty=None)
    model.fit(X, Y)

    print(f'COEF (beta1):\t\t{model.coef_.flatten()[0]:0.5f}')
    print(f'INTERCEPT (beta0):\t{model.intercept_.flatten()[0]:0.5f}') 
    print(f'predict [5, 4]:\t\t{model.predict([[5], [4]])}')
    print(f'predict_proba [5, 4]:\n{model.predict_proba([[5], [4]])}') # type: ignore

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
