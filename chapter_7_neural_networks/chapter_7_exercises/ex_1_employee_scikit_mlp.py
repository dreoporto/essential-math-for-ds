import time

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

import misc.dre_helper as dh
import misc.dre_metrics as dm

CSV_PATH = './chapter_7_neural_networks/data/employee_retention_analysis.csv'

LEARNING_RATE = 0.05
ITERATIONS = 100_000
RANDOM_SEED = 42
SCALING_FACTOR = 100

def main():
    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = (df.values[:, :-1] / SCALING_FACTOR)
    y = df.values[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=RANDOM_SEED)

    nn = MLPClassifier(solver='adam',
                       hidden_layer_sizes=(4, ),
                       activation='relu',
                       max_iter=ITERATIONS,
                       learning_rate_init=LEARNING_RATE)
    
    trainingStart = time.time()
    nn.fit(X_train, y_train)
    trainingTime = time.time() - trainingStart

    print(f'Training time: {trainingTime:0.2f} seconds')

    print('Weights/Coefs:\n', nn.coefs_)
    print('Intercepts/Biases:\n', nn.intercepts_)

    print(f'Training set score: {nn.score(X_train, y_train):0.3%}')
    print(f'Test set score: {nn.score(X_test, y_test):0.3%}')

    print(f'Number of layers: {nn.n_layers_}')

    predictions = nn.predict(X_test)
    print(f'y_test:\t\t{y_test}')
    print(f'predictions:\t{predictions}')

    dh.print_separator('CONFUSION MATRIX')
    dm.print_confusion_matrix(y_test, predictions)
    
    dh.print_separator()
    dm.print_classification_metrics(y_test, predictions)

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
