
# 재귀 함수 : 함수 내부에서 함수 자기 자신을 다시 호출하는 함수.
# Recursive Function
# 무한 루프 현상이 발생할 수 있다.

def hello(num):
    
    print(num)
    
    num -= 1
    
    # 재귀함수의 종료 시점(조건) : 기저 사례(Base Case)
    if num < 0: 
        return
    
    hello(num)

hello(5)

# 일단, 반복문으로 구현한 후에, 재귀함수로 구현.