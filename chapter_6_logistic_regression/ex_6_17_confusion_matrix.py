import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

CSV_PATH = './chapter_6_logistic_regression/data/employee_retention_analysis.csv'
RANDOM_SEED = 10

def main():
    
    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = df.values[:, :-1]
    Y = df.values[:, -1]

    model = LogisticRegression(solver='liblinear')

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=RANDOM_SEED)
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)

    matrix = confusion_matrix(y_true=Y_test, y_pred=prediction)
    print(matrix)

if __name__ == '__main__':
    main()
