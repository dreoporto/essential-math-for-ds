from sympy import Matrix

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

A = Matrix([
    [4, 2, 4],
    [5, 3, 7],
    [9, 3, 6]
])

B = Matrix([
    44,
    56,
    72
])

# dot product between A and its inverse
# will produce identity function
inverse = A.inv()
identity = inverse * A

# A * X = B
# solve for X
# X = 1/A * B
X = A.inv() * B

print ('\n----\n')

print(f'INVERSE:\t{inverse}')
print('EXPECTED:\tMatrix([[-1/2, 0, 1/3], [11/2, -2, -4/3], [-2, 1, 1/3]])\n')

print(f'IDENITITY:\t{identity}')
print('EXPECTED:\tMatrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])\n')

print(f'SOLVED X:\t{X}')
print('EXPECTED:\tMatrix([[2], [34], [-8]])\n')

print ('\n----\n')
