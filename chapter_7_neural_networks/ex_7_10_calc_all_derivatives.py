from sympy import symbols, diff, exp
import misc.dre_helper as dh

def main():

    # W=weight; B=bias; A=activation; Z=unactivated; X=input; Y=output
    W1, W2, B1, B2, A1, A2, Z1, Z2, X, Y = symbols('W1 W2 B1 B2 A1 A2 Z1 Z2 X Y')

    # calc derivative (d) of cost function C with respect to (wrt) A2
    C = (A2 - Y)**2
    dC_dA2 = diff(C, A2)
    print(f'{ dC_dA2 = }')
    dh.verifyCalc(dC_dA2, '2*A2 - 2*Y')

    # calc d of A2 wrt Z2
    logistic = lambda x: 1 / (1 + exp(-x)) # type: ignore
    fA2 = logistic(Z2)
    dA2_dZ2 = diff(fA2, Z2)
    print(f'{dA2_dZ2 = }')
    dh.verifyCalc(dA2_dZ2, 'exp(-Z2)/(1 + exp(-Z2))**2')

    # calc d of Z2 wrt A1
    fZ2 = A1 * W2 + B2
    dZ2_dA1 = diff(fZ2, A1)
    print(f'{dZ2_dA1 = }')
    dh.verifyCalc(dZ2_dA1, 'W2')

    # calc d of Z2 wrt W2
    dZ2_dW2 = diff(fZ2, W2)
    print(f'{dZ2_dW2 = }')
    dh.verifyCalc(dZ2_dW2, 'A1')

    # calc d of Z2 wrt B2
    dZ2_dB2 = diff(fZ2, B2)
    print(f'{dZ2_dB2 = }')
    dh.verifyCalc(dZ2_dB2, '1')

    # calc d of A1 wrt Z1
    # relu = lambda x: Max(x, 0)  # NOT USED
    # fA1 = relu(Z1)  # NOT USED
    d_relu = lambda x: x > 0 # slope is 1 if positive, 0 if negative
    dA1_dZ1 = d_relu(Z1)
    print(f'{dA1_dZ1 = }')
    dh.verifyCalc(dA1_dZ1, 'Z1 > 0')

    # calc d of Z1 wrt W1
    fZ1 = X * W1 + B1
    dZ1_dW1 = diff(fZ1, W1)
    print(f'{dZ1_dW1 = }')
    dh.verifyCalc(dZ1_dW1, 'X')

    # calc d of Z1 wrt B1
    dZ1_dB1 = diff(fZ1, B1)
    print(f'{dZ1_dB1 = }')
    dh.verifyCalc(dZ1_dB1, '1')

if __name__ == '__main__':
    dh.print_separator()
    main()
    dh.print_separator()
