from math import sqrt

def calc_variance(values: list[int]) -> float:
    mean: float = sum(values) / len(values)
    my_variance: float = sum((v - mean) ** 2 for v in values) / len(values)
    return my_variance

def calc_standard_deviation(values: list[int]) -> float:
    return sqrt(calc_variance(values))

def main() -> None:
    # Number of pets each person owns
    data: list[int] = [0, 1, 5, 7, 9, 10, 14]
    print(f'Std. Dev.: {calc_standard_deviation(data):0.2f}') # prints 4.62

if __name__ == '__main__':
    print('\n----\n')
    main()
    print('\n----\n')
