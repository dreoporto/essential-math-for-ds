from numpy import array, diag
from numpy.linalg import eig, inv

def calc_eigendecomposition():

    values_matrix = array([
        [1, 2],
        [4, 5]
    ])

    eigenvals, eigenvecs = eig(values_matrix)

    print('VALUES MATRIX')
    print(values_matrix)

    print('\nEIGENVALUES')
    print(eigenvals)

    print('\nEIGENVECTORS')
    print(eigenvecs)

    print('\nREBUILD MATRIX')

    # Reconstruct A:
    # A = Q∧Q-1
    # A = EVec * DiEVal * EVec**-1

    rebuilt_matrix = eigenvecs @ diag(eigenvals) @ inv(eigenvecs)

    print(rebuilt_matrix)

def main():
    print('\n----\n')
    calc_eigendecomposition()
    print('\n----\n')

if __name__ == '__main__':
    main()
