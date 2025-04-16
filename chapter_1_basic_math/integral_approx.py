"""integral approximation"""

def approximate_integral(a, b, n, f):
    """calculates approximate integrals"""
    delta_x = (b - a) / n
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)

    return total_sum * delta_x

def my_function(x):
    """function we want to calc for"""
    return x**2 + 1

def show_approximation(rectangles:int) -> None:
    """print result of approx calc"""
    area = approximate_integral(a=0, b=1, n=rectangles, f=my_function)
    print(f'area n={rectangles:,}: {area}')

def main() -> None:
    """some example calcs"""
    print('\n----\n')

    show_approximation(5)
    show_approximation(1000)
    show_approximation(1_000_000)
    # show_approximation('xyz') # testing type checking

    print('\n----\n')

if __name__ == '__main__':
    main()
