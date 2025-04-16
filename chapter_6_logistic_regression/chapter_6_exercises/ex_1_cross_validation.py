import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
import misc.dre_helper as dh

CSV_PATH = './chapter_6_logistic_regression/data/light_dark_font_training_set.csv'
RANDOM_SEED = None

def main():
    
    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = df.values[:, :-1]
    Y = df.values[:, -1]

    kfold = KFold(n_splits=3, random_state=RANDOM_SEED, shuffle=True)
    model = LogisticRegression(penalty=None)

    results = cross_val_score(model, X, Y, cv=kfold)
    print(f'Accuracy Mean:  {results.mean():.3f} (stdev={results.std():.3f})')

    results = cross_val_score(model, X, Y, cv=kfold, scoring='roc_auc')
    print(f'AUC Mean:       {results.mean():.3f} (stdev={results.std():.3f})')

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
