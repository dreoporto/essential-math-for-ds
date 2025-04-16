from typing import Any
from numpy import dtype, ndarray
from scipy.stats import norm

# cold has 18 day mean recovery, 1.5 std dev
mean = 18
std_dev = 1.5

# "a p-value of 0.05 or less is traditionally considered statistically significant"
p_threshold = 0.05

def calc_recovery_probability() -> None:

    # 95% probability recovery time takes between 15 and 21 days
    high = norm.cdf(21, mean, std_dev)
    low = norm.cdf(15, mean, std_dev)

    print('high:\t', high)
    print('low:\t', low)
    print('prob:\t', high - low)

def calc_x_value() -> None:

    # what x-value has p% of area behind it?
    x_value = norm.ppf(p_threshold, mean, std_dev)

    print('x_value:', x_value)

def calc_p_value(x_value: float) -> None:
    
    # probability of x or less days
    p_value = norm.cdf(x_value, mean, std_dev)
    print(f'p_value: {p_value} (x={x_value})') # 0.09 exceeds p_threshold; NOT statistically significant

def calc_two_tail_x_values() -> None:

    p2: float = p_threshold / 2

    # what x-value has p% of area behind it?
    x1 = norm.ppf(p2, mean, std_dev)

    # what x-value has 1.0-p% of area behind it?    
    x2 = norm.ppf(1.0 - p2, mean, std_dev)

    print(f'tt_x1:\t {x1:.3f}')
    print(f'tt_x2:\t {x2:.3f}')

def calc_two_tail_p_value(x_value: float) -> None:
    
    # probability of x or less days
    p1 = norm.cdf(x_value, mean, std_dev)

    # probability of x2 or more days
    x2_value = mean + (mean - x_value)
    p2 = 1 - norm.cdf(x2_value, mean, std_dev)

    # p-value of both tails
    p_value = p1 + p2
    print(f'tt_p_v:\t {p_value:.4f} (x={x_value})')

def main() -> None:
    print('\n----\n')
    calc_recovery_probability()
    calc_x_value()
    calc_p_value(16)
    calc_p_value(15.5)
    calc_p_value(15)
    calc_two_tail_x_values()
    calc_two_tail_p_value(16)
    calc_two_tail_p_value(15)
    calc_two_tail_p_value(14.5)
    print('\n----\n')

if __name__ == '__main__':
    main()
