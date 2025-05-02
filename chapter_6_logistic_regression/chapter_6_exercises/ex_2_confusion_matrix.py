import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, f1_score, precision_score,
                             recall_score)
from sklearn.model_selection import train_test_split

import misc.dre_colors as dc
import misc.dre_helper as dh


CSV_PATH = './chapter_6_logistic_regression/data/light_dark_font_training_set.csv'
RANDOM_SEED = 42
RANDOM_COLOR_COUNT = 10

def main() -> None:

    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = df.values[:, :-1]
    Y = df.values[:, -1]

    model = LogisticRegression(solver='liblinear')

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=RANDOM_SEED)
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)

    tn, fp, fn, tp = confusion_matrix(y_true=y_test, y_pred=prediction).ravel()
    dh.print_separator('CONFUSION MATRIX')
    print(f'TP:{tp}\tFN:{fn}')
    print(f'FP:{fp}\tTN:{tn}')
    dh.print_separator()

    score = f1_score(y_true=y_test, y_pred=prediction)
    print(f'F1 score:\t{score:0.4}')

    p_score = precision_score(y_true=y_test, y_pred=prediction)
    print(f'Precision:\t{p_score:0.4f}')

    r_score = recall_score(y_true=y_test, y_pred=prediction)
    print(f'Recall:\t\t{r_score:0.4f}')

    colors = dc.generate_random_colors(RANDOM_COLOR_COUNT)
    dh.print_separator('RANDOM BACKGROUNDS')
    print(colors)

    prediction = model.predict(colors)
    dh.print_separator('PREDICTED FONT COLORS')
    print(prediction)

    # expand PREDICTION to match SHAPE of COLORS using np.newaxis
    combined = np.concatenate((colors, prediction[:, np.newaxis]), axis=1)
    dh.print_separator('COMBINED')
    print(combined)

    dc.plot_colors(colors, prediction)

if __name__ == '__main__':
    main()
