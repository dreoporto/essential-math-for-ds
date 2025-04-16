from math import sqrt
from scipy.stats import norm

MINIMUM_SAMPLE_SIZE = 31

def critical_z_value(prob: float) -> tuple[float, float]:
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area: float = (1.0 - prob) / 2.0
    upper_area: float = 1.0 - left_tail_area
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)

def confidence_interval(prob: float, sample_mean: float, sample_std: float, sample_size: int) -> tuple[float, float]:
    if sample_size < MINIMUM_SAMPLE_SIZE:
        raise Exception(f'Sample size must be {MINIMUM_SAMPLE_SIZE} or more')
    
    lower_z, upper_z = critical_z_value(prob)
    lower_ci: float = lower_z * (sample_std / sqrt(sample_size))
    upper_ci: float = upper_z * (sample_std / sqrt(sample_size))
    return sample_mean + lower_ci, sample_mean + upper_ci

def main() -> None:
    print('\n----\n')

    print('CRITICAL Z VALUE')
    lower_z, upper_z = critical_z_value(prob=0.95)
    print(f'{lower_z},\n {upper_z}')
    print('\n')

    print('CONFIDENCE INTERVAL')
    lower, upper = confidence_interval(prob=0.95, sample_mean=64.408, sample_std=2.05, sample_size=31)
    print(f'{lower},\n{upper}')

    print('\n----\n')

if __name__ == '__main__':
    main()
