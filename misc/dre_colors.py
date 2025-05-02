import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from numpy import ndarray


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
