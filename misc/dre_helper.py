
def print_separator(description: str = '') -> None:
    if str == '':
        print('\n----\n')
    else:
        print(f'\n---- {description}\n')

def verifyCalc(calc, expectedValue):
    """
    Use assertion to verify calculation
    - failure outputs expected vs actual in readable format
    """
    calcString = str(calc)
    assert calcString == expectedValue, f'\n  expected: {expectedValue};\n  actual:   {calcString}'
