
# 5 21
# 5 6 7 8 9

n, m = map(int, input().split())

list_blackjack = list(map(int, input().split()))



result = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if list_blackjack[i] + list_blackjack[j] + list_blackjack[k] > m:
                continue #무시하고 다음반복문 계속
            else:
                result = max(result, list_blackjack[i] + list_blackjack[j] + list_blackjack[k])

print(result)    