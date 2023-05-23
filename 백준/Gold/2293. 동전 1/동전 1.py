import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * 10001
array = []
dp[0] = 1
for _ in range(n):
    array.append(int(input()))
array.sort()

for i in range(n):
    prev = array[i]
    for j in range(array[i], k + 1):
        dp[j] += dp[j-prev]


print(dp[k])