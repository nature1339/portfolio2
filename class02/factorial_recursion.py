n = int(input())

# 함수를 정의할 때 미리 만들어 둔 임시 변수 = 매개변수(Parameter)
def recursion(n):
    
    result = 1
    
    if n > 0:
        result = n * recursion(n-1)   
 
    return result

# print(recursion(n)) # 호출할 때 넣어주는 값 = 인자(Argument)
print(recursion(n))
    
#무한루프, 헷갈릴수있는위험, 현업에 자주쓰이진않음, 
#복잡한 알고리즘은 재귀함수가 나음

def plus_ten(x):
    return x + 10

number = lambda x : x + 10

print(number(10))

## 함수 > 재귀함수 > 리스트 컴프리헨션 + 리스트 > 람다 함수 > Class