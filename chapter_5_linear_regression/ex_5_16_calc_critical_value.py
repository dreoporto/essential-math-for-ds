# Example 5-16. Calculating the critical value from a T-distribution

from scipy.stats import t
import misc.dre_helper as dh

def main():

    n = 10
    lower_cv = t(n-1).ppf(0.025)
    upper_cv = t(n-1).ppf(0.975)

    # -2.262157162740992 2.2621571627409915
    dh.print_separator('CRITICAL VALUE')
    print(lower_cv, upper_cv)
    dh.print_separator()

if __name__ == '__main__':
    main()
