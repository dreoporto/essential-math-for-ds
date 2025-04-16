import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, ShuffleSplit, cross_val_score
from ptmlib.time import Stopwatch
import misc.dre_helper as dh

# CSV_PATH = './chapter_5_linear_regression/data/single_independent_variable_linear.csv'
CSV_PATH = './chapter_5_linear_regression/data/linear_normal.csv'

def main(random_fold:bool = False):
    stopwatch = Stopwatch()

    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = df.values[:, :-1]
    Y = df.values[:, -1]

    stopwatch.start()
    kfold = ShuffleSplit(n_splits=1000, test_size=0.33, random_state=7) if random_fold else KFold(n_splits=3, random_state=7, shuffle=True)
    model = LinearRegression()
    results = cross_val_score(model, X, Y, cv=kfold)
    stopwatch.stop(silent=True)

    # print(results)
    print(f'MSE: mean={results.mean():0.5f}; stdev={results.std():0.6f}')

if __name__ == '__main__':
    dh.print_separator('KFold')
    main()
    dh.print_separator('ShuffleSplit (random fold)')
    main(True)
    dh.print_separator()
