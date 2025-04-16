# import numpy as np
from numpy import array

def python_vector():
    v = [3, 2]
    print(v)
    print('type:', type(v))

def numpy_vector():
    v = array([4, 1, 2])
    print(v)
    print('type:', type(v))

def add_vectors():
    v = array ([3, 2])
    w = array([2, -1])

    v_plus_w = v + w

    print(v_plus_w)

def scale_vector():
    v = array([3, 1])
    scaled_v = 2 * v
    print(scaled_v)

def main():
    # python_vector()
    # numpy_vector()
    # add_vectors()
    scale_vector()

if __name__ == '__main__':
    main()
