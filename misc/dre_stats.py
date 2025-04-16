from math import sqrt
from typing import Any

from scipy.stats import norm


MINIMUM_SAMPLE_SIZE = 31

# "a p-value of 0.05 or less is traditionally considered statistically significant" 
# Source: "Essential Math for Data Science" https://learning.oreilly.com/library/view/essential-math-for/9781098102920
P_THRESHOLD = 0.05

def calc_mean(values: list[float]) -> float:
    mean = sum(values) / len(values)
    return mean

def calc_variance(values: list[float], is_sample: bool) -> float:
    mean = calc_mean(values)
    sum_square_errors = sum((v - mean) ** 2 for v in values) 
    variance = sum_square_errors / (len(values) - (1 if is_sample else 0))
    return variance

def calc_standard_deviation(values: list[float], is_sample: bool) -> float:
    stdev = sqrt(calc_variance(values, is_sample))
    return stdev

def calc_range_probability(low: float, high: float, mean: float, std_dev: float ) -> Any:
    high_cdf = norm.cdf(high, mean, std_dev)
    low_cdf = norm.cdf(low, mean, std_dev)
    return high_cdf - low_cdf

def calc_critical_z_value(prob: float) -> tuple[float, float]:
    left_tail_area: float = (1.0 - prob) / 2.0
    upper_area: float = 1.0 - left_tail_area

    norm_dist = norm(loc=0.0, scale=1.0)
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)

def calc_confidence_interval(prob: float, sample_mean: float, sample_std: float, sample_size: int) -> tuple[float, float]:
    if sample_size < MINIMUM_SAMPLE_SIZE:
        raise Exception(f'Sample size must be {MINIMUM_SAMPLE_SIZE} or more')
    
    lower_z, upper_z = calc_critical_z_value(prob)
    lower_ci: float = lower_z * (sample_std / sqrt(sample_size))
    upper_ci: float = upper_z * (sample_std / sqrt(sample_size))
    return sample_mean + lower_ci, sample_mean + upper_ci

# TODO AEO move to tests! (and create additional)
def main() -> None:
    # Number of pets each person owns
    data: list[float] = [0, 1, 5, 7, 9, 10, 14]
    print(f'Mean: {calc_mean(data):0.3f}') # 6.571
    print(f'Sample Variance: {calc_variance(data, True):0.3f}') # 24.952
    print(f'Sample Std. Dev.: {calc_standard_deviation(data, True):0.3f}') # 4.995

if __name__ == '__main__':
    print('\n----\n')
    main()
    print('\n----\n')