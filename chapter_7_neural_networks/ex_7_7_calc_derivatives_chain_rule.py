from sympy import symbols, diff, exp
import misc.dre_helper as dh

class DerivativeCalcs:

    def __init__(self) -> None:
        self.dC_dA2= None
        self.dA2_dZ2 = None
        self.dZ2_dW2 = None

    def _calc_cost_function_wrt_A2_diff(self):
        # cost = squared error (prediction vs actual)
        A2, Y = symbols('A2, Y')
        C = (A2 - Y)**2
        self.dC_dA2 = diff(C, A2)
        print('Derivative of Cost Function wrt A2:', self.dC_dA2)

    def _calc_A2_wrt_Z2_diff(self):
        Z2 = symbols('Z2')

        logistic = lambda x: 1 / (1 + exp(-x)) # type: ignore

        A2 = logistic(Z2)
        self.dA2_dZ2 = diff(A2, Z2)
        print('Derivative of A2 wrt Z2 Function:', self.dA2_dZ2)

    def _calc_Z2_wrt_W2_diff(self):
        A1, W2, B2 = symbols('A1, W2, B2')
        Z2 = A1 * W2 + B2
        self.dZ2_dW2 = diff(Z2, W2)
        print('Derivative of Z2 wrt W2 Function:', self.dZ2_dW2)

    def calc_derivatives(self):
        self._calc_cost_function_wrt_A2_diff()
        self._calc_A2_wrt_Z2_diff()
        self._calc_Z2_wrt_W2_diff()
        print('Derivative of C wrt W2:', self.dZ2_dW2 * self.dA2_dZ2 * self.dC_dA2  ) # type: ignore

def main():
    dh.print_separator()
    calcs = DerivativeCalcs()
    calcs.calc_derivatives()
    dh.print_separator()

if __name__ == '__main__':
    main()
