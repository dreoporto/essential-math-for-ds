from scipy.stats import beta

def calc_beta_dist(successes:int, failures:int, underlying_probability:float = 0.9) -> None:

    probability = beta.cdf(underlying_probability, successes, failures)

    print(f'\nSuccesses: {successes}; Failures: {failures}')
    print(f'Chance the underlying probability of success is {underlying_probability:} or LESS: {probability:0.4f}')
    print(f'Chance the underlying probability of success is {underlying_probability:} or MORE: {1.0 - probability:0.4f}')

def main():
    print('\n----\n')

    calc_beta_dist(8, 2)
    calc_beta_dist(30, 6)
    # calc_beta_dist(8, 1)
    calc_beta_dist(30, 2)

    print('\n----\n')

if __name__ == '__main__':
    main()
