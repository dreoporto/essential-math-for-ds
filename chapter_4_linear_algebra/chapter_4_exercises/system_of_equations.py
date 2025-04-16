from sympy import Matrix

A = Matrix([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])

B = Matrix([
    54,
    12,
    6
])

# A * X = B
# X = B * 1/A

X = A.inv() * B

print(X)    # Matrix([[99/5], [-27/5], [-6]])
print(3 * 99/5 + 1 * -27/5 + 0 * -6)    # 54
print(2 * 99/5 + 4 * -27/5 + 1 * -6)    # 12
print(3 * 99/5 + 1 * -27/5 + 8 * -6)    # 6
print(99/5)     # 19.8
print(-27/5)    # -5.4
