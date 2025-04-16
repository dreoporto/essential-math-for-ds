import numpy_financial as npf

def irr_fun():
    result = npf.irr([-500, 50, 31, 3, 11])
    print('IRR 1 = ', result)

    result = npf.irr([-250_000, 100_000, 150_000, 200_000, 250_000, 300_000])
    print('IRR 2 = ', result)

def main():
    irr_fun()

if __name__ == '__main__':
    print('\n----\n')
    main()
    print('\n----\n')
