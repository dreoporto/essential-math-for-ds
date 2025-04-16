from collections import defaultdict

def calculate_mean() -> None:
    sample: list[int] = [1, 3, 2, 5, 7, 0, 2, 3]
    mean: float = sum(sample) / len(sample)
    print('Mean:', mean) # prints 2.875

def calc_weighted_mean() -> None:
    sample: list[int] = [90, 80, 63, 87]
    weights: list[float] = [.20, .20, .20, .40]

    weighted_mean: float = sum(s * w for s, w in zip(sample, weights)) / sum(weights)
    print('Weighted Mean:', weighted_mean) # prints 81.4

def calc_median(sample: list[float]) -> None:
 
    ordered: list[float] = sorted(sample)
    n: int = len(ordered)
    median:float = 0

    if n % 2 == 0:
        midpoint: int = int(n / 2) - 1
        median = (ordered[midpoint] + ordered[midpoint + 1]) / 2.0
    else:
        midpoint = int(n / 2)
        median = ordered[midpoint]

    print(f'Median: {median:0.1f}')

def calc_mode() -> None:

    values: list[int] = [1, 3, 2, 5, 7, 0, 2, 3]

    counts = defaultdict(lambda: 0)

    for s in values:
        counts[s] += 1

    max_count: int = max(counts.values())
    modes: list[int] = [v for v in set(values) if counts[v] == max_count]

    print('Mode(s):', modes) # prints [2, 3]

def main() -> None:
    print('\n----\n')
    calculate_mean()
    calc_weighted_mean()
    calc_median([0, 1, 5, 7, 9, 10, 14]) # prints 7.0
    calc_median([0, 1, 5, 7, 9, 10]) # prints 6.0
    calc_mode()
    print('\n----\n')

if __name__ == '__main__':
    main()
