import time

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

import misc.dre_colors as dc
import misc.dre_helper as dh

CSV_PATH = './chapter_7_neural_networks/data/light_dark_font_training_set.csv'

LEARNING_RATE = 0.05
ITERATIONS = 100_000
RANDOM_COLOR_COUNT = 10

def main():
    df = pd.read_csv(CSV_PATH, delimiter=',')

    X = (df.values[:, :-1] / 255.0)
    y = df.values[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    nn = MLPClassifier(solver='sgd',
                       hidden_layer_sizes=(3, ),
                       activation='relu',
                       max_iter=ITERATIONS,
                       learning_rate_init=LEARNING_RATE)
    
    trainingStart = time.time()
    nn.fit(X_train, y_train)
    trainingTime = time.time() - trainingStart

    # scikit-learn (used here) and other libraries (ex: DNN with TensorFlow) are much faster
    print(f'Training time: {trainingTime:0.2f} seconds') # compare to ex_7_11_sgd_neural_net.py

    print('Weights/Coefs:\n', nn.coefs_)
    print('Intercepts/Biases:\n', nn.intercepts_)

    print(f'Training set score: {nn.score(X_train, y_train):0.3%}')
    print(f'Test set score: {nn.score(X_test, y_test):0.3%}')

    colors = dc.generate_random_colors(RANDOM_COLOR_COUNT)
    scaled_colors = colors / 255.0
    predictions = nn.predict(scaled_colors)
    predictions = (predictions >= 0.5).flatten().astype(int)

    dc.plot_colors(colors, predictions)

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
