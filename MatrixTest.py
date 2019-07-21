from Matrix import Matrix

m = Matrix(2, 3)

m.set_values([[5, 2, 8], [4, 9, 1]])

m2 = Matrix(3, 4)

m2.set_values([[1, 2, 3, 4], [1, 1, 1, 1], [2, 1, 3, 1]])

m3 = Matrix (2, 3)

m3.set_values([[1, 0, 1], [0, 1, 0]])

print (m.matrix)
print()
print()
print (m2.matrix)
print()
print()
print (m.multiply(m2).matrix)
print()
print()

print (m.matrix)
print()
print()
print (m3.matrix)
print()
print()
print (m.subtract(m3).matrix)

