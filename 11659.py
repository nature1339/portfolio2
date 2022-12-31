# 1. 주어진 조건대로 알맞게 입력받을 수 있는가.
# 2. 리스트 인덱싱.
# 3. 반복문의 활용.
# 4. 시간 복잡도를 줄이기 위한 알고리즘 기법 : 구간합
# 빅오 표기법 : 반복하는 횟수를 대략적으로 표현 > O(n^2)

# input() : 터미널 입력한 값을 문자열로 저장해주는 함수.
# 입력한 문자열을 잘라서, 원하는 자료형으로 맵핑.
N, M = map(int, input().split())

list_N = list(map(int, input().split()))

for _ in range(M):
    x, y = map(int, input().split())

    sum_number = 0
    
    for i in range(x, y):
        sum_number += list_N[i]

    print(sum_number)