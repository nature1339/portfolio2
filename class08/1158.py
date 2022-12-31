
# 모듈
# > 외부에 있는 코드 뭉치 > 임포트 해와서 코드에 적용

from collections import deque

answer = []
num_list = deque()

n, k = map(int, input().split())

for i in range(1, n+1):
    num_list.append(i)

# num_list 안에 값이 사라질때까지 반복!
while num_list:
    for _ in range(k-1):
        num_list.append(num_list.popleft())
    answer.append(num_list.popleft())
        
print("<", end="")

for i in range(len(answer) - 1):
    # 문자열 포매팅
    print("%d, " % answer[i], end = "")
    # print("{}, ".format())
    # print(f"{}")

print(answer[-1], end = "")
print(">")