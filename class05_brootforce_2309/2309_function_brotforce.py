
list_nine = []

for _ in range(9):
    list_nine.append(int(input()))

two_height = sum(list_nine) - 100
answer_index = list()

def check_answer_index():
    temp_list = list()
    
    for i in range(8):
        for j in range(i + 1, 9):
            if list_nine[i] + list_nine[j] == two_height:
                # [3, 6]
                temp_list.append(i)
                temp_list.append(j)
            
    return temp_list

answer_index = check_answer_index()

del list_nine[answer_index[1]]
del list_nine[answer_index[0]]

# Sort Algorithm

list_nine.sort()

for val in list_nine:
    print(val)

