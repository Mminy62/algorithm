import sys
input = sys.stdin.readline

c, n = map(int, input().split())
info = []
for _ in range(n):
    info.append(tuple(map(int, input().split())))

dp = [0] * 100001

for i in range(n):
    pay, people = info[i]
    for k in range(1, 100001):
        if k - pay >= 0:
            dp[k] = max(dp[k], dp[k-pay] + people)


for i in range(100001):
    if dp[i] >= c:
        print(i)
        break