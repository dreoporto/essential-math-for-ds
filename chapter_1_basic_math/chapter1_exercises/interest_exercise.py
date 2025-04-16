"""perform interest calcs using limits"""
from sympy import symbols, limit, oo

def simple_interest_calc(n:int = 12):
    """ 
    do a simple interest calc using no libraries
    :param n: number of compounding periods per year
    """
    # EXAMPLE:
    # COMPOUND ANNUALLY:    (0.5 + 1)**3 * 1000 =           $1,157.63
    # COMPOUND MONTHLY:     (.05 / 12 + 1)**36 * 1000 =     $1,161.47 (+$3.84)
    principal = 1000
    rate = 0.05
    years = 3
    periods = years * n # compound monthly

    loan_worth = (rate / n + 1)**periods * principal

    print(f"loan is worth: ${loan_worth:.2f}\t(n={n})")

def continuous_interest_calc():
    """do a continuous interest calc using..."""
    # EXAMPLE:
    # (.05 / n + 1)**3n * 1000

    principal = 1000
    rate = 0.05
    years = 3

    n = symbols('n')
    f = (rate / n + 1)**(years*n) * principal
    result = limit(f, n, oo)

    print('limit result:', result)
    print(f'loan is worth: ${result.evalf():.2f}\t(n=oo)')

def main():
    """call other functions here"""
    print("\n----\n")

    simple_interest_calc(1)
    simple_interest_calc()
    simple_interest_calc(100)
    simple_interest_calc(1000)
    continuous_interest_calc()

    print("\n----\n")

if __name__ == '__main__':
    main()
