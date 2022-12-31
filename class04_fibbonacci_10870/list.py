
# Python Object Oriented Language
# Class -> Object
# List Copy > Shallow Copy / Deep Copy

import copy

a = [[0, 0], [0, 0]]
b = copy.deepcopy(a)

b[1][0] = 777

print(id(a))
print(id(a[0]))
print(id(a[1]))

print(id(a[0][0]))
print(id(a[1][0]))

print(a)
print(b)