import time

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

import misc.dre_colors as dc
import misc.dre_helper as dh

CSV_PATH = './chapter_7_neural_networks/data/light_dark_font_training_set.csv'

RANDOM_SEED = 42
LEARNING_RATE = 0.05
ITERATIONS = 100_000
RANDOM_COLOR_COUNT = 10

# create activation/output functions
relu = lambda x: np.maximum(x, 0)
logistic = lambda x: 1 / (1 + np.exp(-x))

# derivatives of output functions 
d_relu = lambda x: x > 0 # calculated manually; see https://tinyurl.com/3ydw4ww6
d_logistic = lambda x: np.exp(-x)/(1 + np.exp(-x)) ** 2 # source: ex_7_10 results

def forward_propagation(X, w_hidden, b_hidden, w_output, b_output):
    # uses @ for matrix multiplication
    # Z: unactivated output
    # A: activated output
    Z1 = w_hidden @ X + b_hidden
    A1 = relu(Z1) # hidden layer result
    Z2 = w_output @ A1 + b_output
    A2 = logistic(Z2) # output layer result
    return Z1, A1, Z2, A2

def backward_propagation(Z1, A1, Z2, A2, X, Y, w_output):
    # returns slopes for weights and biases using chain rule
    # formula source: ex_7_10 results
    dC_dA2 = 2*A2 - 2*Y
    dA2_dZ2 = d_logistic(Z2)
    dZ2_dA1 = w_output
    dZ2_dW2 = A1
    dZ2_dB2 = 1
    dA1_dZ1 = d_relu(Z1)
    dZ1_dW1 = X
    dZ1_dB1 = 1

    dC_dW2 = dC_dA2 @ dA2_dZ2 @ dZ2_dW2.T
    dC_dB2 = dC_dA2 @ dA2_dZ2 * dZ2_dB2
    dC_dA1 = dC_dA2 @ dA2_dZ2 @ dZ2_dA1
    dC_dW1 = dC_dA1 @ dA1_dZ1 @ dZ1_dW1.T
    dC_dB1 = dC_dA1 @ dA1_dZ1 * dZ1_dB1

    return dC_dW1, dC_dB1, dC_dW2, dC_dB2

def main():
    df = pd.read_csv(CSV_PATH)
    X = (df.iloc[:, :-1].values / 255.0) # scale values to between 0, 1
    y = df.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=RANDOM_SEED)
    train_count = X_train.shape[0]

    # init random weights
    w_hidden = np.random.rand(3, 3)
    w_output = np.random.rand(1, 3)

    # init random biases
    b_hidden = np.random.rand(3, 1)
    b_output = np.random.rand(1, 1)

    print('Beginning Training...')
    trainingStart = time.time()

    for _ in range(ITERATIONS):
        # select random item from training data
        index = np.random.choice(train_count, 1, replace=False)
        X_sample = X_train[index].transpose()
        y_sample = y_train[index]

        # run item through neural network
        Z1, A1, Z2, A2 = forward_propagation(X_sample, w_hidden, b_hidden, w_output, b_output)

        # distribute error through backpropagation and return slopes
        dW1, dB1, dW2, dB2 = backward_propagation(Z1, A1, Z2, A2, X_sample, y_sample, w_output)

        # update weights and biases using slopes and learning rate
        w_hidden -= LEARNING_RATE * dW1
        b_hidden -= LEARNING_RATE * dB1
        w_output -= LEARNING_RATE * dW2
        b_output -= LEARNING_RATE * dB2

    trainingTime = time.time() - trainingStart
    
    # calculate accuracy
    predictions = forward_propagation(X_test.transpose(), w_hidden, b_hidden, w_output, b_output)
    predictions = predictions[-1] # grab only A2, output
    predictions = (predictions >= 0.5).flatten().astype(int) # convert to 0,1
    comparisons = np.equal(predictions, y_test)
    accuracy = sum(comparisons.astype(int) / X_test.shape[0])
    print(f'Accuracy: {accuracy:0.3%}')

    print(f'Training time: {trainingTime:0.2f} seconds')

    colors = dc.generate_random_colors(RANDOM_COLOR_COUNT)
    scaled_colors = colors.transpose() / 255.0
    predictions = forward_propagation(scaled_colors, w_hidden, b_hidden, w_output, b_output)[-1]
    predictions = (predictions >= 0.5).flatten().astype(int)

    dc.plot_colors(colors, predictions)

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
