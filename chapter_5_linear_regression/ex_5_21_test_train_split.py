import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
from ptmlib.time import Stopwatch
import misc.dre_helper as dh

CSV_PATH = './chapter_5_linear_regression/data/single_independent_variable_linear.csv'

def main():
    df = pd.read_csv(CSV_PATH, delimiter=',')

    # Extract input variables (all rows, all columns but last column)
    X = df.values[:, :-1]
    # Extract output variables (all rows, last column)
    Y = df.values[:, -1]

    # train/test split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

    model = LinearRegression()

    stopwatch = Stopwatch()
    stopwatch.start()
    model.fit(X_train, Y_train)
    stopwatch.stop(silent=True)

    result = model.score(X_test, Y_test)
    print(f'r^2: {result:0.3%}')
    print(f'x=99.5; y predict={model.predict(np.array([99.5]).reshape(-1, 1))[0]:0.3f}')

if __name__ == '__main__':
    dh.print_separator('TRAIN/TEST SPLIT')
    main()
    dh.print_separator()
