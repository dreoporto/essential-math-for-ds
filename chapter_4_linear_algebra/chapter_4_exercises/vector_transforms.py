from numpy import array

def calc_new_vector(i_hat: list[float], j_hat: list[float], v: list[float]):

    basis = array([i_hat, j_hat]).transpose()
    new_v = basis.dot(v)
    print(new_v)

def main():
    print('\n----\n')
    calc_new_vector([2, 0], [0, 1.5], [1, 2])   # [2. 3.]
    calc_new_vector([-2, 1], [1, -2], [1, 2])   # [ 0 -3]
    print('\n----\n')

if __name__ == '__main__':
    main()
