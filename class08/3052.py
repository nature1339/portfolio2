num_list = []

for _ in range(10):
    num_list.append(int(input()))

answer_list = []

for i in num_list:
    temp = i % 42
    if not (temp in answer_list):
        answer_list.append(temp)

print(len(answer_list))