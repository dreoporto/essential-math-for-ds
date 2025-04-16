from scipy.stats import binom

def calc_binomial_distribution(prob:float, num:int = 10):

    # num = 10    # number of attempts
    cumulative = 0.0

    print(f'\nUNDERLYING PROBABILITY: {prob}\n')
    print('NUM\tCUMLTV\t\tLIKELIHOOD')

    for k in range(num + 1):
        likelihood = binom.pmf(k, num, prob)
        cumulative += likelihood
        print(f'{k}\t{cumulative:0.4f}\t\t({likelihood})')

def main():
    print('\n----\n')

    # calc_binomial_distribution(0.5)
    # calc_binomial_distribution(0.9)
    calc_binomial_distribution(0.6, 137)

    print('\n----\n')

if __name__ == '__main__':
    main()
