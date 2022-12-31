n = int(input())

# 누적곱 배열
# 1 2 3 4 5 6 .... 12
n_list = [1]

fac = 1

# n = 5
for i in range(2, n + 1):
    fac = fac * i
    n_list.append(fac) # [ 1, 2, 6, 24, 120]
    

result = 1

if n > 0:
    for i in range(1, n+1):
        result *= i


print(n_list[n-1])
   
