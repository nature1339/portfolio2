
# List
# Array vs List

a = [10, 20, 30]
b = [40, 50, 60]

a.append(500)

a.extend(b)

a.insert(2, 10000)

del a[2]

a.remove(500)

a.pop()

for i in a:
    print(i)

print()

for i in range(len(a)):
    print(a[i])


for index, value in enumerate(a):
    print(index, value)

print(max(a))
print(min(a))
print(sum(a))
