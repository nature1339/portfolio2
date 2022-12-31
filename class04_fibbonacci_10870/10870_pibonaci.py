n = int(input())


# 3
def fib(n):
    if n <= 1:
        return n
    
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    
    # 2  1
    return fib(n-1) + fib(n-2)
    

print(fib(n))