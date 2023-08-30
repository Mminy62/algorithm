import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
# O(nlongn)으로 dp를 만들어주고 가장 큰 index를 기준으로 다시 O(n) 으로 수열찾기

tmp = []
dp = [1] * n
for i in range(n):
    k = bisect_left(tmp, array[i])
    if len(tmp) <= k:
        tmp.append(array[i])
        dp[i] = len(tmp)
    else:
        tmp[k] = array[i]
        dp[i] = dp[i] + k

idx = dp.index(max(dp))
stack = [array[idx]]
cur = idx
for i in range(idx-1, -1, -1):
    if array[i] < array[cur] and dp[i] + 1 == dp[cur]:
        stack.append(array[i])
        cur = i

print(max(dp))
print(' '.join(map(str, stack[::-1])))