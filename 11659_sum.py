# 입력한 문자열을 잘라서, 원하는 자료형으로 맵핑.
N, M = map(int, input().split())

list_N = list(map(int, input().split()))
# [1, 2, 3, 4, 5]
# 2 5 > 1 - 4
sum_number = [0] # [0, 1, 3, 6, 10, 15]
temp = 0 # 0 1 3 6

for i in list_N:
    temp = temp + i
    sum_number.append(temp)

for _ in range(M):
    x, y = map(int, input().split())
    print(sum_number[y] - sum_number[x-1])

    
# i 의 값이 없음.
#list[sum_number[i]] = list(map(int, sum_number[i].split()))

# 1 2 3 4 5

# 1 1+2 1+2+3  1+2+3+4  1+2+3+4+5

# sum_number += list_N[i]
# sum_number = sum_number + list_N[i]

# i    list[0]
# 0   1     list[i]=+ sum_number
# 1   1+2   list[i]=+ sum_number
# 2   1+2+3  list[i]=+ sum_number

# sum_number[0]  sum_number[1]   sum_number[2]





# for _ in range(M):
#     x, y = map(int, input().split())

#     sum_number = 0
    
#     for i in range(0, y):
#         sum_number += list_N[i]

#     print(sum_number)