from sympy import symbols, diff, exp
import misc.dre_helper as dh

def calc_cost_function_wrt_A2_diff():
    # cost = squared error (prediction vs actual)
    A2, Y = symbols('A2, Y')
    C = (A2 - Y)**2
    dC_dA2 = diff(C, A2)
    print('Derivative of Cost Function:', dC_dA2)

def calc_A2_wrt_Z2_diff():
    Z2 = symbols('Z2')

    logistic = lambda x: 1 / (1 + exp(-x)) # type: ignore

    A2 = logistic(Z2)
    dA2_dZ2 = diff(A2, Z2)
    print('Derivative of A2 wrt Z2 Function:', dA2_dZ2)

def calc_Z2_wrt_W2_diff():
    A1, W2, B2 = symbols('A1, W2, B2')
    Z2 = A1 * W2 + B2
    dZ2_dW2 = diff(Z2, W2)
    print('Derivative of Z2 wrt W2 Function:', dZ2_dW2)

def main():
    dh.print_separator()
    calc_cost_function_wrt_A2_diff()
    calc_A2_wrt_Z2_diff()
    calc_Z2_wrt_W2_diff()
    dh.print_separator()

if __name__ == '__main__':
    main()
