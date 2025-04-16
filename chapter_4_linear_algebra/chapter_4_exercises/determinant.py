from numpy.linalg import det
from numpy import array

def calc_determinant(i: list[float], j: list[float]):

    i_hat = array(i)
    j_hat = array(j)

    basis = array([i_hat, j_hat]).transpose()

    determinant = det(basis)

    linear_warning = '(LINEAR DEPENDENCE)' if determinant == 0 else ''

    print(f'{determinant:0.1f} {linear_warning}')

def main():

    print('\n----\n')
    calc_determinant([1, 0], [2, 2])    # 2.0
    calc_determinant([2, 1], [6, 3])    # 0.0 (LINEAR DEPENDENCE)
    print('\n----\n')

if __name__ == '__main__':
    main()
