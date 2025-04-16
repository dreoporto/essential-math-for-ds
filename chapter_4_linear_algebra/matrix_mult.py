from numpy import array

def combine_transformations():

    # Transformation 1
    i_hat_t1 = array([0, 1])
    j_hat_t1 = array([-1, 0])
    transform1 = array([i_hat_t1, j_hat_t1]).transpose()

    # Transformation 2
    i_hat_t2 = array([1, 0])
    j_hat_t2 = array([1, 1])
    transform2 = array([i_hat_t2, j_hat_t2]).transpose()

    # Combine Transformations
    combined = transform2 @ transform1

    # Test
    print(f'COMBINED MATRIX:\n{combined}\n')

    v = array([1, 2])
    print('RESULT:', combined.dot(v))  # [-1, 1]

def main():
    print('\n----\n')
    combine_transformations()
    print('\n----\n')

if __name__ == '__main__':
    main()
