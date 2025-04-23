import matplotlib.pyplot as plt
from sympy import Max, exp, plot, symbols


def plot_relu():
    """
    can be used for activation layer
    """
    x = symbols('x')
    relu = Max(0, x) # convert negative numbers to 0
    plot(relu)

def plot_logistic():
    """
    can be used for output layer
    """
    x = symbols('x')
    logistic = 1 / (1 + exp(-x)) # type: ignore
    plot(logistic)

def main():
    plt.style.use('ggplot')
    plot_relu()
    plot_logistic()

if __name__ == '__main__':
    main()
