from math import sqrt

def calc_mean(values: list[int]) -> float:
    return sum(values) / len(values)

def calc_variance(values: list[int], is_sample: bool) -> float:
    mean: float = calc_mean(values)
    my_variance: float = sum((v - mean) ** 2 for v in values) / (len(values) - (1 if is_sample else 0))
    return my_variance

def calc_standard_deviation(values: list[int], is_sample: bool) -> float:
    return sqrt(calc_variance(values, is_sample))

def main() -> None:
    # Number of pets each person owns
    data: list[int] = [0, 1, 5, 7, 9, 10, 14]
    print(f'Mean: {calc_mean(data):0.3f}') # 6.571
    print(f'Sample Variance: {calc_variance(data, True):0.3f}') # 24.952
    print(f'Sample Std. Dev.: {calc_standard_deviation(data, True):0.3f}') # 4.995

if __name__ == '__main__':
    print('\n----\n')
    main()
    print('\n----\n')
