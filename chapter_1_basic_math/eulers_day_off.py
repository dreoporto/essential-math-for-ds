
from math import exp
from math import log

def calc_continuous_interest():

    principal:int = 100
    interest_rate:float = 0.2
    time_years:float = 2.0

    # exp returns e (euler) to the power of x
    balance:float = principal * exp(interest_rate * time_years)
    print(f'balance:\t{balance:5.3f}')

def approximate_euler():

    exponent:int = 100_000_000
    approx_e = (1 + 1 / exponent) ** exponent
    print(f'approx e: \t{approx_e}')

if __name__ == '__main__':

    print('\n=======\n')

    calc_continuous_interest()
    euler:float = exp(1)
    print(f'e:\t\t{euler}')
    approximate_euler()
    print(f'log(euler):\t{log(euler)}')
    print(f'log(100):\t{log(100)}')
    print(f'log(100, 10):\t{log(100, 10)}')

    print('\n=======\n')
