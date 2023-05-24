import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [10001] * 10001
array = []
dp[0] = 0

for _ in range(n):
    array.append(int(input()))
array.sort()

for i in range(n):
    prev = array[i]
    for j in range(array[i], k + 1):
        temp = dp[j - prev]
        if temp != 10001: # 해당 방법이 없다는 거니까 거기에 더하기도 못해
            dp[j] = min(dp[j], temp + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])