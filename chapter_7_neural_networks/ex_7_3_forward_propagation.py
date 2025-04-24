import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import misc.dre_helper as dh

CSV_PATH = './chapter_7_neural_networks/data/light_dark_font_training_set.csv'
RANDOM_SEED = 42

# create activation and output functions
relu = lambda x: np.maximum(x, 0)
logistic = lambda x: 1 / (1 + np.exp(-x))

def forward_propagation(X, w_hidden, b_hidden, w_output, b_output):
    # uses @ for matrix multiplication
    # Z: unactivated output
    # A: activated output
    Z1 = w_hidden @ X + b_hidden
    A1 = relu(Z1) # hidden layer result
    Z2 = w_output @ A1 + b_output
    A2 = logistic(Z2) # output layer result
    return Z1, A1, Z2, A2

def main():

    # creates an untrained neural network (unoptimized weights & biases)
    
    df = pd.read_csv(CSV_PATH)

    X = (df.iloc[:, :-1].values / 255.0) # scale values to between 0, 1
    y = df.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=RANDOM_SEED)

    # init random weights
    w_hidden = np.random.rand(3, 3)
    w_output = np.random.rand(1, 3)

    # init random biases
    b_hidden = np.random.rand(3, 1)
    b_output = np.random.rand(1, 1)

    predictions = forward_propagation(X_test.transpose(), w_hidden, b_hidden, w_output, b_output)
    predictions = predictions[-1] # grab only A2, output
    predictions = (predictions >= .5).flatten().astype(int) # convert to 0,1
    comparisons = np.equal(predictions, y_test)
    accuracy = sum(comparisons.astype(int) / X_test.shape[0])

    dh.print_separator()
    print(f'Accuracy: {accuracy:0.4f}')
    dh.print_separator()

if __name__ == '__main__':
    main()
