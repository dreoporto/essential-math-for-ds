import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import misc.dre_helper as dh
import misc.dre_metrics as dm

CSV_PATH = './chapter_6_logistic_regression/data/employee_retention_analysis.csv'
RANDOM_SEED = 10

def main():
    
    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = df.values[:, :-1]
    Y = df.values[:, -1]

    model = LogisticRegression(solver='liblinear')

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=RANDOM_SEED)
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)

    dh.print_separator('CONFUSION MATRIX')
    dm.print_confusion_matrix(y_true=y_test, y_pred=prediction)

    dh.print_separator() 
    dm.print_classification_metrics(y_true=y_test, y_pred=prediction)
    
    dh.print_separator()

if __name__ == '__main__':
    main()
