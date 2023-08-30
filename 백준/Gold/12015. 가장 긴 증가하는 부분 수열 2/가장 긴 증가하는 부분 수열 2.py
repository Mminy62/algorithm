import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = []

for i in range(n):
    k = bisect_left(dp, array[i])
    if len(dp) <= k:# dp 에 없는 숫자는 len()값보다 크거나 같게 나온다. 
        dp.append(array[i])
    else:#이미 있거나 안에 있는 수보다 조금 더 큰 숫자는 그냥 대체로 한다. 
        dp[k] = array[i]

print(len(dp))