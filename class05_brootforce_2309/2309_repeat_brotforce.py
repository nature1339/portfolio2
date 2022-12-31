
list_nine = []

for _ in range(9):
    list_nine.append(int(input()))

two_height = sum(list_nine) - 100
answer_index = list()

for i in range(8):
    for j in range(i + 1, 9):
        if list_nine[i] + list_nine[j] == two_height:
            # [3, 6]
            answer_index.append(i)
            answer_index.append(j)

del list_nine[answer_index[1]]
del list_nine[answer_index[0]]

# Sort Algorithm

list_nine.sort()

for val in list_nine:
    print(val)
