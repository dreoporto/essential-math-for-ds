from scipy.stats import norm
import misc.dre_stats as dst

def calc_pets() -> None:
    # Number of pets each person owns
    data: list[float] = [0, 1, 5, 7, 9, 10, 14]

    print('\n-- CALC PETS --\n')
    print(f'Mean:\t\t{dst.calc_mean(data):0.3f}') # 6.571
    print(f'Sample Var:\t{dst.calc_variance(data, True):0.3f}') # 24.952
    print(f'Smp Std Dev:\t{dst.calc_standard_deviation(data, True):0.3f}') # 4.995    

def calc_mean_etc() -> None:

    """
    You bought a spool of 1.75 mm filament for your 3D printer. You want to measure how close the filament diameter really is to 1.75 mm. You use a caliper tool and sample the diameter five times on the spool:

    1.78, 1.75, 1.72, 1.74, 1.77

    Calculate the mean and standard deviation for this set of values.
    """

    values = [1.78, 1.75, 1.72, 1.74, 1.77]
    print('\n-- CALC MEAN ETC --\n')
    print(f'Mean:\t\t{dst.calc_mean(values)}')
    print(f'Smp Std Dev:\t{dst.calc_standard_deviation(values, is_sample=False):0.5f}')

def calc_phone_probability() -> None:

    """
    A manufacturer says the Z-Phone smart phone has a mean consumer life of 42 months with a standard deviation of 8 months. Assuming a normal distribution, what is the probability a given random Z-Phone will last between 20 and 30 months?
    """

    probability = dst.calc_range_probability(20, 30, 42, 8)
    print('\n-- PHONE RANGE PROBABILITY --\n')
    print(f'{probability:0.5f}')

def calc_confidence_interval() -> None:

    """
    I am skeptical that my 3D printer filament is not 1.75 mm in average diameter as advertised. I sampled 34 measurements with my tool. The sample mean is 1.715588 and the sample standard deviation is 0.029252.

    What is the 99% confidence interval for the mean of my entire spool of filament?
    """
    
    lower, upper = dst.calc_confidence_interval(0.99, 1.715588, 0.029252, 34)
    print('\n-- CONFIDENCE INTERVAL --\n')
    print(f'{lower},\n{upper}')

def calc_two_tailed_hypothesis_test() -> None:
    
    """
    Your marketing department has started a new advertising campaign and wants to know if it affected sales, which in the past averaged $10,345 a day with a standard deviation of $552. The new advertising campaign ran for 45 days and averaged $11,641 in sales.

    Did the campaign affect sales? Why or why not? (Use a two-tailed test for more reliable significance.)
    """    
    mean = 10345
    std_dev = 552
    p_value = 1.0 - norm.cdf(11641, mean, std_dev)
    p_value *= 2 # moved the needle on either side ("affect sales")
    print('\n -- TWO-TAILED TEST--\n')
    print(f'p_value:\t{p_value:0.6f}')
    print(f'Is Significant:\t{p_value < dst.P_THRESHOLD}')

def main() -> None:
    # calc_pets()
    calc_mean_etc()
    calc_phone_probability()
    calc_confidence_interval()
    calc_two_tailed_hypothesis_test()

if __name__ == '__main__':
    main()
    print('\n----\n')
