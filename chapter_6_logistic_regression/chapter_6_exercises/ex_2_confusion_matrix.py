import random

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from numpy import ndarray
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, f1_score, precision_score,
                             recall_score)
from sklearn.model_selection import train_test_split

import misc.dre_helper as dh

CSV_PATH = './chapter_6_logistic_regression/data/light_dark_font_training_set.csv'
RANDOM_SEED = 42
RANDOM_COLOR_COUNT = 10

def generate_random_colors(count: int) -> ndarray:
    colors = []
    for _ in range (0, count):
        rgb_values = generate_random_color()
        colors.append(rgb_values)
    colors = np.array(colors)
    return colors

def generate_random_color() -> ndarray:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    result = np.array([r, g, b])
    return result

def plot_colors(colors: ndarray, background: ndarray) -> None:

    count = len(colors)
    _, axes = plt.subplots(figsize=(5, count))

    axes.set_xlim(0, 1)
    axes.set_ylim(0, count)
    axes.axis('off')

    for i in range(count):
        background_color = colors[i] / 255 # scale to values between 0 and 1
        font_color = 'black' if background[i] == 1 else 'white'
        axes.add_patch(Rectangle((0, i), 1, 1, color=background_color))
        axes.text(0.5, i + 0.5, f'Random Color {i+1} {colors[i]}', ha='center', va='center', color=font_color, fontsize=10)

    plt.show()

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

    colors = generate_random_colors(RANDOM_COLOR_COUNT)
    dh.print_separator('RANDOM BACKGROUNDS')
    print(colors)

    prediction = model.predict(colors)
    dh.print_separator('PREDICTED FONT COLORS')
    print(prediction)

    # expand PREDICTION to match SHAPE of COLORS using np.newaxis
    combined = np.concatenate((colors, prediction[:, np.newaxis]), axis=1)
    dh.print_separator('COMBINED')
    print(combined)

    plot_colors(colors, prediction)

if __name__ == '__main__':
    main()
